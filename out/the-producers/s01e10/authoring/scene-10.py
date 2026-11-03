"""Scene 10: Who Wrote Something Like This? Umbrella PD?."""
ID = 'the-producers-s01e10-scene-10'
PAIR = "ko-en"
SHOW = 'the-producers'
SEASON = 1
EPISODE = 10
SCENE = 10
TITLE = '이런 걸 누가 쓴 거야? 우산 피디?  (Who Wrote Something Like This? Umbrella PD?)'
LEVEL = 'A1 — beginner'
LABELS = {"seungchan": "백승찬", "cindy": "신디", "manager": "매니저"}
SOURCE_NAME = '프로듀사 (The Producers) S1.10'
SOURCE_FILE = 'sources/the-producers/s01/e10.ko.srt'

INTRO = 'After another sleepless night in the editing booth, Baek Seung-chan comes down with first-edit syndrome and hears dramatic variety captions narrating his lunch menu. Meanwhile, Cindy reads the weirdly self-deprecating preview voiceover script in her van, learns Seung-chan wrote it, and decides to record it anyway.'

STORY = [
    ('seungchan', '몇 시입니까? 예, 밤샜습니다.', 'What time is it? Yes, I stayed up all night.', [(498, '몇 시입니까?'), (501, '예')], ''),
    ('seungchan', '이 순간이 왔다! 필연적 선택, 피할 수는 없다, 된장찌개!', 'The moment has arrived! An inevitable choice you cannot escape—soybean-paste stew!', [(506, '이 순간이 왔다 필연적 선택 피할 수는 없다 된장찌개')], ''),
    ('seungchan', '최고의 난제, 오늘 점심엔 뭐 먹지?', "Humanity's greatest riddle: what should we eat for lunch today?", [(507, '최고의 난제 오늘 점심엔 뭐 먹지')], ''),
    ('cindy', '오빠, 이게 뭐야?', 'Wait, what is this script?', [(536, '오빠 이게 뭐야?')], ''),
    ('manager', '이번에 일박 예고를 좀 특이하게 만들어 보겠다고…', "They said they wanted to make the show's preview extra unique this week…", [(537, '좀 특이하게 만들어 보겠다고')], ''),
    ('cindy', '아니 무슨 이런 멘트가… 이게 멘트야? 이런 걸 누가 쓴 거야?', 'What kind of lines are these—you call this a script? Who on earth wrote this?', [(538, '아니 무슨 이런 멘트가'), (539, '이게 멘트야?'), (540, '이런 거 누가 쓴 거야')], ''),
    ('manager', '우산 피디.', 'Umbrella PD.', [(541, '우산')], ''),
    ('cindy', '그 우산 피디는 할 줄 아는 게 뭐야? 감도 없어, 사람 비위도 못 맞춰!', 'What does that Umbrella PD even know how to do?! He has zero sense and cannot flatter anyone!', [(542, '할 줄 아는 게 뭐냐?'), (543, '감도 없어'), (544, '사람 비위도 못 맞춰')], ''),
    ('cindy', '그 예고 멘트도 많이 이상해.', 'And these preview lines are seriously weird too.', [(546, '그 예고 멘트도 많이 이상해')], ''),
    ('manager', '왜? 오빠가 얘기할까, 대본 바꿔달라고?', 'Why? Shall I call and ask them to change the script?', [(547, '왜?'), (548, '오빠가 얘기할까?'), (549, '대본 바꿔달라고')], ''),
    ('cindy', '아니, 뭐 이게 한두 개 바꿔서 될 게 아닌데 뭐. 그냥 하자.', 'No, changing a line or two would not even fix this anyway. Let us just do it.', [(550, '이게 한두 개 바꿔서 될 게 아닌데'), (553, '그냥')], ''),
    ('manager', '확실해? 해? 장난해?', 'Are you sure? You are doing it? Are you kidding me?', [(554, '확실해?'), (557, '해?'), (558, '장난해?')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'What time is it? Yes, I stayed up all night.'"),
    (1, None, "'The moment has arrived! An inevitable choice you cannot escape—soybean-paste stew!'"),
    (2, None, "'Humanity\'s greatest riddle: what should we eat for lunch today?'"),
    (3, None, "'Wait, what is this script?'"),
    (4, None, "'They said they wanted to make the show\'s preview extra unique this week…'"),
    (5, None, "'What kind of lines are these—you call this a script? Who on earth wrote this?'"),
    (6, None, "'Umbrella PD.'"),
    (7, None, "'What does that Umbrella PD even know how to do?! He has zero sense and cannot flatter anyone!'"),
    (8, None, "'And these preview lines are seriously weird too.'"),
    (9, None, "'Why? Shall I call and ask them to change the script?'"),
    (10, None, "'No, changing a line or two would not even fix this anyway. Let us just do it.'"),
    (11, None, "'Are you sure? You are doing it? Are you kidding me?'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Laughing at variety-caption brain fog and grumbling affectionately over an eccentric script set up their dubbing-room reunion. See you next time!'
CLOSING = ('cindy', '또 봐요.')
