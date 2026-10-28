# Authoring module for kukhnya-s05e11-scene-10.
ID = 'kukhnya-s05e11-scene-10'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 11
SCENE = 10
TITLE = "Заказ деда  (Grandpa's Order)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.11'
SOURCE_FILE = 'sources/kukhnya/s05/e11.ru.srt'
INTRO = 'The moment his grandmother steps out the door, Max stops Nastya at the bar to ask what his grandfather just ordered. Learning that the old man asked for roast meat and two hundred grams of strong alcohol, Max cancels the order and serves him steamed diet food instead.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "That brings the bar interception to a close. Notice the comparison word meaning something stronger to drink as Nastya reads back the grandfather's order. See you next time!"
CLOSING = ('max', 'Увидимся!')
STORY = [
    ('max', 'Погоди!', 'Wait!', [(150, 'Погоди')], 'adapted'),
    ('max', 'А что мой дед заказал?', 'And what did my grandpa order?', [(151, 'А что мой дед заказал')], 'adapted'),
    ('nastya', 'Мяса жареного какого-нибудь.', 'Some kind of roast meat.', [(152, 'Мясо жареного какого-нибудь')], 'adapted'),
    ('nastya', 'Выпить что-нибудь покрепче, грамм двести.', 'Something stronger to drink, about two hundred grams.', [(153, 'Выпить что-нибудь покрепче, грамм двести')], 'adapted'),
    ('nastya', 'И компот.', 'And stewed fruit compote.', [(154, 'И компот')], 'adapted'),
    ('max', 'Ясно. Мясо не неси, только компот.', 'Got it. Do not bring the meat, only the compote.', [(155, 'Ясно'), (154, 'И компот')], 'adapted'),
    ('nastya', 'Хорошо, Макс.', 'Alright, Max.', [(155, 'Ясно')], 'adapted'),
    ('max', 'Вот твой обед, дед.', 'Here is your lunch, grandpa.', [(151, 'мой дед')], 'adapted'),
    ('guest', 'Вот это сервис!', 'Now that is service!', [(156, 'Вот это сервис')], 'adapted'),
    ('guest', 'А где же моё мясо?', 'And where is my meat?', [(152, 'Мясо')], 'adapted'),
    ('max', 'Тебе нельзя мясо, дед.', 'You are not allowed meat, grandpa.', [(151, 'дед')], 'adapted'),
    ('guest', 'Ну ладно, внучок.', 'Well alright, grandson.', [(156, 'Вот это сервис')], 'adapted'),
]
WALK = [
    (0, None, '\'Wait!\' Max grounds this vivid term with the guest: "pogodi" means "wait" (from "pogodit"), giving the line its exact edge.'),
    (1, None, '\'And what did my grandpa order?\' Max frames this line at once: putting the question word "chto" right at the front of the line lets Nastya hear the point of the question on the very first beat.'),
    (2, None, "'Some kind of roast meat.' Nastya counters bluntly with a smile, letting the remark speak for itself."),
    (3, None, '\'Something stronger to drink, about two hundred grams.\' Nastya stresses this key choice in reply: "pokrepche" means "stronger" (from "krepkiy"), giving the line its exact edge.'),
    (4, None, "'And stewed fruit compote.' Nastya voices that remark toward the guest: spoken Russian trims this down to just 2 words, dropping the extra helper words that English has to spell out."),
    (5, None, "'Got it. Do not bring the meat, only the compote.' Max counters sharply in this moment, making his position completely clear."),
    (6, None, '\'Alright, Max.\' Nastya sharpens one telling choice in earnest: "khorosho" means "good, fine", and it carries the main weight of what Nastya is saying.'),
    (7, None, '\'Here is your lunch, grandpa.\' Max aims the thought right away: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (8, None, "'Now that is service!' The guest proceeds pointedly facing Max, refusing to let the moment slip past."),
    (9, None, '\'And where is my meat?\' The guest chooses this sharp detail right here: "myaso" means "meat", and it carries the main weight of what the guest is saying.'),
    (10, None, '\'You are not allowed meat, grandpa.\' Max makes the remark with warmth: the single Russian word "nelzya" ("it is not allowed, one must not") sets up the whole statement without needing a separate word for "it is".'),
    (11, None, "'Well alright, grandson.' The guest speaks steadily as they talk, shifting the whole mood of the room in a single beat."),
]
