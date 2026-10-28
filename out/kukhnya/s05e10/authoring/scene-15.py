# Authoring module for kukhnya-s05e10-scene-15.
ID = 'kukhnya-s05e10-scene-15'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 10
SCENE = 15
TITLE = 'Настоящий гипнотизёр  (The Real Hypnotist)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.10'
SOURCE_FILE = 'sources/kukhnya/s05/e10.ru.srt'
INTRO = 'Hearing the cocktail order, Max realizes they were looking for the wrong suspect all day. The woman who ordered the Sex on the Beach cocktail is the real hypnotist who made Nastya blame the moustached man at the next table and forced Sveta to erase the database.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes Max's deduction in the dining room. Pay attention to how he reconstructs the crime and plans to catch the female hypnotist red-handed with the bill. Until next time!"
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Костян, я всё понял! Мы с тобой облажались.', 'Kostyan, I figured it all out! You and I screwed up.', [(214, 'Костян, я все понял. Мы с тобой облажались')], 'adapted'),
    ('kostya', 'Это вообще-то ты облажался!', 'Actually you are the one who screwed up!', [(215, 'Это вообще-то ты облажался')], 'adapted'),
    ('max', 'Мы не того искали. Настя утром обслуживала девушку!', 'We were looking for the wrong person. Nastya served a girl this morning!', [(216, 'Мы не того искали'), (217, 'Настя утром обслуживала девушку')], 'adapted'),
    ('kostya', 'В смысле?', 'What do you mean?', [(218, 'В смысле')], 'adapted'),
    ('max', 'В счёте был дорогой коктейль на пляже.', 'On the bill was an expensive beach cocktail.', [(219, 'В счете был коктейль'), (219, 'на пляже')], 'adapted'),
    ('max', 'Потом эта девушка на ресепшене была.', 'Then this girl was at reception.', [(221, 'Потом эта девушка на ресепшн была')], 'adapted'),
    ('max', 'Заставила Свету базу удалить.', 'She forced Sveta to delete the database.', [(222, 'Заставила Свету базу удалить')], 'adapted'),
    ('max', 'А Насте она внушила, что с ней расплатился усатый.', 'And she made Nastya believe that the moustached man paid her.', [(225, 'А Насте она внушила, что с ней расплатился'), (221, 'Усатый')], 'adapted'),
    ('nastya', 'И запомните, вы обслуживали не меня, а вон того мужчину!', 'And remember, you served not me, but that man over there!', [(226, 'И запомните, вы обслуживали не меня, а вон того мужчину')], 'adapted'),
    ('kostya', 'И что теперь делать?', 'And what do we do now?', [(227, 'И что теперь делать')], 'adapted'),
    ('max', 'Я девушку бить не буду. Она на меня посмотрела.', 'I am not going to hit a girl. She looked at me.', [(228, 'Я девушку бить не буду'), (229, 'Она на меня посмотрела')], 'adapted'),
    ('max', 'Я сейчас отнесу ей счёт. Когда она салфетками расплатится, возьмём с поличным!', 'I will take her the bill now. When she pays with napkins, we will catch her red-handed!', [(230, 'Я сейчас отнесу ей счет. Когда она с лалфетками расплатится, возьмем с поличным')], 'adapted'),
]
WALK = [
    (0, None, "'Kostyan, I figured it all out! You and I screwed up.' Max chimes in calmly on the spot, letting the remark speak for itself."),
    (1, None, '\'Actually you are the one who screwed up!\' Kostya points to one pointed touch right here: "voobshche-to" means "actually", and it carries the main weight of what Kostya is saying.'),
    (2, None, "'We were looking for the wrong person. Nastya served a girl this morning!' Max stands firm firmly as they talk, steering the talk right where he wants it."),
    (3, None, "'What do you mean?' Kostya checks frankly before Nastya can change the subject."),
    (4, None, '\'On the bill was an expensive beach cocktail.\' Max leans on one familiar detail toward Kostya: "schyote" means "bill, check" (from "schyot"), giving the line its exact edge.'),
    (5, None, "'Then this girl was at reception.' Max answers openly to settle things, grounding the moment in plain reality."),
    (6, None, "'She forced Sveta to delete the database.' Max counters warmly with Kostya, before Kostya can change the subject."),
    (7, None, '\'And she made Nastya believe that the moustached man paid her.\' Max centers this telling detail for Nastya: "rasplatilsya" means "paid" (from "rasplatitsya"), giving the line its exact edge.'),
    (8, None, '\'And remember, you served not me, but that man over there!\' Nastya favors one concrete choice right here: "obsluzhivali" means "served, waited on" (from "obsluzhivat"), giving the line its exact edge.'),
    (9, None, "'And what do we do now?' Kostya wonders eagerly how Nastya expects that to work in practice."),
    (10, None, '\'I am not going to hit a girl. She looked at me.\' Max frames one memorable piece in earnest: "devushku" means "young woman" (from "devushka"), giving the line its exact edge.'),
    (11, None, "'I will take her the bill now. When she pays with napkins, we will catch her red-handed!' Max pushes back right away hearing Nastya, testing Nastya's reaction in the middle of the exchange."),
]
