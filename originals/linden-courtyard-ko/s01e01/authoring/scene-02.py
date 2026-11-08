# Authoring module for linden-courtyard-ko-s01e01-scene-02.
ID = 'linden-courtyard-ko-s01e01-scene-02'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 1
SCENE = 2
TITLE = 'Warm Rolls and Two Rings  (따뜻한 모닝빵과 두 번 울리는 벨)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'hannah': 'Hannah', 'tessa': 'Tessa', 'graham': 'Graham'}
INTRO = '고소한 빵 냄새가 가득한 카페 모퉁이에서 아침 제빵사 테사가 갓 구운 롤빵을 들고 해나를 반갑게 맞이해요. 그때 아무도 없는 현관 쪽이 아니라 사 호실 전선에서 신기한 벨 소리가 두 번 울립니다. 먼저 장면 전체를 귀 기울여 들어 보세요.'
OPENER = '그럼 방금 나눈 정겨운 대화를 한 줄씩 함께 풀어 볼까요.'
TRANSITION = '이제 전체 대화를 자연스러운 흐름으로 다시 들어 보세요.'
OUTRO = '따끈한 모닝빵 하나로 금세 가까워진 세 사람 덕분에 해나도 여관 분위기에 한결 편안히 스며들었어요. 제멋대로 두 번 울리는 사 호실 벨 소리도 이제 친근한 인사처럼 느껴지네요. 이따가 다음 장면에서 만나요.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('tessa', 'Hello! You must be Hannah. I am Tessa from the kitchen.', '안녕하세요! 해나 씨시군요. 부엌에서 일하는 테사예요.'),
    ('hannah', 'Nice to meet you, Tessa. Something smells wonderful!', '만나서 반가워요, 테사. 무언가 정말 좋은 냄새가 나네요!'),
    ('tessa', 'Fresh morning rolls! Take one while it is still warm.', '갓 구운 모닝빵이에요! 아직 따뜻할 때 하나 드셔 보세요.'),
    ('hannah', 'Thank you! Do we use first names here?', '고마워요! 여기서는 서로 이름을 편하게 부르나요?'),
    ('tessa', 'With me, always! Leave the stiff polite talk for the guests.', '저한테는 언제나 그러세요! 격식 차린 공손한 말투는 손님들께 남겨 두시고요.'),
    ('graham', 'Tessa talks to everyone on our street like old friends.', '테사는 우리 거리의 모든 사람에게 오랜 친구처럼 말을 건네거든요.'),
    ('tessa', 'Because good coffee and warm bread make people friendly!', '맛있는 커피와 따뜻한 빵은 사람들을 다정하게 만들어 주니까요!'),
    ('hannah', 'What was that bell? Somebody rang twice!', '방금 그 종소리는 뭐였죠? 누군가 두 번 울렸어요!'),
    ('graham', 'Nobody is there. That is the buzzer from room four.', '거기엔 아무도 없어요. 사 호실에서 울리는 호출 벨 소리예요.'),
    ('tessa', 'Even when room four is empty, the old wire rings twice.', '사 호실이 비어 있을 때조차 오래된 전선이 두 번씩 울리곤 해요.'),
    ('hannah', 'So the house says hello on its own?', '그럼 이 집이 혼자서 인사를 건네는 셈이네요?'),
    ('tessa', 'Exactly! You already fit right in.', '바로 그거예요! 벌써 이곳에 딱 어울리시네요.'),
]
WALK = [
    (0, None, ["'안녕하세요! 해나 씨시군요. 부엌에서 일하는 테사예요.' 처음 만난 상대를 반갑게 짐작하며 인사할 때는", (None, 'You must be'), '바로 이 표현 뒤에 이름을 붙여 틀림없이 그분일 거라고 말해요.']),
    (1, None, ["'만나서 반가워요, 테사. 무언가 정말 좋은 냄새가 나네요!' 향기를 나타내는 감각 동사", (None, 'smells'), '그 바로 뒤에 형용사', (None, 'wonderful'), '바로 이 단어를 이어 붙여 감탄을 전해요.']),
    (2, None, ["'갓 구운 모닝빵이에요! 아직 따뜻할 때 하나 드셔 보세요.' 온기가 그대로 남아 있는 상태를 강조할 때는", (None, 'still warm'), '이렇게 부사와 형용사를 나란히 붙여 써요.']),
    (3, None, ["'고마워요! 여기서는 서로 이름을 편하게 부르나요?' 직장 동료 사이의 호칭 습관을 물어볼 때는 조동사로 문을 여는", (None, 'Do we use first names'), '바로 이 질문으로 성 대신 이름을 쓰는지 확인해요.']),
    (4, None, ["'저한테는 언제나 그러세요! 격식 차린 공손한 말투는 손님들께 남겨 두시고요.' 정중하고 예의 바른 손님용 화법을 가리켜", (None, 'polite talk'), '이렇게 두 단어로 간결하게 묶어 말해요.']),
    (5, None, ["'테사는 우리 거리의 모든 사람에게 오랜 친구처럼 말을 건네거든요.' 만나는 사람마다 다정하게 대화를 나눈다는 평소 습관을", (None, 'talks to everyone'), '이렇게 삼 인칭 단수 현재형으로 나타내요.']),
    (6, None, ["'맛있는 커피와 따뜻한 빵은 사람들을 다정하게 만들어 주니까요!' 항상 복수로 쓰이는 명사", (None, 'people'), '여기에 상태를 바꾸어 주는 동사', (None, 'make'), '바로 이 표현이 어우러져 마음을 녹여 준다는 뜻을 전해요.']),
    (7, None, ["'방금 그 종소리는 뭐였죠? 누군가 두 번 울렸어요!' 영어에서 두 번이라는 횟수는 숫자에 번을 붙이지 않고", (None, 'twice'), '바로 이 전용 부사 한 단어로 깔끔하게 말해요.']),
    (8, None, ["'거기엔 아무도 없어요. 사 호실에서 울리는 호출 벨 소리예요.' 아무도 없다는 뜻이 이미 담긴 주어를 써서", (None, 'Nobody is there'), '이렇게 긍정 형태의 동사와 함께 단수로 표현해요.']),
    (9, None, ["'사 호실이 비어 있을 때조차 오래된 전선이 두 번씩 울리곤 해요.' 예상 밖의 상황까지 포함해 강조하고 싶을 때는", (None, 'Even when'), '바로 이 두 단어로 문장 첫머리를 힘 있게 열어 줘요.']),
    (10, None, ["'그럼 이 집이 혼자서 인사를 건네는 셈이네요?' 안부를 건네다라는 뜻의", (None, 'says hello'), '그리고 누구의 손길 없이 저절로라는 뜻의', (None, 'on its own'), '두 표현이 만나 재치 있는 비유가 되었어요.']),
    (11, None, ["'바로 그거예요! 벌써 이곳에 딱 어울리시네요.' 새로운 환경이나 사람들과 금세 자연스럽게 어우러질 때", (None, 'fit right in'), '바로 이 따뜻한 칭찬 표현을 자주 쓴답니다.']),
]
