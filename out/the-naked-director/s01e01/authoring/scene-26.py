ID = 'the-naked-director-s01e01-scene-26'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 26
TITLE = '表と裏の世界  (The Front and Hidden Worlds)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'muranishi': '村西', 'toshi': 'トシ'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Over drinks at the bar, Muranishi asks Toshi what he was selling that caused such a fight. "
    "Toshi pulls out cassette tapes from his bag and tells Muranishi that every human being has two sides: a public surface and a hidden underside. "
    "Listen to Toshi's philosophy."
)

STORY = [
    ('muranishi', 'さっきは何を売ったんだ？', 'What was it you sold earlier?', [(597, '何を売ったんだ')], 'Added さっきは for time context.'),
    ('toshi', 'よくぞ聞いてくれたよ。これだよ。', 'Glad you asked! It is this right here.', [(598, 'よくぞ聞いてくれたよ'), (599, 'これだよ')], ''),
    ('toshi', 'すすきののホテルで録れたシリーズだ。', 'It is a series recorded at hotels in Susukino.', [(601, 'すすきののホテルで'), (601, 'シリーズ')], 'Wrote 録れた in kanji and simplified ending.'),
    ('muranishi', '偽物か？', 'Is it a fake?', [(602, '偽物')], 'Added question marker か.'),
    ('toshi', '違うよ。これは正真正銘の本物だぜ。', 'No way. This is the genuine, real deal.', [(603, '違うよ'), (604, 'これは'), (604, '正真正銘の')], 'Replaced slang モノホン with standard 本物.'),
    ('muranishi', '俺は人生のすべてを家族にささげてきたんだ。', 'I have devoted my entire life to my family.', [(612, '俺は人生のすべてを'), (612, '家族にささげてきたんだ')], ''),
    ('toshi', '気持ちは分かるよ。でもお金だけじゃだめだ。', 'I get how you feel. But money alone is not enough.', [(613, '気持ちは分かるよ'), (617, 'だけじゃ')], 'Added お before 金 and wrote だめ in hiragana.'),
    ('muranishi', 'だったら俺だって言いたいことがある。', 'Well then, I have things I want to say too.', [(618, 'だったら俺だって 言いたいことがある')], ''),
    ('toshi', '誰だって人間には表と裏があるんだよ。', 'Every single person has a public front and a hidden side.', [(620, '誰だって'), (620, '表と裏')], 'Framed cleanly around 人間 for A1 clarity.'),
    ('muranishi', '裏？そんなの隠してるから分からないよ。', 'A hidden side? People hide that, so how could anyone know?', [(624, '裏'), (625, 'そんなの隠して')], 'Simplified 分かりようがない to 分からないよ.'),
    ('toshi', 'お礼に見せてやろうか？裏の世界を。', 'By way of thanks, shall I show it to you? The hidden world.', [(626, 'お礼'), (627, '見せてやろうか 裏の世界を')], ''),
    ('muranishi', '裏の世界か。見てみよう。', 'The hidden world, huh. Let me take a look.', [], 'Clean closing response leading into their night tour.'),
]

OPENER = "This scene introduces the episode's central pair of words—front and back, surface and underside. Let's explore them."

WALK = [
    (0, None, "'What was it you sold earlier?' \"Sakki\" points back to just a few minutes ago—much closer in time than 'yesterday'—and \"utta\" is the past of \"uru\", to sell."),
    (1, 'よくぞ聞いてくれたよ。', "'Glad you asked!' Energetic \"yokuzo\" praises the listener for asking the exact question the speaker was dying to answer, paired with warm \"kiite kureta\"."),
    (3, None, "'Is it a fake?' \"Nisemono\" joins \"nise\", counterfeit or imitation, with \"mono\", thing."),
    (4, 'これは正真正銘の本物だぜ。', "'This is the genuine, real deal.' Meet the opposite of \"nisemono\": \"honmono\", built from \"hon\", true, plus \"mono\", thing! Traditional \"shoushin-shoumei\" stamps it 'one hundred percent genuine'."),
    (5, None, "'I have devoted my entire life to my family.' Pouring his heart out, Muranishi pairs \"jinsei no subete\", all of my life, with \"sasagete kita\", have dedicated up to now."),
    (6, '気持ちは分かるよ。', "'I get how you feel.' \"Kimochi\" means feelings or emotional state, so \"kimochi wa wakaru\" is the most natural way in Japanese to show empathy."),
    (7, None, "'Well then, I have things I want to say too.' Turning \"iu\", to say, into \"iitai\" builds 'want to say', so \"iitai koto ga aru\" means 'I have got something on my chest!'"),
    (8, None, "'Every single person has a public front and a hidden side.' Cultural key to Japan: \"omote\" is the polite front face shown to society, while \"ura\" is the reverse side kept behind closed doors."),
    (9, None, "'A hidden side? People hide that, so how could anyone know?' \"Kakushiteru\" comes from \"kakusu\", to hide or conceal."),
    (10, None, "'By way of thanks, shall I show it to you? The hidden world.' \"Orei\" means gratitude or a thank-you gift, and \"misete yarou ka\" offers 'shall I show you?'—pointing to \"ura no sekai\", the hidden world that gives this episode its title."),
]

TRANSITION = "Now let's listen to Toshi and Muranishi's conversation about surface and underside again."

OUTRO = (
    "Remember that vivid pair—\"nisemono\" for a fake and \"honmono\" for the real thing—alongside cultural twins \"omote\", the public front, and \"ura\", the hidden side. "
    "See you in scene twenty-eight."
)

CLOSING = ('toshi', 'じゃあね。')
