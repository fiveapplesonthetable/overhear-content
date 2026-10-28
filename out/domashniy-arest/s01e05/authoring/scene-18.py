# Authoring module for domashniy-arest-s01e05-scene-18.
ID = 'domashniy-arest-s01e05-scene-18'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 5
SCENE = 18
TITLE = 'Мой избранный  (My Chosen One)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nina': 'Нина', 'samson': 'Самсон', 'yulia': 'Юля'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.05'
SOURCE_FILE = 'sources/domashniy-arest/s01/e05.ru.dual.srt'
INTRO = "Out at lawyer Danila Golovkin's wooden country house, Samson is sitting at the dining table with Nina and teenage Yulia. Still believing Danila's story that he heroically rammed a gang of bank robbers, Samson is basking in Nina's praise—until he notices Yulia smirking at her phone. Let's listen in Russian first."
OPENER = "Let's go through it line by line. At the dacha table, Nina heaps cabbage onto Samson's plate and apologises for scolding him earlier."
TRANSITION = "Now let's listen to the whole family scene at the dacha table again."
OUTRO = "So Samson confiscated Yulia's phone and sent her to wash the dishes, while back at City Hall Pasha phoned the governor to brag that he was shredding the archive folder so the blind would never see it. Next time we'll return to the communal flat, where Marina comes home to find her room wrecked. See you next time!"
CLOSING = ('samson', 'Пока!')
STORY = [
    ('nina', 'Вань, давай капусточки тебе. Извини, Вань, была неправа.', 'Vanya, let me give you some cabbage. Sorry, Vanya, I was wrong.', [(687, 'Вань, давай капусточки тебе'), (689, 'извини, Вань'), (689, 'была неправа')], ''),
    ('samson', 'Лидер! Я вообще с детства чувствовал.', "A leader! I've felt it since childhood, actually.", [(691, 'Лидер'), (692, 'я вообще с детства чувствовал')], ''),
    ('samson', 'Я человек особенный.', 'I am a special person.', [(693, 'человек'), (693, 'особенный')], 'simplified from 693'),
    ('nina', 'Ты считай, Вань, как мой избранный.', 'Consider yourself, Vanya, like my chosen one.', [(694, 'ты считай, Вань, как мой избранный')], ''),
    ('samson', 'А что ты сидишь, улыбаешься?', 'And why are you sitting there smiling?', [(698, 'А что ты сидишь, улыбаешься')], ''),
    ('samson', 'Что ты в телефон свой тычешь?', 'Why are you poking at your phone?', [(698, 'в телефон свой тычешь')], "'Что ты' repeated for split question"),
    ('samson', 'Папа город от преступников очищает!', 'Dad is cleaning the city of criminals!', [(699, 'город от преступников очищает')], "'он' -> 'Папа' for clarity"),
    ('nina', 'Юля, телефон отложи.', 'Yulia, put the phone aside.', [(700, 'Юля, телефон отложи')], ''),
    ('nina', 'С матерью как разговариваешь? Ты вообще почему здесь?', 'How are you talking to your mother? Why are you even here?', [(702, 'С матерью как разговариваешь'), (704, 'Ты вообще почему здесь')], ''),
    ('nina', 'Почему ты не в школе?', "Why aren't you at school?", [(705, 'в школе')], "cue 705 'Что они в школе?' is a transcription slip for 'Почему ты не в школе?'"),
    ('yulia', 'А у меня учительница по математике заболела.', 'My maths teacher fell ill.', [(707, 'а у меня учительница по математике заболела')], ''),
    ('yulia', 'А я всё выучила. Я хорошо учусь.', "And I've learned everything. I do well at school.", [(709, 'А я все выучила'), (710, 'Я хорошо учусь')], ''),
    ('nina', 'Юля, встала и пошла мыть посуду!', 'Yulia, get up and go wash the dishes!', [(716, 'Юля'), (716, 'встала и пошла мыть посуду')], "crude 'рот закрыла' omitted"),
    ('samson', 'Подожди, Нина. Телефончик дай сюда!', 'Hold on, Nina. Hand the little phone over here!', [(717, 'Подожди, Нина. Телефончик дай сюда')], ''),
    ('yulia', 'Пожалуйста.', 'Here you go.', [(720, 'Пожалуйста')], ''),
    ('samson', 'Пока ещё на мои деньги куплен! Встала и мыть посуду, шагом марш!', "It's still bought with my money! Get up and wash the dishes, forward march!", [(721, 'Пока еще на мои деньги куплен'), (722, 'Встала и мыть посуду, шагом марш')], ''),
]
WALK = [
    (0, 'Вань, давай капусточки тебе.', "'Vanya, let me give you some cabbage.' She uses an affectionate diminutive for 'cabbage'."),
    (0, 'Извини, Вань, была неправа.', "'Sorry, Vanya, I was wrong.' Because Nina is a woman, both the action word 'was' and the short form 'wrong' end in '-a'. Samson puffs out his chest."),
    (1, 'Лидер!', "'A leader!' Samson is delighted with the word and repeats it proudly."),
    (1, 'Я вообще с детства чувствовал.', "'I've felt it since childhood, actually.' Then he sums up what he felt."),
    (2, None, "'I am a special person.' Putting the describing word after the word gives it extra weight: 'a person who is special'. Nina looks at him admiringly."),
    (3, None, "'Consider yourself, Vanya, like my chosen one.' Just then, Samson spots teenage Yulia smirking at her smartphone across the table."),
    (4, None, "'And why are you sitting there smiling?' He glares across the table at his daughter."),
    (5, None, "'Why are you poking at your phone?' The action word means to poke or jab at a screen."),
    (6, None, "'Dad is cleaning the city of criminals!' Samson still believes Danila's lie that he rammed a getaway car full of robbers. Afraid that Yulia will read the real news about Samson's drunken crash into the Society of the Blind, Nina quickly steps in."),
    (7, None, "'Yulia, put the phone aside.' Here, Yulia clicks her tongue in annoyance, and Nina snaps at her."),
    (8, 'С матерью как разговариваешь?', "'How are you talking to your mother?' After 'with', the word 'mother' takes the 'with/as' ending."),
    (8, 'Ты вообще почему здесь?', "'Why are you even here?' Nina realises it is the middle of a school day."),
    (9, None, "'Why aren't you at school?' Russian says 'in school' rather than 'at school' when asking why she isn't in class."),
    (10, None, "'My maths teacher fell ill.' Notice how Russian says 'teacher by mathematics' using the little word with the 'to/for' form. When Nina asks about her other subjects, Yulia shrugs."),
    (11, 'А я всё выучила.', "'And I've learned everything.' The prefix on the action word shows she has learned it all thoroughly."),
    (11, 'Я хорошо учусь.', "'I do well at school.' Literally 'I study well'. Nina is not having it."),
    (12, None, "'Yulia, get up and go wash the dishes!' Notice how Russian parents often use past-tense forms—literally 'stood up and went!'—as an immediate command. Before Yulia can leave with her phone, Samson holds out his hand."),
    (13, 'Подожди, Нина.', "'Hold on, Nina.' Samson decides to take charge of the situation himself."),
    (13, 'Телефончик дай сюда!', "'Hand the little phone over here!' Literally 'give hither'."),
    (14, None, "'Here you go.' The same word means both 'please' and 'here you are' when handing something over."),
    (15, 'Пока ещё на мои деньги куплен!', "'It's still bought with my money!' Samson reminds his daughter that for now that phone was bought with his money!"),
    (15, 'Встала и мыть посуду, шагом марш!', "'Get up and wash the dishes, forward march!' He finishes with the army drill command 'forward march!'."),
]
