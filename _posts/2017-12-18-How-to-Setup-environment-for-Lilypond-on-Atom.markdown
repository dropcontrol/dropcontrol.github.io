---
layout: post
title: "LilypondをAtomで使う環境作り"
title_en: "Setting Up Lilypond on Atom"
date: "2017-12-18 07:00:00 +0900"
categories: blog
bilingual: true
original_lang: ja
image: /images/ogp/2017-12-18-How-to-Setup-environment-for-Lilypond-on-Atom.png
---

<div lang="ja" markdown="1">

※ この記事は[IAMAS Advent Calendar 2017](https://qiita.com/advent-calendar/2017/iamas)の12月18日の記事の予定地です。

またしてもライトな環境構築ネタですいません。オープンソースの自分的に最強の譜面書き環境LilypondをAtomエディタ上で使う方法について書きます。

## アジェンダ

* Lilypond ってなに?
* インストールと設定
* 使いかた

アジェンダって程のことでもないですね、、、。

### Lilypondってなに?

Lilypondは "LilyPond is a music engraving program, devoted to producing the highest-quality sheet music possible. It brings the aesthetics of traditionally engraved music to computer printouts. LilyPond is free software and part of the GNU Project." とあるように「楽譜制作のソフトウェア」であり「GNUプロジェクトのfree software」だと[公式ウェブサイト](http://lilypond.org)に書いてあります。

それだけだとちょっと説明が足らないので、もうすこし説明すると世の中にはFinaleとかSiberiusとかNotionとか他にも色々な譜面書きソフトがあります。なんか今こう書いてみると譜面書きソフトがそんなにあるってそんな需要がある市場なんだろうか、、、という素朴な疑問も生れますが(笑)それらのソフトとLilypondが一番ちがうのはLilypondは先日の[LaTexの記事](/blog/2017/12/02/how-to-setup-evironment-for-latex-on-atom-with-live-preview.html)で取り上げたLaTexと同じ感じで「楽譜をマークアップして構造的にテキストで記述出来る」という点にあります。と言われてもあんまりピンこない、という人は公式サイトの[テキスト入力](http://lilypond.org/text-input.ja.html)の説明のページとか見ていただけると良いと思います。

で、使い慣れるとこれがもうマウスでポチポチみたいなGUIのソフトに比べて圧倒的に早く楽譜が記述できます。しかもあたりまえですが手書きと違って綺麗(笑)な楽譜が出来上がります。今回、IAMASで僕が研究してる途中で作った楽譜や修士作品の楽譜なんかは98%はLilypondです(あとの1%は手書き、もう1%はLogicの楽譜出力機能)。

じゃーどこが便利なの? という話は今修士論文書いてるのでそっちに書く予定ですがとりあえずFinale, Siberiusといった2大楽譜作成ソフトでは出来ない記述が可能なのです。ほんと異常な楽譜が書けます(笑)。例えば小節の途中で折りかえすとか、しかもそこが連符の途中でも、みたいな譜面の禁則みたいなのをブッチギレます。いやそれ見付けるまで大変苦労しました。ただかなりマニュアルは日本語訳されているので普通の事をしてる分にはそれほど敷居が高くはないです。ていうか多少のプログラムの心得がある人ならすぐに慣れると思いますよ。

またmusicXMLをLilypond形式にコンバートしてくれるとかの便利コマンドとかもあるので、Logicで作ったMIDIデータをmusicXMLで出力してそれをコンバートしてLilypond上で修正と整形していく、なんて使いかたもできます。僕は使ったことがまだありませんが、LilypondのデータからMIDIを出力もできるので上手くやればAtomで譜面を書きつつ音を確認していく、なんてワークフローが組めるかもしれません(ただ繰返し記号なんかを正確に再生するのには多少は難がある、みたいな話も見た記憶があります)。

そんな便利なLilypondですからそりゃ、マークアップするのに普段使いなれたAtomを使いたくなるじゃないですか。なるのが人情ってものなので調べました。そしたらやっぱり同じようなこと考える人がいるんでしょうね。AtomのLilyPond関連のパッケージがありました。

### インストールと設定

例によって対象はmacOSです。インストールも設定もそんなに大変な話ではないのです。Lilypond本体は先程の公式サイトからmacOS用のパッケージを落してきて普通にインストールします。

次にAtomのパッケージから以下のパッケージをインストールしてください。

* AtLilyPond ... Lylipondのシンタックスハイライトしてくれます
* lilycompile ... AtomからLylipondのコンパイルを走らせてくれます
* pdf-view ... PDFのビュワーです

基本的はこれをAtomにインストールすればインストールは終りです。lilycompile のSettingで出力するファイル形式(File Type)と、出力したときにどこに表示するか?(Opening Behavior)を選んでおくと良いとおもいます。

### 使いかた

.lyという拡張子のファイルを作って(面倒なんで僕はこの拡張子をダブルクリックするとAtomで開くように紐付けしてしまいした。そうじゃないとLilypondのアプリが起動してきます)、"ctrl+alt+l"(最後は小文字のエルです)をタイプすれば、そのファイルをLylipondのコンパイラに渡してコンパイルしてくれます。コンパイルに失敗するとエラーがポップアップされます(あまり詳細なエラーが出る感じじゃないので、構文とかでハマったときにはそれなりに大変でした)。上手くコンパイルが通るとデフォルトだとAtomの右分割されたところに表示されます。

そこまで行けばあとは譜面を書きながらひたすら"ctrl+alt+l"する度にそのPDFが更新されます。保存と同時にライブプレビューされると便利だよなぁ、とか思った人もいると思いますが、Markdownなんかと違って譜面の規模が大きくなるとコンパイルにけっこう時間が掛ったりするので、基本的にこの仕様で便利に使えると思います。ジャズのリードシートくらいなら一瞬でコンパイルしてくれるのでなにも問題ないです(笑)。

というわけで、特に画像もなく文章だけだとあまり伝わり難いかな、、と思いますが、ちょっと狂った譜面の書き方は別途修士研究のアレコレとあわせて書きたいと思います(笑)。というか論文でも触れるところなのでどこまで書いちゃっていいのか微妙ではありますが。。。次回に続く!!(のか?)。

</div>

<div lang="en" markdown="1">

*Note: This post was written for the [IAMAS Advent Calendar 2017](https://qiita.com/advent-calendar/2017/iamas), December 18th.*

Sorry for another lightweight environment setup topic. This time I'll write about how to use Lilypond -- the open-source music notation tool that I personally consider the best -- within the Atom editor.

## Agenda

* What is Lilypond?
* Installation and setup
* How to use it

Not exactly a grand agenda, I know...

### What is Lilypond?

As stated on the [official website](http://lilypond.org): "LilyPond is a music engraving program, devoted to producing the highest-quality sheet music possible. It brings the aesthetics of traditionally engraved music to computer printouts. LilyPond is free software and part of the GNU Project." In short, it is music notation software and free software under the GNU Project.

To elaborate a bit more: there are many notation programs out there, such as Finale, Siberius, Notion, and others. Now that I list them out, I do wonder if there is really that much demand for notation software... But anyway, the biggest difference between those programs and Lilypond is that Lilypond lets you describe music scores structurally as text using markup -- similar to LaTex, which I covered in a [previous article](/blog/2017/12/02/how-to-setup-evironment-for-latex-on-atom-with-live-preview.html). If that still does not quite click, take a look at the [Text Input](http://lilypond.org/text-input.ja.html) page on the official site.

Once you get used to it, you can write music notation dramatically faster compared to GUI software where you click around with a mouse. And of course, unlike handwritten scores, the output is clean and beautiful. About 98% of the scores I created during my research at IAMAS and for my master's thesis were made with Lilypond (the remaining 1% was handwritten, and another 1% came from Logic's score export feature).

As for what exactly makes it so useful -- I plan to cover that in my master's thesis, which I'm currently writing. But in short, Lilypond can handle notation that the two major notation programs, Finale and Siberius, simply cannot. You can write truly unconventional scores. For example, you can break a line in the middle of a measure, even if it falls in the middle of a tuplet -- basically ignoring the usual notation taboos. It took me quite a while to figure that out, though. That said, a significant portion of the manual has been translated into Japanese, so for standard use cases the barrier to entry is not that high. If you have even a little programming experience, you should pick it up quickly.

There are also handy commands for converting musicXML to Lilypond format, so you can export MIDI data created in Logic as musicXML, convert it, and then edit and format it in Lilypond. I have not tried it myself yet, but you can also export MIDI from Lilypond data, so it might be possible to set up a workflow where you write scores in Atom while checking the playback. (Though I have seen mentions that accurately playing back repeat signs and such can be a bit tricky.)

Given how useful Lilypond is, naturally you would want to use your everyday editor, Atom, for the markup work. It is only human nature, so I looked into it. And sure enough, other people had the same idea -- there are Atom packages for LilyPond.

### Installation and Setup

As usual, these instructions are for macOS. Neither the installation nor the setup is particularly difficult. Download the macOS package for Lilypond from the official site mentioned above and install it normally.

Next, install the following packages from Atom's package manager:

* AtLilyPond ... Provides syntax highlighting for Lilypond
* lilycompile ... Runs the Lilypond compiler from within Atom
* pdf-view ... A PDF viewer

That is basically all you need to install in Atom. I recommend going into lilycompile's Settings to configure the output file format (File Type) and where the output should be displayed (Opening Behavior).

### How to Use It

Create a file with the .ly extension (I personally associated this extension so that double-clicking opens it in Atom, because otherwise the Lilypond application launches instead), then press "ctrl+alt+l" (the last character is a lowercase L) to pass the file to the Lilypond compiler. If compilation fails, an error pops up (the error messages are not very detailed, so debugging syntax issues could be a bit of a struggle). When compilation succeeds, the output is displayed by default in a split pane on the right side of Atom.

From there, you just keep writing your score and pressing "ctrl+alt+l" each time to update the PDF. Some of you might think it would be convenient to have a live preview on save, but unlike Markdown, compilation can take quite a while as scores grow larger, so this manual trigger approach actually works well in practice. For something like a jazz lead sheet, compilation is nearly instant, so there is no issue at all.

So there you have it. I realize that without screenshots it may be hard to fully convey, but I plan to write about some of the more unconventional notation techniques alongside my master's research. Though since it will also appear in my thesis, I'm not entirely sure how much I should reveal here... To be continued!! (Maybe?)

</div>
