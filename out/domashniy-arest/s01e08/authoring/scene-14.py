# Authoring module for domashniy-arest-s01e08-scene-14.
ID = 'domashniy-arest-s01e08-scene-14'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 14
TITLE = 'Горе Самсонова  (Ivan Drinking)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'friend': 'Друг', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "Devastated by Osipenko's rumors that his grandfather was a wartime traitor, Ivan sits outside drinking with an acquaintance, pouring out his grief. Let's listen in Russian first."
OPENER = "Let's walk through the conversation step by step. Distraught Samsonov drowns his sorrows over his family honour."
TRANSITION = "Now let's listen to the entire scene once more in Russian."
OUTRO = "Samsonov's pride is shattered by the smear campaign, and he heads into the night on a heavy drinking spree. See you next time!"
CLOSING = ('samson', 'Пока!')
STORY = [
    ('samson', 'Ну как так можно, а?', 'How is that even possible, eh?', [(201, 'Ну, как так, а')], ''),
    ('samson', 'Для нас это святой праздник!', 'For us that is a sacred holiday!', [(203, 'главный праздник')], ''),
    ('samson', 'Я всегда смотрел фильмы про войну.', 'I always watched movies about the war.', [(204, 'все вот эти фильмы про войну')], ''),
    ('samson', 'Есть такая профессия — родину защищать!', 'There is such a profession — defending the motherland!', [(205, 'такая профессия, родину защищать')], ''),
    ('samson', 'Как теперь с этим жить, а?', 'How can one live with this now, eh?', [(206, 'Как мы теперь с этим жить, а')], ''),
    ('friend', 'Да, дела совсем плохие.', 'Yes, things are really bad.', [(207, 'Да, дела')], ''),
    ('friend', 'Где ты был так долго?', 'Where were you for so long?', [(212, 'Ты где был')], ''),
    ('samson', 'Извини, у меня тяжёлая депрессия.', 'Sorry, I have severe depression.', [(213, 'у меня депрессия')], ''),
    ('friend', 'Тогда сходи за новой бутылкой.', 'Then go get a new bottle.', [(214, 'за новый')], 'slang/ASR cleaned for A1'),
    ('samson', 'Ты меня посылаешь за водкой?', 'Are you sending me for vodka?', [(215, 'Ты мне сейчас водочную посылаешь')], ''),
    ('friend', 'Ты же сам всё выпил!', 'You drank it all yourself after all!', [(216, 'Ты все выжрал')], "crude verb cleaned to 'выпил'"),
    ('samson', 'Там на улице одни алкаши.', 'There are only drunks out on the street.', [(217, 'Так там алкаши одни')], ''),
    ('samson', 'Пойдём вместе, я хочу ещё выпить.', "Let's go together, I want to drink more.", [(218, 'Пошли вместе, я еще хочу')], "slang 'бухнуть' cleaned for A1"),
]
WALK = [
    (0, None, "'How is that even possible, eh?' Samsonov shakes his head in disbelief over the allegations."),
    (1, None, "'For us that is a sacred holiday!' Victory Day is sacred to Ivan's whole generation, which is why being called a traitor's grandson cuts him to the bone."),
    (2, None, "'I always watched movies about the war.' Samsonov recalls growing up on Soviet patriotic cinema."),
    (3, None, "'There is such a profession — defending the motherland!' Samsonov quotes the famous line from the classic Soviet movie 'Officers'."),
    (4, None, "'How can one live with this now, eh?' Literally, 'how now with this to live?' — Ivan feels he can never hold his head up in town again."),
    (5, None, "'Yes, things are really bad.' The companion sympathizes with Ivan's awful situation."),
    (6, None, "'Where were you for so long?' The companion asks where Ivan disappeared to."),
    (7, None, "'Sorry, I have severe depression.' Ivan explains his despair using a modern loanword."),
    (8, None, "'Then go get a new bottle.' His drinking buddy has a much simpler priority: somebody needs to go fetch another bottle."),
    (9, None, "'Are you sending me for vodka?' Ivan is offended that he is the one being sent on the liquor run."),
    (10, None, "'You drank it all yourself after all!' His friend points out the obvious: Ivan is the one who polished off the last bottle."),
    (11, None, "'There are only drunks out on the street.' Sitting on a bench with an empty bottle, Ivan ironically complains that the street is full of drunks."),
    (12, None, "'Let's go together, I want to drink more.' Ivan drags his companion along toward the nearest kiosk."),
]
