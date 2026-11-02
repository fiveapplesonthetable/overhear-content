ID = 'the-naked-director-s01e02-scene-21'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 2
SCENE = 21
TITLE = 'もう一度手を洗って  (Wash Your Hands Again)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kayo': '加代', 'megumi': '恵美'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E02'
SOURCE_FILE = 'sources/the-naked-director/s01/e02.ja.srt'

INTRO = (
    "Back at the Sahara home, Kayo calls her daughter Megumi out of the bath because dinner is on the table. "
    "What starts as a warm mealtime moment quickly turns strict again when Kayo inspects Megumi's hands. "
    "Listen to the gentle-sounding motherly commands in Japanese."
)

STORY = [
    ('kayo', '恵美さん。', 'Megumi.', [(566, '恵美さん')], ''),
    ('kayo', '早く上がりなさい。ごはんできてますから。', 'Come out of the bath soon. Dinner is ready.', [(567, '早く上がりなさい'), (567, 'ごはんできてますから')], ''),
    ('megumi', '今、出ます。', 'I am coming out now.', [(568, '出ます')], ''),
    ('kayo', 'どうかしら？', 'What do you think?', [(569, 'どうかしら')], ''),
    ('megumi', 'とってもおいしそう。', 'It looks so delicious.', [(570, 'とってもおいしそう')], ''),
    ('kayo', 'ほんと？', 'Really?', [(571, 'ホント')], 'Written in hiragana.'),
    ('kayo', 'うれしいわ。どうぞ召し上がってちょうだい。', 'That makes me happy. Please go ahead and eat.', [(572, 'うれしいわ'), (572, 'どうぞ召し上がってちょうだい')], ''),
    ('megumi', 'いただきます。', 'Thank you for this meal.', [(573, 'いただきま')], 'Normalized elongated vowel ー.'),
    ('kayo', 'その前に、もう一度手を洗ってきなさい。', 'Before that, go wash your hands one more time.', [(574, 'もう一度'), (574, '手を洗ってきなさい')], ''),
    ('megumi', 'お風呂に入りましたけど。', 'I just took a bath, though.', [(575, 'お風呂に入りましたけど')], ''),
    ('kayo', '手が汚れてるでしょ？もう一度洗ってきなさい。', 'Your hands are dirty, right? Go wash them again.', [(576, '手が汚れてるでしょ'), (576, '洗ってきなさい')], ''),
    ('megumi', 'はい。', 'Yes.', [(577, 'はい')], ''),
]

OPENER = "Even inside her own house, Kayo speaks with refined, controlling poise, while Megumi answers politely. Let's look closer at their exchange."

WALK = [
    (1, '早く上がりなさい。', "'Come out of the bath soon.' \"Hayaku\" means quickly or soon, and \"agaru\"—literally 'step up'—is the everyday action for getting out of a Japanese bath. Ending with \"nasai\" is the classic firm command a parent gives a child."),
    (1, 'ごはんできてますから。', "'Dinner is ready.' \"Gohan\" means cooked rice or any meal, and \"dekitemasu\" says it is finished and ready. Trailing \"kara\", because, gently explains why Megumi should hurry out."),
    (2, None, "'I am coming out now.' \"Ima\" means right now, paired with \"demasu\", the polite form of \"deru\", to come out or exit. Two crisp words reassure someone waiting outside a door."),
    (3, None, "'What do you think?' \"Dou\" asks 'how', and \"kashira\" adds a soft, traditionally feminine 'I wonder'. Together \"dou kashira\" asks 'how does it seem to you?'."),
    (4, None, "'It looks so delicious.' \"Tottemo\" boosts \"totemo\", very, with an extra beat of enthusiasm. Dropping the final \"i\" of \"oishii\", delicious, and adding \"sou\" shifts the meaning to 'looks delicious!'."),
    (6, 'どうぞ召し上がってちょうだい。', "'Please go ahead and eat.' \"Douzo\" warmly invites someone to go ahead. \"Meshiagatte\" comes from \"meshiagaru\", an elevated, respectful word for eating, softened at home by \"choudai\", 'please do'."),
    (7, None, "'Thank you for this meal.' Everyone in Japan says \"itadakimasu\"—literally 'I humbly receive'—right before picking up chopsticks. English has no single everyday match for this pre-meal ritual."),
    (8, None, "'Before that, go wash your hands one more time.' \"Sono mae ni\" means 'before that', and \"mou ichido\" means 'one more time'. \"Te o aratte kinasai\" chains \"arau\", wash, with \"kinasai\", telling her to go wash and come back."),
    (9, None, "'I just took a bath, though.' Japanese says \"ofuro ni hairu\"—literally 'enter the bath'—where English says 'take a bath'. Ending on \"kedo\", though, voices a quiet protest without sounding rude."),
    (10, '手が汚れてるでしょ？', "'Your hands are dirty, right?' \"Te\" is hand or hands, and \"yogoreteru\" describes being stained or dirty right now. Rising \"desho\" presses Megumi to agree rather than truly asking."),
]

TRANSITION = "Now let's listen to the whole dining-room scene again without interruption."

OUTRO = (
    "Table phrases like \"oishisou\" and \"itadakimasu\" come up at almost every Japanese meal, "
    "and \"mou ichido\" is the cleanest way to ask for something one more time. "
    "See you next time."
)

CLOSING = ('megumi', 'またね。')
