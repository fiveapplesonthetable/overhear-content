# Authoring module for haessal-guesthouse-s01e03-scene-08.
ID = 'haessal-guesthouse-s01e03-scene-08'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 3
SCENE = 8
TITLE = '얼음장 같은 배관  (Ice-Cold Pipes)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'junho': '준호', 'mina': '미나', 'sungmin': '성민'}
INTRO = 'Down at the front desk, Mina and Sungmin wait anxiously by the basement door until Junho climbs up wiping his hands on a cloth and shaking his head. Listen first.'
OPENER = "Let's hear Junho's diagnosis from the basement line by line."
TRANSITION = "Now let's listen to the final scene of Episode 3 again from start to finish."
OUTRO = "A suspected travel-guide writer upstairs, a cracked brass valve in the basement, and a seven o'clock race across the bridge tomorrow morning! Episode 3 is complete—see you in Episode 4."
CLOSING = ('junho', '다음에 만나요!')
STORY = [
    ('sungmin', '준호 씨, 그냥 작은 공기 방울이었다고 말해 주세요! 제발요!', 'Junho, tell me it was just a tiny air bubble! Please!'),
    ('junho', '안 좋은 소식이에요. 오래된 보일러의 황동 압력 밸브가 방금 고장 났어요.', 'Bad news. The brass pressure valve on the old boiler just broke down.'),
    ('mina', '그럼 오늘 밤 난방도 안 되고 온수도 안 나와요?', 'Then is there neither heating nor hot water tonight?'),
    ('junho', '벽돌 벽이 열기를 품고 있어서 아침까지는 방이 따뜻할 거예요, 미나 씨.', 'Because the brick walls hold heat, the rooms will stay warm until morning, Mina.'),
    ('sungmin', '천만다행이네요! 그럼 내일 아침 샤워는요?', "Thank goodness! What about tomorrow morning's showers?"),
    ('junho', '내일 아침이면 샤워기 물이 얼음장처럼 찰 거예요.', 'By tomorrow morning, the shower water will be ice-cold.'),
    ('sungmin', '얼음물 샤워라고요?! 삼층에 서울 여행 가이드북 작가가 주무시는데요?!', 'Ice-water showers?! While the Seoul travel guidebook writer is sleeping on the third floor?!'),
    ('mina', '공구함에 여분 황동 밸브는 없어요?', 'Is there no spare brass valve in your toolbox?'),
    ('junho', '지난겨울에 마지막 하나를 썼어요. 다리 건너 오래된 철물점에만 이 치수가 있어요.', 'I used the last one this past winter. Only the old hardware shop across the bridge has this size.'),
    ('mina', '그 철물점은 몇 시에 문을 열어요?', 'What time does that hardware shop open its doors?'),
    ('junho', '일곱 시 정각이요. 아침 식사 삼십 분 전이에요.', "Seven o'clock sharp. Thirty minutes before breakfast."),
    ('mina', '알람 맞추세요, 준호 씨. 내일 아침 우리가 찬물 샤워를 이길 거예요!', 'Set your alarm, Junho. Tomorrow morning we are going to beat those cold showers!'),
]
WALK = [
    (1, None, ["'Bad news. The brass pressure valve on the old boiler just broke down.' Machines, phones, and boilers fail with ", (None, '고장 났어요'), ", 'broke down'."]),
    (4, None, ["'Thank goodness! What about tomorrow morning's showers?' Big sighs of relief reach for ", (None, '천만다행이네요'), ", literally 'fortunate ten million times over'."]),
    (5, None, ["'By tomorrow morning, the shower water will be ice-cold.' Comparing freezing water to a sheet of river ice uses ", (None, '얼음장처럼'), ", 'like a slab of ice'."]),
    (7, None, ["'Is there no spare brass valve in your toolbox?' Extra parts, towels, or keys kept in reserve are ", (None, '여분'), ", 'spare'."]),
    (8, None, ["'I used the last one this past winter. Only the old hardware shop across the bridge has this size.' Neighbourhood tool and pipe shops are called ", (None, '철물점에만'), ", literally 'iron-goods store'."]),
    (9, None, ["'What time does that hardware shop open its doors?' Asking what hour anything opens or starts uses ", (None, '몇 시에'), ", 'at what time?'."]),
    (10, None, ["'Seven o'clock sharp. Thirty minutes before breakfast.' Place ", (None, '전이에요'), " right after a duration to say 'thirty minutes before'."]),
    (11, None, ["'Set your alarm, Junho. Tomorrow morning we are going to beat those cold showers!' Winning a game or a race against the clock uses ", (None, '이길 거예요'), ", 'will win'."]),
]
