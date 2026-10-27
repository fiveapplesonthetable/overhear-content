ID = "kukhnya-s01e17-scene-17"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 17
TITLE = "Спор о блюде  (Dispute Over the Dish)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'viktor': 'anja'}
LABELS = {'anya': 'Elena', 'viktor': 'Viktor'}

INTRO = 'Viktor goes to the rival restaurant and accuses the chef of stealing his new dish. We will hear it in Russian first, do not worry about catching every word.'
OPENER = "Let's walk through it. Viktor storms into the kitchen."
TRANSITION = "Now let's hear the scene once more."
OUTRO = 'Viktor realizes he was wrong. See you next time.'

STORY = [
    ('viktor', 'Так, стоять.', 'Hold it right there.', [(270, 'Так стоять.')], ''),
    ('anya', 'В чём дело?', 'What is the matter?', [(271, 'Это что такое?')], 'Simplified'),
    ('viktor', 'Вы украли наше блюдо.', 'You stole our dish.', [(275, 'Да вы украли у нас сезонное блюдо от шефа.')], 'Simplified'),
    ('anya', 'Мы его сами придумали.', 'We invented it ourselves.', [(277, 'Мы не успели его в меню вставить, как мы его уже украли.')], 'Simplified'),
    ('viktor', 'Я так и знал.', 'I knew it.', [(276, 'А я так и знал, что вы ничего не можете сами, паразиты.')], 'Simplified'),
    ('viktor', 'Вы ничего не можете сами.', 'You cannot do anything yourselves.', [(276, 'А я так и знал, что вы ничего не можете сами, паразиты.')], 'Simplified'),
    ('anya', 'Посмотрите на эту дату.', 'Look at this date.', [(286, 'Посмотрите, пожалуйста, на дату утверждения меню.')], 'Simplified'),
    ('viktor', 'Ну, ну.', 'Well, well.', [(287, 'Ну, ну.')], ''),
    ('anya', 'Дайте мне меню, пожалуйста.', 'Give me the menu, please.', [(285, 'Меню дайте мне, пожалуйста.')], 'Simplified'),
    ('anya', 'Вы хорошо видите?', 'Can you see clearly?', [(288, 'Вы хорошо видите?')], 'Simplified'),
    ('viktor', 'Да, нормально.', 'Yes, fine.', [(289, 'Нормально.')], 'Simplified'),
    ('viktor', 'Извините.', 'Sorry.', [], ''),
]

WALK = [
    (0, None, "'Hold it right there.' Viktor commands the rival chef to stop."),
    (1, None, "'What is the matter?' She asks him what he wants."),
    (2, None, "'You stole our dish.' He accuses her of stealing his new recipe."),
    (3, None, "'We invented it ourselves.' She defends her restaurant's originality."),
    (4, None, "'I knew it.' He feels his suspicions are confirmed."),
    (5, None, "'You cannot do anything yourselves.' He insults their culinary skills."),
    (6, None, "'Look at this date.' She shows him the approval date of her menu."),
    (7, None, "'Well, well.' He mutters skeptically."),
    (8, None, "'Give me the menu, please.' She asks for his menu to compare."),
    (9, None, "'Can you see clearly?' She asks if he can read the earlier date."),
    (10, None, "'Yes, fine.' He admits that he sees it."),
    (11, None, "'Sorry.' He is forced to apologize for his mistake."),
]

CLOSING = ('anya', 'До свидания.')
