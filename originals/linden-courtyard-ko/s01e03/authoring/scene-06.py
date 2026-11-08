# Authoring module for linden-courtyard-ko-s01e03-scene-06.
ID = 'linden-courtyard-ko-s01e03-scene-06'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 3
SCENE = 6
TITLE = 'A Five-Star Sigh of Relief  (별 다섯 개짜리 안도의 한숨)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '아래층 프런트로 내려온 해나와 테사에게 아서가 결과를 묻고, 세 사람은 함께 기뻐해요. 그런데 카운터 위에 놓인 케일럽의 가죽 수첩이 우연히 펼쳐지면서 정숙도 점수가 적힌 뜻밖의 메모를 보게 됩니다. 장면을 들어 보세요.'
OPENER = '카운터에서 벌어진 흥미진진한 대화를 한 줄씩 함께 따라가 볼까요.'
TRANSITION = '그럼 놀라움이 이어지는 장면 전체를 자연스러운 흐름으로 다시 들어 보세요.'
OUTRO = '케일럽이 포틀랜드 여행 안내서 평가원일지도 모른다는 추측에 세 사람이 깜짝 놀랐어요. 설상가상으로 수첩을 돌려주러 가려는 순간 배관에서 요란한 쇳소리까지 들려오네요. 곧 다음 장면에서 만나요.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('arthur', 'Well? Did he shout? Did he ask for his money back?', '자, 어떻게 됐어요? 손님이 소리 지르던가요? 환불해 달라고 하던가요?'),
    ('hannah', 'Neither! He loved the quiet roof beams and thanked us.', '둘 다 아니에요! 조용한 지붕 들보를 아주 마음에 들어 하시며 고마워하셨어요.'),
    ('arthur', 'Hannah, you have a gift for hospitality! My blood pressure is saved!', '해나, 당신은 손님 환대에 타고난 재능이 있어요! 덕분에 제 혈압이 살았네요!'),
    ('tessa', 'He even finished every drop of vegetable soup before going up.', '올라가시기 전에 채소 수프도 한 방울 남김없이 다 비우셨는걸요.'),
    ('hannah', 'Wait, whose small brown leather notebook is this on the counter?', '잠깐만요, 카운터 위에 있는 이 작은 갈색 가죽 수첩은 누구 거죠?'),
    ('tessa', 'Caleb set it down when he took the dry towel from me!', '케일럽 씨가 저한테서 마른 수건을 받아 들 때 내려놓으셨어요!'),
    ('arthur', 'Do not snoop, of course... wait, it fell open to the middle page!', '물론 남의 걸 엿보면 안 되죠. 어라, 가운데 쪽이 저절로 펼쳐져 버렸네요!'),
    ('hannah', 'Why are there neat pencil drawings of three guesthouses on our street?', '왜 우리 거리에 있는 여관 세 곳의 깔끔한 연필 그림이 그려져 있을까요?'),
    ('tessa', "Look at the words beside ours: 'Courtyard width, street noise, quiet score: nine out of ten!'", '우리 여관 옆에 적힌 글씨 좀 봐요, 안뜰 너비, 거리 소음, 정숙도 점수 십 점 만점에 구 점!'),
    ('arthur', 'Nine out of ten?! Nobody measures lobbies unless...', '십 점 만점에 구 점이라고요? 아무도 로비를 재지 않아요, 혹시 이게 아니라면 말이죠!'),
    ('tessa', 'Unless he writes for the annual Portland Travel Guide!', '그분이 해마다 나오는 포틀랜드 여행 안내서 필진이 아니라면 말이죠!'),
    ('hannah', 'Quick, close it! Let us take it upstairs... wait, what is that loud clanking sound?', '얼른 덮어요! 위층으로 가져다드립시다. 잠깐, 저 요란한 쇳소리는 뭐죠?'),
]
WALK = [
    (0, None, ["'자, 어떻게 됐어요? 손님이 소리 지르던가요? 환불해 달라고 하던가요?' 냈던 돈을 도로 돌려달라고 요구한다는 일상적인 표현은", (None, 'ask for his money back'), '어려운 한자어 대신 쉬운 단어들을 조합해 생생하게 나타내요.']),
    (1, None, ["'둘 다 아니에요! 조용한 지붕 들보를 아주 마음에 들어 하시며 고마워하셨어요.' 상대가 물어본 두 가지 경우를 한꺼번에 모두 부정할 때는", (None, 'Neither'), '단 한 단어만 힘주어 말해도 두 질문에 깔끔한 답이 돼요.']),
    (2, None, ["'해나, 당신은 손님 환대에 타고난 재능이 있어요! 덕분에 제 혈압이 살았네요!' 어떤 분야에 남다른 소질이나 천부적인 감각이 있다고 칭찬할 때는", (None, 'have a gift for'), '선물이라는 명사를 재능의 뜻으로 써서 따뜻한 격려를 건네요.']),
    (3, None, ["'올라가시기 전에 채소 수프도 한 방울 남김없이 다 비우셨는걸요.' 어떤 행동을 하기 이전 시점을 간결하게 덧붙일 때는", (None, 'before going up'), '주어를 생략하고 분사나 동명사 형태로 가볍게 이어 주면 자연스러워요.']),
    (4, None, ["'잠깐만요, 카운터 위에 있는 이 작은 갈색 가죽 수첩은 누구 거죠?' 물건의 주인이 누구인지 궁금해하며 소유자를 물어볼 때는", (None, 'whose'), '소유격 의문사를 명사구 맨 앞에 세워 한 덩어리로 질문해요.']),
    (5, None, ["'케일럽 씨가 저한테서 마른 수건을 받아 들 때 내려놓으셨어요!' 손에 들고 있던 물건을 탁자나 바닥 위에 살포시 내려놓았다는 말은", (None, 'set it down'), '대명사를 구동사 한가운데 끼워 넣어 자연스러운 어순을 완성해요.']),
    (6, None, ["'물론 남의 걸 엿보면 안 되죠. 어라, 가운데 쪽이 저절로 펼쳐져 버렸네요!' 책이나 수첩이 툭 떨어지며 저절로 활짝 열린 상태를 묘사할 때는", (None, 'fell open'), '과거형 동사 뒤에 형용사를 바로 붙여 결과 상태를 한눈에 보여 줘요.']),
    (7, None, ["'왜 우리 거리에 있는 여관 세 곳의 깔끔한 연필 그림이 그려져 있을까요?' 무언가가 존재하는 이유를 물으며 문장을 시작할 때는", (None, 'Why are there'), '뒤에 오는 복수 명사에 맞춰 복수형 동사를 먼저 꺼내어 질문해요.']),
    (8, None, ["'우리 여관 옆에 적힌 글씨 좀 봐요, 안뜰 너비, 거리 소음, 정숙도 점수 십 점 만점에 구 점!' 전체 기준점 가운데 몇 점인지를 숫자로 또렷이 밝힐 때는", (None, 'nine out of ten'), '전치사구를 사이에 두어 만점 대비 점수를 알기 쉽게 표현해요.']),
    (9, None, ["'십 점 만점에 구 점이라고요? 아무도 로비를 재지 않아요, 혹시 이게 아니라면 말이죠!' 유일한 예외 조건을 덧붙이며 말끝을 의미심장하게 흐릴 때는", (None, 'unless'), '만약 무엇이 아니라면이라는 접속사 하나로 긴장감을 확 끌어올려요.']),
    (10, None, ["'그분이 해마다 나오는 포틀랜드 여행 안내서 필진이 아니라면 말이죠!' 앞사람이 남긴 접속사를 그대로 받아 추리를 이어 나갈 때는", (None, 'Unless he writes'), '현재시제 동사를 써서 그 사람의 직업이나 평소의 일을 짐작해요.']),
    (11, None, ["'얼른 덮어요! 위층으로 가져다드립시다. 잠깐, 저 요란한 쇳소리는 뭐죠?' 금속끼리 둔탁하게 부딪히며 탕탕 울리는 소리를 생생히 묘사할 때는", (None, 'clanking sound'), '소리를 흉내 낸 분사 형용사를 붙여 현장감을 또렷하게 살려요.']),
]
