"""Scene 20: This Guy Is Writing Fiction Again!."""
ID = 'the-producers-s01e07-scene-20'
PAIR = "ko-en"
SHOW = 'the-producers'
SEASON = 1
EPISODE = 7
SCENE = 20
TITLE = '얘 또 소설 쓴다!  (This Guy Is Writing Fiction Again!)'
LEVEL = "A1 — beginner"
LABELS = {"colleague": "PD 동료", "joonmo": "라준모", "taeho": "김태호"}
SOURCE_NAME = '프로듀사 (The Producers) S1.07'
SOURCE_FILE = 'sources/the-producers/s01/e07.ko.srt'

INTRO = "At a Korean barbecue restaurant, Kim Tae-ho and a fellow producer tell Ra Joon-mo that eyewitnesses claim to have spotted Cindy in Paris. Within seconds, the colleague launches into an even wilder conspiracy theory about the office supply clerk's expensive clothes."

STORY = [
    ('taeho', '변 대표네서 뭐 연락 받은 거 없어?', "Have you not heard anything from CEO Byun's agency?", [(406, '뭐 연락받은 거 없어')], ''),
    ('joonmo', '아유, 없다니까!', 'Ugh, I keep telling you I have not!', [(407, '아유 없다니까')], ''),
    ('taeho', '나도 아까 들었는데 신디가 재벌 2세랑 눈이 맞아서 파리의 어디 호텔에 있다는데.', 'I heard earlier too that Cindy hit it off with a chaebol heir and is at some hotel in Paris.', [(408, '나도 아까 들었는데 신디가'), (408, '눈이 맞아서'), (409, '파리에 어디 호텔에 있다는데')], ''),
    ('joonmo', '다리 다쳐서 깁스한 애가 무슨 파리야, 파리!', 'What business does a girl with an injured leg in a cast have in Paris?!', [(410, '다리 다쳐서 깁스한 애가 무슨 파리야 파리')], ''),
    ('colleague', '나도 들었어, 샹젤리제 거리에서 본 사람이 있대요!', 'I heard that too—they say someone spotted her on the Champs-Elysees!', [(411, '나도 들었어'), (412, '샹젤리제 거리에서 본 사람이 있대요')], ''),
    ('colleague', '아 참, 오늘 행정반 고양미 입고 온 옷 봤어요? 내가 매일 체크하고 있는데 옷을 한 번도 같은 걸 안 입어요!', 'Oh right, did you see what admin clerk Go Yang-mi wore today? I check every day and she never wears the same outfit twice!', [(416, '입고 온 옷 봤어요'), (418, '내가 여기서 매일 체크하고 있는데 옷을 한 번도 같은 걸 안 입어요')], ''),
    ('joonmo', '형, 얘만 너무 한가한 거 아니야? 뭘 그런 걸 체크하고 있냐!', 'Tae-ho, is this guy the only one with way too much free time? Why are you keeping track of that?!', [(419, '형 얘만 너무 한가한 거 아니야'), (419, '뭘 그런 걸 체크하고 있냐')], ''),
    ('colleague', '생각해봐라, 행정반 월급으로 어떻게 그렇게 비싼 걸 입냐고! 이건 고위층과 모종의 관계가 있지 않고서야…', 'Think about it—how can she wear clothes that pricey on an admin salary? Unless she has secret ties to the brass…', [(420, '생각해봐라 행정반 월급으로 어떻게 그렇게 비싼 걸 입냐고'), (423, '이건 고위층과 모종의 관계가 있지 않고서야')], ''),
    ('joonmo', '얘 또 소설 쓴다! 여기 불판 좀 바꿔줘요.', 'He is writing fiction again! Excuse me, could we get a fresh grill plate here?', [(424, '얘 또 소설 쓴다'), (425, '여기 불판 좀 바꿔줘요')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Have you not heard anything from CEO Byun's agency?'"),
    (1, None, "'Ugh, I keep telling you I have not!'"),
    (2, None, "'I heard earlier too that Cindy hit it off with a chaebol heir and is at some hotel in Paris.'"),
    (3, None, "'What business does a girl with an injured leg in a cast have in Paris?!'"),
    (4, None, "'I heard that too—they say someone spotted her on the Champs-Elysees!'"),
    (5, None, "'Oh right, did you see what admin clerk Go Yang-mi wore today? I check every day and she never wears the same outfit twice!'"),
    (6, None, "'Tae-ho, is this guy the only one with way too much free time? Why are you keeping track of that?!'"),
    (7, None, "'Think about it—how can she wear clothes that pricey on an admin salary? Unless she has secret ties to the brass…'"),
    (8, None, "'He is writing fiction again! Excuse me, could we get a fresh grill plate here?'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Dismissing far-fetched rumors over sizzling barbecue and asking the server to swap out the grill plate give you classic after-work Korean. Until next time!'
CLOSING = ('joonmo', '다음에 봐요!')
