# Authoring module for linden-courtyard-ko-s01e04-scene-02.
ID = 'linden-courtyard-ko-s01e04-scene-02'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = 'The Blue Door  (파란 나무 문)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '강을 건너 초록색 약국을 지나온 해나가 작은 돌 분수대 앞에서 그레이엄에게 전화를 걸어요. 마지막 갈림길에서 꽃 가판대 옆길을 택한 해나는 마침내 황금 열쇠 그림이 그려진 파란 문을 발견합니다. 통화 장면을 들어 보세요.'
OPENER = '광장 앞에서 주고받은 긴박한 전화 통화를 한 줄씩 살펴볼까요.'
TRANSITION = '그럼 숨 가쁜 아침 심부름 장면을 처음부터 다시 들어 보세요.'
OUTRO = '다행히 선반에 꼭 맞는 황동 밸브가 두 개나 남아 있어 예비 부품까지 든든히 챙겼어요. 현금 계산을 마치고 다리를 향해 다시 달리는 해나의 뒤편으로 여관에서는 손님의 발소리가 들려옵니다. 곧 다음 장면으로 이어져요.'
CLOSING = ('graham', 'Bye for now!')
STORY = [
    ('hannah', 'Graham, can you hear me? I just passed the green pharmacy!', '그레이엄, 제 목소리 들려요? 방금 초록색 약국을 지나쳤어요!'),
    ('graham', 'Loud and clear. Are you standing by the little stone fountain?', '크고 또렷하게 잘 들립니다. 작은 돌 분수대 옆에 서 있나요?'),
    ('hannah', 'Yes! There are two small streets on the left. Which one do I take?', '네! 왼쪽에 작은 길이 두 갈래 있는데 어느 쪽으로 가야 하나요?'),
    ('graham', 'Take the second street, beside the flower stand, not the narrow alley.', '좁은 골목 말고 꽃 가판대 옆에 있는 두 번째 길로 가세요.'),
    ('hannah', 'Walking now... oh, I see the golden key sign and the blue door!', '지금 걸어가고 있어요. 아, 황금 열쇠 간판이랑 파란 문이 보여요!'),
    ('graham', 'Good! Is the shutter open?', '좋아요! 가게 덧문은 열려 있나요?'),
    ('hannah', 'He is unlocking it right now! Stay on the phone one second.', '주인이 지금 막 자물쇠를 열고 있어요! 전화 끊지 말고 잠시만 기다려 주세요.'),
    ('graham', 'Make sure the brass ring inside is twenty millimeters wide.', '안쪽 황동 고리 너비가 이십 밀리미터인지 꼭 확인하세요.'),
    ('hannah', 'He matched it against the old one. He has two left on the shelf!', '헌 부품에 대어 보더니 딱 맞대요. 선반에 두 개 남아 있네요!'),
    ('graham', 'Buy both! A spare valve saves next winter too.', '둘 다 사 오세요! 여분 밸브가 있으면 내년 겨울도 무사히 넘길 수 있으니까요.'),
    ('hannah', 'Paid in cash! Keep your toolbox open, I am running back across the bridge!', '현금으로 계산했어요! 공구함 열어 두세요, 지금 다리 건너 뛰어가는 중이에요!'),
    ('graham', 'Hurry, I just heard footsteps on the second floor stairs!', '서둘러요, 방금 이 층 계단에서 발소리가 들렸어요!'),
]
WALK = [
    (0, None, ["'그레이엄, 제 목소리 들려요? 방금 초록색 약국을 지나쳤어요!' 전화기를 넘어 내 목소리가 잘 전달되는지 가장 먼저 확인하는 인사가", (None, 'can you hear me'), '통화 연결 상태를 점검하는 가장 자연스럽고 흔한 표현이죠.']),
    (1, None, ["'크고 또렷하게 잘 들립니다. 작은 돌 분수대 옆에 서 있나요?' 음질이 아주 선명해서 한마디도 놓치지 않고 들린다는 관용 표현이", (None, 'Loud and clear'), '두 형용사를 짝지어 전화 응답으로 아주 시원하게 쓰여요.']),
    (2, None, ["'네! 왼쪽에 작은 길이 두 갈래 있는데 어느 쪽으로 가야 하나요?' 눈앞에 놓인 정해진 선택지 가운데 하나를 골라 달라고 물을 때 쓰는 말이", (None, 'Which one'), '막연한 무엇이 아니라 둘 중 어느 길인지 콕 집어 질문해요.']),
    (3, None, ["'좁은 골목 말고 꽃 가판대 옆에 있는 두 번째 길로 가세요.' 거리에서 꽃을 펼쳐 놓고 파는 작은 노점이나 매대를 가리키는 명사구가", (None, 'flower stand'), '길 찾기 이정표로 삼기 좋은 정겨운 거리 풍경 단어예요.']),
    (4, None, ["'지금 걸어가고 있어요. 아, 황금 열쇠 간판이랑 파란 문이 보여요!' 애써 찾지 않아도 시야에 자연스럽게 딱 들어왔다는 순간의 발견은", (None, 'I see'), '진행형이 아닌 단순 현재형 동사로 눈앞에 보인 반가움을 전해요.']),
    (5, None, ["'좋아요! 가게 덧문은 열려 있나요?' 아침 영업 시작 전에 가게 앞을 가려 두는 철제나 나무 덧문을 뜻하는 단어가", (None, 'shutter'), '상점이 문을 열었는지 외관으로 확인할 때 유용하게 쓰여요.']),
    (6, None, ["'주인이 지금 막 자물쇠를 열고 있어요! 전화 끊지 말고 잠시만 기다려 주세요.' 통화를 종료하지 않고 수화기를 든 채 그대로 대기해 달라는 부탁이", (None, 'Stay on the phone'), '연결 상태를 유지하라는 전치사를 써서 현장감을 이어 가요.']),
    (7, None, ["'안쪽 황동 고리 너비가 이십 밀리미터인지 꼭 확인하세요.' 부품의 가로 폭이나 지름 치수를 정확하게 수치로 설명하는 방식이", (None, 'twenty millimeters wide'), '단위 명사 바로 뒤에 폭을 뜻하는 형용사를 붙여 규격을 마무리해요.']),
    (8, None, ["'헌 부품에 대어 보더니 딱 맞대요. 선반에 두 개 남아 있네요!' 팔리고 남은 재고 수량을 간결하게 알려 주는 표현이 바로", (None, 'two left'), '숫자 뒤에 남겨진이라는 분사를 붙여 잔여 수량을 단번에 나타내요.']),
    (9, None, ["'둘 다 사 오세요! 여분 밸브가 있으면 내년 겨울도 무사히 넘길 수 있으니까요.' 남아 있는 두 개를 하나도 빠짐없이 전부 구매하라고 권하는 짧은 명령문이", (None, 'Buy both'), '두 대상 모두를 아우르는 대명사로 망설임 없는 결정을 전해 줘요.']),
    (10, None, ["'현금으로 계산했어요! 공구함 열어 두세요, 지금 다리 건너 뛰어가는 중이에요!' 카드가 아니라 지폐나 동전으로 값을 치렀다는 결제 수단 표현은", (None, 'in cash'), '화폐 형태를 나타내는 전치사와 함께 한 덩어리로 외워 두면 편리해요.']),
    (11, None, ["'서둘러요, 방금 이 층 계단에서 발소리가 들렸어요!' 시간이 촉박한 순간 상대에게 어서 빨리 움직이라고 다급히 외치는 한마디가", (None, 'Hurry'), '동사 하나만 단독으로 던져 일 초가 급한 긴장감을 생생히 전달해요.']),
]
