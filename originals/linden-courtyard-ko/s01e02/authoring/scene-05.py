# Authoring module for linden-courtyard-ko-s01e02-scene-05.
ID = 'linden-courtyard-ko-s01e02-scene-05'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 2
SCENE = 5
TITLE = 'Juice on the Tie  (넥타이에 튄 오렌지 주스)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'arthur': 'Arthur', 'evelyn': 'Evelyn', 'hannah': 'Hannah'}
INTRO = '아침 식탁에 앉은 에블린 선생님이 설탕을 넣지 않은 홍차와 따뜻한 빵 한 조각을 주문합니다. 멋지게 오성급 서비스를 뽐내려던 아서가 넓은 주전자 주둥이 때문에 그만 자기 비단 넥타이에 주스를 쏟고 마네요. 유쾌한 식탁 대화를 들어 보세요.'
OPENER = '그럼 아침 식탁의 정중한 표현들을 한 문장씩 살펴볼까요.'
TRANSITION = '웃음이 번지는 식탁 장면을 처음부터 다시 들어 보세요.'
OUTRO = '차가운 탄산수로 주스 얼룩을 빼면 된다는 에블린 선생님의 지혜로운 조언과 달걀 요리 칭찬 덕분에 식당 분위기가 한층 화기애애해졌어요. 곧 다음 장면에서 이어서 만나요.'
CLOSING = ('evelyn', 'Take care!')
STORY = [
    ('hannah', 'Good morning again, Miss Evelyn! Would you like coffee or black tea?', '다시 좋은 아침이에요, 에블린 선생님! 커피로 드릴까요, 홍차로 드릴까요?'),
    ('evelyn', 'Black tea without sugar, please, and one slice of warm bread.', '설탕 빼고 홍차로 부탁해요, 그리고 따뜻한 빵 한 조각도요.'),
    ('arthur', "Allow me to pour the fresh orange juice, ma'am!", '신선한 오렌지 주스는 제가 따라 드리겠습니다, 선생님!'),
    ('evelyn', 'Oh, how kind of you, sir. Just half a glass.', '어머, 정말 친절하시네요, 사장님. 딱 반 잔만 주세요.'),
    ('arthur', 'At our guesthouse, five-star service comes naturally... whoops!', '저희 게스트하우스에서는 오성급 서비스가 몸에 배어... 어이쿠!'),
    ('hannah', 'Careful, Arthur, the pitcher spout is wide!', '조심하세요, 아서, 피처 주둥이가 넓어요!'),
    ('arthur', 'Oh dear! Not a drop on the table, thank goodness... all of it is on my tie!', '저런! 다행히 식탁 위에는 한 방울도 안 튀었네요... 전부 제 넥타이에 쏟아졌어요!'),
    ('evelyn', 'Do not worry! Cold sparkling water takes orange juice right out.', '걱정하지 마세요! 차가운 탄산수면 오렌지 주스 얼룩이 쏙 빠진답니다.'),
    ('hannah', 'Here is a clean cloth and cold water, Arthur.', '여기 깨끗한 천이랑 찬물 있어요, 아서.'),
    ('arthur', "Excuse me, ma'am, I shall retreat to my office with dignity!", '실례하겠습니다, 선생님, 저는 품위를 지키며 제 사무실로 물러나 보겠습니다!'),
    ('evelyn', 'The scrambled eggs are delicious, Hannah. Tell Tessa my compliments!', '스크램블드에그가 정말 맛있네요, 그레이엄. 테사에게도 훌륭하다고 전해 주세요!'),
    ('hannah', 'I will! Enjoy your morning.', '꼭 전해 드릴게요! 기분 좋은 아침 시간 보내세요.'),
]
WALK = [
    (0, None, ["'다시 좋은 아침이에요, 에블린 선생님! 커피로 드릴까요, 홍차로 드릴까요?' 식탁에서 손님께 음료를 공손하고 다정하게 권할 때는 언제나", (None, 'Would you like'), '여기서 이 세 단어로 질문을 시작해요.']),
    (1, None, ["'설탕 빼고 홍차로 부탁해요, 그리고 따뜻한 빵 한 조각도요.' 셀 수 없는 빵을 얇게 썬 조각 단위로 세어 요청할 때는", (None, 'one slice of warm bread'), '이렇게 단위 명사를 앞에 세워 말해요.']),
    (2, None, ["'신선한 오렌지 주스는 제가 따라 드리겠습니다, 선생님!' 정중하게 손님의 잔을 직접 채워 드리겠다고 나설 때는", (None, 'Allow me to pour'), '여기서 이 격식 있는 표현이 한층 품위를 더해 줘요.']),
    (3, None, ["'어머, 정말 친절하시네요, 사장님. 딱 반 잔만 주세요.' 상대의 세심한 배려에 고마움을 표하는 감탄사", (None, 'how kind of you'), '이어서 절반 분량만 청하는', (None, 'half a glass'), '어순에서 절반이 부정관사 앞에 오는 점을 눈여겨보세요.']),
    (4, None, ["'저희 게스트하우스에서는 오성급 서비스가 몸에 배어... 어이쿠!' 최고 수준의 환대를 자랑하는 복합 수식어", (None, 'five-star service'), '그 직후에 실수를 저지르고 내뱉는 감탄사', (None, 'whoops'), '두 표현의 반전이 웃음을 자아내요.']),
    (5, None, ["'조심하세요, 아서, 피처 주둥이가 넓어요!' 눈앞의 위험이나 실수를 다급히 주의를 주어 막을 때는", (None, 'Careful'), '여기서 이 형용사 한 단어를 단독으로 외치면 충분해요.']),
    (6, None, ["'저런! 다행히 식탁 위에는 한 방울도 안 튀었네요... 전부 제 넥타이에 쏟아졌어요!' 불행 중 다행이라며 가슴을 쓸어내릴 때는", (None, 'thank goodness'), '여기서 이 표현으로 정중하게 안도를 나타내요.']),
    (7, None, ["'걱정하지 마세요! 차가운 탄산수면 오렌지 주스 얼룩이 쏙 빠진답니다.' 톡 쏘는 기포가 든 탄산수를 가리키는", (None, 'sparkling water'), '그리고 얼룩을 말끔히 빼낸다는 뜻의', (None, 'takes orange juice right out'), '살림 지혜가 담긴 유용한 표현이에요.']),
    (8, None, ["'여기 깨끗한 천이랑 찬물 있어요, 아서.' 물기나 얼룩을 닦아 내는 행주나 천 한 장은", (None, 'cloth'), '바로 이 단어를 셀 수 있는 명사로 써서 건네요.']),
    (9, None, ["'실례하겠습니다, 선생님, 저는 품위를 지키며 제 사무실로 물러나 보겠습니다!' 조금 고풍스럽고 익살스러운 어조로 자리를 피하겠다고 말할 때", (None, 'I shall retreat'), '이런 격식 있는 조동사와 동사를 골라 썼어요.']),
    (10, None, ["'스크램블드에그가 정말 맛있네요, 그레이엄. 테사에게도 훌륭하다고 전해 주세요!' 요리사에게 음식이 훌륭했다고 감탄 인사를 전해 달라고 할 때 항상 복수형인", (None, 'my compliments'), '여기서 이 표현을 관용적으로 써요.']),
    (11, None, ["'꼭 전해 드릴게요! 기분 좋은 아침 시간 보내세요.' 상대방의 부탁을 흔쾌히 들어주겠다고 짧게 약속할 때는", (None, 'I will'), '여기서 이 두 단어만으로도 믿음직한 대답이 완성돼요.']),
]
