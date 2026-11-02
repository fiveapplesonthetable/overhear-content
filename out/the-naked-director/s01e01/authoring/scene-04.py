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

OPENER = "Watch how Muranishi stays polite with 'masu' and 'desu' while his boss speaks down to him in plain, clipped endings."

WALK = [
    (0, None, [
        '"\'Muranishi, a moment.\' Calling someone\'s surname followed by " Notice how ',
        (None, "ちょっと"), ", a little bit, this word is the classic office signal for 'step over here a second'."
    ]),
    (2, None, [
        "'Zero contracts again?'  Check out ",
        (None, "また"), " this word means again, ",
        (None, "契約"), " this word is a business contract, and ",
        (None, "ゼロ"), " is borrowed straight from English. Ending with the sharp ",
        (None, "か"), " snaps the question shut."
    ]),
    (3, None, [
        "'Maybe it is the effect of the recession.'  The word ",
        (None, "不景気"), " combines the prefix for non- with the word for economic mood, giving 'recession'. Tacking ",
        (None, "ですかね"), " onto the end softens his excuse into 'could it be... I wonder?'"
    ]),
    (4, '違うよ。', [
        '"\'Wrong.\' Literally " Here, the word ',
        (None, "違う"), " this word means 'it differs', and speakers reach for it constantly to say 'no, that is wrong' or 'not at all'."
    ]),
    (5, None, [
        "'You do not need to come in starting next month.'  The character says ",
        (None, "来月"), " this word means next month, followed by ",
        (None, "から"), ", from. ",
        (None, "来なくていい"), " links the negative form for not come to the word for good—a cold boss's way of saying 'do not bother coming back'."
    ]),
    (6, 'それは困りますよ。', [
        "'That puts me in a bind.'  It features ",
        (None, "困ります"), " comes from the verb meaning to be troubled or stuck. Whenever a rule or schedule causes a problem, ",
        (None, "それは困りますよ"), " politely pushes back without sounding rude."
    ]),
    (6, '家族がいるんで。', [
        "'I have a family.'  Here, the word ",
        (None, "家族"), " is family, and living people take ",
        (None, "いる"), ", to exist. Softening the word for because into ",
        (None, "んで"), " leaves his plea hanging politely."
    ]),
    (7, None, [
        "'You really are a strange guy.'  Listen for ",
        (None, "不思議"), " this word means mysterious or baffling, and the rough ",
        (None, "やつ"), " this word means guy or fellow."
    ]),
    (9, None, [
        "'I am not praising you!'  Starting off with ",
        (None, "褒めてないよ"), " comes from the verb to praise—a key word that will soon transform Muranishi's entire sales career."
    ]),
    (10, None, [
        "'My father taught me to live positively.'  Notice how ",
        (None, "前向き"), " literally faces forward, so it this word means positive or upbeat. ",
        (None, "父"), " this word is the humble word you use when speaking about your own father to outsiders."
    ]),
    (11, None, [
        "'Learn from Ono and get results.'  The speaker uses ",
        (None, "学んで"), " connects the verb for learn into the blunt command ",
        (None, "結果を出せ"), ", literally 'put out results!'"
    ]),
]

TRANSITION = "Now let's listen to the whole office scolding again."

OUTRO = (
    "Keep the phrase for 'that is wrong' handy, express being troubled when something causes problems, "
    "and remember how to talk about having family. "
    "See you next time."
)

CLOSING = ('muranishi', 'さようなら。')
