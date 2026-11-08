# Authoring module for linden-courtyard-ko-s01e02-scene-04.
ID = 'linden-courtyard-ko-s01e02-scene-04'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 2
SCENE = 4
TITLE = 'Herbs from the Courtyard  (안뜰에서 따 온 싱싱한 허브)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'graham': 'Graham', 'tessa': 'Tessa', 'hannah': 'Hannah'}
INTRO = '안뜰까지 버터 소동 소리를 들은 그레이엄이 직접 기른 푸른 허브를 따 가지고 주방으로 들어옵니다. 일곱 시 이십구 분, 손님들이 계단을 내려오는 발소리에 맞춰 세 사람이 호흡을 척척 맞추네요. 먼저 활기찬 대화를 들어 보세요.'
OPENER = '이제 아침 식탁을 완성하는 대화를 한 문장씩 살펴볼까요.'
TRANSITION = '장면 전체를 다시 한번 자연스러운 속도로 들어 보세요.'
OUTRO = '고소한 빵과 프랑스식 달걀 요리, 향긋한 허브까지 모든 준비가 제시간에 완벽히 끝났어요. 둘째 날 아침을 멋지게 해낸 해나에게 그레이엄도 흐뭇한 칭찬을 건네네요. 곧 다음 장면에서 만나요.'
CLOSING = ('graham', 'See you soon!')
STORY = [
    ('graham', 'I heard shouting about butter from all the way out in the courtyard.', '저 바깥 안뜰에까지 버터 때문에 소리치는 게 다 들리더군요.'),
    ('tessa', 'Hannah bought sea salt butter, so today we are making French style eggs!', '해나가 천일염 버터를 사 와서 오늘 우리는 프랑스식 달걀 요리를 만들고 있어요!'),
    ('graham', 'Good. Put these fresh green herbs on top before you serve them.', '잘됐네요. 손님께 내어 드리기 전에 이 싱싱한 푸른 허브를 그 위에 얹으세요.'),
    ('hannah', 'Did you grow those herbs yourself, Graham?', '저 허브들은 그레이엄 씨가 직접 기르신 거예요?'),
    ('graham', 'Somebody has to take care of the courtyard plants.', '누군가는 안뜰 화초들을 돌봐야 하니까요.'),
    ('tessa', 'Smell that! Warm bread, hot eggs, and fresh herbs.', '이 냄새 좀 맡아 보세요! 따뜻한 빵, 따끈한 달걀 요리, 그리고 싱싱한 허브까지요.'),
    ('hannah', 'Where do the small spoons and napkins go?', '작은 스푼들과 냅킨들은 어디에 놓으면 될까요?'),
    ('tessa', 'Put one napkin and one small spoon beside every blue cup.', '파란 찻잔마다 바로 옆에 냅킨 한 장과 작은 스푼 하나씩을 놓아 주세요.'),
    ('graham', 'Seven twenty-nine on my watch. Guests are coming down the stairs.', '제 손목시계로 일곱 시 이십구 분입니다. 손님들이 계단으로 내려오고 계세요.'),
    ('hannah', 'Four tables, eight chairs, everything in place!', '식탁 네 개, 의자 여덟 개, 모든 게 제자리에 준비 완료예요!'),
    ('tessa', 'Pour the hot water into the teapot, Hannah, here they come!', '찻주전자에 뜨거운 물을 부어요, 해나, 이제 손님들이 들어오세요!'),
    ('graham', 'Not bad for day two, rookie.', '둘째 날치고는 꽤 훌륭하네요, 신입.'),
]
WALK = [
    (0, None, ["'저 바깥 안뜰에까지 버터 때문에 소리치는 게 다 들리더군요.' 멀리서 누군가 외치는 소리가 귀에 들려왔다고 할 때는 지각 동사 뒤에 분사를 둔", (None, 'I heard shouting'), '이렇게 생생한 현장감을 전달해요.']),
    (1, None, ["'해나가 천일염 버터를 사 와서 오늘 우리는 프랑스식 달걀 요리를 만들고 있어요!' 사 오다라는 뜻의 동사는 불규칙 과거형인", (None, 'bought'), '바로 이 한 단어로 방금 장을 봐 온 일을 나타내요.']),
    (2, None, ["'잘됐네요. 손님께 내어 드리기 전에 이 싱싱한 푸른 허브를 그 위에 얹으세요.' 신선함과 색깔을 차례로 짚어 주는", (None, 'fresh green herbs'), '그리고 음식 맨 위쪽을 가리키는', (None, 'on top'), '두 표현이 먹음직스러운 마무리를 그려 줘요.']),
    (3, None, ["'저 허브들은 그레이엄 씨가 직접 기르신 거예요?' 남의 손을 빌리지 않고 손수 길렀음을 강조할 때는 문장 끝에 재귀대명사인", (None, 'yourself'), '방금 들은 이 단어를 덧붙여 감탄을 전해요.']),
    (4, None, ["'누군가는 안뜰 화초들을 돌봐야 하니까요.' 식물이나 사람, 공간을 정성껏 보살피고 관리한다는 뜻은", (None, 'take care of'), '방금 들은 이 세 단어가 늘 한 덩어리로 쓰여요.']),
    (5, None, ["'이 냄새 좀 맡아 보세요! 따뜻한 빵, 따끈한 달걀 요리, 그리고 싱싱한 허브까지요.' 포근한 온기가 감도는", (None, 'Warm bread'), '그리고 갓 조리해 김이 모락모락 나는', (None, 'hot eggs'), '두 표현이 온도 차이를 섬세하게 살려 줘요.']),
    (6, None, ["'작은 스푼들과 냅킨들은 어디에 놓으면 될까요?' 식기나 물건의 원래 자리가 어디인지 물어볼 때는 가다라는 동사를 활용한", (None, 'Where do the small spoons and napkins go'), '방금 들은 이 질문이 실생활에서 정말 자연스러워요.']),
    (7, None, ["'파란 찻잔마다 바로 옆에 냅킨 한 장과 작은 스푼 하나씩을 놓아 주세요.' 식탁 위에서 찻잔 바로 옆자리를 정확히 일러 줄 때는", (None, 'beside'), '방금 들은 이 전치사 하나로 깔끔하게 안내해요.']),
    (8, None, ["'제 손목시계로 일곱 시 이십구 분입니다. 손님들이 계단으로 내려오고 계세요.' 내 시계에 찍힌 현재 시각을 기준으로 말할 때는 전치사를 붙인", (None, 'on my watch'), '이렇게 간결하게 덧붙여요.']),
    (9, None, ["'식탁 네 개, 의자 여덟 개, 모든 게 제자리에 준비 완료예요!' 흐트러짐 없이 정해진 자리에 다 정돈된 상태를", (None, 'in place'), '방금 들은 이 짧은 두 단어로 시원하게 표현해요.']),
    (10, None, ["'찻주전자에 뜨거운 물을 부어요, 해나, 이제 손님들이 들어오세요!' 액체를 따르는 동사", (None, 'Pour'), '그 뒤에 주전자 안쪽으로 들어가는 방향 전치사', (None, 'into'), '두 단어가 늘 짝꿍처럼 함께 다닌답니다.']),
    (11, None, ["'둘째 날치고는 꽤 훌륭하네요, 신입.' 무뚝뚝한 듯 다정하게 잘했다고 인정해 주는", (None, 'Not bad'), '그리고 새내기 직원을 정겹게 부르는', (None, 'rookie'), '그레이엄다운 따뜻한 격려 인사예요.']),
]
