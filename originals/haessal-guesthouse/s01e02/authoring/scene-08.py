# Authoring module for haessal-guesthouse-s01e02-scene-08.
ID = 'haessal-guesthouse-s01e02-scene-08'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 2
SCENE = 8
TITLE = '방 하나에 이름 두 개  (Two Names, One Room)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'sungmin': '성민', 'mina': '미나', 'junho': '준호'}
INTRO = "On Wednesday evening, as dusk settles over Seoul, Sungmin steps out of his office holding both the tablet computer and Junho's paper ledger, looking pale. Mina and Junho look up at once. Listen first."
OPENER = "Let's trace how the double booking happened, one line at a time."
TRANSITION = "Now let's listen to the final scene of Episode 2 again from start to finish."
OUTRO = "Two guests booked into Room 7, rain pouring outside, and only forty minutes before the eight o'clock arrival! Episode 2 is done—join us in Episode 3 to see if the attic can save the night."
CLOSING = ('sungmin', '안녕히 가세요!')
STORY = [
    ('sungmin', '준호 씨... 미나 씨... 제발 오늘 밤 육호실이 비어 있다고 말해 주세요.', 'Junho... Mina... please tell me Room 6 is empty tonight.'),
    ('mina', '아니요, 사장님. 한 시간 전에 남쪽에서 온 부부가 육호실에 들어갔어요.', 'No, boss. An hour ago a couple from the south checked into Room 6.'),
    ('junho', '일호실부터 칠호실까지 열쇠가 다 나갔고, 팔호실은 페인트가 아직 안 말랐어요.', 'Every key from Room 1 to Room 7 is out, and in Room 8 the paint is not dry yet.'),
    ('sungmin', '아이고, 큰일 났네요! 어제 안경을 안 쓰고 태블릿으로 전화 예약을 받았거든요!', 'Oh dear, disaster! Yesterday I took a phone booking on the tablet without wearing my glasses!'),
    ('mina', '잠깐만요, 태블릿 화면하고 종이 장부를 같이 볼게요.', 'Wait a moment, let me look at the tablet screen and the paper ledger together.'),
    ('junho', '맞혀 볼까요? 없는 방을 손님한테 약속하셨죠?', 'Shall I guess? You promised a guest a room we do not have, right?'),
    ('mina', '사장님! 칠호실에는 벌써 손님이 계신데 칠호실에 또 다른 손님을 예약하셨어요!', 'Boss! There is already a guest in Room 7, and you booked another guest into Room 7!'),
    ('sungmin', '게다가 그 손님이 오늘 저녁 여덟 시에 여기로 와요! 사십 분 남았어요!', "What's more, that guest arrives here at eight o'clock this evening! Forty minutes left!"),
    ('junho', '그 태블릿은 함정이라고 제가 말했잖아요.', 'I told you that tablet is a trap.'),
    ('sungmin', '밖에는 비가 오고 우리 골목 호텔도 다 찼어요! 이제 어떻게 하죠?', 'Outside it is raining and every hotel in our alley is full! What do we do now?'),
    ('mina', '잠깐만요, 계단 위 삼층에는 뭐가 있어요?', 'Wait—what is up on the third floor above the stairs?'),
    ('junho', '오래된 햇볕 잘 드는 다락방 서재요... 빨리 저를 따라오세요!', 'The old sunlit attic study... follow me quickly!'),
]
WALK = [
    (1, None, ["'No, boss. An hour ago a couple from the south checked into Room 6.' Married couples are referred to politely as ", (None, '부부가'), ', distinct from boyfriend-and-girlfriend pairs.']),
    (2, None, ["'Every key from Room 1 to Room 7 is out, and in Room 8 the paint is not dry yet.' Notice ", (None, '아직'), ", the essential time word for 'still' or 'not yet'."]),
    (5, None, ["'Shall I guess? You promised a guest a room we do not have, right?' Ending on ", (None, '약속하셨죠'), " checks something the speaker already strongly suspects—'you promised, didn't you?'."]),
    (7, None, ["'What's more, that guest arrives here at eight o'clock this evening! Forty minutes left!' Piling a second problem onto the first begins with ", (None, '게다가'), ", 'besides' or 'on top of that'."]),
    (7, None, ["'What's more, that guest arrives here at eight o'clock this evening! Forty minutes left!' Time remaining on the clock uses ", (None, '남았어요'), ", 'are left'."]),
    (8, None, ["'I told you that tablet is a trap.' Reminding someone of something they already heard uses ", (None, '말했잖아요'), ", 'as I told you!'."]),
    (9, None, ["'Outside it is raining and every hotel in our alley is full! What do we do now?' Korean says rain 'comes' rather than 'falls': ", (None, '비가 오고'), '.']),
    (11, None, ["'The old sunlit attic study... follow me quickly!' Tucked under the roof beams is the ", (None, '다락방'), ", 'attic room'."]),
]
