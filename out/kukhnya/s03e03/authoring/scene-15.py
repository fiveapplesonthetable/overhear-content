# Authoring module for kukhnya-s03e03-scene-15.
ID = 'kukhnya-s03e03-scene-15'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 3
SCENE = 15
TITLE = 'Две новости  (Two Pieces of News)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.03'
SOURCE_FILE = 'sources/kukhnya/s03/e03.ru.srt'
INTRO = 'Katya marches into the kitchen to announce that Barinov is her father, but when Barinov glares at her, she stops mid-sentence—convincing all the cooks that she is actually his secret mistress.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes Scene Fifteen. Listen for the irony of Fedya saying 'Definitely her lover—well, he's not her father!'. Until next time!"
CLOSING = ('fedya', 'До завтра!')
STORY = [
    ('katya', 'Внимание всем! У меня для вас две новости.', 'Attention everyone! I have two pieces of news for you.', [(255, 'Внимание'), (255, 'у меня для вас две новости')], 'adapted'),
    ('katya', 'Первая новость — я не лесбиянка.', 'The first piece of news is I am not a lesbian.', [(256, 'Первая новость, я не лесбиянка')], ''),
    ('katya', 'А вторая новость — Виктор Петрович мой...', 'And the second piece of news is Viktor Petrovich is my...', [(257, 'А вторая новость, Виктор Петрович, мой')], ''),
    ('barinov', 'Твой кто?', 'Your who?', [(258, 'Мой')], 'adapted'),
    ('fedya', 'Он её любовник!', 'He is her lover!', [(259, 'Он ее любовник')], ''),
    ('fedya', 'Точно любовник! Ну не отец же.', "Definitely her lover! Well, he's not her father.", [(260, 'любовник. Ну не отец же')], 'adapted'),
    ('fedya', 'Вот почему он так бесился, когда мы все вокруг неё бегали.', 'That is why he was so furious when we were all running around her.', [(261, 'Вот почему он так бесился, когда мы все вокруг неё бегали')], ''),
    ('fedya', 'Зачем тогда она меня поцеловала?', 'Why did she kiss me then?', [(262, 'Зачем тогда она меня поцеловала')], ''),
    ('fedya', 'Для конспирации!', 'For cover!', [(263, 'Для конспирации')], ''),
    ('fedya', 'А я сразу прямо догадался.', 'And I figured it out right away.', [(264, 'А я сразу'), (264, 'догадался')], 'adapted'),
    ('fedya', 'Вот прямо сразу!', 'Right away!', [(265, 'Вот прямо сразу')], ''),
    ('fedya', 'Они прямо сейчас там разговаривают.', 'They are in there talking right now.', [(267, 'прямо сейчас там')], 'adapted'),
]
WALK = [
    (0, None, "'Attention everyone! I have two pieces of news for you.' Katya proceeds at once watching Barinov, steering the talk right where she wants it."),
    (1, None, '\'The first piece of news is I am not a lesbian.\' Talking about a lesbian in front of Barinov, Katya reaches for the Russian word "lesbiyanka" ("lesbian") right at the heart of the line.'),
    (2, None, '\'And the second piece of news is Viktor Petrovich is my...\' Showing how second things are at once, Katya links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (3, None, "'Your who?' Barinov prompts openly to see how Fedya will answer on the spot."),
    (4, None, '\'He is her lover!\' Focusing on the lover on the spot, Fedya puts the emphasis on "lyubovnik" ("lover") in the middle of the talk.'),
    (5, None, '\'Definitely her lover! Well, he\'s not her father.\' Turning to the lover around Barinov, Fedya chooses "lyubovnik" ("lover") so Barinov gets the point right away.'),
    (6, None, "'That is why he was so furious when we were all running around her.' Fedya reacts calmly with a nod, to clear the air between them once and for all."),
    (7, None, '\'Why did she kiss me then?\' Fedya continues dryly in front of Barinov and lands on "potselovala" ("kissed", built on "potselovat") to keep the statement grounded.'),
    (8, None, "'For cover!' Turning to the secrecy to Barinov, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
    (9, None, "'And I figured it out right away.' Fedya speaks up promptly with a sigh, bringing things back to earth after the buildup."),
    (10, None, '\'Right away!\' Fedya responds candidly right here and puts the emphasis on "pryamo" ("right, just") in the middle of the talk.'),
    (11, None, '\'They are in there talking right now.\' Fedya counters plainly with Barinov and centers the thought on "razgovarivayut" ("to talk, to speak", from "razgovarivat") without wasting a word.'),
]
