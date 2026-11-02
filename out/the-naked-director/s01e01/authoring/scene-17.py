ID = 'the-naked-director-s01e01-scene-17'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 17
TITLE = 'もっと広い家に引っ越そう  (Let Us Move to a Bigger House)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mayumi': '真由美', 'muranishi': '村西', 'sachiko': '幸子'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "From zero contracts to number one in the entire company, Muranishi comes home beaming with his sales award. "
    "Over dinner he promises toys to the children and a bigger home to his wife Sachiko. "
    "Listen to the family celebrate."
)

STORY = [
    ('muranishi', '今月の営業成績は一位だったぞ！', 'My sales record this month was number one!', [(427, '今月の営業成績')], 'Adapted president’s award announcement into Muranishi’s proud report at home; wrote 一位 in kanji.'),
    ('mayumi', '本当に？信じられない！', 'Really? I cannot believe it!', [(432, '本当に 信じられない')], ''),
    ('muranishi', '今度リカちゃんハウスを買ってやる。', 'Next time I will buy you a Licca-chan dollhouse.', [(433, '今度リカちゃんハウス'), (434, '買ってやる')], ''),
    ('mayumi', '絶対約束だからね！', 'That is an absolute promise, okay!', [(436, '絶対 約束だからね')], ''),
    ('muranishi', '大輔にはカウンタックのラジコンを買ってやる。', 'For Daisuke, I will buy a remote-control Countach car.', [(437, '大輔 カウンタックの ラジコン買ってやる')], 'Added には and を for clear A1 structure.'),
    ('sachiko', '大丈夫なの？そんな約束をして。', 'Is it really okay, making promises like that?', [(439, '大丈夫なの そんな約束して')], 'Added を after 約束.'),
    ('muranishi', 'ああ、大丈夫だ。', 'Yeah, do not worry.', [(440, 'ああ 大丈夫だ')], ''),
    ('muranishi', 'もっと広い家に引っ越そうな。', 'Let us move to a bigger house, too.', [(440, 'もっと広い'), (440, '引っ越そうな')], 'Used 家に instead of colloquial とこ.'),
    ('sachiko', '楽しみね。', 'Something to look forward to, is it not?', [(442, '楽しみね')], ''),
    ('muranishi', 'はいはい、任せとけ。', 'Yes, yes, leave it to me.', [(444, 'はいはい')], 'Added natural colloquial reassurance 任せとけ.'),
    ('sachiko', 'でも仕事のほうはうまくいってよかったじゃない。', 'Still, I am so glad things went well with your work.', [(457, 'でも仕事のほうは うまくいって よかったじゃない')], ''),
    ('sachiko', '期待してますよ。', 'I am counting on you.', [(458, '期待してますよ')], ''),
]

OPENER = "Happy family talk is full of warm promises and future plans. Let's look at the building blocks."

WALK = [
    (0, None, [
        "'My sales record this month was number one!'  It features ",
        ("muranishi", "今月"), " this word means this month, ",
        ("muranishi", "成績"), " is your score or performance record, and ",
        ("muranishi", "一位"), " puts ",
        ("muranishi", "一位"), ", one, with rank-counter ",
        ("muranishi", "一位"), " for first place."
    ]),
    (1, '信じられない！', [
        '"\'I cannot believe it!\' Built from the word for to believe, " The speaker uses ',
        ("mayumi", "信じられない"), " this word means 'unbelievable!'—used equally for great surprises and shocking news."
    ]),
    (2, None, [
        "'Next time I will buy you a Licca-chan dollhouse.'  In this sentence, ",
        ("muranishi", "今度"), " this word means next time or soon. Attaching ",
        ("muranishi", "買ってやる"), " to the word for to buy, shows a dad proudly treating his kid."
    ]),
    (3, None, [
        '"\'That is an absolute promise, okay!\' Pairing " Here, the word ',
        ("mayumi", "絶対"), ", no matter what, with ",
        ("mayumi", "約束"), ", promise, pins him down so he cannot back out."
    ]),
    (5, '大丈夫なの？', [
        '"\'Is it really okay?\' You already know " The character says ',
        ("sachiko", "大丈夫"), " as 'all right'; adding rising ",
        ("sachiko", "なの"), " asks 'are you sure that is really okay?'"
    ]),
    (7, None, [
        '"\'Let us move to a bigger house, too.\' When talking about rooms and houses, Japanese uses " You will hear ',
        ("muranishi", "広い"), ", spacious or wide, rather than 'big'. Turning the word for to move house, into ",
        ("muranishi", "引っ越そうな"), " warmly says 'let us move!'"
    ]),
    (8, None, [
        '"\'Something to look forward to, is it not?\' Whenever an upcoming trip, meal, or plan excites you, " Focus on ',
        ("sachiko", "楽しみ"), " says 'I cannot wait!'"
    ]),
    (9, None, [
        "'Yes, yes, leave it to me.'  Notice how ",
        ("muranishi", "任せとけ"), " squeezes the expression for 'leave it in my hands', into confident dad-talk."
    ]),
    (10, None, [
        '"\'Still, I am so glad things went well with your work.\' The phrase " In this sentence, ',
        ("sachiko", "うまくいって"), " comes from the word meaning 'go deliciously or skillfully'—the everyday phrase for things working out smoothly, capped with ",
        ("sachiko", "よかった"), ", thank goodness!"
    ]),
    (11, None, [
        '"\'I am counting on you.\' Built on " Check out ',
        ("sachiko", "期待"), ", which is a word for expectation or hope, Sachiko's playful polite ",
        ("sachiko", "期待してますよ"), " cheers her own husband on."
    ]),
]

TRANSITION = "Now let's listen to the whole family celebration again."

OUTRO = (
    "Keep the word for 'unbelievable!', the word to use when you look forward to something, "
    "and the phrase whenever plans work out well. "
    "In the next scene, morning brings a sudden shock at the office."
)

CLOSING = ('sachiko', 'おやすみ、また明日。')
