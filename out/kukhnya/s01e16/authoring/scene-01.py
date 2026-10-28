# Authoring module for kukhnya-s01e16-scene-01.
ID = 'kukhnya-s01e16-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 1
TITLE = 'Пожарная тревога  (Fire Alarm)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'inspector': 'Инспектор', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'Welcome to Kukhnya, the Russian comedy set in Claude Monet, a smart Moscow restaurant where Chef Barinov rules the kitchen. Today a fire inspector arrives and finds fault with everything he sees, while Vika, the art director, tries to keep her cool. Listen first to how polite he stays while he complains.'
OPENER = "Now line by line, starting with the inspector's verdict."
TRANSITION = 'Here is the inspection again, all in one go.'
OUTRO = "Two days is the inspector's deadline, and he doesn't sound like a man who bends. When you watch, listen for the little word that means 'there isn't', because the inspector uses it again and again. See you next time!"
CLOSING = ('vika', 'До свидания!')
STORY = [
    ('inspector', 'У вас очень плохая картина по безопасности.', 'You have a very bad picture regarding safety.', [(1, 'У вас тут просто удручающая картина по технике пожарной безопасности.')], ''),
    ('vika', 'У нас всё в порядке.', 'Everything is fine with us.', [(2, 'Да все же в порядке.')], ''),
    ('vika', 'Мы прошли все проверки.', 'We passed all inspections.', [(2, 'Мы прошли все проверки.')], ''),
    ('inspector', 'Как вы прошли проверки?', 'How did you pass the inspections?', [(3, 'Ну как вы прошли проверки?')], ''),
    ('inspector', 'У вас нет огнетушителей на кухне.', 'You have no fire extinguishers in the kitchen.', [(3, 'Когда у вас на кухне даже огнетушителей нет.')], ''),
    ('vika', 'У нас есть один.', 'We have one.', [(4, 'Да он есть, под собки висит.')], ''),
    ('vika', 'Он висит в подсобке.', 'It is hanging in the back room.', [(4, 'под собки висит.')], ''),
    ('inspector', 'Он должен висеть в трёх метрах.', 'It must hang within three meters.', [(5, 'А должен висеть в трех метрах от предполагаемого места возможного пожара.')], ''),
    ('inspector', 'От места возможного пожара.', 'From the place of a possible fire.', [(5, 'от предполагаемого места возможного пожара.')], ''),
    ('vika', 'Это не проблема.', 'This is not a problem.', [], ''),
    ('inspector', 'Это очень большая проблема.', 'This is a very big problem.', [], ''),
    ('inspector', 'Ох, как всё плохо.', 'Oh, how bad everything is.', [(6, 'Ох-ох-ох.')], ''),
    ('inspector', 'Я даю вам два дня на исправление.', 'I give you two days for correction.', [(7, 'Даю два дня на исправление ситуации.')], ''),
    ('vika', 'Мы всё сделаем.', 'We will do everything.', [], ''),
]
WALK = [
    (0, None, "'You have a very bad picture regarding safety.' 'U vas', literally 'at you', is the everyday Russian way to say 'you have'. 'Kartina', 'picture', is used for how a situation looks, much like English 'the overall picture'."),
    (1, None, "'Everything is fine with us.' 'V poryadke' is literally 'in order', and Russians say it all day long for 'fine' or 'all good'."),
    (2, None, "'We passed all inspections.' 'Proshli' is built on 'pro-', 'through', so to pass a check is literally to go through it. The '-li' ending marks the past for more than one person."),
    (3, None, "'How did you pass the inspections?' The inspector simply puts 'kak', 'how', in front of Vika's own words. Russian needs no 'did' to make a question."),
    (4, None, "'You have no fire extinguishers in the kitchen.' After 'net', 'there is no', the missing thing changes its ending: 'ognetushitel' becomes 'ognetushiteley', 'no extinguishers'."),
    (5, None, "'We have one.' 'Est', 'there is', is the opposite of 'net' in the line before, so 'u nas est' means 'at us there is', or 'we have'."),
    (6, None, "'It is hanging in the back room.' 'Podsobka' is the storeroom behind a shop or kitchen. After 'v', 'in', it becomes 'v podsobke', the ending for where something is."),
    (7, None, "'It must hang within three meters.' 'Dolzhen', 'must', matches the thing it talks about: 'dolzhen' for the extinguisher, which is masculine, and 'dolzhna' for anything feminine."),
    (8, None, "'From the place of a possible fire.' 'Ot', 'from', changes 'mesto', 'place', into 'mesta'. 'Pozhar' is a fire that destroys buildings, as opposed to 'ogon', plain fire or flame."),
    (9, None, "'This is not a problem.' 'Eto', 'this', needs no 'is' after it, so 'eto ne problema' is word for word 'this not problem'."),
    (10, None, "'This is a very big problem.' 'Bolshaya' ends in '-aya' because 'problema' is feminine. With a masculine word, such as a key, it would be 'bolshoy klyuch'."),
    (11, None, "'Oh, how bad everything is.' 'Kak vsyo plokho' is a stock groan, 'how bad it all is'. 'Plokho' has no '-aya' ending here because it describes how things stand, not one particular thing."),
    (12, None, "'I give you two days for correction.' After 'dva', 'two', the word for day changes: 'den' becomes 'dnya', so 'two days' is 'dva dnya'."),
    (13, None, "'We will do everything.' 'Sdelaem' looks like a present-tense form, but the 's-' at the front makes it one finished job, so it points to the future. Without it, 'delaem' means 'we are doing'."),
]
