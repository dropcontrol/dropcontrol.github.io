---
layout: post
title: "AtomでLatexのライブプレビュー環境を作る(OSX対象)"
date: "2017-12-02 08:44:52 +0900"
---
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

brew tapは公式以外のレポジトリをHomebrewに追加して、brewコマンドででinstall, uninstall, updateなどが行うようにします。この場合caskroom/caskのレポジトリを追加。これでMaxTexのインストールをbrewコマンドで行えるので以下を実行。あそうそう、パスワードが要求されることがありますが、そのあたりは表示を良く読んでヨシナに対応してください。

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
