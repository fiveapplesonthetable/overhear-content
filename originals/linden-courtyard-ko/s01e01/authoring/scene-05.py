# Authoring module for linden-courtyard-ko-s01e01-scene-05.
ID = 'linden-courtyard-ko-s01e01-scene-05'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = 'Not My Clothes!  (제 옷이 아니에요!)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'evelyn': 'Evelyn', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '사 호실로 올라간 에블린 선생님이 다급하게 호출 벨을 울립니다. 묵직했던 남색 여행 가방을 열어 보니 원피스와 악보 대신 커다란 남성용 구두와 나무 장난감 기차가 들어 있었거든요. 먼저 놀란 세 사람의 대화를 영어로 들어 보세요.'
OPENER = '이제 가방 속 물건을 확인하는 대화를 한 문장씩 살펴볼까요.'
TRANSITION = '그럼 장면 전체를 자연스러운 속도로 다시 들어 보세요.'
OUTRO = '기차역에서 똑같이 생긴 남색 가방이 뒤바뀌었다는 사실이 밝혀졌어요. 세 사람은 옆면 손잡이에 묶인 작은 종이 카드를 밝은 아래층에서 확인해 보기로 합니다. 곧 다음 장면에서 만나요.'
CLOSING = ('hannah', 'Goodbye!')
STORY = [
    ('hannah', 'Miss Evelyn, is everything all right? You rang the bell!', '에블린 선생님, 다 괜찮으신가요? 벨을 울리셨길래요!'),
    ('evelyn', 'Look inside this suitcase, Hannah! This is not my bag!', '이 여행 가방 안을 좀 보세요, 해나! 이건 제 가방이 아니에요!'),
    ('hannah', 'Wait, it is dark blue, just like yours!', '잠깐만요, 선생님 가방처럼 짙은 파란색인데요!'),
    ('evelyn', 'The outside is identical, yes! But look inside!', '겉모습은 똑같아요, 맞아요! 하지만 안쪽을 보세요!'),
    ('graham', "Two pairs of big brown men's shoes and gray sweaters.", '커다란 갈색 남성용 구두 두 켤레와 회색 스웨터들이네요.'),
    ('hannah', 'And what is this wrapped in white paper? A little wooden train!', '그리고 흰 종이에 싸인 이건 뭐죠? 작은 나무 기차네요!'),
    ('evelyn', 'I certainly do not wear size eleven shoes!', '제가 십일 사이즈 신발을 신을 리는 절대 없잖아요!'),
    ('graham', 'No wonder it was so heavy. Wood and leather!', '어쩐지 그렇게 무겁더라니요. 나무와 가죽이었군요!'),
    ('evelyn', 'Someone at the train station took my blue suitcase by mistake!', '기차역에서 누군가 실수로 제 파란 여행 가방을 가져갔나 봐요!'),
    ('hannah', "Please sit down, ma'am. Do not worry, we will check the tag right now.", '자리에 좀 앉으세요, 선생님. 걱정하지 마세요, 지금 바로 이름표를 확인해 볼게요.'),
    ('graham', 'There is a small paper card tied to the side handle.', '옆면 손잡이에 작은 종이 카드가 하나 묶여 있어요.'),
    ('evelyn', 'Oh, let us bring it downstairs to the light!', '아, 밝은 아래층으로 그걸 가지고 내려가 봐요!'),
]
WALK = [
    (0, None, ["'에블린 선생님, 다 괜찮으신가요? 벨을 울리셨길래요!' 손님의 이름 앞에 정중한 호칭을 붙인", (None, 'Miss Evelyn'), '그리고 벨을 울렸다는 불규칙 과거형 동사', (None, 'rang'), '두 표현으로 다급히 안부를 여쭈어요.']),
    (1, None, ["'이 여행 가방 안을 좀 보세요, 해나! 이건 제 가방이 아니에요!' 눈앞의 물건이 내 것이 아니라고 단호하게 부정할 때는", (None, 'This is not'), '이렇게 비 동사 바로 뒤에 부정어를 붙여요.']),
    (2, None, ["'잠깐만요, 선생님 가방처럼 짙은 파란색인데요!' 앞에 나온 가방이라는 명사를 두 번 반복하지 않으려고", (None, 'yours'), '바로 이 소유대명사 하나로 선생님의 가방을 대신 받았어요.']),
    (3, None, ["'겉모습은 똑같아요, 맞아요! 하지만 안쪽을 보세요!' 가방의 바깥 외관을 가리키는 명사구", (None, 'The outside'), '그리고 그와 선명하게 대비되는 내부를 뜻하는', (None, 'inside'), '두 단어가 겉과 속을 또렷이 대조해 줘요.']),
    (4, None, ["'커다란 갈색 남성용 구두 두 켤레와 회색 스웨터들이네요.' 불규칙 복수 명사에 소유격을 덧붙인", (None, "men's shoes"), '여기 쓰인 이 표현으로 성인 남성용 구두임을 한눈에 알려 줘요.']),
    (5, None, ["'그리고 흰 종이에 싸인 이건 뭐죠? 작은 나무 기차네요!' 목재로 만든 재질을 나타낼 때는 형용사를 앞에 둔", (None, 'wooden train'), '이렇게 말해야 자연스러운 영어 어순이 돼요.']),
    (6, None, ["'제가 십일 사이즈 신발을 신을 리는 절대 없잖아요!' 옷을 입을 때나 신발을 신을 때나 영어에서는 구별 없이", (None, 'wear'), '여기 쓰인 이 동사 하나로 몸에 걸치는 모든 착용을 표현해요.']),
    (7, None, ["'어쩐지 그렇게 무겁더라니요. 나무와 가죽이었군요!' 궁금했던 이유를 뒤늦게 깨닫고 고개를 끄덕일 때는", (None, 'No wonder'), '여기 쓰인 이 관용구로 문장을 열면 무릎을 탁 치는 느낌이 살아나요.']),
    (8, None, ["'기차역에서 누군가 실수로 제 파란 여행 가방을 가져갔나 봐요!' 고의가 아니라 깜빡 착각해서 잘못 가져갔다고 할 때는 문장 끝에", (None, 'by mistake'), '여기 쓰인 이 짧은 전치사구를 덧붙여요.']),
    (9, None, ["'자리에 좀 앉으세요, 선생님. 걱정하지 마세요, 지금 바로 이름표를 확인해 볼게요.' 당황한 손님의 마음을 차분히 가라앉혀 드릴 때는", (None, 'Do not worry'), '여기 쓰인 이 다정한 안심 인사가 가장 먼저 나와요.']),
    (10, None, ["'옆면 손잡이에 작은 종이 카드가 하나 묶여 있어요.' 새로운 물건이 눈에 띄어 존재를 처음 알릴 때는", (None, 'There is'), '여기 쓰인 이 구문으로 문장을 자연스럽게 시작해요.']),
    (11, None, ["'아, 밝은 아래층으로 그걸 가지고 내려가 봐요!' 함께 움직이자고 제안하면서 방향 부사를 바로 붙인", (None, 'let us bring it downstairs'), '여기 쓰인 이 구절에서는 아래층 부사 앞에 전치사를 쓰지 않아요.']),
]
