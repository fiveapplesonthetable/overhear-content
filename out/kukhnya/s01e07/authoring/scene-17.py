# Authoring module for kukhnya-s01e07-scene-17.
ID = 'kukhnya-s01e07-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 17
TITLE = 'В гостях у Кости  (Visiting Kostya)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = "Hoping to spend a quiet romantic evening together, bartender Kostya invites waitress Nastya over to his small rented apartment. Everything seems promising until the passionate animal lover catches sight of a wooden mousetrap on the floor, sparking an emotional explosion that shatters their romantic mood. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine Kostya and Nastya's apartment visit line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "What was meant to be a cozy evening turns into a dramatic breakup over a household mousetrap. Next time you watch the episode, listen for the Russian expressions for 'defenseless' and 'to see' — you will catch every word right away. See you next time!"
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('kostya', 'Настя, добро пожаловать в мою квартиру.', 'Nastya, welcome to my apartment.', [], ''),
    ('nastya', 'У тебя здесь довольно уютно и чисто.', 'It is quite cozy and clean here with you.', [], ''),
    ('kostya', 'Ну, точнее, эта квартира съёмная.', 'Well, more precisely, this apartment is rented.', [(333, 'не моя съемная')], ''),
    ('kostya', 'Вот диван, стул, мягкая подушка.', 'Here is a couch, a chair, a soft pillow.', [(334, 'Диван, стул'), (335, 'Подушка')], ''),
    ('nastya', 'Костя, я всё это отлично вижу.', 'Kostya, I can see all this perfectly.', [(335, 'Кость, я вижу')], ''),
    ('kostya', 'Проходи скорее и садись на диван.', 'Come in quickly and sit on the couch.', [(336, 'Проходи, проходи. Садись')], ''),
    ('nastya', 'Ой, а что это там внизу?', 'Oh, and what is that down there?', [(337, 'Что это?')], ''),
    ('nastya', 'Боже мой, это же мёртвая мышь!', 'My God, that is a dead mouse!', [(338, 'Это…')], ''),
    ('nastya', 'Костя, ты самый настоящий жестокий убийца!', 'Kostya, you are a real cruel murderer!', [(338, 'Ты убийца')], ''),
    ('nastya', 'Ты погубил маленькую беззащитную мышь!', 'You destroyed a little defenseless mouse!', [(339, 'Убил маленькую ни в чем не повинную мышь')], ''),
    ('kostya', 'Настя, но это обычная мышеловка!', 'Nastya, but this is an ordinary mousetrap!', [], ''),
    ('nastya', 'Ты ещё сидишь и спокойно улыбаешься?!', 'You are still sitting and calmly smiling?!', [(340, 'Еще лыбится сидит')], ''),
    ('nastya', 'Ты поступил как настоящий монстр!', 'You acted like a real monster!', [(342, 'Ты вообще монстр')], ''),
]
WALK = [
    (0, None, "'Nastya, welcome to my apartment.' Kostya opens the door and welcomes his guest inside."),
    (1, None, "'It is quite cozy and clean here with you.' Nastya looks around the small room with genuine curiosity."),
    (2, None, "'Well, more precisely, this apartment is rented.' The bartender clarifies the legal status of his modest home."),
    (3, None, "'Here is a couch, a chair, a soft pillow.' Kostya enthusiastically lists all the basic furniture in the room."),
    (4, None, "'Kostya, I can see all this perfectly.' Nastya interrupts his awkward tour with gentle amusement."),
    (5, None, "'Come in quickly and sit on the couch.' Kostya hospitably invites the waitress to make herself comfortable."),
    (6, None, "'Oh, and what is that down there?' Nastya suddenly notices a strange object near the baseboard."),
    (7, None, "'My God, that is a dead mouse!' She gasps in utter horror upon recognizing the small rodent."),
    (8, None, "'Kostya, you are a real cruel murderer!' The passionate animal lover vents her moral fury at the bartender."),
    (9, None, "'You destroyed a little defenseless mouse!' Nastya is heartbroken by the tragic fate of the innocent creature."),
    (10, None, "'Nastya, but this is an ordinary mousetrap!' Kostya tries to defend himself with practical household logic."),
    (11, None, "'You are still sitting and calmly smiling?!' She accuses him of complete callousness and lack of empathy."),
    (12, None, "'You acted like a real monster!' Nastya turns on her heel and storms out into the corridor."),
]
