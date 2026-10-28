# Authoring module for kukhnya-s04e11-scene-16.
ID = 'kukhnya-s04e11-scene-16'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 11
SCENE = 16
TITLE = 'Разговор с диспетчером  (Talking to the Dispatcher)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.11'
SOURCE_FILE = 'sources/kukhnya/s04/e11.ru.srt'
INTRO = 'Still trapped in the apartment elevator hours later, Max loses his patience when a voice finally crackles over the intercom and decides to show Vika how a tough guy talks.'
OPENER = "Let's go through each line of the intercom argument in the elevator."
TRANSITION = "Now let's hear the whole elevator intercom scene again."
OUTRO = "Notice how Russian says 'we want you to pull us out': because the subject changes, you must use 'chtoby' followed by the past-tense word. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('guest', 'Я слушаю, есть там кто?', 'I am listening, is anyone in there?', [(245, 'Я слушаю, есть там кто')], ''),
    ('max', 'Слушай, а сколько можно вас ждать?', 'Listen, how long can we wait for you?', [(246, 'а сколько ждать вас можно')], 'adapted for A1 clarity'),
    ('vika', 'Дай я скажу, ты всё испортишь.', 'Let me talk, you will ruin everything.', [(247, 'Ты опять все испортишь')], 'adapted for A1 clarity'),
    ('vika', 'Здравствуйте, мы тут давно застряли.', 'Hello, we have been stuck in here for a long time.', [(248, 'Здравствуйте')], 'adapted for A1 clarity'),
    ('vika', 'Мы хотим, чтобы вы нас вытащили.', 'We want you to pull us out.', [(251, 'И мы хотим, чтобы вы нас вытащили')], 'adapted for A1 clarity'),
    ('guest', 'Вообще-то у нас уже смена закончилась.', 'Actually, our shift has already ended.', [(252, 'Вообще-то у нас смена закончилась')], 'adapted for A1 clarity'),
    ('max', 'Погоди, какая ещё смена закончилась?', 'Hold on, what do you mean your shift ended?', [(253, 'Ну, погоди. Какая смена')], 'adapted for A1 clarity'),
    ('max', 'Я твой голос хорошо запомнил!', 'I have remembered your voice well!', [(254, 'Я твой голос запомнил')], 'adapted for A1 clarity'),
    ('max', 'Сейчас выйду и найду тебя, понял?', 'I will get out right now and find you, got it?', [(254, 'выйду, найду тебя, понял')], 'adapted for A1 clarity'),
    ('guest', 'Это ты сейчас мне сказал?', 'Did you just say that to me?', [(255, 'Это ты мне')], 'adapted for A1 clarity'),
    ('max', 'Да, тебе, так что открывай быстро!', 'Yes, to you, so open up quickly!', [(256, 'Да, да, тебе')], 'adapted for A1 clarity'),
    ('max', 'Вот так мужчины решают проблемы.', 'That is how men solve problems.', [(258, 'мужики решают проблемы')], 'adapted for A1 clarity'),
    ('max', 'А не пожалуйста, помогите нам.', "And not 'please help us'.", [(259, 'пожалуйста, помогите')], 'adapted for A1 clarity'),
]
WALK = [
    (0, None, '\'I am listening, is anyone in there?\' The guest opens up calmly with Max and chooses "slushayu" ("I\'m listening", from the root "slushat") so Max hears the exact meaning.'),
    (1, None, '\'Listen, how long can we wait for you?\' Pushing back promptly to Vika, Max leans on "mozhno" ("it is possible, one may"), which carries the whole predicate in Russian without needing "it is".'),
    (2, None, "'Let me talk, you will ruin everything.' Vika pushes back earnestly with a sigh, keeping the focus on what actually matters here."),
    (3, None, '\'Hello, we have been stuck in here for a long time.\' Vika briskly directs this formal greeting at the start of the beat using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (4, None, "'We want you to pull us out.' Vika cuts in dryly hearing the guest, to clear the air between them once and for all."),
    (5, None, "'Actually, our shift has already ended.' The guest weighs in earnestly across the room, before Vika can change the subject."),
    (6, None, '\'Hold on, what do you mean your shift ended?\' Underscoring the shift before the guest, Max chooses "zakonchilas" ("ended", from the root "zakonchitsya") so the guest hears the exact meaning.'),
    (7, None, "'I have remembered your voice well!' Max proceeds boldly without any doubt, grounding the moment in plain reality."),
    (8, None, "'I will get out right now and find you, got it?' Max presses sharply if there is more going on behind the scenes."),
    (9, None, "'Did you just say that to me?' Opening up promptly on the spot, the guest keeps normal statement word order here, turning the line into a question for Max purely through rising pitch."),
    (10, None, "'Yes, to you, so open up quickly!' Max continues dryly around the guest, letting the remark speak for itself."),
    (11, None, "'That is how men solve problems.' Max replies quietly without holding back, watching the guest's face to see how the news lands."),
    (12, None, '\'And not \'please help us\'.\' Max weighs in naturally in this beat and brings in "pomogite" ("help", from "pomoch") as the key Russian word here.'),
]
