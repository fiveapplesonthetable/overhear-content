# Authoring module for kukhnya-s01e03-scene-01.
ID = 'kukhnya-s01e03-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = 'Живой гусь  (The Live Goose)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "This is Kukhnya, the Russian comedy about a hot-tempered chef and the staff of a smart Moscow restaurant called Claude Monet. In this third episode, Max, the young cook, has spent a week unloading deliveries and is longing to be allowed near a stove. Instead, Chef Barinov hands him something very different: a live goose. Here is their conversation in Russian first, so don't worry about catching every word."
OPENER = "Let's go back and watch Max's face."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'So Max has been given a goose and an ultimatum. If "zhivoy", alive, sticks in your head after this, good: you\'ll meet it again.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Доброе утро, шеф!', 'Good morning, chef!', [(46, 'Доброе утро, шеф')], ''),
    ('barinov', 'Здравствуй, огузок. Вот твоя работа.', 'Hello, oguzok. Here is your work.', [(48, 'Иди разгружай продукты')], ''),
    ('max', 'Шеф, это живой гусь!', 'Chef, this is a live goose!', [(36, 'Это чего? Гусь'), (40, 'живой гусь')], ''),
    ('barinov', 'У нас сегодня очень важный банкет.', 'We have a very important banquet today.', [(38, 'у нас же сегодня банкет')], ''),
    ('max', 'Зачем нам живой гусь на кухне?', 'Why do we need a live goose in the kitchen?', [(40, 'На хрена мне на кухне живой гусь')], ''),
    ('barinov', 'Гостям нужен самый свежий продукт!', 'The guests need the freshest product!', [(41, 'вы просили самого свежего')], ''),
    ('max', 'Но я повар, а не мясник.', 'But I am a cook, not a butcher.', [(49, 'ну я же не грузчик, я повар')], ''),
    ('barinov', 'Каждый повар обязан уметь разделывать мясо.', 'Every chef is obliged to know how to butcher meat.', [(59, 'Каждый повар должен быть готов')], ''),
    ('max', 'Что, мне нужно убить его?', 'What, do I need to kill it?', [(56, 'Что, прям насмерть')], ''),
    ('barinov', 'А ты думал, мясо растёт на деревьях?', 'Did you think meat grows on trees?', [(58, 'ты думаешь, что мясо кусочком на деревьях растет')], ''),
    ('max', 'Я никогда в жизни этого не делал.', 'I have never done this in my life.', [], ''),
    ('barinov', 'Убей гуся, или ты уволен!', 'Kill the goose, or you are fired!', [(53, 'Убей гуся'), (60, 'Убей, гуся')], ''),
    ('max', 'Хорошо, я попробую сделать это.', 'Fine, I will try to do it.', [], ''),
]
WALK = [
    (0, None, '\'Good morning, chef!\' The first word ends in "-oye" because "utro", morning, is a neuter word. Say "good evening" and the ending changes, since "vecher" is masculine.'),
    (1, None, '\'Hello, oguzok. Here is your work.\' This is the friendly hello, the polite one with its last syllable cut off. "Oguzok" is Barinov\'s nickname for Max, a cut of meat from the rear of the animal. Then "vot", which points at the goose like "here it is".'),
    (2, None, '\'Chef, this is a live goose!\' You can hear "alive" inside "zhivo!", "quick!", from the knife scene. Max says it with a sinking heart.'),
    (3, None, '\'We have a very important banquet today.\' Russian says "at us" for "we have", and the same pattern turns up all the time. "Banquet" is borrowed, so you can guess it.'),
    (4, None, '\'Why do we need a live goose in the kitchen?\' Max asks it as "what for, to us, a goose?", with "nam", "to us", doing the work of "we need". There is no "do" in the Russian question.'),
    (5, None, '\'The guests need the freshest product!\' Russian says "to the guests is needed", the same shape as "mne nuzhno", I need. And "samyy" in front of "fresh" gives "the freshest".'),
    (6, None, '\'But I am a cook, not a butcher.\' The little "a ne", "and not", sets the two jobs against each other. "Myasnik", butcher, has "myaso", meat, tucked inside.'),
    (7, None, '\'Every chef is obliged to know how to butcher meat.\' A woman would say "obyazana" where Barinov says "obyazan". "Know how" is for skills, not facts.'),
    (8, None, "'What, do I need to kill it?' Max can hardly say the word. It is short and blunt, and the goose is the thing it lands on."),
    (9, None, '\'Did you think meat grows on trees?\' Trees have an odd plural, "derev\'ya", and "on trees" ends in "-yakh". Barinov is mocking the idea that meat arrives clean and ready.'),
    (10, None, '\'I have never done this in my life.\' You get the double negative, "never" and "not", and then "in life", which is how Russians say "in my life". Max sounds almost pitiful.'),
    (11, None, '\'Kill the goose, or you are fired!\' The goose ends in "-ya" here, because a living creature as the object takes that shape. "Fired" is a short, final word.'),
    (12, None, '\'Fine, I will try to do it.\' In "poprobuyu", "I will try", the "po-" at the start means "have a go". Max knows he has no way out.'),
]
