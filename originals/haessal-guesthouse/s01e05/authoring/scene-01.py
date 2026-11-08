# Authoring module for haessal-guesthouse-s01e05-scene-01.
ID = 'haessal-guesthouse-s01e05-scene-01'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = '안마당에서의 진실  (Truth in the Courtyard)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'jihoon': '지훈', 'mina': '미나', 'youngmi': '영미'}
INTRO = "Out under the courtyard tree at Sunshine House in Seoul, Jihoon sits down with Mina and Youngmi to explain Monday night's mystery from the very beginning. Listen first."
OPENER = "Let's untangle Monday night's mix-up one line at a time."
TRANSITION = "Now let's listen to the whole courtyard story again."
OUTRO = 'All the puzzle pieces from Monday and Tuesday finally click together! Next time, Jihoon explains why he has not spoken to his brother Minsu in three years.'
CLOSING = ('mina', '또 만나요!')
STORY = [
    ('youngmi', '얼굴 좀 제대로 보자, 지훈아! 피아노보다 훨씬 더 크게 자랐구나!', 'Let me look at your face properly, Jihoon! You grew much taller than the piano!'),
    ('jihoon', '영미 선생님이 똑같은 게스트하우스에 묵고 계실 줄은 꿈에도 몰랐어요.', 'I never dreamed in a million years that you were staying at the exact same guesthouse, Miss Youngmi.'),
    ('mina', '잠깐만요, 그럼 월요일에 같은 기차를 타셨고 선생님이 그 손님 가방을 가져가셨어요?', "Wait—so you rode the same train on Monday and took Miss Youngmi's bag?"),
    ('jihoon', '완전히 실수였어요! 사촌 집에서 가방을 열었더니 악보하고 빨간 리본이 나왔어요.', "It was a total mistake! When I opened the bag at my cousin's home, sheet music and a red ribbon came out."),
    ('youngmi', '왜 밤에 현관 계단에 제 가방만 두고 도망갔어요?', 'Why did you leave only my bag on the front step at night and run away?'),
    ('jihoon', '월요일 저녁에 여기 걸어오다가 우리 형이 이 길을 걸어가는 걸 봤거든요!', 'Because while walking here on Monday evening, I saw my older brother walking down this street!'),
    ('mina', '형님이 여기 서울에 사세요?', 'Does your older brother live here in Seoul?'),
    ('jihoon', '네. 너무 당황해서 벨만 누르고 금요일 쪽지를 손잡이에 끼워 놨어요.', 'Yes. I panicked so badly that I only rang the bell and slipped the Friday note onto the handle.'),
    ('youngmi', '잠깐만요, 그런데 수요일 밤에는 본명으로 여기에 체크인했어요?', 'Wait—and on Wednesday night you checked in here under your real name?'),
    ('jihoon', '금요일 전에 근처 조용한 숙소가 필요했는데, 제 가방을 달라고 하기 너무 민망했어요!', 'Before Friday I needed quiet lodging nearby, and honestly felt too shy to ask for my bag!'),
    ('mina', '화요일에 하얀 꾸러미 때문에 저희한테 전화까지 하셨으면서요!', 'Even after you called us on Tuesday about the white parcel!'),
    ('jihoon', '그 하얀 종이 안에 든 건 제 것이 아니라 우리 형 민수 거예요.', 'What is inside that white paper belongs to my older brother Minsu, not to me.'),
]
WALK = [
    (0, None, ["'Let me look at your face properly, Jihoon! You grew much taller than the piano!' Affectionate elders add the warm exclamation ending on ", (None, '자랐구나'), ", 'look how you have grown!'."]),
    (1, None, ["'I never dreamed in a million years that you were staying at the exact same guesthouse, Miss Youngmi.' Total surprise uses the vivid Korean idiom ", (None, '꿈에도 몰랐어요'), ", literally 'even in a dream I did not know'."]),
    (3, None, ["'It was a total mistake! When I opened the bag at my cousin's home, sheet music and a red ribbon came out.' In Korean, cousins are ", (None, '사촌'), ", literally 'four degrees of family kinship'."]),
    (6, None, ["'Does your older brother live here in Seoul?' Notice Mina upgrades 'older brother' respectfully to ", (None, '형님이'), " when asking about a guest's family."]),
    (7, None, ["'Yes. I panicked so badly that I only rang the bell and slipped the Friday note onto the handle.' Feeling flustered on the spot is ", (None, '당황해서'), ", 'because I panicked'."]),
    (9, None, ["'Before Friday I needed quiet lodging nearby, and honestly felt too shy to ask for my bag!' Feeling embarrassed or shy uses ", (None, '민망했어요'), ", 'I felt too shy'."]),
    (10, None, ["'Even after you called us on Tuesday about the white parcel!' Expressing 'even after you did' uses ", (None, '하셨으면서요'), ", blending politeness with a slight reproach."]),
]
