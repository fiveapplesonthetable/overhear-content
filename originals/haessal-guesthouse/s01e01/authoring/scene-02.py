# Authoring module for haessal-guesthouse-s01e01-scene-02.
ID = 'haessal-guesthouse-s01e01-scene-02'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 1
SCENE = 2
TITLE = '따뜻한 빵과 벨 소리 두 번  (Warm Rolls and Two Rings)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'mina': '미나', 'sora': '소라', 'junho': '준호'}
INTRO = "Five minutes later, the sweet smell of fresh bread drifts out from the small breakfast corner. Morning baker Sora carries over a warm basket of rolls to greet Mina and Junho. Let's listen in first."
OPENER = "Let's slow down and hear how each line works."
TRANSITION = "Now let's hear the whole conversation again at natural speed."
OUTRO = 'Mina has a warm roll in her hand and a friendly ally in the café corner. You will hear those casual and polite endings side by side in every episode. See you next time.'
CLOSING = ('sora', '안녕!')
STORY = [
    ('sora', '안녕! 네가 미나구나. 나는 주방에서 일하는 소라야.', 'Hello! You must be Mina. I am Sora from the kitchen.'),
    ('mina', '반가워요, 소라 씨! 맛있는 냄새가 나요!', 'Nice to meet you, Sora! Something smells delicious!'),
    ('sora', '갓 구운 모닝빵이야! 따뜻할 때 하나 먹어 봐.', 'Freshly baked morning rolls! Try one while it is warm.'),
    ('mina', '고마워요! 여기서 우리는 이름을 편하게 불러요?', 'Thank you! Do we call each other comfortably by name here?'),
    ('sora', '나랑은 항상 편하게 해! 딱딱한 존댓말은 손님한테만 써.', 'With me, always speak casually! Save stiff polite speech for the guests.'),
    ('junho', '소라 씨는 우리 골목 사람들하고 다 친구처럼 이야기해요.', 'Sora talks like an old friend with everyone in our alley.'),
    ('sora', '맛있는 커피하고 따뜻한 빵이 있으면 다 친해지거든!', 'Because good coffee and warm bread make everyone friendly!'),
    ('mina', '방금 무슨 종소리예요? 누가 두 번 눌렀어요!', 'What was that bell sound just now? Someone pressed it twice!'),
    ('junho', '아무도 없어요. 그건 사호실 초인종 소리예요.', 'Nobody is there. That is the buzzer from Room 4.'),
    ('sora', '사호실이 비어 있어도 오래된 전선 때문에 두 번 울려.', 'Even when Room 4 is empty, it rings twice because of the old wire.'),
    ('mina', '그럼 이 집이 혼자서 인사하는 거네요?', 'So this house says hello all by itself?'),
    ('sora', '맞아! 미나는 벌써 여기 식구 같아.', "That's right! You already feel like family here."),
]
WALK = [
    (0, None, ["'Hello! You must be Mina. I am Sora from the kitchen.' Dropping the final polite syllable turns ", (None, '안녕'), " into a friendly 'hi' or 'bye' among close colleagues."]),
    (1, None, ["'Nice to meet you, Sora! Something smells delicious!' Korean says a scent 'comes out', pairing ", (None, '냄새가'), ' with a tiny two-letter action word at the end.']),
    (2, None, ["'Freshly baked morning rolls! Try one while it is warm.' Adding 'see' onto 'eat' in ", (None, '먹어 봐'), " creates the natural Korean way to say 'try eating it'."]),
    (4, None, ["'With me, always speak casually! Save stiff polite speech for the guests.' Respectful everyday Korean is called ", (None, '존댓말은'), ', which Sora tells Mina to save for paying guests.']),
    (5, None, ["'Sora talks like an old friend with everyone in our alley.' Putting ", (None, '친구처럼'), " together builds 'like a friend' in a single tidy chunk."]),
    (8, None, ["'Nobody is there. That is the buzzer from Room 4.' Pairing ", (None, '아무도'), " with 'not exist' is how Korean says 'nobody at all'."]),
    (10, None, ["'So this house says hello all by itself?' Look at ", (None, '혼자서'), ", the everyday word for doing something alone or on one's own."]),
    (11, None, ["'That's right! You already feel like family here.' Warm Korean workplaces use ", (None, '식구'), ", literally 'mouths who eat together', to mean household or family."]),
]
