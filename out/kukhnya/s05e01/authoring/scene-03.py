# Authoring module for kukhnya-s05e01-scene-03.
ID = 'kukhnya-s05e01-scene-03'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 1
SCENE = 3
TITLE = "Услуга «Шеф в номер»  (The 'Chef to the Room' Service)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.01'
SOURCE_FILE = 'sources/kukhnya/s05/e01.ru.srt'
INTRO = 'In the kitchen of Restaurant Victor, Chef Barinov discovers a promotional flyer announcing that hotel guests can summon the head chef directly to their rooms. Listen to his clash with manager Mikhail Dzhekovich.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that brings the argument over Mikhail's marketing stunt to a close. Notice how Barinov turns Mikhail's own slogan back on him. Until next time!"
CLOSING = ('barinov', 'Увидимся!')
STORY = [
    ('lyova', 'Я пытался его предупредить.', 'I tried to warn him.', [(36, 'я пытался его предупредить')], 'verbatim'),
    ('barinov', 'Пошёл вон.', 'Get out.', [(38, 'Пошел')], 'adapted'),
    ('barinov', 'Это что за ерунда?', 'What kind of nonsense is this?', [(39, 'Это что за ерунда?')], 'verbatim'),
    ('mikhail', 'В нашем отеле действует новая услуга.', 'A new service operates in our hotel.', [(40, 'В нашем отеле действует услуга')], 'adapted'),
    ('mikhail', 'Это услуга для наших гостей.', 'This is a service for our guests.', [(40, 'услуга')], 'adapted'),
    ('mikhail', 'Вы сможете посмотреть на работу шефа.', "You will be able to watch the chef's work.", [(41, 'Вы сможете понаблюдать за работой')], 'adapted'),
    ('mikhail', 'Это не прерывает ваш отдых.', 'This does not interrupt your rest.', [(42, 'не прерывая ваш отдых')], 'adapted'),
    ('mikhail', 'Я принимаю это после завтрака.', 'I accept that after breakfast.', [(43, 'я принимаю после завтрака')], 'adapted'),
    ('mikhail', 'А сейчас извини.', 'And right now excuse me.', [(44, 'А сейчас извини')], 'verbatim'),
    ('barinov', 'Ты введи новую услугу.', 'You should introduce a new service.', [(45, 'ты введи новую услугу')], 'verbatim'),
    ('barinov', 'Управляющий идёт прямо в номер.', 'The hotel manager goes straight to the room.', [(46, 'Управляющий в номер')], 'adapted'),
    ('barinov', 'Не мешай нашему отдыху.', 'Do not disturb our rest.', [(47, 'вашего отдыха')], 'adapted'),
]
WALK = [
    (0, None, "'I tried to warn him.' Claiming that he tried to warn him sounds confident, even if Barinov has doubts."),
    (1, None, "'Get out.' Getting out is how Barinov lays out the situation for Lyova."),
    (2, None, '\'What kind of nonsense is this?\' Around the room and hotel, Barinov wants to know where Lyova really stands. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (3, None, "'A new service operates in our hotel.' Between the truth and the hotel, Mikhail gives Barinov a quick, grounded response."),
    (4, None, "'This is a service for our guests.' Noting that this is a service for their guests keeps Mikhail's side of the story simple and clear."),
    (5, None, '\'You will be able to watch the chef\'s work.\' Even though Barinov will be able to watch the work, Mikhail keeps a steady face in front of Barinov. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (6, None, '\'This does not interrupt your rest.\' Admitting that this does not interrupt Barinov\'s rest shows Mikhail being honest for a change. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (7, None, "'I accept that after breakfast.' Mentioning that he accepts that after breakfast moves the talk in a new direction."),
    (8, None, "'And right now excuse me.' With the room and hotel in play, Mikhail keeps this short reply brisk and direct."),
    (9, None, '\'You should introduce a new service.\' Adding that Lyova should introduce a new service fills in the missing piece for Lyova. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (10, None, "'The hotel manager goes straight to the room.' Barinov tells Lyova that the hotel manager goes straight to the room without dressing it up."),
    (11, None, "'Do not disturb our rest.' Since do not disturb their rest, Barinov does not waste words on excuses."),
]
