# Authoring module for linden-courtyard-ko-s01e02-scene-03.
ID = 'linden-courtyard-ko-s01e02-scene-03'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = 'Counting the Change  (정확한 거스름돈과 짭짤한 버터)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'hannah': 'Hannah', 'arthur': 'Arthur', 'tessa': 'Tessa'}
INTRO = '해나가 단 구 분 만에 두 손 가득 장바구니를 들고 숨을 헐떡이며 돌아옵니다. 거스름돈 열두 달러까지 동전 하나 틀리지 않고 완벽했지만 급히 집어 온 금박 포장지 버터가 그만 짭짤한 바닷소금 버터였네요. 먼저 생생한 대화를 들어 보세요.'
OPENER = '이제 위기를 재치 있게 넘기는 표현들을 한 문장씩 살펴볼까요.'
TRANSITION = '장면 전체를 자연스러운 호흡으로 다시 한번 들어 보세요.'
OUTRO = '테사의 재빠른 기지 덕분에 가염 버터는 스크램블드에그에 넣어 풍미를 한층 살리기로 했어요. 이제 안뜰에서 싱싱한 허브만 더하면 아침 식탁 준비가 완성됩니다. 다음 장면에서 만나요.'
CLOSING = ('tessa', 'Bye for now!')
STORY = [
    ('hannah', 'Nine minutes! Here are the milk, the eggs, and the apples!', '구 분 걸렸어요! 여기 우유랑 달걀이랑 사과 다 사 왔어요!'),
    ('tessa', 'You are a hero, Hannah! Give me the milk first for the coffee machine.', '해나 씨, 정말 생명의 은인이에요! 커피 기계에 넣게 우유부터 먼저 주세요!'),
    ('arthur', 'Impressive speed! Did the shopkeeper give you a receipt?', '놀라운 속도네요! 가게 주인이 영수증은 주던가요?'),
    ('hannah', 'Right here! Everything cost thirty-eight, so here is twelve in change.', '바로 여기 있어요! 전부 서른여덟 달러가 들어서 여기 거스름돈 열두 달러예요.'),
    ('arthur', 'Ten, eleven, twelve. Exact to the last coin, thank you!', '열, 열하나, 열둘. 마지막 동전 하나까지 정확하네요, 고마워요!'),
    ('tessa', 'Wait a second, Hannah... which pack of butter did you grab?', '잠깐만요, 해나... 어느 버터 팩을 집어 왔어요?'),
    ('hannah', 'The gold wrapper on the top shelf. Why?', '맨 위 선반에 있던 금빛 포장지 제품이요. 왜요?'),
    ('tessa', 'That is extra salty sea butter! My sweet jam rolls need plain butter!', '그건 아주 짠 바닷소금 버터예요! 달콤한 잼 롤빵에는 무염 기본 버터가 필요한데요!'),
    ('hannah', 'Oh no! All the wrappers looked the same when I was running!', '어머 어쩌죠! 뛰어다니느라 포장지가 전부 똑같아 보였어요!'),
    ('arthur', 'Can we serve salty butter with sweet strawberry jam?', '달콤한 딸기잼에 짭짤한 버터를 같이 내어 드려도 괜찮을까요?'),
    ('tessa', 'Wait, salty butter is terrible for jam, but amazing for scrambled eggs!', '잠깐만요, 짠 버터는 잼에는 최악이지만 스크램블드에그에는 기가 막히게 잘 어울려요!'),
    ('hannah', 'Phew! Quick thinking saves breakfast again.', '휴! 재빠른 판단력이 또 한 번 아침 식사를 구했네요.'),
]
WALK = [
    (0, None, ["'구 분 걸렸어요! 여기 우유랑 달걀이랑 사과 다 사 왔어요!' 여러 가지 물건을 한꺼번에 내놓으며 여기 있다고 알릴 때는 복수형인", (None, 'Here are'), '방금 들은 이 표현으로 경쾌하게 운을 떼요.']),
    (1, None, ["'해나 씨, 정말 생명의 은인이에요! 커피 기계에 넣게 우유부터 먼저 주세요!' 급한 불을 꺼 준 고마운 동료를 힘껏 치켜세울 때는", (None, 'a hero'), '이렇게 영웅이라는 표현을 아낌없이 건네요.']),
    (2, None, ["'놀라운 속도네요! 가게 주인이 영수증은 주던가요?' 상대에게 무언가를 건네주다라는 두 목적어 어순 그대로", (None, 'give you a receipt'), '이렇게 사람 뒤에 물건을 바로 이어 물어봐요.']),
    (3, None, ["'바로 여기 있어요! 전부 서른여덟 달러가 들어서 여기 거스름돈 열두 달러예요.' 과거에도 형태가 똑같은 비용 동사", (None, 'cost'), '그리고 거스름돈으로 남았다는 뜻의', (None, 'in change'), '두 표현은 장보기 회화의 핵심이에요.']),
    (4, None, ["'열, 열하나, 열둘. 마지막 동전 하나까지 정확하네요, 고마워요!' 단 일 센트의 오차도 없이 금액이 딱 맞아떨어질 때", (None, 'to the last coin'), '방금 들은 이 구절로 꼼꼼함을 칭찬해 줘요.']),
    (5, None, ["'잠깐만요, 해나... 어느 버터 팩을 집어 왔어요?' 매대에 있던 여러 종류 가운데 어느 포장을 골랐는지 물어볼 때는", (None, 'which pack'), '이렇게 선택 의문사를 명사 앞에 붙여요.']),
    (6, None, ["'맨 위 선반에 있던 금빛 포장지 제품이요. 왜요?' 선반 표면에 놓인 위치를 가장 위쪽과 함께 짚어 줄 때는", (None, 'on the top shelf'), '방금 들은 이 전치사구로 자리를 정확히 설명해요.']),
    (7, None, ["'그건 아주 짠 바닷소금 버터예요! 달콤한 잼 롤빵에는 무염 기본 버터가 필요한데요!' 소금이나 향료를 더하지 않은 담백한 기본 버터는", (None, 'plain butter'), '이렇게 꾸밈없다는 뜻의 형용사로 불러요.']),
    (8, None, ["'어머 어쩌죠! 뛰어다니느라 포장지가 전부 똑같아 보였어요!' 겉모습이 서로 다름없이 똑같아 보였다고 말할 때는 정관사를 꼭 챙긴", (None, 'looked the same'), '바로 이 표현을 써요.']),
    (9, None, ["'달콤한 딸기잼에 짭짤한 버터를 같이 내어 드려도 괜찮을까요?' 손님 식탁에 그 조합으로 차려 내도 될지 상의할 때는", (None, 'Can we serve'), '이렇게 조동사로 가능성을 차분히 물어봐요.']),
    (10, None, ["'잠깐만요, 짠 버터는 잼에는 최악이지만 스크램블드에그에는 기가 막히게 잘 어울려요!' 달걀을 부드럽게 풀어 익힌 대표 아침 메뉴는 항상 복수형인", (None, 'scrambled eggs'), '방금 들은 이 이름으로 식탁에 올라요.']),
    (11, None, ["'휴! 재빠른 판단력이 또 한 번 아침 식사를 구했네요.' 가슴을 쓸어내리는 안도의 한숨 소리", (None, 'Phew'), '이어서 순간적인 기지를 칭찬하는', (None, 'Quick thinking'), '두 표현이 유쾌한 반전을 마무리해 줘요.']),
]
