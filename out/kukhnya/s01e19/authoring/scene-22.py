# Authoring module for kukhnya-s01e19-scene-22.
ID = 'kukhnya-s01e19-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 22
TITLE = 'Здесь и сейчас  (Here and Now)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = "In the last scene, Vika asks Max what matters most to him, and his answer sums up the whole episode. Let the Russian play first, and let it sink in."
OPENER = "Now Max's answer, phrase by phrase."
TRANSITION = 'And one last time, here and now, in Russian.'
OUTRO = "The episode ends on two words you now know, \"zdes' i seychas\", 'here and now'. See you next time!"
CLOSING = ('vika', 'Всего хорошего!')
STORY = [
    ('vika', 'Макс, что для тебя главное?', "Max, what's the most important thing for you?", [], ''),
    ('max', 'Главное — ценить то, что у нас есть.', 'The important thing is to cherish what we have.', [(383, 'Главное — ценить то, что у нас есть')], ''),
    ('vika', 'Что ты имеешь в виду?', 'What do you mean?', [], ''),
    ('max', 'Мы, наш ресторан, наши друзья.', 'Us, our restaurant, our friends.', [], ''),
    ('vika', 'А когда? Потом?', 'And when? Later?', [], ''),
    ('max', 'Нет, не потом.', 'No, not later.', [], ''),
    ('max', 'Здесь и сейчас.', 'Here and now.', [(383, 'здесь и сейчас')], ''),
    ('vika', 'Здесь и сейчас... Мне нравится.', 'Here and now... I like that.', [], ''),
    ('max', 'Тогда давай начнём прямо сейчас.', "Then let's start right now.", [], ''),
    ('vika', 'Давай.', "Let's.", [], ''),
    ('max', 'Ты сегодня очень красивая.', 'You look very beautiful today.', [], ''),
    ('vika', 'Спасибо, Макс.', 'Thank you, Max.', [], ''),
]
WALK = [
    (0, None, "'Max, what's the most important thing for you?' \"Dlya tebya\", 'for you', uses \"dlya\", the 'for' of 'for someone's sake'. \"Glavnoe\" turns up one more time."),
    (1, None, "'The important thing is to cherish what we have.' \"Tsenit'\", 'to value', comes from \"tsena\", 'price', as in \"tsena restorana\" earlier. To value something is to know its price."),
    (2, None, "'What do you mean?' \"Imet' v vidu\", literally 'to have in view', is 'to mean'. \"Chto ty imeesh' v vidu\" is a phrase to learn whole."),
    (3, None, "'Us, our restaurant, our friends.' \"Nash restoran\" and \"nashi druz'ya\": \"nash\", 'our', changes its ending to match. \"Druz'ya\" is the plural of drug."),
    (4, None, "'And when? Later?' \"Potom\" means 'later' or 'then, after that'. \"Kogda\" is 'when'."),
    (5, None, "'No, not later.' \"Ne potom\" puts ne right in front of the word it rejects, so it's 'later' that gets the no."),
    (6, None, "'Here and now.' \"Zdes'\" i \"seychas\": \"zdes'\", 'here', and \"seychas\", 'now'. The two smallest words in the scene carry its message."),
    (7, None, "'Here and now... I like that.' \"Mne nravitsya\", 'it pleases me', is 'I like it'. Earlier in the episode Max said \"ne nravitsya\" about Igor; now it's positive."),
    (8, None, "'Then let's start right now.' \"Davay nachnyom\", 'let's start', is \"davay\" plus the 'we' form. \"Pryamo seychas\" is 'right now', as Igor said."),
    (9, None, "'Let's.' \"Davay\" on its own is a whole 'yes, let's'. It also means 'okay, bye' at the end of a phone call."),
    (10, None, "'You look very beautiful today.' Russians just say \"ty krasivaya\", 'you beautiful', where English says 'you look'. \"Krasivaya\" ends in -aya for a woman."),
    (11, None, "'Thank you, Max.' \"Spasibo\", then the name: the simplest way to end a scene warmly. The ending of the whole episode is a thank you."),
]
