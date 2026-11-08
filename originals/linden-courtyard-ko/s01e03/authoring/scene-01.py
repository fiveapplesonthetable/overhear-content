# Authoring module for linden-courtyard-ko-s01e03-scene-01.
ID = 'linden-courtyard-ko-s01e03-scene-01'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = 'Thirty-Five Minutes  (삼십오 분)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '린든 코트야드 여관의 칠 호실이 두 번 예약되었다는 사실에 아서는 잔뜩 당황하고 말아요. 침착한 해나와 든든한 그레이엄은 손님이 도착하기 전 삼십오 분 동안 삼 층 다락방을 멋지게 꾸며 보기로 합니다. 먼저 세 사람의 긴박한 대화를 편안하게 들어 보세요.'
OPENER = '그럼 방금 들은 프런트 데스크의 대화를 한 문장씩 차근차근 살펴볼까요.'
TRANSITION = '이제 자연스러운 속도로 장면 전체를 다시 한번 들어 보세요.'
OUTRO = '삼 층 다락방의 은색 열쇠를 손에 쥐고 세 사람이 힘차게 계단을 오르기 시작했어요. 과연 짧은 시간 안에 다락방이 근사한 객실로 변신할 수 있을까요. 곧 이어지는 다음 장면에서 확인해 봐요.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('arthur', 'Thirty-five minutes! He will write a terrible one star review!', '삼십오 분 남았어요! 그 손님이 별 하나짜리 끔찍한 후기를 남길 거예요!'),
    ('hannah', 'Take a deep breath, Arthur. Nobody has written anything yet.', '심호흡 크게 하세요, 아서. 아직 아무도 아무 글도 안 썼잖아요.'),
    ('graham', 'Here is the small silver key for the third floor attic door.', '여기 삼 층 다락방 문에 쓰는 작은 은색 열쇠가 있습니다.'),
    ('arthur', 'Does the attic even have a proper bed?', '다락방에 제대로 된 침대가 있기는 한가요?'),
    ('graham', 'Yes, a good wooden bed, a clean desk, and the best view in the house.', '네, 튼튼한 나무 침대와 깨끗한 책상, 그리고 이 건물에서 가장 멋진 전망이 있죠.'),
    ('hannah', 'Then why do we never rent it to guests?', '그런데 왜 우리는 그 방을 손님들에게 한 번도 내주지 않나요?'),
    ('graham', 'Because the stairs are narrow and Arthur keeps old lamp boxes there.', '계단이 좁은 데다 아서가 거기에 낡은 전등 상자들을 보관하거든요.'),
    ('arthur', 'Only three small boxes! Maybe four!', '작은 상자 딱 세 개뿐이에요! 어쩌면 네 개일지도 모르고요!'),
    ('hannah', 'We can move four boxes in five minutes. Let us go look right now!', '상자 네 개쯤은 오 분이면 옮길 수 있어요. 지금 당장 올라가서 확인해 봐요!'),
    ('graham', 'Up the stairs, turn left at the landing, last door at the top.', '계단으로 올라가서 층계참에서 왼쪽으로 돌면 맨 꼭대기 마지막 문입니다.'),
    ('arthur', 'I will bring clean white sheets from the linen closet!', '제가 린넨 벽장에서 깨끗한 흰 침대 시트를 가져올게요!'),
    ('hannah', 'Come on, race you to the third floor!', '어서요, 누가 삼 층에 먼저 도착하는지 시합해요!'),
]
WALK = [
    (0, None, ["'삼십오 분 남았어요! 그 손님이 별 하나짜리 끔찍한 후기를 남길 거예요!' 앞으로 벌어질 일을 걱정하며 단정 지어 말할 때는", (None, 'will write'), '이렇게 조동사와 동사원형을 나란히 붙여 미래의 행동을 나타내요.']),
    (1, None, ["'심호흡 크게 하세요, 아서. 아직 아무도 아무 글도 안 썼잖아요.' 당황한 상대의 마음을 차분히 가라앉혀 줄 때는", (None, 'Take a deep breath'), '바로 이 한마디로 숨을 깊이 들이쉬라고 다정하게 권해 보세요.']),
    (2, None, ["'여기 삼 층 다락방 문에 쓰는 작은 은색 열쇠가 있습니다.' 층수와 공간 이름을 차례로 겹쳐 문을 설명할 때는", (None, 'third floor attic door'), '이런 어순대로 명사를 차곡차곡 이어 붙이면 깔끔해요.']),
    (3, None, ["'다락방에 제대로 된 침대가 있기는 한가요?' 설마 그것마저 있을까 하고 의구심을 담아 되물을 때는", (None, 'even'), '짧은 강조 부사를 일반동사 바로 앞에 넣어 놀라움을 강조해요.']),
    (4, None, ["'네, 튼튼한 나무 침대와 깨끗한 책상, 그리고 이 건물에서 가장 멋진 전망이 있죠.' 집 안에서 으뜸가는 풍경을 자랑할 때는 최상급 구절인", (None, 'best view in the house'), '이런 표현으로 공간의 매력을 한껏 살려 말해요.']),
    (5, None, ["'그런데 왜 우리는 그 방을 손님들에게 한 번도 내주지 않나요?' 평소 전혀 하지 않는 일의 까닭을 궁금해할 때는", (None, 'why do we never rent'), '여기처럼 의문사 뒤에 빈도부사를 함께 넣어 질문해요.']),
    (6, None, ["'계단이 좁은 데다 아서가 거기에 낡은 전등 상자들을 보관하거든요.' 통로의 폭이 좁다는 상태를 묘사할 때는 복수 명사에 맞춰", (None, 'the stairs are narrow'), '이렇게 복수형 동사와 형용사를 짝지어 설명해요.']),
    (7, None, ["'작은 상자 딱 세 개뿐이에요! 어쩌면 네 개일지도 모르고요!' 방금 한 말에 살짝 자신이 없어 덧붙일 때는 문장 맨 앞에", (None, 'Maybe'), '방금 들은 단어를 가볍게 던져 추측의 느낌을 살려 줘요.']),
    (8, None, ["'상자 네 개쯤은 오 분이면 옮길 수 있어요. 지금 당장 올라가서 확인해 봐요!' 일상 대화에서 가서 직접 보자고 경쾌하게 제안할 때는", (None, 'go look'), '두 동사를 연결어 없이 나란히 붙여 경쾌하게 말해요.']),
    (9, None, ["'계단으로 올라가서 층계참에서 왼쪽으로 돌면 맨 꼭대기 마지막 문입니다.' 실내에서 길을 안내하며 방향을 꺾으라고 알려 줄 때는", (None, 'turn left at the landing'), '전치사로 정확한 지점을 짚어 주어 헷갈리지 않게 해요.']),
    (10, None, ["'제가 린넨 벽장에서 깨끗한 흰 침대 시트를 가져올게요!' 그 자리에서 기꺼이 내가 맡겠다고 자원할 때는", (None, 'I will bring'), '축약하지 않은 또렷한 어조로 든든한 의지를 전해 봐요.']),
    (11, None, ["'어서요, 누가 삼 층에 먼저 도착하는지 시합해요!' 주어를 생략하고 친구처럼 가볍게 달리기 내기를 걸 때는", (None, 'race you'), '짧고 활기찬 이 구절 하나로 유쾌한 분위기를 만들어요.']),
]
