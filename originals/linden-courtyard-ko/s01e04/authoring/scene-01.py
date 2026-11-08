# Authoring module for linden-courtyard-ko-s01e04-scene-01.
ID = 'linden-courtyard-ko-s01e04-scene-01'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = 'Six Forty-Five  (여섯 시 사십오 분)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah'}
INTRO = '이른 새벽 여섯 시 사십오 분, 손님들이 잠에서 깨기 전에 그레이엄이 해나에게 강 건너 철물점 가는 길을 꼼꼼히 일러 줘요. 해나는 고장 난 황동 밸브를 외투 주머니에 챙겨 넣고 아침 거리로 나설 준비를 합니다. 먼저 대화를 들어 보세요.'
OPENER = '새벽 프런트에서 나눈 길 안내 대화를 한 문장씩 함께 짚어 볼까요.'
TRANSITION = '그럼 해나의 발걸음처럼 경쾌한 이 장면을 다시 한번 들어 보세요.'
OUTRO = '사 호실 손님이 깨어나는 일곱 시 십오 분까지는 시간이 얼마 남지 않았어요. 규격과 재질을 입속으로 되뇌며 달려 나간 해나가 철물점을 단번에 찾을 수 있을까요. 다음 장면에서 확인해 봐요.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Good morning, Graham! Are the showers upstairs really cold already?', '좋은 아침이에요, 그레이엄! 위층 샤워기 물이 벌써 정말 차가운가요?'),
    ('graham', 'Cold as river water. Take this broken brass valve in your coat pocket.', '강물처럼 차갑습니다. 이 고장 난 황동 밸브를 외투 주머니에 챙겨 가세요.'),
    ('hannah', 'Got it. Now tell me how to find the hardware shop.', '알겠어요. 자, 이제 철물점 찾는 길을 알려 주세요.'),
    ('graham', 'Turn left outside our gate and walk straight to the stone bridge.', '우리 대문 밖으로 나가 왼쪽으로 돈 다음 돌다리까지 쭉 걸어가세요.'),
    ('hannah', 'Left at the gate, straight to the bridge. Do I cross the river?', '대문에서 왼쪽, 다리까지 직진이요. 강을 건너가나요?'),
    ('graham', 'Yes, cross the bridge, then pass the green pharmacy on your right.', '네, 다리를 건넌 뒤에 오른편에 보이는 초록색 약국을 지나가세요.'),
    ('hannah', 'Bridge, then green pharmacy on the right. And after that?', '다리 건너 오른편 초록색 약국이요. 그다음에는요?'),
    ('graham', 'Turn left into the small square. Look for a blue wooden door.', '작은 광장 안쪽으로 좌회전하세요. 파란 나무 문을 찾으면 됩니다.'),
    ('hannah', 'Does the shop have a big sign outside?', '가게 바깥에 커다란 간판이 걸려 있나요?'),
    ('graham', 'Only a painted golden key above the door. Show the clerk this valve.', '문 위에 그려진 황금 열쇠 그림뿐입니다. 점원에게 이 밸브를 보여 주세요.'),
    ('hannah', 'Twenty millimeters, brass, boiler valve. I will repeat it all the way!', '이십 밀리미터, 황동, 보일러 밸브요. 가는 내내 입속으로 되뇌면서 갈게요!'),
    ('graham', 'Run fast, Hannah. Room four wakes up at seven fifteen!', '빨리 뛰어요, 해나. 사 호실 손님은 일곱 시 십오 분에 일어나거든요!'),
]
WALK = [
    (0, None, ["'좋은 아침이에요, 그레이엄! 위층 샤워기 물이 벌써 정말 차가운가요?' 위층에 있는 욕실 시설의 상태를 묻는 질문이라서", (None, 'Are the showers upstairs'), '복수 동사로 문을 열고 위치 부사를 명사 바로 뒤에 덧붙였어요.']),
    (1, None, ["'강물처럼 차갑습니다. 이 고장 난 황동 밸브를 외투 주머니에 챙겨 가세요.' 얼음장 같은 차가움을 강물에 빗대어 생생하게 들려주는 구절이 바로", (None, 'Cold as river water'), '앞쪽 비교 부사를 생략해 한층 간결하고 힘 있는 대답이 되었죠.']),
    (2, None, ["'알겠어요. 자, 이제 철물점 찾는 길을 알려 주세요.' 물건도 챙겼고 상대의 당부도 확실히 접수했다는 경쾌한 맞장구로", (None, 'Got it'), '일상에서 알았다는 뜻을 가장 짧고 시원하게 전하는 두 단어예요.']),
    (3, None, ["'우리 대문 밖으로 나가 왼쪽으로 돈 다음 돌다리까지 쭉 걸어가세요.' 한눈팔지 말고 목표 지점까지 곧장 걸어가라고 길을 일러 주려면", (None, 'walk straight to'), '동사 뒤에 곧장이라는 부사와 도착지 전치사를 차례로 이어 붙이면 돼요.']),
    (4, None, ["'대문에서 왼쪽, 다리까지 직진이요. 강을 건너가나요?' 안내받은 경로를 따라 내가 직접 건너야 하는지 되물어 확인하는 표현은", (None, 'Do I cross'), '현재시제 의문문을 써서 길 찾기 순서를 또렷하게 점검해요.']),
    (5, None, ["'네, 다리를 건넌 뒤에 오른편에 보이는 초록색 약국을 지나가세요.' 걸어가는 사람의 오른쪽 방향에 건물이 자리 잡고 있음을 알려 주는 말은", (None, 'on your right'), '접촉의 전치사와 소유격을 결합해 진행 방향 기준 위치를 짚어 줘요.']),
    (6, None, ["'다리 건너 오른편 초록색 약국이요. 그다음에는요?' 앞선 설명을 복창한 뒤 이어지는 다음 순서를 재촉해 묻는 한마디가", (None, 'And after that'), '짧은 전치사구만으로 그다음 경로를 자연스럽게 이끌어 내죠.']),
    (7, None, ["'작은 광장 안쪽으로 좌회전하세요. 파란 나무 문을 찾으면 됩니다.' 방향을 꺾어 광장이라는 공간 내부로 들어서라고 안내하기 때문에", (None, 'Turn left into'), '단순한 지점 전치사 대신 안으로 들어가는 움직임의 전치사를 골랐어요.']),
    (8, None, ["'가게 바깥에 커다란 간판이 걸려 있나요?' 건물 외벽이나 문밖 쪽이라는 위치를 군더더기 없이 덧붙이는 부사가", (None, 'outside'), '명사 뒤에 가볍게 놓여 바깥쪽 간판 유무를 깔끔하게 물어봐요.']),
    (9, None, ["'문 위에 그려진 황금 열쇠 그림뿐입니다. 점원에게 이 밸브를 보여 주세요.' 누구에게 무엇을 보여 주라고 간접목적어와 직접목적어를 나란히 놓은 구문이", (None, 'Show the clerk this valve'), '전치사 없이도 사람과 사물 순서만으로 뜻이 명확히 통하는 문장이에요.']),
    (10, None, ["'이십 밀리미터, 황동, 보일러 밸브요. 가는 내내 입속으로 되뇌면서 갈게요!' 출발지부터 목적지에 닿는 거리와 시간 전체를 아우르는 관용구가", (None, 'all the way'), '도중에 잊어버리지 않도록 줄곧 반복하겠다는 의지를 잘 보여 줘요.']),
    (11, None, ["'빨리 뛰어요, 해나. 사 호실 손님은 일곱 시 십오 분에 일어나거든요!' 정해진 아침 기상 습관은 구동사", (None, 'wakes up'), '그리고 분 단위 시각은', (None, 'seven fifteen'), '중간 전치사 없이 시와 분 숫자만 나란히 읽어 경쾌하게 말해요.']),
]
