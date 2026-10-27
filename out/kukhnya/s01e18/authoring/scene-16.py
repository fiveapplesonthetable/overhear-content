ID = "kukhnya-s01e18-scene-16"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 16
TITLE = "Неуклюжий бармен  (The Clumsy Bartender)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {'anya': 'Костя', 'leva': 'Шеф'}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = "Cues 295-301."

INTRO = (
    "Kostya approaches Viktor's table to try and swap the poisoned cognac bottle back. Viktor gets angry and tells him to go away. Let us listen to their conversation in Russian first."
)

STORY = [
    ('anya', 'Извините, приятного вам вечера.', 'Excuse me, have a pleasant evening.', [(295, 'Извини, приятного вечера.')], 'adapted'),
    ('leva', 'Что тебе нужно от меня?', 'What do you need from me?', [(296, 'Че тебе надо?')], 'adapted'),
    ('anya', 'Мне нужна эта бутылка.', 'I need this bottle.', [(297, 'Я бутылку...')], 'adapted'),
    ('leva', 'О чём ты говоришь?', 'What are you talking about?', [(298, 'это... Чего я бутылка?')], 'adapted'),
    ('anya', 'Я возьму эту бутылку.', 'I will take this bottle.', [(299, 'Я вот эту вот возьму,')], 'adapted'),
    ('anya', 'А вам поставлю другую.', 'And I will put another one for you.', [(299, 'а эту поставлю.')], 'adapted'),
    ('leva', 'Тебе что, совсем нечего делать?', 'Do you have absolutely nothing to do?', [(300, 'Тебе заняться нечем?')], 'adapted'),
    ('anya', 'Нет, я просто хочу дать другую.', 'No, I just want to give another one.', [(300, 'Нет, я вот эту вот возьму, а эту поставлю.')], 'adapted'),
    ('leva', 'Не трогай ничего, иди отсюда!', 'Do not touch anything, get out of here!', [(301, 'Иди отсюда.')], 'adapted'),
    ('anya', 'Но я должен её забрать.', 'But I must take it.', [], 'adapted'),
    ('leva', 'Я сказал, иди отсюда!', 'I said, get out of here!', [], 'adapted'),
    ('anya', 'Понятно, давай дальше.', "Got it, let's move on.", [], '')
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None, "'Excuse me, have a pleasant evening.' -- The speaker states this. ENG"),
    (1, None, "'What do you need from me?' -- The speaker states this. ENG"),
    (2, None, "'I need this bottle.' -- The speaker states this. ENG"),
    (3, None, "'What are you talking about?' -- The speaker states this. ENG"),
    (4, None, "'I will take this bottle.' -- The speaker states this. ENG"),
    (5, None, "'And I will put another one for you.' -- The speaker states this. ENG"),
    (6, None, "'Do you have absolutely nothing to do?' -- The speaker states this. ENG"),
    (7, None, "'No, I just want to give another one.' -- The speaker states this. ENG"),
    (8, None, "'Do not touch anything, get out of here!' -- The speaker states this. ENG"),
    (9, None, "'But I must take it.' -- The speaker states this. ENG"),
    (10, None, "'I said, get out of here!' -- The speaker states this. ENG"),
    (11, None, "'Got it, let's move on.' -- The speaker wraps up the exchange in the kitchen.")
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("leva", "Я сказал, иди отсюда!")
