ID = 'the-naked-director-s01e01-scene-07'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 7
TITLE = 'いってらっしゃい  (Have a Good Day)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'daisuke': '大輔', 'muranishi': '村西', 'mayumi': '真由美'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "At the front door, young Daisuke sees his father off to work and asks him to come home early. "
    "Muranishi claims he has overtime tonight, until sharp-eyed Mayumi spots arcade coins spilling out of his pocket. "
    "Listen to this morning send-off."
)

STORY = [
    ('daisuke', 'いってらっしゃい、パパ。', 'Have a good day, Papa.', [(126, 'いってらっしゃい パパ')], ''),
    ('daisuke', '早く帰ってね！', 'Come home early, okay!', [(127, '早く帰ってね')], ''),
    ('muranishi', '今日は残業だから遅いんだよ。', 'I have overtime today, so I will be late.', [(128, '残業だから遅いんだよ')], 'Added は after 今日 for clear A1 topic marking.'),
    ('mayumi', 'どうせゲームでもやってサボってるくせに。', 'Even though you are probably just playing games and slacking off anyway.', [(129, 'どうせゲームでもやって サボってるくせに')], ''),
    ('muranishi', 'そんなこと言うなよ、真由美。', 'Do not say things like that, Mayumi.', [(130, 'そんなこと言うなよ 真由美')], ''),
    ('mayumi', 'ほら！また小銭だ。', 'Look! Pocket change again.', [(133, 'ほら')], 'Added short A1 phrase naming the spilled coins.'),
    ('muranishi', 'いや、これは仕事の小銭だよ。', 'No, these are coins for work.', [], 'Short bridging excuse responding to the spilled coins.'),
    ('mayumi', '頑張って遊んできて。', 'Have fun playing hard out there.', [(135, '頑張って遊んできて')], ''),
    ('muranishi', '本当に仕事だからな。', 'It really is work, you know.', [], 'Short natural reply from Muranishi.'),
    ('muranishi', 'じゃあ、行ってくる。', 'Well then, I am heading out.', [(137, 'じゃあ 行ってくる')], ''),
    ('daisuke', 'いってらっしゃい！', 'See you later, have a good day!', [(138, 'いってらっしゃい')], ''),
    ('muranishi', 'はーい。', 'Okay!', [(138, 'はーい')], ''),
]

OPENER = "Every Japanese home uses a matched pair of doorway greetings every morning. Let's hear how they work alongside Mayumi's teasing."

WALK = [
    (0, None, "'Have a good day, Papa.' Anyone staying at home calls out \"itterasshai\" to the person stepping out the door—literally a polite 'please go and come back'."),
    (1, None, "'Come home early, okay!' \"Hayaku\" turns \"hayai\", early or fast, into 'early', and \"kaette ne\" softens \"kaeru\", to return home, into a warm request."),
    (2, None, "'I have overtime today, so I will be late.' Office workers use \"zangyou\", overtime work, almost daily. Following it with \"dakara\", therefore or because, leads into \"osoi\", late."),
    (3, None, "'Even though you are probably just playing games and slacking off anyway.' \"Douse\" shrugs 'anyway, I bet', and \"sabotteru\" comes from French 'sabotage'—the everyday slang word for skipping class or work!"),
    (4, None, "'Do not say things like that, Mayumi.' Putting rough \"na\" right after dictionary-form \"iu\", to say, creates a blunt 'do not say that', softened a touch by \"yo\"."),
    (5, 'ほら！', "'Look!' Whenever you point at proof right in front of someone's eyes, \"hora\" says 'look!' or 'see, told you!'"),
    (6, None, "'No, these are coins for work.' \"Kozeni\" pairs \"ko\", small, with \"zeni\", money—pocket change or loose coins for payphones and arcade cabinets."),
    (7, None, "'Have fun playing hard out there.' Mayumi mischievously glues \"ganbatte\", do your best, onto \"asonde kite\", go have fun playing—mocking his fake overtime."),
    (9, None, "'Well then, I am heading out.' Here is the other half of the doorway pair: the person leaving always says \"itte kuru\" (or polite \"itte kimasu\"), literally 'I will go and come back'."),
    (11, None, "'Okay!' Stretching \"hai\" into cheerful \"haai\" sounds warm and playful when answering a child."),
]

TRANSITION = "Now let's listen to the whole doorway scene again."

OUTRO = (
    "Remember that matched doorway pair—\"itte kuru\" when you head out, and \"itterasshai\" from the people waving you off—plus \"hayaku kaette ne\" to ask someone home early. "
    "See you next time."
)

CLOSING = ('daisuke', 'またね。')
