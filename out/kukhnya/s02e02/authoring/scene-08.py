ID = "kukhnya-s02e02-scene-08"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 2
SCENE = 8
TITLE = "Держи  (Here You Go)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "anton": "anja", "max": "angelina"}
LABELS = {"anya": "Аня", "anton": "Антон", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S2.02"
SOURCE_FILE = "sources/kukhnya/s02/e02.ru.dual.srt"

INTRO = "In the middle of the kitchen chaos, a very brief exchange happens between two people handing over an item. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ('anya', 'Привет.', 'Hi.', [], 'new'),
    ('anton', 'Привет, аня.', 'Hi, my friend.', [], 'new'),
    ('anya', 'Вот твоя вещь.', 'Here is your thing.', [], 'new'),
    ('anya', 'Возьми это.', 'Take this.', [], 'new'),
    ('anya', 'Держи.', 'Here you go.', [(157, 'Держи')], ''),
    ('anton', 'Спасибо.', 'Thanks.', [], 'new'),
    ('anton', 'Это мне?', 'Is this for me?', [], 'new'),
    ('anya', 'Да, тебе.', 'Yes, for you.', [], 'new'),
    ('anton', 'Очень хорошо.', 'Very good.', [], 'new'),
    ('anton', 'Я рад.', 'I am glad.', [], 'new'),
    ('anya', 'Пожалуйста.', "You're welcome.", [], 'new'),
    ('anya', 'Я пойду.', 'I will go.', [], 'new'),
    ('anton', 'Пока.', 'Bye.', [], 'new')
]

OPENER = "Let's listen to this short interaction."

WALK = [
    (0, None, "'Hi.' A quick greeting."),
    (1, None, "'Hi, my friend.' — Notice the interjection meaning 'hi' paired with the noun for 'Anya'."),
    (2, None, "'Here is your thing.' Something needed to be returned."),
    (3, None, "'Take this.' A simple command."),
    (4, 'Держи.', "'Here you go.' Giving the item over."),
    (5, None, "'Thanks.' Gratitude is always nice."),
    (6, None, "'Is this for me?' Double checking to be sure."),
    (7, None, "'Yes, for you.' Confirming the recipient."),
    (8, None, "'Very good.' Being satisfied with the item."),
    (9, None, "'I am glad.' Showing positive emotion."),
    (10, None, "'You're welcome.' A polite response."),
    (11, None, "'I will go.' Time to leave."),
    (12, None, "'Bye.' A short farewell.")
]

TRANSITION = "Now let's hear the whole thing once more."

OUTRO = "That wraps up this scene."
CLOSING = ("anya", "До свидания!")
