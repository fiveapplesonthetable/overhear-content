# Authoring module for kukhnya-s01e08-scene-12.
ID = 'kukhnya-s01e08-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 12
TITLE = 'Воспоминания о Провансе  (Memories of Provence)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'elena': 'Елена', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Still running Barinov's kitchen at Claude Monet, Elena goes over to Louis, the French pastry chef, who does not want her anywhere near his desserts. She finds a way to win him over. It's in Russian first."
OPENER = 'Slowly now. Louis starts out rude, and Elena wins him over with talk of home.'
TRANSITION = 'Now hear it all again, from the cold start to the warm finish.'
OUTRO = "Elena's method is simple: notice an accent, guess where it's from, and talk about home. She starts with u vas takoy znakomyy aktsent, 'you have such a familiar accent'. See you next time."
CLOSING = ('louis', 'Пока!')
STORY = [
    ('elena', 'Луи, чем вы сейчас занимаетесь на десертах?', 'Louis, what are you doing on the desserts right now?', [], ''),
    ('louis', 'Какое вам вообще дело до моих десертов?', 'What business is it of yours regarding my desserts?', [], ''),
    ('elena', 'У вас такой тёплый и знакомый акцент.', 'You have such a warm and familiar accent.', [(131, 'Какой знакомый акцент')], ''),
    ('louis', 'Да, я приехал сюда из самой Франции.', 'Yes, I came here from France itself.', [], ''),
    ('elena', 'Это же Прованс, я абсолютно права?', 'It is Provence, am I absolutely right?', [(132, 'Прованс? Я права')], ''),
    ('louis', 'Да, мадам, вы очень тонко угадали!', 'Yes, madame, you guessed very subtly!', [(133, 'Да')], ''),
    ('elena', 'Я просто обожаю прекрасный Сен-Поль-де-Ванс!', 'I simply adore wonderful Saint-Paul-de-Vence!', [(133, 'Я обожаю Прованс'), (134, 'Особенно я люблю Сан-Поль-де-Ванс')], ''),
    ('louis', 'Невероятно, вся моя семья живёт именно там!', 'Incredible, my whole family lives right there!', [(135, 'Моя семья там живет')], ''),
    ('elena', 'А какие десерты подают в «Золотой голубке»!', "And what desserts they serve at La Colombe d'Or!", [(136, 'А какие десерты подают золотой голубке')], ''),
    ('louis', 'О, мадам, это моё самое любимое место!', 'Oh, madame, that is my most favorite place!', [(137, 'О, мадам')], ''),
    ('elena', 'Там великолепный вид и совершенно волшебная атмосфера.', 'There is a magnificent view and completely magical atmosphere.', [(136, 'Какой там вид')], ''),
    ('louis', 'Спасибо, я словно ненадолго вернулся домой!', 'Thank you, I felt as if I briefly returned home!', [(138, 'Я как будто ненадолго вернулся домой')], ''),
]
WALK = [
    (0, None, "'Louis, what are you doing on the desserts right now?' After zanimatsya, 'to be busy with', 'what' takes the form chem. Kitchen talk puts a station after na, so na desertakh is the dessert section, like na kukhne for the kitchen."),
    (1, None, "'What business is it of yours regarding my desserts?' Louis answers with kakoye vam delo do..., literally 'what business to you up to...', a blunt 'what's it to you'. His vam is polite, but the phrase is rude anyway."),
    (2, None, "'You have such a warm and familiar accent.' Built on znat, 'to know', znakomyy means 'familiar', and znakomyy on its own is an acquaintance. Here takoy, 'such', matches aktsent."),
    (3, None, "'Yes, I came here from France itself.' Louis says priyekhal, from priyekhat, 'to arrive by transport', not on foot. In iz samoy..., samyy means 'the very', so it's 'from the very France'."),
    (4, None, "'It is Provence, am I absolutely right?' A woman says prava, 'right', and a man prav. Adding zhe to eto, 'it's surely', shows she's confident."),
    (5, None, "'Yes, madame, you guessed very subtly!' His ugadali, 'you guessed', means she got it right. The word tonko, 'subtly', comes from tonkiy, 'thin, fine'."),
    (6, None, "'I simply adore wonderful Saint-Paul-de-Vence!' Saying obozhayu, 'I adore', is stronger than lyublyu, 'I love'. In Russian spelling the town keeps its hyphens."),
    (7, None, "'Incredible, my whole family lives right there!' Literally 'not probable', neveroyatno is ne glued to veroyatno. And imenno tam means 'exactly there'."),
    (8, None, "'And what desserts they serve at La Colombe d'Or!' Here kakiye, 'what', makes an exclamation. Russian translates the restaurant's name as 'the golden dove', and after v the name takes -oy and -e."),
    (9, None, "'Oh, madame, that is my most favorite place!' Both moyo, 'my', and samoye lyubimoye, 'most favourite', match mesto, 'place', which is neuter. One mention of his village and Louis is won over."),
    (10, None, "'There is a magnificent view and completely magical atmosphere.' A volshebnik is a wizard, so volshebnyy is 'magical'. The word vid, 'view', also means 'kind' or 'appearance'."),
    (11, None, "'Thank you, I felt as if I briefly returned home!' His slovno, 'as if', is a slightly literary kak budto. Answering 'where to', domoy means 'home', and nenadolgo, 'not for long', is written as one word."),
]
