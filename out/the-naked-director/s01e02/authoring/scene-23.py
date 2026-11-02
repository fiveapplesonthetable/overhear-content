ID = 'the-naked-director-s01e02-scene-23'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 2
SCENE = 23
TITLE = '四十七店と手入れ  (Forty-Seven Stores and a Raid)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'driver': '配達員', 'muranishi': '村西', 'takei': '武井'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E02'
SOURCE_FILE = 'sources/the-naked-director/s01/e02.ja.srt'

INTRO = (
    "At a loud celebration party, Toru Muranishi raises a glass to forty-seven store openings in three months and sets his sights on one hundred. "
    "Meanwhile, Takei raids a delivery van—where the old picture-book trick suddenly stops working—and Muranishi slips away to go home. "
    "Listen to the celebratory toasts and the sudden police raid."
)

STORY = [
    ('muranishi', 'おかげで三カ月で四十七店出店できた。', 'Thanks to you all, we opened forty-seven stores in three months.', [(612, 'おかげで'), (612, '出店できた')], 'Wrote numerals in kanji for TTS and alignment.'),
    ('muranishi', '次は百店目指そう。乾杯！', 'Next, let us aim for one hundred stores. Cheers!', [(613, '目指そう'), (613, '乾杯')], 'Wrote numeral in kanji.'),
    ('takei', '荷物を見せろ。', 'Show me the cargo.', [(624, '見せろ')], 'Added object marker を.'),
    ('driver', '全部絵本ですよ。', 'They are all picture books.', [(625, '全部')], 'Standardized 絵本っすよ to 絵本ですよ.'),
    ('takei', 'いいから出せ。', 'Never mind that, bring them out.', [(626, 'いいから出せ')], ''),
    ('driver', 'よく見てくださいよ、刑事さん。', 'Take a good look, detective.', [(630, 'よく見てくださいよ'), (630, '刑事さん')], ''),
    ('driver', 'もういいですか？', 'Are we good to go now?', [(638, 'もういい')], 'Standardized もういいっすか to もういいですか.'),
    ('driver', 'ご苦労さまでした。', 'Thank you for your hard work.', [(640, 'ご苦労さま')], 'Standardized ご苦労さまっした to ご苦労さまでした.'),
    ('takei', 'よし、逮捕しろ。', 'Alright, arrest him.', [(642, '逮捕しろ')], 'Normalized よーし to よし.'),
    ('muranishi', 'お前らにボーナスだ！', 'Here is a bonus for all of you!', [(652, 'お前らに'), (652, 'ボーナスだ')], ''),
    ('muranishi', '帰る。', 'I am going home.', [(660, '帰る')], ''),
]

OPENER = "Celebration and danger collide here: Muranishi rallies his crew at the hall while Takei springs a trap at the warehouse. Let's hear the key lines."

WALK = [
    (0, None, "'Thanks to you all, we opened forty-seven stores in three months.' Starting with \"okage de\" gives warm credit—'thanks to your support'. \"Sankagetsu\" counts three months, \"yonjuunana-ten\" counts forty-seven shops, and \"shutten dekita\" says they managed to open them."),
    (1, None, "'Next, let us aim for one hundred stores. Cheers!' \"Tsugi wa\" spotlights what comes next, and \"mezasou\" rallies everyone—'let's aim for'—around \"hyakuten\", a hundred shops. Then comes \"kanpai\", literally 'dry glass', the universal toast for 'cheers!'."),
    (2, None, "'Show me the cargo.' \"Nimotsu\" covers luggage, packages, or freight. \"Misero\" turns \"miseru\", to show, into a sharp police order with zero polite padding."),
    (3, None, "'They are all picture books.' Trying the old checkpoint excuse, the driver pairs \"zenbu\", all of them, with \"ehon\", picture books, plus reassuring \"desu yo\"."),
    (4, None, "'Never mind that, bring them out.' Idiomatic \"ii kara\" brushes aside excuses—'enough already' or 'never mind that'—before \"dase\", the blunt command of \"dasu\", take out."),
    (5, None, "'Take a good look, detective.' \"Yoku\" before \"mite kudasai\" means 'closely' or 'thoroughly', nudging Takei to spot the cash inside. \"Keijisan\" addresses a plainclothes investigator politely."),
    (6, None, "'Are we good to go now?' \"Mou ii desu ka\" literally asks 'is it good already?', a handy everyday check for 'are we done here?' or 'may I go now?'."),
    (8, None, "'Alright, arrest him.' Unlike local patrolmen, Takei pockets nothing: \"yoshi\" signals 'alright, got what we needed', and \"taiho shiro\" orders an immediate arrest."),
    (9, None, "'Here is a bonus for all of you!' Back at the party, rough plural \"omaera\", you guys, marks Muranishi's rowdy bond with his staff before borrowed English \"boonasu da\"."),
    (10, None, "'I am going home.' Amid all the noise, one quiet word—\"kaeru\", to return home—says everything. Japanese needs no 'I' when the speaker's own next move is unmistakable."),
]

TRANSITION = "Now let's hear the whole party and warehouse raid sequence again straight through."

OUTRO = (
    "From celebratory \"kanpai\" to quiet one-word \"kaeru\", "
    "you heard how Japanese can rally a crowd or slip out of a room in just a couple of syllables. "
    "See you soon."
)

CLOSING = ('muranishi', 'じゃあね。')
