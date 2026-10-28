# Authoring module for kukhnya-s01e12-scene-03.
ID = 'kukhnya-s01e12-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 3
TITLE = 'Пустое место  (An Empty Place)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = 'Max follows Vika into her office to say sorry for the trick. It goes badly, because she is not in the mood for jokes. Listen to it in Russian before we pick it apart.'
OPENER = 'Back through it, to see how each answer of hers closes another door.'
TRANSITION = 'Now the scene from beginning to end, without interruptions.'
OUTRO = "Max leaves with 'empty place' still ringing in his ears. Play it again and listen for the moment he drops back to the polite 'you'."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Вика, послушай, нам было так хорошо вместе.', 'Vika, listen, it was so good for us together.', [(16, 'Вик, ты что-то пишешь, пошутил.'), (17, 'Слушай, нам было так трогательно.')], ''),
    ('vika', 'Слушай меня внимательно, мой дорогой друг.', 'Listen to me carefully, my dear friend.', [(19, 'Послушай, можешь шутить сколько угодно')], ''),
    ('max', 'Что с тобой? Ты такая злая сегодня.', 'What is with you? You are so angry today.', [(18, 'что с тобой ты такой?')], ''),
    ('vika', 'Шути свои дурацкие шутки на кухне!', 'Joke your stupid jokes in the kitchen!', [(20, 'как ты, вот там, на кухне, за дверью.')], ''),
    ('max', 'Зачем ты так грубо со мной говоришь?', 'Why are you talking to me so rudely?', [], ''),
    ('vika', 'Там за дверью много таких же идиотов.', 'There are many of the same idiots behind the door.', [(19, 'только в компании таких же идиотов,')], ''),
    ('max', 'Но я принёс нам билеты в кино.', 'But I brought us tickets to the cinema.', [], ''),
    ('vika', 'Мне не интересны твои билеты в кино.', 'I am not interested in your tickets to the cinema.', [(21, 'Мне не интересны твои шутки и твои билеты в кино.')], ''),
    ('max', 'Почему ты не хочешь пойти со мной?', 'Why do you not want to go with me?', [], ''),
    ('vika', 'Потому что ты для меня пустое место.', 'Because you are an empty place to me.', [(22, 'Ты для меня пустое место.')], ''),
    ('max', 'Пустое место? Ты очень добрая девушка.', 'An empty place? You are a very kind girl.', [(24, 'Пустое место, значит?')], ''),
    ('vika', 'Ты всё понял? А теперь уйди отсюда.', 'Have you understood everything? And now leave from here.', [(23, 'Понял?'), (21, 'А ко мне не лезь.')], ''),
    ('max', 'Ладно, извините, я ухожу прямо сейчас.', 'Alright, excuse me, I am leaving right now.', [(26, 'Ладно, извините.')], ''),
]
WALK = [
    (0, None, "'Vika, listen, it was so good for us together.' 'Listen' is the order to a friend. 'Nam bylo khorosho' is literally 'to us it was good': the people go in the 'to' form, 'nam', and 'khorosho' is the plain 'good'."),
    (1, None, "'Listen to me carefully, my dear friend.' It's the same action as Max's 'listen', minus the 'po' at the front. 'Dear' also means 'expensive' in Russian, and here Vika means it sarcastically."),
    (2, None, "'What is with you? You are so angry today.' 'What with you' is how Russians say 'what's wrong with you?'. 'Angry' ends in 'aya' because Max is talking about a woman."),
    (3, None, "'Joke your stupid jokes in the kitchen!' 'Joke' and 'jokes' come from one root. 'Duratskie', stupid, is built from 'durak', fool, so it's close to 'fool-ish'. 'Svoi' means 'your own'."),
    (4, None, "'Why are you talking to me so rudely?' This is a different 'why' from the usual one: 'zachem' asks 'what for'. 'With me' is 'so mnoy', where 'so' is just 'with' with an extra vowel."),
    (5, None, "'There are many of the same idiots behind the door.' After 'many', the next word takes a special ending, which is why 'idiots' finishes in 'ov'. 'Za dveryu' is 'behind the door', and after 'za' meaning 'behind', 'dver' takes the 'yu' ending."),
    (6, None, "'But I brought us tickets to the cinema.' 'Brought' ends in a consonant because Max is a man. It means 'carried here', the one you'd use for a gift or a delivery."),
    (7, None, "'I am not interested in your tickets to the cinema.' Vika doesn't say 'I'. She says 'mne ne interesny', 'to me not interesting'. 'Your' is 'tvoi', for someone you call 'ty'."),
    (8, None, "'Why do you not want to go with me?' 'Khochesh' is 'you want', and 'khochu' would be 'I want'. 'To go' follows it in its basic shape, just like English."),
    (9, None, "'Because you are an empty place to me.' 'Potomu chto', because, shares its start with 'pochemu', why. 'Empty place' is an idiom for a nobody, and 'empty' ends in 'oe' to match 'mesto'."),
    (10, None, "'An empty place? You are a very kind girl.' Max repeats her words as a question, like an echo. 'Kind' is sarcasm, and it's the opposite of what he feels."),
    (11, None, "'Have you understood everything? And now leave from here.' 'Understood' ends in 'l' because Max is a man. 'Uydi' is an order meaning 'go away', and 'from here' is a single word in Russian."),
    (12, None, "'Alright, excuse me, I am leaving right now.' Max switches to the polite 'excuse me', the form you'd use to a boss or a stranger. It tells you he has backed off and put some distance between them."),
]
