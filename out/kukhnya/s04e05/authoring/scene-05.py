# Authoring module for kukhnya-s04e05-scene-05.
ID = 'kukhnya-s04e05-scene-05'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 5
SCENE = 5
TITLE = 'Новый су-шеф  (The New Sous-Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'german': 'Герман', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.05'
SOURCE_FILE = 'sources/kukhnya/s04/e05.ru.srt'
INTRO = 'Out in the gleaming kitchen of Claude Monet, German Land claps his hands for attention and presents Max Lavrov as the new sous-chef. As soon as German walks away, Fedya and the other cooks crowd around Max to tease their newly promoted colleague.'
OPENER = "Let's break down German's announcement and the cooks' reaction line by line."
TRANSITION = "Now let's hear the announcement of the new sous-chef from beginning to end."
OUTRO = "Max is thrilled by his new title, though his authority is about to be tested by both Denis's rent money and a difficult order from German. Until next time!"
CLOSING = ('german', 'До завтра!')
STORY = [
    ('german', 'Уважаемые коллеги, прошу минуточку вашего внимания!', 'Dear colleagues, I ask for a minute of your attention!', [(72, 'Коллеги!'), (73, 'Минуточку внимания.')], 'adapted'),
    ('german', 'Хочу представить вам нашего нового су-шефа.', 'I want to introduce our new sous-chef to you.', [(74, 'Хочу представить вам нашего нового су-шефа.')], ''),
    ('german', 'Это повар Лавров Максим Леонидович.', 'This is cook Lavrov Maksim Leonidovich.', [(75, 'Лавров Максим Леонидович.')], 'adapted'),
    ('german', 'Прошу всех любить и жаловать его.', 'I ask everyone to welcome and respect him.', [(76, 'Прошу любить и жаловать.')], 'adapted'),
    ('max', 'Приветствую вас, дорогие коллеги по кухне!', 'Greetings to you, dear kitchen colleagues!', [], 'new'),
    ('fedya', 'Повара, низко кланяйтесь нашему новому су-шефу!', 'Cooks, bow low to our new sous-chef!', [(77, 'кланяйтесь новому су-шефу.')], 'adapted'),
    ('fedya', 'Макс, скажи честно, что тут происходит?', 'Max, tell us honestly, what is going on here?', [(78, 'Макс, что происходит?')], 'adapted'),
    ('max', 'Ты как к су-шефу обращаешься сейчас?', 'How are you addressing the sous-chef right now?', [(78, 'Ты как к су-шефу обращаюсь')], 'adapted'),
    ('fedya', 'Ой, простите нас, уважаемый Максим Леонидович!', 'Oh, forgive us, respected Maksim Leonidovich!', [(79, 'Максим Леонидович')], 'adapted'),
    ('fedya', 'Ты теперь у нас выбился в начальники!', 'You have now risen to become one of our bosses!', [(79, 'начальники выбились.')], 'adapted'),
    ('max', 'Да, теперь я ваш новый начальник.', 'Yes, now I am your new boss.', [], 'new'),
    ('max', 'Давайте все быстро вернёмся к работе.', "Let's all quickly return to work.", [], 'new'),
]
WALK = [
    (0, None, '\'Dear colleagues, I ask for a minute of your attention!\' Emphasizing the colleagues with Max, German brings in "uvazhayemyye" ("respected, esteemed", from "uvazhayemyy") as the key Russian word here.'),
    (1, None, "'I want to introduce our new sous-chef to you.' German replies promptly without holding back, keeping the focus on what actually matters here."),
    (2, None, '\'This is cook Lavrov Maksim Leonidovich.\' German pushes back pointedly before Max and uses "povar" ("chef, cook") to carry the main weight of the thought.'),
    (3, None, '\'I ask everyone to welcome and respect him.\' German responds promptly around Max and uses "zhalovat" ("to favor, welcome") to carry the main weight of the thought.'),
    (4, None, "'Greetings to you, dear kitchen colleagues!' Max pushes back sharply watching German, leaving no doubt about where he stands."),
    (5, None, '\'Cooks, bow low to our new sous-chef!\' Discussing the low in the exchange, Fedya reaches for the Russian word "klanyaytes" ("low") right at the heart of the line.'),
    (6, None, '\'Max, tell us honestly, what is going on here?\' Reacting boldly on the spot, Fedya puts the question word "chto" right at the start so Max hears the focus immediately.'),
    (7, None, "'How are you addressing the sous-chef right now?' Max asks plainly whether Fedya really thought this through."),
    (8, None, '\'Oh, forgive us, respected Maksim Leonidovich!\' Fedya replies quietly with Max and leans on "uvazhayemyy" ("respected, esteemed") to give the whole sentence its punch.'),
    (9, None, '\'You have now risen to become one of our bosses!\' Touching on the boss at once, Fedya reaches for "u nas" ("by us, at our place") to talk about what they share.'),
    (10, None, "'Yes, now I am your new boss.' Max replies promptly beside Fedya, testing Fedya's reaction in the middle of the exchange."),
    (11, None, '\'Let\'s all quickly return to work.\' Highlighting the work right here, Max chooses "vernyomsya" ("return, go back", from the root "vernutsya") so Fedya hears the exact meaning.'),
]
