# Authoring module for haessal-guesthouse-s02e01-scene-08.
ID = 'haessal-guesthouse-s02e01-scene-08'
SHOW = 'haessal-guesthouse'
SEASON = 2
EPISODE = 1
SCENE = 8
TITLE = '그 스위치 만지지 마세요  (Don\'t Touch That Switch)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'junho': '준호', 'sungmin': '성민', 'mina': '미나'}
INTRO = 'Back at the doorway of Room 9, Junho opens his leather tool bag to inspect the old brass wall switch, but an excited Sungmin reaches past him beside Mina. Listen first.'
OPENER = "Let's see what one impatient click can do, line by line."
TRANSITION = "Now let's listen to the whole switch scene again."
OUTRO = 'One impatient click from Sungmin pops the ground-floor fuse and proves Room 9 needs fresh wiring before Friday! Episode 1 of Season 2 is complete, so see you in Episode 2.'
CLOSING = ('junho', '다음에 만나요!')
STORY = [
    ('junho', '사장님, 그 황동 스위치 만지기 전에 잠깐만 기다리세요.', 'Boss, wait just a moment before you touch that brass switch.'),
    ('sungmin', '왜요? 이 유리 천장 전등 기억나요. 얼마나 예쁘게 빛나는지 보세요!', 'Why? I remember this glass ceiling lamp. Watch how prettily it glows!'),
    ('mina', '사장님, 잠깐만요! 준호 씨가 드라이버를 꺼냈어요!', 'Boss, wait! Junho has his screwdriver out!'),
    ('sungmin', '딱 한 번만 딸깍... 펑! ...아이고.', 'Just one quick click... pop! ...Oh dear.'),
    ('mina', '복도에서 난 큰 펑 소리는 뭐예요?!', 'What was that loud pop in the hallway?!'),
    ('junho', '오래된 전선 때문에 일층 퓨즈가 나갔어요.', 'The old wire blew the ground-floor fuse.'),
    ('sungmin', '로비 전등이 꺼졌어요! 제가 주방 오븐도 고장 냈어요?!', 'The lobby light went out! Did I break the kitchen oven too?!'),
    ('mina', '어머, 지금 어두운 주방에서 소라 언니가 부르는 소리가 들려요!', 'Oh no, I can hear Sora calling from the dark kitchen right now!'),
    ('junho', '삼십 년 된 낡은 전선이에요, 사장님. 제가 안을 보기 전에는 절대 스위치를 켜지 마세요.', 'It is worn-out thirty-year-old wire, boss. Never flip a switch before I look inside.'),
    ('sungmin', '점심 전에 고칠 수 있어요, 준호 씨? 여분 퓨즈가 있다고 말해 주세요!', 'Can you fix it before lunch, Junho? Please tell me you have spare fuses!'),
    ('junho', '주방은 이 분이면 돼요. 하지만 구호실은 새 구리 전선이 필요해요.', 'The kitchen takes two minutes. But Room Nine needs new copper wire.'),
    ('mina', '사장님, 손전등 꼭 잡으세요. 육 일 카운트다운이 진짜 시작됐어요!', 'Boss, hold the flashlight tight. Our six-day countdown has really started!'),
]
WALK = [
    (1, None, ["'Why? I remember this glass ceiling lamp. Watch how prettily it glows!' The chunk ", (None, '얼마나 예쁘게'), " means 'how prettily', perfect for showing off something lovely."]),
    (2, None, ["'Boss, wait! Junho has his screwdriver out!' Taking something out of a bag or pocket is ", (None, '꺼냈어요'), ", the past of 'take out'."]),
    (3, None, ["'Just one quick click... pop! ...Oh dear.' Sungmin's sigh ", (None, '아이고'), " is the classic Korean 'oh dear', heard from young and old."]),
    (5, None, ["'The old wire blew the ground-floor fuse.' In Korean a blown fuse simply 'went out': ", (None, '퓨즈가 나갔어요'), '.']),
    (6, None, ["'The lobby light went out! Did I break the kitchen oven too?!' A light that switches off by itself is ", (None, '꺼졌어요'), ', and breaking a machine is literally making a breakdown, ', (None, '고장 냈어요'), '.']),
    (7, None, ["'Oh no, I can hear Sora calling from the dark kitchen right now!' Sounds that reach your ears use ", (None, '들려요'), ", 'can be heard', rather than 'I hear'."]),
    (8, None, ["'It is worn-out thirty-year-old wire, boss. Never flip a switch before I look inside.' The polite 'don't' is a verb plus ", (None, '마세요'), ', so here: never switch it on.']),
    (9, None, ["'Can you fix it before lunch, Junho? Please tell me you have spare fuses!' A spare or extra one of something is ", (None, '여분'), '.']),
    (10, None, ["'The kitchen takes two minutes. But Room Nine needs new copper wire.' Say how long a job takes with 'if it's X, it's done': ", (None, '이 분이면 돼요'), '.']),
]
