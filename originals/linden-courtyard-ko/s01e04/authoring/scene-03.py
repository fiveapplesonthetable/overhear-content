# Authoring module for linden-courtyard-ko-s01e04-scene-03.
ID = 'linden-courtyard-ko-s01e04-scene-03'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 4
SCENE = 3
TITLE = 'Hot Cinnamon Rolls  (따끈한 시나몬 롤)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'tessa': 'Tessa', 'evelyn': 'Evelyn', 'arthur': 'Arthur'}
INTRO = '일찍 잠에서 깬 사 호실 손님 에블린 선생님이 달콤한 계피 빵 냄새를 맡고 아래층 카페 모퉁이로 내려와요. 욕실 수도꼭지가 왜 차가운지 묻는 에블린 선생님 앞에서 아서와 테사는 갓 구운 시나몬 롤과 차로 시간을 벌어 봅니다. 장면을 들어 보세요.'
OPENER = '향긋한 빵 냄새 속에서 오간 재치 있는 대화를 한 줄씩 살펴볼까요.'
TRANSITION = '그럼 아슬아슬하고 유쾌한 이 장면을 자연스러운 속도로 다시 들어 보세요.'
OUTRO = '따뜻한 시나몬 롤에 버터를 곁들이는 사이 마침내 안뜰 대문으로 해나가 뛰어 들어왔어요. 안도의 미소를 지으며 지하실로 향하는 아서의 뒷모습이 눈에 선하네요. 곧 다음 장면에서 만나요.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('evelyn', 'Good morning! Something smells like warm cinnamon all the way upstairs!', '좋은 아침이에요! 위층까지 내내 따뜻한 계피 향기 같은 좋은 냄새가 나네요!'),
    ('tessa', 'Good morning, Miss Evelyn! My cinnamon rolls just came out of the oven.', '좋은 아침입니다, 에블린 선생님! 제 시나몬 롤이 방금 오븐에서 나왔어요.'),
    ('arthur', "Sit right down by the sunny window, ma'am! No rush to go upstairs yet!", '햇살 잘 드는 창가에 바로 앉으세요, 선생님! 아직 위층으로 서둘러 올라가실 필요 없어요!'),
    ('evelyn', 'Actually, I only came down to ask why the bathroom tap felt so chilly.', '실은 욕실 수도꼭지가 왜 그렇게 싸늘한지 물어보려고 내려왔을 뿐이에요.'),
    ('arthur', 'Chilly? Ah, yes! Our neighborhood water pipes take a gentle morning stretch!', '싸늘하다고요? 아, 네! 우리 동네 수도관이 아침마다 부드럽게 기지개를 켜거든요!'),
    ('tessa', 'Have a hot cup of tea and a cinnamon roll for ten minutes first!', '먼저 십 분 동안 뜨거운 차 한 잔과 시나몬 롤을 드셔 보세요!'),
    ('evelyn', 'Well, nobody wise says no to warm cinnamon bread at seven in the morning.', '하기야 아침 일곱 시에 따뜻한 계피 빵을 마다할 현명한 사람은 아무도 없죠.'),
    ('arthur', 'Wonderful choice! Would you like honey or apple jam beside it?', '탁월한 선택이십니다! 빵 곁에 꿀을 드릴까요, 아니면 사과잼을 드릴까요?'),
    ('evelyn', 'Just a little butter, thank you. Why are you looking at your watch, sir?', '그냥 버터만 조금 주세요, 고마워요. 그런데 왜 자꾸 손목시계를 보시나요, 사장님?'),
    ('arthur', 'Me? Oh, I simply love being on time! Seven fourteen is a beautiful minute!', '저요? 오, 저는 그저 시간 지키는 걸 워낙 좋아해서요! 일곱 시 십사 분은 참 아름다운 시각이죠!'),
    ('tessa', 'Look through the courtyard window, Arthur. Someone just ran through the gate!', '안뜰 창문 너머를 보세요, 아서. 방금 누군가 대문을 통과해 뛰어 들어왔어요!'),
    ('arthur', "Saved! Excuse me one moment, ma'am, enjoy your hot tea!", '살았다! 잠시만 실례하겠습니다, 선생님, 따뜻한 차 맛있게 드세요!'),
]
WALK = [
    (0, None, ["'좋은 아침이에요! 위층까지 내내 따뜻한 계피 향기 같은 좋은 냄새가 나네요!' 어떤 구체적인 재료의 향기와 비슷한 냄새가 풍긴다고 묘사하는 구절이", (None, 'smells like warm cinnamon'), '감각 동사 뒤에 전치사를 붙여 명사구와 자연스럽게 연결했어요.']),
    (1, None, ["'좋은 아침입니다, 에블린 선생님! 제 시나몬 롤이 방금 오븐에서 나왔어요.' 막 구워져 오븐 밖으로 따끈따끈하게 나온 직후임을 알리는 표현이", (None, 'just came out'), '부사와 과거형 동사를 함께 써서 김이 모락모락 나는 순간을 살려요.']),
    (2, None, ["'햇살 잘 드는 창가에 바로 앉으세요, 선생님! 아직 위층으로 서둘러 올라가실 필요 없어요!' 손님에게 망설이지 말고 편히 자리에 앉으라고 권하는 다정한 표현이", (None, 'Sit right down'), '동사와 부사 사이에 강조어를 끼워 넣어 반갑게 자리를 권해요.']),
    (3, None, ["'실은 욕실 수도꼭지가 왜 그렇게 싸늘한지 물어보려고 내려왔을 뿐이에요.' 상대의 짐작과 다른 진짜 속사정이나 원래 용건을 정중히 꺼내는 부사가", (None, 'Actually'), '문장 첫머리에서 화제를 부드럽게 바로잡아 주는 역할을 맡아요.']),
    (4, None, ["'싸늘하다고요? 아, 네! 우리 동네 수도관이 아침마다 부드럽게 기지개를 켜거든요!' 얼음장까지는 아니지만 기분 나쁘게 서늘하고 냉기가 도는 느낌을 가리키는 형용사가", (None, 'Chilly'), '아침 공기나 차가운 수돗물을 일상적으로 표현하기에 딱 알맞은 단어예요.']),
    (5, None, ["'먼저 십 분 동안 뜨거운 차 한 잔과 시나몬 롤을 드셔 보세요!' 음식이나 음료를 권할 때 먹거나 마신다는 동사 대신 가장 자연스럽게 쓰는 구절이", (None, 'Have a hot cup'), '부담 없이 기분 좋게 차 한 잔을 권유하는 대표적인 식탁 인사예요.']),
    (6, None, ["'하기야 아침 일곱 시에 따뜻한 계피 빵을 마다할 현명한 사람은 아무도 없죠.' 부정 대명사는 형용사가 뒤에서 꾸며 준다는 영어 어순 규칙을 잘 보여 주는 구절이", (None, 'nobody wise'), '현명한 사람이라면 누구도 거절하지 않을 거라는 재치 있는 표현이에요.']),
    (7, None, ["'탁월한 선택이십니다! 빵 곁에 꿀을 드릴까요, 아니면 사과잼을 드릴까요?' 손님의 취향을 존중하며 정중하게 곁들일 음식을 권하는 질문 틀이", (None, 'Would you like'), '직접적인 동사보다 훨씬 품위 있고 부드러운 접객 어투를 만들어 줘요.']),
    (8, None, ["'그냥 버터만 조금 주세요, 고마워요. 그런데 왜 자꾸 손목시계를 보시나요, 사장님?' 셀 수 없는 명사인 버터를 아주 소량만 달라고 담백하게 부탁하는 구절이", (None, 'Just a little butter'), '관사가 포함된 수량 표현으로 약간의 양을 기분 좋게 나타내요.']),
    (9, None, ["'저요? 오, 저는 그저 시간 지키는 걸 워낙 좋아해서요! 일곱 시 십사 분은 참 아름다운 시각이죠!' 약속이나 정해진 시각에 늦지 않고 제시간을 지키는 상태를 좋아한다는 표현이", (None, 'love being on time'), '동명사 구문을 목적어로 삼아 평소 성향인 것처럼 능청스럽게 둘러대요.']),
    (10, None, ["'안뜰 창문 너머를 보세요, 아서. 방금 누군가 대문을 통과해 뛰어 들어왔어요!' 유리창을 투과해 그 건너편 풍경을 내다보라고 시선을 이끄는 전치사구가", (None, 'through the courtyard window'), '창문이라는 매개체를 관통해 보는 시선의 움직임을 선명히 그려 줘요.']),
    (11, None, ["'살았다! 잠시만 실례하겠습니다, 선생님, 따뜻한 차 맛있게 드세요!' 자리를 비우며 손님에게 즐거운 다과 시간을 보내시라고 남기는 다정한 인사가", (None, 'enjoy your hot tea'), '맛있게 드시라는 우리말 인사에 꼭 들어맞는 자연스러운 영어 표현이에요.']),
]
