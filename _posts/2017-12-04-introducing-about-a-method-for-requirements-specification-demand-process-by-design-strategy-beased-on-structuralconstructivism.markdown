---
layout: post
title: "論考「デザインにおける要求定義プロセスへの構造構成主義的デザイン論の適用」の紹介"
title_en: "Introducing a Paper on Applying Structural Constructivist Design Theory to Requirements Definition in Design"
date: "2017-12-04 07:00:00 +0900"
categories: blog
bilingual: true
original_lang: ja
---

<div lang="ja" markdown="1">

※ この記事は[IAMAS Advent Calendar 2017](https://qiita.com/advent-calendar/2017/iamas)の12月4日の記事です。

またライトな記事を一本書きたいと思います。この記事では以前自分が共同創業者として立ち上げた「合同会社アライアンス・ポート(現・アライアンス・ポート株式会社)」の代表を務めているとき(現在は退職。アライアンス・ポート自体も共同創業者だった山辺氏の手を離れ、株式会社コルシスさんの子会社になりました > [ニュースリリース](http://www.allianceport.jp/news/2017/11/ap-colsis.html))に、「認知科学学会」に投稿し見事にリジェクトされた(笑)論文、、、というかリジェクトされたので論考「デザインにおける要求定義プロセスへの構造構成主義的デザイン論の適用」について紹介したいと思います。論考のPDFには最後にリンクを張っておきますので、いきなり読んでしまいたい人は下までスクロールしてください。

## アジェンダ

お題は次の通りです。

* この論考が書かれた背景
* 構造構成主義について軽く
* どんなことが書かれているか
* この論考以後どのようなデザインプロセスが生れたか
* 論考の場所と謝辞

です。

### この論考が書かれた背景

まずこの論考が書かれた背景です。この論考自体は多分2010年近辺に書かれたものです。当時、ウェブ制作をメインにお仕事をさせていただいていました。主にYCAM, TWS, アサヒアートフェスティバル、等の公共文化施設などの仕事が代表的で最終的に日本科学未来館のウェブサイトを手掛けたのはいい思い出です。で、順風満帆に仕事をしていたかというと、特に初期ですが僕はエンジニアで後のスタッフはデザイナー(山辺さんはその両方の才能を持っていましたが)で、簡単に言うと仕事のやり方や捉えかたが大きく違うんですね。簡単な話で言うと「お給料の金額感」とかも違います。なのでことあるごとにそれなりに摩擦が起きていて「なんで解りあえないんだろうなぁ」「どうしたらエンジニアとデザイナーの協業が上手くいくかなぁ」と思っていました。そんなときに「構造構成主義」という哲学の第一回の総会(?)みたいな催しに友人の編集者から現場の撮影を依頼されて行くことがありました。そこで話されている内容が大変面白くて「これはエンジニアとデザイナーとが解らないことを分かち合い、一緒に協業する理路になるんじゃないか?」と思ったところが出発点でした。

その後、1年くらい会社で「構造構成主義」とその応用である論考にも出てくる質的研究法"SCQRM(スクラムと読みます)"の話をし続け、方法がセットだったのが幸いし実際にその中の幾つかの方法(例えば「理論化の方法」や「インタビュー分析」やそれを要件定義書に援用するなど)を使ってみた結果、これは「現場でも使えるよね」となって「じゃ一度纏めよう」ということで書かれた論考です。

### 「構造構成主義」について軽く

最近はめっきり「構造構成主義」の現状は追ってないんで最新の状況ではなく、僕の理解の範囲だと先ず断わって起きます。が、今でも「構造構成主義者」を名乗りますし(笑・現在は正確には「構造構成主義者」であり「アドラー心理学派」ですけどね。いやご大層な書きっぷりですが専門家ではありません。念の為。とはいえ構造構成主義の弱点についてはアドラー心理学でカバー出来ると考えているのですが、その辺は長くなるので割愛します)、僕の行動指針や考えかたに大きく影響を与えた哲学だと思います。

構造構成主義については[構造構成主義とは何かー次世代人間科学の原理(西條剛央 2005)](http://amzn.to/2BtHPKe)を当ってもらうのが一番なのですが、ええと正直解りやすいとは言い難い(笑・しかもこの本横書きなのが輪をかけて読み難くしてると思うんですが、、、)ので、軽く本当に軽くだけ説明します。

構造構成主義は西條剛央によって体系化されたメタ哲学で、池田清彦の構造主義科学論(こちらは[構造主義科学論の冒険](http://amzn.to/2zInoZu)で読めます。この本はとても読みやすいし面白いです。ソフィーの世界を読むならまずこっち読んだほうが哲学入門になると思いますよ)と、竹田青嗣の現象学、フッサール、ソシュールなどをその理論の基盤にしています。西條さん自身がお医者さん(心理学者)ということもあって、もともとは臨床と研究の間に起きる「信念対立」を解決する方法として考えられたという経緯だったと思います。

この信念対立、というのは養老孟司の「バカの壁」などが解りやすい例ですが、簡単に言ってしまえば「各々の立場や関心から信じてる物は違う。そのうえ信じてるものは各々正しいとおもってる。なのでお互いの間に無理解が発生する」ということです。ああ簡単に言えてるかなこれ。で、これを構造構成主義では「関心相関性」「目的相関性」「肉体相関性」と「現実的制約」という形で「お互いに立ち表われている現象」に着目することで、理解を一つ下のレイヤーに下げ、お互いが「なにを理解できてないか、ということを理解する」という、、、簡単に言えば「相手の立場になりやすい」状況を作りだす方法を提示しています。

で、このような状況は得てして発生しやすく、こういう方法は色々な場面で活用できるのは容易に想像しやすい、しかも理解しちゃうと「方法として整備されている」「メタ哲学なので応用が効きやすい」こともあって、医学からマーケティング、社会活動まで広く応用されています(最後の社会活動のところの応用については応用できたか、というよりも構造構成主義の限界を西條さんが自ら示した、と僕は考えていますが。とはいえ実際に達成した現象は素晴しいと思います)。

もう書き始めると大作になる上にちょっと先にも書いたように最近の同行を追ってないのでこの辺にしておくので興味がある人はdigってみてください。ただなぁ、読みようによっては構造構成主義の落とし穴に嵌ってしまうので「どんな方法でも限界がある」という事は意識して読むことをお勧めはしますが。

### どんなことが書かれているか

というわけで、そんな背景を持って論考「デザインにおける要求定義プロセスへの構造構成主義的デザイン論の適用」は書かれています。主たる筆者は僕です。とはいえ、論文の体裁にきちんと纏めてくれたのは当時の同僚である常盤拓史さんで、この論考が真面に読める文章になってるとしたらそれは100%彼の手腕に寄るものです(なのでファーストが常盤くんで、ラストが僕、になっています)。当時この原稿の第0稿(だいたいこの量の1.5倍くらいはあった気がする)を一晩くらいで書いて常盤くんに渡した気がします。なつかしい、、、。で、実際にどんなことが書かれているか? ということを掻い摘んで説明すると、まず全体を通じて書かれているのは「デザインの仕事の初期段階の要求定義プロセスでの手法の提案」です。具体的には「構造構成主義的テザイン」と「構造構成主義をベースにした質的研究法と半構造化インタビュー(論考では半理論化インタビューとなってます)をファシリテーショングラフィックの技法で拡張したワークショップについて」と、その実際の事例が掛れています。この辺は論考の「はじめに」の部分を読んでいただければと思います。

で、この論考の(ここから自画自賛しますが・笑)画期的な部分は「構造構成主義的デザイン」としてデザインの定義をしてしまってるところです。「構造構成主義的デザイン」では(理想的に方法が機能していれば)なんと「手戻り」が発生しません(笑)。どうだすごいだろう!! (笑)。 またデザインの定義をデザインされた物や良く言われるファシリテーションプロセスとかではなく『デザインの営みとは「制作物を取りまく関係者間の合意の形成」と定義し位置付けている』ことも(今となっては「そうだよね」って思う人がいそうですが)当時からしたら結構画期的だったと思っています。ようするに「デザインっていうのは、ある瞬間のスナップショットであって、そのスナップショットは予算みたいな現実や関係者間の合意の元に決められるものなのだから、デザイン物自体は無限のバリエーションや質を追うことが出来る。そうである以上、物としてデザインを規程することはできないので、合意形成そのものがデザインの本質だ」と言ってしまっているわけです。まぁ今はワークショップの方法論が沢山あるのでみんな薄らとこういうことは考えているわけですが、今読んでもここまでハッキリ書いてる文章を他で読んだことはありません(笑・ほんと各方面から反論が来そうですが)。

また、その合意形成に「科学的担保」をする為に、質的研究法である"SCQRM"を導入し(実際には"修正SCQRM"。なぜ修正できるかは[ライブ講義・質的研究とは何か (SCQRMベーシック編) (西條 2007)](http://amzn.to/2zHiWKB)を読むと解ります)、マインドマップ、ファシリテーショングラフィック、PMBOKといったツールを使って「方法」として組みたてています。実際の事例や、モデル図の例(「理論化」とも呼ばれます)も載っていますので実際の現場でなにをやったか、はそのあたりを読んでみてください。

また、PMBOKやペルソナ/シナリオ法などとの比較もしてます。いまならアイデアスケッチとかとの比較をしてもいいでしょうね。アイデアスケッチに関しては先の「構造構成主義的デザイン」のデザインの定義からの視点では「合意形成のプロセス」に「関心、目的、肉体相関性」と「現実的制約」が不明瞭な点が常々弱いと思っていまして、アイデアの妥当性の証明の部分で補強をしたらいいのにな、、とか、、、そんなこともアイデアスケッチを知ったときから考えてはいました(が、なんとIAMAS同期のデザイナーさんがまた独自のプロセスでそこを補強しそうな研究をやってる人がいるのでビックリ。今後に期待してます!! がんばろう、論文!! お互いに!!!・笑)。

というわけで、事例ではウェブサイトの話だけですが応用範囲は広く、これ今になって思うと「なんで認知科学学会に出したんだ?」と思うばかりですが(笑)、机上ではなく「現場の経験から立ち上がったデザインに対する論考」として、IAMASみたいなところに来るような誰かさんのお役に少しでも立てたらデザインの仕事に関わった一人としてとても嬉しいです。

この話、さすがに論考読みなおさないとソラでは話せませんが、いわゆる制作物のデザインだけでなくワークショップデザインやいろいろな場面で役に立てる「かも」しれないので、興味がある人は是非一緒に楽しく議論しましょう。

### この論考以後どのようなデザインプロセスが生れたか

次に「じゃ、この論考以後にどのようなプロセスで実際の現場は動いてたのか?」という話をします。ただしこれは次に紹介する資料の主著者曰く(アライアンス・ポートの共同創業者で前代表の山辺さんですが)「構造構成主義を継承してるわけでない」と言ってるので、そういうもんだ、と思って読んでください(とはいえ実際に一緒に仕事はしてたわけですから影響がゼロだという証明は出来ないとは思いますが)。

確かにその後この論考のような厳密さを持って運用されたか? というとそうでもありまん。それはまぁ現場で仕事してるとそんな細かいこと言ってられないよ、という話ではあって、そこが僕の遣り残した仕事でもありましたし、Takramさんの仕事のやり方とか聞いてると「ああ、そういうアウトプットまでしっかりと方法化するところまでやりたかったなあ」と思うばかりではあります。ただ、とはいえ「顧客との合意形成」という「構造構成主義デザイン論」で核としてる部分については[こちらで紹介されている「共創型デザイン」の進め方と小冊子](http://www.allianceport.jp/process/index.html)の中でそれなりに継承されていると思います。詳しい説明は僕は今はもう会社を離れてしまっているので割愛しますが、興味を持った方は先のアライアンス・ポートのサイトにある小冊子を読んでみてもらうといいかな。

### 論考の場所と謝辞

はい。それでは論考「デザインにおける要求定義プロセスへの構造構成主義的デザイン論の適用」のリファレンス先を紹介します。以下のGitHubのレポジトリからダウンロードすることが出来ます。

[constructive-design_v01.pdf](https://github.com/tokiwatch/documents/blob/master/constructive-design_v01.pdf)

最後に、この論考の執筆にあたっては、まず合同会社アライアンス・ポート(現・アライアンス・ポート株式会社)の仲間達、またクライアント様に感謝します。みなさんと一緒に仕事をした経験がこういう形に残っているのは僕の誇りです。また、共著者の山辺さん小川さんに感謝します。２人と仕事をしなければこういうことを書くことも「構造構成主義」にピンと来ることもなかったかもしれないね。あと今IAMASで研究してることもね。そして最後に常盤拓史くんに最大の謝辞を送ります。彼のお陰で始めて「学会に投稿する論文を書く」という機会ができましたし、今でもこういう形で残っていることで会社の中で自分が文字通り七転八倒してたことが無駄なことじゃなかった、無駄なことなんて一つもなかった、と思うことができます。また呑みにいこうね。

というわけで「軽く書く」というつもりが結構な分量になってしまいましたが、以上で論考「デザインにおける要求定義プロセスへの構造構成主義的デザイン論の適用」の紹介を終ります。いつかどこかの誰かの役に立ちますように、、、

</div>

<div lang="en" markdown="1">

*This post is part of the [IAMAS Advent Calendar 2017](https://qiita.com/advent-calendar/2017/iamas), published on December 4th.*

I wanted to write a lighter article this time. In this post, I would like to introduce a paper -- or rather, since it was rejected, let us call it a treatise -- titled "Applying Structural Constructivist Design Theory to the Requirements Definition Process in Design." I submitted it to the Japanese Cognitive Science Society while I was serving as representative of Alliance Port LLC (now Alliance Port Inc.), a company I co-founded. (I have since left the company. Alliance Port itself has also changed hands from co-founder Yamabe and became a subsidiary of Colsis Inc. > [News release](http://www.allianceport.jp/news/2017/11/ap-colsis.html)). The paper was, shall we say, gloriously rejected. I have included a link to the PDF at the end, so if you want to jump straight to reading it, scroll down.

## Agenda

Here is what this article covers:

* The background behind this treatise
* A brief overview of Structural Constructivism
* What the treatise contains
* What design processes emerged after this treatise
* Where to find the treatise, and acknowledgments

### Background of This Treatise

Let me start with the background. This treatise was probably written around 2010. At the time, I was mainly doing web development work. My notable projects included websites for public cultural institutions such as YCAM, TWS, and the Asahi Art Festival, and the crowning achievement was working on the website for the National Museum of Emerging Science and Innovation (Miraikan). But was everything going smoothly? Not quite -- especially in the early days. I was an engineer, while the rest of the staff were designers (though Yamabe had talent in both areas). Put simply, our approaches to work and how we understood it were quite different. Even something as basic as salary expectations differed between us. So friction arose regularly, and I kept thinking, "Why can't we understand each other?" and "How can engineers and designers collaborate better?" Then one day, a friend who was an editor asked me to come photograph the first general meeting of a philosophical movement called "Structural Constructivism." What I heard there was fascinating, and I thought, "This could provide a framework for engineers and designers to share what they don't understand about each other and collaborate together." That was the starting point.

After that, I spent about a year at the company talking about Structural Constructivism and its applied qualitative research method called "SCQRM" (pronounced "scrum"), which also appears in the treatise. Because the theory came with a set of practical methods, we were able to try several of them in practice -- things like "theorization methods," "interview analysis," and adapting these for requirements specification documents. The result was a consensus that "this is actually usable in the field," and so we decided to write it all up. That is how this treatise came to be.

### A Brief Look at Structural Constructivism

Let me preface this by saying I have not been keeping up with the latest developments in Structural Constructivism, so what follows reflects my own understanding. That said, I still call myself a "Structural Constructivist" (and to be precise, I am both a "Structural Constructivist" and an "Adlerian psychologist" -- though I should note I am not an expert in either field. I do believe, however, that Adlerian psychology can cover some of the weaknesses of Structural Constructivism, but that is a longer discussion for another time). It is a philosophy that has profoundly influenced my principles and way of thinking.

The best source on Structural Constructivism is [What Is Structural Constructivism: Principles of Next-Generation Human Science (Saijo Takeo, 2005)](http://amzn.to/2BtHPKe), though I must admit it is not the easiest read (and the horizontal text layout does not help). So let me give a very brief explanation.

Structural Constructivism is a meta-philosophy systematized by Saijo Takeo. It draws on Ikeda Kiyohiko's Structuralist Philosophy of Science (available in [Adventures in Structuralist Philosophy of Science](http://amzn.to/2zInoZu) -- this book is very readable and interesting; I would recommend it over Sophie's World as an introduction to philosophy), Takeda Seiji's phenomenology, Husserl, Saussure, and others. Because Saijo himself is a psychologist, the framework was originally conceived as a way to resolve "belief conflicts" that arise between clinical practice and research.

"Belief conflict" -- illustrated well by Yoro Takeshi's book "The Wall of Fools" -- is essentially this: "People believe different things depending on their positions and interests. Moreover, everyone believes what they believe is correct. This creates mutual misunderstanding." Structural Constructivism addresses this through concepts such as "interest-relativity," "purpose-relativity," "body-relativity," and "practical constraints," focusing on "the phenomena that manifest for each party." By doing so, it lowers the level of understanding and enables both sides to "understand what they do not understand about each other" -- in simpler terms, it presents a method for making it easier to see things from the other person's perspective.

Since these kinds of situations arise frequently, it is easy to imagine how such methods can be useful in many contexts. Once you grasp it, you realize that "the methods are well-organized" and "being a meta-philosophy makes it highly adaptable." As a result, it has been applied broadly, from medicine to marketing to social activism (though regarding the social activism applications, I personally believe that Saijo demonstrated the limits of Structural Constructivism rather than successfully applying it -- though what was actually achieved was still remarkable).

I could write at length about this, but as I mentioned, I have not been following recent developments, so I will stop here. If you are interested, I encourage you to dig in. But I do recommend reading with the awareness that "every method has its limits," lest you fall into the trap of Structural Constructivism.

### What the Treatise Contains

With that background, let me describe the treatise itself. I was the primary author, though the person who properly organized it into an academic paper format was my colleague at the time, Tokiwa Takushi. If this treatise is readable at all, it is 100% thanks to his skill (which is why Tokiwa is listed as first author and I am last). I remember writing the zeroth draft (about 1.5 times the final length) in a single night and handing it to Tokiwa. Good times.

So what does it actually say? In brief, the overall theme is "a proposed methodology for the requirements definition process in the early stages of design work." Specifically, it covers "Structural Constructivist Design," "a workshop that extends qualitative research methods and semi-structured interviews (called 'semi-theorized interviews' in the treatise) based on Structural Constructivism using facilitation graphic techniques," and actual case studies. For details, I recommend reading the introduction section of the treatise.

The groundbreaking part of this treatise (if I may say so myself) is that it defines design through the lens of Structural Constructivism. Under "Structural Constructivist Design," if the method functions ideally, there are no "rework loops." How about that! Furthermore, rather than defining design as the designed artifact or the commonly discussed facilitation process, it positions "the practice of design as the formation of consensus among stakeholders surrounding the deliverable." While some might think "well, obviously" today, at the time this was quite a radical statement. In other words, it says: "Design is a snapshot of a particular moment, and that snapshot is determined by real-world constraints like budgets and consensus among stakeholders. Since a designed artifact can pursue infinite variations and qualities, you cannot define design by the artifact itself -- therefore, consensus-building itself is the essence of design." Nowadays, with so many workshop methodologies available, people vaguely think along these lines, but I have still never read anything else that states it this clearly (and I am sure I will get pushback from many quarters).

To provide "scientific grounding" for this consensus-building, we introduced the qualitative research method "SCQRM" (actually a "modified SCQRM" -- you can understand why it can be modified by reading [Live Lecture: What Is Qualitative Research (SCQRM Basic Edition) (Saijo, 2007)](http://amzn.to/2zHiWKB)), and assembled it as a "method" using tools such as mind maps, facilitation graphics, and PMBOK. The treatise includes actual case studies and examples of model diagrams (also called "theorization"), so please refer to those sections to see what we actually did in practice.

The treatise also includes comparisons with PMBOK, persona/scenario methods, and other approaches. Today, it would be worth comparing it with idea sketching as well. Regarding idea sketching, from the perspective of the definition of design in "Structural Constructivist Design," I have always felt that the weakness lies in the ambiguity of "interest, purpose, and body-relativity" and "practical constraints" within the "consensus-building process," and I have thought it would benefit from reinforcement in validating the legitimacy of ideas. (As it happens, a fellow IAMAS classmate who is a designer is conducting research that might complement this through their own unique process -- I am excited to see where it goes! Let us both keep working on our papers!)

While the case studies deal only with websites, the range of application is broad. Looking back now, I cannot help but wonder "why did we submit this to the Cognitive Science Society?" But as a treatise on design that "arose from real-world experience rather than theory alone," if it can be of any help to someone who finds their way to a place like IAMAS, that would make me very happy as someone who has worked in the field of design.

I cannot discuss this topic off the top of my head without re-reading the treatise, but it may be useful not only for artifact design but also for workshop design and various other contexts. If you are interested, I would love to have a lively discussion about it.

### Design Processes That Emerged After This Treatise

Next, let me talk about "what processes were actually used in the field after this treatise?" However, the primary author of the materials I am about to introduce -- Yamabe, co-founder and former representative of Alliance Port -- has said, "This does not inherit from Structural Constructivism," so please read it with that understanding (though since we were working together, I do not think you can prove the influence was zero).

Indeed, was it applied with the same rigor as this treatise afterward? Not exactly. That is simply the reality of working on the ground -- you cannot be that meticulous about everything. That was unfinished business for me, and when I hear about how companies like Takram approach their work, I think, "I wish I could have taken it that far, formalizing the method all the way to the output." Nevertheless, the core of "Structural Constructivist Design Theory" -- building consensus with clients -- has been carried forward to some degree in [the "Co-creative Design" approach and booklet introduced here](http://www.allianceport.jp/process/index.html). Since I have already left the company, I will not go into detailed explanations, but if you are interested, the booklet on the Alliance Port website is worth a read.

### Where to Find the Treatise and Acknowledgments

The treatise "Applying Structural Constructivist Design Theory to the Requirements Definition Process in Design" can be downloaded from the following GitHub repository:

[constructive-design_v01.pdf](https://github.com/tokiwatch/documents/blob/master/constructive-design_v01.pdf)

Finally, I would like to express my gratitude to the team at Alliance Port LLC (now Alliance Port Inc.) and to our clients. That my experiences working with all of you have been preserved in this form is a source of pride. I also thank my co-authors, Yamabe and Ogawa. Without working with the two of you, I might never have written something like this, never have connected with Structural Constructivism, and never have ended up doing research at IAMAS. And last but not least, my deepest thanks go to Tokiwa Takushi. Thanks to him, I had my first opportunity to write a paper for academic submission. The fact that this work still exists in this form lets me believe that all the struggles I went through at the company were not in vain -- not a single one. Let us go out for drinks again sometime.

What I intended to be a "quick write-up" ended up being quite long, but that concludes my introduction to the treatise "Applying Structural Constructivist Design Theory to the Requirements Definition Process in Design." I hope it helps someone, somewhere, someday...

</div>
