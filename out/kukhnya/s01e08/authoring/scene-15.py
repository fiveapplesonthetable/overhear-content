# Authoring module for kukhnya-s01e08-scene-15.
ID = 'kukhnya-s01e08-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 15
TITLE = 'Звонок Нагиеву  (Phone Call to Nagiyev)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "At Claude Monet, Nagiyev phones while he is away to ask after his dog, Tyson. Vika, the manager, takes the call and has to pretend all is well, though Tyson is lying lifeless in the storeroom. Max is listening. It's in Russian first."
OPENER = "Slowly now. Vika sounds cheerful on the phone, and Max can't believe his ears."
TRANSITION = "Here's the call again, without stopping."
OUTRO = "Vika's call is a model of phone manners: zdravstvuyte, podskazhite pozhaluysta, spasibo vam bolshoye, do svidaniya. And kak nazyvayetsya, 'what is it called', is a question you'll use every day. See you next time."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Да, здравствуйте, Дмитрий Владимирович!', 'Yes, hello, Dmitry Vladimirovich!', [(185, 'Да, Дмитрий Владимирович')], ''),
    ('vika', 'Тайсон чувствует себя прекрасно.', 'Tyson feels great.', [(186, 'Тайсон? Тайсон хорошо')], ''),
    ('vika', 'Он бегает и очень весело играет.', 'He runs around and plays very merrily.', [(187, 'Да, бегает'), (188, 'Такой веселый и гривый')], ''),
    ('max', 'Зачем ты так нагло врёшь?', 'Why are you lying so boldly?', [], ''),
    ('vika', 'Подскажите, пожалуйста, какая у него порода?', 'Could you tell me, please, what breed he is?', [(190, 'а вы не подскажете, что это за порода?')], ''),
    ('vika', 'Я просто влюбилась в эту собаку.', 'I simply fell in love with this dog.', [(191, 'я просто влюблена')], ''),
    ('vika', 'Как называется эта порода, ши-тцу?', 'What is this breed called, Shih Tzu?', [(195, 'А, ши-цу'), (196, 'Ши-цу')], ''),
    ('vika', 'Вы можете совсем не спешить обратно.', 'You do not need to rush back at all.', [(197, 'вы не спешите')], ''),
    ('vika', 'Мы с ним отлично ладим.', 'He and I get along wonderfully.', [(198, 'Мы с Таисиным прекрасно ладим')], ''),
    ('vika', 'Спасибо вам большое, до свидания!', 'Thank you very much, goodbye!', [(199, 'Да, да, спасибо'), (200, 'до свидания')], ''),
    ('max', 'И что теперь нам делать?', 'And what are we to do now?', [], ''),
    ('vika', 'Нужно срочно ехать покупать собаку!', 'We need to go buy a dog urgently!', [(201, 'Нужно ехать покупать собаку')], ''),
    ('max', 'Но где мы найдём такую собаку?', 'But where will we find such a dog?', [(202, 'Куда?')], ''),
]
WALK = [
    (0, None, ["'Yes, hello, Dmitry Vladimirovich!' When answering formal calls, the greeting ", ('vika', 'здравствуйте'), ' adds a polite tone of respect.']),
    (1, None, ["'Tyson feels great.' To describe someone feeling absolutely wonderful, say ", ('vika', 'прекрасно'), ' instead of just good.']),
    (2, None, ["'He runs around and plays very merrily.' For emphasizing an action done happily, ", ('vika', 'весело'), ' captures that pure sense of joy.']),
    (3, None, ["'Why are you lying so boldly?' In moments of utter shock, the expression ", ('max', 'нагло'), ' highlights how brazen a lie is.']),
    (4, None, ["'Could you tell me, please, what breed he is?' Asking about a specific animal type requires ", ('vika', 'порода'), ' to refer to its background.']),
    (5, None, ["'I simply fell in love with this dog.' Expressing strong affection is quite easy with ", ('vika', 'влюбилась'), ' to show falling completely in love.']),
    (6, None, ["'What is this breed called, Shih Tzu?' Finding out the correct name of things uses ", ('vika', 'называется'), ' to get the right answer.']),
    (7, None, ["'You do not need to rush back at all.' Telling someone there is no real rush involves ", ('vika', 'спешить'), ' to mean hurrying back quickly.']),
    (8, None, ["'He and I get along wonderfully.' Showing that two people get along really well takes ", ('vika', 'ладим'), ' for a smooth relationship.']),
    (9, None, ["'Thank you very much, goodbye!' Adding a lot of deep gratitude needs ", ('vika', 'большое'), ' right after giving your thanks.']),
    (10, None, ["'And what are we to do now?' figuring out the very next logical step requires ", ('max', 'теперь'), ' to focus clearly on the present.']),
    (11, None, ["'We need to go buy a dog urgently!' Handling a sudden emergency situation will feature ", ('vika', 'срочно'), ' to indicate an immediate action.']),
    (12, None, ["'But where will we find such a dog?' Looking forward to discovering a fast solution uses ", ('max', 'найдём'), ' for the uncertain search ahead.']),
]
