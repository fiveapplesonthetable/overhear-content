"""Scene 06: Who Are the New Members?."""
ID = 'the-producers-s01e03-scene-06'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 3
SCENE = 6
TITLE = "새 멤버 누구야?  (Who Are the New Members?)"
LEVEL = "A1 — beginner"
LABELS = {"joonmo": "라준모", "reporter": "강기자"}
SOURCE_NAME = "프로듀사 (The Producers) S1.03"
SOURCE_FILE = "sources/the-producers/s01/e03.ko.srt"

INTRO = 'In the KBS lobby, entertainment journalist Reporter Kang intercepts Ra Joon-mo to fish for news about the new season. When Joon-mo dodges the question, Kang immediately guesses the show was turned down and demands an exclusive scoop.'

STORY = [
    ('joonmo', '아, 또 왜 왔어요?', 'Ugh, why did you come here again?', [(203, '아, 또 왜 왔어요?')], ''),
    ('reporter', '에이, 삐졌어? 새 멤버 누구야?', 'Come on, are you sulking? Who are the new cast members?', [(204, '에이, 삐졌어'), (210, '새 멤버 누구')], ''),
    ('joonmo', '아직 결정 안 됐어요.', 'Nothing has been decided yet.', [(211, '아직 결정 안 됐어요')], ''),
    ('reporter', '맞구나! 나 쓴다?', 'So my guess is right! Shall I write the article?', [(215, '맞구나! 나 쓴다?')], ''),
    ('joonmo', '쓰세요. 확신이 들면 쓰시라고요.', 'Go ahead and write it. Write it if you are so sure.', [(216, '쓰세요'), (218, '확신이 들면 쓰시라고')], ''),
    ('reporter', '까였구나!', 'You got rejected!', [(220, '까였구나')], ''),
    ('joonmo', '강 기자님, 나한테 왜 이래요, 진짜?', 'Reporter Kang, why are you doing this to me, seriously?', [(226, '강 기자님 나한테 왜 이래 진짜')], ''),
    ('reporter', '누군지 알려주면 되잖아.', 'All you have to do is tell me who it is.', [(228, '누군지 알려주면 되잖아')], ''),
    ('joonmo', '있어 봐, 조율 중이야.', 'Hold on, we are still coordinating.', [(229, '있어봐 조율 중이야')], ''),
    ('reporter', '촬영이 일주일 남았는데 언제까지 기다려?', 'Filming is one week away, so how long am I supposed to wait?', [(230, '촬영이 일주일 남았는데 언제까지 기다려')], ''),
    ('reporter', '오늘 안에 나한테만 단독으로 연락 주는 거지?', 'You will contact me alone with an exclusive before the day ends, right?', [(233, '오늘 안에 연락 주는 거지?'), (234, '나한테만 단독으로')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Ugh, why did you come here again?'"),
    (1, None, "'Come on, are you sulking? Who are the new cast members?'"),
    (2, None, "'Nothing has been decided yet.'"),
    (3, None, "'So my guess is right! Shall I write the article?'"),
    (4, None, "'Go ahead and write it. Write it if you are so sure.'"),
    (5, None, "'You got rejected!'"),
    (6, None, "'Reporter Kang, why are you doing this to me, seriously?'"),
    (7, None, "'All you have to do is tell me who it is.'"),
    (8, None, "'Hold on, we are still coordinating.'"),
    (9, None, "'Filming is one week away, so how long am I supposed to wait?'"),
    (10, None, "'You will contact me alone with an exclusive before the day ends, right?'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'You just heard crisp workplace expressions for saying nothing is decided yet, coordinating details, and asking someone to wait. See you next time.'
CLOSING = ('joonmo', '다음에 만나요.')
