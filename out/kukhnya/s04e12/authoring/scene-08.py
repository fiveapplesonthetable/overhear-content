# Authoring module for kukhnya-s04e12-scene-08.
ID = 'kukhnya-s04e12-scene-08'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 12
SCENE = 8
TITLE = 'Оценка камня  (Appraising the Stone)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'timur': 'Тимур'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.12'
SOURCE_FILE = 'sources/kukhnya/s04/e12.ru.srt'
INTRO = "Out in the courtyard, Chef Barinov intercepts Fedya carrying a crate of fish from Timur's van, while Senya slyly asks Timur how much his 'grandmother's gemstone' is worth."
OPENER = "Let's examine each line of the fish dispute and Timur's appraisal."
TRANSITION = "Now let's hear the whole courtyard scene again from start to finish."
OUTRO = "That wraps up this scene as outside by the delivery van, Barinov tries to buy Fedya's crate of fish before taking the rest of Timur's batch, and Senya tricks Timur into appraising the diamond for a hundred thousand rubles. See you next time!"
CLOSING = ('timur', 'Всего хорошего!')
STORY = [
    ('barinov', 'Так, стоять, ты куда несёшь?', 'All right, halt, where are you carrying that?', [(102, 'Так, так, стоять')], 'adapted for A1 clarity'),
    ('barinov', 'Федя, вообще-то это моя рыба!', 'Fedya, actually that is my fish!', [(105, 'Федя, это моя рыба')], 'adapted for A1 clarity'),
    ('fedya', 'Как это ваша, я её заказывал!', 'How is it yours when I ordered it!', [(106, 'как это ваша')], 'adapted for A1 clarity'),
    ('timur', 'Шеф, он до тебя заказ делал.', 'Chef, he placed his order before you.', [(109, 'Он до тебя заказ делал')], 'adapted for A1 clarity'),
    ('barinov', 'Федя, по старой дружбе продай рыбу!', "Fedya, for old friendship's sake, sell me the fish!", [(110, 'Федя, по старой дружбе продай мне эту рыбу')], 'adapted for A1 clarity'),
    ('fedya', 'Шеф, не обижайтесь, но не могу.', 'Chef, do not take offense, but I cannot.', [(111, 'Шеф, не обижайтесь, не могу')], 'adapted for A1 clarity'),
    ('timur', 'Шеф, тут много рыбы, всем хватит.', 'Chef, there is plenty of fish here, enough for everyone.', [(112, 'Шеф, тут много рыбы, всем хватит')], ''),
    ('barinov', 'А она точно из той же партии?', 'And is it definitely from the same batch?', [(114, 'Она из той же партии')], 'adapted for A1 clarity'),
    ('barinov', 'Ну да, конечно, забирай всю.', 'Well yes, of course, take it all.', [(115, 'Ну да')], 'adapted for A1 clarity'),
    ('fedya', 'Тимур, ты в драгоценных камнях разбираешься?', 'Timur, do you know about precious stones?', [(117, 'а ты в драгоценных камнях разбираешься')], 'adapted for A1 clarity'),
    ('timur', 'Конечно, я же на ювелира учился.', 'Of course, I studied to be a jeweler, after all.', [(118, 'на ювелире учился')], 'adapted for A1 clarity'),
    ('fedya', 'Мне камушек от бабушки в наследство достался.', 'I inherited a little stone from my grandmother.', [(120, 'Камушек в наследство достался')], 'adapted for A1 clarity'),
    ('timur', 'Слушай, продай мне, сто тысяч дам!', 'Listen, sell it to me, I will give you a hundred thousand!', [(122, 'Слушай, продай, а? Сто тысяч дам')], 'adapted for A1 clarity'),
    ('fedya', 'Значит, он все триста тысяч стоит!', 'That means it is worth a full three hundred thousand!', [(123, 'Значит, он')], 'adapted for A1 clarity'),
]
WALK = [
    (0, None, '\'All right, halt, where are you carrying that?\' Barinov drops the reaction for Fedya: putting the question word "kuda" right at the front of the line lets Fedya hear the point of the question on the very first beat.'),
    (1, None, "'Fedya, actually that is my fish!' Barinov pushes back honestly with Timur, steering the talk right where he wants it."),
    (2, None, '\'How is it yours when I ordered it!\' Fedya features one pointed piece in earnest: "zakazyval" means "ordered" (from "zakazyvat"), giving the line its exact edge.'),
    (3, None, '\'Chef, he placed his order before you.\' Timur points to one familiar detail in earnest: "zakaz" means "order", and it carries the main weight of what Timur is saying.'),
    (4, None, "'Fedya, for old friendship's sake, sell me the fish!' Barinov holds firm frankly beside Fedya, refusing to let the moment slip past."),
    (5, None, '\'Chef, do not take offense, but I cannot.\' Fedya underscores one vivid expression toward Timur: "obizhaytes" means "to take offence" (from "obizhatsya"), giving the line its exact edge.'),
    (6, None, "'Chef, there is plenty of fish here, enough for everyone.' Timur responds boldly with Barinov, saying out loud what both of them already know."),
    (7, None, "'And is it definitely from the same batch?' Barinov asks point-blank if there is more going on behind the scenes."),
    (8, None, '\'Well yes, of course, take it all.\' Barinov stresses one vivid touch with Fedya: "konechno" means "of course", and it carries the main weight of what Barinov is saying.'),
    (9, None, "'Timur, do you know about precious stones?' Fedya brings this answer to Timur: Russian keeps the exact word order of a normal statement here, turning it into a question for Timur purely through rising pitch at the end."),
    (10, None, "'Of course, I studied to be a jeweler, after all.' Timur weighs in evenly hearing Barinov, so Barinov knows he is not just making small talk."),
    (11, None, '\'I inherited a little stone from my grandmother.\' Fedya spotlights one sharp term in earnest: "kamushek" means "little", and it carries the main weight of what Fedya is saying.'),
    (12, None, "'Listen, sell it to me, I will give you a hundred thousand!' Timur chimes in quietly with Barinov, steering the talk right where he wants it."),
    (13, None, "'That means it is worth a full three hundred thousand!' Fedya fires back boldly in this moment, refusing to let the moment slip past."),
]
