# Authoring module for kukhnya-s03e16-scene-18.
ID = 'kukhnya-s03e16-scene-18'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 16
SCENE = 18
TITLE = "Гнев Нагиева после покера  (Nagiyev's Wrath After Poker)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.16'
SOURCE_FILE = 'sources/kukhnya/s03/e16.ru.srt'
INTRO = "Outraged that his poker guests got violently ill at the table and took all his money, Nagiyev bursts into the kitchen, refuses to listen to Chef Barinov's excuses about Grandpa Kirill's ghost, and vows revenge tomorrow! Listen first."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Everyone leaves EXCEPT Senya and Fedya, whom Chef Barinov ordered to clean the kitchen—setting the stage for Barinov's ghostly ambush in Scene Nineteen! See you next time!"
CLOSING = ('barinov', 'Всего хорошего!')
STORY = [
    ('nagiyev', 'Скажите мне, вы гостей чем сейчас накормили?', 'Tell me, what did you just feed the guests?', [(311, 'Вы гостей чем накормили')], 'adapted'),
    ('nagiyev', 'Я все свои деньги сегодня из-за вас спустил!', 'I lost all my money tonight because of you!', [(313, 'из-за вас спустил')], 'adapted'),
    ('barinov', 'Подождите, а что это вообще сейчас было?', 'Wait, what on earth just happened?', [(314, 'это было')], 'adapted'),
    ('barinov', 'А это, наверное, новый фирменный соус Макса!', "That was probably Max's new signature sauce!", [(315, 'А это, наверное, соус')], 'adapted'),
    ('barinov', 'Давай мы лучше завтра будем во всём разбираться, Дима.', "Let's sort everything out tomorrow instead, Dima.", [(317, 'завтра разбираться')], 'adapted'),
    ('max', 'Может быть, это снова призрак деда Кирилла нам мстит?', 'Maybe it is the ghost of Grandpa Kirill taking revenge on us again?', [(318, 'Может, это призрак деда Кирилла'), (319, 'Он нам мстит')], 'adapted'),
    ('barinov', 'Дима, действительно, на кухне творится какая-то чертовщина!', 'Dima, really, some kind of devilry is going on in the kitchen!', [(320, 'действительно, на кухне творится какая-то чертовщина')], 'adapted'),
    ('nagiyev', 'Надоело, я завтра приду и всех строго накажу!', 'I am fed up, I will come tomorrow and punish everyone strictly!', [(321, 'Надоело'), (323, 'завтра приду'), (331, 'всех накажу')], 'adapted'),
    ('nagiyev', 'Уходите отсюда, я видеть вас больше не хочу!', 'Get out of here, I do not want to see you anymore!', [(324, 'Видеть вас не хочу')], 'adapted'),
    ('barinov', 'А убирать кто на кухне будет, призрак уборщицы?', 'And who is going to clean up in the kitchen, the ghost of the cleaning lady?', [(327, 'А убирать кто будет'), (328, 'Призрак уборщицы')], 'adapted'),
    ('max', 'Всё, мы все уходим, до завтра, шеф!', 'Alright, we are all leaving, until tomorrow, Chef!', [(329, 'Все, до завтра')], 'adapted'),
    ('max', 'Покер — это игра такая, брат, непредсказуемая!', 'Poker is that kind of game, brother, unpredictable!', [(332, 'Покер, игра такая, брат, непредсказуемая')], 'adapted'),
]
WALK = [
    (0, None, "'Tell me, what did you just feed the guests?' Nagiyev wonders sharply where this conversation is heading next."),
    (1, None, '\'I lost all my money tonight because of you!\' Addressing his money around Barinov, Nagiyev uses "dengi" ("money") to carry the main weight of the thought.'),
    (2, None, '\'Wait, what on earth just happened?\' Answering dryly around Nagiyev, Barinov drops in "voobshche" ("in general, altogether") to sum up the whole situation at once.'),
    (3, None, "'That was probably Max's new signature sauce!' Barinov responds plainly with Max, shifting the mood of the conversation in a single beat."),
    (4, None, '\'Let\'s sort everything out tomorrow instead, Dima.\' Barinov pushes back briskly on the spot and reaches for the Russian word "razbiratsya" ("to understand well") right at the heart of the line.'),
    (5, None, "'Maybe it is the ghost of Grandpa Kirill taking revenge on us again?' Returning to the ghost during the talk, Max keeps normal statement word order here, turning the line into a question for Barinov purely through rising pitch."),
    (6, None, "'Dima, really, some kind of devilry is going on in the kitchen!' Barinov counters promptly with a shrug, without trying to dress up how he really feels."),
    (7, None, '\'I am fed up, I will come tomorrow and punish everyone strictly!\' Nagiyev speaks quietly to Barinov and chooses "nadoyelo" ("has got boring", from the root "nadoyest") so Barinov hears the exact meaning.'),
    (8, None, "'Get out of here, I do not want to see you anymore!' Nagiyev counters sharply with a shrug, refusing to let the moment slip past."),
    (9, None, "'And who is going to clean up in the kitchen, the ghost of the cleaning lady?' Barinov wonders sharply about what Max just brought up."),
    (10, None, '\'Alright, we are all leaving, until tomorrow, Chef!\' Max steps in firmly before Barinov and brings in "ukhodim" ("are leaving", from "ukhodit") as the key Russian word here.'),
    (11, None, '\'Poker is that kind of game, brother, unpredictable!\' Underscoring how unpredictable things are in front of Barinov, Max links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
]
