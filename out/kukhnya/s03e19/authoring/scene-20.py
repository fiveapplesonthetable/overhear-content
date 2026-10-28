# Authoring module for kukhnya-s03e19-scene-20.
ID = 'kukhnya-s03e19-scene-20'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 19
SCENE = 20
TITLE = 'Раскрытая тайна поцелуя  (The Kiss Secret Exposed)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.19'
SOURCE_FILE = 'sources/kukhnya/s03/e19.ru.srt'
INTRO = 'When Max chases after Katya to stop her from quitting, Chef Barinov explodes and yells that he saw Max and Katya kissing in the kitchen three days ago—with Vika standing right behind them!'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that heartbreaking revelation closes Episode Nineteen: Vika learns about Max's kiss with Katya right after choosing to trust him. See you in the Season Three finale! See you next time!"
CLOSING = ('vika', 'До свидания!')
STORY = [
    ('max', 'Катя, подожди, пожалуйста, стой на месте!', 'Katya, wait, please, stop right there!', [(355, 'Катя, стой')], 'adapted'),
    ('barinov', 'Ну что, Максим, ты теперь наконец доволен?', 'Well, Maxim, are you finally satisfied now?', [(356, 'Ты что, доволен')], 'adapted'),
    ('barinov', 'Ты зачем довёл мою родную девчонку до слёз?', 'Why did you drive my own girl to tears?', [(357, 'Довел девчонку')], 'adapted'),
    ('barinov', 'Поиграл с ней, пока Вики не было, и бросил?', 'You played with her while Vika was away, and dumped her?', [(358, 'пока Вики не было, и все')], 'adapted'),
    ('max', 'Шеф, что за странные намёки? Ничего не было!', 'Chef, what are these strange hints? Nothing happened!', [(359, 'Что за намеки')], 'adapted'),
    ('barinov', 'Ты, Лавров, хотя бы мне-то в глаза не ври!', 'Lavrov, at least do not lie to my face!', [(360, 'хоть мне-то не ври')], 'adapted'),
    ('barinov', 'Я своими глазами видел, как три дня назад вы на кухне целовались!', 'I saw with my own eyes how the two of you were kissing in the kitchen three days ago!', [(361, 'Я своими глазами ее видел, как три дня назад вы с ней на кухне целовались')], 'adapted'),
    ('barinov', 'Ты вообще о ком-нибудь кроме себя думаешь или нет?', 'Do you ever think about anyone besides yourself or not?', [(362, 'Ты вообще о ком-нибудь кроме себя думаешь, нет')], 'adapted'),
    ('max', 'Вика, подожди, я тебе сейчас всё честно объясню!', 'Vika, wait, I will honestly explain everything to you right now!', [(363, 'Вик, я все объясню')], 'adapted'),
    ('vika', 'Зачем объяснять? Я ведь только на секунду поверила тебе.', 'Why explain? I had only believed you for a second.', [(363, 'Зачем'), (364, 'только на секундочку поверил тебе')], 'adapted'),
    ('vika', 'Так что ничего страшного, я ещё не привыкла.', 'So it is no big deal, I had not gotten used to it yet.', [(365, 'Так что не страшно. Я еще не привыкла')], 'adapted'),
    ('vika', 'И мне сейчас совсем не больно, не очень больно.', 'And it does not hurt me at all right now, not very much.', [(366, 'И мне не больно'), (367, 'Не очень больно')], 'adapted'),
]
WALK = [
    (0, None, '\'Katya, wait, please, stop right there!\' Max brings a brisk course in the room, pairing "podozhdi" ("wait") with "stoy" ("stop, wait") to get the point across in plain spoken Russian.'),
    (1, None, '\'Well, Maxim, are you finally satisfied now?\' Barinov checks sharply in front of Vika, leaning on "teper" ("now") before closing the thought with "nakonets" ("at last, finally").'),
    (2, None, '\'Why did you drive my own girl to tears?\' Barinov inquires calmly in front of Max, putting "zachem" ("what for") alongside "dovyol" ("drove, pushed") in a tight, everyday turn of phrase.'),
    (3, None, '\'You played with her while Vika was away, and dumped her?\' Barinov probes directly in the scene, anchoring the Russian line on "poigral" ("to play for a while") and "poka" ("bye") without extra filler.'),
    (4, None, '\'Chef, what are these strange hints? Nothing happened!\' Max asks directly on the spot, joining "strannyye" ("strange") to "namyoki" ("hints, insinuations") so every word pulls its weight.'),
    (5, None, '\'Lavrov, at least do not lie to my face!\' Barinov holds an honest stance for Vika, using "glaza" (from "glaz", "eyes") alongside "vri" ("to lie, to tell lies") to shape the meaning.'),
    (6, None, '\'I saw with my own eyes how the two of you were kissing in the kitchen three days ago!\' Barinov offers a playful attitude in their talk, leaning on "glazami" ("eyes") before closing the thought with "videl" ("saw, have seen").'),
    (7, None, '\'Do you ever think about anyone besides yourself or not?\' Barinov tests evenly in their exchange, putting "voobshche" ("at all") alongside "dumayesh" ("think") in a tight, everyday turn of phrase.'),
    (8, None, '\'Vika, wait, I will honestly explain everything to you right now!\' Max projects a lively course in the scene, using "podozhdi" (from "podozhdat", "wait") alongside "seychas" ("now") to shape the meaning.'),
    (9, None, '\'Why explain? I had only believed you for a second.\' Vika queries calmly beside Max, putting "zachem" ("what for") alongside "obyasnyat" ("to explain") in a tight, everyday turn of phrase.'),
    (10, None, '\'So it is no big deal, I had not gotten used to it yet.\' Vika maintains a firm manner for Barinov, pairing "strashnogo" ("terrible, serious") with "yeshchyo" ("more, still") to get the point across in plain spoken Russian.'),
    (11, None, '\'And it does not hurt me at all right now, not very much.\' Vika favors a clear rhythm in the scene, linking "seychas" ("now"), "sovsem" ("at all"), and "bolno" ("it hurts") in one brisk exchange.'),
]
