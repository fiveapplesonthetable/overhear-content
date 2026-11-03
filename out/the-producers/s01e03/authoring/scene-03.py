"""Scene 03: A Chicken Instead of a Pheasant."""
ID = 'the-producers-s01e03-scene-03'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 3
SCENE = 3
TITLE = "꿩 대신 닭  (A Chicken Instead of a Pheasant)"
LEVEL = "A1 — beginner"
LABELS = {"camera_pd": "촬영자", "seungchan": "백승찬"}
SOURCE_NAME = "프로듀사 (The Producers) S1.03"
SOURCE_FILE = "sources/the-producers/s01/e03.ko.srt"

INTRO = 'Arriving at KBS the next morning, Baek Seung-chan sheepishly asks the Documentary cameraman to cut out his personal remarks from yesterday. On the way inside, he explains a classic Korean proverb about settling for a chicken when you cannot catch a pheasant.'

STORY = [
    ('seungchan', '제가 쓸데없는 얘기를 너무 많이 한 것 같아서요.', 'I feel like I said far too many unnecessary things.', [(88, '쓸데없는 얘기를 너무 많이 한 것 같아서')], ''),
    ('seungchan', '편집 좀 부탁드립니다.', 'Please edit that part out for me.', [(90, '편집 좀')], ''),
    ('camera_pd', '방송이 장난이니?', 'Do you think broadcasting is a joke?', [(94, '방송이 장난이니?')], ''),
    ('seungchan', '아니요.', 'No, sir.', [(95, '아니요')], ''),
    ('camera_pd', '오늘은 무슨 일을 하게 될지 아세요?', 'Do you know what work you will be doing today?', [(99, '오늘은 무슨 일을 하게 될지 아세요?')], ''),
    ('seungchan', '새 시즌을 위해서 새로운 멤버를 섭외하는 일이라고 들었습니다.', 'I heard our job is casting new members for the new season.', [(103, '새 시즌을 위해서'), (106, '새로운 멤버를 섭외하는 일이라고 들었습니다')], ''),
    ('seungchan', '촬영도 일주일밖에 안 남아서 누가 잘 안 하려고 할 거라고요.', 'With only a week left before filming, they said hardly anyone will want to do it.', [(109, '촬영도 일주일밖에 안 남'), (110, '누가 잘 안 하려고 할 거라고')], ''),
    ('camera_pd', '그럼 어떡해요?', 'Then what do you do?', [(111, '그럼 어떡해요?')], ''),
    ('seungchan', '이런 상황에서는 닭을 잡아야 한다고 합니다.', 'They say in a situation like this, we have to catch a chicken instead.', [(112, '이런 상황에서는'), (114, '닭을 잡아야 한다고')], ''),
    ('camera_pd', '꿩 대신 닭이요?', 'A chicken instead of a pheasant?', [(115, '대신 닭')], ''),
    ('seungchan', '예, 저는 그럼 닭 잡으러 가보겠습니다.', 'Yes, then I will head in to catch a chicken now.', [(116, '예'), (117, '저는 그럼'), (118, '닭 잡으러 가보겠습니다')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'I feel like I said far too many unnecessary things.'"),
    (1, None, "'Please edit that part out for me.'"),
    (2, None, "'Do you think broadcasting is a joke?'"),
    (3, None, "'No, sir.'"),
    (4, None, "'Do you know what work you will be doing today?'"),
    (5, None, "'I heard our job is casting new members for the new season.'"),
    (6, None, "'With only a week left before filming, they said hardly anyone will want to do it.'"),
    (7, None, "'Then what do you do?'"),
    (8, None, "'They say in a situation like this, we have to catch a chicken instead.'"),
    (9, None, "'A chicken instead of a pheasant?'"),
    (10, None, "'Yes, then I will head in to catch a chicken now.'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Now you know the classic Korean expression about choosing a chicken instead of a pheasant when you need a practical backup plan. See you next time.'
CLOSING = ('camera_pd', '다음에 또 만나요!')
