# Authoring module for kukhnya-s01e08-scene-13.
ID = 'kukhnya-s01e08-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 13
TITLE = 'Тайник на складе  (Hiding Place in the Storeroom)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "At Claude Monet, Max and Vika are trying to hide Nagiyev's dog, Tyson, in the vegetable storeroom, behind the potatoes. Lyova, the sous-chef, is about to walk in on them. It's in Russian first."
OPENER = 'Slowly now. Max and Vika speak in quick commands, and then Lyova walks in.'
TRANSITION = "Here's the hiding again, all in one go."
OUTRO = "Lyova's put-down, eto vam ne motel, 'this is no motel for you', is a joke and a telling-off at once. And pust ona polezhit, 'let her lie for a while', shows how pust makes a 'let' for someone else. See you next time."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Вот, положи её сюда.', 'Here, put her here.', [(139, 'сюда давай')], ''),
    ('vika', 'Пусть она полежит здесь до вечера.', 'Let her lie here until evening.', [(140, 'Пусть пока до вечера здесь полежит')], ''),
    ('max', 'Мы вынесем её ночью.', 'We will carry her out at night.', [(140, 'вынесем ее')], ''),
    ('vika', 'Возьми свежую кинзу.', 'Take the fresh cilantro.', [(141, 'Так, кинза')], ''),
    ('vika', 'Она легко перебьёт любой запах.', 'It will easily cover any odor.', [(142, 'Она так пахнет, если что, запах перебьет')], ''),
    ('max', 'Помоги мне поднять этот мешок.', 'Help me lift this sack.', [(148, 'Давай помогай')], ''),
    ('vika', 'Положи собаку глубже за картошку.', 'Put the dog deeper behind the potatoes.', [(152, 'Засовывай сюда'), (153, 'Глубже засовывай')], ''),
    ('lyova', 'А чем вы тут занимаетесь?', 'And what are you doing here?', [(154, 'А чем вы тут занимаетесь?')], ''),
    ('vika', 'Я просто ищу чистые скатерти.', 'I am just looking for clean tablecloths.', [(156, 'Я скатерти ищу')], ''),
    ('lyova', 'Скатерти на овощном складе?', 'Tablecloths in the vegetable storeroom?', [(157, 'скатерти на овощном складе')], ''),
    ('lyova', 'Макс, почему ты не на кухне?', "Max, why aren't you in the kitchen?", [(159, 'почему не на рабочем месте')], ''),
    ('max', 'У меня сегодня законный выходной.', 'I have a legitimate day off today.', [(160, 'А у меня выходной')], ''),
    ('lyova', 'Быстро уходите, это вам не мотель.', 'Leave quickly, this is no motel for you.', [(162, 'заканчивайте здесь фритюриться, это вам не мотель')], ''),
]
WALK = [
    (0, None, "'Here, put her here.' You say vot when handing over or showing something. Max's polozhi is the friendly 'put', and yeyo, 'her', is feminine to match sobaka."),
    (1, None, "'Let her lie here until evening.' To let someone else do something, Russian uses pust: pust ona polezhit. With po-, polezhat means lying for a while, and after do, 'until', vecher becomes vechera."),
    (2, None, "'We will carry her out at night.' The vy- in vynesem, 'we'll carry out', is the same 'out' as in vykhod, 'exit'. Russian says 'at night' with one word, nochyu."),
    (3, None, "'Take the fresh cilantro.' Vika's vozmi is the friendly command from vzyat, 'to take'. As the thing taken, kinza, 'cilantro', becomes kinzu."),
    (4, None, "'It will easily cover any odor.' Built from pere-, 'over', and bit, 'to beat', perebit is what a strong smell does to a weaker one. Here ona, 'it', is the cilantro, since kinza is feminine."),
    (5, None, "'Help me lift this sack.' In Russian you give help to someone, so 'me' is mne. Then comes podnyat, 'to lift', in its basic form."),
    (6, None, "'Put the dog deeper behind the potatoes.' Because the dog is being moved there, it's za kartoshku; once she's there, she lies za kartoshkoy. The singular kartoshka means potatoes in general."),
    (7, None, "'And what are you doing here?' Lyova's chem vy tut zanimayetes, 'what are you busy with here', is a classic boss's question. His vy is plural, for both of them."),
    (8, None, "'I am just looking for clean tablecloths.' The object of ishchu, 'I'm looking for', follows with no 'for' at all. The plural skaterti comes from skatert, 'tablecloth'."),
    (9, None, "'Tablecloths in the vegetable storeroom?' By repeating Vika's words with a rising voice, Lyova turns them into a question; Russian needs nothing else. The word ovoshchnoy, 'vegetable', comes from ovoshchi, 'vegetables'."),
    (10, None, "'Max, why aren't you in the kitchen?' Putting ne straight before the place gives ne na kukhne, 'not in the kitchen'. Lyova says ty to Max, as the senior cooks do."),
    (11, None, "'I have a legitimate day off today.' Max's u menya vykhodnoy, literally 'by me a day off', is how you say you're off work. With zakonnyy, 'legitimate', he insists he has every right to it."),
    (12, None, "'Leave quickly, this is no motel for you.' Since ukhodite is plural, he is sending both of them out. A common scolding goes eto vam ne..., 'this is not a ... for you', as in eto vam ne shkola."),
]
