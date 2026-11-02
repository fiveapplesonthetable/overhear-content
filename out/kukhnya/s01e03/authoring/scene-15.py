# Authoring module for kukhnya-s01e03-scene-15.
ID = 'kukhnya-s01e03-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 15
TITLE = 'Живой гусь  (The Live Goose)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nastya': 'Настя', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "In the back hallway, Nastya has found something in a delivery box: a live goose. When she hears the chef intends to cook it, she decides to save it, and Sasha helps her work out how. Here's the Russian first."
OPENER = "Now Nastya's rescue."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Nastya has a secret passenger and a warm corner to put him in. Notice that "I can\'t abandon him" is a nice phrase for any rescue.'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Саша, иди скорее сюда!', 'Sasha, come here quickly!', [(265, 'сюда и позвала')], ''),
    ('sasha', 'Что случилось, Настя?', 'What happened, Nastya?', [(261, 'на минуточку')], ''),
    ('nastya', 'Посмотри, в коробке сидит живой гусь!', 'Look, a live goose is sitting in the box!', [(264, 'гусь')], ''),
    ('sasha', 'Откуда здесь взялся этот гусь?', 'Where did this goose come from?', [(264, 'гусь')], ''),
    ('nastya', 'Шеф хотел приготовить из него блюдо.', 'The chef wanted to prepare a dish out of it.', [], ''),
    ('sasha', 'Ты решила спасти эту птицу?', 'Did you decide to save this bird?', [], ''),
    ('nastya', 'Да, я не могу его бросить.', 'Yes, I cannot abandon him.', [], ''),
    ('sasha', 'Шеф будет в ярости, если узнает!', 'The chef will be furious if he finds out!', [], ''),
    ('nastya', 'Я спрячу гуся в безопасное место.', 'I will hide the goose in a safe place.', [(271, 'перепрячу')], ''),
    ('sasha', 'Только делай это очень осторожно.', 'Just do it very carefully.', [], ''),
    ('nastya', 'Его чуть не нашли гости.', 'The guests almost found him.', [(267, 'в зал'), (270, 'тебя здесь найдут')], ''),
    ('sasha', 'Унеси его с кухни прямо сейчас!', 'Carry him away from the kitchen right now!', [(265, 'сюда и позвала')], ''),
    ('nastya', 'Я найду для него тёплый угол.', 'I will find a warm corner for him.', [(271, 'перепрячу')], ''),
    ('sasha', 'И возвращайся скорее к работе!', 'And return to work quickly!', [(266, 'Спасибо большое')], ''),
]
WALK = [
    (0, None, [
        "'Sasha, come here quickly!' Observe how ",
        ('nastya', 'иди'),
        ('nastya', 'сюда!'),
        " literally translates to 'go to here', the normal way to call someone over. The word for 'faster' is ",
        ('nastya', 'скорее'),
        ', to hurry them along.'
    ]),
    (1, None, [
        "'What happened, Nastya?' Observe how ",
        ('sasha', 'Что'),
        ('sasha', 'случилось,'),
        " translates to 'what happened?', the question for anything gone wrong. It is built from the word for an event."
    ]),
    (2, None, [
        "'Look, a live goose is sitting in the box!' The word for 'have a look' is ",
        ('nastya', 'Посмотри,'),
        '. Russians say a goose ',
        ('nastya', 'сидит'),
        ', sits, in a box, and ',
        ('nastya', 'в'),
        ('nastya', 'коробке'),
        " translates to 'in the box'."
    ]),
    (3, None, [
        "'Where did this goose come from?' Asking where from takes its own word: ",
        ('sasha', 'Откуда'),
        ', next to the word for where, and where to. ',
        ('sasha', 'взялся'),
        " is an action word built from taking, and the ending turns 'took' into 'turned up out of nowhere'."
    ]),
    (4, None, [
        "'The chef wanted to prepare a dish out of it.' Looking closely, ",
        ('nastya', 'из'),
        ('nastya', 'него'),
        " translates to 'out of him', since the word for a goose is a male animal shape, with an extra letter added. ",
        ('nastya', 'хотел'),
        ('nastya', 'приготовить'),
        " translates to 'wanted to prepare'."
    ]),
    (5, None, [
        "'Did you decide to save this bird?' We can hear ",
        ('sasha', 'решила'),
        ' translates to decided, with an ending for a woman. ',
        ('sasha', 'спасти'),
        ', the word for to save, shares a root with the word for thank you, and ',
        ('sasha', 'птицу?'),
        " translates to 'bird'."
    ]),
    (6, None, [
        "'Yes, I cannot abandon him.' Here we see ",
        ('nastya', 'бросить.'),
        " translates to both 'throw' and 'abandon'. ",
        ('nastya', 'его'),
        " translates to 'him', the goose."
    ]),
    (7, None, [
        "'The chef will be furious if he finds out!' You will hear ",
        ('sasha', 'будет'),
        ('sasha', 'в'),
        ('sasha', 'ярости,'),
        " literally translates to 'will be in fury'. ",
        ('sasha', 'узнает!'),
        ', finds out, is built from the word for to know, with a little extra at the start.'
    ]),
    (8, None, [
        "'I will hide the goose in a safe place.' In Russian, ",
        ('nastya', 'безопасное'),
        ', safe, is built from the word for without, plus the word for dangerous. ',
        ('nastya', 'спрячу'),
        " translates to 'I will hide'."
    ]),
    (9, None, [
        "'Just do it very carefully.' Observe how ",
        ('sasha', 'Только'),
        ('sasha', 'делай'),
        ('sasha', 'это'),
        " translates to 'only do it'. ",
        ('sasha', 'осторожно.'),
        ', carefully, is the how-word built from the word for careful.'
    ]),
    (10, None, [
        "'The guests almost found him.' We can hear ",
        ('nastya', 'чуть'),
        ('nastya', 'не'),
        " literally translates to 'barely not', meaning 'almost'. ",
        ('nastya', 'нашли'),
        " translates to 'found', and ",
        ('nastya', 'гости.'),
        ', the word for the guests, comes last.'
    ]),
    (11, None, [
        "'Carry him away from the kitchen right now!' Listen carefully, ",
        ('sasha', 'Унеси'),
        ", carry away, is built from the word for to carry, with a piece that means 'away'. ",
        ('sasha', 'с'),
        ('sasha', 'кухни'),
        " translates to 'off the kitchen', with a matching shape for the last letter."
    ]),
    (12, None, [
        "'I will find a warm corner for him.' In Russian, ",
        ('nastya', 'для'),
        ('nastya', 'него'),
        " translates to 'for him', with the extra letter again. ",
        ('nastya', 'тёплый'),
        ('nastya', 'угол.'),
        " translates to 'warm corner', and ",
        ('nastya', 'найду'),
        " translates to 'I will find'."
    ]),
    (13, None, [
        "'And return to work quickly!' Focusing here, ",
        ('sasha', 'возвращайся'),
        ', the word for come back, has a special ending. ',
        ('sasha', 'к'),
        ('sasha', 'работе!'),
        " translates to 'towards work', with a matching shape at the end."
    ]),
]
