# Authoring module for kukhnya-s01e08-scene-14.
ID = 'kukhnya-s01e08-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 14
TITLE = 'Вежливый шеф  (The Polite Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'elena': 'Елена', 'sasha': 'Саша', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "With Barinov out of the way, Elena is running his kitchen at Claude Monet her own way. She speaks politely, calls the cooks by their full names, and nobody shouts. The cooks don't quite know what to make of it. It's in Russian first."
OPENER = 'Slowly now. Elena asks rather than shouts, even when the guests start to complain.'
TRANSITION = 'Now the whole quiet service again, at full speed.'
OUTRO = "Almost every instruction Elena gives uses the polite plural command form — 'please prepare', 'please ask', 'let us'. A boss who speaks that way is rare in any busy kitchen. See you next time."
CLOSING = ('elena', 'Пока!')
STORY = [
    ('elena', 'Фёдор, приготовьте две порции креветок.', 'Fyodor, prepare two portions of shrimp.', [(163, 'приготовьте, пожалуйста, еще две порции креветок')], ''),
    ('senya', 'Шеф должен кричать на поваров!', 'A chef should shout at cooks!', [(166, 'шеф должен орать на подчиненных')], ''),
    ('elena', 'Арсений, вы заслуживаете достойного обращения.', 'Arseny, you deserve respectful treatment.', [(169, 'вы профессионалы и заслуживаете достойного обращения')], ''),
    ('senya', 'Но на кухне нужна строгая дисциплина.', 'But strict discipline is needed in the kitchen.', [], ''),
    ('elena', 'У вас самое чистое рабочее место.', 'You have the cleanest workstation.', [(168, 'у вас самое чистое рабочее место')], ''),
    ('sasha', 'Где горячее блюдо для третьего столика?', 'Where is the hot dish for table three?', [(170, 'Где моя бобовая косуля, в конце концов')], ''),
    ('sasha', 'Гости ждут уже сорок минут!', 'The guests have been waiting forty minutes already!', [(176, 'Гости уже 40 минут')], ''),
    ('elena', 'Саша, спокойно, давайте глубоко дышать.', 'Sasha, calmly, let us breathe deeply.', [(172, 'спокойно, спокойно'), (173, 'Давайте дышать')], ''),
    ('elena', 'Это блюдо готовится больше часа.', 'This dish takes over an hour to cook.', [(178, 'готовится больше часа')], ''),
    ('sasha', 'Они грозятся уйти без оплаты.', 'They threaten to leave without paying.', [(171, 'Если я сегодня останусь без чаевых')], ''),
    ('elena', 'Попросите гостей подождать ещё немного.', 'Ask the guests to wait a little longer.', [(180, 'попросите их еще подождать')], ''),
    ('elena', 'Новый заказ: куропатка и грибы.', 'New order: partridge and mushrooms.', [(182, 'Новый заказ. Куропатка'), (183, 'грибами в белом соусе')], ''),
    ('senya', 'Мы всё сделаем вовремя, шеф!', 'We will make everything on time, chef!', [(184, 'Да, шеф')], ''),
]
WALK = [
    (0, None, ["'Fyodor, prepare two portions of shrimp.' Listen to how polite she sounds using ", ('elena', 'приготовьте'), ' to tell the cook to prepare the food.']),
    (1, None, ["'A chef should shout at cooks!' Everyone usually expects a chef to ", ('senya', 'кричать'), ' or shout loudly at the cooks.']),
    (2, None, ["'Arseny, you deserve respectful treatment.' Notice how she respectfully tells him that he ", ('elena', 'заслуживаете'), ' or deserves to be treated well.']),
    (3, None, ["'But strict discipline is needed in the kitchen.' He still firmly believes that very ", ('senya', 'строгая'), ' and rigid discipline is absolutely necessary.']),
    (4, None, ["'You have the cleanest workstation.' She kindly compliments his station for being the most ", ('elena', 'чистое'), ' or clean area in the whole place.']),
    (5, None, ["'Where is the hot dish for table three?' Frantically looking for the missing food, she needs a ", ('sasha', 'горячее'), ' hot dish to serve to her waiting table.']),
    (6, None, ["'The guests have been waiting forty minutes already!' Her frustrated customers have been sitting there for ", ('sasha', 'сорок'), ' minutes while waiting for their food.']),
    (7, None, ["'Sasha, calmly, let us breathe deeply.' In an effort to calm the waitress down, she suggests to ", ('elena', 'дышать'), ' deeply and just relax a bit.']),
    (8, None, ["'This dish takes over an hour to cook.' Quietly explaining the delay, she notes the food ", ('elena', 'готовится'), ' or cooks for more than an hour.']),
    (9, None, ["'They threaten to leave without paying.' Furious customers are so upset that they ", ('sasha', 'грозятся'), ' to simply walk out without paying.']),
    (10, None, ["'Ask the guests to wait a little longer.' Instead of panicking, the boss asks the waitress to have them ", ('elena', 'подождать'), ' a little longer.']),
    (11, None, ["'New order: partridge and mushrooms.' Moving on to the next task, a ", ('elena', 'Новый'), ' fresh order comes in for the chefs to prepare.']),
    (12, None, ["'We will make everything on time, chef!' Eager to please the boss, the cook promises they ", ('senya', 'сделаем'), ' everything perfectly on schedule.']),
]
