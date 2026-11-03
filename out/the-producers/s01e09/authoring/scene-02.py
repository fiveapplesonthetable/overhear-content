"""Scene 02: I Do Not Think I Can Watch the Movie Tonight."""
ID = 'the-producers-s01e09-scene-02'
PAIR = "ko-en"
SHOW = 'the-producers'
SEASON = 1
EPISODE = 9
SCENE = 2
TITLE = '영화 못 볼 것 같은데요  (I Do Not Think I Can Watch the Movie Tonight)'
LEVEL = "A1 — beginner"
LABELS = {"seungchan": "백승찬", "yejin": "탁예진"}
SOURCE_NAME = '프로듀사 (The Producers) S1.09'
SOURCE_FILE = 'sources/the-producers/s01/e09.ko.srt'

INTRO = "Rushing into the theater lobby after Tak Ye-jin's phone battery dies, Baek Seung-chan awkwardly apologizes that he cannot watch the movie after all because Cindy is waiting outside his house in the pouring rain."

STORY = [
    ('seungchan', '핸드폰이 꺼져 있어서요.', 'Your phone was turned off.', [(35, '핸드폰이 꺼져 있어서')], ''),
    ('yejin', '어 아까 보니까 그렇더라. 우리 근데 얼마 안 늦었어, 들어가자!', 'Yeah, I noticed that just now. Still, we are barely late—let us head inside!', [(36, '어 아까 보니까 그렇더라'), (37, '우리 근데 얼마 안 늦었어 들어가자')], ''),
    ('seungchan', '아 선배 죄송한데 영화 못 볼 것 같은데요.', 'Ah Senior, I am really sorry, but I do not think I can watch the movie.', [(38, '아 선배 죄송한데'), (40, '영화 못 볼 것 같은데')], ''),
    ('yejin', '얘 뭐래니? 그럼 그렇지, 아유 내 팔자야!', 'What are you talking about? Figures—honestly, just my luck!', [(41, '얘 뭐래니'), (42, '그럼 그렇지'), (43, '아유 내 팔자야')], ''),
    ('yejin', '내가 무슨 한가하게 영화를 본다고 이렇게 팝콘까지 사가지고! 신디 기다린다며?', 'Who am I to watch a movie leisurely after even buying popcorn like this! You say Cindy is waiting?', [(44, '내가 무슨 한가하게 영화를 본다고'), (46, '이렇게 팝콘까지 사가지고'), (47, '신디 기다린다며')], ''),
    ('seungchan', '지금 비가 와서요.', 'Because it is raining right now.', [(48, '지금 비가 와서')], ''),
    ('yejin', '내 말이 그 말이다! 걔는 뭐 이렇게 급히 할 말이 있다고 이 비 오는데 말이야!', 'That is my exact point! What could she possibly need to say so urgently in this pouring rain?!', [(49, '내 말이 그 말이다'), (50, '뭐 이렇게 급히 할 말이 있다고'), (51, '이 비 오는데 말이야')], ''),
    ('yejin', '어머, 변 대표하고 한 판 붙고 또 튄 거 아니니? 정말 욱해서 걱정이다, 걱정이야 진짜!', 'Oh gosh, did she clash with CEO Byun and bolt again? Her fiery temper really worries me!', [(52, '한 판 붙고 또 핀 거 아니니'), (54, '정말 욱해서 걱정이다 걱정이야 진짜')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Your phone was turned off.'"),
    (1, None, "'Yeah, I noticed that just now. Still, we are barely late—let us head inside!'"),
    (2, None, "'Ah Senior, I am really sorry, but I do not think I can watch the movie.'"),
    (3, None, "'What are you talking about? Figures—honestly, just my luck!'"),
    (4, None, "'Who am I to watch a movie leisurely after even buying popcorn like this! You say Cindy is waiting?'"),
    (5, None, "'Because it is raining right now.'"),
    (6, None, "'That is my exact point! What could she possibly need to say so urgently in this pouring rain?!'"),
    (7, None, "'Oh gosh, did she clash with CEO Byun and bolt again? Her fiery temper really worries me!'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Dead phone batteries, calling off movie plans at the last minute, and worrying over an impulsive friend in the rain pack natural everyday Korean. Until next time!'
CLOSING = ('seungchan', '안녕히 계세요!')
