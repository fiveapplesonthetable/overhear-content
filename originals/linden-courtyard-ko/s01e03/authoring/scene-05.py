# Authoring module for linden-courtyard-ko-s01e03-scene-05.
ID = 'linden-courtyard-ko-s01e03-scene-05'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 3
SCENE = 5
TITLE = 'Half Price and Quiet Beams  (반값 할인과 고요한 들보)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb', 'graham': 'Graham'}
INTRO = '삼 층 다락방에 올라온 케일럽은 팔십 년 된 참나무 천장 들보와 거리 소음이 전혀 들리지 않는 고요함에 감탄해요. 반값 할인과 무료 조식 안내까지 듣고 나자 오히려 일 층보다 훨씬 마음에 든다며 반가워합니다. 대화를 들어 보세요.'
OPENER = '그럼 다락방에서 나눈 훈훈한 대화를 한 문장씩 함께 살펴볼까요.'
TRANSITION = '이제 안도감이 감도는 이 장면을 자연스러운 속도로 다시 들어 보세요.'
OUTRO = '케일럽이 은색 열쇠를 기쁘게 받아 들면서 이중 예약 소동은 멋지게 해결되었어요. 고요한 창가 책상에서 편안한 밤을 보내게 되어 모두 마음이 놓이네요. 다음 장면에서 이어지는 이야기를 만나 봐요.'
CLOSING = ('hannah', 'Good night!')
STORY = [
    ('hannah', 'Here we are, sir. Watch your head on this low wooden beam.', '다 왔습니다, 손님. 이 낮은 나무 들보에 머리 부딪히지 않게 조심하세요.'),
    ('caleb', 'Oh... look at the proportions of this timber roof!', '오, 이 목재 지붕의 비례미 좀 보세요!'),
    ('graham', 'Solid oak, eighty years old. Not a single leak.', '단단한 참나무로 팔십 년이나 되었죠. 물 한 방울 새는 곳이 없습니다.'),
    ('hannah', 'Because of our mistake, tonight is half price, with breakfast included.', '저희 실수 때문에 오늘 밤은 반값이고 아침 식사도 포함되어 있습니다.'),
    ('caleb', 'Listen for a second... you cannot hear a single car from the street.', '잠깐만 들어 보세요. 거리에서 지나가는 차 소리가 단 한 대도 안 들리네요.'),
    ('hannah', 'Only the courtyard tree and the rain.', '오직 안뜰의 나무와 빗소리뿐이죠.'),
    ('caleb', 'To tell you the truth, I hate noisy first floor rooms. I love this space!', '솔직히 말씀드리면 저는 시끄러운 일 층 방을 싫어하거든요. 이 공간이 정말 마음에 들어요!'),
    ('graham', 'Really? You do not mind the extra stairs?', '정말요? 계단을 더 올라오시는 건 괜찮으신가요?'),
    ('caleb', 'Not at all! And this wide desk under the window is ideal for my work.', '전혀 괜찮습니다! 게다가 창문 아래 이 넓은 책상은 제 작업에 안성맞춤이에요.'),
    ('hannah', 'What a relief! Here is your silver key, Caleb.', '정말 다행이네요! 여기 은색 열쇠 받으세요, 케일럽.'),
    ('caleb', 'Thank you both for being honest instead of sending me back into the rain.', '저를 다시 빗속으로 돌려보내는 대신 솔직하게 말씀해 주셔서 두 분 모두 감사합니다.'),
    ('graham', 'Sleep well, sir. Breakfast starts at seven thirty downstairs.', '푹 주무십시오, 손님. 아침 식사는 아래층에서 일곱 시 반에 시작합니다.'),
]
WALK = [
    (0, None, ["'다 왔습니다, 손님. 이 낮은 나무 들보에 머리 부딪히지 않게 조심하세요.' 천장이 낮은 곳을 지날 때 머리를 조심하라고 일러 주는 표현으로", (None, 'Watch your head'), '일상에서 위험을 바로 알려 주는 아주 실용적인 인사말이에요.']),
    (1, None, ["'오, 이 목재 지붕의 비례미 좀 보세요!' 건축물의 뼈대를 이루는 굵직한 재목이나 목재를 가리킬 때는", (None, 'timber'), '일반 나무보다 건축 자재의 느낌을 살려 주는 이 명사를 사용해요.']),
    (2, None, ["'단단한 참나무로 팔십 년이나 되었죠. 물 한 방울 새는 곳이 없습니다.' 사람이나 건물의 나이를 서술 자리에서 풀어 말할 때는", (None, 'eighty years old'), '줄임표 없이 복수 명사를 그대로 살려 세월의 깊이를 전해 줘요.']),
    (3, None, ["'저희 실수 때문에 오늘 밤은 반값이고 아침 식사도 포함되어 있습니다.' 문장이 아니라 명사구 앞에서 원인을 간결하게 밝힐 때는", (None, 'Because of'), '전치사까지 함께 붙은 이 구절로 이유를 매끄럽게 연결해요.']),
    (4, None, ["'잠깐만 들어 보세요. 거리에서 지나가는 차 소리가 단 한 대도 안 들리네요.' 주변이 워낙 조용해 아무 소리도 귀에 들어오지 않는다는 뜻은", (None, 'you cannot hear'), '일반적인 사람을 주어로 삼아 누구에게나 들리지 않음을 강조해요.']),
    (5, None, ["'오직 안뜰의 나무와 빗소리뿐이죠.' 앞에 나온 명사가 뒤에 오는 명사를 형용사처럼 꾸며 줄 때는", (None, 'courtyard tree'), '안뜰이라는 공간 명사를 바로 앞에 두어 어떤 나무인지 짚어 줘요.']),
    (6, None, ["'솔직히 말씀드리면 저는 시끄러운 일 층 방을 싫어하거든요. 이 공간이 정말 마음에 들어요!' 건물의 가장 아래층에 있는 객실을 가리켜 말할 때는", (None, 'first floor'), '기수 대신 서수를 써서 층수를 차례대로 세어 표현해요.']),
    (7, None, ["'정말요? 계단을 더 올라오시는 건 괜찮으신가요?' 혹시 불편하거나 꺼려지지는 않는지 세심하게 배려하며 물을 때는", (None, 'You do not mind'), '평서문 어순의 끝을 살짝 올려 상대의 속마음을 부드럽게 확인해요.']),
    (8, None, ["'전혀 괜찮습니다! 게다가 창문 아래 이 넓은 책상은 제 작업에 안성맞춤이에요.' 상대가 괜찮냐고 물었을 때 조금도 상관없다고 흔쾌히 답하려면", (None, 'Not at all'), '경쾌한 이 세 단어로 상대방의 걱정을 말끔히 덜어 줄 수 있어요.']),
    (9, None, ["'정말 다행이네요! 여기 은색 열쇠 받으세요, 케일럽.' 조마조마했던 마음이 한순간에 놓이며 안도의 한숨이 나올 때는", (None, 'What a relief'), '감탄문 형식을 빌려 가슴을 쓸어내리는 기분을 생생히 전해요.']),
    (10, None, ["'저를 다시 빗속으로 돌려보내는 대신 솔직하게 말씀해 주셔서 두 분 모두 감사합니다.' 어떤 행동 대신 다른 선택을 해 주었다고 비교해 말할 때는", (None, 'instead of sending'), '전치사 뒤에 동명사를 이어 붙여 하지 않은 행동을 자연스레 밝혀요.']),
    (11, None, ["'푹 주무십시오, 손님. 아침 식사는 아래층에서 일곱 시 반에 시작합니다.' 잠자리에 드는 사람에게 편안한 밤을 기원하며 건네는 인사는", (None, 'Sleep well'), '동사와 부사 단 두 단어로 다정한 마음을 담백하게 전해요.']),
]
