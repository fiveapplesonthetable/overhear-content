# Authoring module for haessal-guesthouse-s01e01-scene-03.
ID = 'haessal-guesthouse-s01e01-scene-03'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = '내 안경 어디 있어요?  (Where Are My Glasses?)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'sungmin': '성민', 'mina': '미나', 'junho': '준호'}
INTRO = 'Before the first guest arrives, guesthouse owner Sungmin hurries in from the courtyard looking flustered. Mina and Junho watch as Sungmin pats his pockets in a panic. Listen to the whole scene first.'
OPENER = "Now let's take it slowly, one line at a time."
TRANSITION = "Now let's listen to the whole scene again from the top."
OUTRO = 'Sungmin found his glasses perched on his own forehead just as the taxi pulled up outside. Relax and let the rhythm of the words sink in; see you next time.'
CLOSING = ('sungmin', '또 만나요!')
STORY = [
    ('sungmin', '좋은 아침입니다, 여러분! 환영해요, 미나 씨. 준비 다 됐어요?', 'Good morning, everyone! Welcome, Mina. Is everything ready?'),
    ('mina', '안녕하세요, 사장님! 네, 책상도 깨끗하고 열쇠도 준비됐어요.', 'Hello, boss! Yes, the desk is clean and the keys are ready too.'),
    ('sungmin', '오늘 사호실 손님은 일주일 동안 계세요. 모든 게 완벽해야 해요!', "Today's Room 4 guest is staying for a week. Everything must be perfect!"),
    ('junho', '진정하세요, 사장님. 방도 깨끗하고 수건도 새것이에요.', 'Calm down, boss. The room is clean and the towels are fresh.'),
    ('sungmin', '예약 장부를 봐야 하는데 제 안경을 못 찾겠어요!', 'I need to read the reservation ledger, and I cannot find my glasses!'),
    ('mina', '코트 주머니 안에 없어요?', 'Are they not inside your coat pocket?'),
    ('sungmin', '없어요, 볼펜하고 오래된 영수증 세 장뿐이에요!', 'No, only a ballpoint pen and three old receipts!'),
    ('junho', '사장님, 책상 뒤에 있는 거울을 보세요.', 'Boss, look in the mirror behind the desk.'),
    ('sungmin', '거울에 왜 내 안경이... 어! 내 머리 위에 있네요!', 'Why would my glasses be in the mirror... oh! They are on my head!'),
    ('mina', '이마 위에 안전하게 잘 있어요.', 'They are right there on your forehead, safe and sound.'),
    ('sungmin', '아무한테도 말하지 마세요! 자, 종이 울리면 밝게 웃으세요.', 'Do not tell anyone! Now, smile brightly when the bell rings.'),
    ('junho', '지금 바로 대문 앞에 택시가 왔어요.', 'A taxi just pulled up right outside the front gate.'),
]
WALK = [
    (0, None, ["'Good morning, everyone! Welcome, Mina. Is everything ready?' Sungmin enters in crisp business style with ", (None, '좋은 아침입니다'), ", literally 'it is a good morning'."]),
    (1, None, ["'Hello, boss! Yes, the desk is clean and the keys are ready too.' Shop and guesthouse staff address the owner as ", (None, '사장님'), ", adding an honorific suffix to 'company president'."]),
    (2, None, ["'Today's Room 4 guest is staying for a week. Everything must be perfect!' Instead of the plain word for 'stay', Sungmin chooses ", (None, '계세요'), ' to show extra respect toward the guest.']),
    (4, None, ["'I need to read the reservation ledger, and I cannot find my glasses!' Putting ", (None, '못'), " right before 'find' shows he wants to find his ", (None, '안경을'), ' yet is unable to.']),
    (6, None, ["'No, only a ballpoint pen and three old receipts!' Flat thin sheets like paper, tickets, or receipts are counted with ", (None, '장뿐이에요'), ", where 'jang' counts sheets and 'ppun' means 'only'."]),
    (7, None, ["'Boss, look in the mirror behind the desk.' Location words sit after the reference object in Korean, so 'desk' comes before ", (None, '뒤에'), " for 'behind the desk'."]),
    (8, None, ["'Why would my glasses be in the mirror... oh! They are on my head!' Notice ", (None, '있네요'), ', whose ending expresses sudden discovery right before your eyes.']),
    (10, None, ["'Do not tell anyone! Now, smile brightly when the bell rings.' Polite 'do not' requests end with ", (None, '말하지 마세요'), ', a pattern you can attach to any action.']),
]
