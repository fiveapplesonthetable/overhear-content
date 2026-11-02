ID = 'the-naked-director-s01e01-scene-04'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'また契約ゼロか  (Zero Contracts Again?)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kacho': '課長', 'muranishi': '村西'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Back at Bianca International, an English encyclopedia sales office in Sapporo, "
    "the section chief calls Muranishi over to his desk. "
    "Muranishi has sold nothing all month, yet somehow stays cheerful. "
    "Listen to the boss's frustration and Muranishi's polite excuses."
)

STORY = [
    ('kacho', '村西、ちょっと。', 'Muranishi, a moment.', [(65, '村西 ちょっと')], ''),
    ('muranishi', 'はい。', 'Yes, sir.', [(66, 'はい')], ''),
    ('kacho', 'また契約ゼロか？', 'Zero contracts again?', [(68, 'また契約ゼロか')], ''),
    ('muranishi', '不景気の影響ですかね。', 'Maybe it is the effect of the recession.', [(69, '不景気の影響ですかね')], ''),
    ('kacho', '違うよ。お前の問題だろ。', 'Wrong. It is your problem, is it not?', [(70, '違うよ お前の問題だろ')], ''),
    ('kacho', '来月から来なくていい。', 'You do not need to come in starting next month.', [(71, '来月から来なくていい')], 'Trimmed conditional clause for directness.'),
    ('muranishi', 'それは困りますよ。家族がいるんで。', 'That puts me in a bind. I have a family.', [(72, 'それは困りますよ 家族がいるんで')], ''),
    ('kacho', 'ほんと不思議なやつだな。', 'You really are a strange guy.', [(76, '不思議な')], 'Normalized emphatic katakana spelling to hiragana.'),
    ('muranishi', 'ありがとうございます。', 'Thank you very much.', [(77, 'ありがとうございます')], ''),
    ('kacho', '褒めてないよ！', 'I am not praising you!', [(77, '褒めて')], 'Standardised 褒めてねえよ to 褒めてないよ.'),
    ('muranishi', '前向きに生きろと父から教わったので。', 'My father taught me to live positively.', [(79, '前向きに生きろと 父から教わったので')], ''),
    ('kacho', '小野から学んで結果を出せ。', 'Learn from Ono and get results.', [(82, '学んで結果を出せ')], 'Replaced pronoun あいつ with Ono by name.'),
]

OPENER = "Watch how Muranishi stays polite with \"masu\" and \"desu\" while his boss speaks down to him in plain, clipped endings."

WALK = [
    (0, None, "'Muranishi, a moment.' Calling someone's surname followed by \"chotto\", a little bit, is the classic office signal for 'step over here a second'."),
    (2, None, "'Zero contracts again?' \"Mata\" means again, \"keiyaku\" is a business contract, and \"zero\" is borrowed straight from English. Ending with sharp \"ka\" snaps the question shut."),
    (3, None, "'Maybe it is the effect of the recession.' \"Fukeiki\" combines \"fu\", non-, with \"keiki\", economic mood, giving 'recession'. Tacking \"desu ka ne\" onto the end softens his excuse into 'could it be... I wonder?'"),
    (4, '違うよ。', "'Wrong.' Literally \"chigau\" means 'it differs', and Japanese speakers reach for it constantly to say 'no, that is wrong' or 'not at all'."),
    (5, None, "'You do not need to come in starting next month.' \"Raigetsu\" means next month, followed by \"kara\", from. \"Konakute ii\" links negative \"konai\", not come, to \"ii\", good—a cold boss's way of saying 'do not bother coming back'."),
    (6, 'それは困りますよ。', "'That puts me in a bind.' \"Komarimasu\" comes from \"komaru\", to be troubled or stuck. Whenever a rule or schedule causes a problem, \"sore wa komarimasu\" politely pushes back without sounding rude."),
    (6, '家族がいるんで。', "'I have a family.' \"Kazoku\" is family, and living people take \"iru\", to exist, rather than \"aru\". Softening \"node\", because, into \"nde\" leaves his plea hanging politely."),
    (7, None, "'You really are a strange guy.' \"Fushigi\" means mysterious or baffling, and rough \"yatsu\" means guy or fellow."),
    (9, None, "'I am not praising you!' \"Homete nai yo\" comes from \"homeru\", to praise—a key word that will soon transform Muranishi's entire sales career."),
    (10, None, "'My father taught me to live positively.' \"Maemuki\" literally faces \"mae\", forward, so it means positive or upbeat. \"Chichi\" is the humble word you use when speaking about your own father to outsiders."),
    (11, None, "'Learn from Ono and get results.' \"Manande\" connects \"manabu\", to learn, into the blunt command \"kekka o dase\", literally 'put out results!'"),
]

TRANSITION = "Now let's listen to the whole office scolding again."

OUTRO = (
    "Keep \"chigau\" handy for 'that is wrong', \"komarimasu\" when something causes trouble, "
    "and \"kazoku ga iru\" to talk about having family. "
    "See you next time."
)

CLOSING = ('muranishi', 'さようなら。')
