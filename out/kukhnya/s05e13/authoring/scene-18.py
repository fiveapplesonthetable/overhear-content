# Authoring module for kukhnya-s05e13-scene-18.
ID = 'kukhnya-s05e13-scene-18'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 13
SCENE = 18
TITLE = 'Брат-близнец и приговор  (The Twin Brother and the Verdict)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.13'
SOURCE_FILE = 'sources/kukhnya/s05/e13.ru.srt'
INTRO = "In a last-ditch effort, Kostya introduces supplier Timur as Max's supposed evil twin brother Vlad who committed all of Max's mistakes, but Judge Barinov threatens Timur with prison for perjury."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'The imaginary courtroom trial ends in a medieval execution fantasy, snapping the cooks back to the kitchen. See you next time!'
CLOSING = ('barinov', 'Хорошего дня!')
STORY = [
    ('kostya', 'Смотрите, это же тайный брат Максима Влад!', "Look, this is Maxim's secret brother Vlad!", [(244, 'Это брат-близнец Максима')], 'adapted'),
    ('kostya', 'Это он всю жизнь хитро подставлял Макса!', 'He is the one who slyly framed Max his whole life!', [(246, 'Это он всю жизнь подставлял Макса')], 'adapted'),
    ('kostya', 'Это он всем врал и поцеловал Сашу!', 'He is the one who lied to everyone and kissed Sasha!', [(248, 'И это он всем врал')], 'adapted'),
    ('barinov', 'Скажите суду, Влад, это действительно правда?', 'Tell the court, Vlad, is this really true?', [(250, 'Влад, это правда')], 'adapted'),
    ('barinov', 'Вы можете ответить нормально, да или нет?', 'Can you answer properly, yes or no?', [(251, 'Вы можете ответить нормально')], 'adapted'),
    ('max', 'Судья, брат, ну что ты ко мне пристал?', 'Judge, brother, why are you pestering me?', [(253, 'Судья, брат, что ты пристал')], 'adapted'),
    ('max', 'Я же тебе только что нормально кивнул!', 'I just nodded to you properly!', [(254, 'нормально кивнул')], 'adapted'),
    ('barinov', 'За ложные показания вы отправитесь в тюрьму!', 'For false testimony you will go to prison!', [(256, 'ложных показаний вы отправитесь в тюрьму')], 'adapted'),
    ('max', 'Я буду жаловаться на вас в суд!', 'I will file a complaint against you in court!', [(257, 'Я буду жаловаться на вас')], 'adapted'),
    ('barinov', 'Итак, суд постановил признать Лаврова Максима виновным!', 'Thus, the court has ruled to find Maxim Lavrov guilty!', [(259, 'Итак, суд постановил признать Лаврова Максима')], 'adapted'),
    ('barinov', 'Признать его виновным в коварной измене жене!', 'To find him guilty of treacherous infidelity to his wife!', [(260, 'виновным в измене')], 'adapted'),
    ('barinov', 'Приговор суда привести в исполнение немедленно!', "Carry out the court's sentence immediately!", [(261, 'привести в исполнение немедленно')], 'adapted'),
]
WALK = [
    (0, None, "'Look, this is Maxim's secret brother Vlad!' Kostya opens up steadily beside Max, shifting the mood of the conversation in a single beat."),
    (1, None, '\'He is the one who slyly framed Max his whole life!\' Focusing on the life on the spot, Kostya lands on "podstavlyal" ("frame, set up", built on "podstavlyat") to keep the statement grounded.'),
    (2, None, '\'He is the one who lied to everyone and kissed Sasha!\' Kostya answers briskly beside Barinov and brings in "potseloval" ("to kiss", from "potselovat") as the key Russian word here.'),
    (3, None, "'Tell the court, Vlad, is this really true?' Barinov challenges straight out where this conversation is heading next."),
    (4, None, '\'Can you answer properly, yes or no?\' Barinov replies pointedly before Max and brings in "normalno" ("fine, OK") to make the meaning unmistakable.'),
    (5, None, '\'Judge, brother, why are you pestering me?\' Answering earnestly around Barinov, Max puts the question word "chto" right at the start so Barinov hears the focus immediately.'),
    (6, None, "'I just nodded to you properly!' Max counters calmly without a pause, keeping the focus on what actually matters here."),
    (7, None, '\'For false testimony you will go to prison!\' Bringing up the testimony in this beat, Barinov chooses "pokazaniya" ("testimony", from the root "pokazaniye") so Max hears the exact meaning.'),
    (8, None, '\'I will file a complaint against you in court!\' Answering naturally around Barinov, the "-sya" ending on "zhalovatsya" ("complain") marks an action that unfolds mutually or turns back on the speaker.'),
    (9, None, "'Thus, the court has ruled to find Maxim Lavrov guilty!' Barinov fires back calmly during the talk, testing Max's reaction in the middle of the exchange."),
    (10, None, '\'To find him guilty of treacherous infidelity to his wife!\' Touching on the treason with Max, Barinov lands on "vinovnym" ("guilty", built on "vinovnyy") to keep the statement grounded.'),
    (11, None, '\'Carry out the court\'s sentence immediately!\' Focusing on the execution on the spot, Barinov puts the emphasis on "ispolneniye" ("execution, fulfillment") in the middle of the talk.'),
]
