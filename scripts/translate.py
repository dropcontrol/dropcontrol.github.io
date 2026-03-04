#!/usr/bin/env python3
"""
Translate Jekyll posts using DeepL API Free.

Usage:
  python scripts/translate.py                                    # Translate all untranslated posts
  python scripts/translate.py _posts/2017-09-05-example.markdown # Translate a specific file
  python scripts/translate.py --dry-run                           # Preview without API calls
"""

import argparse
import glob
import os
import re
import sys
import tempfile
import shutil
import unicodedata

import requests
import yaml


DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"
FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
CODE_BLOCK_RE = re.compile(r"(```[\s\S]*?```)", re.MULTILINE)
INLINE_CODE_RE = re.compile(r"(`[^`\n]+`)")


def get_api_key():
    key = os.environ.get("DEEPL_API_KEY", "")
    if not key:
        print("Error: DEEPL_API_KEY environment variable is not set.")
        sys.exit(1)
    return key


def detect_language(text):
    """Detect if text is primarily Japanese or English using Unicode character counts.

    Returns 'en' when counts are equal or when no letter characters are found.
    Non-CJK, non-Latin scripts (e.g., Korean, Arabic) count as neither and resolve to 'en'.
    """
    ja_count = 0
    en_count = 0
    for char in text:
        cat = unicodedata.category(char)
        if cat.startswith("L"):
            cp = ord(char)
            # Hiragana, Katakana, CJK Unified Ideographs, CJK Extension A
            if (0x3040 <= cp <= 0x309F or
                0x30A0 <= cp <= 0x30FF or
                0x4E00 <= cp <= 0x9FFF or
                0x3400 <= cp <= 0x4DBF):
                ja_count += 1
            elif cp < 0x0100:
                en_count += 1

    total = ja_count + en_count
    if total == 0:
        raise ValueError(
            "Could not detect language: no letter characters found in post body."
        )
    if total < 20:
        print(f"    Warning: language detection confidence is low ({total} letter chars found).")

    return "ja" if ja_count > en_count else "en"


def protect_code_blocks(text):
    """Replace code blocks and inline code with placeholders."""
    placeholders = {}
    counter = [0]

    def replace_block(match):
        key = f"__CODE_BLOCK_{counter[0]}__"
        placeholders[key] = match.group(0)
        counter[0] += 1
        return key

    text = CODE_BLOCK_RE.sub(replace_block, text)
    text = INLINE_CODE_RE.sub(replace_block, text)
    return text, placeholders


def restore_code_blocks(text, placeholders):
    """Restore placeholders back to original code blocks."""
    for key, value in placeholders.items():
        text = text.replace(key, value)
    return text


def translate_text(text, source_lang, target_lang, api_key):
    """Translate text using DeepL API Free. Raises RuntimeError on failure."""
    # Protect code blocks
    protected_text, placeholders = protect_code_blocks(text)

    headers = {"Authorization": f"DeepL-Auth-Key {api_key}"}
    data = {
        "text": protected_text,
        "source_lang": source_lang.upper(),
        "target_lang": target_lang.upper(),
    }

    # DeepL requires a regional variant for English target; default to EN-US
    if target_lang.upper() == "EN":
        data["target_lang"] = "EN-US"

    try:
        response = requests.post(DEEPL_API_URL, headers=headers, data=data, timeout=(10, 60))
        response.raise_for_status()
        result = response.json()
    except requests.exceptions.Timeout:
        raise RuntimeError("DeepL API request timed out")
    except requests.exceptions.ConnectionError as e:
        raise RuntimeError(f"Failed to connect to DeepL API: {e}")
    except requests.exceptions.HTTPError:
        raise RuntimeError(f"DeepL API returned error {response.status_code}: {response.text}")
    except ValueError as e:
        raise RuntimeError(f"DeepL API returned non-JSON response: {e}")

    translations = result.get("translations")
    if not translations:
        raise RuntimeError(f"DeepL API returned no translations. Response: {result}")

    translated = translations[0]["text"]

    # Restore code blocks
    translated = restore_code_blocks(translated, placeholders)
    return translated


def parse_front_matter(content):
    """Parse front matter and body from a Jekyll post."""
    match = FRONT_MATTER_RE.match(content)
    if not match:
        return None, content
    fm_text = match.group(1)
    body = content[match.end():]
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        raise ValueError(f"Malformed YAML front matter: {e}") from e
    if not isinstance(fm, dict):
        return None, content
    return fm, body


def build_front_matter(fm):
    """Rebuild front matter YAML string using a canonical key order.

    Unknown keys are appended after the ordered set.
    """
    key_order = [
        "layout", "title", "title_en", "title_ja",
        "date", "categories", "bilingual", "original_lang",
        "redirect_from",
    ]
    lines = ["---"]
    written = set()
    for key in key_order:
        if key in fm:
            lines.append(yaml.dump({key: fm[key]}, allow_unicode=True, default_flow_style=False).strip())
            written.add(key)
    for key, value in fm.items():
        if key not in written:
            lines.append(yaml.dump({key: value}, allow_unicode=True, default_flow_style=False).strip())
    lines.append("---")
    return "\n".join(lines) + "\n"


def process_file(filepath, dry_run=False, api_key=None):
    """Translate a Jekyll post file in place using the DeepL API.

    The file is overwritten with bilingual content. Skips files already marked bilingual: true.
    Returns True if the file was processed, False if skipped.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    try:
        fm, body = parse_front_matter(content)
    except ValueError as e:
        print(f"  Skipping {filepath}: {e}")
        return False

    if fm is None:
        print(f"  Skipping {filepath}: no front matter found")
        return False

    if fm.get("bilingual"):
        print(f"  Skipping {filepath}: already bilingual")
        return False

    # Detect original language
    try:
        orig_lang = detect_language(body)
    except ValueError as e:
        print(f"  Skipping {filepath}: {e}")
        return False

    target_lang = "en" if orig_lang == "ja" else "ja"

    print(f"  {filepath}")
    print(f"    Detected: {orig_lang} -> translating to {target_lang}")

    title = fm.get("title", "")

    if dry_run:
        print(f"    [DRY RUN] Would translate title: {title}")
        print(f"    [DRY RUN] Would translate body ({len(body)} chars)")
        return True

    # Translate title and body
    translated_title = translate_text(title, orig_lang, target_lang, api_key)
    print(f"    Translated title: {translated_title}")

    translated_body = translate_text(body.strip(), orig_lang, target_lang, api_key)
    print(f"    Translated body ({len(translated_body)} chars)")

    # Update front matter
    fm["bilingual"] = True
    fm["original_lang"] = orig_lang
    if orig_lang == "ja":
        fm["title_en"] = translated_title
    else:
        fm["title_ja"] = translated_title

    # Build new content
    new_fm = build_front_matter(fm)

    if orig_lang == "ja":
        new_body = f"""
<div lang="ja" markdown="1">

{body.strip()}

</div>

<div lang="en" markdown="1">

{translated_body}

</div>
"""
    else:
        new_body = f"""
<div lang="ja" markdown="1">

{translated_body}

</div>

<div lang="en" markdown="1">

{body.strip()}

</div>
"""

    new_content = new_fm + new_body

    # Atomic write: write to temp file then rename
    dir_name = os.path.dirname(os.path.abspath(filepath))
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=dir_name, delete=False, suffix=".tmp"
        ) as tmp:
            tmp.write(new_content)
            tmp_path = tmp.name
        shutil.move(tmp_path, filepath)
    except OSError as e:
        if tmp_path and os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise RuntimeError(f"Failed to write {filepath}: {e}")

    print(f"    Saved: {filepath}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Translate Jekyll posts with DeepL API")
    parser.add_argument("files", nargs="*", help="Specific files to translate (default: all in _posts/)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without API calls")
    args = parser.parse_args()

    api_key = None if args.dry_run else get_api_key()

    if args.files:
        files = args.files
    else:
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        posts_dir = os.path.join(repo_root, "_posts")
        files = sorted(
            glob.glob(os.path.join(posts_dir, "*.markdown"))
            + glob.glob(os.path.join(posts_dir, "*.md"))
        )

    if not files:
        print("No files found to process.")
        return

    print(f"Processing {len(files)} file(s)...\n")

    translated_count = 0
    failed_files = []
    for filepath in files:
        try:
            if process_file(filepath, dry_run=args.dry_run, api_key=api_key):
                translated_count += 1
        except Exception as e:
            print(f"  ERROR processing {filepath}: {e}")
            failed_files.append(filepath)
        print()

    print(f"Done. {translated_count} file(s) {'would be ' if args.dry_run else ''}translated.")
    if failed_files:
        print(f"\nFailed to process {len(failed_files)} file(s):")
        for f in failed_files:
            print(f"  - {f}")
        print("These files were not modified. Check the errors above and retry.")
        sys.exit(1)


if __name__ == "__main__":
    main()
