# Authoring module for kukhnya-s01e01-scene-04.
ID = 'kukhnya-s01e01-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'Утро после клуба  (The Morning After the Club)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = 'On the morning after a lively night at the club. Max is quietly trying to leave the apartment, but Vika wakes up and catches him at the door. As always, listen to the whole conversation in Russian first, and then we will break it down together in English.'
OPENER = "Let's go through their awkward morning exchange step by step. Max is eager to leave, but Vika has questions."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'That concludes our fourth scene. When you watch the first episode of Kukhnya, listen for Max trying to slip away and Vika asking if he is really running away. You will recognise these lines right away. See you next time!'
CLOSING = ('vika', 'До встречи!')
STORY = [
    ('max', 'Мне уже идти надо.', 'I need to go now.', [(24, 'мне идти надо')], ''),
    ('vika', 'Ты что, убегаешь?', 'What, are you running away?', [(25, 'Ты что'), (25, 'убегаешь')], ''),
    ('max', 'Почему убегаю? Нет, просто ухожу.', "Why running away? No, I'm just leaving.", [(26, 'Почему убегаю'), (26, 'Нет, просто ухожу')], ''),
    ('vika', 'Вот так? И всё?', "Just like that? And that's all?", [(27, 'Вот так вот'), (27, 'И все')], ''),
    ('vika', 'А то, что между нами было?', 'What about what was between us?', [(28, 'то, что между нами было')], ''),
    ('max', 'Спасибо. Прикольно было.', 'Thank you. It was fun.', [(29, 'Спасибо'), (29, 'прикольно было')], ''),
    ('vika', 'Прикольно, и всё?', "Fun, and that's it?", [(30, 'Прикольно и все')], ''),
    ('max', 'А что ещё?', 'What else?', [(31, 'А что ещё')], ''),
    ('vika', 'Да ладно тебе.', 'Oh, come on.', [(32, 'Да ладно')], ''),
    ('max', 'Нет, денег у меня нет.', 'No, I have no money.', [(33, 'Нет, денег у меня нет')], ''),
    ('max', 'Мы с тобой так не договаривались.', "You and I didn't agree to that.", [(34, 'мы с тобой так не договаривались')], ''),
    ('vika', 'Мне не нужны твои деньги.', "I don't need your money.", [], ''),
    ('max', 'Тогда я пошёл. У меня дела.', 'Then I am off. I have things to do.', [], ''),
    ('vika', 'Уходи. И не возвращайся сюда.', 'Leave. And do not come back here.', [], ''),
]
WALK = [
    (0, None, "'I need to go now.' Max attempts to slip out quietly in the morning, keeping his exit brief."),
    (1, None, "'What, are you running away?' Vika catches him at the door and confronts him about sneaking out."),
    (2, None, "'Why running away?' He plays dumb, pretending this is just a normal departure."),
    (3, None, "'No, I'm just leaving.' Max stammers out a weak denial to defend his hasty exit."),
    (4, None, "'Just like that? And that's all?' She is shocked by his casual attitude after their intimate night together."),
    (5, None, "'What about what was between us?' Vika demands to know if their connection meant anything to him."),
    (6, None, "'Thank you. It was fun.' He brushes it off as a casual hookup, completely misreading her emotional investment."),
    (7, None, "'Fun, and that's it?' She repeats his careless word, offended by his dismissive tone."),
    (8, None, "'What else?' Max coldly implies there was nothing more to their encounter."),
    (9, None, "'Oh, come on.' Vika scoffs at his callousness, unable to believe his behavior."),
    (10, None, "'No, I have no money.' He tries to excuse himself by claiming he cannot offer her financial compensation."),
    (11, None, "'You and I didn't agree to that.' Max points out that they made no promises to each other."),
    (12, None, "'I don't need your money.' She snaps back that she doesn't want a payout, deeply insulted by the suggestion."),
    (13, None, "'Then I am off.' He takes her rejection of money as an opportunity to finally leave."),
    (14, None, "'Leave. And do not come back here.' Vika kicks him out in anger, commanding him never to return."),
]
