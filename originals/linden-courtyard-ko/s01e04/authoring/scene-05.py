# Authoring module for linden-courtyard-ko-s01e04-scene-05.
ID = 'linden-courtyard-ko-s01e04-scene-05'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 4
SCENE = 5
TITLE = 'Five-Star Showers  (별 다섯 개짜리 온수 샤워)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'arthur': 'Arthur', 'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = '간발의 차로 온수가 살아난 덕에 케일럽은 상쾌한 얼굴로 아침 식사 자리에 내려와 뜨거운 샤워를 칭찬해요. 신이 난 아서가 무심코 십 점 만점 이야기를 꺼내면서 어젯밤 수첩을 봤다는 사실이 드러나고 맙니다. 유쾌한 대화를 들어 보세요.'
OPENER = '카페 모퉁이에서 벌어진 아침 대화를 한 문장씩 함께 들여다볼까요.'
TRANSITION = '이제 웃음이 번지는 이 장면을 자연스러운 호흡으로 다시 들어 보세요.'
OUTRO = '케일럽이 호텔 평가원이 아니라는 뜻밖의 반전과 함께 세 사람이 안뜰로 향했어요. 과연 가죽 수첩에 적힌 십 점 만점에 구 점은 무엇을 뜻하는 점수였을까요. 곧 이어지는 다음 장면에서 밝혀집니다.'
CLOSING = ('caleb', 'Take care!')
STORY = [
    ('caleb', 'Good morning, Hannah! Good morning, sir! What a bright morning after the rain.', '좋은 아침이에요, 해나! 좋은 아침입니다, 사장님! 비가 그친 뒤라 정말 화창한 아침이네요.'),
    ('hannah', 'Good morning, Caleb! Did you sleep well under the roof beams?', '좋은 아침이에요, 케일럽! 지붕 들보 아래서 푹 주무셨나요?'),
    ('caleb', 'Best sleep I have had all month, and the shower water was wonderfully hot!', '이번 달 통틀어 가장 꿀잠을 잤고, 샤워기 물도 더할 나위 없이 뜨거웠어요!'),
    ('arthur', 'Hot! Hear that, Hannah? Reliable, modern, five-star hot water!', '뜨거웠다고요! 들었죠, 해나? 믿음직하고 현대적인 별 다섯 개짜리 온수랍니다!'),
    ('caleb', 'Old brick buildings usually take ages to warm up on the top floor.', '오래된 벽돌 건물은 보통 꼭대기 층까지 물이 데워지는 데 한세월이 걸리거든요.'),
    ('arthur', "Please write that down! 'Hot water on the third floor: ten out of ten!'", '제발 그 말씀 꼭 적어 주세요! 삼 층 온수 점수, 십 점 만점에 십 점이라고요!'),
    ('caleb', 'Excuse me? Ten out of ten?', '네? 십 점 만점에 십 점이라니요?'),
    ('hannah', 'What Arthur means is... we hope every guest feels ten out of ten here!', '아서 사장님 말씀 뜻은요, 모든 손님이 여기서 십 점 만점 기분을 느끼시길 바란다는 거예요!'),
    ('arthur', 'No, Hannah, let us be honest professionals! Sir, we respect the Portland Travel Guide!', '아니에요, 해나, 우리 정직한 전문가답게 굽시다! 손님, 저희는 포틀랜드 여행 안내서를 존중합니다!'),
    ('caleb', 'The Portland Travel Guide? Wait, do you think I am a hotel inspector?', '포틀랜드 여행 안내서요? 잠깐만요, 저를 호텔 평가원이라고 생각하시는 건가요?'),
    ('hannah', "When your notebook fell open on the counter last night, we saw 'nine out of ten'...", '어젯밤 카운터에서 손님 수첩이 펼쳐졌을 때 십 점 만점에 구 점이라는 글씨를 봤거든요.'),
    ('caleb', 'Oh! Come outside to the courtyard for a minute. Let me show you what I really do!', '아하! 잠깐 안뜰 바깥으로 나와 보세요. 제가 실제로 무슨 일을 하는지 보여 드릴게요!'),
]
WALK = [
    (0, None, ["'좋은 아침이에요, 해나! 좋은 아침입니다, 사장님! 비가 그친 뒤라 정말 화창한 아침이네요.' 맑게 갠 아침 풍경을 보며 기분 좋게 터뜨리는 감탄문은", (None, 'What a bright morning'), '감탄사 뒤에 관사와 형용사, 명사를 차례로 얹어 상쾌한 인상을 완성해요.']),
    (1, None, ["'좋은 아침이에요, 케일럽! 지붕 들보 아래서 푹 주무셨나요?' 간밤에 잠자리가 편안했는지 아침 인사로 다정하게 안부를 챙기려면", (None, 'Did you sleep well'), '과거 의문문 끝에 부사를 붙여 숙면 여부를 살갑게 확인해 보세요.']),
    (2, None, ["'이번 달 통틀어 가장 꿀잠을 잤고, 샤워기 물도 더할 나위 없이 뜨거웠어요!' 이번 한 달 동안 겪은 경험을 최상급과 매끄럽게 이어 주느라", (None, 'I have had all month'), '현재완료 시제를 관계절로 덧붙여 최고의 숙면이었음을 강조했어요.']),
    (3, None, ["'뜨거웠다고요! 들었죠, 해나? 믿음직하고 현대적인 별 다섯 개짜리 온수랍니다!' 상대의 칭찬을 놓치지 않고 옆 사람에게 방금 들었냐며 의기양양하게 되묻는 말로", (None, 'Hear that'), '의문문 앞머리를 과감히 생략해 들뜬 현장 호흡을 살렸어요.']),
    (4, None, ["'오래된 벽돌 건물은 보통 꼭대기 층까지 물이 데워지는 데 한세월이 걸리거든요.' 시간이 아주 오래 걸린다고 일상 대화에서 살짝 과장해 재미있게 풀어내려면", (None, 'take ages'), '세월을 뜻하는 복수 명사를 써서 한참 걸린다는 느낌을 생생히 담아요.']),
    (5, None, ["'제발 그 말씀 꼭 적어 주세요! 삼 층 온수 점수, 십 점 만점에 십 점이라고요!' 잊지 않도록 종이나 수첩에 기록해 달라고 신나서 부탁하는 구동사는", (None, 'write that down'), '지시대명사를 동사와 부사 한가운데 넣어 리듬감 있게 발음해요.']),
    (6, None, ["'네? 십 점 만점에 십 점이라니요?' 상대방이 한 뜻밖의 말을 못 알아들었거나 깜짝 놀라 되물을 때 꺼내는 한마디로", (None, 'Excuse me'), '끝소리를 높여 주면 무슨 말씀이시냐고 정중히 되묻는 뜻이 돼요.']),
    (7, None, ["'아서 사장님 말씀 뜻은요, 모든 손님이 여기서 십 점 만점 기분을 느끼시길 바란다는 거예요!' 다른 사람의 실언을 수습하며 진짜 의도를 부드럽게 다시 풀어 줄 때는", (None, 'What Arthur means is'), '선행사를 품은 관계대명사 절을 주어로 삼아 차분히 설명을 이어 가요.']),
    (8, None, ["'아니에요, 해나, 우리 정직한 전문가답게 굽시다! 손님, 저희는 포틀랜드 여행 안내서를 존중합니다!' 우리 함께 어떤 태도를 갖추자고 격식 있게 제안하는 표현에서는", (None, 'let us be'), '줄임말 대신 두 단어를 또렷이 살려 진지하고 당당한 어조를 연출해요.']),
    (9, None, ["'포틀랜드 여행 안내서요? 잠깐만요, 저를 호텔 평가원이라고 생각하시는 건가요?' 숙박 시설을 암행 점검하고 등급을 매기는 조사관을 가리키는 명사구가", (None, 'a hotel inspector'), '단수 부정관사를 앞에 붙여 직업을 콕 집어 되물었어요.']),
    (10, None, ["'어젯밤 카운터에서 손님 수첩이 펼쳐졌을 때 십 점 만점에 구 점이라는 글씨를 봤거든요.' 바로 어제 저녁부터 밤사이를 가리킬 때는 전치사 없이", (None, 'last night'), '짧은 두 단어만 문장 끝에 놓아도 과거 시점이 자연스럽게 완성돼요.']),
    (11, None, ["'아하! 잠깐 안뜰 바깥으로 나와 보세요. 제가 실제로 무슨 일을 하는지 보여 드릴게요!' 오해를 풀기 위해 내가 직접 보여 주겠다고 흔쾌히 나서는 다정한 제안은", (None, 'Let me show you'), '사역동사 구문을 써서 부담 없이 상대를 안내할 때 참 유용해요.']),
]
