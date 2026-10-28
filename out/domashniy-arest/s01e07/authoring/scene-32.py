# Authoring module for domashniy-arest-s01e07-scene-32.
ID = 'domashniy-arest-s01e07-scene-32'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 7
SCENE = 32
TITLE = 'Заметался пожар голубой  (A Blue Flame Flickered)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'ilona': 'Илона', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.07'
SOURCE_FILE = 'sources/domashniy-arest/s01/e07.ru.dual.srt'
INTRO = "Back in the communal flat after Eduard broke up with Marina, Arkady visits her room, secretly slips his healthy arms out of his plaster casts, and offers her his grandmother's vintage brooch. Let's listen to the scene in Russian first."
OPENER = "Let's walk through Arkady's romantic speech and how a single phone call ruins everything."
TRANSITION = "Let's hear the whole scene in Marina's room again from start to finish."
OUTRO = "Just when Arkady's poetry and family brooch had nearly won Marina's heart, Ilona's speakerphone call exposed his fake broken arms and got him chased into the corridor. See you next time!"
CLOSING = ('marina', 'Пока!')
STORY = [
    ('arkady', 'Здравствуйте ещё раз! Я хотел извиниться за сегодня.', 'Hello again! I wanted to apologize for today.', [(1220, 'Здравствуйте ещё раз. Я хотел извиниться за')], "'сегодняшнее' -> 'сегодня'"),
    ('arkady', 'Я во всём виноват.', 'Everything is my fault.', [(1220, 'Я во всём виноват')], ''),
    ('marina', 'Ну перестаньте, вы же не специально!', "Oh, stop it, you didn't do it on purpose!", [(1221, 'Ну перестаньте, вы же не специально')], ''),
    ('marina', 'Может, это и к лучшему. Всё давно разваливалось.', "Maybe it's for the best. Everything was falling apart for a long time.", [(1221, 'Может'), (1221, 'и к лучшему'), (1221, 'всё разваливалось')], "ASR 'Не везёт несмоченным' omitted"),
    ('arkady', 'Вы достойны самого лучшего! У меня кое-что есть для вас.', 'You deserve the very best! I have something for you.', [(1222, 'Вы достойны самого лучшего'), (1223, 'у меня кое-что есть для вас')], ''),
    ('arkady', 'Возьмите, пожалуйста! Эту брошь подарил мой дедушка моей бабушке.', 'Please take it! My grandfather gave this brooch to my grandmother.', [(1224, 'Возьмите, пожалуйста'), (1226, 'Эту брошь подарил мой дедушка моей бабушке')], ''),
    ('marina', 'Красивая очень! А вдруг вы ещё кого-нибудь встретите?', 'Very beautiful! What if you meet someone else?', [(1231, 'Красивая очень'), (1235, 'вдруг вы еще кого-нибудь встретите')], ''),
    ('arkady', 'Я уже встретил! Но она отвергает мои ухаживания.', 'I already have met her! But she rejects my advances.', [(1236, 'Я уже встретил'), (1237, 'отвергает мои ухаживания')], ''),
    ('arkady', 'Заметался пожар голубой! Первый раз я запел про любовь!', 'A blue flame flickered! For the first time I sang of love!', [(1238, 'Заметался пожар голубой'), (1240, 'Первый раз я запел про любовь')], ''),
    ('arkady', 'Марина, это телефон. Отключите его, пожалуйста!', "Marina, that's the phone. Please turn it off!", [(1249, 'телефон, Марина, отключите его, пожалуйста')], "'Черт' omitted"),
    ('marina', 'Ой, это Илона! Я громко поставлю.', "Oh, it's Ilona! I'll put it on speaker.", [(1250, 'Ой, это Илона'), (1252, 'Я громко поставлю')], ''),
    ('ilona', 'Аркадий Борисович, зачем вам этот ложный гипс на руках?', 'Arkady Borisovich, why do you need those fake casts on your arms?', [], 'speakerphone line heard in cue 1252-1253'),
    ('arkady', 'Илона, ты что такое несёшь? Марина, я всё объясню!', "Ilona, what nonsense are you saying? Marina, I'll explain everything!", [(1253, 'Илона, ты'), (1253, 'несешь такое'), (1254, 'Марина'), (1254, 'я все объясню')], ''),
    ('arkady', 'Марина, послушайте, это всё из-за любви!', "Marina, listen, it's all because of love!", [(1254, 'Марина, послушайте'), (1254, 'это все из-за любви')], ''),
    ('marina', 'Значит, вы симулянт? Вам сейчас больно?', "So, you're a faker? Does it hurt right now?", [(1256, 'Симулянт'), (1258, 'Вам больно')], ''),
    ('arkady', 'Нет, я не симулянт! Ай, мне очень больно, Марина!', "No, I'm not a faker! Ow, it hurts me so much, Marina!", [(1257, 'Нет, я не симулянт'), (1261, 'Мне очень больно'), (1261, 'Марина')], ''),
    ('ilona', 'Что, в третий раз с ногами не вышло?', "What, the shoe-kissing trick didn't work the third time?", [(1266, 'Что, в третий раз с')], "'с ножками не прокатило' -> 'с ногами не вышло'"),
]
WALK = [
    (0, None, "'Hello again! I wanted to apologize for today.' Arkady steps into Marina's room looking contrite after Eduard stormed out."),
    (1, None, "'Everything is my fault.' Notice the location phrase literally meaning 'guilty in everything'."),
    (2, None, "'Oh, stop it, you didn't do it on purpose!' Marina sighs and tells him not to blame himself."),
    (3, None, "'Maybe it's for the best. Everything was falling apart for a long time.' She admits her romance with Eduard was already crumbling."),
    (4, 'Вы достойны самого лучшего!', "'You deserve the very best!' The short-form adjective takes the 'of' form for what someone is worthy of."),
    (4, 'У меня кое-что есть для вас.', "'I have something for you.' Quietly slipping his right hand out of his cast behind his back, Arkady pulls out an antique brooch."),
    (5, None, "'Please take it! My grandfather gave this brooch to my grandmother.' Notice how the direct object comes first for emphasis."),
    (6, None, "'Very beautiful! What if you meet someone else?' Marina admires the family heirloom, hesitating to accept such a personal gift."),
    (7, None, "'I already have met her! But she rejects my advances.' Arkady looks straight into her eyes."),
    (8, None, "'A blue flame flickered! For the first time I sang of love!' Dropping both casts onto the table, Arkady recites Sergei Yesenin's famous love poem and leans in to kiss a moved Marina."),
    (9, None, "'Marina, that's the phone. Please turn it off!' Just as their lips are about to touch, Marina's mobile phone rings."),
    (10, None, "'Oh, it's Ilona! I'll put it on speaker.' Thinking Arkady's arms are in plaster casts, Marina taps speakerphone."),
    (11, None, "'Arkady Borisovich, why do you need those fake casts on your arms?' Ilona's voice rings out across the room."),
    (12, None, "'Ilona, what nonsense are you saying? Marina, I'll explain everything!' Arkady panics as Marina stares at his two healthy, unbandaged hands."),
    (13, None, "'Marina, listen, it's all because of love!' He pleads with her, swearing he only faked the broken arms to win her heart."),
    (14, None, "'So, you're a faker? Does it hurt right now?' Furious at how he tricked her all day, Marina grabs one of his heavy plaster casts and whacks him with it."),
    (15, None, "'No, I'm not a faker! Ow, it hurts me so much, Marina!' Even when he drops to his knees to kiss her shoes, she chases him out into the corridor."),
    (16, None, "'What, the shoe-kissing trick didn't work the third time?' Ilona asks dryly in the hallway, noting that two out of three is still a good score."),
]
