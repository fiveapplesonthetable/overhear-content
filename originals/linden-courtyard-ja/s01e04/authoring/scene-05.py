# Authoring module for linden-courtyard-ja-s01e04-scene-05.
ID = 'linden-courtyard-ja-s01e04-scene-05'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 4
SCENE = 5
TITLE = 'Five-Star Showers  (五つ星のシャワー)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'arthur': 'Arthur', 'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = '雨上がりの朝、ぐっすり眠れたケイレブが上機嫌で朝食に下りてきます。熱いシャワーをほめられたアーサーは舞い上がり、つい点数や旅行ガイドの話を口にしてしまいます。ところが、どうやら大きな勘違いがあったようです。まずは英語で場面を聴いてみましょう。'
OPENER = 'それでは、すれ違う会話のおかしさを一行ずつ味わっていきましょう。'
TRANSITION = '最後に、もう一度通しで自然な速さの英語を聴いてみてください。'
OUTRO = 'ケイレブはホテルの調査員ではありませんでした。本当の仕事を見せるため、みんなを中庭へ誘います。続きは菩提樹の下で。どうぞお元気で。'
CLOSING = ('caleb', 'Take care!')
STORY = [
    ('caleb', 'Good morning, Hannah! Good morning, sir! What a bright morning after the rain.', 'おはよう、ハンナ！おはようございます！雨上がりの、なんて明るい朝でしょう。'),
    ('hannah', 'Good morning, Caleb! Did you sleep well under the roof beams?', 'おはようございます、ケイレブさん！屋根の梁の下でよく眠れましたか？'),
    ('caleb', 'Best sleep I have had all month, and the shower water was wonderfully hot!', '今月いちばんの眠りでしたよ。それにシャワーのお湯が最高に熱かった！'),
    ('arthur', 'Hot! Hear that, Hannah? Reliable, modern, five-star hot water!', '熱い！聞いたかい、ハンナ？頼もしくて、最新式で、五つ星のお湯だ！'),
    ('caleb', 'Old brick buildings usually take ages to warm up on the top floor.', '古いレンガの建物は、たいてい最上階が温まるまでずいぶん時間がかかるんですけどね。'),
    ('arthur', "Please write that down! 'Hot water on the third floor: ten out of ten!'", 'ぜひそれを書き留めてください！『三階の熱いお湯、十点満点中十点！』'),
    ('caleb', 'Excuse me? Ten out of ten?', 'はい？十点満点中十点？'),
    ('hannah', 'What Arthur means is... we hope every guest feels ten out of ten here!', 'アーサーが言いたいのは…お客さま全員にここで十点満点の気分になってほしい、ということなんです！'),
    ('arthur', 'No, Hannah, let us be honest professionals! Sir, we respect the Portland Travel Guide!', 'いや、ハンナ、正直なプロでいようじゃないか！お客さま、私どもはポートランド旅行ガイドを尊敬しております！'),
    ('caleb', 'The Portland Travel Guide? Wait, do you think I am a hotel inspector?', 'ポートランド旅行ガイド？待って、私をホテルの調査員だと思っているんですか？'),
    ('hannah', "When your notebook fell open on the counter last night, we saw 'nine out of ten'...", '昨夜、あなたのノートがフロントで開いてしまったとき、『十点中九点』という文字が見えたんです…'),
    ('caleb', 'Oh! Come outside to the courtyard for a minute. Let me show you what I really do!', 'ああ！ちょっと中庭まで出てきてください。私が本当は何をしているのか、お見せしますよ！'),
]
WALK = [
    (0, None, ["'おはよう、ハンナ！おはようございます！雨上がりの、なんて明るい朝でしょう。' 感嘆文は疑問文と違い、主語と動詞を入れ替えずに", (None, 'What a bright morning'), 'のように、名詞のまとまりの前に感嘆の語を置くだけで作れます。']),
    (1, None, ["'おはようございます、ケイレブさん！屋根の梁の下でよく眠れましたか？' 宿の朝の定番のあいさつが", (None, 'Did you sleep well'), 'です。過去のことを尋ねるので助動詞は過去形になり、続く動詞は原形に戻ります。']),
    (2, None, ["'今月いちばんの眠りでしたよ。それにシャワーのお湯が最高に熱かった！' 最上級の名詞のあとに現在完了を続けた", (None, 'Best sleep I have had'), 'は、今までの経験の中で一番という意味になります。さらに副詞を添えた', (None, 'wonderfully hot'), 'で、形容詞を生き生きと強めています。']),
    (3, None, ["'熱い！聞いたかい、ハンナ？頼もしくて、最新式で、五つ星のお湯だ！' 会話では主語と助動詞を省いて", (None, 'Hear that'), 'とだけ言うことがよくあります。また', (None, 'five-star hot water'), 'のように、数詞と名詞をハイフンでつなぐと形容詞になり、複数形の語尾はつきません。']),
    (4, None, ["'古いレンガの建物は、たいてい最上階が温まるまでずいぶん時間がかかるんですけどね。' 口語の慣用句", (None, 'take ages'), 'は、何年もかかるかのように大げさに言う表現です。動詞の', (None, 'warm up'), 'も、副詞がつくことで「すっかり温まる」という感じが出ます。']),
    (5, None, ["'ぜひそれを書き留めてください！『三階の熱いお湯、十点満点中十点！』' 句動詞", (None, 'write that down'), 'では、目的語が代名詞のとき、必ず動詞と副詞のあいだにはさみます。点数の言い方', (None, 'ten out of ten'), 'も覚えておきましょう。']),
    (6, None, ["'はい？十点満点中十点？' 語尾を上げて言う", (None, 'Excuse me'), 'は、謝罪ではなく、聞き返しや戸惑いを表しています。同じ言葉でも、声の調子で意味が変わる好例です。']),
    (7, None, ["'アーサーが言いたいのは…お客さま全員にここで十点満点の気分になってほしい、ということなんです！' 関係代名詞を使った", (None, 'What Arthur means is'), 'は、誰かの発言を言い直してとりつくろうときの便利な前置きです。']),
    (8, None, ["'いや、ハンナ、正直なプロでいようじゃないか！お客さま、私どもはポートランド旅行ガイドを尊敬しております！' 提案の", (None, 'let us be honest professionals'), 'は、普段は短縮形で言うところを、あえて省略せずに言うことで、堅苦しく芝居がかった響きになっています。']),
    (9, None, ["'ポートランド旅行ガイド？待って、私をホテルの調査員だと思っているんですか？' 相手の誤解を確かめる", (None, 'do you think I am a hotel inspector'), 'では、疑問文の中に続く部分がふつうの語順のままになる点に注意しましょう。']),
    (10, None, ["'昨夜、あなたのノートがフロントで開いてしまったとき、『十点中九点』という文字が見えたんです…' 動詞と形容詞を組み合わせた", (None, 'fell open'), 'は、落ちた結果として開いた状態になった、という一続きの動きを短く表しています。']),
    (11, None, ["'ああ！ちょっと中庭まで出てきてください。私が本当は何をしているのか、お見せしますよ！' 許可を求める形の", (None, 'Let me show you'), 'は、自分から進んで何かを見せたいときの親しみのある申し出です。続く部分も疑問文の語順にはなりません。']),
]
