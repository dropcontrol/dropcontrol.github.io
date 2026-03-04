#!/usr/bin/env python3
"""OGP画像生成スクリプト — Bauhaus Style

ブログ記事のタイトルからバウハウス調のOGP画像(1200x630px)を自動生成する。
日本語・英語のバイリンガル対応。

Usage:
    # 単一タイトルから生成
    python scripts/generate_ogp.py "タイトル" -o images/ogp/output.png

    # 記事ファイルから生成
    python scripts/generate_ogp.py --post _posts/2026-03-05-example.markdown

    # 全記事を一括生成
    python scripts/generate_ogp.py --all

    # デフォルトOGP画像を生成
    python scripts/generate_ogp.py --default
"""

import argparse
import glob
import hashlib
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont

# --- Config ---
WIDTH = 1200
HEIGHT = 630

# Bauhaus color palette
BG_COLOR = "#F5F0E8"          # Warm off-white (Bauhaus paper tone)
TEXT_COLOR = "#1A1A1A"         # Near-black
ACCENT_RED = "#D42D2D"        # Bauhaus red
ACCENT_BLUE = "#1B4B8A"       # Bauhaus blue
ACCENT_YELLOW = "#F2B705"     # Bauhaus yellow
SUB_TEXT_COLOR = "#4A4A4A"    # Dark gray
RULE_COLOR = "#1A1A1A"        # Black rules

SITE_NAME = "HIROSHI YAMATO"

# Fonts — Hiragino Kaku Gothic (heaviest weights for Bauhaus boldness)
FONT_BOLD = "/System/Library/Fonts/ヒラギノ角ゴシック W8.ttc"
FONT_MEDIUM = "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc"
FONT_LIGHT = "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc"

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "images", "ogp")


def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except (OSError, IOError):
        print(f"Warning: Font not found at {path}, using default", file=sys.stderr)
        return ImageFont.load_default()


def title_hash(title):
    """タイトルから決定論的なハッシュ値を生成（デザインバリエーション用）。"""
    return int(hashlib.md5(title.encode()).hexdigest(), 16)


def wrap_text(text, font, max_width, draw):
    """テキストを指定幅で改行する。"""
    has_japanese = bool(re.search(r'[\u3040-\u9fff\uf900-\ufaff]', text))

    if has_japanese:
        lines = []
        current_line = ""
        for char in text:
            test_line = current_line + char
            bbox = draw.textbbox((0, 0), test_line, font=font)
            if bbox[2] > max_width and current_line:
                lines.append(current_line)
                current_line = char
            else:
                current_line = test_line
        if current_line:
            lines.append(current_line)
        return lines
    else:
        words = text.split()
        lines = []
        current_line = ""
        for word in words:
            test_line = f"{current_line} {word}".strip()
            bbox = draw.textbbox((0, 0), test_line, font=font)
            if bbox[2] > max_width and current_line:
                lines.append(current_line)
                current_line = word
            else:
                current_line = test_line
        if current_line:
            lines.append(current_line)
        return lines


def draw_shape(draw, shape_type, bbox, color):
    """幾何学図形を描画する。shape_type: 0=円, 1=四角, 2=三角"""
    x1, y1, x2, y2 = bbox
    if shape_type == 0:
        draw.ellipse([(x1, y1), (x2, y2)], fill=color)
    elif shape_type == 1:
        draw.rectangle([(x1, y1), (x2, y2)], fill=color)
    else:
        cx = (x1 + x2) // 2
        draw.polygon([(cx, y1), (x2, y2), (x1, y2)], fill=color)


def draw_bauhaus_geometry(draw, title):
    """タイトルに基づいてバウハウス風の幾何学装飾を描画する。

    タイトルのハッシュ値から決定論的にデザインが変わるため、
    同じタイトルなら同じデザイン、異なるタイトルなら異なるデザインになる。
    """
    h = title_hash(title)
    colors = [ACCENT_RED, ACCENT_BLUE, ACCENT_YELLOW]

    # メイン図形のパラメータ（右上エリア）
    primary_color = colors[h % 3]
    primary_shape = (h >> 4) % 3
    # 位置をハッシュで微調整（右上象限内で変動）
    offset_x = (h >> 7) % 120  # 0-119
    offset_y = (h >> 14) % 80   # 0-79
    size = 180 + (h >> 20) % 100  # 180-279

    primary_x = WIDTH - 100 - offset_x
    primary_y = -40 + offset_y
    draw_shape(draw, primary_shape,
               (primary_x - size // 2, primary_y - size // 2,
                primary_x + size // 2, primary_y + size // 2),
               primary_color)

    # サブ図形（左下コーナーに配置、テキストと重ならない位置）
    secondary_color = colors[(h >> 8) % 3]
    # 色が被らないようにする
    if secondary_color == primary_color:
        secondary_color = colors[((h >> 8) % 3 + 1) % 3]
    secondary_shape = (h >> 12) % 3
    offset_x2 = (h >> 16) % 40   # 0-39 (コーナー寄り)
    offset_y2 = (h >> 22) % 30   # 0-29 (コーナー寄り)
    size2 = 80 + (h >> 26) % 60  # 80-139 (少し小さめ)

    # 図形の中心を左下コーナーに固定（テキストの下に被らない）
    sub_x = -30 + offset_x2
    sub_y = HEIGHT + 10 - offset_y2
    draw_shape(draw, secondary_shape,
               (sub_x - size2 // 2, sub_y - size2 // 2,
                sub_x + size2 // 2, sub_y + size2 // 2),
               secondary_color)


def generate_ogp(title, output_path, title_en=None):
    """バウハウス調のOGP画像を生成する。"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # 幾何学装飾（タイトルハッシュで決定論的にバリエーション）
    draw_bauhaus_geometry(draw, title)

    # 太い水平ルール（上部）
    draw.rectangle([(0, 0), (WIDTH, 8)], fill=RULE_COLOR)

    # フォントサイズ — 日英同じサイズ・ウェイトで力強く
    title_font_size = 52
    title_font = load_font(FONT_BOLD, title_font_size)

    # レイアウト: 左寄せ、バウハウスの非対称グリッド
    margin_left = 80
    margin_right = 280  # 右側に幾何学図形の余白
    max_text_width = WIDTH - margin_left - margin_right

    line_height = int(title_font_size * 1.4)

    # 日本語タイトル
    ja_lines = wrap_text(title, title_font, max_text_width, draw)
    if len(ja_lines) > 2:
        ja_lines = ja_lines[:2]
        ja_lines[1] = ja_lines[1][:-1] + "…"

    # 英語タイトル（同じフォント・サイズ）
    en_lines = []
    if title_en:
        en_lines = wrap_text(title_en, title_font, max_text_width, draw)
        if len(en_lines) > 2:
            en_lines = en_lines[:2]
            en_lines[1] = en_lines[1][:-1] + "…"

    # 縦位置計算
    total_ja_h = len(ja_lines) * line_height
    total_en_h = len(en_lines) * line_height if en_lines else 0
    gap = 20 if en_lines else 0  # 日英間のスペース

    content_h = total_ja_h + gap + total_en_h
    start_y = (HEIGHT - content_h) // 2 - 20

    # 日本語タイトル描画
    y = start_y
    for line in ja_lines:
        draw.text((margin_left, y), line, font=title_font, fill=TEXT_COLOR)
        y += line_height

    # 英語タイトル描画（同じサイズ・ウェイト）
    if en_lines:
        y += gap
        for line in en_lines:
            draw.text((margin_left, y), line, font=title_font, fill=TEXT_COLOR)
            y += line_height

    # 太い水平ルール（下部区切り）
    rule_y = HEIGHT - 70
    draw.rectangle([(margin_left, rule_y), (WIDTH - margin_left, rule_y + 3)], fill=RULE_COLOR)

    # バイリンガルインジケータ（目立つ位置に）
    if title_en:
        lang_font = load_font(FONT_MEDIUM, 20)
        lang_text = "Read in English & Japanese"
        draw.text((margin_left, rule_y + 14), lang_text, font=lang_font, fill=SUB_TEXT_COLOR)
    else:
        # バイリンガルでない場合はサイトURL
        url_font = load_font(FONT_LIGHT, 16)
        draw.text((margin_left, rule_y + 14), "hiroshiyamato.com", font=url_font, fill=SUB_TEXT_COLOR)

    # 下端のルール
    draw.rectangle([(0, HEIGHT - 8), (WIDTH, HEIGHT)], fill=RULE_COLOR)

    # 保存
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    print(f"Generated: {output_path}")


def generate_default_ogp(output_path):
    """デフォルトOGP画像を生成する。"""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # バウハウスの三原色ブロック
    draw.rectangle([(0, 0), (WIDTH, 8)], fill=RULE_COLOR)
    draw.rectangle([(0, HEIGHT - 8), (WIDTH, HEIGHT)], fill=RULE_COLOR)

    # 三原色の大きな幾何学
    draw.ellipse([(WIDTH - 220, 40), (WIDTH + 40, 300)], fill=ACCENT_RED)
    draw.rectangle([(WIDTH - 300, HEIGHT - 250), (WIDTH - 120, HEIGHT - 70)], fill=ACCENT_BLUE)
    draw.polygon([(40, HEIGHT - 60), (160, HEIGHT - 220), (-80, HEIGHT - 220)], fill=ACCENT_YELLOW)

    title_font = load_font(FONT_BOLD, 64)
    sub_font = load_font(FONT_LIGHT, 22)

    # サイト名を左寄せ（バウハウスの非対称）
    margin_left = 80
    name_y = HEIGHT // 2 - 50
    draw.text((margin_left, name_y), SITE_NAME, font=title_font, fill=TEXT_COLOR)

    # URL
    url_text = "hiroshiyamato.com"
    draw.text((margin_left, name_y + 80), url_text, font=sub_font, fill=SUB_TEXT_COLOR)

    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    print(f"Generated default: {output_path}")


def decode_unicode_escapes(s):
    """\\uXXXX 形式のUnicodeエスケープをデコードする。"""
    def replace_match(m):
        return chr(int(m.group(1), 16))
    return re.sub(r'\\u([0-9A-Fa-f]{4})', replace_match, s)


def clean_title(s):
    """タイトル文字列をクリーンアップする。"""
    s = decode_unicode_escapes(s)
    s = s.replace('\\"', '"')  # エスケープされた引用符を戻す
    # 先頭・末尾の引用符を除去
    s = s.strip('"')
    return s


def parse_front_matter(filepath):
    """記事ファイルのfront matterを解析する。"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None

    fm = {}
    for line in match.group(1).split("\n"):
        m = re.match(r'^(\w+):\s*"?(.+?)"?\s*$', line)
        if m:
            key = m.group(1)
            value = m.group(2)
            if key in ("title", "title_en"):
                value = clean_title(value)
            fm[key] = value
    return fm


def slug_from_filename(filename):
    """ファイル名からスラッグを生成する。"""
    basename = os.path.basename(filename)
    name = re.sub(r'\.(markdown|md)$', '', basename)
    return name


def process_post(filepath):
    """記事ファイルからOGP画像を生成する。"""
    fm = parse_front_matter(filepath)
    if not fm or "title" not in fm:
        print(f"Skipped (no title): {filepath}", file=sys.stderr)
        return None

    slug = slug_from_filename(filepath)
    output_path = os.path.join(OUTPUT_DIR, f"{slug}.png")

    title = fm["title"]
    title_en = fm.get("title_en")

    generate_ogp(title, output_path, title_en=title_en)
    return output_path


def add_image_to_front_matter(filepath, image_path):
    """記事のfront matterにimage フィールドを追加する。"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if re.search(r'^image:', content, re.MULTILINE):
        return False

    rel_path = "/" + os.path.relpath(image_path, os.path.dirname(os.path.dirname(__file__)))
    new_content = content.replace("---\n\n", f"image: {rel_path}\n---\n\n", 1)

    if new_content == content:
        parts = content.split("---")
        if len(parts) >= 3:
            new_content = parts[0] + "---" + parts[1] + f"image: {rel_path}\n---" + "---".join(parts[2:])

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated front matter: {filepath}")
        return True
    return False


def process_all_posts():
    """全記事のOGP画像を一括生成する。"""
    posts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "_posts")
    posts = sorted(glob.glob(os.path.join(posts_dir, "*.markdown")))
    posts += sorted(glob.glob(os.path.join(posts_dir, "*.md")))

    count = 0
    for post in posts:
        slug = slug_from_filename(post)
        output_path = os.path.join(OUTPUT_DIR, f"{slug}.png")

        if os.path.exists(output_path):
            print(f"Skipped (exists): {output_path}")
            continue

        result = process_post(post)
        if result:
            add_image_to_front_matter(post, result)
            count += 1

    print(f"\nGenerated {count} OGP images")


def main():
    parser = argparse.ArgumentParser(description="Generate Bauhaus-style OGP images for blog posts")
    parser.add_argument("title", nargs="?", help="Title text for the OGP image")
    parser.add_argument("-o", "--output", help="Output file path")
    parser.add_argument("--title-en", help="English subtitle")
    parser.add_argument("--post", help="Generate from a post file")
    parser.add_argument("--all", action="store_true", help="Generate for all posts")
    parser.add_argument("--default", action="store_true", help="Generate default OGP image")

    args = parser.parse_args()

    if args.default:
        default_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "images", "ogp-default.png"
        )
        generate_default_ogp(default_path)
    elif args.all:
        process_all_posts()
    elif args.post:
        result = process_post(args.post)
        if result:
            add_image_to_front_matter(args.post, result)
    elif args.title:
        output = args.output or os.path.join(OUTPUT_DIR, "test.png")
        generate_ogp(args.title, output, title_en=args.title_en)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
