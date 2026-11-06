# Authoring module for haessal-guesthouse-s01e04-scene-01.
ID = 'haessal-guesthouse-s01e04-scene-01'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = '여섯 시 사십오 분  (Six Forty-Five)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'junho': '준호', 'mina': '미나'}
INTRO = 'It is six forty-five in the morning at Sunshine House in Seoul. While the guests still sleep upstairs, Junho sketches a quick street map on paper for Mina. Listen to the whole scene first.'
OPENER = "Let's trace Junho's street directions step by step."
TRANSITION = "Now let's listen to the whole map scene again from start to finish."
OUTRO = 'Left at the gate, across the stone bridge, past the green pharmacy, and left into the square—Mina is off on her dawn mission. See you next time.'
CLOSING = ('mina', '또 봐요!')
STORY = [
    ('mina', '좋은 아침이에요, 준호 씨! 위층 샤워기 물이 벌써 정말 차가워요?', 'Good morning, Junho! Is the shower water upstairs really cold already?'),
    ('junho', '강물처럼 차가워요. 이 고장 난 황동 밸브를 코트 주머니에 넣으세요.', 'Cold as river water. Put this broken brass valve in your coat pocket.'),
    ('mina', '넣었어요. 이제 철물점에 어떻게 가는지 알려 주세요.', 'Put it in. Now please tell me how to get to the hardware shop.'),
    ('junho', '대문 밖에서 왼쪽으로 돌아서 돌다리까지 쭉 걸어가세요.', 'Turn left outside the front gate and walk straight to the stone bridge.'),
    ('mina', '대문에서 왼쪽, 돌다리까지 쭉이요. 강을 건너가요?', 'Left at the gate, straight to the stone bridge. Do I cross the river?'),
    ('junho', '네, 다리를 건너서 오른쪽에 있는 초록색 약국을 지나가세요.', 'Yes, cross the bridge and pass the green pharmacy on your right.'),
    ('mina', '다리를 건너고 오른쪽 초록색 약국이요. 그다음에는요?', 'Cross the bridge, green pharmacy on the right. And after that?'),
    ('junho', '작은 광장으로 왼쪽으로 도세요. 파란 나무 문을 찾으세요.', 'Turn left into the small square. Look for a blue wooden door.'),
    ('mina', '가게 밖에 큰 간판이 있어요?', 'Is there a big sign outside the shop?'),
    ('junho', '문 위에 그려진 금색 열쇠 그림뿐이에요. 직원한테 이 밸브를 보여 주세요.', 'Only a golden key painted above the door. Show this valve to the clerk.'),
    ('mina', '이십 밀리미터, 황동, 보일러 밸브! 가는 내내 외우면서 갈게요!', 'Twenty millimetres, brass, boiler valve! I will memorize and repeat it the whole way!'),
    ('junho', '빨리 뛰어요, 미나 씨. 사호실 손님은 일곱 시 십오 분에 일어나세요!', 'Run fast, Mina. The Room 4 guest wakes up at seven fifteen!'),
]
WALK = [
    (1, None, ["'Cold as river water. Put this broken brass valve in your coat pocket.' Slipping an object inside a bag or pocket uses ", (None, '주머니에 넣으세요'), '.']),
    (3, None, ["'Turn left outside the front gate and walk straight to the stone bridge.' One vivid syllable, ", (None, '쭉'), ', tells someone to head straight ahead without turning.']),
    (4, None, ["'Left at the gate, straight to the stone bridge. Do I cross the river?' Crossing a street, bridge, or river uses ", (None, '건너가요'), '.']),
    (5, None, ["'Yes, cross the bridge and pass the green pharmacy on your right.' Neighbourhood pharmacies are easy to spot and named ", (None, '약국을'), ", literally 'medicine office'."]),
    (6, None, ["'Cross the bridge, green pharmacy on the right. And after that?' Keep a direction-giver talking with the short prompt ", (None, '그다음에는요'), ", 'and next?'."]),
    (8, None, ["'Is there a big sign outside the shop?' Shop signs overhead use the Korean word ", (None, '간판이'), '.']),
    (10, None, ["'Twenty millimetres, brass, boiler valve! I will memorize and repeat it the whole way!' Learning words or directions by heart uses ", (None, '외우면서'), ", 'while memorizing'."]),
    (11, None, ["'Run fast, Mina. The Room 4 guest wakes up at seven fifteen!' Waking and getting out of bed is ", (None, '일어나세요'), ', here with respectful flair for the guest.']),
]
