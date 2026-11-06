# Authoring module for haessal-guesthouse-s01e01-scene-01.
ID = 'haessal-guesthouse-s01e01-scene-01'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = '손잡이를 올리세요  (Lift the Handle)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'mina': '미나', 'junho': '준호'}
INTRO = 'Mina arrives early for her very first morning at Sunshine House in Seoul. Behind the front desk, veteran handyman Junho is already pouring hot tea. Listen to the scene first without worrying about catching every word.'
OPENER = "Now let's walk through the conversation one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Mina is inside, the eight brass keys are on the board, and her first morning has begun. Don't worry if a few words went past quickly; they come back all week. See you next time."
CLOSING = ('mina', '안녕히 계세요!')
STORY = [
    ('mina', '안녕하세요! 실례지만 문이 잠겼어요?', 'Good morning! Excuse me, is the door locked?'),
    ('junho', '안녕하세요. 아니요, 먼저 손잡이를 올리세요. 그리고 미세요.', 'Good morning. No, lift the handle first, then push.'),
    ('mina', '아, 열려요! 감사합니다. 저는 새 직원 미나예요.', 'Oh, it opens! Thank you. I am Mina, the new staff member.'),
    ('junho', '저는 준호예요. 십 분이나 일찍 왔네요.', 'I am Junho. You arrived ten minutes early.'),
    ('mina', '첫날에는 항상 빨리 걸어요. 컴퓨터는 어디에 있어요?', 'On my first day I always walk fast. Where is the computer?'),
    ('junho', '서랍 안에 있어요. 여기서는 큰 종이 장부하고 연필을 써요.', 'It is inside the drawer. Here we use a big paper ledger and a pencil.'),
    ('mina', '종이 장부요? 정말요?', 'A paper ledger? Really?'),
    ('junho', '종이는 비가 와도 방 목록을 안 잃어버려요.', 'Paper does not lose the room list even when it rains.'),
    ('mina', '맞아요! 그럼 이건 열쇠예요?', "That's true! Then are these the keys?"),
    ('junho', '네, 방 여덟 개에 황동 열쇠 여덟 개예요. 오늘 사호실 손님이 와요.', 'Yes, eight rooms and eight brass keys. Today the Room 4 guest arrives.'),
    ('mina', '좋아요. 꼭 알아야 할 것을 다 알려 주세요.', 'Great. Please tell me everything I must know.'),
    ('junho', '첫 번째 규칙이에요. 따뜻한 차를 먼저 마시세요. 그다음에 종을 받으세요.', 'Rule number one. Drink warm tea first. After that, answer the bell.'),
]
WALK = [
    (0, None, ["'Good morning! Excuse me, is the door locked?' Morning, afternoon, or evening, Seoul speakers greet each other with ", (None, '안녕하세요'), ', literally asking whether you are at peace.']),
    (1, None, ["'Good morning. No, lift the handle first, then push.' Notice the compound word ", (None, '손잡이를'), ", built from 'hand' and 'grab' for a door handle."]),
    (2, None, ["'Oh, it opens! Thank you. I am Mina, the new staff member.' Humble self-introductions open with ", (None, '저는'), ", pairing the polite 'I' with a topic marker."]),
    (3, None, ["'I am Junho. You arrived ten minutes early.' Adding ", (None, '일찍'), " before 'came' gives you the everyday word for 'early'."]),
    (4, None, ["'On my first day I always walk fast. Where is the computer?' Keep the question chunk ", (None, '어디에 있어요'), ' in your pocket whenever you need to ask where something is.']),
    (5, None, ["'It is inside the drawer. Here we use a big paper ledger and a pencil.' Linking two everyday items in speech is easy with ", (None, '장부하고'), ", where the ending means 'and' or 'with'."]),
    (6, None, ["'A paper ledger? Really?' Adding a soft ending onto ", (None, '정말요'), " turns 'really' into a polite surprised question."]),
    (9, None, ["'Yes, eight rooms and eight brass keys. Today the Room 4 guest arrives.' Look at ", (None, '열쇠'), ", a lovely native compound that joins 'open' with 'iron' to mean 'key'."]),
    (11, None, ["'Rule number one. Drink warm tea first. After that, answer the bell.' Ending on ", (None, '마시세요'), " softens 'drink' into a warm, courteous instruction."]),
]
