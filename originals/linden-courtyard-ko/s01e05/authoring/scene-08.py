# Authoring module for linden-courtyard-ko-s01e05-scene-08.
ID = 'linden-courtyard-ko-s01e05-scene-08'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 5
SCENE = 8
TITLE = 'The Red-Stamped Letter  (빨간 도장이 찍힌 편지)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '창밖 안뜰에서는 오언과 케일럽이 나무 아래 마주 서서 감격스러운 재회를 나누고 있어요. 하지만 로비 안에서 건물주의 등기 우편을 뜯어 본 아서는 상업용 사무실 매각 통지서를 읽고 얼굴이 하얗게 질립니다. 극적인 대비가 담긴 마지막 장면을 들어 보세요.'
OPENER = '기쁨과 위기가 교차하는 로비 안 대화를 차근차근 살펴볼까요.'
TRANSITION = '한마디도 밖에 새어 나가지 않게 숨죽인 세 사람의 대화를 다시 들어 보세요.'
OUTRO = '여관과 주방을 회색 사무실로 바꾼다는 청천벽력 같은 통지서 뒤에 접힌 두 번째 종이 한 장이 클립으로 묶여 있었어요. 과연 그 종이에 어떤 단서가 숨어 있을지 다음 화가 기다려집니다. 다음 이야기에서 만나요.'
CLOSING = ('arthur', 'Bye for now!')
STORY = [
    ('tessa', 'Hannah, look through the glass. They are standing face to face under the tree!', '해나, 유리창 너머로 좀 봐요. 두 사람이 나무 아래서 마주 보고 서 있어요!'),
    ('hannah', 'Neither of them walked away! Caleb is pointing at the two chairs right now!', '두 사람 중 누구도 돌아서지 않았어요! 케일럽이 지금 막 의자 두 개를 가리키고 있어요!'),
    ('arthur', 'Wonderful... let me just glance at this landlord letter while we wait.', '다행이군... 우리가 기다리는 동안 이 건물주 편지나 슬쩍 훑어봐야겠어요.'),
    ('tessa', 'Probably a boring notice about painting the street shutters.', '아마 거리 쪽 덧창에 페인트칠을 한다는 지루한 안내문일 거예요.'),
    ('arthur', 'Oh... oh no. Where is my chair? My knees feel weak.', '오... 이럴 수가. 내 의자가 어디 있지? 무릎에 힘이 다 풀리는군요.'),
    ('hannah', 'Arthur! Your face went completely white! Sit down, what does the letter say?', '아서! 얼굴이 새하얗게 질렸어요! 어서 앉아 보세요, 편지에 뭐라고 적혀 있나요?'),
    ('arthur', 'Read the top line for me, Hannah. Tell me my glasses are playing tricks again!', '맨 윗줄 좀 대신 읽어 줘요, 해나. 내 안경이 또 장난을 치는 거라고 말해 줘요!'),
    ('hannah', "'Notice of Property Transfer: Number Eight Courtyard Building offered for commercial office sale.'", '부동산 양도 통지서, 팔 번지 코트야드 건물이 상업용 사무실 매물로 나왔습니다.'),
    ('tessa', 'Commercial office sale?! Turn our guesthouse and kitchen into gray offices?!', '상업용 사무실 매물이라고요?! 우리 여관과 주방을 회색 사무실로 바꾸겠다는 거예요?!'),
    ('arthur', 'They give us thirty days before new buyers inspect the building!', '새 매수자들이 건물을 점검하러 오기 전까지 삼십 일밖에 안 준대요!'),
    ('hannah', 'Wait, there is a second folded page clipped to the back of this notice...', '잠깐만요, 이 통지서 뒷면에 접힌 두 번째 종이가 클립으로 끼워져 있어요...'),
    ('arthur', 'Not a word to anyone outside yet! Let the two brothers have their Friday afternoon first!', '바깥에 있는 사람들에게는 아직 한마디도 하지 말아요! 두 형제가 금요일 오후를 온전히 보내게 해 줍시다!'),
]
WALK = [
    (0, None, ["'해나, 유리창 너머로 좀 봐요. 두 사람이 나무 아래서 마주 보고 서 있어요!' 두 사람이 정면으로 얼굴을 마주 대하고 선 모습은 관용 부사구", (None, 'face to face'), '표현으로 극적인 대면을 선명하게 그려 줘요.']),
    (1, None, ["'두 사람 중 누구도 돌아서지 않았어요! 케일럽이 지금 막 의자 두 개를 가리키고 있어요!' 둘 가운데 어느 한쪽도 그렇지 않았다고 전체 부정을 할 때는", (None, 'Neither of them'), '주어 자리에 놓아 안도의 한숨을 전해요.']),
    (2, None, ["'다행이군... 우리가 기다리는 동안 이 건물주 편지나 슬쩍 훑어봐야겠어요.' 서류나 화면을 대수롭지 않게 재빨리 한번 눈길을 주어 본다는 뜻은", (None, 'glance at'), '동사와 전치사 조합으로 가벼운 태도를 나타내요.']),
    (3, None, ["'아마 거리 쪽 덧창에 페인트칠을 한다는 지루한 안내문일 거예요.' 무엇에 관한 공지인지 내용을 덧붙일 때는 전치사 뒤에 동명사를 이어 쓴", (None, 'about painting'), '구절로 대수롭지 않은 추측을 보태요.']),
    (4, None, ["'오... 이럴 수가. 내 의자가 어디 있지? 무릎에 힘이 다 풀리는군요.' 큰 충격을 받아 다리가 후들거리고 기운이 빠질 때는 감각 동사를 쓴", (None, 'My knees feel weak'), '문장으로 휘청거리는 몸 상태를 생생히 말해요.']),
    (5, None, ["'아서! 얼굴이 새하얗게 질렸어요! 어서 앉아 보세요, 편지에 뭐라고 적혀 있나요?' 놀람이나 두려움으로 안색이 창백하게 변했다는 갑작스러운 변화는", (None, 'went completely white'), '동사를 활용해 창백해진 표정을 한눈에 보여 줘요.']),
    (6, None, ["'맨 윗줄 좀 대신 읽어 줘요, 해나. 내 안경이 또 장난을 치는 거라고 말해 줘요!' 눈이나 기억이 착각을 일으켜 잘못 본 것이기를 바랄 때는 관용구", (None, 'playing tricks'), '표현을 빌려 현실을 부정하고 싶은 마음을 담아요.']),
    (7, None, ["'부동산 양도 통지서, 팔 번지 코트야드 건물이 상업용 사무실 매물로 나왔습니다.' 건물이 어떤 용도의 매매 대상으로 나왔는지 표시하는 공문서 문구는", (None, 'for commercial office sale'), '명사 수식 구조로 딱딱한 법률 통지의 느낌을 내요.']),
    (8, None, ["'상업용 사무실 매물이라고요?! 우리 여관과 주방을 회색 사무실로 바꾸겠다는 거예요?!' 소중한 공간을 전혀 다른 모습으로 탈바꿈시킨다는 변화 구문은", (None, 'Turn our guesthouse and kitchen into'), '동사와 결과 전치사를 짝지어 분통한 심정을 터뜨려요.']),
    (9, None, ["'새 매수자들이 건물을 점검하러 오기 전까지 삼십 일밖에 안 준대요!' 어떤 일이 닥치기 전까지 남은 기한을 설명할 때는 시간 접속사절", (None, 'before new buyers inspect'), '현재시제를 써서 촉박한 일정을 알려요.']),
    (10, None, ["'잠깐만요, 이 통지서 뒷면에 접힌 두 번째 종이가 클립으로 끼워져 있어요...' 서류 뒤쪽에 클립으로 고정되어 붙어 있는 상태를 설명할 때는 과거분사구", (None, 'clipped to the back'), '수식으로 새로운 단서를 짚어 내요.']),
    (11, None, ["'바깥에 있는 사람들에게는 아직 한마디도 하지 말아요! 두 형제가 금요일 오후를 온전히 보내게 해 줍시다!' 비밀을 당부하며 누구에게도 절대 발설하지 말라고 단속할 때는", (None, 'Not a word to anyone'), '동사 없는 간결한 금지의 말로 깊은 배려를 보여 줘요.']),
]
