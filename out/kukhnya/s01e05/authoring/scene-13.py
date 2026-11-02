# Authoring module for kukhnya-s01e05-scene-13.
ID = 'kukhnya-s01e05-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 13
TITLE = 'Предупреждение от Вики  (A Warning from Vika)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = 'Vika, who runs the Claude Monet dining room, has heard that Nastya has been crying all day. She finds Max at his station in the kitchen, in the middle of making soup, and gives him a warning. Listen to it in Russian first.'
OPENER = 'Now slowly. Vika is angry and precise, which makes her easy to follow.'
TRANSITION = 'Now see how much you catch.'
OUTRO = 'Vika\'s warning is made of pieces you can reuse: "never again", "for the last time", "because of you". And Max\'s reply shows the classic way to survive it: say "understood" and go back to the soup.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('vika', 'Макс, иди сюда прямо сейчас!', 'Max, come here right now!', [(159, 'Иди сюда')], ""),
    ('max', 'Привет, Вика, что случилось?', 'Hi, Vika, what happened?', [(159, 'привет')], ""),
    ('vika', 'Слушай меня очень внимательно.', 'Listen to me very carefully.', [(160, 'слушай сюда внимательно')], ""),
    ('vika', 'Не трогай моих официанток больше никогда!', "Don't touch my waitresses ever again!", [(161, 'кого-то из моих официанток')], ""),
    ('vika', 'Или я приму очень строгие меры.', 'Or I will take very strict measures.', [(162, 'Тебе вот этот')], ""),
    ('max', 'Вика, почему ты так сильно злишься?', 'Vika, why are you so angry?', [(163, 'Вик, да что с тобой')], ""),
    ('vika', 'Бедная Настя плачет из-за тебя весь день.', 'Poor Nastya has been crying because of you all day.', [(164, 'Настя рыдает целый день')], ""),
    ('max', 'Но между нами абсолютно ничего не было!', 'But absolutely nothing happened between us!', [(165, 'ничего не было')], ""),
    ('vika', 'Я видела ваши странные разговоры у бара.', 'I saw your strange conversations by the bar.', [(167, 'я все видела')], ""),
    ('vika', 'Я предупредила тебя в последний раз.', 'I warned you for the last time.', [(169, 'Я тебя предупредила')], ""),
    ('max', 'Хорошо, я понял тебя, спасибо за совет.', 'Alright, I understood you, thanks for the advice.', [(168, 'мне все равно')], ""),
    ('max', 'Теперь мне нужно быстро посолить суп.', 'Now I need to quickly salt the soup.', [(173, 'осталось посолить')], ""),
    ('max', 'И не забыть добавить свежих сливок.', 'And not forget to add fresh cream.', [(174, 'добавить сливок')], ""),
]
WALK = [
    (0, None, [
        "'Max, come here right now!' Russian has two words for 'here': one for where you are, and ",
        ('vika', 'сюда'),
        " for where you're going. ",
        ('vika', 'иди'), ('vika', 'сюда'),
        ", 'come here', needs the second."
    ]),
    (1, None, [
        "'Hi, Vika, what happened?' is the phrase used when someone ",
        ('max', 'что'), ('max', 'случилось?'),
        " looks upset. It originates from the noun for 'an occurrence'."
    ]),
    (2, None, [
        "'Listen to me very carefully.' , 'listen to me', is built ",
        ('vika', 'Слушай'), ('vika', 'меня'),
        ' with ',
        ('vika', 'меня'),
        " directly, with no 'to'. ",
        ('vika', 'внимательно.'),
        ", 'carefully', is the attention word again."
    ]),
    (3, None, [
        "'Don't touch my waitresses ever again!' signifies 'waitresses', created by adding a ",
        ('vika', 'официанток'),
        " itresses', created by adding a feminine ending to the standard word. 'Never again' translates to ",
        ('vika', 'больше'), ('vika', 'никогда!'),
        ", literally 'more never'."
    ]),
    (4, None, [
        "'Or I will take very strict measures.' expresses 'I'll take measures', using the ",
        ('vika', 'приму'), ('vika', 'меры.'),
        ' same base verb Nastya used for taking a decision. ',
        ('vika', 'строгие'),
        ", 'strict', is plural to match ",
        ('vika', 'меры.')
    ]),
    (5, None, [
        "'Vika, why are you so angry?' is used for 'are you angry', ",
        ('max', 'злишься?'),
        ' coming from a reflexive verb that always carries the -sya ending. ',
        ('max', 'так'), ('max', 'сильно'),
        " represents 'so strongly'."
    ]),
    (6, None, [
        "'Poor Nastya has been crying because of you all day.' , 'because of you', points the ",
        ('vika', 'из-за'), ('vika', 'тебя'),
        ' finger at someone. ',
        ('vika', 'плачет'),
        " is present tense, since she's still crying."
    ]),
    (7, None, [
        "'But absolutely nothing happened between us!' , 'between us', puts 'us' in ",
        ('max', 'между'), ('max', 'нами'),
        ' the instrumental form. Max also stacks the negatives again: ',
        ('max', 'ничего'), ('max', 'не'), ('max', 'было!')
    ]),
    (8, None, [
        "'I saw your strange conversations by the bar.' ends in -la, so the one ",
        ('vika', 'видела'),
        ' who saw is a woman. ',
        ('vika', 'у'), ('vika', 'бара.'),
        " indicates 'by the bar', with ",
        ('vika', 'у'),
        ", 'at', changing the ending of the noun."
    ]),
    (9, None, [
        "'I warned you for the last time.' , 'warned', begins with a prefix ",
        ('vika', 'предупредила'),
        " meaning 'before', since a warning comes before trouble. 'For the last time' is written as ",
        ('vika', 'в'), ('vika', 'последний'), ('vika', 'раз.')
    ]),
    (10, None, [
        "'Alright, I understood you, thanks for the advice.' , 'thanks for the advice', is ",
        ('max', 'спасибо'), ('max', 'за'), ('max', 'совет.'),
        ' said a little too politely. The word ',
        ('max', 'совет.'),
        " also denotes 'council', as in Soviet."
    ]),
    (11, None, [
        "'Now I need to quickly salt the soup.' , 'to salt', has the root ",
        ('max', 'посолить'),
        " for 'salt' at its core. ",
        ('max', 'мне'), ('max', 'нужно'),
        " functions as 'I need to', literally 'to me it's needed'."
    ]),
    (12, None, [
        "'And not forget to add fresh cream.' The word for 'cream' only exists in the plural. ",
        ('max', 'свежих'), ('max', 'сливок.'),
        " takes the 'of' form, describing 'some fresh cream'."
    ]),
]
