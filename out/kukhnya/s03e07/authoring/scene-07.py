# Authoring module for kukhnya-s03e07-scene-07.
ID = 'kukhnya-s03e07-scene-07'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 7
SCENE = 7
TITLE = 'Запертый на складе и возврат в начало  (Locked in Storage and Back to the Start)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.07'
SOURCE_FILE = 'sources/kukhnya/s03/e07.ru.srt'
INTRO = "Max lures Nagiyev into the storage room and locks the heavy door from the outside. However, realizing this path leads to disaster, we rewind to Kostya's question at the bar."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Locking the owner in the warehouse is clearly a terrible option, so the clock rewinds and the second version begins. Until next time!'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Смотри, он сейчас там на складе.', 'Look, he is in the storage room right now.', [(86, 'Он на складе')], 'adapted'),
    ('max', 'Дима, успокойся, возьми себя в руки!', 'Dima, calm down, pull yourself together!', [(87, 'Успокойся, возьми себя в руки')], 'adapted'),
    ('nagiyev', 'Я в порядке, быстро отпусти меня.', 'I am fine, let me go quickly.', [(88, 'отпусти меня')], 'adapted'),
    ('nagiyev', 'Я очень рад, что вы меня остановили.', 'I am very glad that you stopped me.', [(89, 'Я очень рад, что вы меня остановили')], 'adapted'),
    ('nagiyev', 'Я вообще благодарен, что я в кругу друзей.', 'I am grateful in general that I am in a circle of friends.', [(90, 'Я вообще благодарен, что я в кругу друзей')], 'adapted'),
    ('nagiyev', 'Какой хитрый малый, обманул меня!', 'What a sly fellow, he tricked me!', [(92, 'малый')], 'adapted'),
    ('nagiyev', 'Ну ничего, мы ещё посмотрим.', 'Well never mind, we will see yet.', [(93, 'Ну ничего, ничего')], 'adapted'),
    ('max', 'Дмитрий Владимирович, шеф этого не хотел.', 'Dmitry Vladimirovich, the chef did not want this.', [(95, 'шеф не хотел')], 'adapted'),
    ('max', 'Нет, это очень плохой вариант.', 'No, this is a very bad option.', [(96, 'Это плохой вариант')], 'adapted'),
    ('kostya', 'А давай лучше у Макса спросим.', 'Let us ask Max instead.', [(96, 'А давай у Макса спросим')], 'adapted'),
    ('kostya', 'Макс, скажи, Дмитрий же лучше?', 'Max, tell us, Dmitry is better, right?', [(97, 'Макс, Дмитрий же лучше')], 'adapted'),
    ('max', 'Не факт, меня вообще Дмитрий бесит.', 'Not a fact, Dmitry infuriates me altogether.', [(99, 'Не факт. Меня вообще Дмитрий бесит')], 'adapted'),
]
WALK = [
    (0, None, "'Look, he is in the storage room right now.' Claiming that he is in the storage room right now sounds confident, even if Kostya has doubts."),
    (1, None, "'Dima, calm down, pull yourself together!' Insisting that Kostya should calm down pull themselves together shows Max is not backing down. Russian puts the key word right up front so his emotion lands on the first beat."),
    (2, None, "'I am fine, let me go quickly.' Because he is fine let him go quickly, Nagiyev treats the matter as settled."),
    (3, None, "'I am very glad that you stopped me.' Here being very glad that Kostya stopped him sets up the next turn in their exchange."),
    (4, None, "'I am grateful in general that I am in a circle of friends.' Since he is grateful in general that he is in a circle of friends, Nagiyev does not waste words on excuses."),
    (5, None, "'What a sly fellow, he tricked me!' With the point and story at stake, Nagiyev reacts without holding back. Russian puts the key word right up front so his emotion lands on the first beat."),
    (6, None, "'Well never mind, we will see yet.' Admitting that never mind they will see yet shows Nagiyev being honest for a change."),
    (7, None, "'Dmitry Vladimirovich, the chef did not want this.' Saying that the did not want this is how Max sets the tone with Kostya."),
    (8, None, '\'No, this is a very bad option.\' Once this is a very bad option, Max can finally tell Kostya what he means. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (9, None, "'Let us ask Max instead.' Explaining that they should ask Max instead lays the cards on the table for Max."),
    (10, None, '\'Max, tell us, Dmitry is better, right?\' Questioning whether tell them Dmitry is better right is how Kostya tests Max\'s story. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (11, None, "'Not a fact, Dmitry infuriates me altogether.' Between the kitchen and the story, Max gives Kostya a quick, grounded response."),
]
