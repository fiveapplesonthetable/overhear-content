"""Scene 07: Sending a Girl in a Cast to an Event?."""
ID = 'the-producers-s01e07-scene-07'
PAIR = "ko-en"
SHOW = 'the-producers'
SEASON = 1
EPISODE = 7
SCENE = 7
TITLE = '깁스까지 한 애한테 행사라니  (Sending a Girl in a Cast to an Event?)'
LEVEL = "A1 — beginner"
LABELS = {"manager": "매니저", "seungchan": "백승찬", "yejin": "탁예진"}
SOURCE_NAME = '프로듀사 (The Producers) S1.07'
SOURCE_FILE = 'sources/the-producers/s01/e07.ko.srt'

INTRO = "On his way to work, Baek Seung-chan gives Tak Ye-jin a ride to the hospital so she can have her stitches removed. Inside that same hospital, Cindy's road manager complains about CEO Byun's harsh schedule—only to turn around and find Cindy gone."

STORY = [
    ('seungchan', '회사 가세요?', 'Are you heading to the station?', [(115, '회사 가세요')], ''),
    ('yejin', '아니, 나 병원 가. 이거 오늘 실밥 푸는 날.', 'No, I am going to the hospital—today is the day my stitches come out.', [(116, '아니 나 병원 가'), (117, '이거 오늘'), (117, '푸는 날')], ''),
    ('seungchan', '타세요, 저 점심때부터 회의라 좀 늦게 가도 되거든요.', 'Hop in—my meeting starts at lunchtime, so I can go in a little late.', [(118, '타세요'), (119, '저 점심때부터 회의라'), (120, '좀 늦게 가도 되거든요')], ''),
    ('yejin', '야, 뭘 깨끗한데 계속 치워? 내 차보다 훨씬 깨끗하다.', 'Hey, why do you keep tidying up when it is already clean? It is way cleaner than my car.', [(123, '야 뭘 깨끗한데 계속 치워'), (124, '훨씬 깨끗하다')], ''),
    ('yejin', '어? 내가 아는 애 아니야?', 'Huh? Is that not someone I know?', [(125, '내가 아는 애 아니야')], ''),
    ('manager', '예, 실장님 연락처 받았습니다. 공항 도착하는 대로 바로 연락드리겠습니다.', 'Yes, Director, I got the contact info. I will call you the moment we arrive at the airport.', [(126, '연락처 받았습니다'), (127, '공항 도착하는 대로 바로 연락드리겠습니다')], ''),
    ('manager', '나도 솔직히 좀 대표님이 너무하신다고 생각한다. 아니, 깁스까지 한 애한테 행사라니.', 'Honestly, even I think CEO Byun is going too far—making a girl in a cast do an event.', [(130, '나도 솔직히 좀 대표님이 너무하신다고 생각한다'), (131, '깁스까지 하는 애한테 행사라니')], ''),
    ('manager', '그래도 어쩌냐, 갔다 와서 좀 쉬자. 오빠도 강력하게 어필해볼게.', 'Still, what can we do—let us get back and rest. I will push back strongly for you too.', [(132, '그래도 어쩌냐'), (133, '갔다 와서 좀 쉬자'), (134, '오빠도 강력하게 어필해볼게')], ''),
    ('manager', '신디야?', 'Cindy?', [(135, '신디야')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Are you heading to the station?'"),
    (1, None, "'No, I am going to the hospital—today is the day my stitches come out.'"),
    (2, None, "'Hop in—my meeting starts at lunchtime, so I can go in a little late.'"),
    (3, None, "'Hey, why do you keep tidying up when it is already clean? It is way cleaner than my car.'"),
    (4, None, "'Huh? Is that not someone I know?'"),
    (5, None, "'Yes, Director, I got the contact info. I will call you the moment we arrive at the airport.'"),
    (6, None, "'Honestly, even I think CEO Byun is going too far—making a girl in a cast do an event.'"),
    (7, None, "'Still, what can we do—let us get back and rest. I will push back strongly for you too.'"),
    (8, None, "'Cindy?'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Offering someone a lift, getting stitches removed, and sympathizing over a grueling schedule give you practical everyday Korean. Until next time!'
CLOSING = ('seungchan', '안녕히 가세요!')
