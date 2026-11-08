# Authoring module for linden-courtyard-ko-s01e01-scene-07.
ID = 'linden-courtyard-ko-s01e01-scene-07'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 1
SCENE = 7
TITLE = 'Tea and a Warm Cardigan  (따뜻한 차와 포근한 가디건)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'tessa': 'Tessa', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = '테사는 놀란 에블린 선생님께 꿀을 탄 뜨거운 민트차와 한 번도 입지 않은 깨끗한 울 가디건을 건네드립니다. 그레이엄은 주인을 모르는 다른 남색 가방을 수하물 벽장에 안전하게 잠가 두었어요. 다정한 저녁 대화를 들어 보세요.'
OPENER = '이제 마음을 녹여 주는 표현들을 한 문장씩 함께 살펴볼까요.'
TRANSITION = '따스한 저녁 장면을 처음부터 끝까지 다시 들어 보세요.'
OUTRO = '여관 식구들의 세심한 배려 덕분에 에블린 선생님도 비로소 따뜻한 미소를 되찾고 편안한 밤을 맞이하게 되었어요. 하지만 오늘 밤 이야기는 아직 끝나지 않았답니다. 다음 장면에서 확인해 보세요.'
CLOSING = ('tessa', 'Good night!')
STORY = [
    ('tessa', "Here you are, ma'am: hot mint tea and honey.", '여기 있습니다, 선생님. 꿀을 곁들인 뜨거운 민트차예요.'),
    ('evelyn', 'Oh, thank you, Tessa. My hands were cold from the shock!', '아, 고마워요, 테사. 너무 놀라서 두 손이 다 차가웠거든요!'),
    ('tessa', 'And look, this soft wool cardigan is clean and never worn. Try it on.', '그리고 이것 보세요, 이 부드러운 울 가디건은 깨끗한 새 옷이에요. 한번 입어 보세요.'),
    ('evelyn', 'Are you sure? It looks lovely and warm!', '정말 괜찮겠어요? 참 예쁘고 따뜻해 보이네요!'),
    ('graham', "It fits you very well, ma'am.", '선생님께 아주 잘 어울리십니다.'),
    ('evelyn', 'You good people are saving my whole trip.', '친절한 여러분이 제 여행 전체를 살려 주고 계시네요.'),
    ('tessa', 'A traveler cannot sit upstairs sad on her first evening in Portland!', '포틀랜드에서의 첫날 저녁에 여행객이 위층에 슬프게 앉아 계시면 안 되죠!'),
    ('graham', 'I locked the other blue suitcase safely in our luggage closet.', '다른 파란 여행 가방은 저희 수하물 벽장 안에 안전하게 잠가 두었습니다.'),
    ('evelyn', 'Thank you, Graham. That little wooden train inside looked old and precious.', '고마워요, 그레이엄. 그 안에 있던 작은 나무 기차는 오래되고 소중한 물건 같았어요.'),
    ('tessa', 'Whoever owns it will surely look for it soon.', '그 가방 주인이 누구든 분명히 곧 찾으러 나설 거예요.'),
    ('evelyn', 'I think I will sleep well tonight after all.', '덕분에 결국 오늘 밤에는 푹 잘 수 있을 것 같네요.'),
    ('graham', "Rest well, ma'am. Ring down if you need anything.", '편안히 쉬세요, 선생님. 필요한 것이 있으시면 아래로 벨을 눌러 주세요.'),
]
WALK = [
    (0, None, ["'여기 있습니다, 선생님. 꿀을 곁들인 뜨거운 민트차예요.' 차나 물건을 두 손으로 건네며 여기 있다고 말할 때는", (None, 'Here you are'), '여기 쓰인 이 정중한 인사가 어떤 자리에서나 자연스러워요.']),
    (1, None, ["'아, 고마워요, 테사. 너무 놀라서 두 손이 다 차가웠거든요!' 양손을 가리키는 복수 주어에 맞춰 과거 비 동사도 복수형을 쓴", (None, 'My hands were cold'), '여기 쓰인 이 문장으로 조금 전까지 손이 시렸던 상태를 설명해요.']),
    (2, None, ["'그리고 이것 보세요, 이 부드러운 울 가디건은 깨끗한 새 옷이에요. 한번 입어 보세요.' 옷을 시험 삼아 걸쳐 보라고 권할 때는 대명사를 구동사 가운데에 넣은", (None, 'Try it on'), '바로 이 어순으로 말해야 자연스러워요.']),
    (3, None, ["'정말 괜찮겠어요? 참 예쁘고 따뜻해 보이네요!' 눈으로 보기에 참 사랑스럽고 좋아 보인다고 칭찬할 때는", (None, 'It looks lovely'), '이렇게 감각 동사 뒤에 형용사를 나란히 이어 줘요.']),
    (4, None, ["'선생님께 아주 잘 어울리십니다.' 옷의 치수와 품이 입은 사람에게 꼭 맞을 때는", (None, 'It fits you'), '여기 쓰인 이 간결한 세 단어로 훌륭한 칭찬을 건넬 수 있어요.']),
    (5, None, ["'친절한 여러분이 제 여행 전체를 살려 주고 계시네요.' 고마운 사람들을 다정하게 높여 부를 때는 대명사 뒤에 명사구를 바로 붙인", (None, 'You good people'), '이런 따뜻한 호칭 표현을 쓰기도 해요.']),
    (6, None, ["'포틀랜드에서의 첫날 저녁에 여행객이 위층에 슬프게 앉아 계시면 안 되죠!' 위층이라는 공간 부사", (None, 'upstairs'), '여기 쓰인 이 단어는 그 자체에 장소의 뜻이 담겨 있어 앞에 전치사를 붙이지 않아요.']),
    (7, None, ["'다른 파란 여행 가방은 저희 수하물 벽장 안에 안전하게 잠가 두었습니다.' 열쇠로 단단히 채워 보관했다는 완료 동작은 규칙 과거형인", (None, 'I locked'), '이렇게 분명하게 알려 드려요.']),
    (8, None, ["'고마워요, 그레이엄. 그 안에 있던 작은 나무 기차는 오래되고 소중한 물건 같았어요.' 값어치를 매길 수 없을 만큼 아끼고 귀중한 느낌은", (None, 'precious'), '바로 이 형용사가 깊이 있게 담아내요.']),
    (9, None, ["'그 가방 주인이 누구든 분명히 곧 찾으러 나설 거예요.' 정체를 모르는 주인을 가리키는", (None, 'Whoever'), '그리고 무언가를 수소문해 찾는다는 구동사', (None, 'look for'), '두 표현이 만나 든든한 추측을 완성해요.']),
    (10, None, ["'덕분에 결국 오늘 밤에는 푹 잘 수 있을 것 같네요.' 우여곡절이 있었지만 결과적으로는 괜찮아졌다고 마무리할 때 문장 끝에", (None, 'after all'), '여기 쓰인 이 두 단어를 덧붙이면 여운이 부드러워져요.']),
    (11, None, ["'편안히 쉬세요, 선생님. 필요한 것이 있으시면 아래로 벨을 눌러 주세요.' 숙소 프런트에서 손님께 건네는 가장 든든한 맺음말인", (None, 'if you need anything'), '여기 쓰인 이 조건절도 입에 익혀 두면 무척 유용해요.']),
]
