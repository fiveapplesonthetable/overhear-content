"""Scene 29: I Have Something Urgent to Say—I Will Wait Outside Your House."""
ID = 'the-producers-s01e08-scene-29'
PAIR = "ko-en"
SHOW = 'the-producers'
SEASON = 1
EPISODE = 8
SCENE = 29
TITLE = '꼭 할 말이 있어서 집 앞에서 기다릴게요  (I Have Something Urgent to Say—I Will Wait Outside Your House)'
LEVEL = "A1 — beginner"
LABELS = {"cindy": "신디", "seungchan": "백승찬", "yejin": "탁예진"}
SOURCE_NAME = '프로듀사 (The Producers) S1.08'
SOURCE_FILE = 'sources/the-producers/s01/e08.ko.srt'

INTRO = "Delighted by Baek Seung-chan's fearless soccer performance, Tak Ye-jin lets him pick his reward—meals, drinks, or a movie—and Seung-chan immediately chooses a movie together. That evening, however, Ye-jin's phone battery dies at the theater just as Cindy calls from outside Seung-chan's house with urgent words to share."

STORY = [
    ('yejin', '어쨌든 오늘 넌 진짜 대박이었으니까 오늘 결제를 네가 원하는 대로 해줄게, 밥, 술, 영화!', "Anyway, you were sensational out there today, so I will settle today's payment however you want: dinner, drinks, or a movie!", [(849, '어쨌든 오늘 넌 진짜 대박이었으니까'), (850, '오늘 결제를 네가 원하는 대로 해줄게'), (851, '밥, 술, 영화')], ''),
    ('seungchan', '영화로 하겠습니다!', 'I will choose the movie!', [(852, '영화로 하겠습니다')], ''),
    ('yejin', '그래, 그럼 나는 집에 잠깐 가서 옷을 갈아입고 영화관으로 가지 뭐.', 'All right, then I will swing by home to change clothes and head to the movie theater.', [(853, '그래'), (854, '그럼 나는 집에 잠깐 가서 옷을 갈아입고 영화관으로 가지 뭐')], ''),
    ('seungchan', '예, 저도 회사 들러서 금방 준비해서 바로 가겠습니다.', 'Yes, I will stop by the station, get ready quickly, and head right over.', [(855, '예 저도 회사 들러서 금방 준비해서 바로 가겠습니다')], ''),
    ('yejin', '알겠어!', 'Got it!', [(856, '알겠어')], ''),
    ('cindy', '응, 나도 오늘 친구 집 간 거 처음이었어. 응, 안녕!', "Yeah, visiting a friend's house today was a first for me too—bye!", [(866, '응 나도 오늘 친구 집 간 거 처음이었어'), (870, '응 안녕')], ''),
    ('yejin', '배터리 나갔나?', 'Did the battery die?', [(876, '배터리 나갔나')], ''),
    ('cindy', '꼭 할 말이 있어서 피디님 집 앞에 와 있어요.', 'There is something I really must tell you, so I am right outside your house, Producer.', [(877, '꼭 할 말이 있어서'), (878, '피디님 집 앞에 와있어요')], ''),
    ('seungchan', '아 신디 씨, 나 지금 약속이 있어서…', 'Ah Ms. Cindy, I actually have plans right now…', [(879, '아 신디씨 나 지금 약속이 있어서')], ''),
    ('cindy', '기다릴게요.', 'I will wait for you.', [(880, '기다릴게요')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Anyway, you were sensational out there today, so I will settle today's payment however you want: dinner, drinks, or a movie!'"),
    (1, None, "'I will choose the movie!'"),
    (2, None, "'All right, then I will swing by home to change clothes and head to the movie theater.'"),
    (3, None, "'Yes, I will stop by the station, get ready quickly, and head right over.'"),
    (4, None, "'Got it!'"),
    (5, None, "'Yeah, visiting a friend's house today was a first for me too—bye!'"),
    (6, None, "'Did the battery die?'"),
    (7, None, "'There is something I really must tell you, so I am right outside your house, Producer.'"),
    (8, None, "'Ah Ms. Cindy, I actually have plans right now…'"),
    (9, None, "'I will wait for you.'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Setting up an evening movie date, a dead phone battery at the worst moment, and an unexpected call from outside the house bring this episode to a dramatic cliffhanger. Until next time!'
CLOSING = ('cindy', '또 만나요!')
