# Authoring module for domashniy-arest-s01e06-scene-09.
ID = 'domashniy-arest-s01e06-scene-09'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 6
SCENE = 9
TITLE = "А что если он не совсем ребёнок?  (What If He's Not Quite a Child?)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'anna': 'Анна', 'chief': 'Михаил Михайлович', 'lavrov': 'Лавров'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.06'
SOURCE_FILE = 'sources/domashniy-arest/s01/e06.ru.dual.srt'
INTRO = "Last time, Edik convinced Marina that he had told his wife about their affair and asked her to bake a condensed milk cake for their date tonight. Meanwhile, at the Sineozersk security service office, Major Lavrov, Colonel Mikhail Mikhailovich, and analyst Anna are looking for a way to ruin Samsonov's reputation. Let's listen in Russian first."
OPENER = "Let's walk through it. Analyst Anna has checked every file on Ivan Samsonov and found nothing shady at all."
TRANSITION = "Let's hear the whole brainstorming session at the security service office again."
OUTRO = 'So Colonel Mikhail Mikhailovich forbids Lavrov to touch his nephew Lyova — which means Lavrov will simply wait until the Colonel leaves the office to talk Lyova into the stunt himself. See you next time!'
CLOSING = ('lavrov', 'Пока!')
STORY = [
    ('anna', 'Да нет на него никакого компромата. Обычный мужик.', 'There is no compromising material on him at all. Just an ordinary guy.', [(315, 'Да нет на него никакого компромата, обычный мужик')], ''),
    ('lavrov', 'Может, какие-то тайные страсти?', 'Maybe some secret passions?', [(316, 'Может, какие-то тайные страсти')], ''),
    ('anna', 'Рыбалка, машины, футбол.', 'Fishing, cars, football.', [(318, 'Рыбалка, машины, футбол')], ''),
    ('lavrov', 'Придётся придумывать. Может, скажем, что он обманщик и пьяница?', "We'll have to make something up. Maybe we'll say he is a cheat and a drunkard?", [(320, 'Придется придумывать')], "cues 321-322 slurs replaced cleanly with 'обманщик и пьяница'"),
    ('chief', 'Не сработает, но мужику жизнь испортим!', "It won't work, and we'll ruin the man's life!", [(325, 'Не сработает, но мужику жизнь испортим')], ''),
    ('lavrov', 'Что за сантименты?', "What's with the sentimentality?", [(326, 'Что за сантименты')], ''),
    ('chief', 'Он мне симпатичен, нормальный мужик. Ладно, тогда давайте сами.', "I like him, he's a decent guy. Fine, then come up with something yourselves.", [(327, 'Он мне симпатичен. Нормальный мужик'), (331, 'Ладно, тогда давайте сами')], 'cues 328-330 omitted'),
    ('anna', 'Я не знаю, может, он обидел инвалида?', "I don't know, maybe he offended a disabled person?", [(333, 'Я не знаю'), (333, 'инвалида')], "cue 333 'избил там' softened to 'может, он обидел'"),
    ('lavrov', 'Меня всё ребёнок не отпускает. Вот если бы он ребёнка ударил!', "I can't stop thinking about a child. Now if he had hit a child!", [(334, 'Меня все ребенок не отпускает'), (335, 'Вот если бы он ребенка ударил')], ''),
    ('chief', 'Ну каким образом? Лёва, я никакие документы не запрашивал!', "Well, how? Lyova, I didn't request any documents!", [(336, 'Ну, каким образом'), (340, 'Лева, я никакие документы не запрашивал')], "Lyova's entry in cue 338 narrated in WALK"),
    ('chief', 'А ну, живо в архив!', 'Come on, back to the archive at once!', [(341, 'А ну, живо в архив')], ''),
    ('lavrov', 'А что если он не совсем ребёнок?', 'And what if he is not quite a child?', [(346, 'А что если он не совсем ребенок')], ''),
    ('chief', 'Лёва, иди в архив! И сиди там!', 'Lyova, go to the archive! And stay there!', [(351, 'Лева, иди в архив'), (352, 'И сиди там')], "Lyova's panicked refusal in 348-349 narrated in WALK"),
    ('chief', 'И не надо больше никаких документов сюда приносить!', "And don't bring any more documents in here!", [(353, 'И не надо больше никаких документов сюда приносить')], ''),
    ('chief', 'Нет! Даже думать забудьте! Убью!', "No! Forget even thinking about it! I'll kill you!", [(354, 'Нет'), (355, 'Даже думать забудьте'), (356, 'Убью')], ''),
]
WALK = [
    (0, None, "'There is no compromising material on him at all. Just an ordinary guy.' Major Lavrov hopes there is a hidden weakness."),
    (1, None, "'Maybe some secret passions?' Meanwhile, Anna reads out Samsonov's entire list of interests."),
    (2, None, "'Fishing, cars, football.' Captain Ovechkin mutters that Samsonov sounds just like him, so Lavrov decides they will have to invent a scandal."),
    (3, None, "'We'll have to make something up. Maybe we'll say he is a cheat and a drunkard?' Colonel Mikhail Mikhailovich shakes his head."),
    (4, None, "'It won't work, and we'll ruin the man's life!' Meanwhile, Lavrov is surprised by the Colonel's sympathy."),
    (5, None, "'What's with the sentimentality?' The Colonel admits he actually likes Samsonov."),
    (6, None, "'I like him, he's a decent guy. Fine, then come up with something yourselves.' At this point, Anna suggests a milder rumour."),
    (7, None, "'I don't know, maybe he offended a disabled person?' Meanwhile, Lavrov, however, is still fixated on involving a child."),
    (8, None, "'I can't stop thinking about a child. Now if he had hit a child!' Notice the conditional particle with the past tense: 'if he had hit'. Just as the Colonel asks how that could ever happen, his short, baby-faced nephew Lieutenant Lyova Sokolov walks in carrying archive folders."),
    (9, None, "'Well, how? Lyova, I didn't request any documents!' At this point, Lyova only brought the folders as an excuse to peek into the meeting."),
    (10, None, "'Come on, back to the archive at once!' But Major Lavrov is staring intently at tiny Lyova from head to toe."),
    (11, None, "'And what if he is not quite a child?' Realising Lavrov wants to dress him up as a schoolboy and have Samsonov hit him on camera, Lyova panics and shouts that he doesn't agree. Uncle Mikhail immediately shields his nephew."),
    (12, None, "'Lyova, go to the archive! And stay there!' He shoos Lyova out of the office."),
    (13, None, "'And don't bring any more documents in here!' Once the door closes, the Colonel turns back to Lavrov and Ovechkin."),
    (14, None, "'No! Forget even thinking about it! I'll kill you!' He refuses to let Moscow agents use his nephew as bait."),
]
