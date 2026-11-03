"""Scene 03: Rent It Out? That Is Not What Matters Right Now!."""
ID = 'the-producers-s01e10-scene-03'
PAIR = "ko-en"
SHOW = 'the-producers'
SEASON = 1
EPISODE = 10
SCENE = 3
TITLE = '전세를 놓으라고? 지금 그게 중요한 게 아니잖아!  (Rent It Out? That Is Not What Matters Right Now!)'
LEVEL = 'A1 — beginner'
LABELS = {"yejin": "탁예진", "joonmo": "라준모"}
SOURCE_NAME = '프로듀사 (The Producers) S1.10'
SOURCE_FILE = 'sources/the-producers/s01/e10.ko.srt'

INTRO = 'Back inside the apartment, Tak Ye-jin corners Ra Joon-mo to find out what he really meant by asking her to lease out her new place. Embarrassed to admit his feelings directly, Joon-mo hedges until Ye-jin accuses him of simply wanting free cooking and cleaning.'

STORY = [
    ('yejin', '전세를 놓으라고? 나 일주일도 안 남았는데.', 'You want me to lease it out? I have less than a week left before moving.', [(73, '전세를 놓으라고?'), (75, '나 일주일도 안 남았는데')], ''),
    ('joonmo', '좀 급한가? 그럼 일단 비워놓고 부동산 내가 알아볼까?', 'Is that too tight? Then leave it empty for now—shall I look into real-estate agencies?', [(76, '좀 급한가?'), (77, '그럼 일단 비워놓고'), (79, '부동산 내가 알아볼까?')], ''),
    ('yejin', '지금 그게 중요한 게 아니잖아! 그럼 뭔데?', 'That is not what matters right now! So what is your real reason?', [(80, '지금 그게 중요한 게 아니잖아'), (82, '그럼 뭔데?')], ''),
    ('joonmo', '그냥 내 의견이야. 난 너랑 같이 살면서 나쁘진 않았고.', 'It is just my opinion. Living together with you has not been bad for me.', [(83, '그냥 내 의견이야'), (84, '난 너랑 같이 살면서 나쁘진 않았고')], ''),
    ('yejin', '나쁘진 않았고?', 'Has not been bad?', [(85, '나쁘진 않았고?')], ''),
    ('joonmo', '아니, 좋았고! 또 꼬투리 잡는다. 좋았다는 것도 안 되냐?', 'Fine, it was good! There you go nitpicking again—am I not even allowed to say it was good?', [(86, '아니, 좋았고'), (88, '또 꼬투리 잡는다'), (90, '좋았다는 것도 안 되냐?')], ''),
    ('yejin', '너 내가 밥도 다 해주고 청소도 해주고 빨래도 가끔 해주고, 그런 게 편했던 거 아니야?', "Isn't it just that you found it convenient having me cook all your meals, clean, and do laundry from time to time?", [(91, '너 내가 밥도 다 해주고 청소도 해주고'), (92, '빨래도 가끔 해주고'), (93, '그런 게 편했던 거 아니야?')], ''),
    ('yejin', '딱 좋았는데 내가 지금 나간다 그러니까 나가지 말라 그러는 거 아니야?', 'Things were nice and cozy for you, so now that I am moving out, you are telling me not to leave, right?', [(96, '딱 좋았는데 내가 지금 나간다 그러니까'), (97, '나가지 말라 그러는 거 아니야?')], ''),
    ('joonmo', '어, 그래! 솔직히 너랑 있으니까 참 편하더라고.', 'Yeah, sure! Honestly, having you around has been super convenient.', [(98, '어 그래'), (100, '솔직히 너랑 있으니까 참 편하더라고')], ''),
    ('yejin', '그러니까 나 나가면 아줌마 구해야 되니까 그게 싫은 거냐?', 'So you just hate the idea of hiring a housekeeper once I move out?', [(101, '그러니까 너'), (102, '나 나가면 아줌마 구해야 되니까'), (103, '그게 싫은 거냐?')], ''),
    ('joonmo', '어떻게 알았냐? 네가 지금 날 그렇게 몰아가고 있잖아, 그런 놈으로!', 'How did you guess?! You are cornering me and painting me as that kind of jerk right now!', [(105, '어떻게 알았냐?'), (108, '지금 날 그렇게 몰아가고 있잖아 그런 놈으로')], ''),
    ('yejin', '됐다, 내가 너랑 무슨 얘기를 하니! 나쁜 놈!', 'Forget it, why do I even bother talking to you?! You jerk!', [(109, '됐다 내가 너랑 무슨 얘기를 하니'), (111, '나쁜 놈')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'You want me to lease it out? I have less than a week left before moving.'"),
    (1, None, "'Is that too tight? Then leave it empty for now—shall I look into real-estate agencies?'"),
    (2, None, "'That is not what matters right now! So what is your real reason?'"),
    (3, None, "'It is just my opinion. Living together with you has not been bad for me.'"),
    (4, None, "'Has not been bad?'"),
    (5, None, "'Fine, it was good! There you go nitpicking again—am I not even allowed to say it was good?'"),
    (6, None, "'Isn\'t it just that you found it convenient having me cook all your meals, clean, and do laundry from time to time?'"),
    (7, None, "'Things were nice and cozy for you, so now that I am moving out, you are telling me not to leave, right?'"),
    (8, None, "'Yeah, sure! Honestly, having you around has been super convenient.'"),
    (9, None, "'So you just hate the idea of hiring a housekeeper once I move out?'"),
    (10, None, "'How did you guess?! You are cornering me and painting me as that kind of jerk right now!'"),
    (11, None, "'Forget it, why do I even bother talking to you?! You jerk!'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Pressing someone for their real motive and deflecting vulnerability with sarcasm turn a near-confession into a classic roommate spat. Until next time!'
CLOSING = ('yejin', '다음에 만나요.')
