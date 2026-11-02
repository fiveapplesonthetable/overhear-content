# Authoring module for kukhnya-s01e04-scene-02.
ID = 'kukhnya-s01e04-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = 'Встреча конкурентов  (Encounter of the Competitors)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = 'Outside, Chef Barinov meets his rival, Elena Sokolova, and mocks her for hiring cooks through a newspaper ad. Elena replies smoothly that some very good people have already applied, and some may be from his own kitchen. Here is the Russian first.'
OPENER = 'Back to the war of words.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Barinov swears he'll eat his hat, and Elena calmly wishes him bon appetit. If you remember anything, take the Russian phrase for 'I\'ll eat my hat'." 
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Елена, вы набираете поваров по объявлению?', 'Elena, are you hiring cooks through an ad?', [(6, 'вы персонал по объявлению набираете')], ''),
    ('elena', 'Здравствуйте, Виктор Петрович. Да, мы расширяемся.', 'Hello, Viktor Petrovich. Yes, we are expanding.', [(6, 'Виктор Петрович')], ''),
    ('barinov', 'Поставьте лучше табличку возле метро!', 'You had better put a sign near the metro!', [(7, 'Вы бы лучше табличку у метро поставили')], ''),
    ('elena', 'В этом нет никакой необходимости.', 'There is no need for that.', [(9, 'в этом нет необходимости')], ''),
    ('barinov', 'Нормальные профессионалы не ищут работу по газетам.', 'Normal professionals do not look for work in newspapers.', [(8, 'проходимость профессиональных поваров выше')], ''),
    ('elena', 'Ко мне уже пришли отличные кандидаты.', 'Excellent candidates have already come to me.', [(10, 'пришло несколько отличных поваров')], ''),
    ('barinov', 'И из каких ресторанов эти люди?', 'And from which restaurants are these people?', [], ''),
    ('elena', 'Некоторые работают в очень достойных местах.', 'Some work in very respectable places.', [(11, 'некоторые из них работают в достойных ресторанах')], ''),
    ('barinov', 'Неужели кто-то уходит из хороших ресторанов?', 'Could someone really be leaving good restaurants?', [], ''),
    ('elena', 'Может быть, даже из вашего ресторана.', 'Maybe even from your restaurant.', [(13, 'если вы считаете свой ресторан')], ''),
    ('barinov', 'Я съем колпак, если мои повара уйдут!', "I will eat my chef's hat if my cooks leave!", [(14, 'Я съем свой колпак, если узнаю, что кто-то из моих')], ''),
    ('elena', 'Тогда заранее желаю вам приятного аппетита!', 'Then in advance I wish you bon appétit!', [(15, 'Тогда приятного аппетита')], ''),
    ('barinov', 'Мои люди преданы мне до конца.', 'My people are loyal to me to the end.', [], ''),
]
WALK = [
    (0, None, [
        "'Elena, are you hiring cooks through an ad?' The expression for gathering up is ",
        ("barinov", "набираете"),
        ", and it is the action word for hiring a team. ",
        ("barinov", "по объявлению?"),
        " literally means 'by an announcement', meaning through an ad."
    ]),
    (1, None, [
        "'Hello, Viktor Petrovich. Yes, we are expanding.' Elena uses his name and father's name, ",
        ("elena", "Виктор Петрович."),
        ", which is formal. The phrase for 'we are expanding' is ",
        ("elena", "расширяемся."),
        ", built from the term for 'wide': we widen ourselves."
    ]),
    (2, None, [
        "'You had better put a sign near the metro!' The expression for 'better', ",
        ("barinov", "лучше"),
        ", before a command turns it into advice. ",
        ("barinov", "табличку"),
        " is a small sign, and ",
        ("barinov", "возле"),
        " translates to 'next to'."
    ]),
    (3, None, [
        "'There is no need for that.' ",
        ("elena", "нет никакой необходимости."),
        " literally means 'there isn't any necessity'. After ",
        ("elena", "нет"),
        ", the translation for necessity takes the 'of' form, ",
        ("elena", "необходимости."),
        "."
    ]),
    (4, None, [
        "'Normal professionals do not look for work in newspapers.' ",
        ("barinov", "ищут"),
        ", meaning 'they look for', is built from the action word to search. ",
        ("barinov", "по газетам."),
        " translates to 'through newspapers'."
    ]),
    (5, None, [
        "'Excellent candidates have already come to me.' ",
        ("elena", "Ко мне"),
        " is the little word for 'to', with an extra 'o' to make it easier to say. The Russian expression for 'came' is ",
        ("elena", "пришли"),
        ", describing a past action by many."
    ]),
    (6, None, [
        "'And from which restaurants are these people?' The expression for 'out of', ",
        ("barinov", "из"),
        ", puts both following words in the multiple 'of' form: ",
        ("barinov", "каких ресторанов"),
        "."
    ]),
    (7, None, [
        "'Some work in very respectable places.' The describing word for 'respectable' or 'worthy', ",
        ("elena", "достойных"),
        ", is built from the phrase for dignity. ",
        ("elena", "местах."),
        " literally means 'in places'."
    ]),
    (8, None, [
        "'Could someone really be leaving good restaurants?' The term for disbelief, ",
        ("barinov", "Неужели"),
        ", opens a question like 'can it really be?'. ",
        ("barinov", "из хороших ресторанов?"),
        " translates to 'from good restaurants'."
    ]),
    (9, None, [
        "'Maybe even from your restaurant.' Literally, this translates to 'may be, even out of your restaurant'. Elena stays polite, so the word for 'your' takes the 'of' ending: ",
        ("elena", "вашего ресторана."),
        "."
    ]),
    (10, None, [
        "'I will eat my chef's hat if my cooks leave!' The phrase for 'I will eat', ",
        ("barinov", "съем"),
        ", describes a future action. ",
        ("barinov", "колпак,"),
        " is the tall chef's hat, and ",
        ("barinov", "уйдут!"),
        " translates to 'they will leave'."
    ]),
    (11, None, [
        "'Then in advance I wish you bon appétit!' The Russian expression for 'in advance' is ",
        ("elena", "заранее"),
        ". ",
        ("elena", "приятного аппетита!"),
        " is in the 'of' form because a wish usually takes it after the action word for 'I wish'."
    ]),
    (12, None, [
        "'My people are loyal to me to the end.' The Russian term for 'devoted', ",
        ("barinov", "преданы"),
        ", and the word to betray are both built from the idea to 'hand over': you hand yourself to someone, or hand them to the enemy. ",
        ("barinov", "до конца."),
        " translates to 'to the end'."
    ]),
]