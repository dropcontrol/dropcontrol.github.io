# Bilingual Support Plan: hiroshiyamato.com

## Context

X (Twitter) の Articles 機能で記事を書いているが、自分のサイト (hiroshiyamato.com) にソースを置いてリンクを共有する運用に切り替えたい。その際、英語圏の読者がブラウザ言語に応じて英語で記事を読めるようにしたい。

**要件**:
- 同じURLで日英切替（URL名前空間を分けない）
- DeepL API Free（月50万文字）で自動翻訳
- `navigator.language` によるブラウザ言語検出 + 手動切替ボタン
- 日本語で書いて英語は自動翻訳、既存の全記事にも適用

**方針**: Python スクリプトで DeepL API を呼び、翻訳済みコンテンツを `<div lang="ja/en">` で同一ファイルに埋め込む。クライアントサイド JS で表示切替。GitHub Pages 標準ビルドのまま動作（カスタムプラグイン不要）。最終的に GitHub Actions で push 時の自動翻訳まで実装する。

**翻訳品質対策**:
- DeepL API の `tag_handling: 'html'` + `ignore_tags` でHTML タグ内コンテンツを保護
- **コードブロック保護**: 翻訳前に Markdown のコードブロック（` ``` `, インラインコード）をプレースホルダーに置換 → 翻訳後に復元。コードは一切翻訳されない
- DeepL Glossary（用語集）API で固有名詞・技術用語を登録（LaTeX, kramdown, PerformanceRNN, IAMAS 等）
- スクリプト実行後に必ず手動レビュー → 問題があれば修正してからコミット
- `original_lang` を front matter に記録し、翻訳元が明確にわかるようにする

**ブランチ戦略（2段階）**:
1. `feature/bilingual-support`: Phase 1〜4（バイリンガル基本機能 + 全記事翻訳）→ テスト → master へ PR マージ
2. `feature/auto-translate-action`: Phase 5（GitHub Actions 自動翻訳）→ テスト → master へ PR マージ

---

## Phase 1: 環境準備 + 1記事で動作確認

### 1-1. DeepL API キーの取得
- https://www.deepl.com/ja/pro-api にアクセス
- Free プランでサインアップ（または既存アカウントでログイン）
- API キーを取得し、環境変数に設定: `export DEEPL_API_KEY=xxx`
- `.gitignore` に `.env` を追加

### 1-2. minima テーマのレイアウトをオーバーライド

新規作成するファイル:

| ファイル | 目的 |
|---------|------|
| `_layouts/default.html` | minima の default を継承し、JS 読み込みを追加 |
| `_layouts/post.html` | 言語切替ボタンを追加 |
| `_layouts/page.html` | 同上（静的ページ用） |
| `_includes/head.html` | 切替ボタンの CSS を追加 |
| `assets/js/lang-toggle.js` | 言語検出 + 切替ロジック |

**`lang-toggle.js` の動作**:
1. `localStorage` から言語設定を取得（なければ `navigator.language` で判定）
2. `<div lang="ja">` / `<div lang="en">` の表示/非表示を切替
3. 切替ボタンクリックで反転、`localStorage` に保存
4. `<html>` の `lang` 属性も動的に更新

**レイアウトの変更点**:
- front matter に `bilingual: true` がある場合のみ切替ボタンを表示
- ボタンテキスト: 日本語表示中は "Read in English" / 英語表示中は "日本語で読む"

### 1-3. テスト記事を手動変換

対象: `_posts/2017-09-06-update-my-profile.markdown`（最短の記事）

変換前:
```markdown
---
layout: post
title: "プロフィールを更新しました"
date: "2017-09-06 09:02:25 +0900"
categories: information
---
本文（日本語）...
```

変換後:
```markdown
---
layout: post
title: "プロフィールを更新しました"
title_en: "Profile has been updated"
date: "2017-09-06 09:02:25 +0900"
categories: information
bilingual: true
original_lang: ja
---

<div lang="ja" markdown="1">

本文（日本語）...

</div>

<div lang="en" markdown="1">

English translation...

</div>
```

**ポイント**: kramdown の `markdown="1"` 属性で div 内の Markdown が正しくレンダリングされる（GitHub Pages 標準対応）。

### 1-4. ローカルテスト

```bash
bundle exec jekyll serve
```

確認項目:
- ブラウザ言語に応じた自動切替
- ボタンによる手動切替
- `localStorage` での設定記憶（ページ遷移後も維持）
- div 内の Markdown レンダリング（リンク、見出し等）

---

## Phase 2: 翻訳スクリプト作成 + 全記事適用

### 2-1. Python 翻訳スクリプト

新規作成: `scripts/translate.py` + `scripts/requirements.txt`

機能:
- `_posts/` 内の Markdown ファイルをスキャン
- 既に `bilingual: true` なファイルはスキップ
- 日本語/英語を Unicode 範囲で自動判定
- **コードブロック保護**: ` ``` ` ブロックとインラインコード `` ` `` をプレースホルダーに置換してから翻訳、翻訳後に復元
- DeepL API Free (`https://api-free.deepl.com/v2/translate`) で翻訳（`tag_handling: 'html'`）
- `<div lang="xx" markdown="1">` で元文と翻訳を包んで保存
- front matter に `bilingual: true`, `original_lang: ja/en`, `title_en/title_ja` を追加
- `--dry-run` フラグで API 呼び出しなしのプレビュー
- 単一ファイル指定可能: `python scripts/translate.py _posts/specific-file.markdown`

```
scripts/requirements.txt:
  requests
  pyyaml
```

### 2-2. 記事の分類と対応

| 分類 | 記事数 | 対応 |
|------|--------|------|
| 日本語のみ | 10 | スクリプトで英語翻訳を追加 |
| 英語のみ | 3 | スクリプトで日本語翻訳を追加 |
| 既にバイリンガル（インライン混在） | 2 | 手動で `<div lang>` を追加（翻訳不要） |
| バイリンガルペア（別ファイル） | 2 (ja/en) | 1ファイルに統合 + リダイレクト設定 |

**推定文字数**: 既存全記事で約 30,000〜40,000 文字 → 月50万文字の上限内

### 2-3. liner notes ペアの統合

`give-way-liner-notes-ja.markdown` + `give-way-liner-notes-en.markdown` → 1ファイルに統合

`jekyll-redirect-from`（github-pages gem に含まれる）で旧URLからリダイレクト:
```yaml
redirect_from:
  - /2018/09/28/give-way-liner-notes-ja.html
  - /2018/09/28/give-way-liner-notes-en.html
```

---

## Phase 3: 静的ページ + ホームページ対応

### 3-1. profile.md / works.md の構造化

現状は英語→日本語の順で混在。`<div lang="xx" markdown="1">` で分離:
- 英語セクションを `<div lang="en">` に
- 日本語セクションを `<div lang="ja">` に
- front matter に `bilingual: true` を追加

### 3-2. ホームページの記事一覧

`_layouts/home.html` をオーバーライドして、記事タイトルも言語切替対応:
- `title_en` / `title_ja` が front matter にあれば両方レンダリング
- JS が `lang` 属性で表示/非表示を制御

---

## Phase 4: _config.yml 更新 + 仕上げ

- `_config.yml` に `lang: ja` を追加（デフォルトサイト言語）
- `.gitignore` に `.env`, `scripts/__pycache__/` を追加
- Dependabot セキュリティアラート（Ruby gem）も合わせて確認・対応

---

## Phase 5: GitHub Actions で自動翻訳

### 5-1. 翻訳ワークフロー

新規作成: `.github/workflows/translate.yml`

動作:
1. `master` ブランチへの push 時に `_posts/` または `*.md` の変更を検出
2. Python + DeepL API で未翻訳記事を自動翻訳
3. 翻訳結果をコミット & プッシュ（bot コミット）
4. GitHub Pages が自動ビルド

```yaml
on:
  push:
    branches: [master]
    paths: ['_posts/**', '*.md']
```

### 5-2. Secrets 設定

GitHub リポジトリの Settings > Secrets > Actions に `DEEPL_API_KEY` を登録

### 5-3. デプロイ方式

現在の GitHub Pages 標準ビルド（master ブランチ）をそのまま維持。
翻訳 Action はコンテンツをコミットするだけで、ビルド・デプロイには関与しない。

---

## 新記事ワークフロー（運用後）

### ローカルで確認してから push する場合:
```
1. 日本語で記事を書く (_posts/YYYY-MM-DD-slug.markdown)
2. 翻訳スクリプト実行:
   DEEPL_API_KEY=xxx python scripts/translate.py _posts/YYYY-MM-DD-slug.markdown
3. 翻訳結果を確認・必要に応じて手修正
4. git commit & push
5. GitHub Pages が自動ビルド → hiroshiyamato.com に反映
6. X にリンクを共有
```

### GitHub Actions に任せる場合:
```
1. 日本語で記事を書く (_posts/YYYY-MM-DD-slug.markdown)
2. git commit & push（日本語のみの状態で push）
3. GitHub Actions が自動で DeepL 翻訳を実行 → 翻訳コミットが自動追加
4. GitHub Pages が自動ビルド → hiroshiyamato.com に反映
5. X にリンクを共有
```
注意: Actions 経由の場合、翻訳品質の手動レビューは push 後になる

---

## 作業ファイル一覧

**新規作成**:
- `_layouts/default.html` — minima オーバーライド + JS 読み込み
- `_layouts/post.html` — 切替ボタン付き投稿レイアウト
- `_layouts/page.html` — 切替ボタン付きページレイアウト
- `_layouts/home.html` — バイリンガルタイトル対応の記事一覧
- `_includes/head.html` — CSS 追加
- `assets/js/lang-toggle.js` — 言語検出・切替 JS
- `scripts/translate.py` — DeepL 翻訳スクリプト
- `scripts/requirements.txt` — Python 依存パッケージ
- `.github/workflows/translate.yml` — GitHub Actions 自動翻訳ワークフロー

**変更**:
- `_config.yml` — `lang: ja` 追加
- `.gitignore` — `.env`, `scripts/__pycache__/` 追加
- `_posts/*.markdown` — 全17記事に `<div lang>` ラッパー追加
- `profile.md` — バイリンガル構造化
- `works.md` — バイリンガル構造化

---

## 検証方法

1. `bundle exec jekyll serve` でローカル確認
2. ブラウザの言語設定を変更して自動切替を検証
3. 切替ボタンの動作確認（クリック + ページ遷移後の保持）
4. `markdown="1"` のレンダリング確認（リンク、コードブロック、iframe 等）
5. 本番デプロイ後に hiroshiyamato.com で最終確認
