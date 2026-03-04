# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal website / blog for HIROSHI YAMATO (dropcontrol) hosted on GitHub Pages at hiroshiyamato.com. Built with Jekyll 3.10.0 using the `github-pages` gem and `minima` theme.

## Development Commands

```bash
# Install dependencies
bundle install

# Local development server (auto-rebuilds on changes, but NOT for _config.yml edits)
bundle exec jekyll serve

# Build site without serving
bundle exec jekyll build
```

The generated site outputs to `_site/` (gitignored).

## Architecture

- **Static site generator**: Jekyll via `github-pages` gem (pins Jekyll 3.10.0 and all plugins)
- **Theme**: minima 2.5.1 (gem-based; override layouts by creating matching files locally)
- **Markdown engine**: kramdown with GFM support
- **Deployment**: Automatic via GitHub Pages on push to `master`

## Content Structure

- `_posts/` — Blog posts in Markdown (YYYY-MM-DD-slug.markdown format). Content is bilingual (English/Japanese)
- `profile.md` — Bio page (permalink: `/profile/`)
- `works.md` — Works page (permalink: `/works/`)
- `index.md` — Home page using the `home` layout from minima
- `images/`, `pdf/` — Static assets

## Key Configuration (_config.yml)

- `timezone: Asia/Tokyo`
- `future: false` — Posts with future dates are not published
- Custom domain configured via `CNAME` file (hiroshiyamato.com)

## Blog Post Format

Posts use Jekyll front matter and are named `YYYY-MM-DD-title-slug.markdown`:

```markdown
---
layout: post
title: "Post Title"
date: YYYY-MM-DD HH:MM:SS +0900
categories: category-name
---
```

## Ruby Environment

- Ruby version: 2.5.3 (specified in `.ruby-version`)
- Bundler 2.7.2
- Dependencies managed through `github-pages` gem which pins compatible versions

## Git Workflow

- Single branch: `master` (deploys directly to GitHub Pages)
- No CI/CD pipeline beyond GitHub Pages auto-build
