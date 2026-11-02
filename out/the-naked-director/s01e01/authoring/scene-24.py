ID = 'the-naked-director-s01e01-scene-24'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 24
TITLE = '金がないと自由になれない  (Without Money, You Cannot Be Free)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kozue': 'こずえ', 'konosuke': '幸之助', 'muranishi': '村西'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Alone in his quiet house, the protagonist remembers post-war Fukushima when he was a boy. "
    "His mother discovers his father spent the money meant to buy rice for his younger brother—and later that night, his father whispers a bitter lesson about money and freedom. "
    "Listen to this childhood memory."
)

STORY = [
    ('kozue', '仕事に戻って稼いでくればいいだろう！', 'You should go back to work and earn money!', [(541, '戻って稼いでくればいい')], 'Rendered northern dialect into standard Japanese.'),
    ('konosuke', '黙ってろ！', 'Keep quiet!', [(542, '黙ってろ')], ''),
    ('kozue', 'あんた、まさか。', 'Wait—surely you did not.', [(543, 'あんた まさか')], ''),
    ('kozue', 'あれはとおるに米を食べさせるお金だったのに！', 'That was the money to feed rice to Toru!', [(544, 'あれは とおるに 米を')], 'Standardised 食わせる金だったっぺ to 食べさせるお金だったのに.'),
    ('konosuke', 'うるさい！', 'Shut up!', [(545, 'うるせえ')], 'Standardised うるせえ to うるさい.'),
    ('muranishi', 'やめろ！', 'Stop it!', [(552, 'やめろ')], ''),
    ('kozue', 'お前、何をやってるんだ！', 'What on earth are you doing!', [(558, '何やってんだ')], 'Standardised おめえ to お前 and added を.'),
    ('kozue', 'ごめんなさい、ごめんなさい。', 'I am sorry, I am so sorry.', [(559, 'ごめん')], 'Standardised dialect ごめんない to ごめんなさい.'),
    ('muranishi', '父ちゃん。', 'Dad.', [(562, '父ちゃん')], ''),
    ('muranishi', '父ちゃん、ごめんな。許してくれ。', 'Dad, I am sorry. Please forgive me.', [(563, '父ちゃん ごめんな'), (563, '許して')], 'Standardised dialect 許してくんちぇ to 許してくれ.'),
    ('konosuke', '結局、金がないと自由にもなれないんだな。', 'In the end, without money you cannot even become free.', [(564, '結局'), (564, '自由にもなれ')], 'Standardised 金がねえと自由にもなれねえんだな.'),
    ('muranishi', '金と自由か。', 'Money and freedom, huh.', [], 'Quiet reflection echoing Konosuke’s words back in 1980.'),
]

OPENER = "Even in these raw childhood memories, the everyday words are short and direct. Let's look at each one."

WALK = [
    (0, None, [
        '"\'You should go back to work and earn money!\' The word for returning is " Watch for ',
        (None, "戻って"), ", and ",
        (None, "稼いで"), " this word means to earn."
    ]),
    (1, None, [
        "'Keep quiet!'  You can catch ",
        (None, "黙ってろ"), " this word crushes the longer phrase for 'stay silent' into a harsh, clipped command to shut one's mouth."
    ]),
    (2, None, [
        '"\'Wait—surely you did not.\' Whenever a dreadful suspicion hits you, " Notice how ',
        (None, "まさか"), " literally gasps 'no way—don't tell me...!'"
    ]),
    (3, None, [
        '"\'That was the money to feed rice to Toru!\' Uncooked rice is " The character says ',
        (None, "米"), " (cooked rice in a bowl this word is a different word). ",
        (None, "食べさせる"), " turns the verb for eating into 'let him eat' or 'feed him'."
    ]),
    (7, None, [
        '"\'I am sorry, I am so sorry.\' Here is full, heartfelt " Pay attention to ',
        (None, "ごめんなさい"), ", more personal and emotional within a family than businesslike apologies."
    ]),
    (8, None, [
        '"\'Dad.\' Rustic, affectionate " It features ',
        (None, "父ちゃん。"), " literally means 'Dad'—warmer and rougher than the textbook word for father."
    ]),
    (9, '許してくれ。', [
        '"\'Please forgive me.\' The verb for forgiving turns into plain " The character says ',
        (None, "許してくれ"), " to beg a family member for forgiveness."
    ]),
    (10, None, [
        "'In the end, without money you cannot even become free.'  They are saying ",
        (None, "結局"), " literally sums things up with 'in the end' or 'after all'. Then ",
        (None, "金がないと"), ", without money, leads into ",
        (None, "自由にもなれない"), ", 'cannot even become free'."
    ]),
    (11, None, [
        '"\'Money and freedom, huh.\' Linking two big ideas with " Check out ',
        (None, "と"), "—",
        (None, "金"), ", money, and ",
        (None, "自由"), ", freedom—and ending on musing ",
        (None, "か"), " shows him turning his father's words over in his mind."
    ]),
]

TRANSITION = "Now let's hear the Fukushima flashback again."

OUTRO = (
    "Remember the expression for 'surely not!', the phrase for heartfelt apologies, "
    "and the word for summing up what something comes down to in the end. "
    "Next, our protagonist wanders into Sapporo's Susukino night district."
)
CLOSING = ('muranishi', 'また会いましょう。')
