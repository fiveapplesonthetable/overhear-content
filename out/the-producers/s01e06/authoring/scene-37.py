"""Scene 37: Please Let Me Sit Alone for a Moment."""
ID = 'the-producers-s01e06-scene-37'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 6
SCENE = 37
TITLE = '혼자 있게 해주라  (Please Let Me Sit Alone for a Moment)'
LEVEL = "A1 — beginner"
LABELS = {"joonmo": "라준모", "yejin": "탁예진"}
SOURCE_NAME = "프로듀사 (The Producers) S1.06"
SOURCE_FILE = 'sources/the-producers/s01/e06.ko.srt'

INTRO = 'Outside the hospital at night, Ra Joon-mo finds Tak Ye-jin sitting alone on a courtyard bench with her arm in a cast. As Ye-jin breaks down blaming herself for hurting Cindy and burdening him, Joon-mo quietly pulls her into an embrace.'

STORY = [
    ('joonmo', '신디 다쳤다며, 넌 왜 남의 프로 출연자를 다치게 하냐?', "I heard Cindy got hurt—why are you injuring a cast member from somebody else's show?", [(1092, '다쳤다며'), (1093, '넌 왜 남의 프로 출연자를')], ''),
    ('yejin', '어 다쳤어, 걔 나 때문에 다쳤다, 1206호야 올라가 봐.', 'Yeah, she got hurt because of me—she is in Room 1206, go on up and see her.', [(1094, '어 다쳤어'), (1095, '걔 나 때문에 다쳤다'), (1096, '1206호야 올라가 봐')], ''),
    ('yejin', '내가 얼마나 칠칠치 못하면, 너 언젠가 한번 사고 칠 줄 알았지?', 'How clumsy can I get—you always knew I would cause an accident someday, right?', [(1097, '내가 얼마나 칠칠치 못하면'), (1098, '너 언젠가 한번 사고 칠 줄 알았')], ''),
    ('joonmo', '그만해라, 어디 봐 얼마나 어떻게 다쳤어?', 'Stop talking like that—let me see where and how badly you hurt yourself.', [(1099, '그만해라'), (1100, '어디 봐 얼마나'), (1100, '어떻게 다치')], ''),
    ('yejin', '아우 놔!', 'Ugh, let go of my arm!', [(1101, '아우 놔')], ''),
    ('yejin', '칠칠치 못한 내가 사고 치고 너희 출연자 다치게 하고,', "Clumsy me caused an accident and got your show's cast member injured.", [(1102, '칠칠치 못한 내가 사고치고'), (1103, '출연자 다치게 하고')], ''),
    ('yejin', '너한테 민폐 끼치고 너 불편하게 만들었다, 진짜 미안하다!', 'I caused trouble for you and made you uncomfortable—I am truly sorry!', [(1104, '너한테'), (1105, '너 불편하게 만들었다'), (1106, '진짜 미안하다')], ''),
    ('joonmo', '야, 너 우니?', 'Hey—are you crying?', [(1107, '야'), (1108, '너')], ''),
    ('yejin', '혼자 있게 해주라.', 'Please just leave me alone for a bit.', [(1110, '혼자 있게 해주라')], ''),
    ('joonmo', '미안해, 오늘.', 'I am sorry about today.', [(1111, '미안해 오늘')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'I heard Cindy got hurt—why are you injuring a cast member from somebody else's show?'"),
    (1, None, "'Yeah, she got hurt because of me—she is in Room 1206, go on up and see her.'"),
    (2, None, "'How clumsy can I get—you always knew I would cause an accident someday, right?'"),
    (3, None, "'Stop talking like that—let me see where and how badly you hurt yourself.'"),
    (4, None, "'Ugh, let go of my arm!'"),
    (5, None, "'Clumsy me caused an accident and got your show's cast member injured.'"),
    (6, None, "'I caused trouble for you and made you uncomfortable—I am truly sorry!'"),
    (7, None, "'Hey—are you crying?'"),
    (8, None, "'Please just leave me alone for a bit.'"),
    (9, None, "'I am sorry about today.'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Checking on an injured friend, apologizing through tears for causing trouble, and offering silent comfort brings Episode 6 to an emotional close. Until next time!'
CLOSING = ('joonmo', '다음에 또 만나요!')
