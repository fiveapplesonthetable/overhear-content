# Authoring module for kukhnya-s01e05-scene-12.
ID = 'kukhnya-s01e05-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 12
TITLE = 'Решительный шаг  (A Decisive Step)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nastya': 'Настя', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "Still in the staff room at Claude Monet, Nastya has heard Sasha's revenge plan: start seeing Kostya, Max's best friend. Nervously, she says yes. Sasha is sure it will work, because she has noticed how Kostya looks at Nastya. Here it is in Russian."
OPENER = "Let's go back and hear Sasha build up her friend's courage, one line at a time."
TRANSITION = 'One more time, at normal pace.'
OUTRO = 'Notice the little words carrying this scene. Small as they are, they make the Russian sound alive.'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Ладно, я согласна на этот план.', 'Alright, I agree to this plan.', [(158, 'Ладно')], ""),
    ('sasha', 'Вот и молодец, ты приняла решение.', "That's a good girl, you made a decision.", [], ""),
    ('nastya', 'Но я всё равно немного боюсь.', 'But I am still a little bit afraid.', [], ""),
    ('sasha', 'Чего именно ты сейчас боишься?', 'What exactly are you afraid of right now?', [], ""),
    ('nastya', 'Вдруг Костя не захочет говорить?', "What if Kostya won't want to talk?", [], ""),
    ('sasha', 'Костя уже давно смотрит на тебя.', 'Kostya has already been looking at you for a long time.', [], ""),
    ('nastya', 'Правда? Ты замечала его взгляды?', 'Really? Did you notice his looks?', [], ""),
    ('sasha', 'Конечно, ты ему очень нравишься.', 'Of course, he likes you very much.', [], ""),
    ('nastya', 'Тогда я пойду к барной стойке.', 'Then I will go to the bar counter.', [], ""),
    ('sasha', 'Улыбнись ему тепло и открыто.', 'Smile at him warmly and openly.', [], ""),
    ('nastya', 'Макс обязательно пожалеет о своём поведении.', 'Max will definitely regret his behavior.', [], ""),
    ('sasha', 'Желаю тебе большой удачи, подруга!', 'I wish you great luck, my friend!', [], ""),
    ('nastya', 'Спасибо за поддержку, дорогая Саша!', 'Thanks for the support, dear Sasha!', [], ""),
]
WALK = [
    (0, None, [
        "'Alright, I agree to this plan.' functions as a relaxed 'okay, fine'. ",
        ('nastya', 'Ладно,'),
        ' The feminine agreement form is seen in ',
        ('nastya', 'согласна'),
        "."
    ]),
    (1, None, [
        "'That's a good girl, you made a decision.' The term ",
        ('sasha', 'молодец,'),
        " translates as 'well done', a masculine noun happily applied to women too. A decision is something you 'take', expressed by ",
        ('sasha', 'приняла'),
        ('sasha', 'решение.')
    ]),
    (2, None, [
        "'But I am still a little bit afraid.' Here, ",
        ('nastya', 'немного'),
        " serves as the equivalent for 'a little'. The phrase ",
        ('nastya', 'всё'),
        ('nastya', 'равно'),
        " literally says 'all the same', but acts as 'still'."
    ]),
    (3, None, [
        "'What exactly are you afraid of right now?' To ask 'what' someone is afraid of, you start with ",
        ('sasha', 'Чего'),
        " instead of the basic form, leading into ",
        ('sasha', 'боишься?')
    ]),
    (4, None, [
        "'What if Kostya won't want to talk?' The word ",
        ('nastya', 'Вдруг'),
        " usually represents 'suddenly', but here at the beginning of a worried question it acts as 'what if'. The sequence ",
        ('nastya', 'не'),
        ('nastya', 'захочет'),
        " is a future tense meaning 'won't want'."
    ]),
    (5, None, [
        "'Kostya has already been looking at you for a long time.' The action uses the present tense verb ",
        ('sasha', 'смотрит'),
        " because it started long ago and continues. You direct this action 'at' someone using ",
        ('sasha', 'на'),
        ('sasha', 'тебя.')
    ]),
    (6, None, [
        "'Really? Did you notice his looks?' In this context, ",
        ('nastya', 'взгляды?'),
        " expresses 'glances' or 'looks'. The ongoing action of observing is captured by ",
        ('nastya', 'замечала'),
        " in the past."
    ]),
    (7, None, [
        "'Of course, he likes you very much.' The phrasing ",
        ('sasha', 'ты'),
        ('sasha', 'ему'),
        ('sasha', 'нравишься.'),
        " works backwards, literally saying 'you to him are pleasing'."
    ]),
    (8, None, [
        "'Then I will go to the bar counter.' The single word ",
        ('nastya', 'пойду'),
        " indicates 'I will go'. Moving 'towards' a destination requires ",
        ('nastya', 'к'),
        ('nastya', 'барной'),
        ('nastya', 'стойке.')
    ]),
    (9, None, [
        "'Smile at him warmly and openly.' The command to smile is ",
        ('sasha', 'Улыбнись'),
        ", where the ending is shortened after a vowel. The adverbs 'warmly' and 'openly' show up as ",
        ('sasha', 'тепло'),
        " and ",
        ('sasha', 'открыто.')
    ]),
    (10, None, [
        "'Max will definitely regret his behavior.' The feeling of regret is carried by ",
        ('nastya', 'пожалеет'),
        ". To point back to Max as the owner of the behavior, the sentence relies on ",
        ('nastya', 'своём'),
        "."
    ]),
    (11, None, [
        "'I wish you great luck, my friend!' A typical good wish opens with ",
        ('sasha', 'Желаю'),
        ('sasha', 'тебе'),
        ". What you wish for takes a special ending, giving us the fragment ",
        ('sasha', 'большой'),
        ('sasha', 'удачи,')
    ]),
    (12, None, [
        "'Thanks for the support, dear Sasha!' The adjective ",
        ('nastya', 'дорогая'),
        " expresses 'dear' but also literally translates to 'expensive'. The exact phrase ",
        ('nastya', 'Спасибо'),
        ('nastya', 'за'),
        ('nastya', 'поддержку,'),
        " is what she said to Vika earlier."
    ]),
]
