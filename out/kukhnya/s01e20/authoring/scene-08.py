# Authoring module for kukhnya-s01e20-scene-08.
ID = 'kukhnya-s01e20-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 8
TITLE = 'Утренний сюрприз  (A Morning Surprise)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = "Next morning, Kostya wakes up in a playful mood. Here's the Russian."
OPENER = "Let's break that down."
TRANSITION = "Here's the moment again."
OUTRO = "We'll see what Nastya has in mind next. In poigrat, 'to play for a bit', the po- at the front makes it short. See you next time!"
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('kostya', 'Доброе утро, Настя.', 'Good morning, Nastya.', [], ''),
    ('nastya', 'Доброе утро. Ты уже проснулся?', 'Good morning. Are you awake already?', [], ''),
    ('kostya', 'Да. Иди ко мне.', 'Yes. Come here.', [], ''),
    ('nastya', 'Проснулся и хочешь поиграть со мной?', 'You are awake and want to play with me?', [(141, 'проснулся и хочешь поиграть со мной?')], ''),
    ('kostya', 'А что, нельзя?', 'What, am I not allowed?', [(142, 'А')], ''),
]
WALK = [
    (0, None, "'Good morning, Nastya.' The word utro, 'morning', is neuter, so 'good' is dobroe."),
    (1, None, "'Morning. Are you up already?' The word prosnulsya, 'woke up', has the ending -sya; a woman would say prosnulas."),
    (2, None, "'Yes. Come here.' Russian says idi ko mne, literally 'go to me'. The word k, 'to', grows into ko before mne."),
    (3, None, "'Awake and wanting to play with me?' With so mnoy, 'with me', the little word s, 'with', becomes so before mnoy."),
    (4, None, "'What, am I not allowed?' The word nelzya means 'it's not allowed', and a nelzya? asks 'can't I?'"),
]
