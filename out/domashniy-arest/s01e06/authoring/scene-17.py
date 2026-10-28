# Authoring module for domashniy-arest-s01e06-scene-17.
ID = 'domashniy-arest-s01e06-scene-17'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 6
SCENE = 17
TITLE = "Кто гном? Я гном?  (Who's a Dwarf? I'm a Dwarf?)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'anna': 'Анна', 'lyova': 'Лёва', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.06'
SOURCE_FILE = 'sources/domashniy-arest/s01/e06.ru.dual.srt'
INTRO = "Out on the snowy footbridge in the park, Samson is walking home from the library with his new copy of The Art of War. Now young Lieutenant Lyova, disguised in a teenager's winter hat and jacket, steps onto the bridge to provoke Samson into a fight on camera. Let's listen in Russian first."
OPENER = "Let's go through it line by line. Disguised as a schoolboy in a bright pom-pom hat, short Lieutenant Lyova blocks Samson's path on the bridge and tries to make him lose his temper."
TRANSITION = "Now let's listen to the whole encounter on the footbridge again."
OUTRO = "So instead of catching Samson beating up a schoolboy, the camera caught him rescuing a drowning boy from the freezing river. Next time we'll return to the communal flat, where Arkady is finishing Klavdia Viktorovna's pedicure. See you next time!"
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('lyova', 'Ты глупый, и вся семья такая! Понял?', 'You are stupid, and your whole family is like that! Understand?', [(614, 'Ты'), (615, 'у тебя'), (616, 'Понял')], 'crude insults in 610–616 replaced with clean A1'),
    ('samson', 'Понял, понял. Ты чего?', "Got it, got it. What's your problem?", [(617, 'Понял. Понял'), (614, 'Ты чего')], ''),
    ('lyova', 'Ну, давай, ударь меня!', 'Well, come on, hit me!', [(621, 'Ну, давай, ударь меня')], ''),
    ('samson', 'Ты что думаешь, Самсонов дурак?', 'What, do you think Samsonov is a fool?', [(622, 'ты что думаешь, Самсонов дурак')], ''),
    ('samson', 'Сыночек, ты провокатор от Осипенко?', 'Sonny, are you a provocateur from Osipenko?', [(623, 'Сыночек'), (623, 'ты провокатор от Осипенко')], ''),
    ('samson', 'Кто здесь снимает? Кто оператор? Запись идёт?', 'Who is filming here? Who is the cameraman? Is it recording?', [(626, 'Кто здесь снимает? Кто оператор'), (628, 'Запись идет')], ''),
    ('anna', 'Идёт, идёт.', "It's rolling, it's rolling.", [(629, 'Идет, идет')], ''),
    ('lyova', 'Книжку отдай! Давай сюда книгу!', 'Give back the little book! Hand the book over here!', [(636, 'Книжку отдай'), (637, 'Давай сюда книгу')], ''),
    ('samson', 'Тихо, тихо! Книгу давай сюда.', 'Easy, easy! Hand the book over here.', [(643, 'Тихо, тихо'), (639, 'Книгу'), (639, 'давай'), (637, 'сюда')], ''),
    ('samson', 'Слышь, ты, гном! Иди отсюда.', 'Listen here, you dwarf! Go away from here.', [(648, 'Слышь, ты гном'), (649, 'отсюда')], "crude verb in 649 replaced with 'Иди'"),
    ('lyova', 'Кто гном? Я гном?', "Who's a dwarf? I'm a dwarf?", [(650, 'Кто гном? Я гном')], ''),
    ('lyova', 'Ну всё, конец тебе!', "Right then, you're finished!", [(652, 'Ну все'), (652, 'тебе')], "slang 'хана' -> 'конец'"),
    ('lyova', 'Тону! Помоги!', "I'm drowning! Help me!", [(655, 'Тону'), (657, 'Помоги')], ''),
    ('samson', 'А чего тону? Там мелко! Сиди!', "What do you mean drowning? It's shallow there! Stay put!", [(656, 'тону? Там'), (653, 'Сиди')], "ASR 'А че тону? Там мелкая' -> 'А чего тону? Там мелко'"),
    ('anna', 'Всё, убежал! Тут уже ничего не сделать.', "That's it, he ran away! Nothing can be done here now.", [(661, 'Все'), (662, 'убежал'), (663, 'тут ничего не')], "colloquial 'наковырять' -> 'сделать'"),
]
WALK = [
    (0, 'Ты глупый, и вся семья такая!', "'You are stupid, and your whole family is like that!' Lyova hurls insults right in Samson's face."),
    (0, 'Понял?', "'Understand?' That is the masculine past tense of 'to understand', used as a sharp 'got it?'."),
    (1, 'Понял, понял.', "'Got it, got it.' Samson stays surprisingly calm after his reading lessons."),
    (1, 'Ты чего?', "'What's your problem?' Literally 'you what?'. From the bushes, Lavrov whispers that Lyova is doing great, though so far there is no effect."),
    (2, None, "'Well, come on, hit me!' This phrase means 'strike me!' or 'hit me!'. Instead of swinging, Samson looks around suspiciously."),
    (3, None, "'What, do you think Samsonov is a fool?' The verb meaning 'do think' works together with 'fool' to carry the point."),
    (4, None, "'Sonny, are you a provocateur from Osipenko?' He uses an affectionate diminutive for 'son' to mock the baby-faced lieutenant, and then spots the camera lens in the bushes."),
    (5, 'Кто здесь снимает?', "'Who is filming here?' The verb for 'to take off' also means 'to film' or 'to shoot video'."),
    (5, 'Кто оператор?', "'Who is the cameraman?' Samson looks straight into the bushes."),
    (5, 'Запись идёт?', "'Is it recording?' Literally 'is the recording going?'."),
    (6, None, "'It's rolling, it's rolling.' From behind the bushes, the camera operator confirms the video is running."),
    (7, 'Книжку отдай!', "'Give back the little book!' Desperate to provoke a fight, Lyova grabs at Samson's library book."),
    (7, 'Давай сюда книгу!', "'Hand the book over here!' Notice how the noun for 'book' takes the feminine object ending."),
    (8, 'Тихо, тихо!', "'Easy, easy!' It literally means 'quiet, quiet!'."),
    (8, 'Книгу давай сюда.', "'Hand the book over here.' Samson effortlessly takes his library book back from the tiny lieutenant."),
    (9, 'Слышь, ты, гном!', "'Listen here, you dwarf!' Samson mutters the one word Lyova cannot stand."),
    (9, 'Иди отсюда.', "'Go away from here.' It literally means 'walk away from here'."),
    (10, None, "'Who's a dwarf? I'm a dwarf?' Lyova completely loses his head over being called short."),
    (11, None, "'Right then, you're finished!' Literally 'end to you!'. Lyova takes a running leap at Samson, misses him completely, and flies straight over the bridge railing into the icy river."),
    (12, None, "'I'm drowning! Help me!' Flailing in the freezing water, Lyova cries out for help."),
    (13, 'А чего тону?', "'What do you mean drowning?' Samson peers over the railing at him."),
    (13, 'Там мелко!', "'It's shallow there!' This phrase means 'it is shallow'."),
    (13, 'Сиди!', "'Stay put!' Seeing that Lyova really cannot swim, Samson throws off his jacket, dives into the river, and pulls the soaking-wet lieutenant onto the bank while passers-by film the rescue."),
    (14, 'Всё, убежал!', "'That's it, he ran away!' Shivering and humiliated, Lyova bolts from the park."),
    (14, 'Тут уже ничего не сделать.', "'Nothing can be done here now.' The agents realise their trap has only made Samson look like a hero."),
]
