# Authoring module for linden-courtyard-ko-s01e05-scene-05.
ID = 'linden-courtyard-ko-s01e05-scene-05'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 5
SCENE = 5
TITLE = 'Simple Words First  (먼저 건네는 소박한 진심)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = '열한 시 사십 분의 안뜰에서 케일럽이 종이 한 장을 쥐고 딱딱한 사과 연설을 연습하고 있어요. 해나는 시원한 물 한 모금을 건네며 길고 복잡한 변명 대신 진심이 담긴 짧은 세 문장을 골라 줍니다. 두 사람의 대화를 들어 보세요.'
OPENER = '마음을 추스르는 두 사람의 대화를 한 문장씩 들여다볼까요.'
TRANSITION = '짧고 솔직한 세 마디를 떠올리며 대화를 다시 들어 보세요.'
OUTRO = '열아홉 가지 변명보다 따뜻한 차와 레몬 케이크를 권하는 세 마디가 훨씬 큰 울림을 주지요. 주머니 속에 종이를 접어 넣은 케일럽의 표정도 한결 부드러워졌어요. 다음 장면으로 넘어가 볼까요.'
CLOSING = ('caleb', 'Take care!')
STORY = [
    ('hannah', 'Here, drink a sip of cool water, Caleb. What is on that paper?', '자, 시원한 물 한 모금 마셔요, 케일럽. 그 종이에는 뭐가 적혀 있나요?'),
    ('caleb', 'A five minute speech explaining nineteen reasons why we were both wrong in April.', '사월에 우리 둘 다 잘못했던 열아홉 가지 이유를 설명하는 오 분짜리 연설문이에요.'),
    ('hannah', 'Nineteen reasons?! Are you welcoming your brother or reading a train schedule?', '열아홉 가지 이유라고요?! 형님을 반갑게 맞이하려는 거예요, 아니면 기차 시간표를 읽으려는 거예요?'),
    ('caleb', 'When I get nervous, my sentences grow very long and formal!', '저는 긴장하면 문장이 아주 길고 딱딱해지거든요!'),
    ('hannah', 'Fold that paper and put it in your pocket right now.', '당장 그 종이는 접어서 주머니 속에 넣어 두세요.'),
    ('caleb', 'Without my notes, what do I say when he walks through that gate?', '메모도 없이 형이 저 대문을 통과해 걸어 들어오면 무슨 말을 하죠?'),
    ('hannah', "Start with three short sentences. First: 'Hello, Owen, thank you for coming.'", '짧은 문장 세 개로 시작해요. 첫째, 안녕하세요, 오언 형, 와 줘서 고마워요.'),
    ('caleb', "'Hello, Owen, thank you for coming.' Okay, I can remember that.", '안녕하세요, 오언 형, 와 줘서 고마워요. 좋아요, 그건 기억할 수 있겠어요.'),
    ('hannah', "Second: 'I missed you these three years.'", '둘째, 지난 삼 년 동안 형이 참 보고 싶었어요.'),
    ('caleb', "'I missed you these three years.' Honest and clear. And third?", '지난 삼 년 동안 형이 참 보고 싶었어요. 솔직하고 분명하네요. 그럼 셋째는요?'),
    ('hannah', "'Sit down, there is hot tea and Friday lemon cake.'", '여기 앉아요, 따뜻한 차와 금요일 레몬 케이크가 있어요.'),
    ('caleb', 'Tea and lemon cake! Hannah, you should open a school for nervous brothers.', '차와 레몬 케이크라니! 해나, 긴장한 동생들을 위한 학교를 하나 차려야겠어요.'),
]
WALK = [
    (0, None, ["'자, 시원한 물 한 모금 마셔요, 케일럽. 그 종이에는 뭐가 적혀 있나요?' 종이나 화면 위에 적힌 내용을 물을 때는 표면 접촉의 전치사를 쓴", (None, 'on that paper'), '구절로 손에 든 메모지를 가리켜요.']),
    (1, None, ["'사월에 우리 둘 다 잘못했던 열아홉 가지 이유를 설명하는 오 분짜리 연설문이에요.' 숫자와 시간 단위가 명사 앞에서 형용사처럼 쓰일 때는 단수형을 유지한", (None, 'five minute speech'), '형태로 길이를 깔끔하게 수식해요.']),
    (2, None, ["'열아홉 가지 이유라고요?! 형님을 반갑게 맞이하려는 거예요, 아니면 기차 시간표를 읽으려는 거예요?' 상대의 현재 의도를 가볍게 꼬집어 물을 때는 진행형 의문문", (None, 'Are you welcoming'), '어순으로 두 행동을 재치 있게 대비시켜요.']),
    (3, None, ["'저는 긴장하면 문장이 아주 길고 딱딱해지거든요!' 마음이 초조해지는 변화를 나타내는", (None, 'get nervous'), '뒤이어 문장이 점점 길어진다는 상태 변화의', (None, 'grow very long'), '두 연결동사가 나란히 자연스러운 흐름을 만들어요.']),
    (4, None, ["'당장 그 종이는 접어서 주머니 속에 넣어 두세요.' 손에 든 종이를 반듯하게 접으라고 권할 때는 동사원형으로 문을 여는", (None, 'Fold that paper'), '명령문으로 단호하고 든든하게 조언해요.']),
    (5, None, ["'메모도 없이 형이 저 대문을 통과해 걸어 들어오면 무슨 말을 하죠?' 문이나 통로를 지나 안쪽으로 들어오는 움직임은 시간 접속사 뒤에", (None, 'when he walks through'), '현재시제를 써서 다가올 순간을 그려요.']),
    (6, None, ["'짧은 문장 세 개로 시작해요. 첫째, 안녕하세요, 오언 형, 와 줘서 고마워요.' 찾아와 준 상대에게 건네는 가장 다정한 첫인사는 전치사 뒤에 동명사를 둔", (None, 'thank you for coming'), '표현 하나로 충분한 진심이 전해져요.']),
    (7, None, ["'안녕하세요, 오언 형, 와 줘서 고마워요. 좋아요, 그건 기억할 수 있겠어요.' 방금 들은 문장을 충분히 외울 수 있다고 스스로 다독일 때는 조동사를 넣은", (None, 'I can remember that'), '짧은 다짐으로 자신감을 되찾아요.']),
    (8, None, ["'둘째, 지난 삼 년 동안 형이 참 보고 싶었어요.' 떨어져 지낸 시간 동안 누군가를 그리워했다는 속마음은 과거형 동사를 쓴", (None, 'I missed you'), '세 단어로 꾸밈없이 고백할 수 있어요.']),
    (9, None, ["'지난 삼 년 동안 형이 참 보고 싶었어요. 솔직하고 분명하네요. 그럼 셋째는요?' 앞에서 첫째와 둘째를 들은 뒤 마지막 순서를 재촉해 물을 때는", (None, 'And third'), '두 단어만 가볍게 올려 물어보면 자연스러워요.']),
    (10, None, ["'여기 앉아요, 따뜻한 차와 금요일 레몬 케이크가 있어요.' 어색하게 서 있는 상대에게 자리를 권할 때는 친근한 구동사", (None, 'Sit down'), '한마디로 편안한 분위기를 열어 주어요.']),
    (11, None, ["'차와 레몬 케이크라니! 해나, 긴장한 동생들을 위한 학교를 하나 차려야겠어요.' 고마운 마음에 농담 섞인 제안을 건넬 때는 조동사를 활용한", (None, 'you should open'), '구절로 해나의 지혜를 재치 있게 칭찬해요.']),
]
