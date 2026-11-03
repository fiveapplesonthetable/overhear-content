"""Scene 27: I Am the Lowest Junior."""
ID = 'the-producers-s01e03-scene-27'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 3
SCENE = 27
TITLE = "제가 제일 아랫사람인데요  (I Am the Lowest Junior)"
LEVEL = "A1 — beginner"
LABELS = {"baek_dad": "백보선", "cindy": "신디", "seungchan": "백승찬"}
SOURCE_NAME = "프로듀사 (The Producers) S1.03"
SOURCE_FILE = "sources/the-producers/s01/e03.ko.srt"

INTRO = 'At a street snack stall, Bo-sun proudly brags to a neighbor that his Seoul National graduate son leads huge television crews at KBS—right as Baek Seung-chan walks up to buy ten pancakes. Moments later, Seung-chan phones Cindy about the overdue umbrella and heads straight to her rehearsal.'

STORY = [
    ('baek_dad', '우리 아들이 서울대를 졸업하고 이번에 KBS에 들어갔거든요.', 'My son graduated from Seoul National University and just joined KBS.', [(902, '우리 아들이 서울대를 졸업하고 이번에 KBS에 들어갔거든요')], ''),
    ('seungchan', '녹차 호떡 다섯 개, 그냥 호떡 다섯 개 주세요.', 'Please give me five green-tea pancakes and five plain pancakes.', [(905, '녹차 호떡 다섯 개 그냥 호떡 다섯 개')], ''),
    ('baek_dad', '승찬아, 네가 왜 여기 있는 거야?', 'Seung-chan, why are you standing out here?', [(908, '네가 여기 있는 거야?')], ''),
    ('baek_dad', '아랫사람 시켜도 되는데 굳이 네가 직접 사러 왔구나!', 'You could have sent a subordinate, yet you came out to buy them yourself—how admirable!', [(910, '시켜도 되는데 굳이 네가 직접')], ''),
    ('seungchan', '제가 제일 아랫사람인데요.', 'I am the very lowest junior on the team.', [(911, '제가 제일 아랫사람인데요')], ''),
    ('cindy', '반납하라고 전화하신 거예요?', 'Did you call to tell me to return the umbrella?', [(915, '반납하라고 전화하신 거예요?')], ''),
    ('seungchan', '오늘치 연체료는 제 월급에서 빠져나가겠네요.', "It looks like today's late fee will come out of my salary.", [(918, '오늘치 연체료는 제 월급에서 빠져나가겠네요')], ''),
    ('cindy', '그래요, 우산도 드리고 연체료도 드릴게요.', 'Fine, I will give you back the umbrella and pay you the late fee too.', [(921, '그래요'), (921, '연체료도 드릴게요')], ''),
    ('seungchan', '그거 지금 주시면 안 되겠습니까?', 'Could you possibly hand it over right now?', [(922, '그거 지금 주시면 안 되겠습니까?')], ''),
    ('cindy', '안 돼요. 지금 무대 리허설 중이에요.', 'No way. I am in the middle of stage rehearsals right now.', [(924, '안 돼요'), (924, '무대 리허설 중이에요')], ''),
    ('seungchan', '네, 금방 가겠습니다!', 'Great, I will be right over!', [(930, '네'), (931, '금방 가겠습니다')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'My son graduated from Seoul National University and just joined KBS.'"),
    (1, None, "'Please give me five green-tea pancakes and five plain pancakes.'"),
    (2, None, "'Seung-chan, why are you standing out here?'"),
    (3, None, "'You could have sent a subordinate, yet you came out to buy them yourself—how admirable!'"),
    (4, None, "'I am the very lowest junior on the team.'"),
    (5, None, "'Did you call to tell me to return the umbrella?'"),
    (6, None, "'It looks like today's late fee will come out of my salary.'"),
    (7, None, "'Fine, I will give you back the umbrella and pay you the late fee too.'"),
    (8, None, "'Could you possibly hand it over right now?'"),
    (9, None, "'No way. I am in the middle of stage rehearsals right now.'"),
    (10, None, "'Great, I will be right over!'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Saying you are in the middle of a rehearsal and promising to head right over are everyday Korean phrases you will hear everywhere. See you next time.'
CLOSING = ('baek_dad', '안녕히 가세요!')
