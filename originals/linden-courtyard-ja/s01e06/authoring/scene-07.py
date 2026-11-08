# Authoring module for linden-courtyard-ja-s01e06-scene-07.
ID = 'linden-courtyard-ja-s01e06-scene-07'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 6
SCENE = 7
TITLE = 'Under the Golden Lanterns  (金色のランタンの下で)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'owen': 'Owen'}
INTRO = '日が暮れて、中庭にはランタンの柔らかな光が広がっています。ハンナとイヴリンとオーウェンは、この一週間に生まれた思いがけない友情に乾杯します。耳を澄ませて、英語の会話を聴いてみましょう。'
OPENER = 'では、穏やかな夜のひとときを一文ずつ味わっていきましょう。'
TRANSITION = 'ここで、乾杯までの流れを通しでもう一度聴きます。'
OUTRO = 'にぎやかで静かな宿に、温かい乾杯の声が響きました。次の場面では、地下室から不思議な箱が見つかります。'
CLOSING = ('evelyn', 'Good night!')
STORY = [
    ('evelyn', 'Look up at those golden lanterns against the evening sky. How peaceful!', '夕暮れの空に浮かぶあの金色のランタンを見上げて。なんて穏やかなの！'),
    ('owen', 'To think on Monday morning Caleb picked up the wrong blue bag on Platform Two.', '月曜日の朝に、ケイレブが二番ホームで間違った青いかばんを持っていったなんてね。'),
    ('hannah', 'If he had picked up the right bag, none of us would be standing here tonight!', 'もし彼が正しいかばんを取っていたら、今夜ここに立っている人は誰もいなかったわ！'),
    ('evelyn', 'My teacup survived, two brothers made peace, and Hannah found a new home.', '私のティーカップは無事で、兄弟は仲直りし、ハンナは新しい居場所を見つけたのね。'),
    ('owen', 'Miss Evelyn, Caleb and I booked a quiet dinner nearby. Will you join us tomorrow?', 'イヴリンさん、ケイレブと私で近くの静かなお店に夕食を予約しました。明日ご一緒しませんか？'),
    ('evelyn', 'Gladly, Owen, as long as nobody talks about selling old pianos!', '喜んで、オーウェン。古いピアノを売る話を誰もしないならね！'),
    ('hannah', 'And tomorrow morning at eight, your first courtyard coffees are on the house!', 'それに明日の朝八時、皆さんの最初の中庭コーヒーはお店のおごりです！'),
    ('owen', "We will bring half of City Hall to Tessa's tables next week, I promise.", '来週は市役所の半分をテッサのテーブルに連れてきますよ。約束します。'),
    ('evelyn', 'Listen, even the buzzer from room four has been quiet all evening!', '聞いて、四号室のブザーまで、今夜はずっと静かよ！'),
    ('hannah', 'Do not tempt it, Miss Evelyn! I am almost fond of those two rings now.', '縁起でもないこと言わないで、イヴリンさん！今ではあの二回の呼び鈴がちょっと愛おしいくらいなんです。'),
    ('owen', 'Here is to the Linden Courtyard Inn, the loudest quiet place in Portland!', 'リンデン・コートヤード・インに乾杯。ポートランドで一番にぎやかな静かな場所に！'),
    ('hannah', 'To good neighbors, warm bread, and open gates!', '良き隣人と、温かいパンと、開かれた門に！'),
]
WALK = [
    (0, None, ["'夕暮れの空に浮かぶあの金色のランタンを見上げて。なんて穏やかなの！' 目線を上に向ける", (None, 'Look up at'), 'は、“上へ”の副詞と対象を示す前置詞を組み合わせた句動詞です。感嘆文の', (None, 'How peaceful'), 'も覚えておきましょう。']),
    (1, None, ["'月曜日の朝に、ケイレブが二番ホームで間違った青いかばんを持っていったなんてね。' 振り返って驚く", (None, 'To think'), 'は、不定詞だけで文を始める感嘆の言い方です。また', (None, 'picked up the wrong blue bag'), 'では形容詞が冠詞と色の間に入ります。']),
    (2, None, ["'もし彼が正しいかばんを取っていたら、今夜ここに立っている人は誰もいなかったわ！' 過去の事実に反する仮定の", (None, 'If he had picked up the right bag'), 'は過去完了を使います。結果の', (None, 'none of us would be standing here'), 'は今の状況なので形が変わります。']),
    (3, None, ["'私のティーカップは無事で、兄弟は仲直りし、ハンナは新しい居場所を見つけたのね。' 和解を表す", (None, 'made peace'), 'は、“平和を作る”と直訳できる定番の言い回しです。“家”を使った', (None, 'found a new home'), 'は建物ではなく心の拠り所を指しています。']),
    (4, None, ["'イヴリンさん、ケイレブと私で近くの静かなお店に夕食を予約しました。明日ご一緒しませんか？' 予約を表す動詞の", (None, 'booked a quiet dinner'), 'は“本”と同じ綴りの語です。誘いの', (None, 'Will you join us tomorrow'), 'も丁寧で自然な言い方です。']),
    (5, None, ["'喜んで、オーウェン。古いピアノを売る話を誰もしないならね！' 快く応じる", (None, 'Gladly'), 'は一語で丁寧な承諾になります。条件の', (None, 'as long as nobody talks about'), 'は「〜さえしなければ」という意味の接続表現です。']),
    (6, None, ["'それに明日の朝八時、皆さんの最初の中庭コーヒーはお店のおごりです！' 無料であることを伝える", (None, 'on the house'), 'は飲食店でよく使う慣用句です。直訳の「家の上に」とはまったく違う意味になります。']),
    (7, None, ["'来週は市役所の半分をテッサのテーブルに連れてきますよ。約束します。' 大勢を連れてくることを誇張する", (None, 'half of City Hall'), 'では、建物の名前で働く人々全体を表しています。文末の', (None, 'I promise'), 'で言葉に重みが加わります。']),
    (8, None, ["'聞いて、四号室のブザーまで、今夜はずっと静かよ！' 意外さを強める副詞の", (None, 'even the buzzer'), 'に注目しましょう。続く', (None, 'has been quiet all evening'), 'は現在完了で、今まで続いている状態を表しています。']),
    (9, None, ["'縁起でもないこと言わないで、イヴリンさん！今ではあの二回の呼び鈴がちょっと愛おしいくらいなんです。' 不吉なことを口にするなという", (None, 'Do not tempt it'), 'は、運命を挑発するなという英語の発想です。好意を表す', (None, 'almost fond of'), 'も便利な表現です。']),
    (10, None, ["'リンデン・コートヤード・インに乾杯。ポートランドで一番にぎやかな静かな場所に！' 乾杯の決まり文句", (None, 'Here is to'), 'の後ろには祝う対象を置きます。続く', (None, 'the loudest quiet place'), 'は反対の意味の語を並べた、ユーモアのある言い方です。']),
    (11, None, ["'良き隣人と、温かいパンと、開かれた門に！' 乾杯の続きとして前置詞だけで始まる", (None, 'To good neighbors'), 'は、乾杯の決まり文句を省略した形です。形容詞としての', (None, 'open gates'), 'は、“開ける”と同じ語がそのまま形容詞になっている例です。']),
]
