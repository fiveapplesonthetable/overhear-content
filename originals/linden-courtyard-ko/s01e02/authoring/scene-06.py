# Authoring module for linden-courtyard-ko-s01e02-scene-06.
ID = 'linden-courtyard-ko-s01e02-scene-06'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = 'The Friday Caller  (금요일에 오겠다는 전화)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '프런트 데스크로 낯선 남자의 전화가 걸려 옵니다. 남색 여행 가방 주인인 듯한 그는 흰 종이 꾸러미는 절대 열지 말아 달라며 금요일 정오에 찾으러 오겠다고 말하고는 이름도 밝히지 않은 채 전화를 끊어 버리네요. 긴장감 도는 통화를 들어 보세요.'
OPENER = '이제 수수께끼의 전화 통화 속 표현들을 한 줄씩 살펴볼까요.'
TRANSITION = '장면 전체를 다시 한번 귀 기울여 들어 보세요.'
OUTRO = '예의 바르지만 어딘가 초조해 보이던 목소리는 왜 장난감 나무 기차 꾸러미를 그토록 신경 쓰는 걸까요. 금요일 정오가 점점 더 기다려집니다. 이따가 다음 장면에서 만나요.'
CLOSING = ('hannah', 'Bye for now!')
STORY = [
    ('hannah', 'Linden Courtyard Inn, good morning! Hannah speaking.', '린든 코트야드 여관입니다, 좋은 아침이에요! 해나입니다.'),
    ('graham', 'Who is it? Another booking for the weekend?', '누구예요? 주말 예약 문의인가요?'),
    ('hannah', 'Wait, hello, sir! You are calling about the dark blue suitcase?', '잠깐만요, 여보세요, 손님! 그 짙은 파란색 여행 가방 때문에 전화하신 거죠?'),
    ('graham', 'Ask him his name! Write it down!', '성함을 물어봐요! 얼른 적어 두세요!'),
    ('hannah', 'Yes, sir, we locked your bag safely in our closet. What is your name, please?', '네, 손님, 가방은 저희 벽장에 안전하게 잠가 두었습니다. 실례지만 성함이 어떻게 되시나요?'),
    ('graham', 'What is he saying? Why are you frowning?', '그 사람이 뭐라고 해요? 왜 미간을 찌푸리고 있어요?'),
    ('hannah', "Sir? He says, 'Please do not open the white paper package. I will come Friday at noon.'", '손님? 흰 종이 꾸러미는 열지 말아 달래요. 금요일 정오에 오겠다고 하시네요.'),
    ('graham', 'Give me the phone, let me ask him properly!', '전화기 이리 줘 보세요, 제가 제대로 물어볼게요!'),
    ('hannah', "Too late! He said 'Thank you' and hung up!", '이미 늦었어요! 감사합니다라고만 말하고 전화를 끊어 버렸어요!'),
    ('graham', 'Polite voice? Young or old?', '예의 바른 목소리였나요? 젊은 사람 같았어요, 나이 든 사람 같았어요?'),
    ('hannah', 'Quiet, polite, maybe thirty-five. He sounded nervous, not angry.', '조용하고 공손한 목소리로 서른다섯 살쯤 같았어요. 화난 게 아니라 긴장한 것처럼 들렸어요.'),
    ('graham', 'Nervous about a wooden toy train? This story gets stranger every hour.', '나무 장난감 기차 때문에 긴장했다고요? 이 사연은 한 시간마다 점점 더 이상해지네요.'),
]
WALK = [
    (0, None, ["'린든 코트야드 여관입니다, 좋은 아침이에요! 해나입니다.' 안내 데스크에서 수화기를 들며 전화를 받는 사람이 누구인지 밝힐 때 이름 뒤에", (None, 'Hannah speaking'), '이렇게 분사를 바로 붙여 인사해요.']),
    (1, None, ["'누구예요? 주말 예약 문의인가요?' 전화기 너머 상대방이 누구인지 물어볼 때는 영어에서 사람 대신 빈자리 주어를 써서", (None, 'Who is it'), '이렇게 묻는 것이 표준 표현이에요.']),
    (2, None, ["'잠깐만요, 여보세요, 손님! 그 짙은 파란색 여행 가방 때문에 전화하신 거죠?' 지금 걸려 온 전화의 용건을 확인하며 되물을 때는 현재진행형에 전치사를 더한", (None, 'You are calling about'), '여기서 이 구절로 핵심을 바로 짚어요.']),
    (3, None, ["'성함을 물어봐요! 얼른 적어 두세요!' 잊어버리지 않게 종이에 받아 적으라고 할 때는 대명사를 구동사 한가운데 넣은", (None, 'Write it down'), '바로 이 어순으로 재빨리 일러 줘요.']),
    (4, None, ["'네, 손님, 가방은 저희 벽장에 안전하게 잠가 두었습니다. 실례지만 성함이 어떻게 되시나요?' 가장 기본적인 이름 질문인", (None, 'What is your name'), '뒤에 공손한 표현만 덧붙여도 훌륭한 응대가 돼요.']),
    (5, None, ["'그 사람이 뭐라고 해요? 왜 미간을 찌푸리고 있어요?' 통화 내용이 의아해서 눈살을 찌푸리고 있는 표정을 현재진행형 분사인", (None, 'frowning'), '여기서 이 단어 하나로 생생하게 포착했어요.']),
    (6, None, ["'손님? 흰 종이 꾸러미는 열지 말아 달래요. 금요일 정오에 오겠다고 하시네요.' 낮 열두 시 정각을 뜻하는 명사 앞에는 정확한 시점을 찍어 주는 전치사를 붙여", (None, 'at noon'), '이렇게 말해요.']),
    (7, None, ["'전화기 이리 줘 보세요, 제가 제대로 물어볼게요!' 절차에 맞게 똑바로 확인해 보겠다고 할 때는 문장 끝에 부사", (None, 'properly'), '여기서 이 단어를 붙여 단호함을 더해요.']),
    (8, None, ["'이미 늦었어요! 감사합니다라고만 말하고 전화를 끊어 버렸어요!' 옛 벽걸이 수화기를 걸어 놓던 동작에서 유래해 전화를 끊었다고 할 때도 불규칙 과거형인", (None, 'hung up'), '여기서 이 구동사를 그대로 써요.']),
    (9, None, ["'예의 바른 목소리였나요? 젊은 사람 같았어요, 나이 든 사람 같았어요?' 목소리 주인공의 연령대를 짧게 대조해 물어볼 때는", (None, 'Young or old'), '이렇게 반대말 형용사 두 개만 나란히 이어도 충분해요.']),
    (10, None, ["'조용하고 공손한 목소리로 서른다섯 살쯤 같았어요. 화난 게 아니라 긴장한 것처럼 들렸어요.' 수화기 너머로 전해진 초조한 기색은 감각 동사 과거형과 형용사를 합친", (None, 'sounded nervous'), '여기서 이 표현으로 정확히 설명해요.']),
    (11, None, ["'나무 장난감 기차 때문에 긴장했다고요? 이 사연은 한 시간마다 점점 더 이상해지네요.' 시간이 갈수록 상태가 점점 더 기묘하게 변해 간다는 뜻은 비교급을 결합한", (None, 'gets stranger'), '바로 이 구절로 맛깔나게 살려 줘요.']),
]
