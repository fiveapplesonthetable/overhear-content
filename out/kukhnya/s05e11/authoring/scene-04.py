# Authoring module for kukhnya-s05e11-scene-04.
ID = 'kukhnya-s05e11-scene-04'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 11
SCENE = 4
TITLE = 'Пересоленный гратен  (The Oversalted Gratin)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'denis': 'Денис', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.11'
SOURCE_FILE = 'sources/kukhnya/s05/e11.ru.srt'
INTRO = 'In the kitchen, Artyom plates his gratin for Eleonora, but when Chef Barinov and Lyova taste it, the dish is terribly oversalted. Refusing to admit to Eleonora that he hired an incompetent cook, Viktor tells Artyom he has potential and secretly remakes the meal himself.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'That brings the kitchen tasting to a close. Notice how Chef Barinov softens his criticism and decides to cook the dishes himself to save face. See you next time!'
CLOSING = ('barinov', 'Хорошего дня!')
STORY = [
    ('barinov', 'Фартук можно взять там.', 'You can take an apron over there.', [(65, 'Фартук можно взять там')], 'adapted'),
    ('denis', 'Гратен! Сейчас принесу перепёлку.', 'The gratin! Right now I will bring the quail.', [(66, 'Гратен, сейчас принесу перепелку')], 'adapted'),
    ('barinov', 'Ну как?', 'Well, how is it?', [(67, 'Ну как')], 'adapted'),
    ('lyova', 'Отлично справился!', 'He handled it great!', [(68, 'отлично справился')], 'adapted'),
    ('barinov', 'Можно подумать, у тебя с первого раза получилось.', 'One might think you got it right the first time.', [(69, 'Можно подумать, у тебя'), (69, 'первый раз получилось')], 'adapted'),
    ('denis', 'Ну как гратен?', 'Well, how is the gratin?', [(70, 'Ну как, гратен')], 'adapted'),
    ('barinov', 'Для первого раза неплохо.', 'Not bad for the first time.', [(71, 'Для первого раза неплохо')], 'adapted'),
    ('barinov', 'Видно, что есть потенциал.', 'It is clear that there is potential.', [(72, 'Видно, что есть потенциал')], 'adapted'),
    ('barinov', 'Но чтобы не было вопросов, лучше я приготовлю сам.', 'But so there are no questions, I had better cook it myself.', [(73, 'чтобы не было вопросов, лучше я приготовлю сам')], 'adapted'),
    ('barinov', 'А ты отдохни пока.', 'And you rest for now.', [(74, 'а ты отдохни пока')], 'adapted'),
    ('denis', 'Спасибо, Виктор Петрович.', 'Thank you, Viktor Petrovich.', [], ''),
    ('lyova', 'Зачем вы его защищаете, шеф?', 'Why are you defending him, chef?', [(67, 'Ну как')], 'adapted'),
]
WALK = [
    (0, None, "'You can take an apron over there.' Since Denis can take an apron over there, Barinov does not waste words on excuses."),
    (1, None, "'The gratin! Right now I will bring the quail.' Denis declares that right now he will bring the quail as the tension in the room peaks. Russian puts the key word right up front so his emotion lands on the first beat."),
    (2, None, '\'Well, how is it?\' Wondering how it is cuts straight through the tension between Barinov and Denis. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (3, None, "'He handled it great!' Over the test and the truth, Lyova lets his real feelings show."),
    (4, None, '\'One might think you got it right the first time.\' Explaining that one might think Denis got it right the first time lays the cards on the table for Denis. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (5, None, '\'Well, how is the gratin?\' By wondering how the gratin is, Denis presses Barinov for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (6, None, "'Not bad for the first time.' Between the work and the argument, Barinov gives Denis a quick, grounded response."),
    (7, None, "'It is clear that there is potential.' Pointing out that it is clear that there is potential gives Denis a sobering reality check."),
    (8, None, "'But so there are no questions, I had better cook it myself.' Barinov explains that there are no questions he had better cook it himself, keeping his voice calm and direct."),
    (9, None, "'And you rest for now.' Realizing that Denis rests for now changes how Barinov handles the situation."),
    (10, None, "'Thank you, Viktor Petrovich.' Over the point and the dish, Denis answers Barinov without a second thought."),
    (11, None, '\'Why are you defending him, chef?\' Asking why Barinov defending him is is how Lyova puts Barinov on the spot. Notice how he sticks to the formal "you", keeping a professional line between them.'),
]
