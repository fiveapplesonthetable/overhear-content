ID = "kukhnya-s04e16-scene-09"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 16
SCENE = 9
TITLE = 'Курсы сомелье  (Sommelier Courses)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'guest': 'anja', 'nastya': 'angelina'}
LABELS = {'anya': 'Костя', 'guest': 'Гость', 'nastya': 'Настя'}
SOURCE_NAME = "Кухня (Kukhnya) S4.16"
SOURCE_FILE = "sources/kukhnya/s04/e16.ru.srt"

INTRO = "Since the restaurant has no sommelier on duty, bartender Kostya puts on an apron and tries to sell a guest the most expensive bottle of wine on the menu to pair with lamb. When the guest exposes Kostya's complete lack of wine knowledge, Nastya suggests paying for professional sommelier lessons."

STORY = [
    ('anya', 'Позвольте предложить вам к ягнёнку прекрасное вино.', 'Allow me to offer you a wonderful wine with your lamb.', [(100, 'Позвольте предложить вам к')], 'adapted'),
    ('guest', 'Почему вы предлагаете мне самое дорогое вино?', 'Why are you offering me the most expensive wine?', [(101, 'А почему мне предлагается')], 'adapted'),
    ('anya', 'Потому что дорогое вино всегда самое лучшее!', 'Because expensive wine is always the very best!', [(102, 'Оно самое лучшее.')], 'adapted'),
    ('guest', 'Дорогое вино вовсе не значит самое лучшее.', 'Expensive wine does not mean the very best at all.', [(103, 'Дорогое не значит лучшее.')], 'adapted'),
    ('guest', 'Это тяжёлое вино полностью перебьёт вкус блюда!', 'This heavy wine will completely overpower the flavor of the dish!', [(105, 'Оно же будет полностью')], 'adapted'),
    ('anya', 'Пусть вкусное вино доминирует на вашем столе!', 'Let tasty wine dominate on your table!', [(106, 'Вкусное вино пусть доминирует.')], 'adapted'),
    ('guest', 'Я просил позвать сомелье, а не буфетчика!', 'I asked to call a sommelier, not a bartender!', [(107, 'Знаете, я просил позвать')], 'adapted'),
    ('guest', 'Позовите сюда администратора, я хочу серьёзно поговорить!', 'Call the manager here, I want to have a serious talk!', [(109, 'Зовите сюда, я хочу')], 'adapted'),
    ('anya', 'Извините, выберите любое хорошее вино за мой счёт!', 'Excuse me, choose any good wine on my tab!', [(111, 'Мне выбирайте вино, которое')], 'adapted'),
    ('nastya', 'Костик, давай запишем тебя на курсы сомелье!', "Kostik, let's sign you up for sommelier courses!", [(115, 'Костик, а давай тебя')], 'adapted'),
    ('anya', 'Это слишком дорого, Настя, я почитаю в интернете.', 'That is too expensive, Nastya, I will read on the internet.', [(116, 'Дорого, Настя. Давай я')], 'adapted'),
    ('nastya', 'Хорошая учёба — это инвестиция в наше будущее!', 'Good education is an investment in our future!', [(117, 'Это инвестиции в будущее.')], 'adapted'),
]

OPENER = "Let's examine Kostya's failed wine pitch and Nastya's career idea."

WALK = [
    (0, None, "'Allow me to offer you a wonderful wine with your lamb.' Kostya uses a polite imperative with the dative singular of the noun for lamb."),
    (1, None, "'Why are you offering me the most expensive wine?' The guest questions Kostya's choice using a neuter superlative adjective."),
    (2, None, "'Because expensive wine is always the very best!' Kostya bluffs with two neuter nominative adjective phrases."),
    (3, None, "'Expensive wine does not mean the very best at all.' The guest corrects him using the third-person singular verb for meaning."),
    (4, None, "'This heavy wine will completely overpower the flavor of the dish!' A perfective future verb governs an accusative noun and a genitive singular complement."),
    (5, None, "'Let tasty wine dominate on your table!' Kostya makes matters worse with a clumsy third-person injunction."),
    (6, None, "'I asked to call a sommelier, not a bartender!' An indeclinable loanword contrasts with an animate masculine accusative noun."),
    (7, None, "'Call the manager here, I want to have a serious talk!' The angry guest demands the manager using a plural imperative."),
    (8, None, "'Excuse me, choose any good wine on my tab!' To avoid a complaint, Kostya offers to pay for the bottle himself."),
    (9, None, "'Kostik, let's sign you up for sommelier courses!' Back at the bar, Nastya proposes classes using a preposition with the accusative plural."),
    (10, None, "'That is too expensive, Nastya, I will read on the internet.' Kostya hesitates over the tuition cost."),
    (11, None, "'Good education is an investment in our future!' Nastya persuades him with a feminine nominative predicate and accusative phrase."),
]

TRANSITION = 'Now listen to the complete wine-tasting scene from start to finish.'

OUTRO = "Encouraged by Nastya's belief in his future, Kostya begins studying wine—while Denis walks into Chef Barinov's office at the worst possible moment. See you in the next scene."

CLOSING = ('nastya', 'Это отличная инвестиция в наше общее будущее!')
CLOSING_TRANS = 'This is an excellent investment in our shared future!'
