# Authoring module for linden-courtyard-ko-s01e06-scene-03.
ID = 'linden-courtyard-ko-s01e06-scene-03'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 6
SCENE = 3
TITLE = 'Thirty Days on Paper  (종이 위에 적힌 삼십 일)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '프런트 데스크 뒤에서 아서가 삼십 일 뒤 매각 통지서를 붙들고 낙담하고 있어요. 그레이엄과 해나는 포기하기 전에 서류 뒷장을 끝까지 읽어 보자며 안뜰에 앉아 있는 뜻밖의 전문가를 떠올립니다. 세 사람의 대화를 들어 보세요.'
OPENER = '위기 속에서 해법을 찾아가는 프런트의 대화를 짚어 볼까요.'
TRANSITION = '희망의 불씨가 살아나는 세 사람의 대화를 다시 들어 보세요.'
OUTRO = '포틀랜드 전역의 역사적인 안뜰 건물을 다루는 건축가 케일럽이 바로 열 미터 밖에 앉아 있었군요! 마침 테사도 안뜰 탁자에서 돌아오고 있습니다. 다음 장면으로 이어 가 볼까요.'
CLOSING = ('graham', 'Bye for now!')
STORY = [
    ('arthur', 'Fifteen years of polishing brass keys and straightening ties... gone in thirty days!', '십오 년 동안 황동 열쇠를 닦고 넥타이를 고쳐 매던 세월이... 삼십 일 만에 사라지게 생겼어요!'),
    ('graham', 'Stop burying us before we read the whole document, Arthur.', '서류 전체를 다 읽어 보기도 전에 우리를 미리 묻어 버리지 마시오, 아서.'),
    ('hannah', 'Yes! Earlier I noticed a second page clipped behind the cover letter.', '맞아요! 아까 표지 서한 뒤쪽에 두 번째 장이 클립으로 묶여 있는 걸 봤거든요.'),
    ('arthur', 'Legal paragraphs give me a headache even with two pairs of glasses!', '법률 문단들은 안경을 두 개나 겹쳐 쓰고 봐도 내 머리를 지끈거리게 만든단 말이에요!'),
    ('graham', 'This house survived eighty winters and one broken boiler valve yesterday.', '이 집은 여든 번의 겨울과 어제 고장 난 보일러 밸브 하나까지 다 버텨 낸 건물이에요.'),
    ('hannah', 'Wait, who is sitting ten meters away in our courtyard right now?', '잠깐만요, 지금 우리 안뜰 열 미터 밖에 누가 앉아 있죠?'),
    ('arthur', 'Two brothers eating lemon cake?', '레몬 케이크를 먹고 있는 두 형제 말인가요?'),
    ('hannah', 'An architect who works with historic courtyard buildings all over Portland!', '포틀랜드 전역의 유서 깊은 안뜰 건물들을 다루는 건축가가 있잖아요!'),
    ('graham', 'Smart thinking, Hannah. Caleb reads city building rules every single week.', '기막힌 생각이군, 해나. 케일럽은 매주 시 건축 법규를 읽는 사람이니까요.'),
    ('arthur', 'Oh, I could never bother a paying guest with our landlord troubles!', '오, 숙박비를 내는 손님에게 우리 건물주 문제로 폐를 끼칠 수는 절대 없어요!'),
    ('hannah', 'After we guarded his blue suitcase all week? He will want to help!', '우리가 일주일 내내 그분 파란 가방을 지켜 드렸는걸요? 분명 돕고 싶어 하실 거예요!'),
    ('graham', 'Wait, here comes Tessa back from their table right now.', '잠깐, 지금 막 테사가 두 사람 탁자에서 이리로 돌아오고 있군요.'),
]
WALK = [
    (0, None, ["'십오 년 동안 황동 열쇠를 닦고 넥타이를 고쳐 매던 세월이... 삼십 일 만에 사라지게 생겼어요!' 얼마의 기간이 지나면 흔적도 없이 끝나 버린다는 뜻은 기간의 전치사를 쓴", (None, 'gone in thirty days'), '구절로 허망한 심정을 토로해요.']),
    (1, None, ["'서류 전체를 다 읽어 보기도 전에 우리를 미리 묻어 버리지 마시오, 아서.' 벌써 끝장난 것처럼 비관하는 행동을 그만두라고 제지할 때는 동명사를 취하는", (None, 'Stop burying us'), '비유적 표현으로 단호하게 정신을 일깨워요.']),
    (2, None, ["'맞아요! 아까 표지 서한 뒤쪽에 두 번째 장이 클립으로 묶여 있는 걸 봤거든요.' 본문 서류 맨 앞에 붙어 용건을 요약해 알리는 안내 편지는 영어로", (None, 'cover letter'), '명사구를 써서 공식 우편물의 구성을 설명해요.']),
    (3, None, ["'법률 문단들은 안경을 두 개나 겹쳐 쓰고 봐도 내 머리를 지끈거리게 만든단 말이에요!' 복잡한 일이나 글씨가 두통을 유발할 때는 수여동사 구조를 활용한", (None, 'give me a headache'), '일상 표현으로 골치 아픈 심정을 생생히 말해요.']),
    (4, None, ["'이 집은 여든 번의 겨울과 어제 고장 난 보일러 밸브 하나까지 다 버텨 낸 건물이에요.' 모진 세월이나 시련을 무사히 견뎌 내고 살아남았다는 뜻은 타동사", (None, 'survived eighty winters'), '표현처럼 전치사 없이 목적어를 바로 붙여 말해요.']),
    (5, None, ["'잠깐만요, 지금 우리 안뜰 열 미터 밖에 누가 앉아 있죠?' 구체적인 수치로 얼마나 떨어져 있는지 거리를 나타낼 때는 단위 뒤에 부사를 붙인", (None, 'ten meters away'), '구절로 가까운 안뜰 쪽을 환기해요.']),
    (6, None, ["'레몬 케이크를 먹고 있는 두 형제 말인가요?' 명사 바로 뒤에서 지금 무엇을 하는 중인지 수식할 때는 현재분사를 이어 붙인", (None, 'Two brothers eating'), '어순으로 눈앞의 모습을 간단히 답해요.']),
    (7, None, ["'포틀랜드 전역의 유서 깊은 안뜰 건물들을 다루는 건축가가 있잖아요!' 도시 곳곳 빠짐없이 전 지역에 걸쳐 활동한다는 공간 범위는", (None, 'all over Portland'), '전치사구로 든든한 전문성을 강조해요.']),
    (8, None, ["'기막힌 생각이군, 해나. 케일럽은 매주 시 건축 법규를 읽는 사람이니까요.' 상대가 떠올린 명쾌한 아이디어에 감탄하며 칭찬할 때는 명사구", (None, 'Smart thinking'), '두 단어만으로도 훌륭한 호응이 돼요.']),
    (9, None, ["'오, 숙박비를 내는 손님에게 우리 건물주 문제로 폐를 끼칠 수는 절대 없어요!' 예의상 차마 남을 번거롭게 성가시게 할 수 없다고 손사래 칠 때는", (None, 'I could never bother'), '조동사와 부정부사를 결합해 조심스러운 성품을 드러내요.']),
    (10, None, ["'우리가 일주일 내내 그분 파란 가방을 지켜 드렸는걸요? 분명 돕고 싶어 하실 거예요!' 상대가 기꺼이 발 벗고 나서려 할 것이라는 밝은 확신은 미래 조동사를 쓴", (None, 'He will want to help'), '문장으로 망설이는 마음을 움직여요.']),
    (11, None, ["'잠깐, 지금 막 테사가 두 사람 탁자에서 이리로 돌아오고 있군요.' 누군가 이쪽으로 걸어 다가오는 모습을 발견해 알릴 때는 부사로 문을 여는", (None, 'here comes Tessa'), '현재시제 도치 구문으로 시선을 모아요.']),
]
