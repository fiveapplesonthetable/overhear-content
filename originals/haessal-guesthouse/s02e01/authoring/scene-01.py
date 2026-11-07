# Authoring module for haessal-guesthouse-s02e01-scene-01.
ID = 'haessal-guesthouse-s02e01-scene-01'
SHOW = 'haessal-guesthouse'
SEASON = 2
EPISODE = 1
SCENE = 1
TITLE = '아홉 번째 열쇠  (The Ninth Key)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'mina': '미나', 'junho': '준호', 'sungmin': '성민'}
INTRO = "It is early Saturday morning at Sunshine House in Seoul, just hours after Junho carried a dusty cedar box stamped 'Room 9' up from the cellar. Mina and Sungmin lean over the front desk as Junho turns the tiny brass key. Listen to the scene first."
OPENER = "Season 2 starts right where we left off, so let's open the box one line at a time."
TRANSITION = "Now let's listen to the whole box-opening scene again."
OUTRO = "Inside the cedar box sits a heavy door key and a floor plan pointing straight behind the hallway bookcase. Don't worry if a word or two went past quickly; they return right away. See you next time."
CLOSING = ('mina', '또 만나요!')
STORY = [
    ('sungmin', '준호 씨, 작은 열쇠를 천천히 돌리세요. 가슴이 두근두근해요!', 'Junho, turn the little key slowly. My heart is pounding!'),
    ('junho', '진정하세요, 사장님. 지하실 황동 자물쇠는 절대 안 부러져요.', 'Relax, boss. A brass lock from the cellar never breaks.'),
    ('mina', '딸깍 소리가 났어요! 나무 뚜껑을 올려 보세요, 준호 씨!', 'It clicked! Lift the wooden lid, Junho!'),
    ('junho', '안에는... 큰 문 열쇠 하나, 파란 도면, 그리고 엽서들이 있어요.', 'Inside there is... one big door key, a blue floor plan, and postcards.'),
    ('sungmin', '접힌 파란 종이 위쪽을 읽어 보세요! 제 안경이 어디 있지요?', 'Read the top of the folded blue paper! Where are my glasses?'),
    ('mina', '아직 이마 위에 있어요, 사장님. 어젯밤하고 똑같아요.', 'Still on your forehead, boss. Same as last night.'),
    ('sungmin', "아하! 여기 보세요. '일층, 구호실, 정원 온실'!", "Aha! Look here: 'Ground floor, Room Nine, garden sunroom'!"),
    ('mina', '잠깐만요, 일층에 정원 온실이 있어요?!', 'Wait, we have a garden sunroom on the ground floor?!'),
    ('junho', '이 화살표를 보세요. 뒤쪽 복도 책장 뒤를 가리켜요.', 'Look at this arrow. It points behind the bookcase in the back hallway.'),
    ('sungmin', '그 무거운 나무 책장은 이십 년 동안 그 벽 앞에 있었어요!', 'That heavy wooden bookcase has stood against that wall for twenty years!'),
    ('mina', '그럼 그 오래된 책들 뒤에 아홉 번째 문이 있어요!', 'Then behind those old books there is a ninth door!'),
    ('junho', '먼저 커피 한 모금 마셔요. 그다음에 책을 옮겨요.', 'Have one sip of coffee first. Then we move the books.'),
]
WALK = [
    (0, None, ["'Junho, turn the little key slowly. My heart is pounding!' Korean loves sound-picture words, and ", (None, '두근두근해요'), ' is the thump-thump of an excited heart turned into a verb.']),
    (1, None, ["'Relax, boss. A brass lock from the cellar never breaks.' Korean builds 'never' from 'absolutely' plus 'not': ", (None, '절대 안 부러져요'), '.']),
    (2, None, ["'It clicked! Lift the wooden lid, Junho!' The little word ", (None, '딸깍'), ' is the click of a lock, and Mina says the click sound came out.']),
    (3, None, ["'Inside there is... one big door key, a blue floor plan, and postcards.' Korean counts after the thing, so 'one key' is literally 'key one': ", (None, '열쇠 하나'), '.']),
    (4, None, ["'Read the top of the folded blue paper! Where are my glasses?' Sungmin half asks himself, and the soft ending in ", (None, '어디 있지요'), " sounds like 'now where are they?'"]),
    (6, None, ["'Aha! Look here: Ground floor, Room Nine, garden sunroom!' The word for a sunroom or greenhouse, ", (None, '온실'), ", is built from 'warm' and 'room'."]),
    (8, None, ["'Look at this arrow. It points behind the bookcase in the back hallway.' Pointing at something with a finger or an arrow is ", (None, '가리켜요'), '.']),
    (9, None, ["'That heavy wooden bookcase has stood against that wall for twenty years!' Put ", (None, '동안'), " after a stretch of time and it means 'for' or 'during'."]),
    (11, None, ["'Have one sip of coffee first. Then we move the books.' A single mouthful of a drink is ", (None, '한 모금'), ', a handy counter for sips.']),
]
