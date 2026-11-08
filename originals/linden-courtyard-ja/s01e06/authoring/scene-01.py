# Authoring module for linden-courtyard-ja-s01e06-scene-01.
ID = 'linden-courtyard-ja-s01e06-scene-01'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 6
SCENE = 1
TITLE = 'At the Iron Gate  (鉄の門のそばで)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'caleb': 'Caleb', 'owen': 'Owen', 'hannah': 'Hannah'}
INTRO = 'ハンナが中庭のテーブルへ熱い紅茶を運んでくる中、ケイレブは教わった三つの短い文を口にします。兄のオーウェンは、絵はがきの字を見た瞬間に弟だとわかっていたと打ち明け、三年間会いたかったのは自分も同じだと微笑みます。まずは場面全体を英語で聴いてみましょう。'
OPENER = '兄弟がゆっくりと距離を縮めていく会話を、一行ずつ丁寧に味わっていきましょう。'
TRANSITION = 'それでは、仲直りの場面をもう一度ふつうの速さで通して聴いてみましょう。'
OUTRO = '三年分のわだかまりは、ほんの数分で溶けてしまいました。次はいよいよ、祖父の工房から来た古い青い鞄を開ける番です。それではまたすぐに、次の場面でお会いしましょう。'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('owen', "So 'someone with something from Grandfather' was you all along, Caleb.", 'じゃあ「祖父のものを持っている誰か」っていうのは、最初からずっとお前だったんだな、ケイレブ。'),
    ('caleb', 'Hello, Owen. Thank you for coming today.', 'やあ、オーウェン。今日は来てくれてありがとう。'),
    ('owen', 'I recognized your neat block handwriting on that postcard in two seconds.', 'あの絵はがきのきちんとした活字体の字、二秒でお前のだとわかったよ。'),
    ('caleb', 'Wait, you knew it was from me and came anyway?', '待って、僕からだとわかっていて、それでも来てくれたの？'),
    ('owen', 'Of course I came. Why did you hide behind a mystery note?', 'もちろん来たさ。どうして謎めいた書き置きなんかに隠れたんだ？'),
    ('caleb', 'Because I was afraid you were still angry. I missed you these three years.', 'まだ怒っているんじゃないかと怖かったんだ。この三年間、ずっと会いたかった。'),
    ('owen', 'Three stubborn years... honestly, little brother, I missed you too.', '意地を張り合った三年か…正直に言うとな、弟よ、俺も会いたかったよ。'),
    ('hannah', 'Excuse me, gentlemen. Here is hot tea, and warm lemon cake is on the way.', '失礼いたします、お二人とも。熱い紅茶をどうぞ。温かいレモンケーキもすぐにお持ちしますね。'),
    ('owen', 'Lemon cake? Wait, how did she know about Friday lemon cake?', 'レモンケーキ？待てよ、金曜日のレモンケーキのこと、どうして彼女が知ってるんだ？'),
    ('caleb', 'Sit down, Owen, take off your heavy coat, and look at this blue suitcase.', '座ってよ、オーウェン。その重いコートを脱いで、この青いスーツケースを見て。'),
    ('owen', "Is that the old dark blue bag from Grandfather's workshop?", 'それって、祖父の工房にあった古い紺色の鞄じゃないか？'),
    ('hannah', 'Take all the time you need. The courtyard is yours.', 'どうぞ、ごゆっくりなさってください。中庭はお二人だけのものですから。'),
]
WALK = [
    (0, None, ["'じゃあ「祖父のものを持っている誰か」っていうのは、最初からずっとお前だったんだな、ケイレブ。' 謎の正体がわかった瞬間の決まり文句が", (None, 'was you all along'), 'です。最後に置かれた副詞句は「始めから終わりまでずっと」という意味で、気づかなかった驚きをにじませます。']),
    (1, None, ["'やあ、オーウェン。今日は来てくれてありがとう。' ハンナに教わった短い文の一つめが", (None, 'Thank you for coming today'), 'です。前置詞の後ろでは動詞に語尾を付けた形を使い、来てくれた行為そのものに感謝します。']),
    (2, None, ["'あの絵はがきのきちんとした活字体の字、二秒でお前のだとわかったよ。' 名詞の前に形容詞を重ねた", (None, 'neat block handwriting'), 'に注目しましょう。ここでの形容詞は続け字ではなく、一文字ずつ離して書く大文字風の字を指します。']),
    (3, None, ["'待って、僕からだとわかっていて、それでも来てくれたの？' 文末にぽんと置かれる", (None, 'anyway'), 'は、事情があっても結局そうした、という気持ちを表します。日本語の「それでも」や「結局」にあたる便利な副詞です。']),
    (4, None, ["'もちろん来たさ。どうして謎めいた書き置きなんかに隠れたんだ？' 迷いのない返事が", (None, 'Of course I came'), 'です。相手の不安を打ち消すときは、前置きなしに過去形でこう言い切ると気持ちがまっすぐ伝わります。']),
    (5, None, ["'まだ怒っているんじゃないかと怖かったんだ。この三年間、ずっと会いたかった。' 怖かった内容を後ろに続ける", (None, 'I was afraid you were'), 'では、主節が過去なので従属節の動詞も過去形にそろえます。日本語の「怒っている」とは時制の扱いが違う点に気をつけましょう。']),
    (6, None, ["'意地を張り合った三年か…正直に言うとな、弟よ、俺も会いたかったよ。' 年下のきょうだいへの親しみを込めた呼びかけが", (None, 'little brother'), 'です。英語には「弟」という一語がないため、形容詞を添えて年下であることを示します。']),
    (7, None, ["'失礼いたします、お二人とも。熱い紅茶をどうぞ。温かいレモンケーキもすぐにお持ちしますね。' 物がこちらへ向かっている途中だと伝える", (None, 'is on the way'), 'は、料理や荷物がもうすぐ届くときの定番表現です。道の途中にある、という発想で覚えましょう。']),
    (8, None, ["'レモンケーキ？待てよ、金曜日のレモンケーキのこと、どうして彼女が知ってるんだ？' 驚きの疑問文", (None, 'how did she know about'), 'では、前置詞が知っている話題を導きます。「…について知る」という形で、事情を知っていることを表します。']),
    (9, None, ["'座ってよ、オーウェン。その重いコートを脱いで、この青いスーツケースを見て。' 身につけた服を脱ぐときは句動詞", (None, 'take off your heavy coat'), 'を使います。反対に着るときは別の句動詞になるので、対にして覚えると便利です。']),
    (10, None, ["'それって、祖父の工房にあった古い紺色の鞄じゃないか？' 所有を表すアポストロフィの形で", (None, "Grandfather's workshop"), 'と言っています。家族の呼び名を大文字で始めると、固有名詞のように特定の祖父を指す響きになります。']),
    (11, None, ["'どうぞ、ごゆっくりなさってください。中庭はお二人だけのものですから。' 相手を急がせない丁寧な決まり文句が", (None, 'Take all the time you need'), 'です。名詞の後ろに関係詞を省いた節が続き、「あなたが必要とする時間すべて」という意味になります。']),
]
