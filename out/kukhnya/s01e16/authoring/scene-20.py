# Authoring module for kukhnya-s01e16-scene-20.
ID = 'kukhnya-s01e16-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 20
TITLE = 'Штраф и депортация  (Fine and Deportation)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'inspector': 'Инспектор'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "Marching the caught pastry chef into Chef Barinov's office, the migration inspector scolds Viktor Petrovich for trying to hide his undocumented staff. Instead of letting the restaurant off with a simple warning, the officer announces a steep fine and orders Louis to be sent back home. Let's listen to their confrontation in Russian."
OPENER = "Let's see how the migration inspector delivers the bad news to Chef Barinov."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Now you know how to talk about warnings, fines, and official consequences in Russian. Keep listening to see how the kitchen staff react to the aftermath. Next time you watch the episode, listen for the Russian expressions for 'to find' and 'cook' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('inspector', 'Вот я и нашёл вашего повара.', 'Here, I found your chef.', [(271, 'Вот')], ''),
    ('barinov', 'Луи, почему ты не спрятался?', 'Louis, why did you not hide?', [], ''),
    ('inspector', 'Зря вы обманывали меня, Виктор Петрович.', 'You deceived me in vain, Viktor Petrovich.', [(272, 'Зря вы, Виктор Петрович')], ''),
    ('barinov', 'Я хотел защитить своего лучшего повара.', 'I wanted to protect my best chef.', [], ''),
    ('inspector', 'Нужно было сразу признаться во всём.', 'You should have confessed to everything right away.', [(273, 'Признались бы сразу во всем')], ''),
    ('inspector', 'Тогда вы получили бы простое предупреждение.', 'Then you would have received a simple warning.', [(273, 'простым предупреждением')], ''),
    ('barinov', 'Мы можем договориться с вами сейчас?', 'Can we reach an agreement with you now?', [], ''),
    ('inspector', 'Нет, теперь уже слишком поздно.', 'No, now it is already too late.', [], ''),
    ('inspector', 'К сожалению, вам придётся платить штраф.', 'Unfortunately, you will have to pay a fine.', [(274, 'придется платить штраф')], ''),
    ('barinov', 'Ладно, ресторан заплатит этот большой штраф.', 'All right, the restaurant will pay this big fine.', [], ''),
    ('inspector', 'Но это ещё далеко не всё.', 'But that is still far from all.', [], ''),
    ('inspector', 'Этого молодого человека мы отправим домой.', 'We will send this young man home.', [(275, 'молодого человека')], ''),
    ('barinov', 'Как я буду работать без Луи?', 'How will I work without Louis?', [], ''),
]
WALK = [
    (0, None, "'You deceived me in vain, Viktor Petrovich.' Opening with the word 'zrya' meaning pointless or for nothing, the official scolds the chef for trying to lie."),
    (1, None, "'You should have confessed to everything right away.' inspector points out that coming clean from the very beginning would have been the right move."),
    (2, None, "'Unfortunately, you will have to pay a fine.' Delivering the bad news, the officer announces that a financial penalty is completely unavoidable."),
    (3, None, "'We will send this young man home.' A stern promise is made to put the pastry cook on a plane back to his home country."),
]
