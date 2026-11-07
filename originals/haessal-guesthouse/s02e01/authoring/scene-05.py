# Authoring module for haessal-guesthouse-s02e01-scene-05.
ID = 'haessal-guesthouse-s02e01-scene-05'
SHOW = 'haessal-guesthouse'
SEASON = 2
EPISODE = 1
SCENE = 5
TITLE = '온실을 재요  (Measuring the Sunroom)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'jihoon': '지훈', 'minsu': '민수', 'mina': '미나'}
INTRO = 'Ten minutes later, Jihoon hurries downstairs with his leather notebook alongside his older brother Minsu, who walked over early from his flat in Seoul after their Friday reunion. Mina meets them at the sunroom door. Listen first.'
OPENER = "Let's measure the sunroom with the brothers, one line at a time."
TRANSITION = "Now let's listen to the whole measuring scene again."
OUTRO = 'Jihoon approves the sound of the room, and Minsu volunteers a pair of strong hands for the weekend. See you next time.'
CLOSING = ('jihoon', '안녕히 계세요!')
STORY = [
    ('jihoon', '미나 씨, 소라 씨한테 들었어요. 숨은 아홉 번째 방을 여셨어요?', 'Mina, we heard from Sora. Did you open a hidden ninth room?'),
    ('minsu', '제 동생이 토스트도 다 안 먹고 줄자를 들고 왔어요.', 'My little brother grabbed his tape measure before he even finished his toast.'),
    ('mina', '두 분 다 들어오세요! 이 방이 안전한지 알려 주세요.', 'Come in, both of you! Tell us if this room is safe.'),
    ('jihoon', '폭 사 미터, 길이 육 미터. 왼쪽은 벽돌 벽, 위는 나무 천장이에요.', 'Four metres wide, six metres long. Brick wall on the left, wooden ceiling above.'),
    ('minsu', '손뼉을 한 번 쳐 보세요. 길 소리가 얼마나 조용한지 들려요?', 'Clap your hands once. Can you hear how quiet the street sounds?'),
    ('jihoon', '메아리가 하나도 없어요! 나무 천장 덕분에 음악도 대화도 부드러워요.', 'No echo at all! Thanks to the wooden ceiling, music and talk both sound soft.'),
    ('mina', '그럼 소라 언니 카페하고 영미 선생님 피아노가 위층 손님들을 안 깨워요?', "So Sora's café and Miss Youngmi's piano will not wake the guests upstairs?"),
    ('jihoon', '전혀요. 두꺼운 벽돌 벽이 계단 쪽 소리를 다 막아요.', 'Not at all. The thick brick wall blocks every sound from the stairs.'),
    ('minsu', '저는 이번 주말에 시청 일이 없어요, 미나 씨. 저희 둘 다 일 시켜 주세요!', 'I have no City Hall work this weekend, Mina. Put us both to work!'),
    ('mina', '점심 먹고 지하실 테이블을 같이 옮겨 주실 수 있어요?', 'After lunch, could you help carry the cellar tables in?'),
    ('minsu', '그럼요. 사무실 책상보다 지훈이 옆에서 일하는 게 훨씬 좋아요.', 'Of course. Working next to Jihoon is much better than sitting at an office desk.'),
    ('jihoon', '먼저 창문 걸쇠를 그려 볼게요. 안마당 바람이 들어오게요.', 'First let me sketch the window latches, so the courtyard air can come in.'),
]
WALK = [
    (0, None, ["'Mina, we heard from Sora. Did you open a hidden ninth room?' Hearing news from someone puts the little word ", (None, '한테'), " after the person, like 'from' in English."]),
    (1, None, ["'My little brother grabbed his tape measure before he even finished his toast.' A tape measure is ", (None, '줄자를'), ", built from 'string' and 'ruler'."]),
    (3, None, ["'Four metres wide, six metres long. Brick wall on the left, wooden ceiling above.' Metres take the second, borrowed set of numbers, so four metres is ", (None, '사 미터'), '.']),
    (4, None, ["'Clap your hands once. Can you hear how quiet the street sounds?' Clapping in Korean is 'hitting your palms': ", (None, '손뼉을 한 번 쳐'), '.']),
    (5, None, ["'No echo at all! Thanks to the wooden ceiling, music and talk both sound soft.' Give credit for a good result with ", (None, '덕분에'), ", 'thanks to'."]),
    (7, None, ["'Not at all. The thick brick wall blocks every sound from the stairs.' A one-word answer meaning 'not at all' is ", (None, '전혀요'), ', made polite by the final sound.']),
    (8, None, ["'I have no City Hall work this weekend, Mina. Put us both to work!' The chunk ", (None, '일 시켜 주세요'), " literally means 'please make us do work'."]),
    (10, None, ["'Of course. Working next to Jihoon is much better than sitting at an office desk.' In family talk an extra sound goes after a name ending in a consonant, so Minsu says ", (None, '지훈이'), '.']),
    (10, None, ["'Of course. Working next to Jihoon is much better than sitting at an office desk.' Put ", (None, '훨씬'), " before 'good' and it becomes 'much better'."]),
]
