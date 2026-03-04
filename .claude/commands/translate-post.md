# Translate Post to Bilingual Format

Translate a blog post into bilingual format for hiroshiyamato.com.

## Arguments

- `$ARGUMENTS` — Path to the target markdown file (e.g., `_posts/2026-02-24-my-new-post.markdown`)

## Instructions

1. **Read the target file** at `$ARGUMENTS`

2. **Check if already bilingual**: If the front matter contains `bilingual: true`, report that it's already converted and stop.

3. **Detect the original language**:
   - If the content contains significant Japanese text (hiragana, katakana, kanji), it's `ja`
   - Otherwise, it's `en`

4. **Translate the content**:
   - If original is `ja`: Translate the body to English
   - If original is `en`: Translate the body to Japanese
   - Preserve all HTML tags, URLs, links, image references, iframe embeds, and code blocks exactly as-is
   - Preserve the conversational tone and personal voice of the author
   - Keep all technical terms, proper nouns, and project names untranslated

5. **Restructure the file** into bilingual format:

   ```markdown
   ---
   layout: post
   title: "Original Title"
   title_en: "English Title"   # if original is ja
   title_ja: "Japanese Title"  # if original is en
   date: "original date"
   categories: original-categories  # if present
   bilingual: true
   original_lang: ja  # or en
   ---

   <div lang="ja" markdown="1">

   Japanese content here...

   </div>

   <div lang="en" markdown="1">

   English content here...

   </div>
   ```

6. **Important rules**:
   - The `markdown="1"` attribute on each div is required for kramdown to render Markdown inside HTML
   - Leave a blank line after `<div lang="xx" markdown="1">` and before `</div>`
   - Do not translate content inside code blocks (``` ``` ```) or inline code (`` ` ``)
   - Do not translate URLs or file paths
   - Preserve YouTube iframe embeds exactly as-is in both languages

7. **Write the modified file** back to the same path.

8. **Report** what was done: original language detected, title translation, and file path.
