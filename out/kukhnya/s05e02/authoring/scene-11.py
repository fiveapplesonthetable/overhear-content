# Authoring module for kukhnya-s05e02-scene-11.
ID = 'kukhnya-s05e02-scene-11'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 2
SCENE = 11
TITLE = 'Номер люкс для мнимого ревизора  (A Luxury Suite for the Supposed Inspector)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'mikhail': 'Михаил', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.02'
SOURCE_FILE = 'sources/kukhnya/s05/e02.ru.srt'
INTRO = 'Eager to impress the supposed inspector, Mikhail upgrades the bewildered guest to a luxury suite and Chef Barinov personally brings him room service, while Vika quietly admits she invented the story to stop their feud. Listen to the scene.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that shows Mikhail and Barinov bending over backward for an ordinary guest. Notice the idiom 'golden hands' to praise someone's skill. Until next time!"
CLOSING = ('barinov', 'Хорошего дня!')
STORY = [
    ('mikhail', 'Добрый день! Рады приветствовать вас в нашем отеле.', 'Good afternoon! We are glad to welcome you to our hotel.', [(118, 'Добрый день'), (118, 'рады приветствовать вас в нашем отеле')], 'adapted'),
    ('mikhail', 'Меня зовут Михаил. Чем я могу вам помочь?', 'My name is Mikhail. How can I help you?', [(119, 'Меня зовут Михаил. Чем я могу вам помочь?')], 'verbatim'),
    ('barinov', 'Мой номер до сих пор не готов.', 'My room is still not ready.', [(120, 'мой номер до сих пор не готов')], 'verbatim'),
    ('mikhail', 'Примите наши глубокие извинения.', 'Please accept our deepest apologies.', [(121, 'В качестве наших'), (121, 'извинений')], 'adapted'),
    ('mikhail', 'Я могу вам предложить номер люкс.', 'I can offer you a luxury suite.', [(121, 'я могу вам предложить номер')], 'adapted'),
    ('mikhail', 'Позвольте вас туда проводить.', 'Allow me to escort you there.', [(122, 'Позвольте вас проводить')], 'adapted'),
    ('vika', 'Это и есть тот самый тайный гость?', 'Is that really the secret guest?', [(123, 'Это и есть тот самый тайный гость?')], 'verbatim'),
    ('vika', 'Нет, это просто обычный гость.', 'No, he is just an ordinary guest.', [(124, 'обычный гость')], 'adapted'),
    ('vika', 'Иначе этих двоих было не примирить.', 'Otherwise there was no way to reconcile those two.', [(124, 'этих двоих было не примирить')], 'adapted'),
    ('barinov', 'Обслуживание прямо в номер.', 'Room service straight to the room.', [(125, 'Обслуживание в номер')], 'adapted'),
    ('barinov', 'Это специальная услуга от шефа.', 'This is a special service from the chef.', [(126, 'Услуга шеф')], 'adapted'),
    ('mikhail', 'У вас просто золотые руки.', 'You simply have golden hands.', [(129, 'У вас золотые руки')], 'adapted'),
    ('barinov', 'Нет, спасибо, я на работе.', 'No, thank you, I am at work.', [(130, 'нет, спасибо'), (131, 'Я на работе')], 'adapted'),
]
WALK = [
    (0, None, "'Good afternoon! We are glad to welcome you to our hotel.' Mikhail speaks frankly without holding back, to clear the air between them once and for all."),
    (1, None, "'My name is Mikhail. How can I help you?' Mikhail checks promptly where this conversation is heading next."),
    (2, None, '\'My room is still not ready.\' Highlighting the number to Mikhail, Barinov centers the remark on "nomer" ("number") without any extra fuss.'),
    (3, None, "'Please accept our deepest apologies.' Turning to the apologies right here, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (4, None, "'I can offer you a luxury suite.' Mikhail answers promptly without holding back, so Barinov knows he is not just making small talk."),
    (5, None, '\'Allow me to escort you there.\' Mikhail replies promptly on the spot and chooses "pozvolte" ("allow me", from the root "pozvolit") so Vika hears the exact meaning.'),
    (6, None, "'Is that really the secret guest?' Making clear how secret things are on the spot, Vika keeps normal statement word order here, turning the line into a question for Mikhail purely through rising pitch."),
    (7, None, "'No, he is just an ordinary guest.' Vika fires back openly with Mikhail, so Mikhail knows she is not just making small talk."),
    (8, None, '\'Otherwise there was no way to reconcile those two.\' Vika speaks up readily with Barinov and centers the remark on "primirit" ("to reconcile") without any extra fuss.'),
    (9, None, "'Room service straight to the room.' Focusing on the service at once, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (10, None, "'This is a special service from the chef.' Barinov chimes in earnestly facing Mikhail, watching Mikhail's face to see how the news lands."),
    (11, None, '\'You simply have golden hands.\' Highlighting the hands right here, Mikhail chooses "zolotyye" ("golden", from the root "zolotoy") so Barinov hears the exact meaning.'),
    (12, None, '\'No, thank you, I am at work.\' Mentioning the thank at once, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
]
