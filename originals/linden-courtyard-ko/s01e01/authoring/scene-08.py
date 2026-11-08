# Authoring module for linden-courtyard-ko-s01e01-scene-08.
ID = 'linden-courtyard-ko-s01e01-scene-08'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = 'Left on the Step  (돌계단 위에 남겨진 가방)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '밤 아홉 시, 조용하던 안뜰 대문에서 갑자기 초인종이 울립니다. 해나와 그레이엄이 함께 문을 열어 보니 사람은 온데간데없고 돌계단 위에 에블린 선생님의 진짜 가방과 흰 봉투 하나만 놓여 있어요. 흥미진진한 마지막 장면을 들어 보세요.'
OPENER = '이제 밤중에 찾아온 수수께끼 같은 대화를 한 줄씩 살펴볼까요.'
TRANSITION = '첫 번째 에피소드의 마지막 장면을 다시 한번 귀 기울여 들어 보세요.'
OUTRO = '에블린 선생님의 가방은 무사히 돌아왔지만 정작 자기 가방은 금요일까지 맡아 달라는 이름 없는 편지만 남았네요. 해나의 둘째 날은 과연 어떤 하루가 될까요. 다음 에피소드에서 만나요.'
CLOSING = ('graham', 'Have a good night!')
STORY = [
    ('hannah', 'Did you hear that, Graham? Someone just rang the gate bell!', '방금 그 소리 들으셨어요, 그레이엄? 누군가 대문 초인종을 울렸어요!'),
    ('graham', "At nine o'clock? Wait, let us open the gate together.", '아홉 시에 도착한다고요? 잠깐만요, 대문을 같이 열자고요.'),
    ('hannah', 'Hello? Good evening! Nobody is standing at the gate!', '계세요? 안녕하세요! 대문에는 아무도 서 있지 않아요!'),
    ('graham', 'Wait. Look down on the stone step.', '잠깐만요. 저기 돌계단 아래쪽을 내려다보세요.'),
    ('hannah', "Another dark blue suitcase! Is this Miss Evelyn's bag?", '또 다른 짙은 파란색 여행 가방이에요! 이게 에블린 선생님 가방인가요?'),
    ('graham', 'Check the zipper... yes, her initials are right here!', '지퍼 쪽을 확인해 보세요... 네, 선생님 이름 머리글자가 바로 여기 있네요!'),
    ('hannah', 'Why did the person run away without taking his own suitcase back?', '그 사람은 왜 자기 여행 가방은 도로 가져가지도 않고 달려가 버렸을까요?'),
    ('graham', 'Look, there is a folded white envelope taped to the handle.', '이것 보세요, 손잡이에 접힌 흰 봉투가 테이프로 붙어 있어요.'),
    ('hannah', "Let me read it: 'Sorry for the mistake. Please keep my blue bag until Friday.'", '제가 읽어 볼게요. 실수해서 죄송합니다, 금요일까지 제 파란 가방을 맡아 주세요.'),
    ('graham', 'Until Friday? No name, no signature!', '금요일까지라고요? 이름도 없고 서명도 없네요!'),
    ('hannah', 'Why leave your own shoes and wooden train with strangers until Friday?', '왜 자기 신발과 나무 기차를 금요일까지 낯선 사람들에게 맡겨 두는 걸까요?'),
    ('graham', 'Welcome to the Linden Courtyard Inn, Hannah. Your second day will not be boring.', '린든 코트야드 여관에 오신 걸 환영해요, 해나. 둘째 날도 지루할 틈이 없겠네요.'),
]
WALK = [
    (0, None, ["'방금 그 소리 들으셨어요, 그레이엄? 누군가 대문 초인종을 울렸어요!' 방금 들린 소리를 상대방도 들었는지 재빨리 확인할 때는", (None, 'Did you hear that'), '여기 쓰인 이 과거형 질문이 반사적으로 튀어나와요.']),
    (1, None, ["'아홉 시에 도착한다고요? 잠깐만요, 대문을 같이 열자고요.' 분 단위 없이 딱 떨어지는 정각 시각을 강조할 때는 숫자 뒤에", (None, "nine o'clock"), '이렇게 정각 표현을 붙여 말해요.']),
    (2, None, ["'계세요? 안녕하세요! 대문에는 아무도 서 있지 않아요!' 밤 시간이라도 누군가를 처음 맞이할 때는 잠자리 인사가 아니라", (None, 'Good evening'), '바로 이 저녁 인사로 말을 건네야 자연스러워요.']),
    (3, None, ["'잠깐만요. 저기 돌계단 아래쪽을 내려다보세요.' 시선을 발밑이나 아래쪽으로 낮추어 살피라고 할 때는", (None, 'Look down'), '이렇게 동사와 방향 부사를 나란히 이어 줘요.']),
    (4, None, ["'또 다른 짙은 파란색 여행 가방이에요! 이게 에블린 선생님 가방인가요?' 이미 있던 것에 더해 하나가 더 나타났을 때는 단수 명사 앞에", (None, 'Another'), '여기 쓰인 이 한정사를 붙여 놀라움을 전해요.']),
    (5, None, ["'지퍼 쪽을 확인해 보세요... 네, 선생님 이름 머리글자가 바로 여기 있네요!' 성과 이름의 첫 글자들을 함께 일컬을 때는 복수형을 써서", (None, 'her initials'), '이렇게 소유격과 함께 말해요.']),
    (6, None, ["'그 사람은 왜 자기 여행 가방은 도로 가져가지도 않고 달려가 버렸을까요?' 어떤 행동을 하지 않은 채로 떠났다고 할 때는 전치사 뒤에 동명사를 둔", (None, 'without taking'), '여기 쓰인 이 구조가 문장을 깔끔하게 묶어 줘요.']),
    (7, None, ["'이것 보세요, 손잡이에 접힌 흰 봉투가 테이프로 붙어 있어요.' 명사인 테이프를 동사로도 그대로 활용해서 분사 형태인", (None, 'taped'), '바로 이 한 단어로 테이프로 붙여 두었다는 상태를 묘사해요.']),
    (8, None, ["'제가 읽어 볼게요. 실수해서 죄송합니다, 금요일까지 제 파란 가방을 맡아 주세요.' 쪽지 첫머리에 정중하고 간결하게 사과를 적을 때는", (None, 'Sorry for the mistake'), '이렇게 전치사로 사과의 이유를 바로 연결해요.']),
    (9, None, ["'금요일까지라고요? 이름도 없고 서명도 없네요!' 상태가 계속 이어지는 기한을 나타내는 전치사", (None, 'Until'), '그 뒤에 마감 요일을 뜻하는 고유명사', (None, 'Friday'), '두 단어가 나란히 붙어 금요일까지 계속 보관해 달라는 뜻이 돼요.']),
    (10, None, ["'왜 자기 신발과 나무 기차를 금요일까지 낯선 사람들에게 맡겨 두는 걸까요?' 일면식도 없는 남들을 가리킬 때는 복수 명사인", (None, 'strangers'), '바로 이 단어를 써서 의아한 마음을 드러내요.']),
    (11, None, ["'린든 코트야드 여관에 오신 걸 환영해요, 해나. 둘째 날도 지루할 틈이 없겠네요.' 앞으로 다가올 일이 결코 심심하지 않을 거라고 재치 있게 예고할 때", (None, 'will not be boring'), '여기 쓰인 이 미래 부정 표현으로 미소를 남기며 마무리해요.']),
]
