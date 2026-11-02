ID = 'the-naked-director-s01e01-scene-08'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = 'セールスにはいつ行くんですか  (When Do We Go Selling?)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'muranishi': '村西', 'ono': '小野'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "On their first morning teamed up together, Ono takes Muranishi straight to a movie theater instead of visiting customers. "
    "When Muranishi anxiously asks about work, Ono hands him a novel about a seagull and talks about freedom. "
    "Listen to their whispered conversation in the dark cinema."
)

STORY = [
    ('muranishi', '小野さん。', 'Ono-san.', [(140, '小野さん')], ''),
    ('ono', '正気か？お前。', 'Are you out of your mind?', [(141, '正気か お前')], ''),
    ('ono', '今から一番面白いパートだぞ。', 'The most exciting part is starting right now.', [(142, '今から'), (142, '一番面白いパートだぞ')], 'Trimmed aircraft names for beginner focus.'),
    ('ono', '見せ場だよ、見せ場！', 'It is the best scene, the highlight!', [(143, '見せ場だよ 見せ場')], ''),
    ('muranishi', '確かにそうみたいですけど。', 'Well, it certainly looks that way, though.', [(144, '確かに そうみたいですけど')], ''),
    ('muranishi', 'セールスにはいつ行くんですか？', 'When are we going out to do sales?', [(147, 'セールスには いつ行くんですか')], ''),
    ('ono', '気が向いたらに決まってるだろ。', 'Whenever I feel like it, obviously.', [(149, '気が向いたらに決まって')], 'Expanded 決まってんだろ to 決まってるだろ.'),
    ('ono', '君は真の自分に立ち返る自由を得たのだ。', 'You have gained the freedom to return to your true self.', [(150, '君は'), (151, '真の自分に立ち返る自由を得たのだ')], ''),
    ('muranishi', '助言ですか？ありがとうございます。', 'Is that advice? Thank you very much.', [(152, '助言ですか ありがとうございます')], ''),
    ('ono', 'ジョナサンの一節だよ。', 'It is a passage from Jonathan.', [(153, 'ジョナサン'), (153, 'の一節だよ')], 'Dropped rough insult at end of cue 153.'),
    ('muranishi', '空でやれることは何か知りたいだけなんだ。', 'I just want to know what I can do in the sky.', [(154, '空でやれることは何か'), (155, '知りたいだけなんだ')], ''),
    ('muranishi', 'ただそれだけのことさ。', 'That is all there is to it.', [(156, 'ただ それだけのことさ')], ''),
]

OPENER = "Even inside a dark theater, Muranishi worries about schedules while Ono quotes literature. Let's look closer at each line."

WALK = [
    (2, None, [
        '"\'The most exciting part is starting right now.\' Notice the word for starting right now is " Listen for ',
        (None, "今から。"),
        " and ",
        (None, "一番。"),
        ", literally number one, sits before ",
        (None, "面白い。"),
        ", interesting or fun, to say 'the most exciting'."
    ]),
    (3, None, [
        '"\'It is the best scene, the highlight!\' Here, the word for highlight is " The word ',
        (None, "見せ場。"),
        ", which joins the verb to show, with ",
        (None, "場。"),
        ", place—literally the 'showing-place', meaning the big highlight of a movie or play."
    ]),
    (4, None, [
        '"\'Well, it certainly looks that way, though.\' In this case, the word for certainly is " The phrase contains ',
        (None, "確かに。"),
        ". Trailing off on ",
        (None, "けど。"),
        ", though, is a classic Japanese way to agree politely before raising a concern."
    ]),
    (5, None, [
        '"\'When are we going out to do sales?\' Unlike English, which puts the word for \'when\' at the front, Japanese leaves " You will hear ',
        (None, "いつ。"),
        ", when, right before ",
        (None, "行く。"),
        ", to go."
    ]),
    (6, None, [
        '"\'Whenever I feel like it, obviously.\' This literally says \'if my spirit turns that way\'—a natural idiom for \'when I am in the mood\'. " In this line, ',
        (None, "気が向いたら。"),
        " comes before ",
        (None, "決まってる。"),
        ", which adds 'that is settled' or 'obviously'."
    ]),
    (7, None, [
        '"\'You have gained the freedom to return to your true self.\' Ono switches to the formal word for \'you\', " The word ',
        (None, "君。"),
        ", and dramatic ",
        (None, "得たのだ。"),
        ", 'have obtained', quoting a translation about ",
        (None, "自由。"),
        ", freedom."
    ]),
    (8, '助言ですか？', [
        '"\'Is that advice?\' Earnest Muranishi misses the quote and asks if the word for advice is " Here, the word ',
        (None, "助言。"),
        ", personal counsel or advice."
    ]),
    (9, None, [
        '"\'It is a passage from Jonathan.\' Looking closely, the word for passage means one short verse from a book—here the bestseller Jonathan Livingston Seagull. It is " You can catch ',
        (None, "一節。"),
        "."
    ]),
    (10, None, [
        '"\'I just want to know what I can do in the sky.\' Reading the page aloud, Muranishi uses the word for sky, " Hear how ',
        (None, "空。"),
        ", and ",
        (None, "知りたいだけ。"),
        ", 'only want to know', built by attaching the desire ending to the verb to know."
    ]),
    (11, None, [
        '"\'That is all there is to it.\' Using the word for just that, " The phrase contains ',
        (None, "ただ。"),
        ", and ",
        (None, "それだけ。"),
        " both reinforce 'just that and nothing more', while the breezy ",
        (None, "さ。"),
        " at the end gives the line a light, storybook tone."
    ]),
]

TRANSITION = "Now let's hear the cinema conversation from start to finish again."

OUTRO = (
    "Take away the phrase for 'the most interesting', the question asking when someone is going, "
    "and the expression for whenever you want to know something. "
    "See you out on the sales route next."
)

CLOSING = ('ono', 'じゃあね。')
