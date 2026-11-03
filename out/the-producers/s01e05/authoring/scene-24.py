"""Scene 24: Is Paper Really Your Problem?."""
ID = 'the-producers-s01e05-scene-24'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 5
SCENE = 24
TITLE = '넌 종이가 문제니?  (Is Paper Really Your Problem?)'
LEVEL = "A1 — beginner"
LABELS = {"colleague": "PD 동료", "yejin": "탁예진"}
SOURCE_NAME = "프로듀사 (The Producers) S1.05"
SOURCE_FILE = 'sources/the-producers/s01/e05.ko.srt'

INTRO = 'At her desk in the variety department, hungover Tak Ye-jin groans that she wants to cut yesterday completely out of her life. Meanwhile, a fellow producer fumes because the admin desk refuses to give his team fresh printer paper.'

STORY = [
    ('yejin', '난 그냥 나가 죽어야 될 거 같아.', 'I feel like I should just crawl into a hole and die.', [(624, '난 그냥 나가 죽어야 될 거 같아')], ''),
    ('colleague', '너 술 먹고 누구랑 또 싸웠냐?', 'Did you get drunk and get into another fight with someone?', [(625, '너 술 먹고'), (625, '또 싸웠냐')], ''),
    ('yejin', '나 그런 이미지니?', 'Is that really my image?', [(626, '나 그런 이미지니')], ''),
    ('colleague', '좀 그렇지, 아무래도.', 'Kind of, to be honest.', [(627, '좀 그렇지 아무래도')], ''),
    ('yejin', '그냥 어제를 내 인생에서 확 도려내버리고 싶다.', 'I just want to carve yesterday right out of my life.', [(628, '그냥 어제를 내 인생에서 확')], ''),
    ('colleague', '크게 싸웠구나, 합의금 물어줘야 되고 그래?', 'Must have been a huge fight—do you have to pay settlement money or something?', [(629, '크게 싸웠구나'), (630, '합의금'), (630, '되고 그래')], ''),
    ('colleague', '너네 팀이 종이 타러 가면 행정반에서 별소리 안 하고 주지?', 'When your team goes to pick up paper, the admin desk hands it over without a fuss, right?', [(632, '팀이 종이 타러 가면'), (633, '행정반에서 별소리')], ''),
    ('yejin', '넌 종이가 문제니?', 'Is paper really your problem?', [(635, '넌 종이가 문제니')], ''),
    ('colleague', '난 지금 종이가 문제야, 우리 팀만 안 주는 것 같단 말이야!', 'Paper is my problem right now—it feels like our team is the only one she refuses to give paper to!', [(636, '난 지금 종이가 문제야'), (637, '우리 팀만 안 주는 것 같단 말이야')], ''),
    ('yejin', '좋겠다, 넌 종이가 문제라서.', 'Must be nice for you, having nothing worse than paper to worry about.', [(638, '좋겠다'), (639, '넌 종이가 문제라서')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'I feel like I should just crawl into a hole and die.'"),
    (1, None, "'Did you get drunk and get into another fight with someone?'"),
    (2, None, "'Is that really my image?'"),
    (3, None, "'Kind of, to be honest.'"),
    (4, None, "'I just want to carve yesterday right out of my life.'"),
    (5, None, "'Must have been a huge fight—do you have to pay settlement money or something?'"),
    (6, None, "'When your team goes to pick up paper, the admin desk hands it over without a fuss, right?'"),
    (7, None, "'Is paper really your problem?'"),
    (8, None, "'Paper is my problem right now—it feels like our team is the only one she refuses to give paper to!'"),
    (9, None, "'Must be nice for you, having nothing worse than paper to worry about.'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Wishing you could erase an embarrassing night and envying someone with tiny office worries gives you dry, relatable Korean humor. Until next time!'
CLOSING = ('yejin', '안녕히 계세요!')
