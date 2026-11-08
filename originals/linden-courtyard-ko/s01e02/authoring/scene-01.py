# Authoring module for linden-courtyard-ko-s01e02-scene-01.
ID = 'linden-courtyard-ko-s01e02-scene-01'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 2
SCENE = 1
TITLE = 'The Red Ribbon  (빨간 리본의 주인)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = '화요일 아침, 프런트로 내려온 에블린 선생님이 간밤에 대문 앞으로 돌아온 자신의 진짜 여행 가방과 반갑게 재회합니다. 아끼던 찻잔도 멀쩡하지만 이름표의 손글씨가 어딘가 묘하게 낯익다는 이야기가 나오네요. 먼저 대화를 편안하게 들어 보세요.'
OPENER = '이제 반가운 아침 대화를 한 문장씩 차례대로 살펴볼까요.'
TRANSITION = '장면 전체를 다시 한번 자연스러운 속도로 들어 보세요.'
OUTRO = '주인 모를 가방은 금요일까지 단단히 잠가 두고 에블린 선생님은 이제 든든한 아침 식사를 하러 가시네요. 하지만 바로 그 시각 주방에서는 뜻밖의 비상이 걸렸답니다. 곧 다음 장면에서 만나요.'
CLOSING = ('evelyn', 'See you soon!')
STORY = [
    ('hannah', 'Good morning, Miss Evelyn! Look what arrived at our gate last night.', '좋은 아침이에요, 에블린 선생님! 어젯밤 저희 대문 앞에 무엇이 도착했는지 보세요.'),
    ('evelyn', 'My suitcase! Let me open the top pocket... yes, my red ribbon!', '제 여행 가방이군요! 윗주머니를 한번 열어 볼게요... 맞아요, 제 빨간 리본이에요!'),
    ('graham', 'And your teacup inside? Is it still in one piece?', '안에 있던 찻잔은요? 깨진 곳 없이 아직 온전한가요?'),
    ('evelyn', 'Not a single crack! Who brought it back?', '금 하나도 안 갔어요! 누가 이걸 도로 가져다주었나요?'),
    ('hannah', 'We do not know. Someone left it on the step and rang the bell.', '저희도 모르겠어요. 누군가 계단 위에 가방을 두고 벨을 울렸거든요.'),
    ('evelyn', 'And he did not ask for his own suitcase with the wooden train?', '그런데 나무 기차가 든 자기 가방은 달라고 하지 않던가요?'),
    ('graham', 'He left a short note asking us to keep it until Friday.', '금요일까지 맡아 달라고 부탁하는 짧은 쪽지를 남겼어요.'),
    ('evelyn', 'How curious! The handwriting on that tag felt oddly familiar to me.', '참 신기하네요! 그 이름표에 적힌 손글씨가 어딘가 묘하게 낯익게 느껴졌거든요.'),
    ('hannah', 'Really? Do you know someone in Portland?', '정말요? 포틀랜드에 아는 분이 계시나요?'),
    ('evelyn', 'Twenty-five years ago I taught piano near here, though memories fade.', '스물다섯 해 전에 이 근처에서 피아노를 가르쳤지만 기억이 희미해지네요.'),
    ('graham', 'For now, his bag stays safe under lock and key.', '우선 당분간은 그분 가방도 자물쇠를 채워 안전하게 보관해 둘게요.'),
    ('evelyn', 'Wonderful! Now I am ready for a big breakfast.', '든든하네요! 이제 푸짐한 아침 식사를 먹을 준비가 다 되었어요.'),
]
WALK = [
    (0, None, ["'좋은 아침이에요, 에블린 선생님! 어젯밤 저희 대문 앞에 무엇이 도착했는지 보세요.' 지나간 어젯밤을 말할 때는 앞에 전치사를 붙이지 않고", (None, 'last night'), '방금 들은 이 두 단어만으로 시점을 깔끔하게 나타내요.']),
    (1, None, ["'제 여행 가방이군요! 윗주머니를 한번 열어 볼게요... 맞아요, 제 빨간 리본이에요!' 내가 직접 무언가를 열어 보겠다고 자연스럽게 운을 뗄 때는", (None, 'Let me open'), '이렇게 동사원형을 바로 이어 말해요.']),
    (2, None, ["'안에 있던 찻잔은요? 깨진 곳 없이 아직 온전한가요?' 그릇이나 유리가 부서지지 않고 멀쩡한 한 덩어리 상태임을 물을 때", (None, 'in one piece'), '방금 들은 이 생생한 관용구를 자주 쓴답니다.']),
    (3, None, ["'금 하나도 안 갔어요! 누가 이걸 도로 가져다주었나요?' 누가 한 일인지 주어를 물어볼 때는 별도의 조동사 없이 의문사 뒤에 과거동사를 바로 붙인", (None, 'Who brought it back'), '방금 들은 이 어순 그대로 질문해요.']),
    (4, None, ["'저희도 모르겠어요. 누군가 계단 위에 가방을 두고 벨을 울렸거든요.' 확실히 알지 못한다고 솔직하고 담백하게 답할 때는", (None, 'We do not know'), '방금 들은 이 기본 부정문이 가장 또렷해요.']),
    (5, None, ["'그런데 나무 기차가 든 자기 가방은 달라고 하지 않던가요?' 질문을 묻는 것이 아니라 물건을 내달라고 요청할 때는 전치사를 더한", (None, 'ask for'), '방금 들은 이 두 단어를 짝지어 써요.']),
    (6, None, ["'금요일까지 맡아 달라고 부탁하는 짧은 쪽지를 남겼어요.' 쪽지가 어떤 내용을 정중히 청하고 있는지 뒤에서 꾸며 줄 때", (None, 'asking us to keep'), '이런 분사 구문으로 매끄럽게 이어 줘요.']),
    (7, None, ["'참 신기하네요! 그 이름표에 적힌 손글씨가 어딘가 묘하게 낯익게 느껴졌거든요.' 손으로 직접 쓴 고유의 글씨체나 필적은 한 단어로 묶어", (None, 'handwriting'), '바로 이 명사로 표현해요.']),
    (8, None, ["'정말요? 포틀랜드에 아는 분이 계시나요?' 특정 도시에 알고 지내는 지인이 있는지 가볍게 여쭐 때는", (None, 'know someone'), '방금 들은 이 표현 뒤에 장소만 덧붙이면 돼요.']),
    (9, None, ["'스물다섯 해 전에 이 근처에서 피아노를 가르쳤지만 기억이 희미해지네요.' 현재에서 거슬러 올라간 세월을 뜻하는", (None, 'Twenty-five years ago'), '그 뒤에는 가르쳤다는 불규칙 과거형 동사', (None, 'taught'), '바로 이 형태가 자연스럽게 호응해요.']),
    (10, None, ["'우선 당분간은 그분 가방도 자물쇠를 채워 안전하게 보관해 둘게요.' 아무도 손대지 못하게 철통같이 잠가 둔 상태를 영어에서는", (None, 'under lock and key'), '이렇게 자물쇠와 열쇠를 나란히 묶어 말해요.']),
    (11, None, ["'든든하네요! 이제 푸짐한 아침 식사를 먹을 준비가 다 되었어요.' 어떤 식사나 활동을 맞이할 채비가 끝났다고 할 때는 전치사를 이은", (None, 'ready for'), '방금 들은 이 표현 뒤에 명사를 붙이면 자연스러워요.']),
]
