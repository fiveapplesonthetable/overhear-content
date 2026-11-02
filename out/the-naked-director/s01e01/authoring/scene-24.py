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
    "Alone in his quiet house, Muranishi remembers post-war Fukushima when he was a boy. "
    "His mother Kozue discovers his father Konosuke spent the money meant to buy rice for young Toru—and later that night, Konosuke whispers a bitter lesson about money and freedom. "
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
    (0, None, "'You should go back to work and earn money!' \"Modotte\" comes from \"modoru\", to return, and \"kasegu\" means to earn a living."),
    (1, None, "'Keep quiet!' \"Damattero\" crushes \"damatte iro\", stay silent, into a harsh, clipped command from \"damaru\", to shut one's mouth."),
    (2, None, "'Wait—surely you did not.' Whenever a dreadful suspicion hits you, \"masaka\" gasps 'no way—don't tell me...!'"),
    (3, None, "'That was the money to feed rice to Toru!' Uncooked rice is \"kome\" (cooked rice in a bowl is \"gohan\"). \"Tabesaseru\" turns \"taberu\", to eat, into 'let him eat' or 'feed him'."),
    (7, None, "'I am sorry, I am so sorry.' Here is full, heartfelt \"gomennasai\", more personal and emotional within a family than businesslike \"sumimasen\"."),
    (8, None, "'Dad.' Rustic, affectionate \"touchan\" is like 'Dad'—warmer and rougher than textbook \"otousan\"."),
    (9, '許してくれ。', "'Please forgive me.' \"Yurusu\" means to forgive or pardon, and plain \"yurushite kure\" begs a family member for forgiveness."),
    (10, None, "'In the end, without money you cannot even become free.' \"Kekkyoku\" sums things up with 'in the end' or 'after all'. Then \"kane ga nai to\", without money, leads into \"jiyuu ni mo narenai\", 'cannot even become free'."),
    (11, None, "'Money and freedom, huh.' Linking two big ideas with \"to\"—\"kane\", money, and \"jiyuu\", freedom—and ending on musing \"ka\" shows Muranishi turning his father's words over in his mind."),
]

TRANSITION = "Now let's hear the Fukushima flashback again."

OUTRO = (
    "Remember \"masaka\" for 'surely not!', \"gomennasai\" for heartfelt apologies, "
    "and \"kekkyoku\" when summing up what something comes down to in the end. "
    "Next, Muranishi wanders into Sapporo's Susukino night district."
)

CLOSING = ('muranishi', 'また会いましょう。')
