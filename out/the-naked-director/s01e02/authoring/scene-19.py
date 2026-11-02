ID = 'the-naked-director-s01e02-scene-19'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 2
SCENE = 19
TITLE = '倉庫の配達とパトカー  (Warehouse Delivery and Patrol Car)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'furuya': '古谷', 'toshi': 'トシ', 'muranishi': '村西'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E02'
SOURCE_FILE = 'sources/the-naked-director/s01/e02.ja.srt'

INTRO = (
    "Inside a busy Sapporo warehouse, Toshi oversees a delivery with distributor Furuya while Toru Muranishi looks on. "
    "After a sharp warning about fire safety gives way to polite business thanks, Toshi and Muranishi drive off—only to spot trouble ahead. "
    "Listen to how rough warehouse talk contrasts with Muranishi's polished manners."
)

STORY = [
    ('toshi', 'よろしく頼むよ。', 'I am counting on you.', [(479, 'よろしく頼むよ')], 'Trimmed interjection and repetition.'),
    ('toshi', '何で業者がタバコを吸ってるんだよ。', 'Why is a contractor smoking here?', [(480, '何で業者が')], 'Added object marker を and smoothed spoken contraction.'),
    ('toshi', '火事になったら全部弁償させるぞ。', 'If a fire starts, I will make you pay for everything.', [(481, '火事になったら全部')], 'Used standard させるぞ for spoken させんぞ.'),
    ('furuya', '悪かったな、兄さん。', 'My bad, young man.', [(486, '悪かったな')], ''),
    ('toshi', '古谷さん、頼むよ。', 'Count on your help, Mr. Furuya.', [(489, '古谷さん')], ''),
    ('muranishi', 'いつもお世話になってます。', 'Thank you as always for looking after us.', [(492, 'いつもお世話になってます')], ''),
    ('furuya', 'よく売れるわ。しばらくは稼げそうだ。', 'They sell really well. Looks like I can earn well for a while.', [(493, 'よく売れるわ'), (494, 'しばらくは稼げそうだ')], 'Joined two consecutive clean sales lines.'),
    ('furuya', 'それじゃあ。', 'Well then, see you.', [(499, 'それじゃあ')], ''),
    ('toshi', '毎度。', 'Thanks as always.', [(499, '毎度')], ''),
    ('muranishi', '大丈夫なんですか？あんなこと言って。', 'Is it really okay to say something like that?', [(500, '大丈夫なんですか')], ''),
    ('toshi', 'どうってことないよ。', 'It is nothing to worry about.', [(502, 'どうってこと')], 'Standardized ねえよ to ないよ.'),
    ('toshi', 'パトカーだ！', 'A patrol car!', [(518, 'パトカー')], 'Added だ for natural spoken urgency.'),
]

OPENER = "Toshi barks out blunt orders on the warehouse floor, while Muranishi sticks to textbook business etiquette. Let's unpack their key lines."

WALK = [
    (0, None, "'I am counting on you.' Pairing \"yoroshiku\", nicely or favorably, with \"tanomu\", to ask a favor, is an everyday workplace way to hand off a job. Casual \"yo\" at the end gives it a firm, friendly push."),
    (1, None, "'Why is a contractor smoking here?' \"Nande\" is the punchy spoken cousin of \"naze\", meaning 'why'. Next comes \"gyousha\", contractor or vendor, and \"tabako o suu\", literally to inhale tobacco."),
    (2, None, "'If a fire starts, I will make you pay for everything.' \"Kaji\" means a destructive fire, and \"nattara\" turns \"naru\", become, into 'if it becomes'. \"Zenbu\", everything, leads into \"benshou saseru\", forcing someone to pay compensation, capped by tough masculine \"zo\"."),
    (3, None, "'My bad, young man.' Instead of a stiff apology, Furuya drops \"warukatta na\", the past form of \"warui\", bad—literally 'that was bad of me'. Calling Toshi \"niisan\", older brother, is classic street warmth toward a younger man."),
    (5, None, "'Thank you as always for looking after us.' Muranishi greets Furuya with \"itsumo osewa ni nattemasu\", the gold-standard Japanese business greeting. \"Itsumo\" means always, and \"osewa\" means care or support."),
    (6, 'しばらくは稼げそうだ。', "'Looks like I can earn well for a while.' \"Shibaraku\" covers 'for a while', marked off by \"wa\" to set a safe horizon. Attaching \"sou da\" onto \"kasegeru\", able to earn money, expresses how things look right now."),
    (7, None, "'Well then, see you.' \"Sore jaa\" literally says 'well then' and doubles as an effortless casual goodbye when stepping out of a meeting. Friends often trim it even shorter to \"jaa\"."),
    (8, None, "'Thanks as always.' At delivery docks, drivers call out \"maido\", literally 'every time', as shorthand for 'thanks for your repeat business'. Two syllables do all the work of a full thank-you."),
    (9, '大丈夫なんですか？', "'Is it really okay?' \"Daijoubu\" is the indispensable all-purpose word for 'okay' or 'safe'. Slipping \"nan desu ka\" right after it asks for reassurance when something feels risky."),
    (11, None, "'A patrol car!' Japanese blends English 'patrol car' into brisk four-beat \"patokaa\". Adding plain \"da\" turns the noun into an urgent shout from the driver's seat."),
]

TRANSITION = "Now let's listen to the whole warehouse and highway scene straight through."

OUTRO = (
    "Keep \"itsumo osewa ni nattemasu\" handy for polite work greetings, "
    "and listen for \"patokaa\" whenever sirens appear on Japanese streets. "
    "See you in the next scene."
)

CLOSING = ('muranishi', 'また会いましょう。')
