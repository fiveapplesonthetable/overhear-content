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
    (0, None, "'Kostyan, I figured it all out! You and I screwed up.' Max responds calmly in their talk, grounding the moment in plain reality."),
    (1, None, '\'Actually you are the one who screwed up!\' Kostya counters warmly in this beat and reaches for the Russian word "oblazhalsya" ("screw up, mess up", built from "oblazhatsya") right at the center of the line.'),
    (2, None, '\'We were looking for the wrong person. Nastya served a girl this morning!\' Highlighting the young woman in front of Nastya, Max puts the weight on "obsluzhivala" ("served", from "obsluzhivat") as the exchange unfolds.'),
    (3, None, "'What do you mean?' Kostya checks frankly where this conversation is heading next."),
    (4, None, '\'On the bill was an expensive beach cocktail.\' Addressing the bill on the spot, Max puts the weight on "schyote" ("bill, check", from "schyot") as the exchange unfolds.'),
    (5, None, '\'Then this girl was at reception.\' Focusing on the reception desk at once, Max lands on "resepshene" ("reception desk", built on "resepshen") to keep the statement grounded.'),
    (6, None, "'She forced Sveta to delete the database.' Max speaks warmly without any doubt, so Nastya knows he is not just making small talk."),
    (7, None, '\'And she made Nastya believe that the moustached man paid her.\' Max jumps in decisively beside Nastya and lands on "rasplatilsya" ("paid", built on "rasplatitsya") to keep the statement grounded.'),
    (8, None, "'And remember, you served not me, but that man over there!' Nastya speaks up earnestly without any doubt, leaving no doubt about where she stands."),
    (9, None, "'And what do we do now?' Kostya wonders eagerly how Max expects that to work in practice."),
    (10, None, '\'I am not going to hit a girl. She looked at me.\' Touching on the young woman at once, Max brings in "devushku" ("young woman", from "devushka") as the key Russian word here.'),
    (11, None, '\'I will take her the bill now. When she pays with napkins, we will catch her red-handed!\' Pointing to the napkins right here, Max brings in "salfetkami" ("napkins", from "salfetka") as the key Russian word here.'),
]
