# Authoring module for kukhnya-s05e20-scene-06.
ID = 'kukhnya-s05e20-scene-06'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 20
SCENE = 6
TITLE = 'Слухи по всему отелю  (Rumors Across the Whole Hotel)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.20'
SOURCE_FILE = 'sources/kukhnya/s05/e20.ru.srt'
INTRO = "Chef Barinov's excuse about Eleonora being seriously ill quickly snowballs through the hotel staff into a rumor that Eleonora Andreyevna is dying. Mikhail Dzhekovich is horrified when he hears it."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Heartbroken by the rumor, Mikhail rushes toward Eleonora's office to find out if it is true. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('eleonora', 'Вы слышали, наша хозяйка совсем умирает.', 'Have you heard, our owner is dying.', [(88, 'Умирает она')], 'adapted'),
    ('mikhail', 'Ещё раз услышу, что ты распространяешь сплетни...', 'If I hear one more time that you are spreading gossip...', [(89, 'Еще раз я услышу, что ты распространяешь сплетни')], 'adapted'),
    ('mikhail', 'Я тебя в тот же день уволю!', 'I will fire you that very same day!', [(90, 'Уволю')], 'adapted'),
    ('eleonora', 'Честное слово, я сплетни не распространяю.', 'Honestly, I am not spreading gossip.', [(90, 'Я сплетни не распространяю')], 'adapted'),
    ('mikhail', 'Всё, иди спокойно работай и не плачь.', 'That is all, go work calmly and do not cry.', [(91, 'Все')], 'adapted'),
    ('barinov', 'Чего ты сегодня мрачный чернее тучи?', 'Why are you gloomier than a storm cloud today?', [(94, 'Чего это'), (94, 'черней черного')], 'adapted'),
    ('mikhail', 'Говорят, наша Элеонора Андреевна скоро умирает.', 'They say our Eleonora Andreyevna is dying soon.', [(95, 'Андреевна умирает')], 'adapted'),
    ('eleonora', 'А Михаил Джекович меня за это чуть не уволил.', 'And Mikhail Dzhekovich almost fired me for it.', [(96, 'А он уволил')], 'adapted'),
    ('mikhail', 'Подожди, что значит Элеонора умирает?', 'Wait, what do you mean Eleonora is dying?', [(97, 'Что значит умирает, а')], 'adapted'),
    ('barinov', 'Она очень сильно болеет, все уже знают.', 'She is very seriously ill, everyone already knows.', [(98, 'Она сильно болеет, все знают')], 'adapted'),
    ('mikhail', 'Откуда вы вообще всё это взяли?', 'Where on earth did you get all of this?', [(97, 'Что значит умирает')], 'adapted'),
    ('eleonora', 'Нам утром сам Виктор Петрович рассказал.', 'Viktor Petrovich himself told us this morning.', [(98, 'все знают')], 'adapted'),
]
WALK = [
    (0, None, "'Have you heard, our owner is dying.' Eleonora weighs in earnestly around Mikhail, keeping the focus on what actually matters here."),
    (1, None, '\'If I hear one more time that you are spreading gossip...\' Pointing to the gossip right here, Mikhail chooses "rasprostranyayesh" ("you spread", from the root "rasprostranyat") so Eleonora hears the exact meaning.'),
    (2, None, "'I will fire you that very same day!' Mikhail replies pointedly with a sigh, refusing to let the moment slip past."),
    (3, None, "'Honestly, I am not spreading gossip.' Eleonora weighs in frankly without holding back, to clear the air between them once and for all."),
    (4, None, '\'That is all, go work calmly and do not cry.\' Mikhail chimes in vividly to Eleonora and centers the remark on "spokoyno" ("calmly") without any extra fuss.'),
    (5, None, '\'Why are you gloomier than a storm cloud today?\' Making clear how gloomy things are in this beat, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (6, None, "'They say our Eleonora Andreyevna is dying soon.' Mikhail cuts in quietly facing Eleonora, grounding the moment in plain reality."),
    (7, None, '\'And Mikhail Dzhekovich almost fired me for it.\' Eleonora steps in evenly on the spot and chooses "uvolil" ("to fire, to dismiss", from the root "uvolit") so Mikhail hears the exact meaning.'),
    (8, None, '\'Wait, what do you mean Eleonora is dying?\' Turning promptly right here, Mikhail puts the question word "chto" right at the start so Eleonora hears the focus immediately.'),
    (9, None, "'She is very seriously ill, everyone already knows.' Barinov opens up openly toward Mikhail, before Mikhail can change the subject."),
    (10, None, '\'Where on earth did you get all of this?\' Mikhail replies directly with Eleonora and reaches for the Russian word "voobshche" ("at all") right at the heart of the line.'),
    (11, None, '\'Viktor Petrovich himself told us this morning.\' Eleonora jumps in firmly in this beat and leans on "utrom" ("this morning") to give the whole sentence its punch.'),
]
