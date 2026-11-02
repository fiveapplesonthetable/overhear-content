ID = 'the-naked-director-s01e01-scene-13'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 13
TITLE = 'ラブ、グッド、ハロー  (Love, Good, and Hello)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'nakai': '中井', 'muranishi': '村西'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Seated on the tatami mat across from the terrifying Nakai, Muranishi is trembling from head to toe. "
    "Remembering Ono's lesson, he praises Nakai as one of a kind and promises that three tiny English words are enough to talk with foreigners—until his tongue slips. "
    "Listen to this high-wire pitch."
)

STORY = [
    ('muranishi', 'すいません、すいません！', 'I am sorry, I am so sorry!', [(241, 'すいません すいません')], ''),
    ('muranishi', '失礼いたしました。', 'Please forgive my rudeness.', [(252, '失礼いたしました')], ''),
    ('nakai', '早く説明しろよ。', 'Hurry up and explain it.', [(253, '早く説明しろよ')], ''),
    ('muranishi', 'はい。ご主人、とてもビューティフォーです。', 'Yes! Sir, it looks truly beautiful on you.', [(254, 'はい'), (255, 'ご主人'), (258, 'とてもビューティフォーです')], ''),
    ('muranishi', '特別なオーラでオンリーワンでございます。', 'With its special aura, it is truly one of a kind.', [(265, '特別なオーラ'), (266, 'オンリーワンでございます')], 'Streamlined praise for A1 length.'),
    ('nakai', 'そうかもな。', 'Maybe you are right.', [(268, 'そうかもな')], ''),
    ('muranishi', '最近、海外との取り引きも増えたのではないでしょうか？', 'Have business dealings overseas not increased lately?', [(276, '最近 海外との取り引きも')], 'Expanded 増えたんではない to 増えたのではない.'),
    ('muranishi', 'そこでこのエンサイクロペディアが役に立ちます。', 'That is right where this encyclopedia comes in handy.', [(278, 'そこで'), (279, 'エンサイクロペディアが 役に立ちます')], ''),
    ('muranishi', 'ラブ、グッド、ハロー、短い単語を覚えるだけです。', 'Love, good, hello—you just memorize short words like these.', [(281, 'ラブ グッド'), (282, 'ハロー'), (282, '短い単語を覚えるだけで')], 'Completed clause cleanly with です.'),
    ('muranishi', 'それで外国人と話すことができます。', 'With just that, you can speak with foreigners.', [(283, '外国人と話すことができます')], ''),
    ('nakai', 'その三つなら俺でも覚えられそうだな。', 'If it is just those three, even I could probably learn them.', [(284, '覚えられそうだな')], 'Wrote 三つ in kanji and dropped school-level slang for A1 clarity.'),
    ('muranishi', '小学生でも覚えることができますから。', 'Because even a grade-schooler can learn them!', [(285, '小学生でも 覚えることができますから')], ''),
]

OPENER = "Muranishi swings from formal apologies to bold sales claims—and walks right into trouble on the final line. Let's inspect each piece."

WALK = [
    (1, None, [
        '"\'Please forgive my rudeness.\' When the casual word for sorry is not nearly polite enough, " Pay attention to ',
        (None, "失礼いたしました。"),
        " literally says 'I humbly committed a rudeness'—the gold-standard business apology."
    ]),
    (2, None, [
        '"\'Hurry up and explain it.\' As a noun, the word for explanation is " In this line, ',
        (None, "説明。"),
        ", and turning the verb to do into ",
        (None, "しろよ。"),
        " barks 'explain it now!'"
    ]),
    (3, None, [
        '"\'Yes! Sir, it looks truly beautiful on you.\' Addressing the man of the house respectfully as " The phrase contains ',
        (None, "ご主人。"),
        ", Muranishi leans on ",
        (None, "とても。"),
        ", very, plus English ",
        (None, "ビューティフォー。"),
        "."
    ]),
    (4, None, [
        '"\'With its special aura, it is truly one of a kind.\' Notice homegrown Japanese English " Here, the word ',
        (None, "オンリーワン。"),
        ", from 'only one'! Where English says 'one of a kind' or 'unique', Japanese loves ",
        (None, "オンリーワン。"),
        "."
    ]),
    (5, None, [
        '"\'Maybe you are right.\' This response, " Focus on ',
        (None, "そうかもな。"),
        ", packs ",
        (None, "そう。"),
        ", so, with ",
        (None, "かも。"),
        ", short for maybe—showing the flattery just melted Nakai's guard."
    ]),
    (7, None, [
        '"\'That is right where this encyclopedia comes in handy.\' In everyday speech, the phrase for being useful is " You can catch ',
        (None, "役に立ちます。"),
        ", which literally means 'stand in service'."
    ]),
    (8, None, [
        '"\'Love, good, hello—you just memorize short words like these.\' Hear how English \'love\', \'good\', and \'hello\' become " It features ',
        (None, "ラブ。"),
        ", ",
        (None, "グッド。"),
        ", and ",
        (None, "ハロー。"),
        " in Japanese syllables, followed by ",
        (None, "短い。"),
        ", short, and ",
        (None, "覚える。"),
        ", to memorize."
    ]),
    (9, None, [
        '"\'With just that, you can speak with foreigners.\' The word for foreigner is " The word ',
        (None, "外国人。"),
        ", which combines outside country with person. Adding ",
        (None, "ことができます。"),
        " after ",
        (None, "話す。"),
        ", to speak, states politely 'you are able to speak'."
    ]),
    (10, None, [
        '"\'If it is just those three, even I could probably learn them.\' By itself, the word for three things is " Starting off with ',
        (None, "三つ。"),
        ", using native Japanese counting, and attaching the suffix for appearance onto the verb can memorize, forming ",
        (None, "覚えられそう。"),
        ", expresses 'looks like I could'."
    ]),
    (11, None, [
        '"\'Because even a grade-schooler can learn them!\' The word for an elementary-school child is " Pay attention to ',
        (None, "小学生。"),
        ", and ",
        (None, "でも。"),
        " here means 'even'—a well-meant reassurance that accidentally insults the boss!"
    ]),
]

TRANSITION = "Now let's listen to Muranishi's high-stakes tatami pitch again."

OUTRO = (
    "Keep the formal phrase for apologies, the expression when something comes in handy, "
    "and the polite phrasing to talk about languages you can speak. "
    "Let's see how Muranishi rescues himself in scene fourteen."
)

CLOSING = ('muranishi', 'また会いましょう。')
