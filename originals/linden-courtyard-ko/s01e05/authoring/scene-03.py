# Authoring module for linden-courtyard-ko-s01e05-scene-03.
ID = 'linden-courtyard-ko-s01e05-scene-03'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 5
SCENE = 3
TITLE = 'Friday Lemon Cake  (금요일의 레몬 케이크)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'evelyn': 'Evelyn', 'caleb': 'Caleb', 'tessa': 'Tessa'}
INTRO = '카페 모퉁이에서 에블린 선생님이 어린 시절 두 형제가 금요일 피아노 수업 뒤에 늘 나누어 먹던 간식을 떠올려요. 그 이야기를 들은 제빵사 테사의 눈빛이 반짝이기 시작합니다. 고소한 추억이 피어나는 대화를 들어 보세요.'
OPENER = '달콤한 추억이 담긴 대화 속 영어 표현들을 함께 풀어 볼까요.'
TRANSITION = '따뜻한 부엌 분위기를 느끼며 대화를 처음부터 다시 들어 보세요.'
OUTRO = '바구니 속 노란 레몬 여섯 개가 오늘 정오의 재회를 위해 준비되어 있었던 것만 같네요. 설탕 시럽이 반짝이는 모서리 조각이 두 형제의 마음도 사르르 녹여 줄 거예요. 잠시 뒤에 다음 장면에서 만나요.'
CLOSING = ('tessa', 'Bye for now!')
STORY = [
    ('tessa', 'So, Caleb, you are really staying in the courtyard to greet Owen at noon?', '그럼 케일럽, 정오에 오언 형님을 맞이하려고 정말 안뜰에 남기로 한 거예요?'),
    ('caleb', 'Yes, Tessa. Even if he turns around and walks straight back out the gate.', '네, 테사. 비록 형이 몸을 돌려 대문 밖으로 곧장 다시 걸어 나간다 해도요.'),
    ('evelyn', 'Owen will not walk out. He always acted tough for five seconds, then softened.', '오언은 그냥 나가지 않을 거야. 늘 오 초 동안만 강한 척하다가 금세 마음이 누그러졌거든.'),
    ('caleb', 'You still remember that after all these years?', '이렇게 오랜 세월이 흘렀는데도 그 모습을 아직 기억하세요?'),
    ('evelyn', 'Of course! Every Friday when he missed a piano note, he frowned at the wall.', '그럼! 매주 금요일마다 피아노 음을 하나 틀릴 때면 벽을 보며 인상을 찌푸렸지.'),
    ('tessa', 'How did you get him smiling again, Miss Evelyn?', '에블린 선생님, 그럴 때 어떻게 다시 웃게 만드셨어요?'),
    ('evelyn', 'His grandfather sliced warm lemon cake with powdered sugar on top!', '할아버지께서 고운 설탕 가루를 위에 솔솔 뿌린 따뜻한 레몬 케이크를 썰어 주셨단다!'),
    ('caleb', 'Oh! Yellow lemon glaze! We fought over the corner piece every single Friday!', '아! 노란 레몬 설탕 시럽이요! 금요일마다 모서리 조각을 차지하려고 형이랑 다투었어요!'),
    ('tessa', 'Hold everything! What time is it right now? Nine thirty-five!', '모두 잠깐만 멈춰 보세요! 지금 몇 시죠? 아홉 시 삼십오 분이네요!'),
    ('caleb', 'Tessa, please do not do extra work because of us.', '테사, 저희 때문에 일부러 번거로운 일을 더 하지는 마세요.'),
    ('tessa', 'Six yellow lemons are sitting in my basket right now. This kitchen was waiting for today!', '노란 레몬 여섯 개가 지금 제 바구니 안에 놓여 있어요. 우리 주방이 바로 오늘을 기다려 온 거예요!'),
    ('evelyn', 'Bake plenty of corner pieces, my dear!', '모서리 조각이 넉넉히 나오게 구워 주렴, 얘야!'),
]
WALK = [
    (0, None, ["'그럼 케일럽, 정오에 오언 형님을 맞이하려고 정말 안뜰에 남기로 한 거예요?' 이미 마음먹은 가까운 미래의 계획을 확인하며 물을 때는 현재진행형인", (None, 'you are really staying'), '어순에 부사를 끼워 넣어 반가운 확신을 확인해요.']),
    (1, None, ["'네, 테사. 비록 형이 몸을 돌려 대문 밖으로 곧장 다시 걸어 나간다 해도요.' 설령 어떤 일이 벌어지더라도 변함없다는 양보의 접속사", (None, 'Even if'), '그 뒤에 발길을 돌린다는 구동사', (None, 'turns around'), '현재시제가 이어져 굳은 다짐을 보여 줘요.']),
    (2, None, ["'오언은 그냥 나가지 않을 거야. 늘 오 초 동안만 강한 척하다가 금세 마음이 누그러졌거든.' 겉으로만 센 척 행동했다는 과거 습관은 형용사를 붙인", (None, 'acted tough'), '두 단어로 형의 속마음을 다정하게 짚어 내요.']),
    (3, None, ["'이렇게 오랜 세월이 흘렀는데도 그 모습을 아직 기억하세요?' 수많은 해가 지난 뒤에도 여전하다는 감회를 담을 때는", (None, 'after all these years'), '관용구처럼 통째로 외워 두면 참 유용해요.']),
    (4, None, ["'그럼! 매주 금요일마다 피아노 음을 하나 틀릴 때면 벽을 보며 인상을 찌푸렸지.' 악기 연주에서 음을 놓치거나 틀렸다는 표현은 동사를 살린", (None, 'missed a piano note'), '구절로 자연스럽게 묘사해요.']),
    (5, None, ["'에블린 선생님, 그럴 때 어떻게 다시 웃게 만드셨어요?' 누군가의 기분을 풀어 다시 미소 짓게 유도했다는 뜻은 분사를 결합한", (None, 'get him smiling'), '구조로 부드러운 변화를 나타내요.']),
    (6, None, ["'할아버지께서 고운 설탕 가루를 위에 솔솔 뿌린 따뜻한 레몬 케이크를 썰어 주셨단다!' 음식의 맨 윗부분에 토핑이 올라가 있음을 덧붙일 때는", (None, 'on top'), '짧은 전치사구로 먹음직스러운 장면을 완성해요.']),
    (7, None, ["'아! 노란 레몬 설탕 시럽이요! 금요일마다 모서리 조각을 차지하려고 형이랑 다투었어요!' 단 한 번도 빠짐없이 매주 금요일마다 그랬음을 강조할 때는", (None, 'every single Friday'), '가운데 강조 형용사를 넣어 생생한 추억을 살려요.']),
    (8, None, ["'모두 잠깐만 멈춰 보세요! 지금 몇 시죠? 아홉 시 삼십오 분이네요!' 좋은 생각이 번쩍 떠올라 하던 일을 다 멈추라고 외칠 때는", (None, 'Hold everything'), '활기찬 감탄 표현으로 주의를 단번에 집중시켜요.']),
    (9, None, ["'테사, 저희 때문에 일부러 번거로운 일을 더 하지는 마세요.' 절이 아니라 대명사 목적어를 바로 붙여 이유를 말할 때는 복합 전치사", (None, 'because of us'), '세 단어로 미안하고 고마운 마음을 전해요.']),
    (10, None, ["'노란 레몬 여섯 개가 지금 제 바구니 안에 놓여 있어요. 우리 주방이 바로 오늘을 기다려 온 거예요!' 사물이 바구니 안에 얌전히 자리 잡고 있는 상태를 영어에서는", (None, 'are sitting in my basket'), '앉아 있다는 진행형 동사로 정겹게 표현해요.']),
    (11, None, ["'모서리 조각이 넉넉히 나오게 구워 주렴, 얘야!' 어른이 젊은 상대를 따뜻하고 다정하게 부를 때는 문장 끝에", (None, 'my dear'), '애정 어린 호칭을 살짝 덧붙여 정을 나누어요.']),
]
