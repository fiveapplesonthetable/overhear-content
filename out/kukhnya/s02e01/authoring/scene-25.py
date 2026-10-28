# Authoring module for kukhnya-s02e01-scene-25.
ID = 'kukhnya-s02e01-scene-25'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 1
SCENE = 25
TITLE = 'Смена власти  (Shift of Power)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена', 'igor': 'Игорь'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.01'
SOURCE_FILE = 'sources/kukhnya/s02/e01.ru.dual.srt'
INTRO = "Igor Valentinovich tries to fire Fedya and take full control of the kitchen. But Elena arrives with documents proving she owns the restaurant. Let's listen closely to the conversation in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the exchange around Shift of Power line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Elena takes control of the restaurant, saving the kitchen staff and forcing Igor to step down. Next time you watch the episode, listen for the Russian expressions for 'shameful' and 'particularly' — you will catch every word right away. See you next time!"
CLOSING = ('elena', 'Пока!')
STORY = [
    ('igor', 'Виктор Петрович, не стыдно мне.', "Viktor Petrovich, aren't you ashamed of me?", [(278, 'не стыдно мне')], ''),
    ('barinov', 'Да не особо.', 'Not really.', [(279, 'Да не особо')], ''),
    ('barinov', 'Здорово, когда начальство понятливое.', 'It is great when the boss is understanding.', [(281, 'когда начальство понятливое')], ''),
    ('igor', 'Шеф, Федю уволили.', 'Boss, Fedya has been fired.', [(282, 'Федю уволили')], ''),
    ('barinov', 'Ты что себе позволяешь?', 'What do you think you are doing?', [(283, 'что себе позволяешь')], ''),
    ('barinov', 'Ты зачем Федю уволил?', 'Why did you fire Fedya?', [(284, 'зачем Федю уволил')], ''),
    ('barinov', 'Я не позволю увольнять моих людей.', 'I will not let you fire my people.', [(286, 'не позволю увольнять моих людей')], ''),
    ('igor', 'Здесь я хозяин.', 'I am in charge here.', [(290, 'я хозяин')], ''),
    ('igor', 'Я решаю, кого увольнять, а кого нет.', "I decide who gets fired and who doesn't.", [(291, 'кого увольнять, а кого нет')], ''),
    ('barinov', 'С меня хватит.', 'I have had enough.', [(295, 'С меня хватит')], ''),
    ('igor', 'Вы все уволены.', 'You are all fired.', [(296, 'Вы все уволены')], ''),
    ('elena', 'Я так не думаю.', 'I do not think so.', [(296, 'Я так не думаю')], ''),
    ('elena', 'Это бумаги, которые подтверждают.', 'These are the papers that prove it.', [(298, 'бумаги, которые подтверждают')], ''),
    ('elena', 'Я являюсь владелицей.', 'I am the owner.', [(298, 'являюсь владелицей')], ''),
    ('igor', 'Этого не может быть.', 'That cannot be.', [(300, 'Этого не может быть')], ''),
    ('elena', 'А пока я буду решать.', 'And for now, I will decide.', [(304, 'я буду решать')], ''),
]
WALK = [
    (0, None, "'Boss, Fedya has been fired.' Word reaches the chef that Igor has just fired Fedya."),
    (1, None, "'What do you think you are doing?' Furious, Barinov confronts Igor and asks who he thinks he is."),
    (2, None, "'I will not let you fire my people.' Viktor declares that nobody is allowed to fire his kitchen crew."),
    (3, None, "'I am in charge here.' Igor snaps back that he is the owner here."),
    (4, None, "'I have had enough.' Barinov says he has had enough of Igor's tyranny."),
    (5, None, "'You are all fired.' The character uses the polite everyday 'you' alongside 'fired', keeping a formal or respectful register. Then Elena responds."),
    (6, None, "'I do not think so.' Stepping into the room, Kristina's friend or Elena calmly disagrees."),
    (7, None, "'I am the owner.' She announces with legal papers in hand that she is the rightful owner now."),
    (8, None, "'That cannot be.' Igor stares in disbelief, unable to accept that he has lost the restaurant."),
]
