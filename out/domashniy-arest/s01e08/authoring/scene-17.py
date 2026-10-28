# Authoring module for domashniy-arest-s01e08-scene-17.
ID = 'domashniy-arest-s01e08-scene-17'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 17
TITLE = 'Тяжёлый груз  (Heavy Cargo)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'first_man': 'Первый мужчина', 'second_man': 'Второй мужчина'}
SOURCE_NAME = 'Домашний арест, Сезон 1, Эпизод 8'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "Previously, back in the communal apartment, Arkady accidentally crushed Lyosha's plastic toy tank under his pillow and tried to calm the upset boy before he could call his mother. Meanwhile, out on a chilly city street, two men are loading heavy boxes and luggage into the trunk of a car."
OPENER = "Let's break down the dialogue between the two men loading the car."
TRANSITION = 'Now listen to the loading scene on the street once more.'
OUTRO = 'The two men finish loading the heavy car and prepare to drive away. See you next time!'
CLOSING = ('first_man', 'Пока!')
STORY = [
    ('first_man', 'Ну ладно, не расстраивайся.', "Alright, come on, don't be upset.", [(251, 'Ну ладно, ну чего ты, не расстраивайся')], 'shortened cue 251'),
    ('first_man', 'Здесь пока подождите.', 'Wait here for now.', [(252, 'Здесь пока подождите')], ''),
    ('second_man', 'Мы вещи в машине забираем?', 'Are we getting the things from the car?', [(253, 'В машине забирайте')], 'turned into a question'),
    ('first_man', 'Да, в машине забирайте.', 'Yes, get it from the car.', [(253, 'В машине забирайте')], 'added Да'),
    ('second_man', 'Осторожно, этот ящик очень тяжёлый!', 'Careful, this box is very heavy!', [(254, 'Тяжелый')], 'expanded cue 254'),
    ('first_man', 'Держи крепче! Всё хорошо?', 'Hold it tighter! Is everything okay?', [(255, 'Хорошо?')], 'added Держи крепче'),
    ('second_man', 'Да, держу нормально.', 'Yes, I am holding it fine.', [], 'transitional dialogue line'),
    ('first_man', 'Сейчас ещё один ящик принесу.', "I'll bring one more box now.", [(256, 'Сейчас еще')], 'expanded cue 256'),
    ('second_man', 'Давай быстрее, на улице холодно.', "Hurry up, it's cold outside.", [], 'transitional dialogue line'),
    ('first_man', 'Сейчас будет совсем хорошо.', "Now it'll be just right.", [(257, 'Сейчас будет совсем хорошо')], ''),
    ('second_man', 'А где твои тёплые перчатки?', 'And where are your warm gloves?', [], 'transitional dialogue line'),
    ('first_man', 'Ай, у меня перчаток нет.', "Ow, I don't have gloves.", [(258, 'Ай, у меня нет, нет')], 'adapted cue 258'),
    ('second_man', 'Ладно, давай сюда скорее!', 'Alright, give it here quickly!', [(259, 'еще')], 'cleaned cue 259, omitting profanity'),
    ('first_man', 'Отлично, закрывай скорее багажник!', 'Great, close the trunk quickly!', [], 'concluding dialogue line'),
]
WALK = [
    (0, None, "'Alright, come on, don't be upset.' The negative command reassures someone who is worried."),
    (1, None, "'Wait here for now.' The adverb indicates a temporary pause while waiting."),
    (3, None, "'Yes, get it from the car.' The command form tells him where to collect the items."),
    (4, None, "'Careful, this box is very heavy!' The short adjective describes the heavy load."),
    (5, 'Всё хорошо?', "'Is everything okay?' A common Russian phrase asking if things are fine."),
    (7, None, "'I will bring one more box now.' The adverb indicates an additional item coming."),
    (8, None, "'Hurry up, it is cold outside.' The impersonal phrase describes the freezing weather."),
    (9, None, "'Now it will be just right.' The future tense promises that the job will soon be done."),
    (11, None, "'Ow, I do not have gloves.' The negative construction uses the 'of' form."),
    (12, None, "'Alright, give it here quickly!' The colloquial command urges him to hurry up."),
    (13, None, "'Great, close the trunk quickly!' They finish loading and shut the car trunk."),
]
