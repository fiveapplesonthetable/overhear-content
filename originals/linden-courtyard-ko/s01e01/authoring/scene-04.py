# Authoring module for linden-courtyard-ko-s01e01-scene-04.
ID = 'linden-courtyard-ko-s01e01-scene-04'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'Room Four on the Second Floor  (이 층에 있는 사 호실)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = '은퇴한 피아노 선생님 에블린이 기차 여행을 마치고 짙은 파란색 여행 가방과 함께 사 호실에 체크인합니다. 원피스와 악보, 아끼는 찻잔만 넣었다는데도 가방이 유난히 묵직하게 느껴지네요. 먼저 따뜻한 환영 인사를 영어로 들어 보세요.'
OPENER = '그럼 손님을 맞이하는 정중한 표현들을 한 문장씩 살펴볼까요.'
TRANSITION = '장면 전체를 다시 한번 편안한 마음으로 들어 보세요.'
OUTRO = '그레이엄이 묵직한 파란 가방을 이 층 사 호실까지 들어다 드리면서 첫 손님 체크인이 순조롭게 끝났어요. 과연 저 무거운 가방 안에는 무엇이 들어 있을까요. 다음 장면에서 곧 확인해 보세요.'
CLOSING = ('evelyn', 'Take care!')
STORY = [
    ('hannah', "Welcome! Good morning, ma'am.", '환영합니다! 좋은 아침이에요, 선생님.'),
    ('evelyn', 'Good morning, my dear. I have a booking for Evelyn.', '좋은 아침이에요, 아가씨. 에블린 이름으로 예약이 있어요.'),
    ('hannah', 'Yes, room four on the second floor! How was your train trip?', '네, 이 층 사 호실이세요! 기차 여행은 어떠셨나요?'),
    ('evelyn', 'Quiet and pleasant, thank you, though this suitcase feels very heavy today.', '조용하고 쾌적했어요, 고마워요. 그런데 오늘따라 이 여행 가방이 아주 무겁게 느껴지네요.'),
    ('graham', 'Allow me. Goodness, did you pack stones in here?', '제가 들어 드릴게요. 세상에, 여기 안에 돌멩이라도 챙겨 넣으셨나요?'),
    ('evelyn', 'Only dresses, sheet music, and my favorite teacup!', '원피스 몇 벌하고 악보, 그리고 제가 가장 아끼는 찻잔뿐인걸요!'),
    ('hannah', 'Here is your key, number four. Breakfast is from seven thirty to ten.', '여기 사 호실 열쇠 있습니다. 아침 식사는 일곱 시 삼십 분부터 열 시까지예요.'),
    ('evelyn', 'Wonderful. Is the window facing the street or the courtyard?', '정말 좋네요. 방 창문은 거리 쪽을 향하나요, 아니면 안뜰 쪽을 향하나요?'),
    ('hannah', 'The courtyard, right above the old tree. It is very quiet.', '안뜰 쪽이에요, 오래된 나무 바로 위쪽이죠. 아주 조용해요.'),
    ('evelyn', 'Just what I need. Where are the stairs?', '딱 제가 바라던 곳이네요. 계단은 어디에 있나요?'),
    ('graham', 'Right through this archway. I will carry the blue bag up for you.', '바로 이 아치형 통로를 지나가시면 돼요. 파란 가방은 제가 위층까지 들어 드릴게요.'),
    ('evelyn', 'Thank you both very much.', '두 분 모두 정말 고맙습니다.'),
]
WALK = [
    (0, None, ["'환영합니다! 좋은 아침이에요, 선생님.' 성함을 아직 모르는 여성 손님께 예의를 갖추어 인사할 때는 문장 끝에", (None, "ma'am"), '바로 이 존칭을 덧붙여 정중함을 나타내요.']),
    (1, None, ["'좋은 아침이에요, 아가씨. 에블린 이름으로 예약이 있어요.' 프런트에서 예약 사실을 차분히 알릴 때는", (None, 'I have a booking for'), '바로 이 구절 뒤에 예약자 이름을 바로 이어 말해요.']),
    (2, None, ["'네, 이 층 사 호실이세요! 기차 여행은 어떠셨나요?' 손님의 이동 길이 편안했는지 안부를 여쭐 때는 과거형을 쓴", (None, 'How was your train trip'), '바로 이 다정한 질문으로 대화를 이어 가요.']),
    (3, None, ["'조용하고 쾌적했어요, 고마워요. 그런데 오늘따라 이 여행 가방이 아주 무겁게 느껴지네요.' 손에 전해지는 묵직한 무게감을 묘사할 때는 감각 동사를 써서", (None, 'feels very heavy'), '이렇게 자연스럽게 표현해요.']),
    (4, None, ["'제가 들어 드릴게요. 세상에, 여기 안에 돌멩이라도 챙겨 넣으셨나요?' 정중하게 짐을 대신 들어 드릴 때는", (None, 'Allow me'), '이어서 깜짝 놀란 마음을 예의 바르게 나타낼 때는', (None, 'Goodness'), '바로 이 감탄사를 가볍게 덧붙여요.']),
    (5, None, ["'원피스 몇 벌하고 악보, 그리고 제가 가장 아끼는 찻잔뿐인걸요!' 종이에 인쇄된 연주용 악보는 셀 수 없는 명사로 묶어", (None, 'sheet music'), '바로 이 표현으로 가리켜요.']),
    (6, None, ["'여기 사 호실 열쇠 있습니다. 아침 식사는 일곱 시 삼십 분부터 열 시까지예요.' 시각의 시와 분을 간단히 알려 줄 때는 숫자 두 개를 나란히 이어", (None, 'seven thirty'), '이렇게 읽으면 아주 깔끔해요.']),
    (7, None, ["'정말 좋네요. 방 창문은 거리 쪽을 향하나요, 아니면 안뜰 쪽을 향하나요?' 창문이 어느 방향을 마주 보고 있는지 물을 때는 분사 형태인", (None, 'facing the street'), '바로 이 표현을 써서 전망을 확인해요.']),
    (8, None, ["'안뜰 쪽이에요, 오래된 나무 바로 위쪽이죠. 아주 조용해요.' 무언가의 바로 위층 위치를 또렷하게 짚어 줄 때는 강조어를 더한", (None, 'right above'), '바로 이 두 단어가 꼭 알맞아요.']),
    (9, None, ["'딱 제가 바라던 곳이네요. 계단은 어디에 있나요?' 상대의 안내가 내 마음에 쏙 들었을 때는", (None, 'Just what I need'), '바로 이 한마디로 만족감을 품위 있게 전할 수 있어요.']),
    (10, None, ["'바로 이 아치형 통로를 지나가시면 돼요. 파란 가방은 제가 위층까지 들어 드릴게요.' 그 자리에서 기꺼이 돕겠다는 의지를 밝히는", (None, 'I will carry'), '그리고 위층 방향을 보태 주는 짧은 부사', (None, 'up'), '두 요소가 어우러져 든든한 안내가 돼요.']),
    (11, None, ["'두 분 모두 정말 고맙습니다.' 도움을 준 두 사람을 함께 챙겨 감사 인사를 건넬 때는", (None, 'both'), '바로 이 단어를 대명사 뒤에 넣은', (None, 'Thank you both'), '바로 이 표현이 무척 따뜻하게 들려요.']),
]
