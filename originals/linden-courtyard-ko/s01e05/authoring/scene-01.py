# Authoring module for linden-courtyard-ko-s01e05-scene-01.
ID = 'linden-courtyard-ko-s01e05-scene-01'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'Truth in the Courtyard  (안뜰에서 밝혀진 진실)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'evelyn': 'Evelyn'}
INTRO = '메인주 포틀랜드의 린든 코트야드 여관 안뜰에서 마침내 케일럽과 에블린 선생님이 마주 섰어요. 월요일 기차에서 가방이 뒤바뀐 사연부터 밤중에 현관 계단에 가방을 두고 달아났던 이유까지 차례차례 밝혀집니다. 먼저 세 사람의 대화를 편안하게 들어 보세요.'
OPENER = '방금 들은 안뜰의 대화를 한 문장씩 찬찬히 짚어 볼까요.'
TRANSITION = '이제 사연의 흐름을 떠올리며 장면 전체를 다시 들어 보세요.'
OUTRO = '우연히 뒤바뀐 가방과 월요일 밤의 급한 걸음 뒤에 형 오언의 이야기가 숨어 있었군요. 하얀 종이 꾸러미에 담긴 사연이 무엇인지 점점 더 궁금해집니다. 다음 장면에서 이어서 만나요.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('evelyn', 'Let me look at you properly, Caleb! You grew taller than the piano!', '제대로 얼굴 좀 보자꾸나, 케일럽! 피아노보다도 키가 더 자랐구나!'),
    ('caleb', 'I cannot believe you are staying in the exact same guesthouse, Miss Evelyn.', '에블린 선생님께서 바로 이 똑같은 여관에 묵고 계시다니 믿기지 않아요.'),
    ('hannah', 'Wait, so you rode the same train on Monday and took her suitcase?', '잠깐, 그럼 선생님이 월요일에 같은 기차를 타셨고, 부인 가방을 가져가신 거예요?'),
    ('caleb', "By complete accident! At my cousin's apartment I opened it and saw sheet music and a red ribbon.", '완전히 실수였어요! 사촌 아파트에서 가방을 열어 보고 악보와 빨간 리본을 발견했거든요.'),
    ('evelyn', 'Why did you leave my bag on the step at night and run away?', '어째서 밤에 내 가방을 현관 계단에 두고 그대로 달아났니?'),
    ('caleb', 'Because when I walked here on Monday evening, I saw my older brother walking down this street!', '월요일 저녁에 이리로 걸어오다가 우리 형이 이 거리를 걸어 내려가는 모습을 보았거든요!'),
    ('hannah', 'Your older brother lives here in Portland?', '형님이 여기 포틀랜드에 살고 계시나요?'),
    ('caleb', 'Yes. I panicked, rang your bell, and slipped the Friday note onto the handle.', '네. 당황해서 여관 벨을 누르고 손잡이 위에 금요일 쪽지를 끼워 넣었어요.'),
    ('evelyn', 'Wait, and Wednesday night you checked in here under your real name?', '잠깐, 그런데 수요일 밤에는 본명으로 이곳에 숙박 수속을 한 거니?'),
    ('caleb', 'I needed a quiet place nearby before Friday, and honestly felt too shy to ask for my bag!', '금요일 전에 근처 조용한 숙소가 필요했는데, 제 가방을 달라고 하기 너무 민망했거든요!'),
    ('hannah', 'Even after you called us on Tuesday about the white package!', '화요일에 하얀 소포 때문에 저희한테 전화까지 하셨으면서요!'),
    ('caleb', 'Everything in that white paper belongs to my brother Owen, not me.', '저 하얀 종이 안에 든 물건은 전부 제가 아니라 제 형 오언의 것이에요.'),
]
WALK = [
    (0, None, ["'제대로 얼굴 좀 보자꾸나, 케일럽! 피아노보다도 키가 더 자랐구나!' 비교급 형용사 뒤에 기준 대상을 이어 붙인", (None, 'taller than the piano'), '어린 제자가 훌쩍 자랐음을 재치 있게 비유한 구절이에요.']),
    (1, None, ["'에블린 선생님께서 바로 이 똑같은 여관에 묵고 계시다니 믿기지 않아요.' 뜻밖의 반가운 우연 앞에서 놀라움을 터뜨릴 때", (None, 'I cannot believe'), '뒤쪽에 대절 전체를 자연스럽게 이어 말해요.']),
    (2, None, ["'잠깐, 그럼 선생님이 월요일에 같은 기차를 타셨고, 부인 가방을 가져가신 거예요?' 기차나 버스를 이용했다는 과거 동작은 불규칙 동사를 살린", (None, 'rode the same train'), '이렇게 간결한 어순으로 표현해요.']),
    (3, None, ["'완전히 실수였어요! 사촌 아파트에서 가방을 열어 보고 악보와 빨간 리본을 발견했거든요.' 고의가 전혀 아니었음을 힘주어 해명할 때는", (None, 'By complete accident'), '전치사구 하나로 억울한 마음을 깔끔하게 전해요.']),
    (4, None, ["'어째서 밤에 내 가방을 현관 계단에 두고 그대로 달아났니?' 의문문 조동사 뒤라 물건을 두고 떠나다는 동사원형", (None, 'leave'), '그리고 서둘러 도망치다는 구동사', (None, 'run away'), '두 표현 모두 원형 그대로 나란히 놓였어요.']),
    (5, None, ["'월요일 저녁에 이리로 걸어오다가 우리 형이 이 거리를 걸어 내려가는 모습을 보았거든요!' 지각동사 목적어 뒤에 현재분사를 덧붙인", (None, 'walking down this street'), '눈앞에서 걸어가던 생생한 순간을 그대로 그려 내요.']),
    (6, None, ["'형님이 여기 포틀랜드에 살고 계시나요?' 현재 거주지를 확인하며 되물을 때는 삼 인칭 단수 동사를 쓴", (None, 'lives here in Portland'), '평서문 어순 그대로 끝 억양만 높여 질문해요.']),
    (7, None, ["'네. 당황해서 여관 벨을 누르고 손잡이 위에 금요일 쪽지를 끼워 넣었어요.' 움직여서 어딘가 표면에 닿게 올리는 방향감은", (None, 'onto the handle'), '전치사 하나로 손잡이에 쪽지를 건 동작을 선명히 보여 줘요.']),
    (8, None, ["'잠깐, 그런데 수요일 밤에는 본명으로 이곳에 숙박 수속을 한 거니?' 여관에 투숙 등록을 마쳤다는 구동사", (None, 'checked in'), '뒤이어 가명이 아닌 진짜 이름이라는 뜻의', (None, 'under your real name'), '전치사구가 덧붙어 놀라움을 드러내요.']),
    (9, None, ["'금요일 전에 근처 조용한 숙소가 필요했는데, 제 가방을 달라고 하기 너무 민망했거든요!' 명사 뒤에서 가까운 곳이라는 위치를 보태 줄 때는", (None, 'nearby'), '한 단어를 뒤쪽에 가볍게 붙여 거리를 설명해요.']),
    (10, None, ["'화요일에 하얀 소포 때문에 저희한테 전화까지 하셨으면서요!' 상대에게 어떤 행동을 하지 말아 달라고 정중히 청할 때는", (None, 'about the white package'), '투 부정사 바로 앞에 부정어를 두어 말해요.']),
    (11, None, ["'저 하얀 종이 안에 든 물건은 전부 제가 아니라 제 형 오언의 것이에요.' 물건의 진짜 주인이 누구인지 밝힐 때는 소유격 대명사 대신", (None, 'belongs to my brother'), '자동사와 전치사를 짝지어 소속을 분명히 나타내요.']),
]
