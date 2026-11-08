# Authoring module for linden-courtyard-ko-s01e06-scene-08.
ID = 'linden-courtyard-ko-s01e06-scene-08'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 6
SCENE = 8
TITLE = 'Room Nine  (아홉 번째 방, 구 호실)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = '내일 아침 카페에 놓을 여분의 접이식 의자를 찾으러 지하 보일러실 뒤편에 내려갔던 그레이엄이 낡은 삼나무 상자 하나를 들고 올라와요. 먼지를 털어 낸 황동 명판 위에는 놀랍게도 구 호실이라는 글자가 새겨져 있습니다. 설레는 시즌 마지막 장면을 들어 보세요.'
OPENER = '새로운 수수께끼가 시작되는 마지막 대화를 하나씩 살펴볼까요.'
TRANSITION = '아홉 번째 황동 열쇠의 비밀을 상상하며 다시 한번 들어 보세요.'
OUTRO = '객실이 여덟 개뿐인 줄 알았던 여관 일 층 도면에 숨겨진 문이 그려져 있다니 가슴이 두근거리네요! 손전등을 챙겨 든 세 사람과 함께 해나의 두 번째 주도 힘차게 막을 올립니다. 다음 시즌에서 다시 만나요!'
CLOSING = ('graham', 'Until tomorrow!')
STORY = [
    ('hannah', 'Did you find the three folding chairs behind the boiler room, Graham?', '그레이엄, 보일러실 뒤편에서 접이식 의자 세 개는 찾으셨나요?'),
    ('graham', 'Found the chairs, and behind an old brick wall, I found this.', '의자들은 찾았고요, 오래된 벽돌 벽 뒤에서 이것도 발견했습니다.'),
    ('arthur', 'A small cedar chest? I have never seen that box in fifteen years!', '작은 삼나무 상자라고요? 십오 년 동안 저런 상자는 한 번도 본 적이 없어요!'),
    ('hannah', 'Brush the dust off the brass plate on top... wait, read that number!', '윗면 황동 명판에 쌓인 먼지를 좀 털어 내 봐요... 잠깐, 저 숫자 좀 읽어 보세요!'),
    ('arthur', "Let me pull my glasses down from my forehead... 'Room Nine'?!", '이마에서 안경을 좀 끌어 내려 보고요... 구 호실이라고요?!'),
    ('hannah', 'Graham, look at the wooden key board behind us: one, two, three, four, five, six, seven, eight!', '그레이엄, 우리 뒤쪽 나무 열쇠 걸이판을 보세요, 하나, 둘, 셋, 넷, 다섯, 여섯, 일곱, 여덟뿐이잖아요!'),
    ('arthur', 'This guesthouse has only ever had eight rooms! Where on earth is Room Nine?!', '이 여관에는 여태껏 객실이 여덟 개밖에 없었어요! 대체 구 호실은 어디에 있다는 거죠?!'),
    ('graham', 'Listen when I tilt the box. Something metal just slid inside.', '제가 상자를 기울일 때 소리를 들어 보세요. 금속으로 된 무언가가 방금 안에서 미끄러졌어요.'),
    ('hannah', 'There is a tiny keyhole on the front latch, and look taped underneath: an old brass key!', '앞쪽 걸쇠에 아주 작은 열쇠 구멍이 있고요, 바닥 밑에 테이프로 붙어 있는 것 좀 보세요, 낡은 황동 열쇠예요!'),
    ('arthur', 'A ninth brass key?! Do we open it tonight or wait until morning?!', '아홉 번째 황동 열쇠라고요?! 오늘 밤 당장 열어 볼까요, 아니면 아침까지 기다릴까요?!'),
    ('graham', 'Look at the folded blueprint sticking out of the hinge. There is a hidden door drawn on this floor!', '경첩 틈으로 삐죽 나와 있는 접힌 설계 도면을 보세요. 바로 이 층에 숨겨진 문이 그려져 있어요!'),
    ('hannah', 'Grab the flashlight, both of you. My second week starts right now!', '두 분 다 손전등 챙기세요. 저의 두 번째 주 근무는 바로 지금 시작이에요!'),
]
WALK = [
    (0, None, ["'그레이엄, 보일러실 뒤편에서 접이식 의자 세 개는 찾으셨나요?' 필요할 때 폈다가 접어서 보관하는 실용적인 의자는 분사형 수식어를 붙인", (None, 'folding chairs'), '복합 명사로 자연스럽게 가리켜요.']),
    (1, None, ["'의자들은 찾았고요, 오래된 벽돌 벽 뒤에서 이것도 발견했습니다.' 일상 대화에서 주어를 가볍게 생략하고 과거형 동사로 곧장 대답을 여는", (None, 'Found the chairs'), '어순이 담담한 그레이엄의 말투를 잘 살려 줘요.']),
    (2, None, ["'작은 삼나무 상자라고요? 십오 년 동안 저런 상자는 한 번도 본 적이 없어요!' 지금까지 살면서 단 한 차례도 목격한 경험이 없음을 강조할 때는 현재완료 부정형", (None, 'I have never seen'), '구문으로 깜짝 놀란 반응을 보여 줘요.']),
    (3, None, ["'윗면 황동 명판에 쌓인 먼지를 좀 털어 내 봐요... 잠깐, 저 숫자 좀 읽어 보세요!' 표면에 내려앉은 먼지를 손이나 솔로 쓸어 떨어뜨릴 때는 분리의 전치사를 더한", (None, 'Brush the dust off'), '동사구로 호기심 어린 행동을 지시해요.']),
    (4, None, ["'이마에서 안경을 좀 끌어 내려 보고요... 구 호실이라고요?!' 이마 위에 올려 두었던 안경을 코 쪽으로 끌어 내리는 동작은 구동사에 출처 전치사를 이은", (None, 'pull my glasses down from'), '표현으로 아서 특유의 버릇을 재미있게 묘사해요.']),
    (5, None, ["'그레이엄, 우리 뒤쪽 나무 열쇠 걸이판을 보세요, 하나, 둘, 셋, 넷, 다섯, 여섯, 일곱, 여덟뿐이잖아요!' 서 있는 사람들의 등 뒤편 위치를 손쉽게 가리킬 때는 전치사구", (None, 'behind us'), '두 단어를 명사 뒤에 붙여 시선을 돌리게 해요.']),
    (6, None, ["'이 여관에는 여태껏 객실이 여덟 개밖에 없었어요! 대체 구 호실은 어디에 있다는 거죠?!' 도대체 어디냐며 놀라움과 의문을 강하게 터뜨릴 때는 의문사 뒤에 강조구를 붙인", (None, 'Where on earth'), '표현이 극적인 감탄을 더해 줘요.']),
    (7, None, ["'제가 상자를 기울일 때 소리를 들어 보세요. 금속으로 된 무언가가 방금 안에서 미끄러졌어요.' 부정대명사는 수식어가 항상 뒤에서 꾸며 주므로 재질을 나타내는 단어를 뒤에 둔", (None, 'Something metal'), '어순으로 상자 속 물체의 단서를 전해요.']),
    (8, None, ["'앞쪽 걸쇠에 아주 작은 열쇠 구멍이 있고요, 바닥 밑에 테이프로 붙어 있는 것 좀 보세요, 낡은 황동 열쇠예요!' 열쇠를 꽂아 넣는 작은 구멍은 두 명사가 하나로 합쳐진 복합어", (None, 'keyhole'), '단어로 깔끔하게 말해요.']),
    (9, None, ["'아홉 번째 황동 열쇠라고요?! 오늘 밤 당장 열어 볼까요, 아니면 아침까지 기다릴까요?!' 여덟 개 다음에 이어지는 아홉째 순서를 나타낼 때는 철자에 주의해야 하는 서수", (None, 'ninth'), '단어를 써서 숨겨진 열쇠 번호를 짚어요.']),
    (10, None, ["'경첩 틈으로 삐죽 나와 있는 접힌 설계 도면을 보세요. 바로 이 층에 숨겨진 문이 그려져 있어요!' 틈새 밖으로 일부분이 삐져나와 있는 상태를 생생히 묘사할 때는 분사구", (None, 'sticking out of'), '표현을 명사 뒤에 붙여 결정적 단서를 비춰 줘요.']),
    (11, None, ["'두 분 다 손전등 챙기세요. 저의 두 번째 주 근무는 바로 지금 시작이에요!' 새로운 모험이나 일정이 지금 이 순간 막을 올린다고 힘차게 외칠 때는 현재시제", (None, 'starts right now'), '세 단어로 생동감 넘치는 마무리를 장식해요.']),
]
