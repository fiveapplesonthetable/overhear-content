"""Scene 05: I Already Know Everything, Producer."""
ID = 'the-producers-s01e08-scene-05'
PAIR = "ko-en"
SHOW = 'the-producers'
SEASON = 1
EPISODE = 8
SCENE = 5
TITLE = '저 다 알고 왔습니다, 피디님  (I Already Know Everything, Producer)'
LEVEL = "A1 — beginner"
LABELS = {"joonmo": "라준모", "manager": "매니저", "yejin": "탁예진"}
SOURCE_NAME = '프로듀사 (The Producers) S1.08'
SOURCE_FILE = 'sources/the-producers/s01/e08.ko.srt'

INTRO = "Finally arriving at the amusement park, Tak Ye-jin gets a call saying her car headlights were left on—even though she peeled her phone-number card off the windshield. Startled in the dark lot, she swings first and discovers Cindy's chief manager standing right there."

STORY = [
    ('joonmo', '아이고, 얘는 온다 온다 하고 왜 이렇게 안 와? 불꽃놀이 그렇게 좋아하면서 20분밖에 안 남았구먼!', 'Good grief, she keeps saying she is coming—why is she still not here when fireworks start in twenty minutes?!', [(81, '얘는 온다 온다 하고 왜 이렇게 안 와'), (82, '불꽃놀이 그렇게 좋아하면서 20분밖에 안 남았구만')], ''),
    ('yejin', '나 들어갔다가 누가 내 차 라이트 켜져 있다고 그래가지고. 근데 준모야, 나 번호 치웠는데 내 번호 어떻게 알고 전화했지?', 'I walked in and someone phoned saying my headlights were on—wait Joon-mo, I removed my number card, so how did they know my number?', [(84, '나 들어갔다가 누가'), (85, '번호 치웠는데'), (86, '내 번호 어떻게 알고 전화했지')], ''),
    ('joonmo', '야 그게 무슨 소리야, 네 번호를 치웠는데 누가 전화를 해? 여보세요?', 'Wait, what are you talking about—if you removed your number, who would call you? Hello?!', [(87, '그게 무슨 소리야 네 번호를 치웠는데 누가 전화를 해'), (88, '여보세요')], ''),
    ('yejin', '아 뭐야, 놀랐잖아요! 김 실장님이 여기 어떻게 오셨어요?', 'Oh gosh, you startled me! Chief Manager Kim, how did you end up out here?', [(89, '아 뭐야'), (91, '여기'), (96, '여기는 어떻게 오셨냐고요')], ''),
    ('manager', '죄송합니다, 피디님이 제 번호로 전화 안 받으시니까…', 'I am sorry—since you would not pick up calls from my own number, Producer…', [(90, '죄송합니다'), (93, '제 번호도 전화 안 받으시니까')], ''),
    ('yejin', '나는 나중에 다시 전화하려고 그랬죠! 근데 여기는 신디 때문에요?', 'I was going to call you back later! Wait—did you come out here because of Cindy?', [(94, '나는 나중에 다시 전화하려고 그랬죠'), (97, '신디 때문에요')], ''),
    ('manager', '신디 데리고 계시잖아요.', 'You have Cindy with you right now, after all.', [(99, '신디 데리고 계시잖아요')], ''),
    ('yejin', '네? 누가, 내가? 난 무슨 소리 하는지 통 모르겠는데!', 'Pardon? Who, me?! I have zero clue what you are talking about!', [(100, '네? 누가 내가'), (101, '난 무슨 소리 하는지 통 모르겠는데')], ''),
    ('manager', '저 다 알고 왔습니다, 피디님.', 'I came here already knowing everything, Producer.', [(102, '저 다 알고 왔습니다 PD님')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Good grief, she keeps saying she is coming—why is she still not here when fireworks start in twenty minutes?!'"),
    (1, None, "'I walked in and someone phoned saying my headlights were on—wait Joon-mo, I removed my number card, so how did they know my number?'"),
    (2, None, "'Wait, what are you talking about—if you removed your number, who would call you? Hello?!'"),
    (3, None, "'Oh gosh, you startled me! Chief Manager Kim, how did you end up out here?'"),
    (4, None, "'I am sorry—since you would not pick up calls from my own number, Producer…'"),
    (5, None, "'I was going to call you back later! Wait—did you come out here because of Cindy?'"),
    (6, None, "'You have Cindy with you right now, after all.'"),
    (7, None, "'Pardon? Who, me?! I have zero clue what you are talking about!'"),
    (8, None, "'I came here already knowing everything, Producer.'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Realizing a caller could not have seen your windshield card, playing innocent on the spot, and getting caught red-handed pack suspenseful Korean dialogue. Until next time!'
CLOSING = ('yejin', '다음에 봐요!')
