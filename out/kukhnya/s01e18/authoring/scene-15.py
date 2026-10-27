ID = "kukhnya-s01e18-scene-15"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 15
TITLE = "Ошибочная бутылка  (The Wrong Bottle)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "dima": "angelina"}
LABELS = {'anya': 'Макс', 'leva': 'Костя', 'dima': 'Шеф'}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = "Cues 273-294."

INTRO = (
    "Max discovers Senya was poisoned by their fake cognac. Viktor asks Kostya for a bottle of cognac and accidentally takes the fake one. Let us listen to their conversation in Russian first."
)

STORY = [
    ('anya', 'Костя, это просто ужас!', 'Kostya, this is just a nightmare!', [(273, 'Костян, это пипец.')], 'adapted'),
    ('anya', 'Сеня отравился нашим коньяком.', 'Senya got poisoned by our cognac.', [(281, 'что Сеня отравился этим коньяком.')], 'adapted'),
    ('leva', 'О нет, что делать?', 'Oh no, what to do?', [], 'adapted'),
    ('dima', 'Костя, дай мне бутылку коньяка.', 'Kostya, give me a bottle of cognac.', [(275, 'Костя, дай мне бутылочку коньяка.')], 'adapted'),
    ('dima', 'Ту, которая стоит справа.', 'The one that stands on the right.', [(276, 'А вон иксо, дай. Правее.')], 'adapted'),
    ('leva', 'Вот эту бутылку?', 'This bottle right here?', [(277, 'Нет, правее. Это?')], 'adapted'),
    ('dima', 'Нет, дай мне другую. Да, эту.', 'No, give me another one. Yes, this one.', [(278, 'Эту бутылку?'), (279, 'Эту бутылку.')], 'adapted'),
    ('anya', 'Шеф забрал наш коньяк!', 'Chef took our cognac!', [], 'adapted'),
    ('anya', 'Надо забрать эту бутылку назад.', 'We need to take this bottle back.', [(291, 'Надо забрать бутылку, Костян.')], 'adapted'),
    ('leva', 'Я не могу к нему подойти.', 'I can not approach him.', [(293, 'Я же не могу к ней подойти.')], 'adapted'),
    ('anya', 'Давай, Костя, ты должен.', 'Come on, Kostya, you must.', [(294, 'Давай, Костян, давай, дружок.')], 'adapted'),
    ('anya', 'Понятно, давай дальше.', "Got it, let's move on.", [], '')
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None, "'Kostya, this is just a nightmare!' -- The speaker states this. ENG"),
    (1, None, "'Senya got poisoned by our cognac.' -- The speaker states this. ENG"),
    (2, None, "'Oh no, what to do?' -- The speaker states this. ENG"),
    (3, None, "'Kostya, give me a bottle of cognac.' -- The speaker states this. ENG"),
    (4, None, "'The one that stands on the right.' -- The speaker states this. ENG"),
    (5, None, "'This bottle right here?' -- The speaker states this. ENG"),
    (6, None, "'No, give me another one. Yes, this one.' -- The speaker states this. ENG"),
    (7, None, "'Chef took our cognac!' -- The speaker states this. ENG"),
    (8, None, "'We need to take this bottle back.' -- The speaker states this. ENG"),
    (9, None, "'I can not approach him.' -- The speaker states this. ENG"),
    (10, None, "'Come on, Kostya, you must.' -- The speaker states this. ENG"),
    (11, None, "'Got it, let's move on.' -- The speaker wraps up the exchange in the kitchen.")
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("anya", "Давай, Костя, ты должен.")
