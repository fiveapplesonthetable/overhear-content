"""Scene 05: Please Edit Out That Phone Call."""
ID = 'the-producers-s01e05-scene-05'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 5
SCENE = 5
TITLE = '전화 통화한 거 편집해 주세요  (Please Edit Out That Phone Call)'
LEVEL = "A1 — beginner"
LABELS = {"cindy": "신디", "seungchan": "백승찬"}
SOURCE_NAME = "프로듀사 (The Producers) S1.05"
SOURCE_FILE = 'sources/the-producers/s01/e05.ko.srt'

INTRO = "Before leaving Cindy's tent for the night, Baek Seung-chan kindly offers her soothing music, his own bedtime book, and an emergency cap for morning hair. Touched yet embarrassed, Cindy asks him to edit out her awkward phone call."

STORY = [
    ('seungchan', '거치 카메라 두 대만 놓고 나갈게요.', 'I will just set down two fixed cameras and head out.', [(96, '거치 카메라 두 대만 놓고 나갈게요')], ''),
    ('seungchan', '저도 밖에서는 잠을 잘 못 자서요, 이것저것 준비했거든요.', 'Since I cannot sleep well outdoors either, I prepared a few things.', [(99, '저도 밖에서는 잠을 잘 못 자서요'), (100, '준비했거든요')], ''),
    ('seungchan', '음악이라도 들으시면 잠이 잘 오실 거예요.', 'If you listen to at least some music, you should fall asleep more easily.', [(102, '음악이라도 들으시면 잠이 잘 오실 거예요')], ''),
    ('seungchan', '그리고 이거 읽어보세요, 제가 자기 전에 꼭 읽는 책인데.', 'And try reading this—it is a book I always read right before bed.', [(103, '그리고 이거 읽어보세요'), (104, '제가 자기 전에 꼭 읽는 책인데')], ''),
    ('cindy', '나보고 지금 여기서 책을 읽으라고요?', 'Are you telling me to read a book right here right now?', [(105, '나보고 지금 여기서 책을 읽으라고요')], ''),
    ('seungchan', '잠이 잘 옵니다, 그리고 이거는 내일 아침에 머리 떡지면 쓰세요.', 'It puts you right to sleep, and wear this cap tomorrow morning if your hair gets greasy.', [(106, '잠이 잘 옵니다'), (107, '그리고 이거는 내일 아침에 머리 떡지면 쓰세요')], ''),
    ('cindy', '아까 전화 통화한 거, 그거 편집해 주세요.', 'That phone call from earlier—please edit that out.', [(113, '아까'), (114, '전화 통화한 거 그거 편집해 주세요')], ''),
    ('seungchan', '편집은 큰 사안이라서 제 소관은 아닙니다만.', 'Editing is a major matter, so it is not really within my authority, though.', [(116, '편집은'), (117, '제 소관은 아닙니다만')], ''),
    ('cindy', '나 왕따 아니에요, 친구도 없는 거 아니야, 있어요!', 'I am not an outcast—it is not like I have no friends, I do have them!', [(118, '나 왕따 아니에요'), (119, '친구도 없는 거 아니야, 있어요')], ''),
    ('cindy', '다들 너무 바빠서 그렇지, 방송 나가면 사람들이 나 왕따라고 오해할 거 아니에요.', 'Everyone is just too busy, and if this airs, people are going to misunderstand and think I am an outcast.', [(120, '다들 너무'), (121, '방송 나가면 사람들이 나 왕따라고 오해할 거 아니에요')], ''),
    ('cindy', '편집해 주세요.', 'Please edit it out.', [(123, '편집해 주세요')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'I will just set down two fixed cameras and head out.'"),
    (1, None, "'Since I cannot sleep well outdoors either, I prepared a few things.'"),
    (2, None, "'If you listen to at least some music, you should fall asleep more easily.'"),
    (3, None, "'And try reading this—it is a book I always read right before bed.'"),
    (4, None, "'Are you telling me to read a book right here right now?'"),
    (5, None, "'It puts you right to sleep, and wear this cap tomorrow morning if your hair gets greasy.'"),
    (6, None, "'That phone call from earlier—please edit that out.'"),
    (7, None, "'Editing is a major matter, so it is not really within my authority, though.'"),
    (8, None, "'I am not an outcast—it is not like I have no friends, I do have them!'"),
    (9, None, "'Everyone is just too busy, and if this airs, people are going to misunderstand and think I am an outcast.'"),
    (10, None, "'Please edit it out.'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Offering thoughtful items for sleeping outdoors and asking someone not to misunderstand a delicate moment gives you warm, natural Korean polite speech. Until next time!'
CLOSING = ('cindy', '안녕히 가세요!')
