# Authoring module for linden-courtyard-ko-s01e03-scene-03.
ID = 'linden-courtyard-ko-s01e03-scene-03'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 3
SCENE = 3
TITLE = 'Left at the Landing  (층계참에서 왼쪽으로)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'hannah': 'Hannah', 'tessa': 'Tessa', 'arthur': 'Arthur'}
INTRO = '다락방에 침대 시트를 팽팽하게 끼우고 황동 전등을 켜자 노란 불빛이 방 안을 따뜻하게 채워요. 손님에게 드릴 할인 혜택까지 정한 순간 마침내 아래층 대문 종소리가 울립니다. 세 사람의 분주한 마무리 대화를 들어 보세요.'
OPENER = '방금 들은 다락방 단장 장면을 한 문장씩 차근차근 풀어 볼까요.'
TRANSITION = '이제 완성된 장면을 처음부터 끝까지 다시 한번 들어 보세요.'
OUTRO = '정각 여덟 시에 맞춰 오늘 밤의 주인공이 여관 문을 두드렸어요. 두근거리는 가슴을 쓸어내리는 아서를 뒤로하고 해나가 침착하게 손님을 맞으러 내려갑니다. 다음 장면에서 곧 이어서 만나요.'
CLOSING = ('hannah', 'Bye for now!')
STORY = [
    ('tessa', 'Tuck that sheet corner tight, Hannah! Here go the two soft pillows.', '그쪽 시트 모서리를 팽팽하게 밀어 넣어요, 해나! 여기 푹신한 베개 두 개 갑니다.'),
    ('hannah', 'Done! And the blue rug fits right beside the bed.', '다 됐어요! 그리고 파란 깔개가 침대 바로 옆에 딱 맞네요.'),
    ('arthur', 'Where should I hang this round mirror? Left of the window or right?', '이 둥근 거울은 어디에 걸까요? 창문 왼쪽이 좋을까요, 오른쪽이 좋을까요?'),
    ('hannah', 'Right beside the desk, where the light is good.', '빛이 잘 드는 책상 바로 옆에 걸어 주세요.'),
    ('tessa', "Plug in Graham's brass lamp... oh, look how warm that yellow light is!", '그레이엄의 황동 전등 플러그를 꽂아 봐요. 와, 저 노란 불빛이 얼마나 포근한지 보세요!'),
    ('arthur', 'Honestly, I almost want to sleep up here myself tonight!', '솔직히 말해서 오늘 밤엔 저라도 여기 위에서 직접 자고 싶을 정도예요!'),
    ('hannah', 'Wait, what discount should we offer him for changing rooms?', '잠깐만요, 방을 바꾸게 해 드린 대가로 어떤 할인을 제안해야 할까요?'),
    ('arthur', 'Half price for tonight, and free breakfast all week!', '오늘 밤 숙박료는 반값으로 해 드리고, 일주일 내내 아침 식사도 무료로 드립시다!'),
    ('tessa', 'Generous! Did you just hear the courtyard gate bell downstairs?', '정말 통이 크시네요! 방금 아래층 안뜰 대문 종소리 들으셨어요?'),
    ('hannah', "Eight o'clock on the dot! Our guest is here!", '여덟 시 정각이네요! 우리 손님이 도착했어요!'),
    ('arthur', 'My heart is pounding! Hannah, you explain it, you sound calm and honest!', '심장이 쿵쾅거려요! 해나, 당신이 설명해 줘요, 침착하고 솔직하게 들리니까요!'),
    ('hannah', 'Leave it to me. Let us go down and welcome him.', '저한테 맡기세요. 함께 내려가서 손님을 맞이해요.'),
]
WALK = [
    (0, None, ["'그쪽 시트 모서리를 팽팽하게 밀어 넣어요, 해나! 여기 푹신한 베개 두 개 갑니다.' 침대보 끝자락을 매트리스 밑으로 단단히 꽂아 넣으라고 할 때는", (None, 'Tuck that sheet corner tight'), '동사와 상태 형용사를 함께 써서 깔끔한 손놀림을 묘사해요.']),
    (1, None, ["'다 됐어요! 그리고 파란 깔개가 침대 바로 옆에 딱 맞네요.' 조금도 떨어지지 않은 바로 곁의 자리를 강조하고 싶을 때는", (None, 'right beside'), '전치사 앞에 강조 부사를 덧붙여 바짝 붙은 느낌을 살려요.']),
    (2, None, ["'이 둥근 거울은 어디에 걸까요? 창문 왼쪽이 좋을까요, 오른쪽이 좋을까요?' 상대방의 의견을 구하며 물건을 걸 위치를 상의할 때는", (None, 'Where should I hang'), '조동사를 넣어 부드럽고 예의 바르게 방향을 물어봐요.']),
    (3, None, ["'빛이 잘 드는 책상 바로 옆에 걸어 주세요.' 앞에 나온 장소를 자연스럽게 이어받아 어떤 곳인지 설명할 때는", (None, 'where the light is good'), '관계부사 절을 뒤에 붙여 채광이 좋은 자리임을 밝혀 줘요.']),
    (4, None, ["'그레이엄의 황동 전등 플러그를 꽂아 봐요. 와, 저 노란 불빛이 얼마나 포근한지 보세요!' 전자기기의 전원을 콘센트에 연결하라고 말할 때는 구동사", (None, 'Plug in'), '두 단어를 짝지어 일상 속 동작을 간단히 표현해요.']),
    (5, None, ["'솔직히 말해서 오늘 밤엔 저라도 여기 위에서 직접 자고 싶을 정도예요!' 주어 자신이 직접 그러고 싶다고 뜻을 한층 강조할 때는", (None, 'myself'), '재귀대명사를 문장 뒤쪽에 덧붙여 진심 어린 감탄을 전해요.']),
    (6, None, ["'잠깐만요, 방을 바꾸게 해 드린 대가로 어떤 할인을 제안해야 할까요?' 보상이나 제안을 건네는 이유를 또렷이 밝힐 때는 전치사구", (None, 'for changing rooms'), '동명사 형태를 이어 붙여 방 변경에 대한 보답임을 나타내요.']),
    (7, None, ["'오늘 밤 숙박료는 반값으로 해 드리고, 일주일 내내 아침 식사도 무료로 드립시다!' 절반 가격이라는 혜택을 말할 때는", (None, 'Half price'), '이어서 공짜 조식을 덧붙일 때는', (None, 'free breakfast'), '군더더기 없는 명사구로 파격적인 제안을 시원하게 건네요.']),
    (8, None, ["'정말 통이 크시네요! 방금 아래층 안뜰 대문 종소리 들으셨어요?' 막 지나간 순간의 소리를 상대도 들었는지 확인할 때는", (None, 'Did you just hear'), '과거 의문문 안에 부사를 끼워 넣어 방금 일어난 일을 짚어 줘요.']),
    (9, None, ["'여덟 시 정각이네요! 우리 손님이 도착했어요!' 일 분의 오차도 없이 정확한 시각임을 생동감 있게 말할 때는", (None, 'on the dot'), '시각 뒤에 이 관용 표현을 붙여 칼같이 맞은 시간을 강조해요.']),
    (10, None, ["'심장이 쿵쾅거려요! 해나, 당신이 설명해 줘요, 침착하고 솔직하게 들리니까요!' 다급한 상황에서 상대방을 콕 집어 역할을 맡길 때는", (None, 'you explain it'), '명령문 앞에 주어를 일부러 남겨 네가 해 달라는 뜻을 뚜렷이 살려요.']),
    (11, None, ["'저한테 맡기세요. 함께 내려가서 손님을 맞이해요.' 걱정하는 동료를 든든하게 안심시키며 일을 떠맡을 때는", (None, 'Leave it to me'), '짧고 미더운 이 한마디로 믿음직한 태도를 보여 줄 수 있어요.']),
]
