# Authoring module for kukhnya-s06e10-scene-06.
ID = 'kukhnya-s06e10-scene-06'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 10
SCENE = 6
TITLE = 'Луковый суп с сюрпризом  (Onion Soup with a Surprise)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.10'
SOURCE_FILE = 'sources/kukhnya/s06/e10.ru.srt'
INTRO = 'Chef Barinov visits Eleonora in her suite carrying a bottle of wine and a hot bowl of her favorite French onion soup. Eleonora suspiciously wonders if he drugged the wine to send her to the clinic—not realizing he put the sleeping pills in the soup.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Once Eleonora dozes off after eating the soup, Barinov hands her over to the clinic orderlies and heads down to Elena's ex-husband's wedding banquet. See you next time!"
CLOSING = ('barinov', 'До завтра!')
STORY = [
    ('eleonora', 'Привет, кроме шеф-повара некому бутылку принести?', 'Hello, is there nobody besides the head chef to bring a bottle?', [(78, 'Привет'), (79, 'Что, кроме шеф-повара уже некому бутылку привезти')], 'adapted'),
    ('barinov', 'Ты сильно удивишься, но я волнуюсь за тебя.', 'You will be very surprised, but I am worried about you.', [(80, 'Ты, конечно, сильно удивишься'), (81, 'но мне не плевать на твое здоровье')], 'adapted'),
    ('eleonora', 'Неужели ты сам меня сегодня лечить пришёл?', 'Did you really come to treat me yourself today?', [(82, 'И ты меня лечить пришел')], 'adapted'),
    ('barinov', 'Да, я пришёл к тебе с горячим супом.', 'Yes, I came to you with hot soup.', [(83, 'Да. С супом')], 'adapted'),
    ('barinov', 'Ведь ты уже четыре дня нормально не ешь.', 'After all, you have not eaten properly for four days already.', [(84, 'Ты четыре дня нормально не ешь')], 'adapted'),
    ('barinov', 'Я тебе твой любимый луковый суп приготовил.', 'I cooked your favorite onion soup for you.', [(85, 'А я тебе твой любимый луковый приготовил')], 'adapted'),
    ('barinov', 'И принёс бокал хорошего вина за твоё здоровье.', 'And brought a glass of good wine for your health.', [(86, 'за твое здоровье')], 'adapted'),
    ('eleonora', 'Раз ты такой заботливый, давай выпьем за здоровье.', 'Since you are so caring, let us drink to my health.', [(87, 'Ну, раз ты такой заботливый, давай выпьем за моё здоровье')], 'adapted'),
    ('eleonora', 'Или ты мне в вино что-то тайком подсыпал?', 'Or did you secretly slip something into my wine?', [(88, 'Или ты мне в вино что-то подсыпал')], 'adapted'),
    ('eleonora', 'Чтобы я уснула, а ты меня в психушку увёз?', 'So that I fall asleep and you take me to the mental clinic?', [(89, 'а ты меня в психушку вывез')], 'adapted'),
    ('barinov', 'Ну что ты говоришь, давай выпьем за тебя.', 'What are you saying, let us drink to you.', [(90, 'Давай за тебя')], 'adapted'),
    ('barinov', 'Я лекарство не в вино, а в суп подсыпал!', 'I slipped the medicine not into the wine, but into the soup!', [(91, 'В суп я подсыпал, Элечка, в суп')], 'adapted'),
]
WALK = [
    (0, None, '\'Hello, is there nobody besides the head chef to bring a bottle?\' Checking whether there nobody besides the head to bring a bottle is how Eleonora puts Barinov on the spot. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (1, None, "'You will be very surprised, but I am worried about you.' Noting that Eleonora will be very surprised but he is worried about Eleonora keeps Barinov's side of the story simple and clear."),
    (2, None, '\'Did you really come to treat me yourself today?\' By asking whether Barinov really come to treat her themselves today, Eleonora presses Barinov for a straight answer. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (3, None, '\'Yes, I came to you with hot soup.\' Admitting that he came to Eleonora with hot soup shows Barinov being honest for a change. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (4, None, "'After all, you have not eaten properly for four days already.' Saying that after all Eleonora has not eaten properly for four days already is how Barinov sets the tone with Eleonora."),
    (5, None, '\'I cooked your favorite onion soup for you.\' With the kitchen and wine in play, Barinov keeps this short reply brisk and direct. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (6, None, '\'And brought a glass of good wine for your health.\' Adding that brought a glass of good wine for Eleonora\'s health fills in the missing piece for Eleonora. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (7, None, "'Since you are so caring, let us drink to my health.' Eleonora tells Barinov that since Barinov is so caring let them drink to her health without dressing it up."),
    (8, None, '\'Or did you secretly slip something into my wine?\' Checking whether Barinov secretly slip something into her wine is how Eleonora puts Barinov on the spot. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (9, None, '\'So that I fall asleep and you take me to the mental clinic?\' Questioning whether that she falls asleep and Barinov takes her to the mental clinic is how Eleonora tests Barinov\'s story. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (10, None, "'What are you saying, let us drink to you.' Barinov tells Eleonora that what are Eleonora saying let them drink to Eleonora without dressing it up."),
    (11, None, "'I slipped the medicine not into the wine, but into the soup!' With the wine and work at stake, Barinov reacts without holding back. Russian puts the key word right up front so his emotion lands on the first beat."),
]
