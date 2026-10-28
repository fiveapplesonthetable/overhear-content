# Authoring module for kukhnya-s04e07-scene-02.
ID = 'kukhnya-s04e07-scene-02'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 7
SCENE = 2
TITLE = "Банкет кинематографистов  (The Filmmakers' Banquet)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'nagiyev': 'Нагиев', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.07'
SOURCE_FILE = 'sources/kukhnya/s04/e07.ru.srt'
INTRO = "An important visitor enters Claude Monet before opening hours: Gavril Ilyich, deputy chairman of the Filmmakers' Union, sent by legendary director Nikita Mikhalkov. He wants to book a prestigious banquet at the restaurant, but only if Viktor Barinov is the chef!"
OPENER = "Let's examine the Filmmakers' Union banquet request line by line."
TRANSITION = "Now let's listen to the banquet booking conversation again in full."
OUTRO = 'Having promised that Viktor Barinov will personally cook the banquet tasting tonight, Nagiyev now has to convince his fired chef to come back. See you next time!'
CLOSING = ('guest', 'Пока!')
STORY = [
    ('vika', 'Дмитрий Владимирович, к нам пришёл важный гость.', 'Dmitry Vladimirovich, an important guest has come to see us.', [(17, 'Дмитрий Владимирович, у нас гость.')], 'adapted'),
    ('nagiyev', 'Доброе утро, но наш ресторан ещё закрыт.', 'Good morning, but our restaurant is still closed.', [(18, 'Доброе утро.'), (19, 'Мы еще закрыты.')], 'adapted'),
    ('guest', 'Позвольте мне сначала представиться вам, господа.', 'Allow me to introduce myself to you first, gentlemen.', [(21, 'Позвольте представиться.')], 'adapted'),
    ('guest', 'Я пришёл по поручению известного кинорежиссёра.', 'I have come on behalf of the famous film director.', [(23, 'я к вам по поручению Никиты Сергеевича Михалкова.')], 'adapted'),
    ('nagiyev', 'Ради съёмок я готов освободить любые даты!', 'For the sake of filming I am ready to clear any dates!', [(24, 'Я ради.'), (25, 'готов освободить все даты')], 'adapted'),
    ('guest', 'Спасибо, но я здесь по другому вопросу.', 'Thank you, but I am here on another matter.', [(26, 'но я здесь по другому вопросу.')], 'adapted'),
    ('guest', 'Мы хотим провести банкет в вашем ресторане.', 'We want to hold a banquet in your restaurant.', [(27, 'Мы хотели бы провести банкет Союза кинематографистов в вашем ресторане.')], 'adapted'),
    ('guest', 'Мы недавно обедали у вас, всё понравилось.', 'We had lunch at your place recently, we liked everything.', [(28, 'пару месяцев назад у вас обедали, нам очень понравилось.')], 'adapted'),
    ('guest', 'Все были в восторге от Виктора Баринова!', 'Everyone was delighted with Viktor Barinov!', [(29, 'был в восторге от вашего шеф-повара Виктора Баринова.')], 'adapted'),
    ('guest', 'Мы с нетерпением вновь ждём встречи с ним.', 'We eagerly look forward to meeting him again.', [(31, 'Так что с нетерпением.'), (32, 'Вновь ждем встречи с ним.')], 'adapted'),
    ('guest', 'Я зайду сегодня вечером попробовать банкетное меню.', 'I will drop by this evening to taste the banquet menu.', [(37, 'я зайду сегодня часиков в 7,'), (38, 'попробовать банкетное меню.')], 'adapted'),
    ('nagiyev', 'Можете не сомневаться, Баринов обязательно будет здесь!', 'You need not doubt it, Barinov will definitely be here!', [(39, 'Можете не сомневаться, Маринов будет как штык.')], 'adapted'),
]
WALK = [
    (0, None, '\'Dmitry Vladimirovich, an important guest has come to see us.\' Turning to an important guest at once, Vika puts the emphasis on "vazhnyy" ("important") in the middle of the talk.'),
    (1, None, "'Good morning, but our restaurant is still closed.' Nagiyev pushes back sharply during the talk, letting the remark speak for itself."),
    (2, None, '\'Allow me to introduce myself to you first, gentlemen.\' Focusing on the gentlemen before Nagiyev, the guest leans on "predstavitsya" ("to introduce oneself") to give the whole sentence its punch.'),
    (3, None, '\'I have come on behalf of the famous film director.\' Bringing up the director in the exchange, the guest chooses "kinorezhissyora" ("director") so Nagiyev gets the point right away.'),
    (4, None, "'For the sake of filming I am ready to clear any dates!' Nagiyev continues steadily without a pause, so the guest knows he is not just making small talk."),
    (5, None, '\'Thank you, but I am here on another matter.\' Discussing the thank before Nagiyev, the guest chooses "spasibo" ("thank you") so Nagiyev gets the point right away.'),
    (6, None, '\'We want to hold a banquet in your restaurant.\' Touching on the restaurant around Nagiyev, the guest chooses "restorane" ("restaurant", from the root "restoran") so Nagiyev hears the exact meaning.'),
    (7, None, "'We had lunch at your place recently, we liked everything.' The guest cuts in wryly hearing Nagiyev, refusing to let the moment slip past."),
    (8, None, '\'Everyone was delighted with Viktor Barinov!\' Pointing to the delight in the exchange, the guest leans on "vostorge" ("delight", a form of "vostorg") to give the remark its edge.'),
    (9, None, '\'We eagerly look forward to meeting him again.\' Discussing the meeting right here, the guest uses "neterpeniyem" ("to forward", from "neterpenit") to make the point stick.'),
    (10, None, "'I will drop by this evening to taste the banquet menu.' The guest responds quietly during the talk, before Nagiyev can change the subject."),
    (11, None, '\'You need not doubt it, Barinov will definitely be here!\' Nagiyev steps in directly at once and centers the remark on "somnevatsya" ("to doubt") without any extra fuss.'),
]
