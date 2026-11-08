# Authoring module for linden-courtyard-ko-s01e04-scene-06.
ID = 'linden-courtyard-ko-s01e04-scene-06'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 4
SCENE = 6
TITLE = 'The Acoustic Architect  (음향 건축가)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '안뜰 나무 아래에서 케일럽이 수첩 속 스케치를 펼쳐 보이며 자신이 호텔 평가원이 아니라 소리를 연구하는 음향 건축가라고 밝혀요. 그러다 어린 시절 이 동네에 살았다는 이야기와 함께 금요일이라는 단어를 꺼내자 테사가 깜짝 놀랍니다. 대화를 들어 보세요.'
OPENER = '안뜰에서 오해를 풀며 나눈 흥미로운 대화를 한 줄씩 살펴볼까요.'
TRANSITION = '그럼 비밀에 한 걸음 다가선 이 장면을 자연스럽게 다시 들어 보세요.'
OUTRO = '케일럽이 어릴 적 두 거리 건너편에 살았고 금요일이 중요한 날이라고 말했어요. 월요일 기차에서 온 파란 가방의 금요일 정오 약속과 무슨 관련이 있을까요. 다음 장면에서 단서가 이어집니다.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('caleb', 'Look closely at this page. It measures decibels and quietness, not hotel stars!', '이 쪽을 가까이서 자세히 보세요. 호텔 별점이 아니라 데시벨과 정숙도를 잰 기록이에요!'),
    ('hannah', "Decibels? So 'nine out of ten' was not a review of my front desk?", '데시벨이라고요? 그럼 십 점 만점에 구 점이 제 프런트 응대 평가가 아니었나요?'),
    ('caleb', 'Well, your front desk deserves ten! Honestly, though, I am an acoustic architect.', '글쎄요, 해나 씨 프런트는 십 점 받을 자격이 충분하죠! 하지만 솔직히 저는 음향 건축가예요.'),
    ('tessa', 'An acoustic architect! Do you design concert halls?', '음향 건축가시군요! 연주회장을 설계하시나요?'),
    ('caleb', 'Small libraries and courtyards, mostly. I measure how old stone walls block street noise.', '주로 작은 도서관이나 안뜰을 맡아요. 오래된 돌담이 거리 소음을 어떻게 막는지 측정하죠.'),
    ('hannah', 'That is why you listened for cars up in the attic last night!', '그래서 어젯밤 위층 다락방에서 차 소리가 나는지 귀 기울여 들으셨군요!'),
    ('caleb', 'Exactly. Outside on the avenue it is loud, yet inside this courtyard you hear leaves and birds.', '맞아요. 바깥 큰길은 시끄럽지만, 이 안뜰 안에서는 나뭇잎과 새소리가 들리잖아요.'),
    ('tessa', 'Wait until Arthur hears he panicked all night over decibels!', '자기가 밤새 데시벨 때문에 전전긍긍했다는 걸 아서가 들으면 어떨지 기대되네요!'),
    ('caleb', 'Truthfully, I also chose this neighborhood for an old family reason.', '사실은 오래된 가족 사연 때문에 이 동네를 고른 것도 있어요.'),
    ('hannah', 'Oh? Did your family live near here once?', '어머, 그래요? 예전에 가족분들이 이 근처에 사셨나요?'),
    ('caleb', 'Two streets away, when I was small. Friday is... an important day for me.', '두 거리 건너편에요, 제가 어렸을 때요. 금요일이 저한테는 중요한 날이거든요.'),
    ('tessa', 'Wait, did he just say Friday?!', '잠깐만요, 방금 그분이 금요일이라고 하셨나요?!'),
]
WALK = [
    (0, None, ["'이 쪽을 가까이서 자세히 보세요. 호텔 별점이 아니라 데시벨과 정숙도를 잰 기록이에요!' 눈을 가까이 대고 세밀하게 들여다보라고 권유할 때는 동사 뒤에", (None, 'Look closely'), '부사 형태를 붙여 세심하고 면밀하게 살펴보라는 뜻을 전해요.']),
    (1, None, ["'데시벨이라고요? 그럼 십 점 만점에 구 점이 제 프런트 응대 평가가 아니었나요?' 자기가 짐작했던 후기나 평점이 아니었는지 확인하며 안도하는 과거 부정 구문이", (None, 'was not a review'), '명사 앞에 부정관사를 넣어 한 건의 평가 기록이 아니었음을 밝혀요.']),
    (2, None, ["'글쎄요, 해나 씨 프런트는 십 점 받을 자격이 충분하죠! 하지만 솔직히 저는 음향 건축가예요.' 앞말을 인정하면서도 화제를 살짝 틀어 진짜 사실을 덧붙일 때 요긴한 단어가", (None, 'though'), '문장 중간이나 끝에 가볍게 끼어들어 구어체의 부드러운 반전을 만들어요.']),
    (3, None, ["'음향 건축가시군요! 연주회장을 설계하시나요?' 음악 공연이 열리는 대규모 실내 공연장을 일상적으로 가리키는 복수 명사구가", (None, 'concert halls'), '특정한 한 곳이 아니라 일반적인 건축 분야를 묻기 때문에 복수형으로 썼어요.']),
    (4, None, ["'주로 작은 도서관이나 안뜰을 맡아요. 오래된 돌담이 거리 소음을 어떻게 막는지 측정하죠.' 대다수의 경우나 주된 작업 분야를 간결하게 요약해 덧붙일 때 쓰는 부사가", (None, 'mostly'), '명사구 뒤에 쉼표와 함께 놓여 대개 그러하다는 뉘앙스를 더해 줘요.']),
    (5, None, ["'그래서 어젯밤 위층 다락방에서 차 소리가 나는지 귀 기울여 들으셨군요!' 앞선 설명 덕분에 비로소 이유를 깨달았을 때는", (None, 'That is why'), '그리고 혹시 차 소리가 들릴까 집중해 귀를 기울였다는 동작은', (None, 'listened for cars'), '목적을 뜻하는 전치사를 결합해 특정 소리를 찾으려 애썼음을 나타내요.']),
    (6, None, ["'맞아요. 바깥 큰길은 시끄럽지만, 이 안뜰 안에서는 나뭇잎과 새소리가 들리잖아요.' 두 공간의 상반된 분위기를 깔끔하고 세련되게 대조해 이어 주는 접속사가", (None, 'yet'), '일상의 반전 접속사보다 한결 차분하고 지적인 느낌으로 문장을 연결해요.']),
    (7, None, ["'자기가 밤새 데시벨 때문에 전전긍긍했다는 걸 아서가 들으면 어떨지 기대되네요!' 누군가 이 소식을 알게 될 순간이 몹시 기다려진다고 재치 있게 말할 때는", (None, 'Wait until Arthur hears'), '시간 접속사 뒤에 현재시제를 써서 곧 벌어질 재미있는 반응을 상상해요.']),
    (8, None, ["'사실은 오래된 가족 사연 때문에 이 동네를 고른 것도 있어요.' 여러 선택지 가운데 마음을 정해 선택했다는 동사의 불규칙 과거형이", (None, 'chose'), '모음 하나가 줄어든 철자와 발음을 함께 눈여겨보시면 좋아요.']),
    (9, None, ["'어머, 그래요? 예전에 가족분들이 이 근처에 사셨나요?' 한 번이라는 횟수 말고 과거의 어느 한때를 아련하게 가리킬 때도 쓰는 부사가", (None, 'once'), '문장 맨 끝에서 옛 시절의 기억을 조심스럽게 불러내 줘요.']),
    (10, None, ["'두 거리 건너편에요, 제가 어렸을 때요. 금요일이 저한테는 중요한 날이거든요.' 어린 시절을 회상할 때 나이 대신 몸집이 작았다는 형용사로 정겹게 표현한 절이", (None, 'when I was small'), '원어민들이 유년기를 떠올릴 때 참 따뜻하고 흔하게 쓰는 구절이에요.']),
    (11, None, ["'잠깐만요, 방금 그분이 금요일이라고 하셨나요?!' 귀를 의심할 만큼 놀라운 단어를 막 들었을 때 옆 사람에게 확인하는 과거 의문문이", (None, 'did he just say'), '조동사와 주어 뒤에 부사를 바짝 붙여 방금 나온 말임을 강조해요.']),
]
