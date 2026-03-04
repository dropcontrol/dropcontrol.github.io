# Import X (Twitter) Article as Blog Post

Fetch an article from X (Twitter) Articles and create a bilingual blog post.

## Arguments

- `$ARGUMENTS` — URL of the X article (e.g., `https://x.com/username/articles/...`)

## Instructions

1. **Fetch the article content** from the provided URL using WebFetch tool.
   - Extract the article title, body text, and any embedded media references
   - If WebFetch fails, ask the user to paste the article content directly

2. **Detect the language** of the article:
   - If it contains significant Japanese text → `original_lang: ja`
   - Otherwise → `original_lang: en`

3. **Create the post file**:
   - Filename: `_posts/YYYY-MM-DD-slug.markdown` (use today's date, generate slug from English title)
   - Slug should be lowercase, hyphens instead of spaces, ASCII only

4. **Adapt the content for blog format**:
   - Convert the X article content to Markdown
   - Preserve the author's voice and tone
   - Keep any relevant links and references
   - Add the original X article URL as a reference link at the end

5. **Apply bilingual format** (same as /translate-post):
   - Translate to the other language
   - Wrap in `<div lang="ja" markdown="1">` and `<div lang="en" markdown="1">`
   - Add front matter: `bilingual: true`, `original_lang`, `title_en`/`title_ja`
   - Preserve all URLs, code blocks, embeds, and technical terms

6. **Report** what was done: file path, detected language, title in both languages, and the source X article URL.

## Notes

- The original X article URL should be included in the blog post for reference
- X Articles content may need reformatting for blog readability
- Images from X may not be directly embeddable; note any media that needs manual handling
