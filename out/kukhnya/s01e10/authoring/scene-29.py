# Authoring module for kukhnya-s01e10-scene-29.
ID = 'kukhnya-s01e10-scene-29'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 29
TITLE = 'Щучья икра  (Pike Caviar)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = 'Senya slips into the office with a secret box for the chef. Inside is pike caviar, not black caviar. The price is low and the colour is wrong. The Russian comes first.'
OPENER = "We'll take it a bit at a time."
TRANSITION = 'And again, the whole conversation.'
OUTRO = 'The caviar is cheap and yellow, and the chef already has a plan to fix both. Senya is ready to help. On to the next.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Ну что, принёс?', 'Well, did you bring it?', [(202, 'Ну что? Принёс')], ''),
    ('senya', 'Вот товар, как вы заказывали, шеф.', 'Here is the goods, as you ordered, chef.', [(203, 'Как'), (204, 'вы заказывали')], ''),
    ('barinov', 'Открой коробку и покажи мне икру.', 'Open the box and show me the caviar.', [], ''),
    ('senya', 'Это отличная щучья икра, пять килограммов.', 'This is excellent pike caviar, five kilograms.', [(205, 'Икра щучья. Пять кило')], ''),
    ('senya', 'Цена всего двести рублей за килограмм.', 'The price is only two hundred rubles per kilogram.', [(206, 'Двести рублей килограмм')], ''),
    ('barinov', 'Это действительно очень дешёвая цена.', 'This is indeed a very cheap price.', [], ''),
    ('senya', 'Мы сэкономили ресторану очень много денег.', 'We saved the restaurant a lot of money.', [], ''),
    ('barinov', 'Но цвет этой икры слишком жёлтый.', 'But the color of this caviar is too yellow.', [], ''),
    ('senya', 'Щучья икра всегда бывает жёлтого цвета.', 'Pike caviar is always yellow in color.', [], ''),
    ('barinov', 'А гости ждут дорогую чёрную икру.', 'And the guests expect expensive black caviar.', [], ''),
    ('senya', 'Что же нам делать с этим цветом?', 'What are we to do with this color?', [], ''),
    ('barinov', 'У меня появился один хитрый план.', 'I have got a clever plan.', [], ''),
    ('senya', 'Я готов помочь вам в этом деле.', 'I am ready to help you in this business.', [], ''),
]
WALK = [
    (0, None, "'Well, did you bring it?' 'Nu chto' is a quick 'well?'. 'Prinyos' is 'brought', the past of prinesti; it has no l at the end, unlike most past forms."),
    (1, None, '\'Here is the goods, as you ordered, chef.\' "Tovar", "goods", is singular, so "vot tovar" is "here is the goods". "Kak vy zakazyvali" is "as you ordered", from "zakaz", "order".'),
    (2, None, '\'Open the box and show me the caviar.\' "Otkroy" is "open" and "pokazhi" is "show", both said to one person. "Otkroy" is from "otkryt", the opposite of "zakryt", "to close". "Pokazhi mne" is "show me".'),
    (3, None, '\'This is excellent pike caviar, five kilograms.\' "Shchuchya", "pike", is made from "shchuka", "a pike", and it describes the caviar. "Pyat kilogrammov" here has the full ending. "Otlichnaya" is "excellent".'),
    (4, None, '\'The price is only two hundred rubles per kilogram.\' "Vsego", "only", comes from "ves", "all", so it\'s "in all two hundred". "Za kilogramm" is "per kilogram", with "za". "Tsena" is "price".'),
    (5, None, '\'This is indeed a very cheap price.\' "Deshyovaya", "cheap", is the opposite of "dorogaya", "expensive". Barinov said \"deystvitelno\", \"indeed\", at the tasting, "deystvitelno ochen vkusnaya".'),
    (6, None, '\'We saved the restaurant a lot of money.\' "Sekonomili" is "saved", for money, from "ekonomiya". "Restoranu" is "for the restaurant": "restoran" adds -u. "Mnogo deneg" is "a lot of money".'),
    (7, None, '\'But the color of this caviar is too yellow.\' "Slishkom", "too", came up with the slow hotplate, "slishkom medlenno". "Tsvet" is "colour", and "zhyolty" is "yellow".'),
    (8, None, '\'Pike caviar is always yellow in color.\' "Byvaet" is "happens to be", for something that\'s usually true. "Zhyoltogo tsveta", "of yellow colour", is how Russian describes a colour. "Vsegda" is "always".'),
    (9, None, '\'And the guests expect expensive black caviar.\' "Zhdut", "wait", here means "expect", with no word for "for". "Dorogaya" is "expensive", and also "dear". "Chyornuyu ikru" is "black caviar".'),
    (10, None, '\'What are we to do with this color?\' "Chto zhe nam delat" is "what on earth are we to do", with the little "zhe". "S etim tsvetom" is "with this colour": "tsvet" becomes "tsvetom" after "s".'),
    (11, None, '\'I have got a clever plan.\' "U menya poyavilsya", literally "at me appeared", is "I\'ve come up with". "Khitry", "cunning", is the word in Alisa\'s "khitraya krysa", "cunning rat". "Plan" is easy to catch.'),
    (12, None, '\'I am ready to help you in this business.\' "Gotov", "ready", comes from Barinov\'s "vsegda gotov igrat", "always ready to play". "Pomoch" is "to help". "V etom dele" is "in this matter", from "delo".'),
]
