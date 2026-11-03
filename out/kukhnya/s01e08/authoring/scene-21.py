# Authoring module for kukhnya-s01e08-scene-21.
ID = 'kukhnya-s01e08-scene-21'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 21
TITLE = 'Строгие порядки  (Strict Orders)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'elena': 'Елена', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Back in the kitchen at Claude Monet, Elena Pavlovna, borrowed from a rival restaurant, is in charge while Barinov sulks. The cooks want a smoke break, the way they had under Barinov. Lyova, the sous-chef, asks for one, and Elena says no. Here it is in Russian first."
OPENER = "Let's go through the standoff. Lyova stays polite, and Elena doesn't give an inch."
TRANSITION = "Now the full exchange without stopping."
OUTRO = "Lyova gets the last word in spirit — 'I'm a sous-chef, not a courier' — and then trudges off to fetch the arugula anyway. See you next time."
CLOSING = ('elena', 'Пока!')
STORY = [
    ('lyova', 'Шеф, можно поварам выйти перекурить?', 'Chef, can the cooks go smoke?', [(241, 'Шеф, мы перекурить')], ''),
    ('elena', 'Вы в своём уме? Заказов полно!', 'Are you mad? Plenty of orders!', [(242, 'Вы в своем уме')], ''),
    ('lyova', 'Но по мясу сейчас чеков нет.', 'But there are no meat orders now.', [(244, 'По мясу ни одного чека нет')], ''),
    ('elena', 'Значит, быстро переходите на курицу!', 'Then quickly switch over to poultry!', [(245, 'Значит, переходи на курицу')], ''),
    ('lyova', 'Повара очень устали от этой работы.', 'The cooks are very tired from this work.', [], ''),
    ('elena', 'Никаких перекуров, все остаются на кухне!', 'No smoke breaks, everyone stays in the kitchen!', [(246, 'никаких перекурок')], ''),
    ('lyova', 'Вы слишком строги с нашей командой.', 'You are too strict with our team.', [], ''),
    ('elena', 'Мне нужно, чтобы вы отлично работали!', 'I need you to work excellently!', [(249, 'А мне нужно, чтобы вы работали')], ''),
    ('lyova', 'На кухне закончилась свежая рукола.', 'The kitchen has run out of fresh arugula.', [(251, 'Так, у нас закончилась рукола')], ''),
    ('elena', 'Лёва, быстро принесите руколу со склада!', 'Lyova, quickly bring arugula from the storeroom!', [(252, 'Лев, принесите, пожалуйста, руколу со склада')], ''),
    ('lyova', 'Я су-шеф, а не курьер!', 'I am a sous-chef, not a courier!', [(255, 'А вообще-то я здесь суша')], ''),
    ('elena', 'Я сама решаю, кто пойдёт туда!', 'I decide myself who will go there!', [(257, 'я буду решать, кто пойдет')], ''),
    ('lyova', 'Хорошо, шеф, я принесу эту зелень.', 'Fine, Chef, I will bring this greenery.', [], ''),
]
WALK = [
    (0, None, ["'Chef, can the cooks go smoke?' This polite request for a quick ", ('lyova', 'перекурить'), ' shows how the staff wants a break.']),
    (1, None, ["'Are you mad? Plenty of orders!' The new boss expresses her frustration by saying ", ('elena', 'полно'), ' to emphasize the high volume of orders.']),
    (2, None, ["'But there are no meat orders now.' In local kitchen slang, the printed ", ('lyova', 'чеков'), ' refer to the incoming paper food orders.']),
    (3, None, ["'Then quickly switch over to poultry!' Notice how she casually mentions the ", ('elena', 'курицу'), ' when demanding an immediate switch to poultry.']),
    (4, None, ["'The cooks are very tired from this work.' To highlight that the cooks are ", ('lyova', 'устали'), ', he mentions their deep physical exhaustion.']),
    (5, None, ["'No smoke breaks, everyone stays in the kitchen!' A very flat and strict denial starts with ", ('elena', 'Никаких'), ', making it clear that breaks are forbidden.']),
    (6, None, ["'You are too strict with our team.' He tries to soften his feedback with ", ('lyova', 'слишком'), ' to tell her she went too far.']),
    (7, None, ["'I need you to work excellently!' She firmly demands that they work ", ('elena', 'отлично'), ' without making any careless mistakes today.']),
    (8, None, ["'The kitchen has run out of fresh arugula.' When a specific ingredient has completely ", ('lyova', 'закончилась'), ', it sounds as if it finished itself.']),
    (9, None, ["'Lyova, quickly bring arugula from the storeroom!' The necessary supplies are at the ", ('elena', 'склада'), ', so she sends him to fetch them.']),
    (10, None, ["'I am a sous-chef, not a courier!' Feeling quite insulted by the task, he insists he is no mere ", ('lyova', 'курьер'), ' who just runs basic errands for people.']),
    (11, None, ["'I decide myself who will go there!' Asserting absolute authority over everyone, she uses the word ", ('elena', 'решаю'), ' to state that she makes the choices.']),
    (12, None, ["'Fine, Chef, I will bring this greenery.' Rather than repeating the plant name, the simple term ", ('lyova', 'зелень'), ' is used for general leafy greens.']),
]
