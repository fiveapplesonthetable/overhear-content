# Authoring module for kukhnya-s01e17-scene-17.
ID = 'kukhnya-s01e17-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 17
TITLE = 'Спор о блюде  (Dispute Over the Dish)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = "Viktor goes to the rival restaurant and accuses the chef of stealing his new dish. We will hear it in Russian first, do not worry about catching every word. Let's listen closely to the conversation in Russian first, and then walk through each line together."
OPENER = "Let's walk through it. Viktor storms into the kitchen."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Viktor realizes he was wrong. Next time you watch the episode, listen for the Russian expressions for 'to stand' and 'matter' — you will catch every word right away. See you next time!"
CLOSING = ('elena', 'До свидания.')
STORY = [
    ('barinov', 'Так, стоять.', 'Hold it right there.', [(270, 'Так стоять.')], ''),
    ('elena', 'В чём дело?', 'What is the matter?', [(271, 'Это что такое?')], ''),
    ('barinov', 'Вы украли наше блюдо.', 'You stole our dish.', [(275, 'Да вы украли у нас сезонное блюдо от шефа.')], ''),
    ('elena', 'Мы его сами придумали.', 'We invented it ourselves.', [(277, 'Мы не успели его в меню вставить, как мы его уже украли.')], ''),
    ('barinov', 'Я так и знал.', 'I knew it.', [(276, 'А я так и знал, что вы ничего не можете сами, паразиты.')], ''),
    ('barinov', 'Вы ничего не можете сами.', 'You cannot do anything yourselves.', [(276, 'А я так и знал, что вы ничего не можете сами, паразиты.')], ''),
    ('elena', 'Посмотрите на эту дату.', 'Look at this date.', [(286, 'Посмотрите, пожалуйста, на дату утверждения меню.')], ''),
    ('barinov', 'Ну, ну.', 'Well, well.', [(287, 'Ну, ну.')], ''),
    ('elena', 'Дайте мне меню, пожалуйста.', 'Give me the menu, please.', [(285, 'Меню дайте мне, пожалуйста.')], ''),
    ('elena', 'Вы хорошо видите?', 'Can you see clearly?', [(288, 'Вы хорошо видите?')], ''),
    ('barinov', 'Да, нормально.', 'Yes, fine.', [(289, 'Нормально.')], ''),
    ('barinov', 'Извините.', 'Sorry.', [], ''),
]
WALK = [
    (0, None, "'Hold it right there.' Barinov commands attention, stopping the interaction instantly."),
    (1, None, "'What is the matter?' Elena demands to know the reason for his sudden interruption."),
    (2, None, "'You stole our dish.' Barinov makes a blunt accusation of theft regarding the recipe."),
    (3, None, "'We invented it ourselves.' Elena fires back, firmly claiming originality."),
    (4, None, "'I knew it.' Barinov expresses his lack of surprise at the situation."),
    (5, None, "'You cannot do anything yourselves.' He insults their competence, insisting they rely on stealing ideas."),
    (6, None, "'Look at this date.' Elena presents evidence to counter his claim, drawing attention to a specific detail."),
    (7, None, "'Well, well.' Barinov reacts with slight hesitation as he takes in the new information."),
    (8, None, "'Give me the menu, please.' Elena confidently asks for the item back, knowing she has the upper hand."),
    (9, None, "'Can you see clearly?' She mocks his observation skills, driving her point home."),
    (10, None, "'Yes, fine.' Barinov curtly acknowledges the evidence, realizing he was wrong."),
    (11, None, "'Sorry.' He offers a brief, somewhat reluctant apology to end the dispute."),
]
