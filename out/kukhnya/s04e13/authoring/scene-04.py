# Authoring module for kukhnya-s04e13-scene-04.
ID = 'kukhnya-s04e13-scene-04'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 13
SCENE = 4
TITLE = 'Собеседование у Германа  (Job Interview with German)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'german': 'Герман', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.13'
SOURCE_FILE = 'sources/kukhnya/s04/e13.ru.srt'
INTRO = "Realizing he was too harsh, Chef Barinov calls Katya to apologize, but she quickly hangs up. She is already sitting inside Claude Monet interviewing with Barinov's rival, the new head chef German Land, who is intrigued to learn that she is Viktor Barinov's daughter."
OPENER = "Let's look closely at how German interviews Katya and why he decides to hire her."
TRANSITION = 'Now listen to the complete interview scene from beginning to end.'
OUTRO = "Delighted to hire Chef Barinov's own daughter after she admits they clashed in character, German leads her into the kitchen. Next, we watch the Claude Monet cooks react to Katya's return. See you next time!"
CLOSING = ('german', 'До встречи!')
STORY = [
    ('barinov', 'Алло, Катя, глупо у нас получилось.', 'Hello, Katya, things turned out foolishly between us.', [(34, 'Алло, Катя, как-то глупо')], 'adapted'),
    ('katya', 'Я не могу сейчас говорить, пока.', 'I cannot talk right now, bye.', [(35, 'Я не могу сейчас')], 'adapted'),
    ('katya', 'Извините, пожалуйста, продолжайте.', 'Excuse me, please, go ahead.', [(36, 'Извините.')], 'adapted'),
    ('german', 'Вы уже работали в нашем ресторане.', 'You already worked in our restaurant.', [(37, 'Тут указано, что вы')], 'adapted'),
    ('german', 'Причём это было совсем недавно.', 'Moreover, that was quite recently.', [(38, 'Причем не так давно.')], 'adapted'),
    ('katya', 'Да, всё верно, я работала здесь.', 'Yes, that is all true, I worked here.', [(39, 'Да, все верно. Я')], 'adapted'),
    ('katya', 'Я тогда работала у своего отца.', 'Back then I worked under my father.', [(39, 'Да, все верно. Я')], 'adapted'),
    ('katya', 'Он тогда был здесь шеф-поваром.', 'He was the head chef here back then.', [(40, 'Он тогда был шеф-поваром.')], 'adapted'),
    ('german', 'Потом вы уволились по собственному желанию.', 'Then you resigned of your own accord.', [(43, 'Вы проработали у него')], 'adapted'),
    ('german', 'Можно узнать причину этого желания?', 'May I find out the reason for this wish?', [(45, 'Можно узнать мотив этого')], 'adapted'),
    ('katya', 'Мы просто не сошлись характерами.', 'We simply did not get along in character.', [(46, 'Ну, если коротко, мы')], 'adapted'),
    ('german', 'Это неудивительно, пойдёмте со мной.', 'That is not surprising, come with me.', [(47, 'Неудивительно. Пойдемте со мной.')], 'adapted'),
]
WALK = [
    (0, None, '\'Hello, Katya, things turned out foolishly between us.\' Barinov picks this sharp element in earnest: "poluchilos" means "worked out" (from "poluchitsya"), giving the line its exact edge.'),
    (1, None, '\'I cannot talk right now, bye.\' Katya states this point facing German: the "-sya" ending on "seychas" ("now") turns the action inward or makes it happen between people naturally.'),
    (2, None, "'Excuse me, please, go ahead.' Katya continues lightly with Barinov, keeping the focus on what actually matters here."),
    (3, None, '\'You already worked in our restaurant.\' German underscores one sharp element in reply: "restorane" means "restaurant" (from "restoran"), giving the line its exact edge.'),
    (4, None, '\'Moreover, that was quite recently.\' German brings the comment beside Barinov: adding "sovsem" ("completely, at all") pushes the statement all the way, leaving zero room for doubt.'),
    (5, None, "'Yes, that is all true, I worked here.' Katya answers evenly in this moment, letting the remark speak for itself."),
    (6, None, '\'Back then I worked under my father.\' Katya focuses on this clear element at once: "rabotala" means "worked" (from "rabotat"), giving the line its exact edge.'),
    (7, None, "'He was the head chef here back then.' Katya weighs in pointedly with a shrug, so German knows she is not just making small talk."),
    (8, None, "'Then you resigned of your own accord.' German steps in pointedly toward Barinov, refusing to let the moment slip past."),
    (9, None, '\'May I find out the reason for this wish?\' German picks this direct piece at once: "zhelaniya" means "wish", and it carries the main weight of what German is saying.'),
    (10, None, '\'We simply did not get along in character.\' Katya states the comeback briskly now: the little word "prosto" ("simply, just") works like a shrug in the sentence, making a big claim sound effortless.'),
    (11, None, "'That is not surprising, come with me.' German responds wryly to be clear, grounding the moment in plain reality."),
]
