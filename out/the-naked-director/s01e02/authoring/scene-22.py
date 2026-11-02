ID = 'the-naked-director-s01e02-scene-22'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 2
SCENE = 22
TITLE = '東京から来た武井  (Takei Arrives from Tokyo)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mori': '森', 'police': '警察官', 'takei': '武井'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E02'
SOURCE_FILE = 'sources/the-naked-director/s01/e02.ja.srt'

INTRO = (
    "At police headquarters in Hokkaido, officers haul in more confiscated boxes and gossip about Muranishi's newest release. "
    "Then sharp-eyed investigator Takei walks in from Tokyo and reprimands Mori because the books have spread to the capital. "
    "Listen to the abrupt shift from casual office chatter to stiff police hierarchy."
)

STORY = [
    ('police', 'また押収したらしいぞ。', 'I hear they confiscated another batch.', [(579, 'また押収したらしいぞ')], ''),
    ('police', 'ほんとですか？', 'Is that true?', [(580, 'ホントすか')], 'Standardized colloquial ホントすか.'),
    ('police', '早くしろ！', 'Hurry up!', [(581, '早くしろ')], ''),
    ('police', '新作が出たんだって？', 'I heard a new release came out?', [(584, '新作'), (584, '出たんだって')], 'Added subject marker が.'),
    ('mori', '誰だ、お前。', 'Who are you?', [(601, '誰だ')], 'Standardized おめえ to お前.'),
    ('takei', '警視庁の武井だよ。', 'I am Takei from Tokyo police headquarters.', [(602, '警視庁の')], ''),
    ('mori', 'ご苦労さまです。', 'Thank you for your trouble.', [(603, 'ご苦労さまです')], ''),
    ('takei', 'また新しい店がオープンしたらしいな。', 'I hear another new store opened up.', [(604, 'また新しい店が'), (604, 'オープンしたらしいな')], ''),
    ('takei', '北海道だけの問題じゃねえぞ。', 'This is not just a problem for Hokkaido.', [(608, '北海道だけの問題じゃねえぞ')], ''),
    ('takei', '東京にも出回ってるんだよ！', 'They are circulating in Tokyo too!', [(609, '東京にも出回ってんだよ')], 'Standardized 出回ってんだよ to 出回ってるんだよ.'),
    ('mori', '申し訳ございません！', 'We are deeply sorry!', [(610, '申し訳ございません')], ''),
]

OPENER = "Notice how fast Mori drops his tough tone the instant Takei names Tokyo headquarters. Let's walk through the key lines."

WALK = [
    (0, None, "'I hear they confiscated another batch.' Opening with \"mata\", again, sets up repeat trouble, followed by \"oushuu shita\", confiscated. Adding \"rashii\" passes along secondhand news—'apparently' or 'I hear'."),
    (1, None, "'Is that true?' \"Honto\" trims everyday \"hontou\", truth, for brisk speech, and \"desu ka\" keeps it polite toward a colleague. You can use \"honto desu ka\" any time news catches you by surprise."),
    (2, None, "'Hurry up!' \"Hayaku\" means fast, and \"shiro\" is the blunt command form of \"suru\", do. Together \"hayaku shiro\" barks out 'make it quick!' among superiors or rough peers."),
    (3, None, "'I heard a new release came out?' Combining \"shin\", new, with \"saku\", work, gives \"shinsaku\", a brand-new book, film, or product. Ending with \"nda tte\" quotes office rumor—'they say it came out?'."),
    (4, None, "'Who are you?' \"Dare\" is the word for 'who', snapped out as \"dare da\" before rough \"omae\", you. Speaking to an unknown visitor like that backfires the moment he outranks you."),
    (5, None, "'I am Takei from Tokyo police headquarters.' \"Keishichou\" specifically names the capital's police department in Tokyo, linked to \"Takei\" by \"no\", of. Calm \"da yo\" informs Mori just who walked through his door."),
    (6, None, "'Thank you for your trouble.' Mori scrambles to recover with \"gokurousama desu\", a workplace greeting that acknowledges someone's effort or long trip. In strict etiquette, officers usually prefer \"otsukaresama desu\" toward higher ranks."),
    (7, None, "'I hear another new store opened up.' \"Atarashii mise\" pairs \"atarashii\", new, with \"mise\", shop or store. Borrowed English \"oopun shita\" means opened for business, followed again by hearsay \"rashii\"."),
    (8, None, "'This is not just a problem for Hokkaido.' \"Dake\" limits something to 'only', so \"Hokkaidou dake no mondai\" means 'only Hokkaido's problem'. Rough \"ja nee zo\" compresses polite \"de wa arimasen\" into an angry warning."),
    (9, None, "'They are circulating in Tokyo too!' \"Toukyou ni mo\" stacks \"ni\", in, with \"mo\", also, meaning 'even in Tokyo'. \"Demawatteru\" comes from \"demawaru\", to circulate widely on the market."),
    (10, None, "'We are deeply sorry!' Gone is Mori's swagger: \"moushiwake gozaimasen\" literally says 'there is no excuse', the most formal apology in business and official life."),
]

TRANSITION = "Now let's listen to the whole headquarters confrontation again from start to finish."

OUTRO = (
    "Notice the huge gap between rough \"dare da, omae\" at the start and stiff \"moushiwake gozaimasen\" at the end—register tells the whole story in Japanese. "
    "Until the next scene, goodbye."
)

CLOSING = ('mori', 'さようなら。')
