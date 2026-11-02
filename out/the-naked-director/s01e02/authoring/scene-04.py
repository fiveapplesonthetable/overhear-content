ID = 'the-naked-director-s01e02-scene-04'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 2
SCENE = 4
TITLE = '行列のできる書店  (Lines Around the Block)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'police': '警察官', 'kitamori': '北森'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E02'
SOURCE_FILE = 'sources/the-naked-director/s01/e02.ja.srt'

INTRO = (
    "Soon after Muranishi buys the shop, two uniformed patrol officers walk down a Sapporo street looking for lunch. "
    "Instead of a quiet neighborhood block, they spot Kitamori managing a long line outside Hokudai Kanda Bookstore—and identical storefronts opening down the road. "
    "Hear the scene in Japanese first, and don't worry about catching every word."
)

STORY = [
    ('police', 'ああ、腹が減ったな。', 'Man, I am hungry.', [(64, '腹 減ったな')], ''),
    ('police', '定食ですか？', 'Are we getting a set meal?', [(65, '定食')], 'Changed casual っすか to polite ですか.'),
    ('police', 'なんであんなに繁盛してるんだ？', 'Why is that place doing such booming business?', [(67, 'なんで あんなに繁盛')], 'Expanded contraction してんだ.'),
    ('police', '北大神田書店？', 'Hokudai Kanda Bookstore?', [(68, '書店')], ''),
    ('kitamori', 'お待たせしてすみません。', 'Sorry to keep you waiting.', [(72, 'お待たせしてすみません')], ''),
    ('kitamori', '順番になります。', 'We will serve you in order.', [(72, '順番になります')], 'Trimmed trailing particle.'),
    ('kitamori', 'あっ、新作が出ました！', 'Oh, a new release just came out!', [(73, 'あっ 新作 出ました')], 'Added subject particle が.'),
    ('kitamori', '千五百円になります。', 'That comes to one thousand five hundred yen.', [(75, 'になります')], 'Spelled 1,500 in kanji.'),
    ('kitamori', 'どうぞ。', 'Here you are.', [(76, 'どうぞ')], ''),
    ('police', '先輩、ちょっと！', 'Senior officer, look here!', [(77, '先輩　ちょっと')], ''),
    ('police', 'あそこも北大神田書店ができてます。', 'Another Hokudai Kanda Bookstore has opened over there too.', [(83, '北大神田書店ができてます')], 'Shortened repeated あそこも.'),
    ('police', '何なんですかね？', 'Just what is going on here?', [(84, '何なんですかね')], ''),
]

OPENER = "Notice the contrast between the patrol officers chatting casually about lunch and Kitamori's crisp shop-counter Japanese. Let's look closer."

WALK = [
    (0, None, "'Man, I am hungry.' Literally \"hara ga hetta\" says 'my belly has shrunk'. Men often use blunt \"hara\", belly, where polite everyday speech uses \"onaka ga suita\", my stomach got empty."),
    (1, None, "'Are we getting a set meal?' A \"teishoku\" is a classic Japanese lunch set—main dish, rice, miso soup, and pickles served together on one tray."),
    (2, None, "'Why is that place doing such booming business?' Casual \"nande\" asks 'why', while \"hanjou\" pictures a shop bustling with customers."),
    (4, None, "'Sorry to keep you waiting.' You will hear \"omatase shite sumimasen\" at cafés, registers, and counters all across Japan whenever staff thank you for waiting."),
    (5, None, "'We will serve you in order.' \"Junban\" means turn-by-turn order, and \"ni narimasu\" politely states how things are arranged."),
    (6, None, "'Oh, a new release just came out!' Combining \"shin\", new, with \"saku\", work, gives \"shinsaku\"—used for new books, films, and seasonal menus alike."),
    (7, None, "'That comes to one thousand five hundred yen.' \"Sen\" is one thousand and \"gohyaku\" is five hundred, followed by \"en\", yen. Shop staff routinely say \"ni narimasu\" for 'that comes to'."),
    (9, None, "'Senior officer, look here!' \"Senpai\" addresses any colleague or classmate who joined before you, whether at school, in an office, or on a police beat."),
    (10, None, "'Another Hokudai Kanda Bookstore has opened over there too.' \"Asoko\" points to a spot over there away from both speakers, and \"dekitemasu\" says a new shop has sprung up."),
    (11, None, "'Just what is going on here?' Pairing \"nan\", what, with explanatory \"nan desu ka ne\" wonders aloud 'what on earth could this be?' while inviting the listener's guess."),
]

TRANSITION = "Now let's listen to the whole street scene again."

OUTRO = (
    "Listen for how shop staff rely on \"omatase shite sumimasen\" and \"ni narimasu\" to keep a busy counter running smoothly. "
    "See you next time."
)

CLOSING = ('kitamori', 'さようなら。')
