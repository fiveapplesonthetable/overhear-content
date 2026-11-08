# Authoring module for haessal-guesthouse-s01e03-scene-04.
ID = 'haessal-guesthouse-s01e03-scene-04'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = '빗속에서 온 손님  (In from the Rain)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'mina': '미나', 'jihoon': '지훈', 'sora': '소라'}
INTRO = 'Down in the lobby, quiet thirty-something traveller Jihoon steps inside shaking out a wet umbrella. Mina greets him at the desk while Sora brings a warm towel. Listen first.'
OPENER = "Now let's hear how Mina breaks the news gently."
TRANSITION = "Now let's listen to the whole lobby greeting again."
OUTRO = 'Honesty, a dry towel, and a cup of hot soup kept the conversation calm. Next time, Jihoon climbs the stairs to judge the attic room for himself.'
CLOSING = ('jihoon', '또 만나요!')
STORY = [
    ('mina', '어서 오세요! 비가 많이 오는데 안으로 들어오세요, 손님.', 'Welcome! It is raining hard—please come inside, sir.'),
    ('jihoon', '안녕하세요. 깨끗한 바닥에 빗물을 떨어뜨려서 죄송합니다.', 'Good evening. Sorry for dripping rainwater on your clean floor.'),
    ('mina', '전혀 괜찮아요! 지훈 님이시죠?', 'Not a problem at all! You must be Mr Jihoon, right?'),
    ('jihoon', '네, 지훈입니다. 어제 전화로 칠호실을 예약했어요.', 'Yes, I am Jihoon. Yesterday I booked Room 7 by phone.'),
    ('sora', '손님, 코트 닦으실 마른 수건하고 따뜻한 수프 한 컵 드릴게요.', 'Sir, here are a dry towel for your coat and a cup of warm soup.'),
    ('jihoon', '뜨거운 수프라고요? 빗속을 춥게 걸어왔더니 정말 반가운 말씀이네요.', 'Hot soup? After that cold walk in the rain, that sounds wonderful.'),
    ('mina', '손님, 위층으로 올라가기 전에 솔직하게 사과드릴 일이 있어요.', 'Sir, before we head upstairs, I owe you an honest apology.'),
    ('jihoon', '네? 제 예약에 무슨 문제가 있나요?', 'Oh? Is there some problem with my booking?'),
    ('mina', '오늘 밤 칠호실에 실수로 손님 두 명을 예약해 버렸어요.', 'We accidentally booked two guests into Room 7 tonight.'),
    ('jihoon', '아... 이렇게 비가 오는데요? 역 근처 호텔은 다 만실 같았어요.', 'Ah... in rain like this? Every hotel near the station looked full.'),
    ('mina', '걱정하지 마세요! 손님을 위해 조용한 삼층 다락방 서재를 정성껏 준비했어요.', 'Please do not worry! Just for you, we lovingly prepared our quiet third-floor attic study.'),
    ('jihoon', '다락방 서재요? 먼저 올라가서 봐도 될까요?', 'An attic study? May I go up and see it first?'),
]
WALK = [
    (0, None, ["'Welcome! It is raining hard—please come inside, sir.' Welcoming someone indoors uses the polite phrase ", (None, '안으로 들어오세요'), ", meaning 'please come inside'."]),
    (1, None, ["'Good evening. Sorry for dripping rainwater on your clean floor.' Rain and water fuse into ", (None, '빗물을'), ", 'rainwater'."]),
    (4, None, ["'Sir, here are a dry towel for your coat and a cup of warm soup.' Contrast wet clothes with the Korean chunk ", (None, '마른 수건하고'), ", where the first word means 'dry'."]),
    (6, None, ["'Sir, before we head upstairs, I owe you an honest apology.' Offering a sincere workplace apology uses ", (None, '사과드릴'), ", humble for 'give an apology'."]),
    (7, None, ["'Oh? Is there some problem with my booking?' Checking calmly whether something went wrong uses the handy phrase ", (None, '문제가 있나요'), ", 'is there a problem?'."]),
    (9, None, ["'Ah... in rain like this? Every hotel near the station looked full.' Hotels with zero vacancies post the two-syllable word ", (None, '만실'), ", literally 'full rooms'."]),
    (10, None, ["'Please do not worry! Just for you, we lovingly prepared our quiet third-floor attic study.' Doing work with wholehearted care is ", (None, '정성껏'), '.']),
    (11, None, ["'An attic study? May I go up and see it first?' Polite permission questions end smoothly with ", (None, '봐도 될까요'), ", literally 'even if I look, will it be okay?'."]),
]
