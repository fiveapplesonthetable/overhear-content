# Authoring module for linden-courtyard-ko-s01e05-scene-06.
ID = 'linden-courtyard-ko-s01e05-scene-06'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 5
SCENE = 6
TITLE = 'Ten Minutes to Twelve  (열두 시 십 분 전)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '시계가 열한 시 오십 분을 가리키는 프런트 데스크에서 아서가 넥타이를 반듯하게 매만지며 정오를 기다려요. 그때 우편배달부가 붉은 부동산 도장이 찍힌 두툼한 등기 우편을 남기고 갑니다. 정오 직전의 설레는 소란을 들어 보세요.'
OPENER = '정오를 코앞에 둔 프런트의 대화를 차례대로 살펴볼까요.'
TRANSITION = '종소리가 울리기 직전의 긴장감을 느끼며 다시 들어 보세요.'
OUTRO = '등기 우편은 잠시 장부 옆에 미루어 두고 모두가 숨을 죽인 채 창가에서 한 걸음 물러섰어요. 이제 거리 저편 교회 시계탑에서 정오의 종소리가 울려 퍼집니다. 곧이어 펼쳐질 다음 장면에서 만나요.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('arthur', 'How does my tie look today, Hannah? Zero orange juice in sight!', '오늘 내 넥타이 어때 보여요, 해나? 오렌지 주스 자국은 하나도 없죠!'),
    ('hannah', 'Sharp and spotless, Arthur! Even your glasses are on your nose instead of your forehead.', '단정하고 티 하나 없이 깔끔해요, 아서! 심지어 안경도 이마 대신 코 위에 제대로 걸려 있네요.'),
    ('arthur', 'Progress! Today our courtyard hosts a family reunion. Quiet dignity from everyone!', '발전했군! 오늘 우리 안뜰에서 가족 상봉이 열리니 모두 조용한 품위를 지켜 주세요!'),
    ('tessa', 'Says the man peeking through the lace curtain every thirty seconds!', '삼십 초마다 레이스 커튼 사이로 몰래 내다보는 분이 하실 말씀은 아닌걸요!'),
    ('arthur', 'I am checking the weather, Tessa! Who left this thick envelope by the bell?', '날씨를 확인하는 중이에요, 테사! 누가 벨 옆에 이 두툼한 봉투를 두고 갔죠?'),
    ('hannah', 'The mailman just asked me to sign for it. It has a red property office stamp.', '방금 우편배달부가 서명해 달라고 하셨어요. 빨간 부동산 사무소 도장이 찍혀 있네요.'),
    ('arthur', "From the building landlord's lawyer? Strange, our rent is paid until next summer.", '건물주 변호사한테서 온 건가? 이상하군, 우리 집세는 내년 여름까지 다 내놓았는데.'),
    ('tessa', 'Open it after twelve, boss! Look at the clock: five minutes to noon!', '열두 시 지나서 열어 봐요, 사장님! 시계 좀 보세요, 정오 오 분 전이에요!'),
    ('arthur', 'Right you are. Paperwork can wait. Put it beside the book for now.', '네 말이 맞다. 서류 일은 기다려도 되지. 우선은 장부 옆에 놓아두렴.'),
    ('hannah', "I placed the blue suitcase right beside Caleb's table under the tree.", '파란 여행 가방은 나무 아래 케일럽의 탁자 바로 옆에 갖다 놓았어요.'),
    ('tessa', 'And the teapot is hot! Everybody step back from the window!', '찻주전자도 뜨겁게 데워졌어요! 모두 창가에서 뒤로 한 걸음 물러서세요!'),
    ('arthur', 'Listen... the church clock down the street is starting to chime twelve!', '들어 보세요... 거리 아래쪽 교회 시계가 열두 시 종을 치기 시작했어요!'),
]
WALK = [
    (0, None, ["'오늘 내 넥타이 어때 보여요, 해나? 오렌지 주스 자국은 하나도 없죠!' 눈에 보이는 시야 범위 안이라는 뜻으로 자주 쓰이는 전치사구", (None, 'in sight'), '표현을 붙여 얼룩이 전혀 없다고 자랑해요.']),
    (1, None, ["'단정하고 티 하나 없이 깔끔해요, 아서! 심지어 안경도 이마 대신 코 위에 제대로 걸려 있네요.' 먼지나 얼룩이 한 점도 없이 깨끗하다는 칭찬은 형용사", (None, 'spotless'), '한 단어로 산뜻하게 표현할 수 있어요.']),
    (2, None, ["'발전했군! 오늘 우리 안뜰에서 가족 상봉이 열리니 모두 조용한 품위를 지켜 주세요!' 장소가 뜻깊은 모임이나 행사를 맞이해 연다는 표현은 동사", (None, 'hosts'), '단수 현재형으로 격식 있게 말해요.']),
    (3, None, ["'삼십 초마다 레이스 커튼 사이로 몰래 내다보는 분이 하실 말씀은 아닌걸요!' 말과 행동이 다른 상대를 유쾌하게 놀릴 때 도치 어순으로 시작하는", (None, 'Says the man'), '관용적 대꾸가 재치를 더해 줘요.']),
    (4, None, ["'날씨를 확인하는 중이에요, 테사! 누가 벨 옆에 이 두툼한 봉투를 두고 갔죠?' 의문사가 곧바로 주어 노릇을 할 때는 조동사 없이 과거형 동사를 붙인", (None, 'Who left'), '어순으로 간단히 물건을 두고 간 사람을 찾아요.']),
    (5, None, ["'방금 우편배달부가 서명해 달라고 하셨어요. 빨간 부동산 사무소 도장이 찍혀 있네요.' 등기 우편이나 소포를 수령하며 서명하다는 실생활 표현은", (None, 'sign for it'), '전치사를 함께 챙겨 한 덩어리로 써요.']),
    (6, None, ["'건물주 변호사한테서 온 건가? 이상하군, 우리 집세는 내년 여름까지 다 내놓았는데.' 어떤 상태가 특정 시점까지 쭉 유효함을 나타낼 때는 전치사를 쓴", (None, 'until next summer'), '구절로 계약 기간의 여유를 짚어 줘요.']),
    (7, None, ["'열두 시 지나서 열어 봐요, 사장님! 시계 좀 보세요, 정오 오 분 전이에요!' 정각까지 몇 분 남았는지 시각을 알려 줄 때는 방향 전치사를 넣은", (None, 'five minutes to noon'), '방식으로 다급한 순간을 외쳐요.']),
    (8, None, ["'네 말이 맞다. 서류 일은 기다려도 되지. 우선은 장부 옆에 놓아두렴.' 상대 의견에 흔쾌히 동의하는 도치 표현", (None, 'Right you are'), '그리고 당분간은 그대로 두자는 뜻의', (None, 'for now'), '두 구절이 어우러져 여유 있는 결정을 보여 줘요.']),
    (9, None, ["'파란 여행 가방은 나무 아래 케일럽의 탁자 바로 옆에 갖다 놓았어요.' 물건을 조심스럽고 반듯하게 제자리에 두었다고 말할 때는 동사", (None, 'I placed'), '표현을 골라 정성스러운 손길을 드러내요.']),
    (10, None, ["'찻주전자도 뜨겁게 데워졌어요! 모두 창가에서 뒤로 한 걸음 물러서세요!' 호기심에 다가선 사람들에게 뒤쪽으로 물러나라고 지시할 때는 구동사", (None, 'step back'), '두 단어로 경쾌하게 주의를 줘요.']),
    (11, None, ["'들어 보세요... 거리 아래쪽 교회 시계가 열두 시 종을 치기 시작했어요!' 길을 따라 조금 내려간 곳에 자리한 위치를 가리킬 때는", (None, 'down the street'), '명사 뒤 수식어로 공간감을 자연스럽게 살려 줘요.']),
]
