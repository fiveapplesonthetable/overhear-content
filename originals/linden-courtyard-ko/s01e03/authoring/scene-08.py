# Authoring module for linden-courtyard-ko-s01e03-scene-08.
ID = 'linden-courtyard-ko-s01e03-scene-08'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 3
SCENE = 8
TITLE = 'Ice-Cold Pipes  (얼음장 같은 배관)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = '지하실을 살피고 올라온 그레이엄이 굳은 표정으로 보일러의 황동 압력 밸브가 고장 났다는 소식을 전해 줘요. 당장 내일 아침 일곱 시면 샤워기에서 얼음장 같은 찬물이 나올 위기에 처합니다. 세 사람의 대책 회의를 들어 보세요.'
OPENER = '오늘의 마지막 장면에 담긴 대화를 한 문장씩 또렷하게 살펴볼까요.'
TRANSITION = '이제 긴장감 넘치는 장면 전체를 자연스러운 속도로 다시 들어 보세요.'
OUTRO = '내일 아침 일곱 시 정각에 문을 여는 다리 건너 철물점만이 유일한 희망이 되었어요. 과연 해나와 그레이엄은 손님들이 깨기 전에 뜨거운 물을 되살릴 수 있을까요. 다음 화에서 흥미진진한 아침 질주가 이어집니다.'
CLOSING = ('graham', 'See you tomorrow!')
STORY = [
    ('arthur', 'Tell me it was just a tiny air bubble, Graham! Please!', '그냥 아주 작은 공기 방울이었다고 말해 줘요, 그레이엄! 제발요!'),
    ('graham', 'Bad news. The brass pressure valve on the old boiler just gave up.', '안 좋은 소식입니다. 낡은 보일러의 황동 압력 밸브가 방금 수명을 다했어요.'),
    ('hannah', 'Does that mean no radiators tonight, or no hot water too?', '그럼 오늘 밤 난방이 안 된다는 뜻인가요, 아니면 뜨거운 물도 안 나오나요?'),
    ('graham', 'The rooms will stay warm until morning, Hannah, because the brick walls hold heat.', '벽돌 벽이 열기를 품고 있어서 아침까지는 방들이 따뜻하게 유지될 겁니다, 해나.'),
    ('arthur', 'Thank heavens! And the morning showers?', '하늘이 도왔군요! 그럼 아침 샤워는 어떻게 되나요?'),
    ('graham', 'By tomorrow morning, the shower water will be ice cold.', '내일 아침이면 샤워기 물이 얼음장처럼 차가울 겁니다.'),
    ('arthur', 'Ice cold showers?! With the Portland Travel Guide inspector on the third floor?!', '얼음물 샤워라고요? 삼 층에 포틀랜드 여행 안내서 평가원이 묵고 있는데요?'),
    ('hannah', 'Do you have a spare brass valve in your toolbox?', '공구함에 여분의 황동 밸브가 하나 남아 있나요?'),
    ('graham', 'Used my last one in winter. Only the old hardware shop past the bridge sells this size.', '지난겨울에 마지막 남은 걸 썼어요. 다리 너머 오래된 철물점에서만 이 규격을 팝니다.'),
    ('hannah', 'What time does that hardware shop open?', '그 철물점은 몇 시에 문을 여나요?'),
    ('graham', 'Seven sharp, half an hour before breakfast.', '일곱 시 정각이요, 아침 식사 삼십 분 전입니다.'),
    ('hannah', 'Set your alarm, Graham. Tomorrow morning we beat the cold showers!', '자명종 맞춰 두세요, 그레이엄. 내일 아침엔 우리가 찬물 샤워를 꼭 이겨 내요!'),
]
WALK = [
    (0, None, ["'그냥 아주 작은 공기 방울이었다고 말해 줘요, 그레이엄! 제발요!' 간절히 바라는 소식을 상대의 입으로 직접 듣고 싶을 때는", (None, 'Tell me'), '명령문 뒤에 접속사를 생략하고 듣고 싶은 내용을 바로 이어 말해요.']),
    (1, None, ["'안 좋은 소식입니다. 낡은 보일러의 황동 압력 밸브가 방금 수명을 다했어요.' 달갑지 않은 상황을 알릴 때는", (None, 'Bad news'), '그리고 기계 부품이 완전히 멈춰 버렸다고 의인화해 말할 때는', (None, 'gave up'), '포기했다는 뜻의 구동사로 고장 난 상태를 생생히 표현해요.']),
    (2, None, ["'그럼 오늘 밤 난방이 안 된다는 뜻인가요, 아니면 뜨거운 물도 안 나오나요?' 앞에 말한 내용에 더해 또 다른 항목까지 포함되는지 덧붙여 물을 때는", (None, 'too'), '문장 맨 끝에 이 짧은 부사를 얹어 역시 그러한지 확인해요.']),
    (3, None, ["'벽돌 벽이 열기를 품고 있어서 아침까지는 방들이 따뜻하게 유지될 겁니다, 해나.' 현재의 온기나 상태가 변함없이 그대로 이어진다고 설명할 때는", (None, 'stay warm'), '유지 동사 뒤에 형용사를 바로 붙여 따뜻한 상태의 지속을 나타내요.']),
    (4, None, ["'하늘이 도왔군요! 그럼 아침 샤워는 어떻게 되나요?' 큰 걱정을 한시름 덜었을 때 반사적으로 터져 나오는 안도의 감탄사는", (None, 'Thank heavens'), '일상에서 놀란 가슴을 쓸어내릴 때 아주 자주 쓰이는 표현이에요.']),
    (5, None, ["'내일 아침이면 샤워기 물이 얼음장처럼 차가울 겁니다.' 손이 시릴 만큼 매섭게 차가운 물의 온도를 비유해 강조할 때는", (None, 'ice cold'), '명사와 형용사를 나란히 결합해 피부에 와닿는 한기를 전해 줘요.']),
    (6, None, ["'얼음물 샤워라고요? 삼 층에 포틀랜드 여행 안내서 평가원이 묵고 있는데요?' 건물 내 특정 층에 머물고 있다는 위치를 정확히 짚어 말할 때는", (None, 'on the third floor'), '바닥 면에 발을 딛고 있으므로 접촉의 전치사를 함께 사용해요.']),
    (7, None, ["'공구함에 여분의 황동 밸브가 하나 남아 있나요?' 비상시를 대비해 따로 챙겨 둔 예비 부품을 가리킬 때는 형용사", (None, 'spare'), '명사 바로 앞에 이 단어를 붙여 남는 여분이 있는지 물어봐요.']),
    (8, None, ["'지난겨울에 마지막 남은 걸 썼어요. 다리 너머 오래된 철물점에서만 이 규격을 팝니다.' 공구와 부품을 파는 가게는", (None, 'hardware shop'), '이어서 어떤 지점을 지나 그 너머를 뜻할 때는', (None, 'past the bridge'), '지나침을 나타내는 전치사로 가게 위치를 선명히 그려 줘요.']),
    (9, None, ["'그 철물점은 몇 시에 문을 여나요?' 가게나 기관의 정해진 영업 시작 시각을 물어볼 때는", (None, 'What time does'), '삼인칭 단수 조동사를 챙겨 규칙적인 일정을 깔끔하게 질문해요.']),
    (10, None, ["'일곱 시 정각이요, 아침 식사 삼십 분 전입니다.' 에누리 없이 딱 떨어지는 정각 시간을 짧고 힘 있게 말할 때는", (None, 'Seven sharp'), '숫자 바로 뒤에 날카롭다는 뜻의 단어를 붙여 정확한 시각을 강조해요.']),
    (11, None, ["'자명종 맞춰 두세요, 그레이엄. 내일 아침엔 우리가 찬물 샤워를 꼭 이겨 내요!' 아침에 제시간에 일어나도록 알람 시계를 맞추라고 당부할 때는", (None, 'Set your alarm'), '설정을 뜻하는 동사를 써서 내일 아침의 결의를 다잡아요.']),
]
