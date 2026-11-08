# Authoring module for linden-courtyard-ko-s01e03-scene-04.
ID = 'linden-courtyard-ko-s01e03-scene-04'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = 'In from the Rain  (빗속에서 들어온 손님)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb', 'tessa': 'Tessa'}
INTRO = '차가운 가을비를 맞으며 조용한 인상의 손님 케일럽이 여관 안으로 들어와요. 해나와 테사는 마른 수건과 뜨거운 수프로 먼저 몸을 녹여 드린 뒤 이중 예약 사실을 솔직하게 털어놓습니다. 두근거리는 첫 만남을 들어 보세요.'
OPENER = '이제 비를 뚫고 도착한 케일럽과의 대화를 한 문장씩 살펴볼까요.'
TRANSITION = '그럼 정중하고 따뜻한 이 장면을 자연스러운 속도로 다시 들어 보세요.'
OUTRO = '진심 어린 사과와 정성껏 준비한 다락방 서재 이야기에 케일럽이 먼저 방을 보겠다고 답했어요. 과연 깐깐해 보이는 이 손님의 마음에 다락방이 쏙 들 수 있을까요. 다음 장면에서 바로 이어집니다.'
CLOSING = ('caleb', 'See you soon!')
STORY = [
    ('hannah', 'Good evening! Come inside out of the rain, sir.', '좋은 저녁이에요! 비 맞지 마시고 어서 안으로 들어오세요, 손님.'),
    ('caleb', 'Good evening. Sorry for dripping water on your clean floor.', '좋은 저녁입니다. 깨끗한 바닥에 빗물을 뚝뚝 떨어뜨려 죄송해요.'),
    ('hannah', 'Do not worry at all! You must be Caleb.', '전혀 걱정하지 마세요! 케일럽 씨 맞으시죠.'),
    ('caleb', 'Yes, Caleb. I booked room seven by phone yesterday.', '네, 케일럽입니다. 어제 전화로 칠 호실을 예약했어요.'),
    ('tessa', 'Here is a dry towel for your coat and a cup of hot soup, sir.', '외투 닦으실 마른 수건과 뜨거운 수프 한 컵 여기 있습니다, 손님.'),
    ('caleb', 'Hot soup? After that cold walk in the rain, that sounds wonderful.', '뜨거운 수프라고요? 빗속을 춥게 걸어왔더니 정말 반가운 말씀이네요.'),
    ('hannah', 'Sir, before we go upstairs, I owe you an honest apology.', '손님, 위층으로 올라가기 전에 솔직한 사과를 먼저 드려야 할 것 같아요.'),
    ('caleb', 'Oh? Is there a problem with my booking?', '어라? 제 예약에 무슨 문제라도 있나요?'),
    ('hannah', 'We accidentally booked two guests into room seven tonight.', '저희가 실수로 오늘 밤 칠 호실에 손님 두 분을 예약해 버렸어요.'),
    ('caleb', 'Ah... in this rain? Every hotel near the station looked full.', '아, 이런 빗속에요? 역 근처 호텔은 전부 만실로 보이던데요.'),
    ('hannah', 'Please do not worry! We prepared our quiet third floor attic study just for you.', '부디 걱정하지 마세요! 오직 손님만을 위해 조용한 삼 층 다락방 서재를 준비해 두었거든요.'),
    ('caleb', 'An attic study? May I see it first?', '다락방 서재요? 제가 먼저 한번 봐도 될까요?'),
]
WALK = [
    (0, None, ["'좋은 저녁이에요! 비 맞지 마시고 어서 안으로 들어오세요, 손님.' 궂은 날씨 속에서 실내로 어서 피하라고 반갑게 맞이할 때는", (None, 'inside out of the rain'), '방향을 나타내는 말을 겹쳐 비에서 벗어나 안으로 오라는 뜻을 살려요.']),
    (1, None, ["'좋은 저녁입니다. 깨끗한 바닥에 빗물을 뚝뚝 떨어뜨려 죄송해요.' 자신의 실수나 행동에 대해 가볍게 사과를 건넬 때는", (None, 'Sorry for dripping'), '전치사 뒤에 동명사를 바로 이어 무엇이 미안한지 구체적으로 밝혀요.']),
    (2, None, ["'전혀 걱정하지 마세요! 케일럽 씨 맞으시죠.' 부정문 끝에 붙어 조금도 신경 쓸 필요 없다고 강조할 때는", (None, 'at all'), '부정 표현과 단짝을 이루는 이 두 단어로 상대의 부담을 덜어 줘요.']),
    (3, None, ["'네, 케일럽입니다. 어제 전화로 칠 호실을 예약했어요.' 통신 수단이나 교통수단을 말할 때는 관사 없이", (None, 'by phone'), '전치사와 단수 명사만 간결하게 붙여 예약 방식을 설명해요.']),
    (4, None, ["'외투 닦으실 마른 수건과 뜨거운 수프 한 컵 여기 있습니다, 손님.' 상대방에게 필요한 물건을 정중히 건네며 챙겨 드릴 때는", (None, 'Here is a dry towel'), '가까운 곳을 가리키는 말로 시작해 자연스럽게 물건을 내밀어요.']),
    (5, None, ["'뜨거운 수프라고요? 빗속을 춥게 걸어왔더니 정말 반가운 말씀이네요.' 상대의 제안이 귀가 번쩍 뜨일 만큼 좋게 들릴 때는", (None, 'that sounds wonderful'), '감각 동사를 활용해 제안을 들은 기쁜 마음을 표현해요.']),
    (6, None, ["'손님, 위층으로 올라가기 전에 솔직한 사과를 먼저 드려야 할 것 같아요.' 마땅히 드려야 할 사과나 감사가 있다고 정중히 운을 뗄 때는", (None, 'I owe you'), '빚지고 있다는 뜻의 동사를 써서 진심 어린 책임감을 나타내요.']),
    (7, None, ["'어라? 제 예약에 무슨 문제라도 있나요?' 뜻밖의 말에 상황의 이상 유무를 차분하게 되물을 때는", (None, 'Is there a problem'), '존재를 묻는 의문문 틀로 곤란한 일이 생겼는지 확인해요.']),
    (8, None, ["'저희가 실수로 오늘 밤 칠 호실에 손님 두 분을 예약해 버렸어요.' 이미 지나간 시점에 장부에 기록한 일을 말할 때는 불규칙 과거형", (None, 'booked'), '모음이 바뀐 이 한 단어로 과거의 실수를 정확하게 전달해요.']),
    (9, None, ["'아, 이런 빗속에요? 역 근처 호텔은 전부 만실로 보이던데요.' 전체를 아우르면서도 하나하나를 개별적으로 가리킬 때는", (None, 'Every hotel'), '의미는 모두이지만 형태는 반드시 단수 명사로 맞춘다는 점을 기억해요.']),
    (10, None, ["'부디 걱정하지 마세요! 오직 손님만을 위해 조용한 삼 층 다락방 서재를 준비해 두었거든요.' 특별히 당신 한 사람을 배려했다는 따뜻한 마음을 담을 때는", (None, 'just for you'), '강조 부사를 앞에 더해 세심한 환대의 느낌을 살려 줘요.']),
    (11, None, ["'다락방 서재요? 제가 먼저 한번 봐도 될까요?' 낯선 자리에서 격식 있고 공손하게 허락을 구할 때는", (None, 'May I see it'), '정중한 조동사로 문을 열어 품위 있는 질문으로 마무리해요.']),
]
