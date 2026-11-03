"""Scene 25: My Nickname Is Drunken Liar."""
ID = 'the-producers-s01e05-scene-25'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 5
SCENE = 25
TITLE = '내 별명이 취중구라야  (My Nickname Is Drunken Liar)'
LEVEL = "A1 — beginner"
LABELS = {"seungchan": "백승찬", "yejin": "탁예진"}
SOURCE_NAME = "프로듀사 (The Producers) S1.05"
SOURCE_FILE = 'sources/the-producers/s01/e05.ko.srt'

INTRO = 'Summoning Baek Seung-chan to a quiet stairwell at KBS, Tak Ye-jin probes how much of her street-tent confession he overheard. She insists her drunken habit is making up lies, then panics as Seung-chan quotes her word for word.'

STORY = [
    ('yejin', '어젯밤에 뭐 들었니?', 'What did you overhear last night?', [(659, '어젯밤에 뭐'), (659, '들었니')], ''),
    ('seungchan', '아무것도.', 'Nothing at all.', [(660, '아무것도')], ''),
    ('yejin', '들었네, 아무것도라고 할 만한 그 무언가를 들었어!', 'You did hear it—you heard something big enough to make you answer "nothing at all"!', [(661, '들었네'), (662, '아무것도라고 할 만한 그 무언가를 들었어')], ''),
    ('yejin', '네가 어제 뭘 들었건 뭘 봤건 그건 사실이 아니야.', 'Whatever you heard or whatever you saw yesterday, none of it is true.', [(664, '네가 어제 뭘 들었건'), (665, '뭘 봤건'), (666, '그건 사실이 아니야')], ''),
    ('yejin', '거짓말하는 게 내 술버릇이거든, 내 별명이 취중구라야!', 'Telling lies is my drinking habit—my nickname is the Drunken Liar!', [(670, '거짓말하는 거'), (671, '내 별명이')], ''),
    ('yejin', '그래서 뭘 듣긴 들었니?', 'So what exactly did you hear?', [(676, '뭘 듣긴 들었니')], ''),
    ('seungchan', '어제 거짓말하신 거 좀 들은 것 같습니다.', 'I think I overheard a bit of the lies you told yesterday.', [(678, '어제 거짓말하신 거'), (679, '좀 들은 것 같습니다')], ''),
    ('seungchan', '잔인한 놈이라고, 왜 선을 보냐, 검사가 이쁘면 다냐!', 'Calling him a cruel jerk, asking why he went on a matchmaking date, and asking "so what if the prosecutor is pretty"!', [(683, '잔인한 놈이라고'), (684, '왜 선을 보냐'), (685, '검사가 이쁘면 다냐')], ''),
    ('seungchan', '그럴 거면 나한테 뽀뽀는 왜 했는데!', 'And "if you were going to do that, why did you kiss me"!', [(686, '그럴 거면 나한테 뽀뽀는 왜 했는데')], ''),
    ('yejin', '그만해 됐어, 어차피 다 거짓말인걸!', 'Stop, that is enough—it was all a lie anyway!', [(688, '그만해 됐어'), (690, '어차피 다 거짓말인걸')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'What did you overhear last night?'"),
    (1, None, "'Nothing at all.'"),
    (2, None, '\'You did hear it—you heard something big enough to make you answer "nothing at all"!\''),
    (3, None, "'Whatever you heard or whatever you saw yesterday, none of it is true.'"),
    (4, None, "'Telling lies is my drinking habit—my nickname is the Drunken Liar!'"),
    (5, None, "'So what exactly did you hear?'"),
    (6, None, "'I think I overheard a bit of the lies you told yesterday.'"),
    (7, None, '\'Calling him a cruel jerk, asking why he went on a matchmaking date, and asking "so what if the prosecutor is pretty"!\''),
    (8, None, '\'And "if you were going to do that, why did you kiss me"!\''),
    (9, None, "'Stop, that is enough—it was all a lie anyway!'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Claiming last night was all made-up nonsense and stopping someone from reciting an embarrassing quote gives you lively, comedic Korean dialogue. See you next time!'
CLOSING = ('seungchan', '안녕히 계세요!')
