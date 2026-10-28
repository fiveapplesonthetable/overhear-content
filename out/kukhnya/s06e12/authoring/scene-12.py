# Authoring module for kukhnya-s06e12-scene-12.
ID = 'kukhnya-s06e12-scene-12'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 12
SCENE = 12
TITLE = 'Подмена сыворотки  (Swapping the Serum)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'mikhail': 'Михаил', 'nikita': 'Никита'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.12'
SOURCE_FILE = 'sources/kukhnya/s06/e12.ru.srt'
INTRO = "When Nikita reports that the bookmaker guest has arrived claiming he won a free lunch from the chef, Barinov prepares a special dish for him. While Barinov yells at the chefs over a ruined roast, Mikhail dumps the truth serum into the staff's pasta pot and fills the vial with water."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Unaware that his vial now holds plain water while the staff pasta is loaded with belladonna, Barinov plates his soup for the bookmaker. See you next time!'
CLOSING = ('barinov', 'До встречи!')
STORY = [
    ('mikhail', 'Виктор, а как эта сыворотка попадёт к букмекеру?', 'Viktor, and how will this serum get to the bookmaker?', [(192, 'А как сыворотка попадет')], 'adapted'),
    ('nikita', 'Шеф, там пришёл гость на бесплатный обед от шефа.', 'Chef, a guest arrived there for a free lunch from the chef.', [(193, 'Шеф, там пришел гость и сказал, что выиграл бесплатный обед от шефа')], 'adapted'),
    ('barinov', 'Спасибо, Никита, считай, что сыворотка уже попала!', 'Thank you, Nikita, consider the serum already delivered!', [(194, 'Спасибо, Никита')], 'adapted'),
    ('barinov', 'Ну что, Миша, ты сегодня ставишь со мной?', 'Well what, Misha, are you betting with me today?', [(195, 'Ну что, ставишь')], 'adapted'),
    ('mikhail', 'Да нет, я пас, у меня сейчас нет денег.', 'No, I pass, I have no money right now.', [(195, 'Да нет, я пас')], 'adapted'),
    ('barinov', 'Повара, скажите, кто поставил такой сильный режим в печи?', 'Chefs, tell me, who set such a strong mode on the oven?', [(198, 'кто ж такой режим поставил')], 'adapted'),
    ('barinov', 'Сеня, признавайся, это ты сегодня ставил мясо в печь?', 'Senya, admit it, was it you who put the meat in the oven today?', [(199, 'Сеня'), (200, 'Ты ставил')], 'adapted'),
    ('nikita', 'Нет, шеф, я сегодня вообще к печи не подходил.', 'No, chef, I did not even go near the oven today.', [(201, 'Нет')], 'adapted'),
    ('barinov', 'Тогда скажите мне немедленно, кто это сегодня сделал?', 'Then tell me immediately, who did this today?', [(202, 'Кто это сделал')], 'adapted'),
    ('barinov', 'Где Лёва, неужели он опять всё блюдо испортил?', 'Where is Lyova, did he really ruin the whole dish again?', [(203, 'Где этот Лёва')], 'adapted'),
    ('mikhail', 'Ладно, Виктор, я тогда пойду по своим делам.', 'Alright, Viktor, then I will go about my business.', [(206, 'Ну, пойду я')], 'adapted'),
    ('barinov', 'Давай, иди, а я пока приготовлю суп для гостя!', 'Go ahead, go, and meanwhile I will prepare soup for the guest!', [(207, 'Давай-давай')], 'adapted'),
]
WALK = [
    (0, None, "'Viktor, and how will this serum get to the bookmaker?' Mikhail asks skeptically about what Barinov just brought up."),
    (1, None, '\'Chef, a guest arrived there for a free lunch from the chef.\' Turning to a guest during the talk, Nikita brings in "besplatnyy" ("free") to make the meaning unmistakable.'),
    (2, None, '\'Thank you, Nikita, consider the serum already delivered!\' Underscoring the serum right here, Barinov brings in "syvorotka" ("serum") to make the meaning unmistakable.'),
    (3, None, "'Well what, Misha, are you betting with me today?' Barinov wonders eagerly why things suddenly took this turn between them."),
    (4, None, '\'No, I pass, I have no money right now.\' Pointing to the money right here, Mikhail chooses "deneg" ("money", from the root "dengi") so Barinov hears the exact meaning.'),
    (5, None, '\'Chefs, tell me, who set such a strong mode on the oven?\' Pointing to the cook with Mikhail, Barinov puts the question word "kto" right at the start so Mikhail hears the focus immediately.'),
    (6, None, "'Senya, admit it, was it you who put the meat in the oven today?' Barinov wonders briskly how Nikita expects that to work in practice."),
    (7, None, '\'No, chef, I did not even go near the oven today.\' Nikita responds firmly right here and reaches for the Russian word "voobshche" ("at all") right at the heart of the line.'),
    (8, None, '\'Then tell me immediately, who did this today?\' Turning boldly in front of Nikita, Barinov puts the question word "kto" right at the start so Nikita hears the focus immediately.'),
    (9, None, "'Where is Lyova, did he really ruin the whole dish again?' Barinov questions plainly where this conversation is heading next."),
    (10, None, '\'Alright, Viktor, then I will go about my business.\' Talking about his business on the spot, Mikhail chooses "delam" ("business", from the root "delo") so Barinov hears the exact meaning.'),
    (11, None, '\'Go ahead, go, and meanwhile I will prepare soup for the guest!\' Discussing the soup in front of Mikhail, Barinov starts with "davay" ("come on, let\'s") to invite Mikhail right into the action.'),
]
