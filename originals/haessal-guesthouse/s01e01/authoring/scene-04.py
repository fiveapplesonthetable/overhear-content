# Authoring module for haessal-guesthouse-s01e01-scene-04.
ID = 'haessal-guesthouse-s01e01-scene-04'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = '이층 사호실  (Room Four on the Second Floor)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'mina': '미나', 'youngmi': '영미', 'junho': '준호'}
INTRO = "At the front desk, retired piano teacher Youngmi steps inside from her taxi pulling a large dark-blue suitcase. Mina greets her first real guest while Junho stands ready to help with the bag. Let's hear how it goes."
OPENER = "Let's walk through the check-in line by line."
TRANSITION = "Now let's hear the whole check-in scene one more time."
OUTRO = 'Mina handled her first check-in smoothly, though Junho noticed that blue suitcase felt strangely heavy. See you next time to find out why.'
CLOSING = ('youngmi', '또 봐요!')
STORY = [
    ('mina', '어서 오세요! 좋은 아침이에요, 손님.', "Welcome! Good morning, ma'am."),
    ('youngmi', '안녕하세요, 아가씨. 영미 이름으로 방을 예약했어요.', 'Good morning, miss. I booked a room under the name Youngmi.'),
    ('mina', '네, 이층 사호실이에요! 기차 여행은 어떠셨어요?', 'Yes, Room 4 on the second floor! How was your train trip?'),
    ('youngmi', '조용하고 좋았어요, 고마워요. 그런데 오늘 이 가방이 아주 무겁네요.', 'It was quiet and pleasant, thank you. Though today this bag feels very heavy.'),
    ('junho', '제가 들어 드릴게요. 세상에, 안에 돌을 넣으셨어요?', 'Let me carry it for you. Goodness, did you pack stones inside?'),
    ('youngmi', '원피스하고 악보하고 제가 좋아하는 찻잔만 넣었어요!', 'I only packed dresses, sheet music, and my favourite teacup!'),
    ('mina', '여기 사호실 열쇠예요. 아침 식사는 일곱 시 반부터 열 시까지예요.', "Here is the Room 4 key. Breakfast is from seven thirty to ten o'clock."),
    ('youngmi', '좋네요. 창문은 길 쪽이에요, 안마당 쪽이에요?', 'Lovely. Is the window facing the street side or the courtyard side?'),
    ('mina', '오래된 나무 바로 위, 안마당 쪽이에요. 아주 조용해요.', 'It faces the courtyard, right above the old tree. It is very quiet.'),
    ('youngmi', '딱 좋네요. 계단은 어디에 있어요?', 'Just right. Where are the stairs?'),
    ('junho', '이 아치문 바로 뒤예요. 파란 가방은 제가 위로 옮겨 드릴게요.', 'Right behind this archway. I will carry the blue bag upstairs for you.'),
    ('youngmi', '두 분 다 정말 고마워요.', 'Thank you both very much.'),
]
WALK = [
    (0, None, ["'Welcome! Good morning, ma'am.' Step into any café, shop, or guesthouse in Seoul and you will immediately hear ", (None, '어서 오세요'), ", literally 'please come in quickly'."]),
    (1, None, ["'Good morning, miss. I booked a room under the name Youngmi.' Booking a room or table uses ", (None, '예약했어요'), ", combining 'reservation' with 'did'."]),
    (2, None, ["'Yes, Room 4 on the second floor! How was your train trip?' Floors stack Korean numbers onto 'floor', making ", (None, '이층'), ' the second floor.']),
    (3, None, ["'It was quiet and pleasant, thank you. Though today this bag feels very heavy.' Conversations pivot smoothly with ", (None, '그런데'), ", meaning 'by the way' or 'though'."]),
    (4, None, ["'Let me carry it for you. Goodness, did you pack stones inside?' Offering humble help sounds extra gracious when Junho says ", (None, '들어 드릴게요'), ", literally 'I will lift and give to you'."]),
    (6, None, ["'Here is the Room 4 key. Breakfast is from seven thirty to ten o'clock.' Time spans pair ", (None, '일곱 시 반부터'), " ('from seven-thirty') with ", (None, '열 시까지예요'), " ('until ten')."]),
    (8, None, ["'It faces the courtyard, right above the old tree. It is very quiet.' Look at ", (None, '안마당'), ", built from 'inside' and 'yard' for an enclosed courtyard."]),
    (11, None, ["'Thank you both very much.' Instead of counting guests or staff with plain 'people', Korean uses the respectful counter in ", (None, '두 분'), " for 'two esteemed people'."]),
]
