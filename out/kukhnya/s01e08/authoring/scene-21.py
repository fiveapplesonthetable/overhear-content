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
INTRO = "With Chef Barinov away, guest chef Elena Pavlovna Sokolova takes command of the Claude Monet kitchen. Accustomed to Barinov's relaxed habits, the cooks struggle under Elena's uncompromising discipline. When she refuses smoke breaks and orders sous-chef Lyova to fetch herbs from the cellar, tension flares. Let's listen to their confrontation in Russian first."
OPENER = "Let's examine how authority and resistance clash in this restaurant kitchen. Notice the decisive imperative commands and the indignant defensive replies."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Lyova reluctantly heads off to the storage room, stewing over Elena's demanding management style. Outstanding work mastering workplace and culinary Russian! Next time you watch the episode, listen for the Russian expressions for 'fast' and 'to go out' — you will catch every word right away. See you next time!"
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
    (0, None, "'Chef, can the cooks go smoke?' Lyova asks for a simple break, expecting the usual relaxed kitchen atmosphere."),
    (1, None, "'Are you mad? Plenty of orders!' Elena reacts with pure outrage, pointing to the endless stream of waiting orders."),
    (2, None, "'But there are no meat orders now.' He tries to justify the request logically by noting a lull in his specific station."),
    (3, None, "'Then quickly switch over to poultry!' Elena demands absolute efficiency, ordering him to immediately pivot to a different task."),
    (4, None, "'The cooks are very tired from this work.' Lyova attempts to appeal to her sympathy, explaining the crew's exhaustion."),
    (5, None, "'No smoke breaks, everyone stays in the kitchen!' She completely shuts down any talk of rest, enforcing a strict lockdown on the line."),
    (6, None, "'You are too strict with our team.' He bravely calls out her dictatorial management style right to her face."),
    (7, None, "'I need you to work excellently!' Elena does not care about being liked, only about achieving flawless culinary results."),
    (8, None, "'The kitchen has run out of fresh arugula.' Lyova reports a missing ingredient, expecting someone else to handle the logistics."),
    (9, None, "'Lyova, quickly bring arugula from the storeroom!' She barks a direct order at him to fetch it himself from the basement."),
    (10, None, "'I am a sous-chef, not a courier!' Lyova protests the severe demotion, insulted that a sous-chef is being sent on errands."),
    (11, None, "'I decide myself who will go there!' Elena brutally reminds him that her word is absolute law in this kitchen."),
    (12, None, "'Fine, Chef, I will bring this greenery.' Defeated, he bites his tongue and accepts the humiliating task."),
]
