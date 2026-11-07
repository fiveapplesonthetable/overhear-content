# Authoring module for haessal-guesthouse-s02e01-scene-03.
ID = 'haessal-guesthouse-s02e01-scene-03'
SHOW = 'haessal-guesthouse'
SEASON = 2
EPISODE = 1
SCENE = 3
TITLE = '유리와 먼지  (Glass and Dust)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'mina': '미나', 'sora': '소라', 'sungmin': '성민'}
INTRO = 'Mina pushes the narrow white door open, and morning light filters through dusty glass panes into a quiet forgotten room. Sora and Sungmin step inside behind her in amazement. Listen to the whole scene first.'
OPENER = "Let's step into the hidden room together, one line at a time."
TRANSITION = "Now let's listen to the whole sunroom discovery again."
OUTRO = "Room 9 is a dry, sunlit glass tea room, and something tall is waiting under a white sheet in the corner. Let's find out what it is next time."
CLOSING = ('sungmin', '안녕히 가세요!')
STORY = [
    ('mina', '이 높은 유리창들 좀 보세요! 안마당 나무가 보여요!', 'Look at these tall glass windows! You can see the courtyard tree!'),
    ('sora', '밖에 덧문이 닫혀 있어서 아무도 몰랐네요!', 'The shutters were closed outside, so nobody knew!'),
    ('sungmin', "이제 기억나요! 제가 열 살 때 삼촌이 여기를 '겨울 찻집'이라고 불렀어요!", "Now I remember! When I was ten, my uncle called this place 'the winter tea room'!"),
    ('mina', '왜 이렇게 밝고 예쁜 방을 책장 뒤에 숨겼어요?', 'Why did someone hide such a bright, pretty room behind a bookcase?'),
    ('sungmin', '비 오는 어느 봄에 유리 지붕이 샜어요. 고칠 돈이 없었어요.', 'One rainy spring the glass roof leaked. There was no money to fix it.'),
    ('sora', '사장님, 돌 바닥을 보세요. 물이 한 방울도 없어요!', 'Boss, look at the stone floor. There is not a single drop of water!'),
    ('mina', '몇 년 전에 안마당 지붕을 고친 사람이 이 천장도 고쳤어요!', 'Whoever fixed the courtyard roof years ago fixed this ceiling too!'),
    ('sora', '사장님, 여기에 작은 카페 테이블이 몇 개 들어갈까요?', 'Boss, how many small café tables could fit in here?'),
    ('sungmin', '잠깐만요! 우리가 시청에 동네 북카페를 약속했어요!', 'Wait! We promised City Hall a neighbourhood reading café!'),
    ('mina', '시청 편지에 나온 방이 바로 여기네요!', 'The room in the City Hall letter is right here!'),
    ('sora', '따뜻한 빵, 뜨거운 차, 아침 햇살! 차가운 바람은 하나도 없어요!', 'Warm bread, hot tea, morning sunshine! And no cold wind at all!'),
    ('sungmin', '어, 저 구석에 하얀 커버 밑에 뭐가 있어요?', 'Hey, what is under that white cloth in the corner?'),
]
WALK = [
    (0, None, ["'Look at these tall glass windows! You can see the courtyard tree!' The word ", (None, '유리창들'), " is built from 'glass' and 'window', with a plural tag on the end."]),
    (1, None, ["'The shutters were closed outside, so nobody knew!' Korean pairs 'anybody' with a negative to say 'nobody': ", (None, '아무도 몰랐네요'), '.']),
    (2, None, ["'Now I remember! When I was ten, my uncle called this place the winter tea room!' In Korean a memory comes out by itself: ", (None, '기억나요'), ", literally 'memory comes out'."]),
    (4, None, ["'One rainy spring the glass roof leaked. There was no money to fix it.' A leaking roof or bottle uses ", (None, '샜어요'), ", the past of 'to leak'."]),
    (5, None, ["'Boss, look at the stone floor. There is not a single drop of water!' Adding 'even' to 'one drop' and then a negative gives 'not a single drop': ", (None, '한 방울도 없어요'), '.']),
    (7, None, ["'Boss, how many small café tables could fit in here?' Ask 'how many things' with ", (None, '몇 개'), ", and swap in any object you are counting."]),
    (8, None, ["'Wait! We promised City Hall a neighbourhood reading café!' Korean borrows 'book café' from English for a café full of books: ", (None, '북카페'), '.']),
    (10, None, ["'Warm bread, hot tea, morning sunshine! And no cold wind at all!' Listen for ", (None, '햇살'), ', the sunshine in the name Sunshine House itself.']),
    (11, None, ["'Hey, what is under that white cover in the corner?' The corner of a room is ", (None, '구석'), ', the inside corner where things get forgotten.']),
]
