# Authoring module for linden-courtyard-ko-s01e06-scene-02.
ID = 'linden-courtyard-ko-s01e06-scene-02'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 6
SCENE = 2
TITLE = 'The Wooden Train  (나무로 깎은 장난감 기차)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'caleb': 'Caleb', 'owen': 'Owen', 'evelyn': 'Evelyn'}
INTRO = '하얀 종이 꾸러미를 펼치자 할아버지가 손수 깎아 만든 나무 기차 기관차가 모습을 드러내요. 바퀴 밑에 연필로 적힌 두 형제의 이름을 들여다보는 순간, 옛 피아노 스승 에블린 선생님이 반갑게 다가옵니다. 감동적인 이중 상봉을 들어 보세요.'
OPENER = '추억 속 보물과 스승을 다시 만나는 대화를 살펴볼까요.'
TRANSITION = '마치 아름다운 이중주 같은 세 사람의 대화를 다시 들어 보세요.'
OUTRO = '월요일 아침 기차에서 뒤바뀐 파란 가방 하나가 이십오 년 만의 사제 상봉까지 이끌어 주었네요. 하지만 로비 안에서는 아서의 한숨 소리가 깊어지고 있습니다. 다음 장면에서 확인해 봐요.'
CLOSING = ('evelyn', 'See you later!')
STORY = [
    ('caleb', 'Before the movers cleared Linden Street, I saved this box from the attic shelf.', '이삿짐센터 직원들이 린든 거리 집을 비우기 전에 제가 다락방 선반에서 이 상자를 구해 두었어요.'),
    ('owen', "Open the white paper... no! Grandfather's carved wooden train engine!", '하얀 종이를 펼쳐 보니... 설마! 할아버지께서 깎으신 나무 기차 기관차잖아!'),
    ('caleb', 'Look underneath the wheels. Your name and mine are still penciled there.', '바퀴 바로 밑쪽을 봐요. 형 이름이랑 제 이름이 아직도 연필로 적혀 있어요.'),
    ('owen', 'I thought this was lost when we sold the house! Why keep it for me?', '집을 팔았을 때 이건 잃어버린 줄만 알았어! 왜 나를 위해 이걸 간직해 둔 거니?'),
    ('caleb', 'Because a house is brick and timber, Owen, while family is what we keep.', '집은 벽돌과 목재일 뿐이지만, 오언 형, 가족은 우리가 지켜 내는 것이니까요.'),
    ('evelyn', 'And you two boys kept the best part of Number twelve right here.', '그리고 너희 두 소년이 십이 번지 집의 가장 소중한 부분을 바로 여기 지켜 냈구나.'),
    ('owen', "Excuse me, ma'am... wait. That voice! Miss Evelyn, my piano teacher?!", '실례합니다, 부인... 잠깐만요. 저 목소리는! 제 피아노 선생님이셨던 에블린 선생님?!'),
    ('evelyn', 'Still waiting for you to play your F major scale slowly, Owen!', '네가 바장조 음계를 천천히 연주해 주기를 아직도 기다리고 있단다, 오언!'),
    ('owen', 'Am I dreaming?! Did you plan this whole reunion, Caleb?', '제가 지금 꿈을 꾸고 있는 건가요?! 케일럽, 네가 이 모든 상봉을 다 계획한 거니?'),
    ('caleb', "Pure luck, and one swapped blue suitcase on Monday morning's train!", '순전한 행운이죠, 거기에 월요일 아침 기차에서 뒤바뀐 파란 여행 가방 하나 덕분이고요!'),
    ('evelyn', 'Life arranges better duets than we do, my dear boys.', '인생은 우리보다 훨씬 더 멋진 이중주를 편곡해 준단다, 사랑하는 얘들아.'),
    ('owen', 'Please sit with us, Miss Evelyn! Tell me I am not twenty-five years late for my lesson!', '저희와 함께 앉으세요, 에블린 선생님! 레슨 시간에 이십오 년이나 지각한 건 아니라고 말씀해 주세요!'),
]
WALK = [
    (0, None, ["'이삿짐센터 직원들이 린든 거리 집을 비우기 전에 제가 다락방 선반에서 이 상자를 구해 두었어요.' 가구와 짐을 옮겨 주는 이사업체 사람들을 일상 영어에서는 복수 명사", (None, 'the movers'), '단어로 간결하게 불러요.']),
    (1, None, ["'하얀 종이를 펼쳐 보니... 설마! 할아버지께서 깎으신 나무 기차 기관차잖아!' 열차 맨 앞에서 객차를 이끄는 기관차 부분을 가리킬 때는 복합 명사", (None, 'train engine'), '표현을 써서 정교한 나무 장난감을 묘사해요.']),
    (2, None, ["'바퀴 바로 밑쪽을 봐요. 형 이름이랑 제 이름이 아직도 연필로 적혀 있어요.' 사물의 바로 아랫면이라는 위치를 짚는 전치사", (None, 'underneath'), '그리고 내 이름을 소유대명사로 줄여 나란히 묶은', (None, 'Your name and mine'), '구절이 세월을 건넌 형제애를 보여 줘요.']),
    (3, None, ["'집을 팔았을 때 이건 잃어버린 줄만 알았어! 왜 나를 위해 이걸 간직해 둔 거니?' 조동사와 주어를 덜어 내고 동사원형만 바로 붙인 구어체 의문문", (None, 'Why keep it'), '어순으로 벅차오르는 고마움을 짧게 물어요.']),
    (4, None, ["'집은 벽돌과 목재일 뿐이지만, 오언 형, 가족은 우리가 지켜 내는 것이니까요.' 선행사를 품은 관계대명사로 우리가 소중히 간직하는 것이라는 뜻을 빚어낸", (None, 'what we keep'), '명사절이 문장 끝에 묵직한 울림을 남기네요.']),
    (5, None, ["'그리고 너희 두 소년이 십이 번지 집의 가장 소중한 부분을 바로 여기 지켜 냈구나.' 대명사 바로 뒤에 명사를 덧대어 어릴 적 모습 그대로 다정히 부르는", (None, 'you two boys'), '호칭에서 스승의 변함없는 사랑이 묻어나요.']),
    (6, None, ["'실례합니다, 부인... 잠깐만요. 저 목소리는! 제 피아노 선생님이셨던 에블린 선생님?!' 악기 이름과 가르치는 사람을 나란히 붙여 직업을 나타내는", (None, 'piano teacher'), '복합 명사로 반가운 옛 은사를 단번에 불러요.']),
    (7, None, ["'네가 바장조 음계를 천천히 연주해 주기를 아직도 기다리고 있단다, 오언!' 음악 수업에서 자주 연습하는 기본 장조 음계를 영어로 일컫는", (None, 'F major scale'), '표현을 빌려 어린 시절 수업 풍경을 유쾌하게 되살려요.']),
    (8, None, ["'제가 지금 꿈을 꾸고 있는 건가요?! 케일럽, 네가 이 모든 상봉을 다 계획한 거니?' 믿기 힘들 만큼 놀라운 현실 앞에서 꿈인지 생시인지 되물을 때는 진행형 의문문", (None, 'Am I dreaming'), '한마디로 황홀한 기분을 터뜨려요.']),
    (9, None, ["'순전한 행운이죠, 거기에 월요일 아침 기차에서 뒤바뀐 파란 여행 가방 하나 덕분이고요!' 다른 계산 없이 오로지 운이 좋았을 뿐이라고 말할 때는 형용사를 붙인", (None, 'Pure luck'), '두 단어로 기분 좋은 우연을 요약해요.']),
    (10, None, ["'인생은 우리보다 훨씬 더 멋진 이중주를 편곡해 준단다, 사랑하는 얘들아.' 앞선 일반동사구 전체를 다시 쓰지 않고 대동사로 깔끔하게 받아 비교하는", (None, 'than we do'), '구조가 문장을 한층 세련되게 마무리해 줘요.']),
    (11, None, ["'저희와 함께 앉으세요, 에블린 선생님! 레슨 시간에 이십오 년이나 지각한 건 아니라고 말씀해 주세요!' 수업이나 약속 시간에 늦었다고 말할 때 세트로 외워 두는 형용사구", (None, 'late for my lesson'), '표현으로 재치 만점의 인사를 건네요.']),
]
