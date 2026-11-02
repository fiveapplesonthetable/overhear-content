# Authoring module for kukhnya-s01e13-scene-03.
ID = 'kukhnya-s01e13-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 3
TITLE = 'Пешком до работы  (Walking to Work)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Vika is driving Max to work, and they are both pretending that nothing is going on between them. She stops the car a short way from the restaurant and tells him to walk. Listen to the scene in the original language before we take it apart."
OPENER = 'Starting with where she makes him get out.'
TRANSITION = 'Now the car ride in one piece.'
OUTRO = "Max steps out and promises to see her in the kitchen. Keep an ear out for the word for together, which keeps coming back in this episode. See you in the next one."
CLOSING = ('max', 'Пока!')
STORY = [
    ('vika', 'Макс, останови машину возле этого угла.', 'Max, stop the car near this corner.', [], ''),
    ('max', 'Почему здесь? Ресторан находится дальше.', 'Why here? The restaurant is located further.', [(42, 'Это почему?')], ''),
    ('vika', 'Давай дальше ты пойдёшь пешком.', 'Let us have you walk the rest on foot.', [(41, 'Давай отсюда ты дойдешь пешком.')], ''),
    ('max', 'Ты не хочешь ехать со мной?', 'You do not want to ride with me?', [], ''),
    ('vika', 'Коллеги не должны видеть нас вместе.', 'Colleagues should not see us together.', [(43, 'если мы боимся на работе вместе.')], ''),
    ('max', 'Ты боишься глупых слухов на работе?', 'Are you afraid of silly rumors at work?', [], ''),
    ('vika', 'Это вызовет лишние вопросы на кухне.', 'This will cause unnecessary questions in the kitchen.', [], ''),
    ('max', 'Ты абсолютно права, дорогая.', 'You are completely right, darling.', [(44, 'ты права.')], ''),
    ('max', 'Это может испортить мою важную репутацию.', 'This could ruin my important reputation.', [(44, 'Это может нанести серьезный урон моей репутации.')], ''),
    ('vika', 'Макс, ты серьёзно так думаешь?', 'Max, do you seriously think so?', [], ''),
    ('max', 'Я просто шучу, успокойся.', 'I am just joking, calm down.', [], ''),
    ('vika', 'Тогда выходи быстрее, я спешу.', 'Then get out faster, I am in a hurry.', [], ''),
    ('max', 'Хорошо, увидимся на кухне, администратор!', 'All right, see you in the kitchen, administrator!', [], ''),
]
WALK = [
    (0, None, ["'Max, stop the car near this corner.' The word for 'stop', ", ('vika', 'останови'), ", is the order you give a friend. The word for 'near', ", ('vika', 'возле'), ", is followed by the 'of' form, and the term for 'corner', ", ('vika', 'угла'), ", drops its 'o' to become this form."]),
    (1, None, ["'Why here? The restaurant is located further.' The restaurant 'finds itself' further, and that is how locals say 'is located', using the word ", ('max', 'находится'), ". Notice for 'further', ", ('max', 'дальше'), ', is the comparing form of far.']),
    (2, None, ["'Let us have you walk the rest on foot.' The word for 'on foot', ", ('vika', 'пешком'), ", tells you it is not by car, which is Vika's whole point. She opens with 'let's', using ", ('vika', 'Давай'), ', and then hands him an order.']),
    (3, None, ["'You do not want to ride with me?' The language has two words for 'go': one on foot and one in a vehicle. Max uses the vehicle one, ", ('max', 'ехать'), ", since a car is exactly what they are in. Notice for 'with me' is ", ('max', 'со'), ('max', 'мной'), '.']),
    (4, None, ["'Colleagues should not see us together.' The term for 'us', ", ('vika', 'нас'), ", is the form 'we' takes after the verb to see, ", ('vika', 'видеть'), ". Notice for 'must not', ", ('vika', 'не'), ('vika', 'должны'), ", has the plural ending to match 'colleagues'."]),
    (5, None, ["'Are you afraid of silly rumors at work?' After 'afraid of', the thing feared takes a new ending, so 'rumors', ", ('max', 'слухов'), ", changes. The same word for 'rumor' also means 'hearing', since a rumor is something you hear."]),
    (6, None, ["'This will cause unnecessary questions in the kitchen.' The term for 'unnecessary' or 'extra' is ", ('vika', 'лишние'), ", and the set phrase for awkward questions uses it together with the term for 'questions'. Locals say 'on the kitchen' where English says 'in', and she uses it for the whole room."]),
    (7, None, ["'You are completely right, darling.' A woman is right, so the term for 'right', ", ('max', 'права'), ", ends in 'a'. Notice for 'darling', ", ('max', 'дорогая'), ", is also the term for 'expensive'."]),
    (8, None, ["'This could ruin my important reputation.' Putting 'important', ", ('max', 'важную'), ", in front of 'reputation', ", ('max', 'репутацию'), ", makes Max sound like a minister. Both words end in 'yu', since they are what is being ruined."]),
    (9, None, ["'Max, do you seriously think so?' The term for 'seriously' is ", ('vika', 'серьёзно'), ", and locals say it as a question when they suspect a joke. The term for 'you think' is ", ('vika', 'думаешь'), '.']),
    (10, None, ["'I am just joking, calm down.' The expression 'I'm joking', ", ('max', 'шучу'), ', comes from the term for joke. The calming order, ', ('max', 'успокойся'), ", has an ending that means 'calm yourself', and it works for babies, too."]),
    (11, None, ["'Then get out faster, I am in a hurry.' The order to get out, ", ('vika', 'выходи'), ", is 'out' plus the verb for going on foot, and it is what you say to someone getting out of a car. Here we have for 'I am in a hurry', ", ('vika', 'спешу'), ", is just 'I hurry', one word."]),
    (12, None, ["'All right, see you in the kitchen, administrator!' Locals say 'we will see each other', ", ('max', 'увидимся'), ", with an ending for 'each other'. Max teases her by using her job title instead of her name."]),
]
