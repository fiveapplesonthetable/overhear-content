# Authoring module for linden-courtyard-ko-s01e01-scene-06.
ID = 'linden-courtyard-ko-s01e01-scene-06'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = 'The Luggage Tag  (수하물 이름표의 단서)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'arthur': 'Arthur'}
INTRO = '프런트 데스크로 내려온 세 사람과 아서가 안경을 쓰고 가방 이름표의 작은 손글씨를 함께 살펴봅니다. 해나는 곧바로 기차역 분실물 센터에 전화를 걸어 뒤바뀐 파란 가방이 신고되었는지 확인해요. 먼저 긴박한 대화를 들어 보세요.'
OPENER = '이제 단서를 찾아가는 대화를 한 문장씩 짚어 볼까요.'
TRANSITION = '자연스러운 호흡으로 장면 전체를 다시 한번 들어 보세요.'
OUTRO = '역 분실물 센터에는 아직 접수된 소식이 없었지만 카페 쪽에서 지켜보던 테사가 좋은 생각이 떠오른 듯 손을 흔드네요. 과연 테사는 어떤 따뜻한 도움을 준비했을까요. 곧 다시 만나요.'
CLOSING = ('arthur', 'See you soon!')
STORY = [
    ('arthur', 'Dear me, what a mix-up! Let me look at the tag with my glasses.', '저런, 세상에 이런 착오가 다 있군요! 안경을 쓰고 이름표를 한번 볼게요.'),
    ('evelyn', 'Is there a name or a phone number on it?', '거기에 이름이나 전화번호가 적혀 있나요?'),
    ('arthur', 'No phone number, unfortunately. Only two initials and an old street name.', '아쉽게도 전화번호는 없네요. 머리글자 두 자와 옛 거리 이름뿐이에요.'),
    ('hannah', 'Wait, that street is right here in our neighborhood, five minutes away!', '잠깐만요, 그 거리는 바로 우리 동네잖아요, 오 분 거리에 있어요!'),
    ('evelyn', 'How strange! We rode the same morning train to the same district.', '참 신기하네요! 같은 아침 기차를 타고 같은 구역까지 왔던 거군요.'),
    ('arthur', 'Hannah, call the station lost and found office right away.', '해나, 지금 바로 기차역 분실물 센터에 전화해 보세요.'),
    ('hannah', 'I am dialing now... Hello? Did anyone report a swapped blue suitcase?', '지금 번호 누르고 있어요... 여보세요? 혹시 뒤바뀐 파란 여행 가방을 신고한 분이 있나요?'),
    ('evelyn', 'Tell them mine has a red ribbon inside the top pocket!', '제 가방에는 윗주머니 안쪽에 빨간 리본이 달려 있다고 전해 주세요!'),
    ('hannah', 'Not yet? Please take our guesthouse number and address. Thank you!', '아직인가요? 저희 게스트하우스 번호와 주소를 적어 주세요. 감사합니다!'),
    ('arthur', "They have nothing yet, ma'am, I am terribly sorry.", '아직 들어온 게 없다고 하네요, 선생님. 정말 대단히 죄송합니다.'),
    ('evelyn', 'It is not your fault. Still, I only have the coat on my back!', '사장님 잘못이 아닌걸요. 그렇긴 해도 지금 가진 옷이라곤 입고 있는 이 코트뿐이네요!'),
    ('hannah', 'Wait one moment, Tessa in the cafe just waved to me with an idea!', '잠시만 기다려 보세요, 카페에 있는 테사가 좋은 생각이 났다며 방금 저한테 손을 흔들었어요!'),
]
WALK = [
    (0, None, ["'저런, 세상에 이런 착오가 다 있군요! 안경을 쓰고 이름표를 한번 볼게요.' 짐이 뒤바뀐 해프닝에 탄식하는 감탄 표현", (None, 'what a mix-up'), '뒤이어 시선을 고정해 살핀다는 뜻의', (None, 'look at'), '두 표현이 상황을 생생히 보여 줘요.']),
    (1, None, ["'거기에 이름이나 전화번호가 적혀 있나요?' 무언가가 있는지 유무를 정중히 물어볼 때는 어순을 뒤집은", (None, 'Is there'), '여기 쓰인 이 두 단어로 질문을 간단히 열어요.']),
    (2, None, ["'아쉽게도 전화번호는 없네요. 머리글자 두 자와 옛 거리 이름뿐이에요.' 찾는 정보가 전혀 없을 때는 명사 바로 앞에 부정어를 둔", (None, 'No phone number'), '이렇게 간결한 명사구로도 자연스럽게 답해요.']),
    (3, None, ["'잠깐만요, 그 거리는 바로 우리 동네잖아요, 오 분 거리에 있어요!' 얼마나 떨어져 있는지 거리를 나타내는 부사", (None, 'away'), '바로 이 말을 시간 뒤에 붙인', (None, 'five minutes away'), '여기 쓰인 이 표현으로 걸어서 오 분 거리임을 알려 줘요.']),
    (4, None, ["'참 신기하네요! 같은 아침 기차를 타고 같은 구역까지 왔던 거군요.' 우연에 놀라는 감탄문", (None, 'How strange'), '그리고 기차를 탔다는 과거 동작을 나타내는', (None, 'rode'), '두 표현이 기묘한 우연을 잘 살려 줘요.']),
    (5, None, ["'해나, 지금 바로 기차역 분실물 센터에 전화해 보세요.' 잃어버린 물건과 습득물을 관리하는 곳을 영어에서는", (None, 'lost and found'), '이렇게 두 분사를 나란히 묶어 불러요.']),
    (6, None, ["'지금 번호 누르고 있어요... 여보세요? 혹시 뒤바뀐 파란 여행 가방을 신고한 분이 있나요?' 과거의 신고 여부를 묻는 전화 문의에서는 조동사로 시작하는", (None, 'Did anyone report'), '여기 쓰인 이 구절 뒤에 동사원형을 그대로 유지해요.']),
    (7, None, ["'제 가방에는 윗주머니 안쪽에 빨간 리본이 달려 있다고 전해 주세요!' 내 가방이라는 말을 한 단어로 깔끔하게 줄일 때", (None, 'mine'), '바로 이 소유대명사가 주어 자리를 든든히 채워 줘요.']),
    (8, None, ["'아직인가요? 저희 게스트하우스 번호와 주소를 적어 주세요. 감사합니다!' 아직 소식이 없다는 상대의 말을 짧게 되받아 확인할 때", (None, 'Not yet'), '여기 쓰인 이 두 단어가 통화에서 아주 자주 쓰여요.']),
    (9, None, ["'아직 들어온 게 없다고 하네요, 선생님. 정말 대단히 죄송합니다.' 미안한 마음을 한층 깊고 정중하게 전하고 싶을 때는", (None, 'terribly sorry'), '이렇게 강조 부사를 앞에 더해 예의를 갖춰요.']),
    (10, None, ["'사장님 잘못이 아닌걸요. 그렇긴 해도 지금 가진 옷이라곤 입고 있는 이 코트뿐이네요!' 자책하는 상대를 따뜻하게 위로할 때는", (None, 'It is not your fault'), '여기 쓰인 이 문장 전체를 통째로 외워 두면 참 좋아요.']),
    (11, None, ["'잠시만 기다려 보세요, 카페에 있는 테사가 좋은 생각이 났다며 방금 저한테 손을 흔들었어요!' 바로 직전에 일어난 동작을 생생하게 전할 때는 과거동사 앞에 부사를 둔", (None, 'just waved'), '이렇게 말하면 방금 손을 흔들었다는 뜻이 돼요.']),
]
