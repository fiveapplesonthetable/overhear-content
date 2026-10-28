# Authoring module for kukhnya-s01e18-scene-09.
ID = 'kukhnya-s01e18-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 9
TITLE = 'Квартплата  (Rent)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ilya': 'Илья', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = "At the bar, Max explains his risky scheme to Kostya for paying their apartment rent by swapping cheap cognac from Timur with the restaurant's expensive bottles. Let's listen to their conversation in Russian first."
OPENER = "Let's break down Max and Kostya's conversation line by line."
TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = 'Max lays out his cognac-swapping scheme at the bar, hoping it will cover their rent. See you next time!'
CLOSING = ('ilya', 'До встречи!')
STORY = [
    ('kostya', 'Наша квартплата?', 'Our rent?', [(173, 'Наша кварплата?')], ''),
    ('max', 'В смысле?', 'What do you mean?', [(173, 'В смысле?')], ''),
    ('max', 'В прямом смысле.', 'In the literal sense.', [(174, 'В прямом')], ''),
    ('max', 'Сейчас я тебе всё объясню.', 'Now I will explain everything to you.', [(174, 'Сейчас объясню')], ''),
    ('kostya', 'Я ничего не понимаю.', 'I do not understand anything.', [], ''),
    ('max', 'Предположим одну простую ситуацию.', 'Let us suppose one simple situation.', [(175, 'Предположим')], ''),
    ('ilya', 'Тимур привозит нам коньяк.', 'Timur brings us cognac.', [(175, 'Тимур'), (175, 'коньяка')], ''),
    ('max', 'Пять литров коньяка каждую неделю.', 'Five liters of cognac every week.', [(175, 'каждую неделю')], ''),
    ('max', 'Он привозит его бесплатно?', 'Does he bring it for free?', [(176, 'бесплатно')], ''),
    ('max', 'Да, абсолютно бесплатно.', 'Yes, absolutely free.', [(175, 'абсолютно'), (176, 'бесплатно')], ''),
    ('kostya', 'И что мы делаем с ним?', 'And what do we do with it?', [], ''),
    ('max', 'Мы меняем бутылки и платим за квартиру.', 'We swap the bottles and pay for the apartment.', [(178, 'меняем на настоящий коньяк')], ''),
]
WALK = [
    (0, None, "'Our rent?' Kostya repeats the word for apartment rent in surprise."),
    (1, None, "'What do you mean?' This short two-word phrase is the everyday Russian way to ask 'what do you mean?'."),
    (2, None, "'In the literal sense.' Max answers with the matching phrase meaning 'literally'."),
    (3, None, "'Now I will explain everything to you.' Max promises to lay out his plan step by step."),
    (4, None, "'I do not understand anything.' Kostya is still puzzled by how the bar can pay their rent."),
    (5, None, "'Let us suppose one simple situation.' Max sets up a hypothetical example."),
    (6, None, "'Timur brings us cognac.' He names the supplier who offered them cheap alcohol."),
    (7, None, "'Five liters of cognac every week.' Max specifies how much Timur can deliver."),
    (8, None, "'Does he bring it for free?' Rising intonation turns this statement into a question."),
    (9, None, "'Yes, absolutely free.' Max confirms that the first supply costs nothing."),
    (10, None, "'And what do we do with it?' Kostya asks how that turns into rent money."),
    (11, None, "'We swap the bottles and pay for the apartment.' Max reveals the core of his risky scheme. Now let's listen to the conversation again without interruption."),
]
