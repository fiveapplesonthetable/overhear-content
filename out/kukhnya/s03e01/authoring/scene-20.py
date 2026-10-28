# Authoring module for kukhnya-s03e01-scene-20.
ID = 'kukhnya-s03e01-scene-20'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 1
SCENE = 20
TITLE = 'Настоящее свидание  (A Real Date)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.01'
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'
INTRO = "In the final scene of the episode, Max tracks down Vika's riverboat and leaps off a bridge into the water so the crew has to pull him aboard, turning Nikolai's cruise into his own date with Vika."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that wraps up the Season Three premiere of Kukhnya. Listen for Max's triumphant line after his river jump brings Vika right to his side. See you in Episode Two! See you next time!"
CLOSING = ('max', 'До свидания!')
STORY = [
    ('guest', 'Это самое настоящее свидание.', 'This is a real, genuine date.', [(349, 'Это самое настоящее свидание')], ''),
    ('guest', 'Меня зовут Николай.', 'My name is Nikolai.', [(350, 'Меня зовут Николай')], ''),
    ('guest', 'Мы встречались год назад на фестивале.', 'We met a year ago at a festival.', [(351, 'встречались год назад на кулинарном фестивале')], 'adapted'),
    ('guest', 'Вы выглядели просто потрясающе.', 'You looked simply stunning.', [(353, 'вы выглядели просто потрясающе')], ''),
    ('max', 'Привет! Между прочим, за бой посуды штраф.', 'Hi! By the way, there is a fine for breaking dishes.', [(360, 'Привет'), (361, 'Между прочим, за'), (361, 'посуды штраф')], 'adapted'),
    ('vika', 'Когда ты уйдёшь из моей жизни?', 'When will you get out of my life?', [(362, 'из моей жизни')], 'adapted'),
    ('max', 'Стоп! Хочешь, чтобы я ушёл?', 'Stop! Do you want me to leave?', [(363, 'Стоп! Хочешь, чтоб я ушел')], 'adapted'),
    ('max', 'Ладно, я могу и уйти.', 'Fine, I can leave.', [(364, 'Ладно, я могу и уйти')], ''),
    ('guest', 'Всё нормально?', 'Is everything all right?', [(366, 'Все нормально')], ''),
    ('max', 'Да. Спасибо.', 'Yes. Thank you.', [(367, 'Да. Спасибо')], ''),
    ('vika', 'Ну и чего ты этим добился?', 'Well, and what did you achieve with this?', [(368, 'Ну и чего ты этим добился')], ''),
    ('max', 'Ты пришла ко мне на свидание.', 'You came on a date with me.', [(369, 'Ты пришла ко мне на свидание')], ''),
]
WALK = [
    (0, None, '\'This is a real, genuine date.\' Saying that this is a real genuine date is how the guest sets the tone with Max. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (1, None, "'My name is Nikolai.' Once his name is Nikolai, the guest can finally tell Max what he means."),
    (2, None, "'We met a year ago at a festival.' Adding that they met a year ago at a festival fills in the missing piece for Max."),
    (3, None, '\'You looked simply stunning.\' The guest tells Max that Max looked simply stunning without dressing it up. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (4, None, "'Hi! By the way, there is a fine for breaking dishes.' Because there is a fine for breaking dishes, Max does not bother softening the blow for the guest. Russian puts the key word right up front so his emotion lands on the first beat."),
    (5, None, "'When will you get out of my life?' Wondering when the guest gets out of her life will is how Vika puts the guest on the spot."),
    (6, None, '\'Stop! Do you want me to leave?\' Here checking whether the guest wants him to leave shows Max looking for the real truth. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (7, None, "'Fine, I can leave.' Because fine he can leave, Max treats the matter as settled."),
    (8, None, "'Is everything all right?' Checking whether everything all right cuts straight through the tension between the guest and Max."),
    (9, None, "'Yes. Thank you.' Explaining that the guest should thank the guest lays the cards on the table for the guest."),
    (10, None, '\'Well, and what did you achieve with this?\' Here asking what the guest achieve with this shows Vika looking for the real truth. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (11, None, "'You came on a date with me.' Pointing out that the guest came on a date with him gives the guest a sobering reality check."),
]
