# Authoring module for linden-courtyard-ko-s01e06-scene-06.
ID = 'linden-courtyard-ko-s01e06-scene-06'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 6
SCENE = 6
TITLE = 'Permanent Keys  (정식 직원의 열쇠)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'arthur': 'Arthur', 'tessa': 'Tessa', 'hannah': 'Hannah'}
INTRO = '안도의 미소를 되찾은 아서가 카페 모퉁이에서 테사의 오랜 꿈이었던 아침 안뜰 카페 개장을 전격 선언해요. 이어서 닷새간의 수습 기간 마지막 날을 맞은 해나에게도 잊지 못할 제안을 건넵니다. 기쁨이 넘치는 대화를 들어 보세요.'
OPENER = '새 출발을 축하하는 세 사람의 대화를 차례로 살펴볼까요.'
TRANSITION = '지워지지 않는 잉크처럼 단단해진 동료애를 느끼며 다시 들어 보세요.'
OUTRO = '그레이엄의 커다란 종이 장부에 해나의 이름이 지워지지 않는 잉크로 당당히 적히게 되었어요. 내일 아침 여덟 시부터 동네 사람들에게 활짝 열릴 안뜰 카페도 참 기대됩니다. 다음 장면에서 만나요.'
CLOSING = ('arthur', 'See you later!')
STORY = [
    ('arthur', 'Tessa, how many cinnamon rolls and lemon cakes can your oven bake each morning?', '테사, 매일 아침 주방 오븐에서 시나몬 롤과 레몬 케이크를 몇 개나 구워 낼 수 있겠어요?'),
    ('tessa', 'Double what I make now! Are we really opening the courtyard cafe to our street?', '지금 만드는 양의 두 배는 거뜬해요! 정말 우리 거리 이웃들에게 안뜰 카페를 여는 건가요?'),
    ('arthur', 'Starting tomorrow at eight! Four tables inside, three tables under the tree!', '내일 아침 여덟 시부터 바로 시작합시다! 실내에 탁자 네 개, 나무 아래에 탁자 세 개로요!'),
    ('tessa', "My dream cafe, right here in our own courtyard! Wait until I tell the baker's market!", '제가 꿈꾸던 카페가 바로 우리 안뜰에 생기다니요! 제빵사 시장 사람들에게 알리면 다들 깜짝 놀랄 거예요!'),
    ('arthur', 'And now, Hannah, today is Friday, the last day of your five day trial week.', '그리고 이제 해나, 오늘은 금요일이니 닷새간의 수습 주간 마지막 날이군요.'),
    ('hannah', 'Oh! With the suitcases, the boiler, and the letter, I completely forgot!', '아! 여행 가방이며 보일러며 편지 소동 때문에 까맣게 잊고 있었어요!'),
    ('arthur', 'On Monday you opened our tricky door; since then you saved rooms, pipes, breakfast, and our lease.', '월요일에는 까다로운 현관문을 열더니, 그때 이후로 객실과 배관, 아침 식사, 이제는 임대 계약까지 구해 냈군요.'),
    ('tessa', 'If you do not hire her full time, Arthur, I am hiring her in my kitchen!', '아서, 해나를 정규직으로 채용하지 않으시면 제가 우리 주방 직원으로 데려갈 거예요!'),
    ('arthur', 'Hands off, Tessa! Hannah, would you stay as our permanent front desk manager?', '탐내지 말아요, 테사! 해나, 우리 여관의 정식 프런트 매니저로 계속 함께해 주겠어요?'),
    ('hannah', 'Stay here with all of you? Yes, a hundred times yes!', '여러분 모두와 이곳에 계속 함께하냐고요? 네, 백 번이고 네예요!'),
    ('arthur', "Wonderful! Your name goes in Graham's big paper book in permanent ink!", '정말 반갑군요! 그레이엄의 커다란 종이 장부에 지워지지 않는 잉크로 해나의 이름이 올라갑니다!'),
    ('hannah', 'Best first week of my life!', '제 인생 최고의 첫 출근 주간이에요!'),
]
WALK = [
    (0, None, ["'테사, 매일 아침 주방 오븐에서 시나몬 롤과 레몬 케이크를 몇 개나 구워 낼 수 있겠어요?' 셀 수 있는 빵과 케이크의 수량을 물어볼 때는 의문사 덩어리", (None, 'how many'), '뒤에 복수 명사를 나란히 이어 붙여요.']),
    (1, None, ["'지금 만드는 양의 두 배는 거뜬해요! 정말 우리 거리 이웃들에게 안뜰 카페를 여는 건가요?' 현재 분량의 갑절이라는 뜻을 힘차게 말할 때는 관계대명사절 앞에", (None, 'Double what I make now'), '어순을 세워 자신만만한 대답을 완성해요.']),
    (2, None, ["'내일 아침 여덟 시부터 바로 시작합시다! 실내에 탁자 네 개, 나무 아래에 탁자 세 개로요!' 새로운 일정이 언제부터 개시되는지 시원스럽게 선언할 때는 분사로 시작하는", (None, 'Starting tomorrow'), '구절로 활기찬 출발을 알려요.']),
    (3, None, ["'제가 꿈꾸던 카페가 바로 우리 안뜰에 생기다니요! 제빵사 시장 사람들에게 알리면 다들 깜짝 놀랄 거예요!' 오랫동안 마음속에 그려 온 이상적인 공간을 가리킬 때는 명사를 나란히 둔", (None, 'My dream cafe'), '표현으로 벅찬 설렘을 전해요.']),
    (4, None, ["'그리고 이제 해나, 오늘은 금요일이니 닷새간의 수습 주간 마지막 날이군요.' 일솜씨를 맞춰 보는 닷새짜리 수습 기간은 하이픈 느낌의 복합 수식어", (None, 'five day trial week'), '단수 명사 조합으로 간결하게 일컬어요.']),
    (5, None, ["'아! 여행 가방이며 보일러며 편지 소동 때문에 까맣게 잊고 있었어요!' 정신없이 바빠서 어떤 사실을 완전히 잊어버렸다고 고백할 때는 부사를 넣은", (None, 'I completely forgot'), '세 단어로 솔직한 놀라움을 나타내요.']),
    (6, None, ["'월요일에는 까다로운 현관문을 열더니, 그때 이후로 객실과 배관, 아침 식사, 이제는 임대 계약까지 구해 냈군요.' 앞서 언급한 과거 시점부터 지금까지 줄곧 이어진 흐름을 짚을 때는", (None, 'since then'), '짧은 부사구로 눈부신 활약을 이어 줘요.']),
    (7, None, ["'아서, 해나를 정규직으로 채용하지 않으시면 제가 우리 주방 직원으로 데려갈 거예요!' 임시직이 아닌 전일제 정식 직원으로 고용한다는 직장 표현은", (None, 'hire her full time'), '동사 목적어 뒤에 부사구를 바로 덧붙여 말해요.']),
    (8, None, ["'탐내지 말아요, 테사! 해나, 우리 여관의 정식 프런트 매니저로 계속 함께해 주겠어요?' 손대지 말라고 유쾌하게 가로막는", (None, 'Hands off'), '그리고 정중하게 의향을 묻는 제안 구문', (None, 'would you stay'), '두 표현이 어우러져 따뜻한 채용 제안을 완성해요.']),
    (9, None, ["'여러분 모두와 이곳에 계속 함께하냐고요? 네, 백 번이고 네예요!' 조금의 망설임도 없이 온 마음으로 승낙할 때는 횟수를 강조한", (None, 'a hundred times yes'), '관용구로 벅찬 기쁨을 터뜨려요.']),
    (10, None, ["'정말 반갑군요! 그레이엄의 커다란 종이 장부에 지워지지 않는 잉크로 해나의 이름이 올라갑니다!' 연필 대신 영구히 남는 만년필 잉크로 기록한다는 비유는 전치사구", (None, 'in permanent ink'), '표현을 써서 든든한 한 식구가 되었음을 축하해요.']),
    (11, None, ["'제 인생 최고의 첫 출근 주간이에요!' 일생에서 가장 행복하고 뜻깊었던 첫 주를 감탄문으로 압축할 때는 최상급으로 여는", (None, 'Best first week of my life'), '명사구 하나로 벅찬 감동을 마무리해요.']),
]
