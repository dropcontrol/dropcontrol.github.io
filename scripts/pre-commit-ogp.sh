#!/usr/bin/env bash
# pre-commit hook: _posts/ 内の変更を検知してOGP画像を自動生成する
#
# インストール方法:
#   ln -sf ../../scripts/pre-commit-ogp.sh .git/hooks/pre-commit
#
# 既存のpre-commit hookがある場合は、そのスクリプト内からこのファイルを呼び出す:
#   bash scripts/pre-commit-ogp.sh

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
SCRIPT_DIR="${REPO_ROOT}/scripts"
POSTS_DIR="${REPO_ROOT}/_posts"
OGP_DIR="${REPO_ROOT}/images/ogp"

# Pillow が利用可能かチェック（なければスキップ）
if ! python3 -c "from PIL import Image" 2>/dev/null; then
    echo "OGP: Warning: Pillow not installed, skipping OGP generation"
    echo "OGP: Install with: pip3 install Pillow"
    exit 0
fi

# ステージされた _posts/ 内のファイルを検出（新規・変更）
STAGED_POSTS=$(git diff --cached --name-only --diff-filter=ACM -- '_posts/*.markdown' '_posts/*.md' 2>/dev/null || true)

if [ -z "$STAGED_POSTS" ]; then
    exit 0
fi

echo "OGP: Checking staged posts for OGP image generation..."

GENERATED=0
while IFS= read -r post; do
    [ -z "$post" ] && continue
    post_path="${REPO_ROOT}/${post}"
    basename=$(basename "$post")
    slug="${basename%.*}"
    ogp_path="${OGP_DIR}/${slug}.png"

    # 既にOGP画像が存在する場合はスキップ
    if [ -f "$ogp_path" ]; then
        echo "OGP: Skipped (exists): ${slug}.png"
        continue
    fi

    echo "OGP: Generating ${slug}.png..."
    python3 "${SCRIPT_DIR}/generate_ogp.py" --post "$post_path"

    if [ -f "$ogp_path" ]; then
        git add "$ogp_path"
        # front matterが更新されていたら記事も再ステージ
        git add "$post_path"
        GENERATED=$((GENERATED + 1))
    fi
done <<< "$STAGED_POSTS"

if [ $GENERATED -gt 0 ]; then
    echo "OGP: Generated ${GENERATED} new OGP image(s)"
fi
