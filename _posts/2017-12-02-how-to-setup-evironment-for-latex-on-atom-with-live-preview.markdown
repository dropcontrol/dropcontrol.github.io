---
layout: post
title: "AtomでLatexのライブプレビュー環境を作る(OSX対象)"
title_en: "Setting Up a LaTeX Live Preview Environment in Atom (for macOS)"
date: "2017-12-02 08:44:52 +0900"
categories: blog
bilingual: true
original_lang: ja
image: /images/ogp/2017-12-02-how-to-setup-evironment-for-latex-on-atom-with-live-preview.png
---

<div lang="ja" markdown="1">
※ この記事は[IAMAS Advent Calendar 2017](https://qiita.com/advent-calendar/2017/iamas)の12月2日の記事です。

というわけで参加者が少なそうなので、一本ライトな記事を書くことにします。丁度現在IAMAS m2のみなさんは論文カキコモードに突入してる筈、なので「論文と言えばLatex!!」という時代錯誤な感じで今自分が丁度[iCSAF2017](http://ic.jssa.info)の併設の研究発表会である[第34回先端芸術音楽創作学会](http://jssa.info)での発表予稿を書くにあたっての執筆環境について書いておきます。Latexで論文書くやつあと一人くらいしか同期にはいそうにないけどな、、、。

## Latexって
簡単に言うと「難しい数式の記述をテキストで構造的に書くことができるマークアップ方式の記述方法」というやつで理科系論文に良く使われたりします。hrr曰く「最近はワードで書いて出せる学会が多いけどね、LaTex指定とか今時珍しいね、、」と言う話だったりしますが。ちなみに、マークアップ形式なので何らかの形にコンパイルして処理しないと正確な文章は見れません。

## Setup
### 前提
* homebrewがインストールされていて環境が整っていること
* Atomがインストールされていること
* macOS Sierraをこの記事では対象にしてます(その他でも別に似たようなもんだけど)

です。homebrewのインストールとかAtomのインストールについては触れませんので各自ググり力を発揮してください。

### Atom環境へのPackageのインストール
AtomのPreferenceから下記のパッケージをインストールします。
* latex (AtomからLaTexのコンパイルをしてくれる)
* language-latex (Atom上でシンタックスハイライトをしてくれる)
* pdf-view (PDFをATOM上で表示してくれる)

### MacTexのインストール
homebrewのcaskをつかってインストールします(MacTexでパッケージも配布されている気がするのでそれでもいいかも。そのうち自分の環境をなるべくcaskで管理したいな、、と思いましたはい)。homebrewはOSXでのUNIXパッケージのパッケージマネージャです。caskはそれをOSXのアプリケーションを対象にしたもの、という理解で大体大丈夫。とりあえずhomebrewのインストールについては本家を見ていただくの良いのでココ > [https://brew.sh/index_ja.html](https://brew.sh/index_ja.html)

で、homebrewの環境が整ってる人は、まずcaskが利用できるようにします。

```console
brew tap caskroom/cask
```

brew tapは公式以外のレポジトリをHomebrewに追加して、brewコマンドででinstall, uninstall, updateなどが行うようにします。この場合caskroom/caskのレポジトリを追加。これでMacTexのインストールをbrewコマンドで行えるので以下を実行。あそうそう、パスワードが要求されることがありますが、そのあたりは表示を良く読んでヨシナに対応してください。

```console
brew cask install mactex
```

これでMacTexがインストールされるはずです。
その間にAtomの設定してしまいましょう。

### Atomの設定
Atomで先程インストールしたlatexパッケージを検索なりして「Setting」をクリックして設定を開きます。そこで以下の項目をチェック。

![latexパッケージの設定](https://i.gyazo.com/2ff0b89a21437113287dddd6376b71a0.png)

* Move Result to Source Directoryはチェック
* Build on Saveはチェック
* Atomだけでブレビューしたいのであと二つはチェックしない。もしAcrobatとかで確認したいとかならチェックいれる

です。

### 動作について
これで適当にLatexで記事を書いて、Saveすると自動的にPDFにコンパイルしてくれる環境になりました。その生成されたPDFを"Split in Right"とかでATOMの別タブに表示しておくとSaveされる毎にコンパイルが走って、ライブプレビューしてくれます。実際の動作は[こんな感じ(いい感じでGIFを貼る方法がわからなかったのでとりあえずGyazoを使ってます)](https://gyazo.com/e49e0ef99a3a361609e87f51f8b7349a)になります。書き途中の発表予稿の概要部分なんでまぁ見られても問題ないかな、、、。

というわけでみんな論文がんばろう!!(笑)
</div>

<div lang="en" markdown="1">
*This post is the December 2nd entry for the [IAMAS Advent Calendar 2017](https://qiita.com/advent-calendar/2017/iamas).*

Since it looks like there aren't many participants, I decided to write a light article. Right now, all the IAMAS M2 students should be deep in thesis-writing mode, so in a somewhat old-school spirit of "theses mean LaTeX!!", I'm going to write about my current writing environment. I'm using it to prepare my presentation manuscript for the [34th Japanese Society for Sonic Arts](http://jssa.info), a research presentation session held alongside [iCSAF2017](http://ic.jssa.info). Though I suspect there's maybe only one other person in my cohort who still writes papers in LaTeX...

## What is LaTeX?
Put simply, it's a markup-based writing system that lets you describe complex mathematical formulas structurally using plain text. It's commonly used for scientific papers. As my professor put it, "These days most conferences accept papers written in Word; requiring LaTeX is pretty rare nowadays..." By the way, since it's a markup format, you need to compile it in some way to see the properly formatted output.

## Setup
### Prerequisites
* homebrew is installed and your environment is set up
* Atom is installed
* This article targets macOS Sierra (though other versions should be similar)

I won't cover installing homebrew or Atom, so please use your searching skills for those.

### Installing Packages in Atom
Install the following packages from Atom's Preferences:
* latex (compiles LaTeX from within Atom)
* language-latex (provides syntax highlighting in Atom)
* pdf-view (displays PDF files within Atom)

### Installing MacTeX
We'll install it using homebrew's cask (MacTeX also distributes its own package installer, so that works too. I've been wanting to manage my environment through cask as much as possible...). homebrew is a UNIX package manager for macOS. cask extends it to handle macOS applications -- that's a good enough understanding. For installing homebrew itself, check the official site here: [https://brew.sh/index_ja.html](https://brew.sh/index_ja.html)

If you already have homebrew set up, first enable cask:

```console
brew tap caskroom/cask
```

`brew tap` adds third-party repositories to Homebrew, allowing you to install, uninstall, and update packages from them via the `brew` command. In this case, we're adding the caskroom/cask repository. Now we can install MacTeX using brew. Oh, and you may be prompted for your password -- just read the prompts and respond accordingly.

```console
brew cask install mactex
```

This should install MacTeX.
While that's running, let's configure Atom.

### Configuring Atom
In Atom, search for the latex package you installed earlier and click "Settings" to open its configuration. Check the following options:

![latex package settings](https://i.gyazo.com/2ff0b89a21437113287dddd6376b71a0.png)

* Check "Move Result to Source Directory"
* Check "Build on Save"
* If you want to preview only within Atom, leave the other two unchecked. Check them if you'd prefer to view in Acrobat or another external viewer.

### How It Works
Now you have an environment where writing LaTeX and hitting Save automatically compiles it to PDF. If you open the generated PDF in a separate Atom tab using "Split Right," it will recompile and refresh the preview every time you save -- giving you live preview. Here's [what it looks like in action (I couldn't figure out a good way to embed a GIF, so I'm using Gyazo for now)](https://gyazo.com/e49e0ef99a3a361609e87f51f8b7349a). It shows the abstract section of a presentation manuscript I'm still working on, so I guess it's fine if people see it...

So let's all do our best with our papers! (laughs)
</div>
