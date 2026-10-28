# Authoring module for domashniy-arest-s01e08-scene-45.
ID = 'domashniy-arest-s01e08-scene-45'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 45
TITLE = 'Интересный персонаж  (An Interesting Character)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'lavrov': 'Лавров', 'pasha': 'Паша', 'zavarzin': 'Заварзин'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "Inside their surveillance van, Major Lavrov orders acting mayor Pasha Osipenko to focus on campaign funding, while Captain Zavarzin wonders how they can still pressure Arkady now that Marina is completely out of their reach. Let's hear the conversation in Russian first."
OPENER = "Let's walk through how Major Lavrov finds a new leverage point against Arkady."
TRANSITION = "Now let's listen to the surveillance van strategy session again from start to finish."
OUTRO = 'Having lost direct leverage over Marina, Major Lavrov targets her former lover Eduard Valentinovich and his embezzlement of university funds. See you next time!'
CLOSING = ('lavrov', 'Пока!')
STORY = [
    ('lavrov', 'Займитесь деньгами, мэр!', 'Handle the money, Mayor!', [(1046, 'Займитесь деньгами, мэр')], ''),
    ('pasha', 'Есть, товарищ майор!', 'Yes, sir, Comrade Major!', [(1047, 'Есть')], "'товарищ майор' added"),
    ('zavarzin', 'Ну и что мы теперь делать будем?', 'So what are we going to do now?', [(1053, 'Ну что делать будете')], "'мы теперь' added"),
    ('lavrov', 'Пока точно не знаю.', "I don't know for sure yet.", [(1054, 'Не знаю пока')], "'точно' added"),
    ('lavrov', 'Аникеев сильно любит эту женщину.', 'Anikeyev loves this woman deeply.', [(1055, 'Он любит эту')], "'чокнутую' -> 'женщину'"),
    ('zavarzin', 'Но на неё у нас влияния нет.', 'But we have no influence over her.', [(1056, 'Но на нее у нас влияния'), (1056, 'нет')], "'больше' omitted"),
    ('lavrov', 'У кого нет, а у кого есть!', "Some don't, but some do!", [(1057, 'У кого нет, а у кого есть')], ''),
    ('zavarzin', 'Вы кого имеете в виду?', 'Who do you have in mind?', [], 'context question'),
    ('lavrov', 'Эдуард Валентинович Каргополов.', 'Eduard Valentinovich Kargopolov.', [(1058, 'Эдуард Валентинович')], ''),
    ('lavrov', 'Бывший любовник Марины Белинкиной.', "Marina Belinkina's former lover.", [(1059, 'Любовник Марины')], "'Бывший' added"),
    ('lavrov', 'Это очень интересный персонаж.', 'This is a very interesting character.', [(1060, 'Интересный персонаж')], "'Это очень' added"),
    ('lavrov', 'Он любит пользоваться бюджетными деньгами.', 'He likes to help himself to public funds.', [(1061, 'Любит'), (1062, 'бюджетными')], "'средствами' -> 'деньгами'"),
    ('zavarzin', 'Отличный план, товарищ майор!', 'Excellent plan, Comrade Major!', [], 'approval line'),
]
WALK = [
    (0, None, "'Handle the money, Mayor!' Major Lavrov firmly instructs Pasha Osipenko to secure his campaign sponsors."),
    (1, None, "'Yes, sir, Comrade Major!' Pasha gives a crisp military affirmative and hurried nod."),
    (2, None, "'So what are we going to do now?' Captain Zavarzin turns to Lavrov once Pasha steps outside the van."),
    (3, None, "'I don't know for sure yet.' Lavrov studies the surveillance reports on his laptop."),
    (4, None, "'Anikeyev loves this woman deeply.' He knows Arkady's genuine affection for Marina is his biggest vulnerability."),
    (5, None, "'But we have no influence over her.' Zavarzin points out that Marina despises both City Hall and the security services."),
    (6, None, "'Some don't, but some do!' Lavrov smirks with a sly gleam in his eye."),
    (7, None, "'Who do you have in mind?' Zavarzin asks, leaning closer to the desk."),
    (8, None, "'Eduard Valentinovich Kargopolov.' Lavrov pulls up the file on Marina's former dean."),
    (9, None, "'Marina Belinkina's former lover.' Notice the masculine noun for a lover in the basic dictionary form."),
    (10, None, "'This is a very interesting character.' Lavrov notes Kargopolov's shady academic bookkeeping."),
    (11, None, "'He likes to help himself to public funds.' The 'with/as' form is used with the self-action verb form meaning 'to make use of'."),
    (12, None, "'Excellent plan, Comrade Major!' Zavarzin grins, realizing they can use the dean's corruption to squeeze Marina and Arkady."),
]
