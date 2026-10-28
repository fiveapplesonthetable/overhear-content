ID = 'kukhnya-s06e02-scene-10'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 10
TITLE = "Катя отшивает обоих  (Katya Rejects Both of Them)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "denis": "anja", "katya": "angelina"}
LABELS = {"denis": "Денис", "katya": "Катя"}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'

INTRO = "At the party, Nikita asks to drink with Katya and gets a sarcastic toast about her mother's advice; moments later, Denis tries his luck and gets toasted as a runaway coward."

STORY = [
    ('denis', 'Катя, я могу с тобой выпить?', 'Katya, may I have a drink with you?', [(160, 'Катя, я могу с тобой выпить?')], 'exact'),
    ('katya', 'Давай за мою маму и за ее мудрые советы.', "Let's drink to my mom and her wise advice.", [(161, 'Давай за мою маму и за ее мудрые советы')], 'exact'),
    ('katya', 'Ведь ты без них никуда, свободен.', 'After all, you are nowhere without them, dismissed.', [(162, 'Ведь ты без них никуда'), (163, 'Свободен')], 'adapted'),
    ('denis', 'Катя, привет.', 'Katya, hi.', [(164, 'Катя. Привет')], 'exact'),
    ('katya', 'Тоже выпить со мной хочешь, да?', 'You want to have a drink with me too, right?', [(165, 'Тоже выпить со мной хочешь, да?')], 'exact'),
    ('katya', 'За тех, которые сбегают, выпьешь?', 'To those who run away, will you drink?', [(167, 'которые сбегают'), (168, 'Выпьешь?')], 'adapted'),
    ('denis', 'Нет, за это не буду.', 'No, I will not drink to that.', [(168, 'Нет')], 'adapted'),
    ('katya', 'А я выпью, у тебя это очень хорошо получается.', 'Well I will drink, you are very good at that.', [(169, 'А я выпью'), (170, 'Ведь у тебя это очень хорошо получается')], 'adapted'),
    ('denis', 'Она права, я виноват.', 'She is right, I am at fault.', [(171, 'Она права, я виноват')], 'exact'),
    ('denis', 'Это не повод так долго обижаться.', 'That is no reason to stay offended for so long.', [(172, 'не повод так долго обижаться')], 'adapted'),
    ('denis', 'Я не понял, она у нас работает?', 'I do not understand, does she work here with us?', [(174, 'Я не понял, она у нас работает?')], 'exact'),
    ('denis', 'Моя тоже тут работает.', 'Mine works here too.', [(175, 'Моя тоже')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Katya, may I have a drink with you?' Nikita addresses the listener with the informal singular 'you' alongside 'to drink'."),
    (1, None, "'Let's drink to my mom and her wise advice.' Here the Russian phrasing highlights 'come on' before landing on 'advice'."),
    (2, None, "'After all, you are nowhere without them, dismissed.' Katya addresses the listener with the informal singular 'you' alongside 'free'. Denis answers right away."),
    (3, None, "'Katya, hi.' Denis anchors the line on 'Katya', while 'hello' completes the thought."),
    (4, None, "'You want to have a drink with me too, right?' In Russian, the idea of 'also' flows naturally into 'yes' without extra filler words."),
    (5, None, "'To those who run away, will you drink?' Spoken Russian keeps this brisk, leaning on 'for' and finishing on 'will drink'. Denis answers right away."),
    (6, None, "'No, I will not drink to that.' Denis anchors the line on 'no', while 'will be' completes the thought."),
    (7, None, "'Well I will drink, you are very good at that.' Katya brings out the contrast between 'and' and 'I' in a few short words."),
    (8, None, "'She is right, I am at fault.' Notice how Russian expresses 'she' and 'at fault' with crisp inflection rather than helper words. Nikita answers right away."),
    (9, None, "'That is no reason to stay offended for so long.' The meaning hinges on 'this' working together with 'to stay offended' in spoken Russian."),
    (10, None, "'I do not understand, does she work here with us?' In Russian, the idea of 'I' flows naturally into 'works' without extra filler words."),
    (11, None, "'Mine works here too.' Nikita anchors the line on 'my', while 'works' completes the thought."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Still unaware that they are both pining for Katya, Nikita and Denis bond over their stubborn girlfriends. See you next time!'
CLOSING = ("denis", "Пока!")
