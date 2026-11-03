"""Scene 16: The Caption Just Aired Wrong!."""
ID = 'the-producers-s01e06-scene-16'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 6
SCENE = 16
TITLE = '자막 잘못 나갔잖아!  (The Caption Just Aired Wrong!)'
LEVEL = "A1 — beginner"
LABELS = {"joonmo": "라준모", "yejin": "탁예진"}
SOURCE_NAME = "프로듀사 (The Producers) S1.06"
SOURCE_FILE = 'sources/the-producers/s01/e06.ko.srt'

INTRO = "At his apartment, Ra Joon-mo watches the premiere alongside Tak Ye-jin and brags about his editing until Ye-jin spots a geographic typo in an on-air caption. Minutes later, Joon-mo's mother calls Ye-jin about his skipped blind date."

STORY = [
    ('joonmo', '괜찮아? 방금 자막 센스 있었지?', 'Looks good, right? That caption just now was pretty clever, was it not?', [(449, '괜찮아'), (450, '방금 자막 센스 있었지')], ''),
    ('yejin', '백승찬 화면에 나오는 거 나쁘지 않다, 제법이야.', 'Baek Seung-chan appearing on screen is not bad at all—he actually holds his own.', [(452, '백승찬'), (453, '화면에 나오는 거 나쁘지 않다'), (454, '제법이야')], ''),
    ('joonmo', '내가 편집을 기가 막히게 해서 그렇지, 쟤가 무슨 남자야, 애지!', 'Only because my editing is phenomenal—what kind of grown man is he, he is just a kid!', [(457, '내가 편집을 기가 막히게 해서 그렇지'), (458, '남자는'), (459, '애지')], ''),
    ('yejin', '야, 근데 경남 고령 맞아? 경북 고령 아니야?', 'Wait—is Goryeong really in South Gyeongsang? Is it not in North Gyeongsang?', [(460, '야 근데 경남 고령 맞아? 경북 고령 아니야')], ''),
    ('joonmo', '어떻게 된 거야, 자막 잘못 나갔잖아 지금, 자막 누가 쓴 거야!', 'How did this happen—the caption just aired wrong, who wrote the captions!', [(462, '야 어떻게 된 거야'), (463, '자막'), (463, '나갔잖아 지금'), (464, '자막 누가 쓴 거야')], ''),
    ('yejin', '네 아줌마 괜찮아요, 말씀하세요.', "Yes, ma'am, I am free to talk—please go ahead.", [(466, '네 아줌마 괜찮아요 말씀하세요')], ''),
    ('yejin', '근데 선도 본다면서요, 그 여자 검사랑?', 'Wait, did you not say he was having a matchmaking meeting with that female prosecutor?', [(472, '근데 뭐 선도 본다면서요, 그 여자 검사랑')], ''),
    ('yejin', '어머, 안 봤대요? 편집실에서 잠들어서요?', 'Oh my, he skipped it because he fell asleep in the editing room?', [(474, '어머, 안 봤대요'), (476, '편집실에서')], ''),
    ('yejin', '이제 준모도 나이를 먹을 만큼 먹었고 스스로 결정하게 해주시는 게 어떨까요.', 'Joon-mo is old enough now, so maybe it would be best to let him decide for himself.', [(488, '나이를 먹을 만큼 먹었고'), (490, '스스로 결정하게 해주시는 게')], ''),
    ('yejin', '아줌마가 여의도 아파트로 쳐들어가신다고요? 아뇨, 제가 얘기하겠습니다!', 'You will storm into his Yeouido apartment and move in? No, I will talk to him right away!', [(491, '여의도 아파트로 확 쳐들어가서'), (493, '제가 얘기하겠습니다')], ''),
    ('yejin', '그럼요, 준모가 제 말 잘 듣잖아요!', 'Of course—Joon-mo always listens to me!', [(494, '그럼요'), (495, '제 말 잘 듣잖아요')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Looks good, right? That caption just now was pretty clever, was it not?'"),
    (1, None, "'Baek Seung-chan appearing on screen is not bad at all—he actually holds his own.'"),
    (2, None, "'Only because my editing is phenomenal—what kind of grown man is he, he is just a kid!'"),
    (3, None, "'Wait—is Goryeong really in South Gyeongsang? Is it not in North Gyeongsang?'"),
    (4, None, "'How did this happen—the caption just aired wrong, who wrote the captions!'"),
    (5, None, "'Yes, ma'am, I am free to talk—please go ahead.'"),
    (6, None, "'Wait, did you not say he was having a matchmaking meeting with that female prosecutor?'"),
    (7, None, "'Oh my, he skipped it because he fell asleep in the editing room?'"),
    (8, None, "'Joon-mo is old enough now, so maybe it would be best to let him decide for himself.'"),
    (9, None, "'You will storm into his Yeouido apartment and move in? No, I will talk to him right away!'"),
    (10, None, "'Of course—Joon-mo always listens to me!'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Catching a live caption mistake on television and learning someone quietly skipped a matchmaking date gives you dramatic, everyday Korean conversation. Until next time!'
CLOSING = ('yejin', '안녕히 계세요!')
