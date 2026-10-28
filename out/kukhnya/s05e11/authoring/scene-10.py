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
OUTRO = "That brings the bar interception to a close. Notice the comparative adjective meaning something stronger to drink as Nastya reads back the grandfather's order. See you next time!"
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
    (0, None, "'Wait!' With the meat and shift at stake, Max reacts without holding back."),
    (1, None, '\'And what did my grandpa order?\' Asking what his order is how Max puts the guest on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, "'Some kind of roast meat.' Between the point and the meat, Nastya gives the guest a quick, grounded response."),
    (3, None, "'Something stronger to drink, about two hundred grams.' With the truth and order in play, Nastya keeps this short reply brisk and direct."),
    (4, None, "'And stewed fruit compote.' Around the truth and order, Nastya sets a calm, everyday tone with the guest."),
    (5, None, "'Got it. Do not bring the meat, only the compote.' Max mentions that do not bring the meat only the compote so the guest sees what is at stake."),
    (6, None, "'Alright, Max.' Between the truth and the order, Nastya gives the guest a quick, grounded response."),
    (7, None, '\'Here is your lunch, grandpa.\' Explaining that here is the guest\'s lunch lays the cards on the table for the guest. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (8, None, '\'Now that is service!\' Saying that that is service is how the guest takes charge of the moment. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (9, None, "'And where is my meat?' Asking where his meat is is how the guest puts Max on the spot."),
    (10, None, "'You are not allowed meat, grandpa.' Noting that the guest is not allowed meat keeps Max's side of the story simple and clear. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (11, None, "'Well alright, grandson.' Around the truth and conversation, the guest sets a calm, everyday tone with Max."),
]
