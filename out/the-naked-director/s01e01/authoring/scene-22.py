ID = 'the-naked-director-s01e01-scene-22'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 22
TITLE = 'これは俺らの問題だ  (This Is Our Problem)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'sachiko': '幸子', 'muranishi': '村西', 'daisuke': '大輔'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Walking home in the middle of the day after losing his job, Muranishi discovers his marriage has fallen apart too. "
    "After a bitter argument, Sachiko packs up to leave the house, taking Mayumi and little Daisuke with her. "
    "Listen to this painful turning point."
)

STORY = [
    ('sachiko', '何でそんなところにいるのよ？', 'Why are you standing there?', [(515, '何でそんなところにいるのよ')], ''),
    ('muranishi', '幸子、どういうことだ？', 'Sachiko, what is the meaning of this?', [(516, '幸子')], 'Added clean A1 question framing the confrontation.'),
    ('sachiko', '嫌だ！もう終わりよ。', 'No! Everything is over.', [(517, '嫌だ')], 'Added もう終わりよ for dramatic clarity.'),
    ('muranishi', 'みっともない！', 'How shameful!', [(520, 'みっともない')], ''),
    ('sachiko', 'みっともないのはあんたでしょ！', 'You are the one who is shameful!', [(521, 'みっともないのは あんたでしょ')], ''),
    ('muranishi', '俺のどこがみっともないんだ！', 'What part of me is shameful!', [(522, '俺のどこが みっともないんだ')], ''),
    ('daisuke', 'パパ！ラジコンは？カウンタックは？', 'Papa! What about my remote-control car? What about the Countach?', [(529, 'パパ ラジコンは カウンタックは')], ''),
    ('muranishi', '大輔、ごめんな。', 'Daisuke, I am sorry.', [], 'Short gentle reply from Muranishi to his son.'),
    ('muranishi', 'これは俺らの問題だ。', 'This is our problem.', [(532, 'これは俺らの問題だ')], ''),
    ('muranishi', '母さんは口を出すな！', 'Stay out of this, Mother!', [(532, '母さんは')], 'Standardised 口出すな 母さんは word order.'),
    ('sachiko', '大輔、行くよ！', 'Daisuke, we are leaving!', [(534, '大輔 行くよ')], ''),
    ('sachiko', 'ほら、早く行って！', 'Come on, hurry and go!', [(535, 'ほら 早く行って')], ''),
]

OPENER = "Even during a heated breakup, Japanese relies on compact everyday patterns. Let's look at how each line works."

WALK = [
    (0, None, [
        "'Why are you standing there?'  Here, the word ",
        (None, "そんなところ"), " this word means 'a place like that', followed by ",
        (None, "にいる"), ". This word means to be there, and sharp feminine ",
        (None, "のよ"), " demanding an explanation."
    ]),
    (1, None, [
        '"\'Sachiko, what is the meaning of this?\' Whenever something shocking happens and you want an explanation, " You can catch ',
        (None, "どういうことだ"), " literally asks 'what kind of thing does this say?'"
    ]),
    (2, '嫌だ！', [
        '"\'No!\' Strong " Watch for ',
        (None, "嫌だ"), " this word expresses visceral refusal or distress—'I hate this!' or 'no way!'—much stronger than a polite refusal."
    ]),
    (3, None, [
        "'How shameful!'  Watch for ",
        (None, "みっともない！"), " this word criticizes behaviour or appearances as undignified, embarrassing, or unseemly."
    ]),
    (4, None, [
        '"\'You are the one who is shameful!\' Turning " Check out ',
        (None, "みっともない！"), " into ",
        (None, "みっともないのは"), " spotlights 'the shameful one', and ",
        (None, "でしょ"), " snaps back 'is you, obviously!'"
    ]),
    (5, None, [
        '"\'What part of me is shameful!\' Literally, " The speaker uses ',
        (None, "俺のどこが"), " asks 'where of me?'—the natural Japanese way to challenge someone with 'just what is wrong with me?!'"
    ]),
    (6, None, [
        '"\'Papa! What about my remote-control car? What about the Countach?\' With a sad little voice, Daisuke uses " Pay attention to ',
        (None, "ラジコン"), ", which is the everyday word for a remote-control toy, plus rising ",
        (None, "は"), " to ask 'what about my car?'"
    ]),
    (7, None, [
        '"\'Daisuke, I am sorry.\' Built around casual " The speaker uses ',
        (None, "ごめん"), ", sorry, ",
        (None, "ごめんな"), " this word is how a parent or close friend apologizes softly, gentler than formal apologies."
    ]),
    (9, None, [
        "'Stay out of this, Mother!'  Starting off with ",
        (None, "口を出す"), " literally this word means 'stick your mouth out'—a vivid idiom for meddling or butting into someone else's business!"
    ]),
    (10, None, [
        '"\'Daisuke, we are leaving!\' Simple dictionary-form " Here, the word ',
        (None, "行く"), ", to go, plus ",
        (None, "よ"), " this word tells a child 'come on, we are going now'."
    ]),
]

TRANSITION = "Now let's listen to the whole confrontation at the house again."

OUTRO = (
    "Notice the phrase for 'what does this mean?', the words for a warm personal apology, "
    "and the expression for sticking your mouth in—for meddling. "
    "Next, the empty house triggers a memory from Muranishi's childhood."
)
CLOSING = ('muranishi', 'さようなら。')
