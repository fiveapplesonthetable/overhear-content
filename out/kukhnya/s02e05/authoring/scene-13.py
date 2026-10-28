# Authoring module for kukhnya-s02e05-scene-13.
ID = 'kukhnya-s02e05-scene-13'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 5
SCENE = 13
TITLE = 'Звонок из больницы  (The Call from the Hospital)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nastya': 'Настя', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.05'
SOURCE_FILE = 'sources/kukhnya/s02/e05.ru.srt'
INTRO = 'Resting in a hospital ward after having his stomach pumped, Max panics when his phone rings and asks his hospital roommate to pretend to be a doctor and say Max wandered off. Seconds later, Max takes the phone back and realizes that the caller was actually Sasha, while he still needs an excuse for Vika.'
OPENER = "Now let's go back through the conversation line by line."
TRANSITION = "Alright, let's hear the whole conversation once more from start to finish."
OUTRO = 'That wraps up this scene as taken to the hospital with food poisoning, Max has a fellow patient tell Vika on the phone that he went missing, only to realize he accidentally pulled the prank on Sasha instead. Until next time!'
CLOSING = ('max', 'Хорошего дня!')
STORY = [
    ('max', 'Алло, здравствуйте.', 'Hello, good afternoon.', [(208, 'Алло, здравствуйте')], ''),
    ('vika', 'Сейчас не может подойти.', 'He cannot come to the phone right now.', [(210, 'Сейчас не может подойти')], ''),
    ('nastya', 'Здрасте, я его друг.', 'Hello, I am a friend of his.', [(211, 'Здрасте, я его друг')], ''),
    ('max', 'О, хорошо, что вы позвонили.', 'Oh, it is good that you called.', [(212, 'О, хорошо, что вы позвонили')], ''),
    ('vika', 'У меня для вас плохие новости.', 'I have bad news for you.', [(213, 'У меня для вас плохие новости')], ''),
    ('nastya', 'Мы его потеряли.', 'We lost him.', [(214, 'Мы его потеряли')], ''),
    ('max', 'Вышел в коридор, куда-то делся.', 'He walked out into the hallway and disappeared somewhere.', [(215, 'Вышел в коридор, куда-то делся')], ''),
    ('vika', 'Теперь не можем его найти.', 'Now we cannot find him anywhere.', [(216, 'Теперь не можем его найти')], ''),
    ('nastya', 'Подождите, так он живой?', 'Wait a second, so he is alive?', [(217, 'Подождите, так он живой')], ''),
    ('max', 'Слушай, это ты так пошутил?', 'Listen, was that you playing a prank?', [(219, 'это ты. Слушай')], 'adapted'),
    ('vika', 'Ну что, ты где?', 'Well, where are you?', [(220, 'Ну что, ты где')], ''),
    ('nastya', 'Походу, что-то сел не то.', 'It looks like I ate something bad.', [(222, 'Походу, что-то сел не то')], ''),
    ('max', 'Вот лежу, отдыхаю.', 'So here I am lying down and resting.', [(223, 'Вот лежу, отдыхаю')], ''),
]
WALK = [
    (0, None, "'Hello, good afternoon.' Over the kitchen and the moment, Max answers Nastya without a second thought."),
    (1, None, "'He cannot come to the phone right now.' Noting that he cannot come to the phone right now keeps Vika's side of the story simple and clear."),
    (2, None, "'Hello, I am a friend of his.' Realizing that she is a friend changes how Nastya handles the situation."),
    (3, None, "'Oh, it is good that you called.' Admitting that it is good that Nastya called shows Max being honest for a change."),
    (4, None, '\'I have bad news for you.\' Claiming that she has bad news for Max sounds confident, even if Max has doubts. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (5, None, "'We lost him.' Once they lost him, Nastya can finally tell Max what she means."),
    (6, None, "'He walked out into the hallway and disappeared somewhere.' Adding that he walked out into the hallway and disappeared somewhere fills in the missing piece for Nastya."),
    (7, None, "'Now we cannot find him anywhere.' Here refusing to find him anywhere sets up the next turn in their exchange."),
    (8, None, '\'Wait a second, so he is alive?\' Asking whether a second so he is alive puts Max right on the defensive. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (9, None, "'Listen, was that you playing a prank?' Asking whether that Nastya playing a prank cuts straight through the tension between Max and Nastya."),
    (10, None, '\'Well, where are you?\' Wondering where Max is is how Vika puts Max on the spot. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (11, None, "'It looks like I ate something bad.' Because it looks like she ate something bad, Nastya treats the matter as settled."),
    (12, None, "'So here I am lying down and resting.' Explaining that here he is lying down and resting lays the cards on the table for Nastya."),
]
