---
layout: post
title: "ICSAF2017と第34回JSSA先端芸術音楽創作学会研究会への参加します(あとそのついでにIAMASの卒論用のLaTexフォーマット作りました)"
title_en: "Participating in ICSAF2017 and the 34th JSSA Research Meeting (and I made a LaTeX format for IAMAS theses)"
date: "2017-12-09 07:00:00 +0900"
categories: event
bilingual: true
original_lang: ja
image: /images/ogp/2017-12-09-icsaf2018-and-iamas-research-latex-format.png
---

<div lang="ja" markdown="1">

※ この記事は[IAMAS Advent Calendar 2017](https://qiita.com/advent-calendar/2017/iamas)の12月9日の記事です。

来たる12月16日、17日に行なわれる[インターカレッジソニックアートフェスティバル2018](http://ic.jssa.info)と[第34回JSSA先端芸術音楽創作学会研究会](http://jssa.info)に参加に今年も参加します([IAMASの公式サイトでも告知していただきました](http://www.iamas.ac.jp/activity/icsaf2017/)。ありがとうございます)。

去年はインカレのみに参加して若者達にまじって「ギター少年みたいなオッサンが来たな」という感じでギターを弾いてパフォーマンスしてきましたが、今年は修士作品の一部として作った演奏の映像記録(演奏は僕はしていません)を上映しにいきます。また第34回JSSA先端芸術音楽創作学会研究会で研究報告も行います。こちらは三輪さんと連盟での研究報告なんで昨日まで必死に原稿書いてました。とりあえず原稿はできたのですがまだ三輪さんからチェックは戻って来てないので甚だ不安ではありますがいつものクオリティで発表は楽しくやれたらな、、と思うので他の参加者は他校の先生のみなさまどうぞよろしくお願いします。会場は昭和音大の南校舎です。基本的に誰でも見にこれるはずなんですが、金山さんの来場は固くお断りします(笑・冗談だよ)。とはいえ、研究の内容はそこそこ議論になるんじゃないかと思ってるんで他者が聞いてどういう感想を持つのかは楽しみですね。僕の出番は両イベント共に16日(土曜)なので見掛けたら気軽に声をかけてくださいませ。いろいろ忙しいので17日は行けないかもだけど、、、。

で。

そんなわけでJSSA用の発表予稿(査読なし論文)を書いてたのですが、その原稿が「LaTexもしくは、HTMLみたいなMarkdown」で正直「この時代にLaTex指定とか、、、」と辟易してたのですが、いい機会なんでLaTexで書いてみたらミイラ取りがミイラになるとはこの事、いやぁ楽だわ、LaTex。とすっかり宗旨替えしてしまいました。LaTex便利だよ、なにこれ!! 目次とか章番号とか図版番頭とリファレンスとかがズレる可能性がない、というのは精神的安定につながりますね、、、

もともとIAMASの修士論文をどんどん書いていかないとならない状況だったので、いい機会なんで論文で予定されている章の一部をJSSAの発表予稿として書いてることもあって「じゃーもうこのまま修士論文もLaTexで書いてしまおう」ということになって、先日IAMASの修士論文用のLaTexのフォーマットを作って[GitHubにアップしておきました](https://github.com/dropcontrol/IAMAS-Resarch-LaTex-Format)。さきほど昨年度の卒業生の篠田さんにその話したら「去年欲しかった、それ」って言われて一定の需要があるのをこれで2件は確認できたのでうまく使ってもらえればと。

IAMASの修士論文は過去の卒業生の論文を見ると基本的な構成は

* 表紙
* アブストラクト(日本語)
* アブストラクト(英語)
* 本文
* その他資料とかのおまけ

みたいな構成になってるようです。事務局から伝えられているレギュレーションとしては「アブストラクトは指定の書式に従うこと」ということでWordとPDFが配布されています。また本文は1ページ1000文字程度ということです。なので、アブストのところはテーブルでWordの内容を丸コピして作ってあります。日本語で1000文字程度、英語で500ワード程度、のダミーが埋めてありますので大体量感も解るかな、、、これが1ページに収まらないようならレギュレーション的に問題がある、ということで大体いいのでは。で本文については1ページ1000文字ということなので1カラムで収まるように余白と文字サイズの調整をしてあります。

といっても、実は殆どLatexの標準的なフォーマットをそのまま使って文字サイズを\large指定しただけという代物なのでiamas.styには一行も定義が書いてありません(笑)。今後必要なら書き加えていこうと思うのですが、まぁ同期で使う人はいなそうなので来年の人とかが育ててくれると嬉しいです。適当にフォークしてプルリクエスト送ってください。

追記・多少iamas.styに手を加えました。インカレのを参考に「参考文献」と「参考作品」を別に引用できるようになってます(要、cicago.sty)。
追記2・タイトルのICSAF2017を2018と時空が歪んだ間違いをしていたのを修正しました。

</div>

<div lang="en" markdown="1">

*This post is the December 9th entry for the [IAMAS Advent Calendar 2017](https://qiita.com/advent-calendar/2017/iamas).*

I will be participating again this year in the [Intercollege Sonic Arts Festival 2018](http://ic.jssa.info) and the [34th JSSA (Japanese Society of Sonic Arts) Research Meeting](http://jssa.info), taking place on December 16th and 17th ([IAMAS also posted an announcement on their official site](http://www.iamas.ac.jp/activity/icsaf2017/) -- thank you!).

Last year I only participated in the Intercollege event, mixing in with the younger crowd and performing guitar, giving off the vibe of "some old guy who looks like a guitar kid showed up." This year, however, I will be screening a video recording of a performance that I created as part of my master's thesis work (I was not the performer). I will also be giving a research presentation at the 34th JSSA Research Meeting. Since this is a joint presentation with Miwa-san, I was writing the manuscript frantically until yesterday. The manuscript is done for now, but I have not gotten Miwa-san's feedback yet, so I am fairly anxious. I hope to have fun presenting at the usual quality level -- to all the other participants and faculty from other schools, I look forward to meeting you. The venue is the South Building of Showa University of Music. In principle, anyone should be able to come and watch, though I must firmly decline a visit from Kanayama-san (just kidding). That said, I think the research content will generate some good discussion, so I am looking forward to hearing what others think. My appearances at both events are on the 16th (Saturday), so please feel free to say hello if you see me. I might not be able to make it on the 17th since things are busy...

So.

Anyway, I was writing the proceedings paper (non-peer-reviewed) for the JSSA presentation, and the manuscript format was specified as "LaTeX or Markdown that looks like HTML." Honestly, I was put off at first thinking "LaTeX in this day and age..." But since it was a good opportunity, I gave LaTeX a try, and before I knew it I had become a complete convert. LaTeX is so convenient -- what is this thing?! The fact that there is no chance of the table of contents, chapter numbers, figure numbers, or references getting out of sync really brings peace of mind...

I was already in a situation where I needed to keep writing my IAMAS master's thesis, and since I was writing part of a chapter planned for the thesis as the JSSA proceedings paper, I decided "let's just write the entire master's thesis in LaTeX too." So I created a LaTeX format for IAMAS master's theses and [uploaded it to GitHub](https://github.com/dropcontrol/IAMAS-Resarch-LaTex-Format). When I mentioned this to Shinoda-san, a graduate from last year, they said "I wish I had that last year," so I have now confirmed at least two cases of demand. I hope people can make good use of it.

Looking at theses from past IAMAS graduates, the basic structure of a master's thesis appears to be:

* Cover page
* Abstract (Japanese)
* Abstract (English)
* Main text
* Supplementary materials and appendices

The regulations communicated by the administration state that "the abstract must follow the designated format," and Word and PDF templates are distributed. The main text should be approximately 1,000 characters per page. So for the abstract section, I replicated the Word content using tables. I have included dummy text of approximately 1,000 Japanese characters and about 500 English words, so you can get a rough sense of the volume. If it does not fit on one page, there is likely a regulation issue -- that should be a good guideline. For the main text, since it requires about 1,000 characters per page, I adjusted the margins and font size to fit in a single column.

That said, the truth is I mostly just used the standard LaTeX format and specified \large for the font size, so there is not a single line of definitions in iamas.sty (laughs). I plan to add more as needed, but since none of my classmates seem likely to use it, I would be happy if students in future years develop it further. Feel free to fork it and send pull requests.

Addendum: I made some additions to iamas.sty. Referencing the Intercollege format, you can now cite "References" and "Referenced Works" separately (requires cicago.sty).
Addendum 2: I fixed the title where I had written ICSAF2018 instead of ICSAF2017 -- a time-warping mistake.

</div>
