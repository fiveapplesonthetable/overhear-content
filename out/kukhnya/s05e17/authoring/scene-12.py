# Authoring module for kukhnya-s05e17-scene-12.
ID = 'kukhnya-s05e17-scene-12'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 17
SCENE = 12
TITLE = 'Все предродовые заняты  (All Delivery Rooms Are Full)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'doctor': 'Врач', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.17'
SOURCE_FILE = 'sources/kukhnya/s05/e17.ru.srt'
INTRO = 'While Chef Barinov discovers that his kitchen oven has completely died and Mikhail has vanished, Max and Vika arrive at the maternity hospital only to be given a gurney in the hallway.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Determined to find Vika a proper room, Max searches the maternity floor while Vika rests. See you next time!'
CLOSING = ('max', 'Всего хорошего!')
STORY = [
    ('max', 'Нам отдельная палата сейчас нужна.', 'We need a private room right now.', [(229, 'Нам палата нужна')], 'adapted'),
    ('max', 'Нам не нужна экскурсия по роддому.', 'We do not need a tour of the maternity hospital.', [(229, 'а не экскурсия по роддому')], 'adapted'),
    ('doctor', 'Молодой человек, не хамите, вот палата.', 'Young man, do not be rude, here is your ward.', [(230, 'Молодой человек, не хамите. Вот ваша палата')], 'adapted'),
    ('max', 'Вы просто издеваетесь над нами?', 'Are you simply mocking us?', [(231, 'Издеваетесь')], 'adapted'),
    ('doctor', 'Сейчас все предродовые палаты заняты.', 'Right now all pre-delivery rooms are occupied.', [(231, 'Все предродовые заняты')], 'adapted'),
    ('max', 'Моя жена не будет лежать в коридоре.', 'My wife will not lie in the corridor.', [(233, 'Моя жена не будет лежать в коридоре')], 'adapted'),
    ('max', 'Позовите сюда главврача, пожалуйста.', 'Call the head doctor here, please.', [(234, 'Позовите главврача, пожалуйста')], 'adapted'),
    ('doctor', 'Он сейчас сложные роды принимает.', 'He is delivering a difficult birth right now.', [(235, 'Он роды принимает')], 'adapted'),
    ('doctor', 'Сегодня половина Москвы у нас рожает.', 'Half of Moscow is giving birth here today.', [(235, 'сегодня рожает')], 'adapted'),
    ('vika', 'Макс, прости меня за утро.', 'Max, forgive me for this morning.', [(237, 'Прости')], 'adapted'),
    ('max', 'Давай я тебе сейчас помогу.', 'Let me help you right now.', [(238, 'Давай, я тебе помогу')], 'adapted'),
    ('vika', 'Спасибо тебе большое, родной.', 'Thank you so much, my dear.', [(239, 'Спасибо')], 'adapted'),
]
WALK = [
    (0, None, "'We need a private room right now.' Needing a private room right now moves the conversation forward without extra drama."),
    (1, None, "'We do not need a tour of the maternity hospital.' Even though they do not need a tour of the maternity hospital, Max keeps a steady face in front of the doctor."),
    (2, None, "'Young man, do not be rude, here is your ward.' Admitting that young man do not be rude here is Max's ward shows the doctor being honest for a change."),
    (3, None, '\'Are you simply mocking us?\' By checking whether the doctor simply mocking them, Max presses the doctor for a straight answer. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (4, None, "'Right now all pre-delivery rooms are occupied.' Once right now all delivery rooms are occupied, the doctor can finally tell Max what he means."),
    (5, None, "'My wife will not lie in the corridor.' Adding that his wife will not lie in the corridor fills in the missing piece for the doctor."),
    (6, None, "'Call the head doctor here, please.' Adding that the doctor should call the head doctor here please fills in the missing piece for the doctor."),
    (7, None, "'He is delivering a difficult birth right now.' The doctor reminds Max that he is delivering a difficult birth right now before the moment passes."),
    (8, None, '\'Half of Moscow is giving birth here today.\' Mentioning that half of Moscow is giving birth here today moves the talk in a new direction. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (9, None, "'Max, forgive me for this morning.' Around the work and hospital, Vika sets a calm, everyday tone with the doctor."),
    (10, None, "'Let me help you right now.' Here telling the doctor to let him help the doctor right now sets up the next turn in their exchange."),
    (11, None, '\'Thank you so much, my dear.\' Between the point and the hospital, Vika gives the doctor a quick, grounded response. Speaking with the close, informal "you" strips away any polite distance between them.'),
]
