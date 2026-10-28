# Authoring module for kukhnya-s01e18-scene-02.
ID = 'kukhnya-s01e18-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 2
TITLE = 'Низкая выручка  (Low Revenue)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nagiyev': 'Нагиев', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = "Dmitry is shocked by the tiny revenue numbers in the financial report and confronts Vika and Viktor. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Let's break down this tense business meeting."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Dmitry sends Kristina away so he can take personal control of the restaurant's finances. Next time you watch the episode, listen for the Russian expressions for 'small' and 'number' — you will catch every word right away. See you next time!"
CLOSING = ('nagiyev', 'Пока!')
STORY = [
    ('nagiyev', 'Что это за маленькие цифры в отчёте?', 'What are these small numbers in the report?', [(18, 'а что это за такие')], ''),
    ('nagiyev', 'Почему у нас так мало денег?', 'Why do we have so little money?', [(21, 'Почему так мало у нас')], ''),
    ('vika', 'Дмитрий Владимирович, сейчас у нас мало гостей.', 'Dmitry Vladimirovich, we have few guests right now.', [(22, 'Дмитрий Владимирович')], ''),
    ('vika', 'Рядом открылся новый итальянский ресторан.', 'A new Italian restaurant opened nearby.', [], ''),
    ('nagiyev', 'А мне что теперь делать?', 'And what am I supposed to do now?', [(24, 'А мне что делать')], ''),
    ('nagiyev', 'Мне нужно кормить свою большую семью!', 'I need to feed my big family!', [], ''),
    ('barinov', 'Дима, ну сейчас просто нет людей.', 'Dima, well there are simply no people right now.', [(27, 'ну нет людей')], ''),
    ('barinov', 'Мы не можем тащить их сюда силой.', 'We cannot drag them in here by force.', [(27, 'Не можем же мы их сюда')], ''),
    ('nagiyev', 'У вас всегда одна и та же история!', 'You always have the exact same story!', [(28, 'история')], ''),
    ('vika', 'Мы обязательно придумаем хорошее решение.', 'We will definitely come up with a good solution.', [], ''),
    ('nagiyev', 'Вы видите, мы здесь серьёзно работаем.', 'You see, we are working seriously here.', [(36, 'ты видишь, мы здесь работаем')], ''),
    ('nagiyev', 'Я остаюсь в ресторане со своими коллегами!', 'I am staying at the restaurant with my colleagues!', [(37, 'с коллегами')], ''),
]
WALK = [
    (0, None, "'What are these small numbers in the report?' Nagiyev demands an explanation for the terrible financial results, pointing directly at the tiny numbers on the page."),
    (1, None, "'Why do we have so little money?' Nagiyev expresses pure shock, asking why they possess so little cash right now."),
    (2, None, "'Dmitry Vladimirovich, we have few guests right now.' Vika tries to calmly explain the lack of customers, using his formal name to maintain a respectful tone."),
    (3, None, "'A new Italian restaurant opened nearby.' Vika shifts the blame to a newly opened competitor in the neighborhood."),
    (4, None, "'And what am I supposed to do now?' Nagiyev acts helpless, asking what he is expected to do with this terrible situation."),
    (5, None, "'I need to feed my big family!' Nagiyev dramatically claims he has a large family to support, making the low revenue sound like a personal crisis."),
    (6, None, "'Dima, well there are simply no people right now.' Chef Barinov speaks to him casually, stating the obvious fact that the dining room is completely empty."),
    (7, None, "'We cannot drag them in here by force.' Chef Barinov points out they cannot literally force people off the street to come eat at Claude Monet."),
    (8, None, "'You always have the exact same story!' Nagiyev angrily dismisses their excuses, claiming they constantly tell him the exact same thing."),
    (9, None, "'We will definitely come up with a good solution.' Vika promises they will find a way out of this mess, trying to soothe her furious boss."),
    (10, None, "'You see, we are working seriously here.' Nagiyev demands they take the financial crisis as seriously as he does."),
    (11, None, "'I am staying at the restaurant with my colleagues!' Nagiyev announces he is not leaving until they figure this out, committing to stay on site."),
]
