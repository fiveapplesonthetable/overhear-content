# Authoring module for kukhnya-s01e07-scene-06.
ID = 'kukhnya-s01e07-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 6
TITLE = 'Покупка ножа  (Buying a Knife)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'seller': 'Продавец'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = 'Still at the Moscow market, Chef Barinov moves on to a stall that sells kitchen knives. A salesman tries to sell him something ordinary, and the chef shows him he knows his steel. Here is the Russian.'
OPENER = 'Slowly now. The salesman is flattering, and Barinov is hard to impress.'
TRANSITION = 'The knife stall once more, start to finish.'
OUTRO = "Barinov asks the shopper's question: how much does it cost. That's worth keeping, along with a few words for describing a good knife. See you next time."
CLOSING = ('barinov', 'До встречи!')
STORY = [
    ('seller', 'Уважаемый шеф, подходите и выбирайте ножи!', 'Respected chef, step right up and choose knives!', [(56, 'Подходим, выбираем')], ''),
    ('seller', 'Посмотрите, какое острое и тонкое лезвие!', 'Look what a sharp and thin blade!', [(56, 'Острый')], ''),
    ('barinov', 'Осторожно, этот клинок острый, как кинжал.', 'Careful, this blade is sharp as a dagger.', [(57, 'Ой, как кинзал'), (58, 'Осторожно')], ''),
    ('barinov', 'Но здесь металл слишком мягкий.', 'But here the metal is too soft.', [(59, 'Что-то не то')], ''),
    ('seller', 'Это лучшая прочная сталь для кухни!', 'This is the best strong steel for the kitchen!', [(56, 'выбираем')], ''),
    ('barinov', 'Не обманывай меня, я опытный повар.', "Don't deceive me, I am an experienced chef.", [(59, 'Что-то не то')], ''),
    ('barinov', 'Таким ножом мясо резать нельзя.', 'One cannot cut meat with such a knife.', [(59, 'Что-то не то')], ''),
    ('seller', 'Тогда посмотрите вот этот японский нож.', 'Then look at this Japanese knife.', [(56, 'выбираем')], ''),
    ('seller', 'Его сделали мастера из твёрдой стали.', 'Craftsmen made it from hard steel.', [(56, 'выбираем')], ''),
    ('barinov', 'Да, этот нож лежит в руке идеально.', 'Yes, this knife rests in the hand perfectly.', [(58, 'Осторожно')], ''),
    ('barinov', 'Сколько стоит такой отличный инструмент?', 'How much does such an excellent tool cost?', [(56, 'Подходим')], ''),
    ('seller', 'Для вас отдам всего за три тысячи.', 'For you I will give it for only three thousand.', [(56, 'Подходим')], ''),
    ('barinov', 'Хорошо, я забираю этот нож.', 'Fine, I am taking this knife.', [(56, 'выбираем')], ''),
    ('barinov', 'На моей кухне нужен острый порядок!', 'In my kitchen sharp order is needed!', [(56, 'Острый')], ''),
]
WALK = [
    (0, None, '\'Respected chef, step right up and choose knives!\' "Uvazhaemyy", \'respected\', is how a formal letter or announcement begins, like \'Dear Sir\'. "Podkhodite" and vybirayte are both polite commands, ending in -te.'),
    (1, None, '\'Look what a sharp and thin blade!\' "Lezviye", a blade, is neuter, so kakoe, ostroe and tonkoe all end in -oe to match it.'),
    (2, None, '\'Careful, this blade is sharp as a dagger.\' Barinov says klinok, another word for blade. "Kak kinzhal", \'like a dagger\', shows kak doing the job of \'as\' in a comparison.'),
    (3, None, '\'But here the metal is too soft.\' "Slishkom", \'too\', goes straight in front of the word it changes, like English: slishkom myagkiy, too soft.'),
    (4, None, '\'This is the best strong steel for the kitchen!\' "Stal\'", steel, is feminine, so the salesman says luchshaya prochnaya, both ending in -aya. "Dlya kukhni", \'for the kitchen\', changes kukhnya to kukhni after dlya.'),
    (5, None, '\'Don\'t deceive me, I am an experienced chef.\' "Opytnyy", experienced, comes from opyt, experience, which Max used at the start of the episode. Barinov uses casual ty with the salesman, while the salesman sticks to vy.'),
    (6, None, '\'One cannot cut meat with such a knife.\' "Takim nozhom", \'with such a knife\', has no word for \'with\': the -im and -om endings mean \'using\'. "Nel\'zya" at the end is the flat \'can\'t be done\'.'),
    (7, None, '\'Then look at this Japanese knife.\' "Yaponskiy", Japanese, has a small letter in Russian, as do all nationality words. "Vot etot" is \'this one right here\'.'),
    (8, None, '\'Craftsmen made it from hard steel.\' Ego sdelali, \'they made it\', has no named subject, which is how Russian often says \'it was made\'. "Mastera" is the plural of master, a skilled craftsman.'),
    (9, None, '\'Yes, this knife rests in the hand perfectly.\' A knife that lezhit v ruke, \'lies in the hand\', is one that feels right to hold. "Ruka" becomes ruke after v.'),
    (10, None, '\'How much does such an excellent tool cost?\' "Skol\'ko stoit?", \'how much costs?\', is the question to keep for any shop. "Takoy", \'such\', is masculine to agree with the word for tool.'),
    (11, None, '\'For you I will give it for only three thousand.\' "Otdam" is \'I\'ll hand it over\', a seller\'s way of naming a price. "Vsego" means \'only\', and after tri, \'three\', tysyacha becomes tysyachi.'),
    (12, None, '\'Fine, I am taking this knife.\' "Zabirayu" means \'I\'m taking it with me\', which is how a buyer says \'I\'ll have it\'. "Khorosho", \'good\', doubles as \'fine\' or \'OK\'.'),
    (13, None, '\'In my kitchen sharp order is needed!\' "Nuzhen", \'needed\', is masculine to match poryadok, order. "Ostryy", sharp, is the word the salesman used for his blade, so Barinov ends on a pun.'),
]
