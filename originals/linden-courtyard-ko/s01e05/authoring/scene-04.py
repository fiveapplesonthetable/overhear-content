# Authoring module for linden-courtyard-ko-s01e05-scene-04.
ID = 'linden-courtyard-ko-s01e05-scene-04'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 5
SCENE = 4
TITLE = 'Two Chairs Under the Tree  (나무 아래 놓인 의자 두 개)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '정오가 가까워지자 해나와 테사, 그레이엄이 안뜰 피나무 아래에 두 형제를 위한 아늑한 자리를 마련해요. 무심한 척 종이 등불 줄을 손보는 그레이엄과 다락방에서 셔츠를 세 번이나 갈아입는 케일럽의 모습이 미소를 자아냅니다. 먼저 대화를 들어 보세요.'
OPENER = '정성껏 자리를 꾸미는 세 사람의 대화를 한 줄씩 알아볼까요.'
TRANSITION = '분주하고도 따뜻한 안뜰 풍경을 그리며 다시 한번 들어 보세요.'
OUTRO = '하얀 식탁보와 파란 찻잔, 식힘망 위의 레몬 케이크까지 모든 준비가 끝났어요. 이제 긴장한 케일럽의 마음을 다독여 줄 차례입니다. 곧 다음 장면에서 만나요.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Let us put the small wooden table right here under the tree, away from the door.', '작은 나무 탁자를 출입문에서 떨어진 여기 나무 바로 아래에 놓아요.'),
    ('graham', 'Good spot. Two solid chairs, facing the garden herbs instead of the lobby window.', '좋은 자리군요. 로비 창문 대신 정원 허브 화분을 마주 보도록 튼튼한 의자 두 개를 둡시다.'),
    ('tessa', 'Here is a clean white cloth and two blue teacups.', '여기 깨끗한 하얀 식탁보와 파란 찻잔 두 개를 가져왔어요.'),
    ('hannah', 'Graham, are you polishing those hanging paper lanterns for noon?', '그레이엄, 정오 시간에 맞추어 저기 매달린 종이 등불들을 닦고 계신 건가요?'),
    ('graham', 'The wire needed straightening anyway. Nothing sentimental about good maintenance.', '어차피 철사를 좀 반듯하게 펼 필요가 있었어요. 꼼꼼한 시설 관리에 감상적인 이유 같은 건 없습니다.'),
    ('tessa', 'Oh, listen to Mister Maintenance! Yesterday you fixed the boiler, today you fix two brothers!', '어머, 시설 관리 대장님 말씀 좀 들어 보세요! 어제는 보일러를 고치더니 오늘은 두 형제를 고쳐 주시네요!'),
    ('graham', 'I fix pipes and chairs. People have to fix their own words.', '나는 배관과 의자를 고칠 뿐입니다. 사람이 내뱉은 말은 각자 스스로 고쳐야 해요.'),
    ('hannah', 'What time does your watch say now, Graham?', '그레이엄, 지금 시계가 몇 시를 가리키고 있나요?'),
    ('graham', 'Eleven twenty. Cake ready, Tessa?', '열한 시 이십 분입니다. 케이크는 준비됐나요, 테사?'),
    ('tessa', 'Cooling on the rack right now, golden crust and sweet lemon sugar!', '노릇한 겉면과 달콤한 레몬 설탕 옷을 입고 지금 식힘망 위에서 식고 있어요!'),
    ('hannah', 'Look upstairs at the attic window: Caleb has changed his shirt three times!', '위층 다락방 창문 좀 보세요, 케일럽이 벌써 세 번이나 셔츠를 갈아입었어요!'),
    ('tessa', 'Go talk to him, Hannah, before he wears out the wooden floor!', '해나, 케일럽이 나무 마룻바닥을 다 닳게 만들기 전에 얼른 가서 말을 걸어 봐요!'),
]
WALK = [
    (0, None, ["'작은 나무 탁자를 출입문에서 떨어진 여기 나무 바로 아래에 놓아요.' 사람들의 시선이 닿는 출입구에서 거리를 둔다는 위치 설명은", (None, 'away from the door'), '부사와 전치사를 나란히 묶어 오붓한 자리를 나타내요.']),
    (1, None, ["'좋은 자리군요. 로비 창문 대신 정원 허브 화분을 마주 보도록 튼튼한 의자 두 개를 둡시다.' 의자나 건물이 어느 방향을 향해 놓여 있는지 설명할 때는 분사", (None, 'facing'), '한 단어로 시선의 방향을 깔끔하게 잡아 줘요.']),
    (2, None, ["'여기 깨끗한 하얀 식탁보와 파란 찻잔 두 개를 가져왔어요.' 천 조각이나 식탁에 덮는 테이블보를 가리킬 때는 명사", (None, 'cloth'), '단어 하나로 단정한 찻자리 분위기를 살려 내요.']),
    (3, None, ["'그레이엄, 정오 시간에 맞추어 저기 매달린 종이 등불들을 닦고 계신 건가요?' 공중에 줄지어 걸려 있는 종이 등불들을 묘사할 때는 현재분사를 앞세운", (None, 'hanging paper lanterns'), '명사구로 정원의 아늑한 소품을 가리켜요.']),
    (4, None, ["'어차피 철사를 좀 반듯하게 펼 필요가 있었어요. 꼼꼼한 시설 관리에 감상적인 이유 같은 건 없습니다.' 사물에 손질이나 정리가 필요했다는 수동의 의미는 동명사를 쓴", (None, 'needed straightening'), '구문으로 담백하게 둘러대요.']),
    (5, None, ["'어머, 시설 관리 대장님 말씀 좀 들어 보세요! 어제는 보일러를 고치더니 오늘은 두 형제를 고쳐 주시네요!' 상대의 특징에 호칭을 붙여 장난스러운 별명처럼 부를 때는", (None, 'Mister Maintenance'), '유쾌한 애칭으로 무뚝뚝한 동료를 놀려요.']),
    (6, None, ["'나는 배관과 의자를 고칠 뿐입니다. 사람이 내뱉은 말은 각자 스스로 고쳐야 해요.' 남이 대신해 줄 수 없는 자기 자신의 말이라는 점을 힘주어 말할 때는", (None, 'their own words'), '소유격 뒤에 강조 형용사를 덧붙여 책임감을 일깨워요.']),
    (7, None, ["'그레이엄, 지금 시계가 몇 시를 가리키고 있나요?' 손목시계에 찍힌 현재 시각을 물어볼 때 영어에서는 말하다는 동사를 활용한", (None, 'What time does your watch say'), '자연스러운 일상 의문문으로 확인해요.']),
    (8, None, ["'열한 시 이십 분입니다. 케이크는 준비됐나요, 테사?' 바쁜 현장에서 비 동사를 생략하고 핵심만 짧게 묻는", (None, 'Cake ready'), '두 단어만으로도 다정한 확인 질문이 완성돼요.']),
    (9, None, ["'노릇한 겉면과 달콤한 레몬 설탕 옷을 입고 지금 식힘망 위에서 식고 있어요!' 갓 구운 빵이나 케이크를 올려 두는 철망 선반 위라는 자리는", (None, 'on the rack'), '전치사구로 제빵 현장의 느낌을 생생히 살려요.']),
    (10, None, ["'위층 다락방 창문 좀 보세요, 케일럽이 벌써 세 번이나 셔츠를 갈아입었어요!' 동작을 세 차례 반복했다는 횟수 표현은 복수 명사를 쓴", (None, 'three times'), '구절을 문장 끝에 붙여 긴장한 모습을 재미있게 전해 줘요.']),
    (11, None, ["'해나, 케일럽이 나무 마룻바닥을 다 닳게 만들기 전에 얼른 가서 말을 걸어 봐요!' 서성이느라 바닥이나 신발이 해지고 닳아 없어진다는 뜻은 구동사", (None, 'wears out'), '표현으로 초조한 발걸음을 익살스럽게 비유해요.']),
]
