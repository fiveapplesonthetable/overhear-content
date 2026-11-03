"""Scene 11: Could We Settle My Remaining Debt All at Once Tonight?."""
ID = 'the-producers-s01e11-scene-11'
PAIR = "ko-en"
SHOW = 'the-producers'
SEASON = 1
EPISODE = 11
SCENE = 11
TITLE = '남은 빚 청산 오늘 밤 한꺼번에 해주시면 안 되겠습니까?  (Could We Settle My Remaining Debt All at Once Tonight?)'
LEVEL = 'A1 — beginner'
LABELS = {"ilyong": "유일용", "seungchan": "백승찬", "yejin": "탁예진"}
SOURCE_NAME = '프로듀사 (The Producers) S1.11'
SOURCE_FILE = 'sources/the-producers/s01/e11.ko.srt'

INTRO = 'Dropping by the Music Bank office while Tak Ye-jin is checking stage sets, Baek Seung-chan leaves a thoughtful gift on her desk with Ryu Il-yong and texts to ask if they can settle his remaining tab all at once tonight. Torn over how to respond, Ye-jin sits down for blunt love-triangle advice over coffee.'

STORY = [
    ('ilyong', '여기 놓고 가세요. 선물 주러 오신 거 아니에요?', "You can leave it right here—didn't you come to drop off a gift?", [(747, '여기 놓고 가세요'), (750, '선물')], ''),
    ('seungchan', '아닌데요? 예진 선배 드리려고… 어디 가셨습니까?', 'Oh, well—it is for Senior Ye-jin. Where did she step out to?', [(751, '아닌데요?'), (753, '예진 선배 드리려고 어디 가셨습니까?')], ''),
    ('ilyong', '무대 세트 보러 가셨어요.', 'She went down to inspect the stage set.', [(754, '네 무대 세트 보러')], ''),
    ('seungchan', '예진 선배 오시면 꼭 말씀 좀 전해주십시오, 그거 예진 선배 거라고!', 'When Senior Ye-jin gets back, please be sure to tell her this is for her!', [(755, '예진 선배 오시면 꼭 말씀 좀 꼭 전해주십시오 그거 예진 선배 거라고')], ''),
    ('ilyong', '알겠다고요! 아무튼 백승찬 섬세해.', 'Got it! Man, Baek Seung-chan really thinks of everything.', [(755, '알겠다고요 아무튼 백승찬 섬세해')], ''),
    ('seungchan', '선배, 남은 빚 청산 오늘 밤 한꺼번에 해주시면 안 되겠습니까?', 'Senior, could we settle my remaining debt all at once tonight?', [(755, '선배 남은 빚 청산 오늘 밤 한꺼번에 해주시면 안 되겠습니까')], ''),
    ('yejin', '네가 그렇게 연애를 잘한다며? 나랑 커피 한잔할래?', 'I hear you are an expert at dating—want to grab a cup of coffee with me?', [(757, '네가 그렇게 연애를 잘한다며'), (760, '나랑 커피 한 잔 할래?')], ''),
    ('yejin', '내가 아니고 내 친구한테 이십 년 넘은 남자가 있는데…', 'Not me—my friend has this guy she has known for over twenty years…', [(762, '넘은 남자가 있는데'), (764, '내 친구한테 내가 아니고')], ''),
    ('yejin', '역시 명쾌하구나, 너!', 'You really cut straight to the point!', [(774, '역시 명쾌하구나 너')], ''),
    ('yejin', '그래, 두 번째는? 더 미안한 쪽을 버리라고?', 'Okay, and what is your second solution—let go of whichever one she feels sorrier toward?', [(778, '그래 두 번째는'), (779, '더 미안한 쪽을 버려요')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'You can leave it right here—didn\'t you come to drop off a gift?'"),
    (1, None, "'Oh, well—it is for Senior Ye-jin. Where did she step out to?'"),
    (2, None, "'She went down to inspect the stage set.'"),
    (3, None, "'When Senior Ye-jin gets back, please be sure to tell her this is for her!'"),
    (4, None, "'Got it! Man, Baek Seung-chan really thinks of everything.'"),
    (5, None, "'Senior, could we settle my remaining debt all at once tonight?'"),
    (6, None, "'I hear you are an expert at dating—want to grab a cup of coffee with me?'"),
    (7, None, "'Not me—my friend has this guy she has known for over twenty years…'"),
    (8, None, "'You really cut straight to the point!'"),
    (9, None, "'Okay, and what is your second solution—let go of whichever one she feels sorrier toward?'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = "Leaving a thoughtful gift and weighing how to answer an earnest suitor set up Ye-jin and Seung-chan's evening meeting. Until next time!"
CLOSING = ('yejin', '다음에 봐요.')
