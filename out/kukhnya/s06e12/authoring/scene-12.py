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
    (0, None, '\'Viktor, and how will this serum get to the bookmaker?\' Mikhail inquires earnestly as they speak, putting "kak" ("how") alongside "syvorotka" ("serum") in a tight, everyday turn of phrase.'),
    (1, None, '\'Chef, a guest arrived there for a free lunch from the chef.\' Nikita brings a grounded view toward Mikhail, anchoring the Russian line on "tam" ("there") and "prishyol" ("came, have come") without extra filler.'),
    (2, None, '\'Thank you, Nikita, consider the serum already delivered!\' Barinov offers a candid footing in the conversation, linking "spasibo" ("thank you"), "schitay" ("consider, count it"), and "syvorotka" ("serum") in one brisk exchange.'),
    (3, None, '\'Well what, Misha, are you betting with me today?\' Barinov asks candidly without a pause, anchoring the Russian line on "segodnya" ("today") and "stavish" ("are betting") without extra filler.'),
    (4, None, '\'No, I pass, I have no money right now.\' Mikhail shows a thoughtful mood in their talk, leaning on "pas" ("pass") before closing the thought with "seychas" ("now").'),
    (5, None, '\'Chefs, tell me, who set such a strong mode on the oven?\' Barinov questions pointedly to Nikita here, leaning on "povara" ("cook") before closing the thought with "skazhite" ("tell").'),
    (6, None, '\'Senya, admit it, was it you who put the meat in the oven today?\' Barinov wonders frankly in the scene, building the phrase around "priznavaysya" ("confess") and "segodnya" ("today") for a crisp, natural delivery.'),
    (7, None, '\'No, chef, I did not even go near the oven today.\' Nikita sustains a sharp bearing in this beat, joining "segodnya" ("today") to "voobshche" ("at all") so every word pulls its weight.'),
    (8, None, '\'Then tell me immediately, who did this today?\' Barinov prompts sharply beside Mikhail, combining "togda" ("back then") and "skazhite" ("tell") so the key meaning lands right away.'),
    (9, None, '\'Where is Lyova, did he really ruin the whole dish again?\' Barinov questions evenly at this point, combining "gde" ("where") and "opyat" ("again") so the key meaning lands right away.'),
    (10, None, '\'Alright, Viktor, then I will go about my business.\' Mikhail offers an easygoing tack in the conversation, joining "togda" ("back then") to "poydu" ("go") so every word pulls its weight.'),
    (11, None, '\'Go ahead, go, and meanwhile I will prepare soup for the guest!\' Barinov projects an earnest manner at once, putting "davay" ("let\'s") alongside "idi" ("go") in a tight, everyday turn of phrase.'),
]
