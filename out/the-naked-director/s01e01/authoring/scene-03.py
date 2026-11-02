ID = 'the-naked-director-s01e01-scene-03'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = '外でやれ  (Take It Outside)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'student': '生徒', 'muranishi': '村西'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "The story jumps back to Sapporo in 1980. "
    "Instead of making door-to-door sales calls, Toru Muranishi is killing time inside a noisy coffeehouse arcade. "
    "When schoolboys start shouting over a tabletop video game, Muranishi snaps at them. "
    "Listen to the rough, casual speech first."
)

STORY = [
    ('student', 'いつまでやってんだ！', 'How long are you going to keep playing!', [(41, 'いつまでやってんだ')], ''),
    ('student', 'もう少しでハイスコアだったのに！', 'I almost had the high score!', [(42, 'もう少しで ハイスコアだったのに')], 'Trimmed rough final particle.'),
    ('student', 'お前、どこだ？', 'Where are you from?', [(43, 'どこだ')], 'Standardised おめえ to お前.'),
    ('student', '北高だ。', 'Kita High.', [(44, '高だ')], 'Kept school name short and clear.'),
    ('student', 'そっちこそどこだ！', 'Where are you from yourself!', [(45, 'こそ どこだ')], 'Softened rough pronoun てめえ to そっち.'),
    ('student', '西中だ！', 'Nishi Middle School!', [(45, '中だ')], ''),
    ('muranishi', 'うるさいな、外でやれ！', 'Shut up, take it outside!', [(49, '外でやれ')], 'Standardised うるせえな to うるさいな.'),
    ('student', '外ではゲームできないだろう。', 'We cannot play the game outside, obviously.', [(51, 'ゲーム')], 'Standardised casual contractions for A1 clarity.'),
    ('student', 'こっちはまだ終わっていない。', 'I am not finished over here yet.', [(52, 'こっち まだ')], 'Expanded contracted negative.'),
    ('student', '痛い！', 'Ouch!', [(56, 'いって')], 'Standardised elongated slang いって to 痛い.'),
    ('student', '行くぞ！', 'Here we go!', [(58, 'いくぞ')], 'Written with kanji 行く.'),
    ('muranishi', 'ここは札幌の喫茶店だぞ。', 'This is a coffeehouse in Sapporo, you know.', [(60, '札幌')], 'Adapted from the background Sapporo announcement to ground location.'),
]

OPENER = "Teenagers arguing over an arcade machine drop almost every polite ending. Let's unpack what they are shouting."

WALK = [
    (0, None, "'How long are you going to keep playing!' \"Itsu\" means when, and adding \"made\" stretches it into 'until when' or 'how long'. At the end, \"yatte nda\" squeezes \"yatte iru no da\", 'are you doing it', into fast street talk."),
    (1, None, "'I almost had the high score!' \"Mou sukoshi de\" literally says 'with a little bit more', the go-to chunk for 'almost'. Trailing off with \"noni\" lets frustration hang in the air—'even though I was so close!'"),
    (2, None, "'Where are you from?' Rough \"omae\" points straight at 'you' among boys picking a fight—never use it with strangers in real life. \"Doko da\" simply asks 'where is it?', leaving 'your school' unspoken."),
    (3, None, "'Kita High.' \"Kita\" means north, and \"kou\" shortens \"koukou\", high school, just as \"Nishi\" means west in the rival boy's answer."),
    (4, None, "'Where are you from yourself!' Putting \"koso\" right after \"socchi\", your side, bounces the question right back—'you are the one who should answer!'"),
    (6, None, "'Shut up, take it outside!' Muranishi barks \"urusai\", noisy or annoying, softened only slightly by grumbling \"na\". Then \"soto de yare\" puts \"soto\", outside, before the blunt command \"yare\", do it!"),
    (7, None, "'We cannot play the game outside, obviously.' \"Soto de wa\" contrasts 'outdoors' with inside the cafe. \"Dekinai\" means cannot do, and \"darou\" nudges the listener with 'right?' or 'obviously'."),
    (8, None, "'I am not finished over here yet.' Pairing \"mada\", still or yet, with negative \"owatte inai\", has not ended, gives you the natural Japanese pattern for 'not finished yet'."),
    (9, None, "'Ouch!' One word, \"itai\", covers both 'it hurts' as a description and 'ouch!' as a sudden cry when somebody bumps you."),
    (10, None, "'Here we go!' \"Iku\", to go, plus tough masculine \"zo\" turns a plain statement into a rallying shout."),
    (11, None, "'This is a coffeehouse in Sapporo, you know.' \"Koko\" points to right here, and \"kissaten\" is a traditional Japanese coffee shop where salarymen linger over coffee."),
]

TRANSITION = "Now let's hear the whole arcade argument play out again."

OUTRO = (
    "Notice the contrast between polite studio Japanese in scene one and blunt street talk here: "
    "\"itsu made\" for 'until when', \"mada\" with a negative for 'not yet', and \"itai\" whenever something hurts. "
    "See you in the next scene."
)

CLOSING = ('muranishi', 'じゃあね。')
