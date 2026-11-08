# Authoring module for linden-courtyard-ko-s01e05-scene-02.
ID = 'linden-courtyard-ko-s01e05-scene-02'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 5
SCENE = 2
TITLE = 'Three Years of Silence  (세 해 동안의 침묵)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '프런트 데스크로 자리를 옮긴 그레이엄이 일주일 내내 보관해 둔 파란 여행 가방의 자물쇠를 풀어 줍니다. 케일럽은 지난 세 해 동안 형 오언과 말을 섞지 못했던 가슴 아픈 가족사를 조심스레 털어놓아요. 세 사람의 잔잔한 대화를 귀 기울여 들어 보세요.'
OPENER = '이제 형제 사이의 사연이 담긴 문장들을 하나씩 살펴볼까요.'
TRANSITION = '대화의 감정선을 따라가며 장면 전체를 다시 들어 보세요.'
OUTRO = '이름도 적지 못한 짧은 엽서 한 장에 케일럽의 오랜 그리움과 걱정이 고스란히 담겨 있었네요. 다정한 여관 식구들을 만난 덕분에 케일럽도 이제 숨지 않고 형을 마주할 용기를 얻었습니다. 곧 다음 장면에서 만나요.'
CLOSING = ('graham', 'See you later!')
STORY = [
    ('graham', 'So our mystery Friday caller was sleeping upstairs under my attic roof all along.', '그러니까 수수께끼 같던 금요일 전화의 주인공이 내내 위층 다락방 지붕 아래서 자고 있었군요.'),
    ('caleb', 'Sorry for the trouble, Graham. Thank you for guarding this bag all week.', '번거롭게 해 드려 죄송해요, 그레이엄. 일주일 내내 이 가방을 지켜 주셔서 감사합니다.'),
    ('hannah', 'Why could you not simply hand Owen the wooden train at his front door?', '왜 그냥 오언 형님 댁 현관문 앞에서 나무 기차를 직접 건네주지 못했어요?'),
    ('caleb', 'Three years ago, after our grandfather died, Owen and I argued bitterly over selling the old house.', '삼 년 전 할아버지께서 돌아가신 뒤에 옛집을 파는 문제로 오언 형과 심하게 다투었거든요.'),
    ('graham', 'Family houses and old memories, those arguments cut deep.', '가족이 살던 집과 오랜 추억이 얽힌 다툼은 마음에 깊은 상처를 남기지요.'),
    ('caleb', 'We have not spoken since that Sunday. Last week I sent him one short postcard.', '그 일요일 이후로 서로 말 한마디 안 했어요. 지난주에 형에게 짧은 엽서 한 장을 보냈죠.'),
    ('hannah', 'Asking him to meet you here on Friday at noon?', '금요일 정오에 이곳에서 만나자고 청하는 내용이었나요?'),
    ('caleb', "Actually, I only wrote: 'Something from Grandfather is waiting at the Linden Courtyard Inn Friday at noon.'", '사실 할아버지께서 남기신 물건이 금요일 정오에 린든 코트야드 여관에서 기다리고 있다고만 적었어요.'),
    ('graham', 'Aha! You feared that if you signed your name, stubborn big brother would stay home!', '아하! 본인 이름을 적으면 고집 센 형님이 집에 그냥 계실까 봐 걱정했군요!'),
    ('caleb', 'You know older brothers well, Graham.', '형들의 마음을 정말 잘 아시네요, 그레이엄.'),
    ('hannah', 'Wait, were you planning to hand the clerk the bag and watch from across the street?!', '잠깐만요, 설마 직원에게 가방만 맡기고 길 건너편에서 지켜볼 생각이었나요?!'),
    ('caleb', 'That was my cowardly Monday plan... before I met all of you.', '그건 겁 많던 제 월요일 계획이었어요... 여러분 모두를 만나기 전까지는요.'),
]
WALK = [
    (0, None, ["'그러니까 수수께끼 같던 금요일 전화의 주인공이 내내 위층 다락방 지붕 아래서 자고 있었군요.' 처음부터 줄곧 내내 그러했다는 시간의 지속은", (None, 'all along'), '문장 끝에 이 두 단어를 놓아 유쾌하게 짚어 줘요.']),
    (1, None, ["'번거롭게 해 드려 죄송해요, 그레이엄. 일주일 내내 이 가방을 지켜 주셔서 감사합니다.' 폐를 끼쳐 미안한 마음을 공손하게 건넬 때는", (None, 'Sorry for the trouble'), '일상에서 두루 쓰이는 정중한 사과 인사예요.']),
    (2, None, ["'왜 그냥 오언 형님 댁 현관문 앞에서 나무 기차를 직접 건네주지 못했어요?' 손으로 직접 물건을 건네주다는 뜻으로 쓰인 동사", (None, 'hand Owen'), '전치사 없이 받는 사람을 바로 뒤에 이어 말해요.']),
    (3, None, ["'삼 년 전 할아버지께서 돌아가신 뒤에 옛집을 파는 문제로 오언 형과 심하게 다투었거든요.' 말다툼의 주제가 무엇이었는지 밝힐 때는 동명사를 짝지은", (None, 'over selling'), '전치사구로 갈등의 원인을 콕 집어 나타내요.']),
    (4, None, ["'가족이 살던 집과 오랜 추억이 얽힌 다툼은 마음에 깊은 상처를 남기지요.' 말이나 다툼이 마음속 깊이 아픔을 남긴다는 비유는", (None, 'cut deep'), '짧고 묵직한 두 단어로 진한 여운을 전해요.']),
    (5, None, ["'그 일요일 이후로 서로 말 한마디 안 했어요. 지난주에 형에게 짧은 엽서 한 장을 보냈죠.' 과거의 특정 시점부터 지금까지 이어진 공백을 말할 때는", (None, 'since that Sunday'), '현재완료 시제와 찰떡같이 어울리는 시간 표현이에요.']),
    (6, None, ["'금요일 정오에 이곳에서 만나자고 청하는 내용이었나요?' 앞선 명사 엽서를 자연스럽게 부연하며 되물을 때는 분사로 시작하는", (None, 'Asking him to meet you'), '구절만으로 엽서 속 요청을 매끄럽게 이어받아요.']),
    (7, None, ["'사실 할아버지께서 남기신 물건이 금요일 정오에 린든 코트야드 여관에서 기다리고 있다고만 적었어요.' 물건이 특정 장소에서 주인을 기다리는 중이라는 표현은", (None, 'is waiting at'), '현재진행형과 장소 전치사를 나란히 써서 생동감을 살려요.']),
    (8, None, ["'아하! 본인 이름을 적으면 고집 센 형님이 집에 그냥 계실까 봐 걱정했군요!' 과거 시점에서 상상한 가정의 결과를 말할 때는 조동사를 쓴", (None, 'would stay home'), '구절로 외출하지 않고 집에 남으리라는 추측을 나타내요.']),
    (9, None, ["'형들의 마음을 정말 잘 아시네요, 그레이엄.' 누구의 성격을 속속들이 잘 안다고 맞장구칠 때는 부사를 끝에 둔", (None, 'know older brothers well'), '간결한 어순으로 공감을 표해요.']),
    (10, None, ["'잠깐만요, 설마 직원에게 가방만 맡기고 길 건너편에서 지켜볼 생각이었나요?!' 도로 맞은편이라는 위치에서 바라본다는 뜻은 이중 전치사 느낌의", (None, 'from across the street'), '구절로 시선의 출발점을 선명히 그려 줘요.']),
    (11, None, ["'그건 겁 많던 제 월요일 계획이었어요... 여러분 모두를 만나기 전까지는요.' 형태는 부사처럼 생겼지만 실제로는 비겁하고 겁 많은을 뜻하는 형용사", (None, 'cowardly'), '명사 앞에서 부끄러웠던 옛 계획을 솔직히 꾸며 줘요.']),
]
