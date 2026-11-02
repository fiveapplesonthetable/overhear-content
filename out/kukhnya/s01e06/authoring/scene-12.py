# Authoring module for kukhnya-s01e06-scene-12.
ID = 'kukhnya-s01e06-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 12
TITLE = 'Строгая проверка  (A Strict Inspection)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'inspector': 'Инспектор'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Inside the kitchen at Claude Monet the sanitary inspector is checking everything: the floor, the grill, a bottle that should not be open. Barinov, the head chef, follows him and tries to keep up appearances. It's in Russian first."
OPENER = 'Slowly now. The inspector speaks in short official remarks, and Barinov answers with excuses.'
TRANSITION = 'Here is the inspection again, from the slippery floor on.'
OUTRO = 'Barinov keeps saying "lichno", personally, and the inspector keeps saying "narushenie", violation. Between them they\'ve given you the vocabulary of a very bad afternoon. See you next time.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('inspector', 'Скользкий пол — это источник опасности.', 'A slippery floor is a source of danger.', [(160, 'Скользкий пол — это источник опасности для сотрудников')], ''),
    ('barinov', 'Мы сейчас же вытрем эту воду.', 'We will wipe up this water immediately.', [], ''),
    ('inspector', 'Почему у гриля открыта эта бутылка?', 'Why is this bottle open by the grill?', [(161, 'Почему у гриля открыта бутылка с алкоголем')], ''),
    ('barinov', 'Это вино нужно для мясного соуса.', 'This wine is needed for meat sauce.', [], ''),
    ('inspector', 'Понятно, но это всё равно нарушение.', 'Understood, but that is still a violation.', [(162, 'Понятно')], ''),
    ('barinov', 'Я лично уберу бутылку в шкаф.', 'I will personally put the bottle in the cupboard.', [], ''),
    ('inspector', 'Простым штрафом вы здесь не отделаетесь!', "You won't get off with a simple fine here!", [(163, 'простым штрафом вы здесь не отделаетесь')], ''),
    ('barinov', 'Поверьте, у нас образцовый ресторан!', 'Believe me, we have an exemplary restaurant!', [], ''),
    ('inspector', 'Пойдёмте дальше, я осмотрю склад.', "Let's move on, I will inspect the storage.", [(164, 'Пойдемте дальше')], ''),
    ('barinov', 'Прошу вас, идите прямо за мной.', 'Please, walk right behind me.', [], ''),
    ('inspector', 'А что находится за этой дверью?', 'And what is located behind this door?', [(165, 'А тут что')], ''),
    ('barinov', 'Там наш склад для закрытых бутылок.', 'There is our storage for unopened bottles.', [(166, 'Склад алкоголя')], ''),
    ('inspector', 'Откройте замок, я должен всё увидеть.', 'Open the lock, I must see everything.', [], ''),
]
WALK = [
    (0, None, ["'A slippery floor is a source of danger.' Let us start by focusing on ", ('inspector', 'источник'), ', which typically describes a natural spring of water but here describes the origin of a problem.']),
    (1, None, ["'We will wipe up this water immediately.' Pay close attention to the word ", ('barinov', 'вытрем'), ', which conveys the physical action of cleaning up a spill using a cloth or mop.']),
    (2, None, ["'Why is this bottle open by the grill?' You might notice how he uses ", ('inspector', 'гриля'), ', a familiar piece of cooking equipment that has found its way into the language.']),
    (3, None, ["'This wine is needed for meat sauce.' Notice the specific word chosen here: ", ('barinov', 'мясного'), ', describing something hearty and savory that comes from an animal.']),
    (4, None, ["'Understood, but that is still a violation.' Here we see the everyday expression ", ('inspector', 'нарушение'), ', pointing to a broken rule or an action that goes against the established guidelines.']),
    (5, None, ["'I will personally put the bottle in the cupboard.' The chef emphasizes his commitment with ", ('barinov', 'лично'), ', ensuring the inspector that he will handle the task himself rather than delegating it.']),
    (6, None, ["'You won't get off with a simple fine here!' Listen carefully for the severe penalty, ", ('inspector', 'штрафом'), ', which implies a financial punishment that will cost the restaurant money.']),
    (7, None, ["'Believe me, we have an exemplary restaurant!' He tries to sound reassuring using ", ('barinov', 'образцовый'), ', suggesting their establishment is a perfect model that others should copy.']),
    (8, None, ["'Let's move on, I will inspect the storage.' The inspector gives a clear directive: ", ('inspector', 'осмотрю'), ', showing his intent to look carefully in every corner for any further issues.']),
    (9, None, ["'Please, walk right behind me.' The chef shows polite manners with ", ('barinov', 'прямо'), ', asking the guest to step directly and exactly where he leads without wandering off.']),
    (10, None, ["'And what is located behind this door?' A key detail to catch is ", ('inspector', 'находится'), ', meaning something is situated or physically placed in a specific spot.']),
    (11, None, ["'There is our storage for unopened bottles.' The storage room is described as ", ('barinov', 'склад'), ', an area dedicated to keeping supplies and inventory safe and organized.']),
    (12, None, ["'Open the lock, I must see everything.' The final instruction is given with ", ('inspector', 'замок'), ', referring to the security device on the door that keeps unauthorized people out.']),
]
