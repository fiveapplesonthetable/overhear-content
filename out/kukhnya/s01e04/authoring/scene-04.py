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
    ('max', 'Витюшенька, мой огузок.', 'Vityushenka, my little runt.', [(31, 'Витюшенька'), (31, 'Мой Агузак')], ''),
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
    (0, None, '\'Good job, Vitka.\' "Ty molodets" is the "well done" praise. "Vit\'ka" is a rude short form of Viktor, and Max uses "ty" with the boss. That\'s the dream talking.'),
    (1, None, '\'Vityushenka, my little runt.\' "Vityushen\'ka" is a tender pet name, with extra syllables for affection. He flips the nickname by calling the chef his "oguzok".'),
    (2, None, '\'Have you completely lost your mind?\' Literally "went off the mind". Barinov says "ty chto" at the start, as a kind of "what\'s wrong with you?".'),
    (3, None, '\'Why are you sleeping here?\' "Ty chto" works as "why" here, a colloquial "what are you...?". "Spish\'" is "you sleep".'),
    (4, None, '\'Chef, please forgive me.\' Now Max switches to "vy", the polite you, awake at last. "Prostite" is the polite command.'),
    (5, None, '\'I lay down for five minutes.\' The little "pri-" on the front turns "lay down" into "lay down for a bit". For a stretch of time Russian uses "na", so "na pyat\' minut" is "for five minutes".'),
    (6, None, '\'You cannot sleep in the kitchen!\' "Nel\'zya" means "it\'s not allowed", or "it can\'t be done". It\'s a very useful word, and the one Nastya used to ask why she couldn\'t buy a knife.'),
    (7, None, '\'I could not sleep all night.\' Russian puts "all night" straight in the object form, "vsyu noch\'", with no "during" in front. "Couldn\'t" is just "ne mog".'),
    (8, None, '\'Why didn\'t you sleep at night?\' "Noch\'yu" is "at night", with "-yu" meaning "in the course of". Parts of the day work this way.'),
    (9, None, '\'Probably it is acclimatization.\' Max reaches for a long borrowed word, "akklimatizatsiya", because it sounds scientific. "Navernoye", probably, softens it.'),
    (10, None, '\'What acclimatization?\' "Kakaya yeshchyo" asks "what kind of", with an edge. The chef repeats the word to mock it.'),
    (11, None, '\'I am not used to Moscow yet.\' "Privyk k" means "got used to", with "k" for "to". "Yeshchyo ne" is "not yet", and "Moskve" has an -e.'),
    (12, None, '\'Quickly get up and wash dishes!\' "Moy" here is the command "wash", which is spelled like "my" but means something else. "Posuda" is "dishes", singular in Russian.'),
    (13, None, '\'Already getting up, Chef.\' The present form "vstayu" stands for "I\'m getting up", since Russian has no "-ing". Max sounds beaten.'),
]
