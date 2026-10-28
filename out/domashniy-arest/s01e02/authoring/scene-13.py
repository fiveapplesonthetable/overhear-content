# Authoring module for domashniy-arest-s01e02-scene-13.
ID = 'domashniy-arest-s01e02-scene-13'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 2
SCENE = 13
TITLE = 'Я же извинился  (But I Said Sorry)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'boss': 'Николай Филиппович', 'foreman': 'Прораб', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.02'
SOURCE_FILE = 'sources/domashniy-arest/s01/e02.ru.dual.srt'
INTRO = "Meanwhile, on the building site where Samson used to drive an excavator. Last time, Pasha begged his angry Moscow partners for three more days to find the money, not knowing that someone was secretly watching them. Now Samson has taken Nina's advice and come to apologise to his boss, Nikolai Filippovich, the man he insulted when he quit. Let's listen in Russian first."
OPENER = "Let's go through it slowly. Samson walks into his boss's cabin, all smiles and good manners."
TRANSITION = 'And now the whole scene again, all the way through.'
OUTRO = "Samson has lost his job, but he hasn't lost his spirit, and he's about to prove it with a pile of radiators. Don't worry if it all went by fast. See you next time!"
CLOSING = ('samson', 'Пока!')
STORY = [
    ('samson', 'Николай Филиппович, приветствую. Не помешал?', 'Nikolai Filippovich, greetings. Am I interrupting?', [(354, 'Николай Филиппович, приветствую'), (355, 'Не помешал')], 'two cues joined'),
    ('boss', 'Помешал. Уходи.', 'You are. Go away.', [(356, 'Помешал')], "'Вали отсюда' (get lost) -> 'Уходи'"),
    ('samson', 'Ну что ты, Филиппович. Я же извинился.', "Oh, come on, Filippovich. I said sorry, didn't I?", [(358, 'Филиппович, ну что ты'), (359, 'Я же извинился')], "cue 358 reordered; 'Ладно' dropped"),
    ('boss', 'А я тебя уже простил. Ты уволен.', "And I've already forgiven you. You're fired.", [(361, 'Ты уволен')], "cue 360 ('А я тебе уже извинил', mistranscribed) -> 'А я тебя уже простил'; 'с обслуном' dropped"),
    ('samson', 'Филиппович! Ну как же так?', 'Filippovich! How can you?', [(362, 'Филиппович')], "'Ну как же так?' new"),
    ('boss', 'Ты назвал меня плохим словом. Меня, начальника!', 'You called me a bad word. Me, your boss!', [], 'new: a clean retelling of cues 364-366 (an operator calling his boss a crude name)'),
    ('samson', 'Ну что, забыли?', 'So, shall we forget it?', [(367, 'что, забыли')], "'Филипп' dropped"),
    ('boss', 'Как я могу это забыть? Ну, давай попробуем.', "How can I forget that? Well, let's try.", [(369, 'Как я могу это забыть'), (370, 'давай попробуем')], "'хотя' dropped; 'ты идиот' (368) left out"),
    ('samson', 'Давай. Забываем!', "Go on. We're forgetting!", [(371, 'Давай'), (372, 'забываем')], "'Поехали' dropped"),
    ('boss', 'Не получается у меня это забыть. Удачи тебе на новом месте работы.', "No, I just can't forget it. Good luck to you in your new job.", [(374, 'не получается у меня это забыть'), (376, 'удачи тебе'), (377, 'на новом месте работы')], "'Так что' dropped; cue 375 left out"),
    ('foreman', 'Филиппыч, миксер проехать не может. Радиаторы мешают.', "Filippych, the mixer truck can't get through. The radiators are in the way.", [(379, 'Филиппыч, миксер проехать не может'), (380, 'Радиаторы мешают')], ''),
    ('boss', 'Ну и в чём проблема? Возьмите их сами и перенесите.', "So what's the problem? Pick them up yourselves and move them.", [(381, 'Ну и в чем проблема'), (382, 'Возьмите их сами и')], "'перетащите' (drag over) -> 'перенесите'"),
    ('foreman', 'Нет никого. Всех забрала полиция.', "There's nobody. The police have taken everyone.", [(383, 'Нет никого'), (385, 'Полиция')], 'simplified from cues 384-386 (all the best men taken by the police for a document check)'),
    ('boss', 'Ну где я сейчас найду грузчиков?', 'Well, where am I going to find movers right now?', [(389, 'сейчас найду грузчиков')], "'тебе' dropped"),
    ('samson', 'Ну я. Ничего, я могу.', "Well, me. It's fine, I can do it.", [(390, 'Ну я'), (392, 'Ничего, я могу')], 'two cues joined'),
    ('boss', 'Самсонов, ты видел эти радиаторы?', 'Samsonov, have you seen those radiators?', [(393, 'Самсонов, ты видел эти радиаторы')], ''),
    ('samson', 'Да я три года грузчиком работал. Тут дел на пятнадцать минут.', "Oh, I worked as a mover for three years. This is fifteen minutes' work.", [(396, 'Да я три года грузчиком работал'), (397, 'минут')], "cue 397 'делов-то на 15' -> 'дел на пятнадцать'"),
]
WALK = [
    (0, 'Николай Филиппович, приветствую.', "'Nikolai Filippovich, greetings.' A first name and patronymic, the respectful way to address a boss, and a slightly formal hello. Then a careful question."),
    (0, 'Не помешал?', "'Am I interrupting?' Literally, 'did I not disturb you?' The action word is in the past, in its masculine form, because Samson is a man. The boss answers with the very same word."),
    (1, None, "'You are. Go away.' He just repeats the key word without the 'not', which is a very rude way of saying 'yes'. Samson tries again."),
    (2, 'Ну что ты, Филиппович.', "'Oh, come on, Filippovich.' Old colleagues sometimes call each other by the patronymic alone, which is friendly and familiar. Then his main argument."),
    (2, 'Я же извинился.', "'I said sorry, didn't I?' The word for 'to apologise' ends in a little '-sya' form, and the word before it adds 'but surely'. The boss has a surprise."),
    (3, 'А я тебя уже простил.', "'And I've already forgiven you.' Sounds good, so far."),
    (3, 'Ты уволен.', "'You're fired.' A short past form, the same kind of form as 'blocked' or 'detained'. Samson is shocked."),
    (4, None, "'Filippovich! How can you?' The last part is a common cry of protest, literally 'how so?'. The boss explains what still hurts."),
    (5, None, "'You called me a bad word. Me, your boss!' After the action word 'to call' something, the name you call someone goes into the 'with/as' form, so the words for 'bad word' change their endings. When Samson quit, he was very rude to him. Samson suggests a simple solution."),
    (6, None, "'So, shall we forget it?' The action word is in the past and the plural, as if it were already done: 'forgot it, right?' The boss isn't sure he can."),
    (7, 'Как я могу это забыть?', "'How can I forget that?' The action word 'can' is followed by a basic action word, just like in English."),
    (7, 'Ну, давай попробуем.', "'Well, let's try.' 'Let's' plus a action word in the 'we' form is the standard way to suggest doing something together. Samson cheers him on."),
    (8, None, "'Go on. We're forgetting!' It's like a countdown at the start of a race. But it doesn't work."),
    (9, 'Не получается у меня это забыть.', "'I just can't forget it.' Literally, 'it doesn't work out for me to forget it'. A very common way to say that you try but can't. And then a polite goodbye with a sting in it."),
    (9, 'Удачи тебе на новом месте работы.', "'Good luck to you in your new job.' Literally 'at the new place of work'. The word for luck is in the 'of' form, because it really means 'I wish you some luck'. At that moment a worker rushes in."),
    (10, None, "'Filippych, the mixer truck can't get through. The radiators are in the way.' At this point, Filippych is an even shorter, chummier form of the boss's patronymic. The mixer is the concrete lorry, and a stack of heavy radiators blocks its path. The boss sees no problem."),
    (11, None, "'So what's the problem? Pick them up yourselves and move them.' Both action words are commands in the polite or plural form, because he's talking to the whole crew. But there is no crew."),
    (12, None, "'There's nobody. The police have taken everyone.' After 'there is no', the word for 'nobody' is in the 'of' form. The police came to check the workers' documents and took them all away. The boss is stuck."),
    (13, None, "'Well, where am I going to find movers right now?' The action word is a one-time action word, so this present-looking form is really a future: 'will I find'. And Samson sees his chance."),
    (14, None, "'Well, me. It's fine, I can do it.' The word for 'nothing' here means 'no problem'. The boss can hardly believe it."),
    (15, None, "'Samsonov, have you seen those radiators?' Here, Samsonov is Samson's real surname; the boss uses it like a sergeant. Samson isn't worried at all."),
    (16, 'Да я три года грузчиком работал.', "'Oh, I worked as a mover for three years.' The job, 'mover', is in the 'with/as' form after 'worked': you work 'as' something. Then a promise."),
    (16, 'Тут дел на пятнадцать минут.', "'This is fifteen minutes' work.' Literally, 'here there's work for fifteen minutes'."),
]
