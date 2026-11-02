ID = 'the-naked-director-s01e01-scene-15'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 15
TITLE = '一日百円です  (One Hundred Yen a Day)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'ono': '小野', 'muranishi': '村西', 'customer': '客'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Outside Nakai's mansion, Ono bursts out laughing—the last salesman who visited that house ended up in the hospital! "
    "Fired up by his breakthrough, Muranishi develops his own passionate style, turning a three-thousand-yen monthly fee into a hundred yen a day. "
    "Listen to Muranishi find his voice."
)

STORY = [
    ('ono', 'やるじゃないか！', 'Well, look at you go!', [(344, 'やるじゃ')], 'Standardised やるじゃねえか to やるじゃないか.'),
    ('muranishi', '知ってたなら教えてくださいよ！', 'If you knew, you should have told me!', [(347, '知ってたなら 教えてくださいよ')], ''),
    ('ono', '愛情だよ。一人前のセールスマンになれる。', 'Call it tough love. You can become a full-fledged salesman.', [(348, '愛情だよ'), (351, '一人前のセールスマンになれる')], ''),
    ('muranishi', '英会話の必要性を感じますか？', 'Do you feel the need for English conversation?', [(352, '英会話の必要性を')], 'Simplified honorific verb to polite 感じますか.'),
    ('customer', '俺には必要ないね。', 'I do not need it.', [(353, '俺には必要ないね')], ''),
    ('muranishi', 'わたくしはそのようには考えません。', 'I do not see it that way.', [(355, 'わたくしは そのようには考えません')], ''),
    ('muranishi', '一日十五分、三か月続けてみてください。', 'Please try keeping at it fifteen minutes a day for three months.', [(370, '続けてみてください')], 'Wrote 一日十五分 and 三か月 in kanji.'),
    ('muranishi', 'あなた様に人生を諦めてほしくないのです。', 'I do not want you to give up on your life.', [(375, 'あなた様に 人生を諦めてほしくないのです')], ''),
    ('customer', 'でもさ、少し高くない？', 'Still, is it not a little expensive?', [(376, 'でもさ 少し高くない')], ''),
    ('muranishi', '確かに少し高いと感じるかもしれません。', 'Certainly, it might feel a little expensive.', [(377, '確かに'), (378, '少し高いと感じ'), (378, 'かもしれません')], ''),
    ('muranishi', '月三千円ということは一日百円です。', 'Three thousand yen a month means one hundred yen a day.', [(383, 'ということは')], 'Wrote 三千円, 一日, and 百円 in kanji.'),
    ('muranishi', '高いどころか安すぎると思っております。', 'Far from being expensive, I believe it is way too cheap.', [(387, '高いどころか 安すぎると思っております')], ''),
]

OPENER = "Watch how Muranishi agrees politely with a customer's objection before flipping the price upside down."

WALK = [
    (0, None, "'Well, look at you go!' Literally \"yaru ja nai ka\" asks 'do you not do well?', an idiomatic pat on the back meaning 'hey, not bad at all!'"),
    (1, None, "'If you knew, you should have told me!' \"Shitteta nara\" means 'if you knew', followed by \"oshiete kudasai yo\", 'please tell me!' with an exasperated \"yo\"."),
    (2, '一人前のセールスマンになれる。', "'You can become a full-fledged salesman.' \"Ichininmae\" literally counts 'one full person's portion'—used in sushi shops for one serving and at work for a professional who stands on their own feet."),
    (4, None, "'I do not need it.' Adding \"ni wa\" onto casual \"ore\", me, draws a line: 'as for me, there is no need', \"hitsuyou nai\"."),
    (6, None, "'Please try keeping at it fifteen minutes a day for three months.' \"Ichinichi juugofun\" sets the pace at fifteen minutes per day, and \"tsuzukete mite kudasai\" attaches \"mite\", try and see, to \"tsuzukeru\", to continue."),
    (7, None, "'I do not want you to give up on your life.' \"Jinsei\" means a human lifetime, and \"akirameru\" means to give up. Gluing \"hoshikunai\" onto \"akiramete\" expresses 'I want you not to give up'."),
    (8, None, "'Still, is it not a little expensive?' Customers everywhere ask \"sukoshi takakunai\" with a rising lilt—turning \"takai\", expensive, negative to nudge 'a bit pricey, right?'"),
    (9, None, "'Certainly, it might feel a little expensive.' Never argue head-on: Muranishi opens with \"tashika ni\", certainly, and cushions the thought with \"kamoshiremasen\", 'it might be'."),
    (10, None, "'Three thousand yen a month means one hundred yen a day.' \"Tsuki sanzen-en\" is three thousand yen a month; \"to iu koto wa\" bridges neatly into what that really means—\"ichinichi hyaku-en\", a hundred yen a day!"),
    (11, None, "'Far from being expensive, I believe it is way too cheap.' Placing \"dokoroka\" right after \"takai\" flips the claim completely—'far from expensive!'—and lands on \"yasusugiru\", built from \"yasui\", cheap, plus \"sugiru\", too much."),
]

TRANSITION = "Now let's listen to Muranishi's price-flipping pitch again."

OUTRO = (
    "Remember \"takai\" for expensive, \"yasui\" for cheap, \"mite kudasai\" to invite someone to try something, "
    "and \"to iu koto wa\" whenever you reframe numbers in your favour. "
    "See you in scene sixteen."
)

CLOSING = ('muranishi', 'さようなら。')
