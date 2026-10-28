# Authoring module for domashniy-arest-s01e11-scene-31.
ID = 'domashniy-arest-s01e11-scene-31'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 11
SCENE = 31
TITLE = 'Электронный браслет  (The Ankle Monitor)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'officer': 'Офицер'}
SOURCE_NAME = 'Домашний арест, Сезон 1, Эпизод 11'
SOURCE_FILE = 'sources/domashniy-arest/s01/e11.ru.dual.srt'
INTRO = 'Following his sudden return from freedom, former mayor Arkady Borisovich is escorted back to the communal apartment. An enforcement officer attaches the electronic tracking bracelet to his ankle, formally re-establishing house arrest.'
OPENER = "Let's examine how the officer reinstates Arkady's electronic house arrest."
TRANSITION = "Now let's listen to the formal electronic tagging procedure once more."
OUTRO = 'With the electronic cuff secured around his ankle, Arkady returns to his familiar confinement. See you next time!'
CLOSING = ('officer', 'Пока!')
STORY = [
    ('officer', 'Аркадий Борисович, приготовьтесь к процедуре.', 'Arkady Borisovich, prepare for the procedure.', [], 'formal address'),
    ('arkady', 'Я готов, проходите в коридор.', 'I am ready, come into the hallway.', [], "Arkady's compliance"),
    ('officer', 'Это обязательная техническая процедура.', 'This is a mandatory technical procedure.', [], 'adapted cue'),
    ('arkady', 'Я уже носил этот электронный браслет.', 'I already wore this electronic bracelet.', [], "Arkady's reminder"),
    ('officer', 'Мы должны зафиксировать датчик на ноге.', 'We must fasten the sensor on your leg.', [], "officer's instruction"),
    ('arkady', 'Пожалуйста, не затягивайте ремень слишком сильно.', 'Please do not tighten the strap too tightly.', [], "Arkady's polite request"),
    ('officer', 'Всё готово, электронный браслет работает.', 'Everything is ready, the electronic bracelet is working.', [(920, 'Браслет работает.')], 'adapted cue'),
    ('officer', 'Дальше вы всё прекрасно знаете сами.', 'You know everything very well yourself from here.', [(921, 'Дальше вы знаете.')], 'adapted cue'),
    ('arkady', 'Я помню все установленные законом правила.', 'I remember all the rules established by law.', [], "Arkady's assurance"),
    ('officer', 'Вам строго запрещено покидать эту квартиру.', 'You are strictly forbidden from leaving this apartment.', [], 'official warning'),
    ('arkady', 'Я буду сидеть дома и ждать суда.', 'I will sit at home and wait for the trial.', [], "Arkady's resignation"),
    ('officer', 'Любое нарушение сигнала фиксируется немедленно.', 'Any breach of signal is recorded immediately.', [], 'enforcement rule'),
    ('arkady', 'Я не собираюсь никуда убегать.', 'I do not intend to run away anywhere.', [], "Arkady's commitment"),
    ('officer', 'Тогда соблюдайте режим и не нарушайте.', 'Then observe the regime and do not violate.', [], "officer's farewell"),
]
WALK = [
    (0, None, "'Arkady Borisovich, prepare for the procedure.' Even while strapping an ankle monitor back onto him, the officer uses the formal name and patronymic."),
    (1, None, "'I am ready, come into the hallway.' Arkady holds out his leg without a fuss—he knows the drill by heart now."),
    (2, None, "'This is a mandatory technical procedure.' Bureaucratic language makes locking a man in a communal flat sound like routine maintenance."),
    (3, None, "'I already wore this electronic bracelet.' Only a few hours ago he was celebrating taking that very cuff off."),
    (4, None, "'We must fasten the sensor on your leg.' Snapping the plastic strap shut officially ends Arkady's brief taste of freedom."),
    (5, None, "'Please do not tighten the strap too tightly.' Stripped of his millions, the one thing he can still negotiate is a little room around his ankle."),
    (6, None, "'Everything is ready, the electronic bracelet is working.' A blinking light confirms he is back on the federal map."),
    (7, None, "'You know everything very well yourself from here.' Since this is his second round under house arrest, the officer skips the standard lecture."),
    (8, None, "'I remember all the rules established by law.' Hearing a career crook recite his respect for the law has a dry irony to it."),
    (9, None, "'You are strictly forbidden from leaving this apartment.' Cross the front threshold again, and the next stop is a real prison cell."),
    (10, None, "'I will sit at home and wait for the trial.' Remember that double meaning of \"sidet\" in Russian: both \"sit at home\" and \"do time\"."),
    (11, None, "'Any breach of signal is recorded immediately.' One bad signal from the ankle cuff brings a squad car straight to the courtyard."),
    (12, None, "'I do not intend to run away anywhere.' With no passport and no cash left, he has nowhere to run anyway."),
    (13, None, "'Then observe the regime and do not violate.' With that standard parting warning, the officer leaves Arkady to his neighbors."),
]
