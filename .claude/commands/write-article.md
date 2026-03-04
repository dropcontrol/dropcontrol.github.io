# Write Article from GitHub Issue

Create a bilingual blog post from a GitHub Issue in this repository.

## Arguments

- `$ARGUMENTS` — GitHub Issue number (e.g., `5`)

## Instructions

1. **Fetch the Issue** using `gh issue view $ARGUMENTS --json title,body,labels,createdAt`

2. **Parse the Issue content**:
   - Title becomes the post title
   - Body becomes the article content
   - Labels can suggest categories (optional)

3. **Detect the language** of the Issue body:
   - If it contains significant Japanese text → `original_lang: ja`
   - Otherwise → `original_lang: en`

4. **Create the post file**:
   - Filename: `_posts/YYYY-MM-DD-slug.markdown` (use today's date, generate slug from English title)
   - Slug should be lowercase, hyphens instead of spaces, ASCII only

5. **Write the article** based on the Issue content:
   - Use the Issue body as the main content
   - Clean up formatting if needed (Issues may have task lists, mentions, etc.)
   - Preserve the author's voice and tone

6. **Apply bilingual format** (same as /translate-post):
   - Translate to the other language
   - Wrap in `<div lang="ja" markdown="1">` and `<div lang="en" markdown="1">`
   - Add front matter: `bilingual: true`, `original_lang`, `title_en`/`title_ja`
   - Preserve all URLs, code blocks, embeds, and technical terms

7. **Close the Issue** with a comment linking to the created file:
   ```
   gh issue close $ARGUMENTS --comment "Article created: _posts/YYYY-MM-DD-slug.markdown"
   ```

8. **Report** what was done: file path, detected language, title in both languages.

## Workflow Context

This skill is designed for a workflow where:
- Other projects or Claude instances create Issues as article drafts
- This skill converts those Issues into published bilingual blog posts
- The Issue serves as the "draft" and the blog post is the "published" version
