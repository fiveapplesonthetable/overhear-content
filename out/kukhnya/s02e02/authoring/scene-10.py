# Authoring module for kukhnya-s02e02-scene-10.
ID = 'kukhnya-s02e02-scene-10'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 2
SCENE = 10
TITLE = "Отец Насти  (Nastya's Father)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nastya_father': 'Отец Насти'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.02'
SOURCE_FILE = 'sources/kukhnya/s02/e02.ru.dual.srt'
INTRO = "An angry man comes looking for Kostya. Max opens the door and a case of mistaken identity leads to threats. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the exchange around Nastya's Father line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "An angry man comes looking for Kostya. Next time you watch the episode, listen for the Russian expressions for 'internet' and 'to fix' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'До свидания!')
STORY = [
    ('max', 'Здравствуйте.', 'Hello.', [(163, 'Здравствуйте')], ''),
    ('nastya_father', 'Константин Анисимов?', 'Konstantin Anisimov?', [(163, 'Константин Анисимов')], ''),
    ('max', 'Да, это я.', 'Yes, that is me.', [(164, 'Да, это я')], ''),
    ('max', 'А вы интернет чинить?', 'Are you here to fix the internet?', [(164, 'А вы интернат чинить')], ''),
    ('nastya_father', 'Я отец Насти.', "I am Nastya's father.", [], ''),
    ('nastya_father', 'Обидишь Настю, я из тебя колбасу сделаю.', 'If you hurt Nastya, I will turn you into sausage.', [(172, 'Обидишь Настю, я из тебя колбасу сделаю')], ''),
    ('max', 'Подождите.', 'Wait.', [(174, 'Подождите')], ''),
    ('max', 'Вы неправильно поняли.', 'You understood incorrectly.', [(174, 'вы неправильно поняли')], ''),
    ('max', 'Я не Костя.', 'I am not Kostya.', [(174, 'Я не Костя')], ''),
    ('max', 'Я Макс.', 'I am Max.', [(174, 'я Макс')], ''),
    ('max', 'А я интернет чинить.', 'And I am here to fix the internet.', [(179, 'я интернет чинить')], ''),
    ('max', 'Кто из вас Константин?', 'Which one of you is Konstantin?', [(180, 'А кто из вас Константин')], ''),
    ('nastya_father', 'Я.', 'Me.', [(181, 'Я')], ''),
]
WALK = [
    (0, None, "'Hello.' Opening the apartment door to a burly stranger, Max greets him politely."),
    (1, None, "'Konstantin Anisimov?' Here, Nastya's father turns a statement into a question purely through rising intonation on the word meaning 'Konstantin', followed by 'Anisimov'."),
    (2, None, "'Yes, that is me.' When the man asks for Konstantin Anisimov, Max carelessly says yes to sign for whatever it is."),
    (3, None, "'Are you here to fix the internet?' Expecting a technician, Max asks if the man came to fix their internet."),
    (4, None, "'I am Nastya's father.' The worst possible answer for Kostya's roommate."),
    (5, None, "'If you hurt Nastya, I will turn you into sausage.' After revealing he is Nastya's father, the man threatens to turn 'Konstantin' into sausage if he ever hurts her."),
    (6, None, "'Wait.' Terrified by the threat, Max tells the angry father to wait a second."),
    (7, None, "'You understood incorrectly.' He scrambles to explain that there has been a huge misunderstanding."),
    (8, None, "'I am not Kostya.' Max blurts out that he is not actually Kostya."),
    (9, None, "'I am Max.' He introduces himself by his real name, Max."),
    (10, None, "'And I am here to fix the internet.' Panicking further, Max even pretends he is only the internet repairman himself."),
    (11, None, "'Which one of you is Konstantin?' Looking around the room in confusion, Max asks who is supposed to be Konstantin."),
    (12, None, "'Me.' Meanwhile, Nastya's father delivers a punchy one-word reaction built around the Russian word meaning 'I'."),
]
