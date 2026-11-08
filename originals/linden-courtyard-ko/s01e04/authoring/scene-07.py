# Authoring module for linden-courtyard-ko-s01e04-scene-07.
ID = 'linden-courtyard-ko-s01e04-scene-07'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 4
SCENE = 7
TITLE = 'Sunlight on the Tag  (이름표에 비친 햇살)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = '그레이엄이 짐 보관용 벽장을 청소하느라 문제의 파란 여행 가방을 잠시 프런트로 꺼내 놓아요. 밝은 아침 햇살 아래서 종이 이름표를 다시 들여다본 에블린 선생님은 린든 거리 십이 번지 주소와 머리글자를 알아보고 깜짝 놀랍니다. 들어 보세요.'
OPENER = '햇살 아래서 옛 기억이 되살아나는 대화를 한 문장씩 살펴볼까요.'
TRANSITION = '그럼 놀라운 인연이 드러나는 장면 전체를 다시 들어 보세요.'
OUTRO = '스물다섯 해 전 린든 거리 십이 번지 목수 할아버지 댁에 피아노를 치던 형과 기차를 좋아하던 동생이 살았대요. 가방 속 작은 나무 장난감 기차의 비밀이 드디어 풀리려나 봅니다. 마지막 장면에서 확인해 봐요.'
CLOSING = ('evelyn', 'Bye for now!')
STORY = [
    ('graham', 'Let me set this blue suitcase here for five minutes while I sweep the closet.', '벽장을 쓰는 오 분 동안만 이 파란 여행 가방을 여기에 내려놓을게요.'),
    ('hannah', 'Careful with it, Graham. Friday at noon is tomorrow!', '조심해서 다뤄 주세요, 그레이엄. 금요일 정오가 바로 내일이잖아요!'),
    ('evelyn', "Oh, is that the twin suitcase from Monday's train?", '어머, 저게 월요일 기차에서 온 그 쌍둥이 여행 가방인가요?'),
    ('hannah', "Yes, ma'am, still waiting for its owner.", '네, 선생님, 아직도 주인을 기다리고 있어요.'),
    ('evelyn', 'May I look at the paper tag again here in the bright sunlight?', '여기 밝은 햇살 아래서 종이 이름표를 다시 한번 봐도 될까요?'),
    ('graham', "Go right ahead, ma'am. Monday afternoon the lobby was dark.", '얼마든지 그러세요, 선생님. 월요일 오후에는 로비가 어두웠으니까요.'),
    ('evelyn', 'Wait a moment... Number twelve, Linden Street, and two childhood initials written in the corner!', '잠깐만요. 린든 거리 십이 번지, 게다가 모서리에 적힌 어린 시절 머리글자 두 개라니요!'),
    ('hannah', 'Miss Evelyn, you look amazed! Do you know Number twelve, Linden Street?', '에블린 선생님, 정말 놀라신 표정이에요! 린든 거리 십이 번지를 아시나요?'),
    ('evelyn', 'Know it? Every Friday for six years I climbed those wooden stairs to teach piano!', '아느냐고요? 육 년 동안 매주 금요일마다 피아노를 가르치러 그 나무 계단을 올랐는걸요!'),
    ('graham', 'Twenty-five years ago? In that same house?', '스물다섯 해 전에요? 바로 그 똑같은 집에서요?'),
    ('evelyn', 'A carpenter lived there with his two grandsons. The older boy played piano, and the little one loved trains!', '목수 한 분이 두 손자와 함께 거기 사셨죠. 형은 피아노를 쳤고, 작은아이는 기차를 무척 좋아했어요!'),
    ('hannah', 'A carpenter... and a little wooden toy train inside the bag!', '목수 할아버지. 그리고 가방 안에 들어 있던 작은 나무 장난감 기차라니!'),
]
WALK = [
    (0, None, ["'벽장을 쓰는 오 분 동안만 이 파란 여행 가방을 여기에 내려놓을게요.' 행동이 이어지는 구체적인 시간의 길이를 숫자와 함께 밝혀 줄 때는", (None, 'for five minutes'), '지속 기간을 이끄는 전치사를 앞에 두어 잠깐 동안임을 알려 줘요.']),
    (1, None, ["'조심해서 다뤄 주세요, 그레이엄. 금요일 정오가 바로 내일이잖아요!' 낮 열두 시 정각을 뜻하는 명사 앞에 정확한 지점의 전치사를 결합한 구절이", (None, 'at noon'), '관사 없이 단 두 단어만으로 낮의 한가운데 시각을 또렷이 짚어 줘요.']),
    (2, None, ["'어머, 저게 월요일 기차에서 온 그 쌍둥이 여행 가방인가요?' 겉모습이 똑같이 닮은 한 쌍의 가방 가운데 하나를 재치 있게 부른 표현이", (None, 'twin suitcase'), '쌍둥이라는 명사를 앞에 두어 똑같은 가방 두 개라는 사연을 떠올리게 해요.']),
    (3, None, ["'네, 선생님, 아직도 주인을 기다리고 있어요.' 가방이 사람처럼 자기 주인이 나타나기를 계속 기다리는 중이라고 묘사한 구절이", (None, 'waiting for its owner'), '사물을 가리키는 소유격을 챙겨 넣어 가방의 주인임을 정확히 나타냈어요.']),
    (4, None, ["'여기 밝은 햇살 아래서 종이 이름표를 다시 한번 봐도 될까요?' 환하게 쏟아지는 햇빛에 둘러싸여 있다는 느낌을 영어로 옮길 때는", (None, 'in the bright sunlight'), '아래라는 말 대신 빛의 공간 속에 들어와 있다는 전치사를 사용해요.']),
    (5, None, ["'얼마든지 그러세요, 선생님. 월요일 오후에는 로비가 어두웠으니까요.' 상대가 허락을 구했을 때 사양하지 말고 편히 하시라고 흔쾌히 권하는 인사가", (None, 'Go right ahead'), '중간에 강조 부사를 넣어 한결 반갑고 너그러운 승낙을 건네요.']),
    (6, None, ["'잠깐만요. 린든 거리 십이 번지, 게다가 모서리에 적힌 어린 시절 머리글자 두 개라니요!' 나무나 가죽 표면에 글자가 파여 새겨져 있는 상태를 뒤에서 꾸며 주는 분사구가", (None, 'written in the corner'), '수동의 의미를 담은 과거분사로 세월의 흔적을 선명히 보여 줘요.']),
    (7, None, ["'에블린 선생님, 정말 놀라신 표정이에요! 린든 거리 십이 번지를 아시나요?' 상대방 얼굴에 떠오른 깜짝 놀란 기색을 보고 건네는 생생한 묘사가", (None, 'you look amazed'), '사람이 놀란 감정을 느낀 상태이므로 과거분사 형용사를 골라 썼어요.']),
    (8, None, ["'아느냐고요? 육 년 동안 매주 금요일마다 피아노를 가르치러 그 나무 계단을 올랐는걸요!' 악기 이름을 배움이나 가르침의 대상으로 말할 때는 관사 없이", (None, 'teach piano'), '교과목처럼 간결하게 동사 뒤에 바로 악기 명사를 붙이기도 해요.']),
    (9, None, ["'스물다섯 해 전에요? 바로 그 똑같은 집에서요?' 지금으로부터 얼마만큼 거슬러 올라간 과거 시점인지를 밝히는 표현이", (None, 'Twenty-five years ago'), '시간의 길이 뒤에 이전을 뜻하는 부사를 놓아 옛날 시점을 분명히 해요.']),
    (10, None, ["'목수 한 분이 두 손자와 함께 거기 사셨죠. 형은 피아노를 쳤고, 작은아이는 기차를 무척 좋아했어요!' 앞에 나온 소년이라는 명사의 반복을 피해 어린 동생을 가리킨 표현이", (None, 'the little one'), '대명사를 활용해 간결하면서도 다정한 어감을 잘 살렸어요.']),
    (11, None, ["'목수 할아버지. 그리고 가방 안에 들어 있던 작은 나무 장난감 기차라니!' 크기와 재질, 용도를 나타내는 꾸밈말들을 자연스러운 영어 순서대로 배열한 명사구가", (None, 'little wooden toy train'), '크기 다음에 나무 재질과 장난감 용도가 차례로 이어지는 흐름을 익혀 두세요.']),
]
