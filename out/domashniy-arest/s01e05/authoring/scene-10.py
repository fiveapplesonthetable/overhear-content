# Authoring module for domashniy-arest-s01e05-scene-10.
ID = 'domashniy-arest-s01e05-scene-10'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 5
SCENE = 10
TITLE = 'Беги в деревню  (Run to the Village)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'dean': 'Эдуард Владимирович', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.05'
SOURCE_FILE = 'sources/domashniy-arest/s01/e05.ru.dual.srt'
INTRO = "Now, at the university, Marina tells her lover, Dean Eduard Vladimirovich, how the debt collectors terrified her son Lyosha and asks him to help pay off the loan. Let's listen in Russian first."
OPENER = "Let's walk through it. Shaken by the debt collectors' visit, Marina comes to Dean Eduard Vladimirovich's office hoping he will rescue her."
TRANSITION = "Now let's hear the whole conversation again from the beginning."
OUTRO = "So rather than pay off Marina's loan, the cowardly dean lectures her about reading the fine print and tells her to hide in her mother's village for six months — pushing Marina straight toward Major Lavrov. See you next time!"
CLOSING = ('dean', 'Пока!')
STORY = [
    ('dean', 'Бедная моя! Ничего, мы всё решим.', "My poor thing! It's okay, we'll sort it all out.", [(363, 'Бедная моя'), (367, 'Ничего, мы все решим')], "cues 360-362 toilet-door tail skipped; 'подонков' in 364 omitted"),
    ('marina', 'Да что я, вот Лёшка испугался.', "Never mind me, it's Lyoshka who got scared.", [(365, 'Да что я, вот Лешка испугался')], ''),
    ('dean', 'Теперь давай всё по порядку. Скажи мне, сколько ты им должна?', "Now let's go through everything in order. Tell me, how much do you owe them?", [(369, 'Теперь давай все по порядку'), (370, 'Скажи мне, сколько ты им должна')], ''),
    ('marina', 'Сто пятьдесят тысяч. Я брала двадцать.', 'A hundred and fifty thousand. I borrowed twenty.', [(371, '150'), (373, 'я брала 20')], "digits '150' and '20' written out as words; 'тысяч' added for clarity"),
    ('marina', 'А они накрутили со своими бандитскими процентами.', 'And they piled it on with their gangster interest rates.', [(374, 'они накрутили'), (374, 'со своими бандитскими процентами')], "'в итоге ... как-то' trimmed"),
    ('marina', 'Сказали, что надо читать мелкий шрифт.', 'They said that you have to read the fine print.', [(376, 'Сказали, что надо читать'), (376, 'мелкий шрифт')], "'какой-то' trimmed"),
    ('dean', 'Мариночка, конечно, они правы. Мелкий шрифт тоже надо читать.', "Marinochka, of course they're right. You have to read the fine print too.", [(377, 'Мариночка, конечно, они правы. Мелкий шрифт тоже надо читать')], ''),
    ('marina', 'Ты мне поможешь?', 'Will you help me?', [(378, 'Ты мне поможешь')], ''),
    ('dean', 'Ну конечно! Я думаю, как. Все мои доходы забрала Алла Евгеньевна.', "Well, of course! I'm thinking how. Alla Yevgenyevna has taken over all my income.", [(379, 'Ну конечно. Я думаю, как'), (380, 'все мои доходы'), (380, 'Алла Евгеньевна')], "'узурпировала' -> 'забрала'"),
    ('dean', 'Я снимаю деньги с карточки. И Алла Евгеньевна сразу получает смс.', 'I withdraw money from my card. And Alla Yevgenyevna immediately gets a text message.', [(380, 'Алла Евгеньевна'), (381, 'я снимаю деньги с карточки'), (381, 'получает смс')], "'Когда ... она получает смс-ку' split into two short sentences"),
    ('marina', 'Но ты же ректор! У тебя есть какие-то возможности.', "But you're the rector! You have some possibilities.", [(382, 'Но ты же ректор. У тебя есть'), (382, 'какие-то возможности')], ''),
    ('dean', 'Да какие возможности? У меня университет!', 'What possibilities? I run a university!', [(383, 'Да какие возможности? У меня университет')], 'Chechen students joke in 384-385 omitted'),
    ('marina', 'Хорошо. Что мне делать?', 'Fine. What should I do?', [(386, 'Хорошо. Что мне делать')], ''),
    ('dean', 'Надо бежать! Беги в деревню к маме.', "You need to run! Run to the village to your mum's.", [(387, 'Надо бежать'), (388, 'Беги в'), (388, 'к маме'), (389, 'деревню')], "'в шпаковку' -> 'в деревню'"),
    ('dean', 'Уезжай с Алёшей на шесть месяцев. И все всё забудут!', 'Go away with Alyosha for six months. And everyone will forget everything!', [(389, 'Алешу'), (389, 'на шесть'), (389, 'месяцев'), (390, 'И все все забудут')], "'Берешь Алешу, уезжаешь в эту деревню на шесть-семь месяцев' tightened"),
    ('marina', 'Я думаю, что у меня есть мужчина. Он сможет меня защитить.', 'I think that I have a man. He will be able to protect me.', [(391, 'Я думаю, что у меня есть мужчина'), (391, 'сможет меня защитить')], 'split into two short sentences; condom callback in 393 omitted'),
    ('dean', 'Марина, я делаю всё возможное! Послушай, ты несправедлива!', "Marina, I'm doing everything possible! Listen, you're being unfair!", [(392, 'Марина, я делаю все возможное'), (396, 'Послушай, ты несправедлива')], ''),
]
WALK = [
    (0, None, "'My poor thing! It's okay, we'll sort it all out.' At first the dean sounds warm and reassuring. Marina says she wasn't only worried about herself."),
    (1, None, "'Never mind me, it's Lyoshka who got scared.' Literally 'what am I — here Lyoshka got scared'. The dean asks for the details."),
    (2, 'Теперь давай всё по порядку.', "'Now let's go through everything in order.' Literally 'now let's everything by order'."),
    (2, 'Скажи мне, сколько ты им должна?', "'Tell me, how much do you owe them?' Here, Marina gives him the number."),
    (3, 'Сто пятьдесят тысяч.', "'A hundred and fifty thousand.' Marina names the terrifying sum the collectors are demanding now: a hundred and fifty thousand roubles."),
    (3, 'Я брала двадцать.', "'I borrowed twenty.' She used the ongoing-action form of 'to take': 'I took twenty'. She explains how twenty turned into a hundred and fifty."),
    (4, None, "'And they piled it on with their gangster interest rates.' The verb literally means 'wound up, cranked up'. And the collectors blamed her for not reading the contract carefully."),
    (5, None, "'They said that you have to read the fine print.' Literally 'small font'. Instead of taking her side, the dean nods sagely."),
    (6, 'Мариночка, конечно, они правы.', "'Marinochka, of course they're right.' Using a syrupy pet name, the dean sighs that legally the collectors are in the right."),
    (6, 'Мелкий шрифт тоже надо читать.', "'You have to read the fine print too.' Here, Marina cuts straight to the point."),
    (7, None, "'Will you help me?' Notice the future tense of 'help' takes the 'to/for' form: 'to me'. The dean immediately starts making excuses."),
    (8, 'Ну конечно! Я думаю, как.', "'Well, of course! I'm thinking how.' Put on the spot, Eduard claims he is of course already thinking about how to help."),
    (8, 'Все мои доходы забрала Алла Евгеньевна.', "'Alla Yevgenyevna has taken over all my income.' His domineering wife controls every rouble he earns."),
    (9, 'Я снимаю деньги с карточки.', "'I withdraw money from my card.' Literally 'I take off money from the card'."),
    (9, 'И Алла Евгеньевна сразу получает смс.', "'And Alla Yevgenyevna immediately gets a text message.' Meanwhile, Marina isn't buying it."),
    (10, 'Но ты же ректор!', "'But you're the rector!' That particle adds 'after all'."),
    (10, 'У тебя есть какие-то возможности.', "'You have some possibilities.' He spreads his hands helplessly."),
    (11, None, "'What possibilities? I run a university!' Literally 'I have a university!'. Seeing he won't give her a single rouble, Marina asks what his brilliant plan is."),
    (12, None, "'Fine. What should I do?' Literally 'what to me to do?'. The dean brightens up with a solution that costs him nothing."),
    (13, 'Надо бежать!', "'You need to run!' He says it with complete seriousness."),
    (13, 'Беги в деревню к маме.', "'Run to the village to your mum's.' Notice 'into the village' uses the object-form, and 'to mum' uses the preposition 'toward' plus 'to'-form."),
    (14, 'Уезжай с Алёшей на шесть месяцев.', "'Go away with Alyosha for six months.' His grand solution is for Marina to pack up and leave town with little Lyosha for half a year."),
    (14, 'И все всё забудут!', "'And everyone will forget everything!' Notice those two almost identical words side by side: 'everyone' with an 'e' and 'everything' with 'yo'. Marina thinks of Major Lavrov's business card."),
    (15, 'Я думаю, что у меня есть мужчина.', "'I think that I have a man.' Marina puts 'think' up front and finishes with 'man' to make the point unmistakable."),
    (15, 'Он сможет меня защитить.', "'He will be able to protect me.' As she walks out, the dean calls after her indignantly."),
    (16, 'Марина, я делаю всё возможное!', "'Marina, I'm doing everything possible!' As Marina storms out, the dean calls after her that he is doing everything he possibly can."),
    (16, 'Послушай, ты несправедлива!', "'Listen, you're being unfair!' Eduard uses the command form command form of the verb meaning 'listen'."),
]
