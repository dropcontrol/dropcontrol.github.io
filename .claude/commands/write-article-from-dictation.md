# Write Article from Dictation

Create a bilingual blog post from user's dictation. The user dictates content verbally, and this skill converts it into a published blog post.

## Arguments

- `$ARGUMENTS` — (Optional) Article slug or topic hint (e.g., `ai-and-music`)

## Critical Rules

- **NEVER add, embellish, or fabricate ANY content** that the user did not dictate
- **NEVER add transitional sentences, topic sentences, or decorative phrases**
- Preserve the user's voice, tone, and speaking style
- If something is unclear, ASK the user — do not guess or fill in

## Workflow

### Phase 1: Dictation Capture

1. Tell the user: "口述をどうぞ。話し終わったら教えてください。"
2. Capture everything the user says as raw text
3. Save raw dictation to `docs/draft/dictation-notes.md`:
   - Include structured summary (key topics, proper nouns, facts mentioned)
   - Include full raw dictation text verbatim
4. Confirm with the user that the dictation capture is complete

### Phase 2: Draft Composition

1. Compose the article **strictly from dictation content only**:
   - Maintain the user's conversational tone (do NOT formalize)
   - Remove verbal fillers and repetitions
   - Organize into natural paragraph breaks
   - Do NOT add section headings (this is an essay, not a structured article)
   - Do NOT add transitional sentences between paragraphs
2. Save draft to `docs/draft/article-draft-v1.md`
3. Show the user the draft and get approval before proceeding

### Phase 3: Jekyll Post Creation

1. Generate the post file:
   - Filename: `_posts/YYYY-MM-DD-slug.markdown`
   - Use today's date
   - Generate slug from content topic (ASCII, lowercase, hyphens)
   - **Set time to `00:00:00 +0900`** (not noon — avoids `future: false` hiding the post)
2. Front matter (bilingual-ready, but start with Japanese only):
   ```yaml
   ---
   layout: post
   title: "タイトル（後でユーザーが決める）"
   date: YYYY-MM-DD 00:00:00 +0900
   categories: blog
   ---
   ```
3. Ask the user if they want to set the title now or later

### Phase 4: Proper Noun Verification

1. Extract all proper nouns, product names, person names, and URLs from the article
2. For each proper noun:
   - Verify correct spelling via web search
   - Verify URLs are valid (especially GitHub repos)
   - Check official names (e.g., band names, book titles, company names)
3. Report findings to the user:
   - List each proper noun with verified spelling
   - Flag any URLs that don't resolve
   - Suggest corrections where needed
4. Apply corrections after user approval

### Phase 5: Bilingual Support

1. Add bilingual front matter:
   ```yaml
   title_en: "English Title"
   bilingual: true
   original_lang: ja
   ```
2. Wrap Japanese content in `<div lang="ja" markdown="1">...</div>`
3. Translate the article to English:
   - Translate faithfully — no additions or embellishments
   - Maintain the author's casual, conversational tone
   - Keep all proper nouns, URLs, and markdown links exactly as-is
   - Cultural references: translate naturally, don't over-explain
4. Add English translation in `<div lang="en" markdown="1">...</div>`

### Phase 6: Local Verification

1. Check if `docs/` is in `_config.yml` exclude list:
   - If not, add `docs/` to the `exclude:` list
   - Note: `_config.yml` changes require server restart
2. Start local Jekyll server: `bundle exec jekyll serve` (with `dangerouslyDisableSandbox: true`)
3. Verify:
   - Article appears on the top page (http://127.0.0.1:4000/)
   - Article page renders correctly
   - Language toggle works (if bilingual support is active on the site)
4. If article doesn't appear on top page:
   - Check if `future: false` is hiding it (post time must be in the past)
   - Check if draft files are polluting the menu
5. Report the local URL to the user for manual review

## Notes

- The dictation notes in `docs/draft/` serve as the **source of truth** for fact-checking
- If any content in the article cannot be traced back to the dictation, it must be removed
- The user may make manual edits between phases — always re-read the file before making changes
