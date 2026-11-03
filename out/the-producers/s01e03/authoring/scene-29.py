"""Scene 29: It Freezes Sometimes When the Signal Is Weak."""
ID = 'the-producers-s01e03-scene-29'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 3
SCENE = 29
TITLE = "가끔 신호가 약할 때 이럽니다  (It Freezes Sometimes When the Signal Is Weak)"
LEVEL = "A1 — beginner"
LABELS = {"byun": "변대표", "joonmo": "라준모", "rep": "소속사 대표"}
SOURCE_NAME = "프로듀사 (The Producers) S1.03"
SOURCE_FILE = "sources/the-producers/s01/e03.ko.srt"

INTRO = 'Meanwhile at another entertainment agency, Ra Joon-mo connects by video call to pitch a Miss A star for the new season. Every time Joon-mo makes his request, the screen suspiciously freezes—right before CEO Byun calls his cell phone.'

STORY = [
    ('joonmo', '제가 오늘 섭외 관련해서 부탁드릴 일이 좀 있는데요.', 'Today I have a favor to ask you regarding casting.', [(1030, '제가 오늘 그 부탁드릴 일이 좀 있는데'), (1031, '섭외 관련해서')], ''),
    ('rep', '가끔 이럽니다, 신호가 약할 때.', 'It freezes like this sometimes when the signal is weak.', [(1037, '가끔 이럽니다 신호가 약할 때')], ''),
    ('joonmo', '저희가 이번에 새롭게 하는 거라서 세게 가려고요.', 'Because we are revamping the show from scratch, we want to go big.', [(1041, '새롭게 하는 거라서'), (1042, '세게 가려고요')], ''),
    ('joonmo', '전화 통화로 하면 안 될까요?', 'Could we not just talk by phone instead?', [(1046, '전화 통화로 하면 안 될까?')], ''),
    ('rep', '공연 앞두고는 전화를 꺼 두셔서요.', 'Before a concert, he always keeps his phone switched off.', [(1047, '공연 앞두고는 전화를 꺼두셔서요')], ''),
    ('byun', '라 피디님? 우리 오랜만이네.', 'Producer Ra? It has been a long time.', [(1050, '라PD님?'), (1051, '우리 오랜만이네')], ''),
    ('joonmo', '우리가 통화할 일이 있습니까?', 'Do you and I have any reason to be on the phone?', [(1053, '우리가 통화할 일이 있습니까?')], ''),
    ('byun', '나도 없을 줄 알았는데 생겼네.', 'I thought we never would either, yet something just came up.', [(1055, '나도 없을 줄 알았는데 생겼네')], ''),
    ('byun', '그쪽 팀 막내 피디라는 사람이 날 찾아왔어요.', 'Someone claiming to be the youngest producer on your team came to see me.', [(1056, '그쪽 팀 막내'), (1056, '사람이 날 찾아왔어요')], ''),
    ('joonmo', '뭐라고요? 거기 어딥니까?', 'What did you say? Where are you right now?', [(1057, '뭐라고요?'), (1058, '거기 어딥니까?')], ''),
    ('joonmo', '내가 지금 급한 일이 좀 생겨서요!', 'An urgent matter just came up for me right now!', [(1060, '내가 지금 급한 일이 좀 생겨서요')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Today I have a favor to ask you regarding casting.'"),
    (1, None, "'It freezes like this sometimes when the signal is weak.'"),
    (2, None, "'Because we are revamping the show from scratch, we want to go big.'"),
    (3, None, "'Could we not just talk by phone instead?'"),
    (4, None, "'Before a concert, he always keeps his phone switched off.'"),
    (5, None, "'Producer Ra? It has been a long time.'"),
    (6, None, "'Do you and I have any reason to be on the phone?'"),
    (7, None, "'I thought we never would either, yet something just came up.'"),
    (8, None, "'Someone claiming to be the youngest producer on your team came to see me.'"),
    (9, None, "'What did you say? Where are you right now?'"),
    (10, None, "'An urgent matter just came up for me right now!'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Saying it has been a long time and excusing yourself when an urgent matter comes up are essential phrases for Korean phone calls. See you next time.'
CLOSING = ('byun', '다음에 봐요.')
