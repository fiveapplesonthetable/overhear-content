"""Scene 02: Tell Me Once You Have Sorted Out Your Feelings."""
ID = 'the-producers-s01e08-scene-02'
PAIR = "ko-en"
SHOW = 'the-producers'
SEASON = 1
EPISODE = 8
SCENE = 2
TITLE = '마음이 정리가 되면 그때 얘기해 주세요  (Tell Me Once You Have Sorted Out Your Feelings)'
LEVEL = "A1 — beginner"
LABELS = {"cindy": "신디", "seungchan": "백승찬"}
SOURCE_NAME = '프로듀사 (The Producers) S1.08'
SOURCE_FILE = 'sources/the-producers/s01/e08.ko.srt'

INTRO = "At the start of Episode 8, Baek Seung-chan stands frozen at the amusement park right after Cindy's surprise kiss. When he blurts out that it is his first time, Cindy playfully bristles and tells him to take his time before giving her his answer."

STORY = [
    ('seungchan', '처음이라…', 'Because it is my first time…', [(3, '처음이라')], ''),
    ('cindy', '아니 그럼 난 뭐 여러 번일 것 같아요? 연예인은 아무 때나 아무한테나 이럴 것 같냐고요!', 'Wait, so do you think I have done this plenty of times? Do you think celebrities kiss just anyone whenever they feel like it?!', [(4, '아니 그럼 난 뭐 여러 번일 것 같아요'), (7, '아무 때나'), (8, '아무한테나 이럴 것 같냐고요')], ''),
    ('seungchan', '아니요, 그런 뜻은 아니고요! 그런 의미 아니었습니다.', 'No, I did not mean that at all! That was not what I meant.', [(5, '아니요 그런 뜻은 아니고요'), (9, '아닙니다 그런 의미 아니었습니다')], ''),
    ('cindy', '그럼 무슨 의미인데요?', 'Then what did you mean by it?', [(10, '그럼 무슨 의미인데요')], ''),
    ('seungchan', '네?', 'Pardon?', [(11, '네')], ''),
    ('cindy', '무슨 의미냐고요! 아니 뭐 말을 좀 해봐요.', 'I asked what it means! Come on, say something already.', [(12, '무슨 의미냐고요'), (13, '아니 뭐 말을 좀 해봐요')], ''),
    ('cindy', '나 MC예요? 왜 나 혼자 진행을 하고 있어?', 'Am I a show host here? Why am I hosting this whole conversation by myself?', [(14, '나 MC예요'), (15, '왜 나 혼자 진행을 하고 있어')], ''),
    ('cindy', '시간을 좀 드릴게요. 피디님이 당황스러울 테니까 지금 당장 대답하는 건 좀 아닌 것 같아요.', 'I will give you some time—you must be flustered, so answering right on the spot does not seem right.', [(16, '시간을 좀 드릴게요'), (17, '피디님이 좀 당황스러울 테니까 지금 당장 대답하는 건 좀 아닌 것 같아요')], ''),
    ('cindy', '시간을 드릴 테니까 마음 같은 게 정리가 되면 그때 얘기해 주세요.', 'Take the time I give you, and once your feelings are sorted out, tell me then.', [(18, '시간을 드릴 테니까 마음 같은게 정리가 되면 그때 얘기해 주세요')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Because it is my first time…'"),
    (1, None, "'Wait, so do you think I have done this plenty of times? Do you think celebrities kiss just anyone whenever they feel like it?!'"),
    (2, None, "'No, I did not mean that at all! That was not what I meant.'"),
    (3, None, "'Then what did you mean by it?'"),
    (4, None, "'Pardon?'"),
    (5, None, "'I asked what it means! Come on, say something already.'"),
    (6, None, "'Am I a show host here? Why am I hosting this whole conversation by myself?'"),
    (7, None, "'I will give you some time—you must be flustered, so answering right on the spot does not seem right.'"),
    (8, None, "'Take the time I give you, and once your feelings are sorted out, tell me then.'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Clearing up an awkward phrasing, asking someone to say what they mean, and giving someone time to sort out their feelings give you expressive romantic-comedy Korean. Until next time!'
CLOSING = ('cindy', '또 만나요!')
