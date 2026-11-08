# Authoring module for linden-courtyard-ko-s01e03-scene-02.
ID = 'linden-courtyard-ko-s01e03-scene-02'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 3
SCENE = 2
TITLE = 'The Sunny Attic  (아늑한 다락방)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '삼 층 다락방 문을 열자 큼직한 나무 들보와 안뜰이 내려다보이는 창문이 모습을 드러내요. 해나와 그레이엄, 그리고 테사는 빗소리가 들리는 조용한 방을 둘러보며 손님을 맞기 위해 필요한 물건들을 하나씩 챙겨 봅니다. 먼저 장면을 들어 보세요.'
OPENER = '이제 다락방에서 세 사람이 나눈 대화를 한 줄씩 함께 짚어 볼까요.'
TRANSITION = '그럼 장면 전체 대화를 자연스러운 호흡으로 다시 들어 보세요.'
OUTRO = '전등과 베개, 푸른 깔개까지 챙기기로 하니 다락방이 벌써 포근한 침실처럼 느껴지네요. 상자를 들고 계단을 내려가는 세 사람의 발걸음이 한결 가벼워졌습니다. 잠시 후 다음 장면에서 만나요.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('hannah', 'Oh, look at this room! Big wooden beams and a window over the courtyard!', '와, 이 방 좀 보세요! 커다란 나무 들보가 있고 안뜰 너머로 창문도 나 있어요!'),
    ('tessa', 'Listen to the rain on the roof. It feels so cozy up here!', '지붕 위에 내리는 빗소리 좀 들어 봐요. 여기 위는 정말 아늑하게 느껴져요!'),
    ('graham', 'Dry, warm, and quiet. Now tell me what is missing.', '건조하고 따뜻하고 조용하죠. 자, 이제 무엇이 빠져 있는지 말해 보세요.'),
    ('hannah', 'Okay: there is a bed, a table, and a chair, but no bedside lamp.', '좋아요, 침대와 탁자와 의자는 있는데 머리맡 전등이 없네요.'),
    ('tessa', 'And no mirror on the wall, and the floor feels bare without a rug.', '그리고 벽에 거울도 없고, 깔개가 없으니 바닥이 허전해 보여요.'),
    ('graham', 'There is a brass reading lamp in my workshop downstairs.', '아래층 제 작업실에 황동 독서등이 하나 있습니다.'),
    ('tessa', 'And I have two soft pillows and a woven blue rug in the closet!', '그리고 제 벽장에는 푹신한 베개 두 개와 직조된 파란 깔개가 있어요!'),
    ('hannah', 'What about the small bathroom next door? Does the light work?', '바로 옆에 있는 작은 욕실은 어때요? 전등 불은 잘 들어오나요?'),
    ('graham', 'New bulb last week, clean soap, plenty of hot water.', '지난주에 새 전구로 갈았고 깨끗한 비누에 뜨거운 물도 넉넉합니다.'),
    ('tessa', 'Give us fifteen minutes and this attic will beat room seven!', '십오 분만 주시면 이 다락방이 칠 호실을 거뜬히 이길 거예요!'),
    ('hannah', 'Grab those cardboard boxes, Graham. Down the stairs we go!', '저 판지 상자들 챙기세요, 그레이엄. 자, 계단 아래로 내려갑시다!'),
    ('graham', 'Careful on the turn, do not bump the wall!', '모퉁이 돌 때 조심해요, 벽에 부딪히지 말고요!'),
]
WALK = [
    (0, None, ["'와, 이 방 좀 보세요! 커다란 나무 들보가 있고 안뜰 너머로 창문도 나 있어요!' 눈앞의 공간에 상대의 시선을 집중시키고 싶을 때는", (None, 'look at this room'), '전치사를 꼭 챙겨서 대상을 정확히 가리켜 줘요.']),
    (1, None, ["'지붕 위에 내리는 빗소리 좀 들어 봐요. 여기 위는 정말 아늑하게 느껴져요!' 가만히 귀 기울여 소리를 느껴 보라고 권할 때는", (None, 'Listen to the rain'), '동사 뒤에 전치사를 함께 써서 무엇을 듣는지 이어 줘요.']),
    (2, None, ["'건조하고 따뜻하고 조용하죠. 자, 이제 무엇이 빠져 있는지 말해 보세요.' 문장 중간에 간접의문문을 넣어 부족한 물건을 물을 때는", (None, 'what is missing'), '의문사가 곧바로 주어 역할을 맡아 어순이 그대로 유지돼요.']),
    (3, None, ["'좋아요, 침대와 탁자와 의자는 있는데 머리맡 전등이 없네요.' 여러 가구를 나열하더라도 맨 처음 나오는 단수 명사에 맞춰", (None, 'there is a bed'), '단수 동사로 문장을 자연스럽게 열어 주는 점이 핵심이에요.']),
    (4, None, ["'그리고 벽에 거울도 없고, 깔개가 없으니 바닥이 허전해 보여요.' 그림이나 거울이 벽면에 맞닿아 걸린 위치를 나타낼 때는", (None, 'on the wall'), '표면의 접촉을 뜻하는 전치사를 골라 쓰는 습관을 들여 보세요.']),
    (5, None, ["'아래층 제 작업실에 황동 독서등이 하나 있습니다.' 아래쪽 층이라는 위치를 한 단어로 깔끔하게 덧붙일 때는", (None, 'downstairs'), '별도의 전치사 없이 이 부사 하나만 문장 끝에 놓으면 충분해요.']),
    (6, None, ["'그리고 제 벽장에는 푹신한 베개 두 개와 직조된 파란 깔개가 있어요!' 실을 촘촘히 엮어 짠 천의 질감을 표현할 때는 과거분사 형용사", (None, 'woven'), '바로 이 단어를 명사 앞에 두어 포근한 느낌을 더해 줘요.']),
    (7, None, ["'바로 옆에 있는 작은 욕실은 어때요? 전등 불은 잘 들어오나요?' 대화 주제를 자연스럽게 다른 대상으로 옮겨 물어볼 때는", (None, 'What about'), '간결한 이 두 단어로 손쉽게 새로운 질문을 꺼낼 수 있어요.']),
    (8, None, ["'지난주에 새 전구로 갈았고 깨끗한 비누에 뜨거운 물도 넉넉합니다.' 셀 수 없는 물이나 시간 등이 충분하다고 안심시킬 때는", (None, 'plenty of hot water'), '풍부함을 뜻하는 이 구절을 써서 넉넉한 인상을 전해 줘요.']),
    (9, None, ["'십오 분만 주시면 이 다락방이 칠 호실을 거뜬히 이길 거예요!' 어느 한쪽이 다른 쪽보다 훨씬 낫다고 재치 있게 비교할 때는", (None, 'will beat'), '경기를 이긴다는 동사를 활용해 자신감을 생생히 드러내요.']),
    (10, None, ["'저 판지 상자들 챙기세요, 그레이엄. 자, 계단 아래로 내려갑시다!' 방향을 나타내는 말들을 맨 앞으로 끌어당겨 활기차게 외칠 때는", (None, 'Down the stairs we go'), '도치 구문으로 다 함께 움직이는 리듬감을 살려 말해요.']),
    (11, None, ["'모퉁이 돌 때 조심해요, 벽에 부딪히지 말고요!' 무거운 짐을 옮기며 어딘가에 쿵 부딪치지 말라고 당부할 때는", (None, 'do not bump'), '부정 명령문 뒤에 부딪친다는 동사를 써서 주의를 환기해요.']),
]
