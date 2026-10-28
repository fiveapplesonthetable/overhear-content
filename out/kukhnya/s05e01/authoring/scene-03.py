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
    (0, None, "'I tried to warn him.' Lyova steps in openly with Barinov, refusing to let the moment slip past."),
    (1, None, '\'Get out.\' Barinov steps in candidly in front of Lyova and centers the thought on "poshyol" ("went, set off", from "poyti") without wasting a word.'),
    (2, None, '\'What kind of nonsense is this?\' Checking on the trifle with Mikhail, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (3, None, "'A new service operates in our hotel.' Mikhail speaks up plainly in this moment, making his position completely clear."),
    (4, None, '\'This is a service for our guests.\' Pointing to the favor right here, Mikhail reaches for the Russian word "usluga" ("favor, service") right at the heart of the line.'),
    (5, None, "'You will be able to watch the chef's work.' Mikhail speaks up calmly with a shrug, to clear the air between them once and for all."),
    (6, None, "'This does not interrupt your rest.' Mikhail steps in honestly in this moment, watching Barinov's face to see how the news lands."),
    (7, None, '\'I accept that after breakfast.\' Pointing to the breakfast in this beat, Mikhail centers the thought on "zavtraka" ("breakfast", from "zavtrak") without wasting a word.'),
    (8, None, '\'And right now excuse me.\' Mikhail directly drops this informal apology in front of Barinov using "izvini" ("sorry") — the casual singular apology you use with someone you know well.'),
    (9, None, "'You should introduce a new service.' Barinov chimes in wryly without any doubt, shifting the mood of the conversation in a single beat."),
    (10, None, '\'The hotel manager goes straight to the room.\' Mentioning the hotel manager in the exchange, Barinov brings in "upravlyayushchiy" ("manager") to make the meaning unmistakable.'),
    (11, None, "'Do not disturb our rest.' Mentioning his rest with Mikhail, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
]
