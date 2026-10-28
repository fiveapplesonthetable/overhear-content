# Authoring module for kukhnya-s01e04-scene-04.
ID = 'kukhnya-s01e04-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 4
TITLE = 'Сладкий сон  (A Sweet Dream)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "Max has fallen asleep in the dining room and is having a lovely dream about the chef. When Barinov shakes him awake, Max is still half in the dream and says things he really shouldn't. Here's the Russian first."
OPENER = "Now let's see what Max says in his sleep."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Calling the boss by a pet name is not the way to keep a job. If you take one thing away, remember "nel\'zya", "it\'s not allowed".'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Ты молодец, Витька.', 'Good job, Vitka.', [(30, 'Ты молодец, Витька')], ''),
    ('max', 'Витюшенька, мой огузок.', 'Vityushenka, my Oguzok.', [(31, 'Витюшенька'), (31, 'Мой Агузак')], ''),
    ('barinov', 'Ты что, совсем с ума сошёл?', 'Have you completely lost your mind?', [(32, 'Ты что, совсем')], ''),
    ('barinov', 'Ты что здесь спишь?', 'Why are you sleeping here?', [(33, 'Ты что здесь')], ''),
    ('max', 'Шеф, простите меня, пожалуйста.', 'Chef, please forgive me.', [(33, 'Шеф, я')], ''),
    ('max', 'Я прилёг на пять минут.', 'I lay down for five minutes.', [(34, 'прилег на пять минут заснуть')], ''),
    ('barinov', 'На кухне спать нельзя!', 'You cannot sleep in the kitchen!', [], ''),
    ('max', 'Я всю ночь не мог уснуть.', 'I could not sleep all night.', [(35, 'Всю ночь не мог')], ''),
    ('barinov', 'Почему ты ночью не спал?', "Why didn't you sleep at night?", [], ''),
    ('max', 'Наверное, это акклиматизация.', 'Probably it is acclimatization.', [(35, 'акклиматизация, наверное')], ''),
    ('barinov', 'Какая ещё акклиматизация?', 'What acclimatization?', [], ''),
    ('max', 'Я ещё не привык к Москве.', 'I am not used to Moscow yet.', [], ''),
    ('barinov', 'Быстро вставай и мой посуду!', 'Quickly get up and wash dishes!', [], ''),
    ('max', 'Уже встаю, шеф.', 'Already getting up, Chef.', [], ''),
]
WALK = [
    (0, None, '\'Good job, Vitka.\' "Ty molodets" is "you\'re a fine fellow", the everyday praise. "Vit\'ka" is an overfamiliar short form of "Viktor", and Max says "ty" to his boss in his sleep.'),
    (1, None, '\'Vityushenka, my Oguzok.\' "Vityushen\'ka" is a doting pet form of "Viktor", with extra syllables for tenderness. Max then flips the chef\'s nickname for him back onto the chef: "moy oguzok".'),
    (2, None, '\'Have you completely lost your mind?\' "S uma soshyol" is "came down off the mind". "Ty chto" at the start means "what\'s wrong with you?".'),
    (3, None, '\'Why are you sleeping here?\' Here "ty chto" does the job of "why", as in speech. "Spish\'" is "you sleep".'),
    (4, None, '\'Chef, please forgive me.\' Awake, Max switches to "vy": "prostite", forgive, with the polite -te.'),
    (5, None, '\'I lay down for five minutes.\' "Pri-" turns "lyog", lay down, into "prilyog", lay down for a bit. "Na pyat\' minut" is "for five minutes".'),
    (6, None, '\'You cannot sleep in the kitchen!\' "Nel\'zya" is "it\'s not allowed", and it needs no subject. "Spat\'" is the plain "to sleep".'),
    (7, None, '\'I could not sleep all night.\' "Vsyu noch\'" needs no "during". "Ne mog usnut\'" is "could not fall asleep", with "mog" the man\'s past of "can".'),
    (8, None, '\'Why didn\'t you sleep at night?\' "Noch\'yu", at night, is "noch\'" with -yu. Other times of day work the same way: "utrom", in the morning, and "vecherom", in the evening.'),
    (9, None, '\'Probably it is acclimatization.\' Max gives the same long borrowed word as before, "akklimatizatsiya". "Navernoye" is "probably".'),
    (10, None, '\'What acclimatization?\' "Kakaya yeshchyo" repeats the word back with an edge, like "what acclimatization, exactly?".'),
    (11, None, '\'I am not used to Moscow yet.\' "Privyk k" is "got used to", and "k" puts an -e on the city: "k Moskve". "Yeshchyo ne" is "not yet".'),
    (12, None, '\'Quickly get up and wash dishes!\' "Moy" here is the command "wash", from "myt\'", and it is spelled the same as "moy", my. "Posuda", dishes, is one singular word in Russian.'),
    (13, None, '\'Already getting up, Chef.\' "Uzhe vstayu" is "already I get up". The plain present stands in for "I\'m getting up".'),
]
