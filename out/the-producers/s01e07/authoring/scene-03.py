"""Scene 03: I Am Dropping the Honorific Suffix From Now On."""
ID = 'the-producers-s01e07-scene-03'
PAIR = "ko-en"
SHOW = 'the-producers'
SEASON = 1
EPISODE = 7
SCENE = 3
TITLE = '앞으로 님 자 뺄 겁니다  (I Am Dropping the Honorific Suffix From Now On)'
LEVEL = "A1 — beginner"
LABELS = {"seungchan": "백승찬", "yejin": "탁예진"}
SOURCE_NAME = '프로듀사 (The Producers) S1.07'
SOURCE_FILE = 'sources/the-producers/s01/e07.ko.srt'

INTRO = 'At the playground, Tak Ye-jin suddenly notices that Baek Seung-chan just called her Senior without the extra honorific suffix. Seung-chan stands his ground and announces a permanent change in how he addresses her.'

STORY = [
    ('yejin', '응, 근데 너 왜 갑자기 선배라고 해? 님 자 어디 갔어?', 'Yeah, wait—why are you suddenly calling me plain Senior? Where did the honorific suffix go?', [(23, '근데 너 왜 갑자기 선배라고 해'), (24, '님자 어디 갔어')], ''),
    ('yejin', '뭐야, 왜 대답을 못 해? 갑자기 왜 선배님이 선배가 됐지?', 'What is it, why can you not answer? How did honored Senior suddenly turn into plain Senior?', [(27, '뭐야 왜 대답을 못해'), (28, '갑자기 왜 선배님이 선배가 됐지')], ''),
    ('seungchan', '제 동기 창식이도 선배라고 하고요.', 'My rookie classmate Chang-sik calls you plain Senior too.', [(29, '제 동기 창식이도 선배라고 하고')], ''),
    ('seungchan', '저랑 한 살밖에 차이 안 나는 이승기 씨도 누나라고 잘만 하던데.', 'Even Lee Seung-gi, who is only one year apart from me, calls you older sister just fine.', [(30, '저랑 한 살밖에 차이 안 나는 이승기씨도 누나라고 잘만 하던데')], ''),
    ('seungchan', '말도 막 반말 존댓말 섞어서 하고.', 'He even mixes casual speech and polite speech freely when talking to you.', [(31, '말도 막 반말 존댓말 섞어서 하고')], ''),
    ('yejin', '그래서 너도 말을 짧게 하겠다?', 'So you are saying you plan to shorten your speech with me too?', [(32, '그래서 너도 말을 짧게 하겠다')], ''),
    ('seungchan', '네, 저도 선배라고 할 겁니다.', 'Yes, I am going to call you plain Senior too.', [(33, '네, 저도 선배라고 할 겁니다')], ''),
    ('seungchan', '님 자 뺄 겁니다, 앞으로 쭉.', 'I am going to drop the honorific suffix—from now on, all the way.', [(34, '님 짤 뺄 겁니다'), (35, '앞으로 쭉')], ''),
    ('yejin', '그래라, 그럼.', 'Go right ahead, then.', [(36, '그래라, 그럼')], ''),
    ('seungchan', '네, 선배!', 'Yes, Senior!', [(37, '네, 선배')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Yeah, wait—why are you suddenly calling me plain Senior? Where did the honorific suffix go?'"),
    (1, None, "'What is it, why can you not answer? How did honored Senior suddenly turn into plain Senior?'"),
    (2, None, "'My rookie classmate Chang-sik calls you plain Senior too.'"),
    (3, None, "'Even Lee Seung-gi, who is only one year apart from me, calls you older sister just fine.'"),
    (4, None, "'He even mixes casual speech and polite speech freely when talking to you.'"),
    (5, None, "'So you are saying you plan to shorten your speech with me too?'"),
    (6, None, "'Yes, I am going to call you plain Senior too.'"),
    (7, None, "'I am going to drop the honorific suffix—from now on, all the way.'"),
    (8, None, "'Go right ahead, then.'"),
    (9, None, "'Yes, Senior!'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Dropping an extra honorific suffix in Korean marks a big step closer between a junior and a senior. Until next time!'
CLOSING = ('yejin', '다음에 봐요!')
