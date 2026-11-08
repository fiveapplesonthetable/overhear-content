# Authoring module for linden-courtyard-ko-s01e02-scene-02.
ID = 'linden-courtyard-ko-s01e02-scene-02'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 2
SCENE = 2
TITLE = 'No Milk in the Fridge  (냉장고에 우유가 없어요!)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = '아침 식사 시작을 불과 이십 분 앞두고 유제품 배달 승합차의 타이어가 시내 외곽에서 펑크가 났습니다. 냉장고에는 우유 몇 방울과 달걀 두 개뿐이고 버터는 아예 없네요. 해나가 구원투수로 나서는 긴박한 장면을 들어 보세요.'
OPENER = '그럼 다급한 주방 소동 속 핵심 표현들을 한 줄씩 살펴볼까요.'
TRANSITION = '숨 가쁘게 이어지는 장면 전체를 다시 한번 들어 보세요.'
OUTRO = '현금 오십 달러와 장바구니를 챙긴 해나가 바람처럼 모퉁이 마트로 달려 나갔어요. 과연 십 분 안에 모든 재료를 무사히 사 올 수 있을까요. 이따가 다음 장면에서 확인해 보세요.'
CLOSING = ('hannah', 'See you later!')
STORY = [
    ('tessa', 'Oh no! Arthur, Hannah, we have a kitchen emergency!', '큰일 났어요! 아서, 해나, 주방에 비상사태가 생겼어요!'),
    ('arthur', 'Please do not say the word emergency before my morning coffee!', '모닝커피도 마시기 전에는 제발 비상사태라는 말 좀 꺼내지 말아 줘요!'),
    ('tessa', 'The dairy van has a flat tire outside town. Look in the fridge!', '유제품 배달 차가 시내 외곽에서 타이어가 펑크 났대요. 냉장고 안을 좀 보세요!'),
    ('hannah', 'One tiny splash of milk, two eggs, and no butter at all!', '우유는 아주 몇 방울뿐이고 달걀 두 개에 버터는 아예 하나도 없네요!'),
    ('arthur', 'Eight hungry guests will come down the stairs at seven thirty!', '일곱 시 삼십 분이면 배고픈 손님 여덟 분이 계단으로 내려오실 텐데요!'),
    ('tessa', 'My bread is already in the oven, at least.', '적어도 제 빵은 이미 오븐에 들어 있어요.'),
    ('hannah', 'Give me a bag and some cash! The corner market opens at seven.', '가방이랑 현금 좀 주세요! 모퉁이 마트가 일곱 시에 문을 열어요.'),
    ('arthur', 'Can you run there and back in ten minutes?', '십 분 안에 거기까지 뛰어갔다 돌아올 수 있겠어요?'),
    ('hannah', 'Watch me! Tell me exactly what to buy.', '제가 하는 거 보세요! 정확히 무엇을 사야 하는지 알려 주세요.'),
    ('tessa', 'Three bottles of milk, twenty eggs, butter, cheese, and red apples!', '우유 세 병, 달걀 스무 개, 버터, 치즈, 그리고 빨간 사과요!'),
    ('arthur', 'Here is fifty from the cash box. Bring back the receipt!', '여기 현금 상자에서 꺼낸 오십 달러예요. 영수증 꼭 챙겨 오세요!'),
    ('hannah', 'Hold the fort, I am already out the door!', '여기를 잘 부탁해요, 전 벌써 문밖으로 나갑니다!'),
]
WALK = [
    (0, None, ["'큰일 났어요! 아서, 해나, 주방에 비상사태가 생겼어요!' 두 명사를 나란히 붙여 어디에서 터진 급한 일인지 바로 알려 주는", (None, 'kitchen emergency'), '방금 들은 이 복합명사가 다급한 분위기를 단번에 전해 줘요.']),
    (1, None, ["'모닝커피도 마시기 전에는 제발 비상사태라는 말 좀 꺼내지 말아 줘요!' 농담 섞인 간곡한 부탁으로 그 말은 삼가 달라고 할 때", (None, 'Please do not say'), '이렇게 정중한 부정 명령문으로 문을 열어요.']),
    (2, None, ["'유제품 배달 차가 시내 외곽에서 타이어가 펑크 났대요. 냉장고 안을 좀 보세요!' 바퀴에서 바람이 빠져 납작해진 고장 상태를 영어에서는", (None, 'a flat tire'), '이렇게 평평하다는 형용사로 생생하게 묘사해요.']),
    (3, None, ["'우유는 아주 몇 방울뿐이고 달걀 두 개에 버터는 아예 하나도 없네요!' 전혀 없다는 뜻을 끝에서 강하게 못 박아 주는", (None, 'at all'), '방금 들은 이 표현이 앞선 부정 명사구', (None, 'no butter'), '바로 그 말과 호응해 빈 냉장고를 실감 나게 보여 줘요.']),
    (4, None, ["'일곱 시 삼십 분이면 배고픈 손님 여덟 분이 계단으로 내려오실 텐데요!' 아침 식사를 기다리는 투숙객들을 묘사하는", (None, 'hungry guests'), '방금 들은 이 구절처럼 형용사는 복수 명사 앞에서도 형태가 변하지 않아요.']),
    (5, None, ["'적어도 제 빵은 이미 오븐에 들어 있어요.' 어려운 상황 속에서도 다행스러운 최소한의 한 가지를 짚어 줄 때 문장 끝에", (None, 'at least'), '방금 들은 이 부사구를 덧붙여 한숨을 돌려요.']),
    (6, None, ["'가방이랑 현금 좀 주세요! 모퉁이 마트가 일곱 시에 문을 열어요.' 돈 전체를 뜻하는 현금은 셀 수 없는 명사여서 부정관사 대신", (None, 'some cash'), '이렇게 수량 표현과 함께 써요.']),
    (7, None, ["'십 분 안에 거기까지 뛰어갔다 돌아올 수 있겠어요?' 목적지까지 갔다가 다시 돌아오는 왕복 이동을 영어에서는", (None, 'there and back'), '방금 들은 이 세 단어로 아주 경쾌하게 압축해 말해요.']),
    (8, None, ["'제가 하는 거 보세요! 정확히 무엇을 사야 하는지 알려 주세요.' 자신 있게 맡겨 달라고 외치는", (None, 'Watch me'), '이어서 사야 할 품목을 간결하게 묶은', (None, 'what to buy'), '두 표현이 해나의 씩씩한 기세를 잘 보여 줘요.']),
    (9, None, ["'우유 세 병, 달걀 스무 개, 버터, 치즈, 그리고 빨간 사과요!' 셀 수 없는 우유를 병 단위로 정확히 세어 주문할 때는", (None, 'Three bottles of milk'), '이렇게 용기 명사를 복수로 만들어 연결해요.']),
    (10, None, ["'여기 현금 상자에서 꺼낸 오십 달러예요. 영수증 꼭 챙겨 오세요!' 심부름을 다녀오며 잊지 말고 도로 가지고 오라고 당부할 때는", (None, 'Bring back'), '방금 들은 이 구동사로 문장을 힘차게 시작해요.']),
    (11, None, ["'여기를 잘 부탁해요, 전 벌써 문밖으로 나갑니다!' 잠시 자리를 비우며 남은 사람들에게 현장을 든든히 지켜 달라고 할 때", (None, 'Hold the fort'), '방금 들은 이 유쾌한 관용구를 자주 쓴답니다.']),
]
