---
layout: post
title: "AIと暮らす"
title_en: "Living with AI"
date: 2026-03-05 00:00:00 +0900
categories: blog
bilingual: true
original_lang: ja
---

<div lang="ja" markdown="1">

この2月はかなり仕事が忙しかった。去年の9月から続けていた仕事が3月の頭に大体片付くというスケジュールで動いていて、その間にジャズバンドでのライブと、自作のライブコーディングツール[OrbitScore](https://github.com/signalcompose/orbitscore)を使ったライブもやっていた。まあ、そうやって自分のことに挑戦しているだけであれば、自分の責任と体力と、持っているリソースを使ってやるだけだから、本人がやるだけの話なんだけど。

そして、去年の12月に母親が倒れた。倒れた中では運が良かった方ではあったが、体にそこそこちゃんとした障害は出た。けれど、認知能力とか記憶とか言葉とか、そういったところにはダメージがなく、コミュニケーションも取れるし、認知も大丈夫。今はリハビリテーション病院でリハビリを受けている。見舞いに行っても話ができるので、うちの弟と代わる代わる見舞いに行って、母が楽しみにしているコーヒーを持っていく。母はモダンな人というか、ハイカラな人なので、どんな話をしても大抵通じる。仕事の話、AIの話、音楽の話。今は5月に、倒れる前に取ってあったSnarky Puppyのライブのチケットが母の分もあるので、「それを見に行きたいね」という話をして、それを励みにリハビリを頑張っている。

今、僕は実家からすぐそばのところに会社のスペースを借りて寝泊まりしている。実家からは出ているけど、歩いて30秒くらいの距離なので、何かあれば見に行ける。とはいえ普段から実家にいるわけじゃないから、弟が父親とどういう暮らしをしているかなんて、考えも及ばなかった。そしたら、父親が認知症気味で——今まで認知症だとは言われていなかったんだけど——弟にかなり世話をかけるような状況になっていることが判明した。弟がずいぶん大変そうだということになって、そこから僕が介入して、地域のケアプラザの人に状況を話したり、母の介護申請は入院してすぐに行っていたけれど、ケアプラザの人のアドバイスもあって父の介護申請もすぐに出したりした。ここしばらくお兄ちゃん業務を頑張ってなんとかやっていた。これは考えるより軽い作業ではなかった。人の気持ちの入る作業だからなかなか辛かった。介護疲れで親を殺してしまうニュースとか、それはあるよなって、身に染みて感じるようになった。

クライアントには事情を話して、「少し時間がそっちに取られます」と伝えた。でもクライアント側だって本来は「それをなんとかするのはあなたの問題でしょ」という話なわけで——そんなこと言わないけどね、僕のクライアントはものすごくいい人たちなので——僕はそう考えなきゃいけない。社員にも事情を話して協力してもらって、母の見舞いに行ったり、弟のケアをしたり、サポートに回ったりして、その中で仕事を進めないとならなかった。

そういう時に、生成AIでプログラムを書くという時代が来てくれたのは、本当にありがたかった。思い返せば、母が倒れたすぐ後や、父の介護認定がどうしたという時も、ChatGPTに聞いて、横浜市で取れるステップにはどういうものがあるかをまとめたりして、母と弟に資料化して見せたりしたりと、物事を順序立ててこなせるようにした。誰かがやらなきゃいけない仕事だったので、一番やる能力があった人間がやるべきことをやった。そんなに冷静でもなかったが、ただ、やれる人間が仕事してやった。

AIを使ってプログラムを書くということは、もう能力的には完全にAIの方が僕よりプログラムが書ける。この前ライブコーディングのライブで使ったOrbitScoreというプログラムは、僕は一行もプログラムを書いていない。僕がやったのは、DSL——ドメインスペシフィックランゲージ——の言語仕様を作ること。自分のやりたい音楽を規定する言語仕様を作って、その仕様書を作ることだった。その上でプログラムしてもらう。コンピュータリーダブルな情報であれば、今の生成AIはかなりいいところまで詰めてくれる。けど、きちっと指示をしないとダメというのもある。

この記事も、僕が口述したのを後から編集して作成を行なっている。書くのが嫌いなわけじゃないけど、やり方を変えようと思ったから。実はこれは2回目で、1回目はめちゃくちゃ嘘を書かれた。僕はなぜか実家が名古屋にあることになっているし、東京で仕事していることになっているし、嘘八百すぎて記事を全部没にした。今回はそうならないことを祈っている。今も自分でリライトしてるしね。

じゃあAIにどう仕事をしてもらうかというと、結局、一緒にいい企画書を書いて、いい仕様書を起こして、技術スタックを考えて決めて、ドキュメント駆動開発、TDD、DRY、Git flow、Issueを必ず書く——そういう開発スタイルをしっかり守れるガードレイル作りをやって文章できちっと担保することがとても大事になってくる。これは人間同士でやっても理想とされていることだと思う。

TDDを理想的にやれるかと言ったら、正直、人間のリソースで完璧に回すのは無理だと僕は思っている。友達にものすごく優秀なエンジニアがいるので、そっちから石つぶてが飛んできそうで怖いんだけど、テストをすべて書いて実装するという理想をクライアントワークの中でやれる人はよほどのスーパーマンだと思う。僕の実力だとなかなか難しい。ただ、AIを使うと、このスタイルが正しくAIに動いてもらうためにとても大事になる。ドキュメントが唯一の真実、one source of truthであり、そこからissueを起こし、red testを書き、実装を行い、green testまで続ける。コンテキストに限りがあるAIを使う中でも、コンテキストが途切れた時に開発が正しく進むのが、このやり方だ。

Claude codeを使っていてConversation Compactingが起こるたびにAIが物忘れする。「このルール忘れた、あのルール忘れた」って。そのたびに「思い出して」と言ってやるんだけど、最近父と話していると、「AIみたいだな父」と思ったりする。正直、プログラムの性能なんて上げなくていいから、AIの長期記憶の問題は早くなんとかしてほしい。そうならないためにドキュメント駆動開発とかいろんな手法を使ったり、プロジェクトによってはコミットする時に必ずワークログを書かせたりしている。その辺はみんな各々工夫していると思うので、将来的に改善される項目だとは思っているけど。

よく、AIを使うことでクリエイティビティが損なわれるとか、人間の仕事が奪われるとか、果ては人類が滅ぶとかいう言説を見ることもある。でも暮らしの中でこうやってAIを使っていくと、これは便利な道具であるし、この道具によって生まれるものがあまりにも大きいので、そこから逃げ出すことは不可能だとすら思う。たとえまだ数パーセントの人しか使ってないとしても、だ。

僕がインターネットを初めて触ったのは多分20代前後で、10代の頃は草の根BBSだった。インターネットが出てきて不可逆な革命が起きた。あれも産業革命レベルの革命だったと思う。その後、梅田望夫さんの『[ウェブ進化論](https://amzn.asia/d/0fEXlJf2)』が出て結構なヒットをしたけど、あれを読んだ時に思った。あの本には「国境の壁がなくなる」みたいなことが書いてあったけど、ぶっちゃけ「すごく牧歌的なこと書いているな」と思った。僕があれを読んで一番最初に思い浮かんだのは、「これによって持つ者と持たざる者の格差が起きる」ということだった。今、AIによって同じことが起ころうとしている。

Claude Codeを提供しているAnthropicがオープンソースに貢献している人には6ヶ月無料とか平気でやってしまう。すごく雑で嫌な選民主義的な思想だなと思った。もちろん自分がそういう活動をしていなかったから仕方がないし、やっかみかもしれないけど、AI自体がもたらしている可能性やチャンスはそういうことなのかと思ってしまう。OpenAIにしろAnthropicにしろAlibabaにしろ、みんな営利企業だから仕方がないとは思うけど。

僕は今年で56歳になる。おかげさまで体は元気で、頭も働く。若い人に対してアドバンテージがあるとすれば、いろんなものを見聞きした経験がある。言っちゃロートルですよ。ロートルにはロートルの戦い方があって、そのアドバンテージを使うことがAIによってできるようになった。数年前は自分が一生で作れるものの数はもう計算できる年になっていて、何を作るかの優先順位を立てて、あと指折りいくつしかできないだろうと考えていた。会社もやっているから、すべてのリソースを創作活動に注げるわけでもない。でも、Claude Codeや生成AIによって、諦めかけていたことや、やりたいと思っていたことの数が飛躍的に増えた。少なくともコンピュータで表現するということにおいては。年を取った人も、お金がなくて勉強するチャンスがない人も、僕みたいに物を覚えることが苦手な人も、すごく救われたんじゃないかと思う。

本当はこういうものはインフラ化して、誰もが平等に使えるようになるのが一番なんだろうけど、知っての通り、アメリカは戦争に使おうとしているし、企業同士がバチバチやり合っている。まあ、どこまで本当でどこまで嘘か知らないよ。だけど、そんなことやっている人類なら滅んじゃってもいいんじゃないかと個人的には思う。なぜ人類だけが生き残れると思っているんだ、というのが正直な気持ちだ。

でも、よくAIはいろんな情報のベクトルだという人がいる。人類は滅びたくないと思っている。滅びたくないと思っている割には、宗教的対立、信念的対立で人が死んでも構わないようなことを平気でやるわけだけど。人間が滅びたくないと思っているのだとしたら、その情報を集めたAIも、人間は滅びたくないんだと思ってくれているんじゃないかと、ちょっとだけ思う。そんなことないのかもしれないけど。命令一つでミサイルだって撃てるわけだし。

2025年の9月くらいから、僕は本格的にAIをメインにいろいろ活動するようになった。自分のやることがより上流に向かっていって、その分、正直大変になった。AIを使ってものを作っている方が、それ以前より大変だという感覚がある。自分以外のものに正しく動いてもらうというのは、おかげさまで社長業を36歳くらいからやらせてもらっているけど、人もなかなか話が通じないし、AIも負けず劣らず通じない。通じるようにしていくのは上流工程にいる人間の責務であり、僕の仕事だと思う。

AIを使うことでクリエイティビティが損なわれるとか、そういう言説は軽蔑する。人間が暮らすというのはそんな綺麗事じゃない。AIは道具で、人間は幸せになりたいと思っている以上、道具をどう使うかが人間の主題だ。それによってクリエイティブでないなんてことはありえない。体を使う喜びは人間側にいつまでも残り続けるだろうし、不得意なことを得意なものにやってもらえるのはいいことだと思う。

大丈夫、そう簡単に仕事も奪われない。AIを使ってコンテンツを乱造しても、いいものなんかできない。だって考えていないんだから。いいものを作ろうと思ったら、考えなきゃいけないし、勉強しなきゃいけない。昔、サウンド&レコーディング・マガジンで山下達郎さんがいいことを言っていた。「3コードで書ける曲には限界がある。3コードで書けるのはせいぜい数曲だ。だから僕は音楽の勉強をする。研究をする」。アプリケーションだろうとWebサービスだろうと、同じことだ。

AIと暮らしていく世界がやってきて、AIと暮らす季節が始まった。その中で自分がどう勉強するか、どう振る舞うかを考えていかないといけないんだろうなと思う。残念ながら僕はもういい年なので、最前線で頑張れるのはそんなに長くないだろうけど、やれるだけのことをやっていくつもりだ。若い人たちは、ここから先、その季節を前提に満喫しなければいけない。

お互い頑張りましょう。たくさん勉強をしましょう。

---

*付記：この文章は、筆者が口述した内容をClaude Codeとともにブログ記事としてまとめ、著者が加筆修正したものである。すべての内容は筆者が確認した上で公開しており、文章に対する一切の責任は筆者個人に帰属する。*

</div>

<div lang="en" markdown="1">

This February was incredibly busy with work. I'd been working on a project since last September that was scheduled to wrap up around the beginning of March, and in the meantime I was doing live performances with my jazz band and also performing with [OrbitScore](https://github.com/signalcompose/orbitscore), a live coding tool I built myself. Well, if it were just me challenging myself with my own stuff, that's simply a matter of my own responsibility, stamina, and resources. Just me doing what I do.

Then, in December last year, my mother collapsed. As far as these things go, she was relatively lucky, but she did end up with some real physical impairments. However, her cognitive abilities, memory, speech — none of that was damaged. She can communicate fine, and her cognition is intact. She's currently in a rehabilitation hospital doing rehab. Since we can talk when I visit, my younger brother and I take turns visiting her, bringing the coffee she looks forward to. My mother is a modern person — sophisticated, you might say — so she can follow pretty much any conversation. Work talk, AI talk, music talk. Right now, we're talking about how she had tickets to see Snarky Puppy in May, bought before she collapsed — she has a ticket too — and we keep saying, "Let's go see that show." That's what's motivating her through rehab.

Right now, I'm staying at a company space I'm renting right near my parents' house. I've moved out of the family home, but it's about a 30-second walk away, so I can check in if anything happens. That said, since I wasn't normally living there, I had no idea what kind of life my brother and father had been living together. It turned out that my father was showing signs of dementia — he'd never been diagnosed with it before — and it had gotten to the point where he was putting a significant burden on my brother. My brother was clearly struggling, so I stepped in. I talked to people at the local care plaza, and while I'd already filed my mother's care application right after she was hospitalized, on the care plaza staff's advice, I filed one for my father too. I'd been doing my best playing the big brother role for a while. This was not as light a task as you might think. It's work that involves people's emotions, so it was genuinely tough. Those news stories about caregivers killing their parents out of exhaustion — I started to truly feel how that happens.

I told my clients the situation: "Some of my time is going to be taken up by this." But from the client's perspective, it's really a case of "dealing with that is your problem" — not that they'd ever say that; my clients are incredibly good people — but I have to think of it that way. I explained the situation to my employees too and got their cooperation, and between visiting my mother, supporting my brother, and backing everyone up, I had to keep pushing work forward.

In times like these, I was truly grateful that the era of writing programs with generative AI had arrived. Looking back, right after my mother collapsed and when we were figuring out my father's care certification, I was asking ChatGPT things, compiling what steps were available in Yokohama, turning it into documents to show my mother and brother, getting things organized so we could handle them step by step. Someone had to do the work, so the person most capable of doing it did what needed to be done. I wasn't exactly calm about it, but the person who could do the work just did the work.

When it comes to writing programs with AI — in terms of raw ability, AI is already completely better at writing programs than I am. The program called OrbitScore that I used in my live coding performance the other day — I didn't write a single line of code. What I did was create the language specification for a DSL — a domain-specific language. I created a language specification that defines the music I want to make, and then I wrote the spec document for it. Then I had the AI do the programming. As long as the information is computer-readable, today's generative AI can get you pretty far. But you also have to give it precise instructions.

This article, too, was created by me dictating it and then editing afterward. It's not that I dislike writing, but I decided to change my approach. Actually, this is the second attempt — the first time, it wrote a ton of lies. Somehow my parents' house ended up in Nagoya, I was supposedly working in Tokyo — it was so full of nonsense that I scrapped the entire article. I'm hoping that doesn't happen this time. I'm also rewriting it myself as I go.

So how do you get AI to work for you? In the end, it comes down to writing good proposals together, creating good spec documents, thinking through and deciding on the tech stack, and then firmly building guardrails around your development style — documentation-driven development, TDD, DRY, Git flow, always writing Issues — and making sure it's all properly documented. I think this is what's considered ideal even when working between humans.

Can you do TDD ideally? Honestly, I think it's impossible to execute perfectly with human resources alone. I have a friend who's an incredibly talented engineer, so I'm a little scared of getting rocks thrown at me for saying this, but I think anyone who can write every test and implement everything perfectly within client work must be some kind of superman. It's tough at my skill level. But when you use AI, this style becomes crucial for getting the AI to work correctly. Documentation is the single source of truth. From there, you create issues, write red tests, implement, and continue until you get green tests. Even when using AI with its limited context, this approach keeps development on track when context gets lost.

Every time Conversation Compacting happens while I'm using Claude Code, the AI forgets things. "Forgot this rule, forgot that rule." Each time, I tell it to remember. Lately, when I'm talking with my father, I sometimes think, "He's kind of like an AI." Honestly, I don't need better program performance — I just want them to fix AI's long-term memory problem already. To work around that, I use documentation-driven development and other techniques, and depending on the project, I make it write work logs with every commit. I think everyone has their own workarounds, and I believe this will improve over time.

You often see claims that AI undermines creativity, or that it'll steal human jobs, or even that humanity will go extinct. But when you actually use AI in your daily life like this, it's a useful tool, and what this tool makes possible is so enormous that I think it's impossible to walk away from it. Even if only a few percent of people are using it so far.

I first touched the internet when I was probably around 20. As a teenager, it was grassroots BBS. When the internet came along, an irreversible revolution happened. I think that was a revolution on the level of the Industrial Revolution. After that, Mochio Umeda's *[Web Shinkaron (Web Evolution Theory)](https://amzn.asia/d/0fEXlJf2)* came out and was a big hit. When I read it, I had a thought. The book said things like "national borders will disappear," but frankly, I thought, "This is incredibly naive." The first thing that came to my mind when I read it was, "This is going to create a gap between the haves and the have-nots." Now, the same thing is about to happen with AI.

Anthropic, which provides Claude Code, casually offers six free months to people who contribute to open source. I thought that was a pretty crude and unpleasant form of elitism. Of course, I wasn't doing that kind of work myself so I can't really complain, and maybe it's just jealousy, but it makes me wonder if that's really what the possibilities and opportunities AI brings are all about. Whether it's OpenAI, Anthropic, or Alibaba — they're all for-profit companies, so I suppose it can't be helped.

I'm turning 56 this year. Thankfully, my body is healthy and my mind still works. If I have any advantage over younger people, it's the experience of having seen and heard a lot of things. I'm an old veteran, to put it bluntly. Old veterans have their own way of fighting, and AI has made it possible to leverage that advantage. A few years ago, I'd reached the age where I could calculate the number of things I'd be able to create in my remaining lifetime. I was prioritizing what to make, counting on my fingers how few things I could still get done. I'm running a company too, so I can't pour all my resources into creative work. But with Claude Code and generative AI, the number of things I'd nearly given up on, the things I wanted to do — that number has grown dramatically. At least when it comes to expression through computers. I think people who've gotten older, people who can't afford the chance to study, people like me who are bad at memorizing things — we've all been given a real lifeline.

Ideally, this kind of thing would become infrastructure that everyone can use equally. But as you know, the U.S. is trying to use it for war, and companies are going at each other's throats. Well, I don't know how much of that is true and how much is lies. But if that's what humanity is going to do with it, maybe it's fine if we go extinct. Why do we assume only humans deserve to survive? That's how I honestly feel.

But people often say AI is just a vector of various information. Humanity doesn't want to go extinct. For a species that doesn't want to go extinct, we sure don't seem to mind people dying over religious conflicts and ideological clashes. But if humans don't want to go extinct, then maybe, just maybe, the AI that's been trained on all that information also thinks humans don't want to go extinct. Maybe not, though. After all, a single command can launch a missile.

Starting around September 2025, I began seriously centering my activities around AI. My work shifted further upstream, and honestly, it got harder. I have the sense that making things with AI is more demanding than it was before. Getting something other than yourself to work correctly — I've been fortunate to run a company since I was about 36, but people are often hard to communicate with, and AI is every bit as difficult. Making yourself understood is the responsibility of the person working upstream, and I believe that's my job.

I have contempt for the claim that AI undermines creativity. Human life is not that clean and tidy. AI is a tool, and as long as humans want to be happy, how we use our tools is the central question of being human. There's no way that makes us less creative. The joy of using our bodies will always remain on the human side, and I think it's a good thing to let something skilled handle what we're not good at.

Don't worry — jobs won't be stolen that easily either. Mass-producing content with AI won't make anything good. Because there's no thought behind it. If you want to make something good, you have to think, and you have to study. A long time ago, Tatsuro Yamashita said something great in Sound & Recording Magazine: "There's a limit to songs you can write with three chords. You can write maybe a few songs with three chords. That's why I study music. That's why I do research." Whether it's an application or a web service, the same thing applies.

A world of living with AI has arrived, and the season of living with AI has begun. Within it, I think we need to consider how we study, how we conduct ourselves. Unfortunately, I'm already getting on in years, so I probably can't stay on the front lines for much longer. But I intend to do everything I can. Young people — from here on out, you need to fully embrace this season as a given.

Let's do our best, all of us. Let's study hard.

---

*Postscript: This text was composed as a blog post together with Claude Code based on the author's dictation, with additions and revisions by the author. All content has been reviewed by the author before publication, and sole responsibility for the text lies with the author.*

</div>
