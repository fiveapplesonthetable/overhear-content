"""Scene 21: Which Do You Want to Be Scolded For First?."""
ID = 'the-producers-s01e06-scene-21'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 6
SCENE = 21
TITLE = '뭐부터 혼날래?  (Which Do You Want to Be Scolded For First?)'
LEVEL = "A1 — beginner"
LABELS = {"inpyo": "장인표", "joonmo": "라준모", "taeho": "김태호"}
SOURCE_NAME = "프로듀사 (The Producers) S1.06"
SOURCE_FILE = 'sources/the-producers/s01/e06.ko.srt'

INTRO = "Summoned to director Jang In-pyo's office alongside Kim Tae-ho, Ra Joon-mo gets chewed out for mislabeling the province in yesterday's caption. In-pyo reveals why the executive floor is furious: that county is the station president's hometown."

STORY = [
    ('inpyo', '뭐부터 혼날래, 방송사고하고 시청률?', 'Which one do you want to get chewed out for first—the broadcast accident or the ratings?', [(600, '뭐부터 혼날래'), (602, '방송사고하고 시청률')], ''),
    ('joonmo', '땡기는 것부터 하세요.', 'Start with whichever one you feel like, sir.', [(603, '땡기는 것부터 하세요')], ''),
    ('inpyo', '방송국에 시험 봐서 들어온 애가 경북 고령인지 경남 고령인지 구분이 안 되니?', 'You passed the entrance exam into a broadcasting station and cannot tell North Gyeongsang Goryeong from South Gyeongsang?', [(604, '방송국에 시험 봐서 들어온 애가 경북 고령인지 경남 고령인지'), (604, '구분이 안 되니')], ''),
    ('inpyo', '경북 고령 이상하지 않니? 경남 고령이 자연스럽지!', 'Wait—does North Gyeongsang Goryeong not sound weird? South Gyeongsang Goryeong sounds natural!', [(605, '경북 고령'), (606, '경남 고령이 자연스럽지')], ''),
    ('taeho', '국장님, 경북 고령입니다, 경남이라고 해서 사고가 난 거고요.', 'Director, it actually is North Gyeongsang Goryeong—writing South Gyeongsang is what caused the accident.', [(607, '국장님'), (608, '경북 고령입니다 경남이라고 해서 사고가 난 거고요')], ''),
    ('inpyo', '이게 이렇게 헷갈리는구나, 그럴수록 네가 더 신경을 썼어야지!', 'Oh, it really is confusing—which means you should have paid all the more attention!', [(609, '이게 이렇게 헷갈리는구나'), (612, '그럴수록 네가 더 신경을')], ''),
    ('joonmo', '고령 군청에 사과 전화 다 했고요, 다음 주에 사과 자막 넣기로 했어요.', 'We already phoned the county office to apologize and agreed to air an apology caption next week.', [(613, '고령 군청에 사과 전화 다'), (614, '사과 자막이랑 다 넣기로')], ''),
    ('inpyo', '너 지금 그게 문제가 아니야, 우리 사장님 고향이 고령이야!', "That is not the real problem right now—Goryeong is our station president's hometown!", [(615, '너 지금 그게 문제가 아니야'), (615, '우리 사장님 고향이 고령이야')], ''),
    ('taeho', '오 마이 갓!', 'Oh my goodness!', [(616, '오마이갓')], ''),
    ('inpyo', '이거 책임 소재 확실히 찾아, 그래야 나도 올라가서 보고할 때 할 말이 있지!', 'Pinpoint exactly who is responsible so I have something to say when I report upstairs!', [(616, '이거 책임 소재 확실히 찾아'), (616, '그래야 나도 올라가서 보고할 때 할 말이 있지')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Which one do you want to get chewed out for first—the broadcast accident or the ratings?'"),
    (1, None, "'Start with whichever one you feel like, sir.'"),
    (2, None, "'You passed the entrance exam into a broadcasting station and cannot tell North Gyeongsang Goryeong from South Gyeongsang?'"),
    (3, None, "'Wait—does North Gyeongsang Goryeong not sound weird? South Gyeongsang Goryeong sounds natural!'"),
    (4, None, "'Director, it actually is North Gyeongsang Goryeong—writing South Gyeongsang is what caused the accident.'"),
    (5, None, "'Oh, it really is confusing—which means you should have paid all the more attention!'"),
    (6, None, "'We already phoned the county office to apologize and agreed to air an apology caption next week.'"),
    (7, None, "'That is not the real problem right now—Goryeong is our station president's hometown!'"),
    (8, None, "'Oh my goodness!'"),
    (9, None, "'Pinpoint exactly who is responsible so I have something to say when I report upstairs!'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Apologizing for an on-air mistake, mixing up tricky place names yourself, and hunting down who is responsible gives you vivid Korean executive-office expressions. Until next time!'
CLOSING = ('taeho', '안녕히 계세요!')
