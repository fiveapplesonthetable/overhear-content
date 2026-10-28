# Authoring module for kukhnya-s04e09-scene-07.
ID = 'kukhnya-s04e09-scene-07'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 9
SCENE = 7
TITLE = 'Разговор окончен  (Conversation Over)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'german': 'Герман', 'kostya': 'Костя'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.09'
SOURCE_FILE = 'sources/kukhnya/s04/e09.ru.srt'
INTRO = "German storms into Chef Barinov's new kitchen at Arcobaleno to reclaim the copper sauté pan and reminds Viktor that he cannot afford any new trouble with the police."
OPENER = "Let's step through the confrontation between the two rival head chefs."
TRANSITION = "Now let's listen to the whole scene again without interruption."
OUTRO = "Listen for the crisp two-word phrase German uses to shut down the argument — 'conversation finished'. Until next time!"
CLOSING = ('german', 'Хорошего дня!')
STORY = [
    ('barinov', 'Никакая это не кража.', 'This is no theft at all.', [(82, 'Никакая это не кража')], ''),
    ('barinov', 'Я забрал свой сотейник.', 'I took back my own sauté pan.', [(83, 'Я забрал свой сотейник')], ''),
    ('barinov', 'Я эту сковородку купил во Франции.', 'I bought this pan in France.', [(84, 'Я эту сковородку когда-то купил во Франции')], 'adapted for A1 clarity'),
    ('german', 'Теперь я шеф-повар в ресторане.', 'Now I am the head chef at the restaurant.', [(85, 'как я стал шеф-поваром')], 'adapted for A1 clarity'),
    ('german', 'Всё на кухне теперь моё.', 'Everything in the kitchen is mine now.', [(86, 'что находится на кухне')], 'adapted for A1 clarity'),
    ('german', 'Я хочу его вернуть.', 'I want to get it back.', [(87, 'Я хочу его вернуть')], ''),
    ('german', 'Разговор окончен.', 'The conversation is over.', [(87, 'разговор окончен')], ''),
    ('german', 'На вашем месте я бы не спорил.', 'In your place, I would not argue.', [(88, 'на вашем месте я бы сейчас не спорил')], 'adapted for A1 clarity'),
    ('german', 'Вам не нужны проблемы с полицией.', 'You do not need problems with the police.', [(89, 'вам не нужны проблемы с полицией')], ''),
    ('kostya', 'Алло, Макс, привет, как вы там?', 'Hello, Max, hi, how are you doing there?', [(91, 'Алло, Макс, привет. Ну, как вы там')], 'adapted for A1 clarity'),
    ('kostya', 'Как Стёпка, да всё хорошо?', 'How is Styopa, is everything good?', [(92, 'Как Степка? Да, все хорошо')], ''),
    ('barinov', 'Стёпка в порядке, он уснул.', 'Styopa is fine, he fell asleep.', [(93, 'Степка в порядке')], 'adapted for A1 clarity'),
    ('kostya', 'Странно, он обычно не спит сейчас.', 'Strange, he usually does not sleep right now.', [(95, 'Странно, он обычно не спит')], 'adapted for A1 clarity'),
    ('kostya', 'Ты, главное, не переживай.', 'Above all, do not worry.', [(98, 'Ты, главное, не переживай')], ''),
]
WALK = [
    (0, None, "'This is no theft at all.' Because this is no theft at all, Barinov treats the matter as settled."),
    (1, None, "'I took back my own sauté pan.' Explaining that he took back his own pan lays the cards on the table for German."),
    (2, None, "'I bought this pan in France.' Barinov mentions that he bought this pan in France so German sees what is at stake."),
    (3, None, "'Now I am the head chef at the restaurant.' By being the head at the restaurant, German keeps his side of the story grounded."),
    (4, None, "'Everything in the kitchen is mine now.' Explaining that everything in the kitchen is his now lays the cards on the table for Barinov."),
    (5, None, "'I want to get it back.' Here wanting to get it back sets up the next turn in their exchange."),
    (6, None, "'The conversation is over.' Realizing that the conversation is changes how German handles the situation."),
    (7, None, "'In your place, I would not argue.' Noting that in Barinov's place he would not argue keeps German's side of the story simple and clear."),
    (8, None, '\'You do not need problems with the police.\' Noting that Barinov does not need problems with the police keeps German\'s side of the story simple and clear. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (9, None, "'Hello, Max, hi, how are you doing there?' Here wondering how Barinov doing there is shows Kostya looking for the real truth."),
    (10, None, '\'How is Styopa, is everything good?\' By asking how Styopa is everything good is, Kostya presses Barinov for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (11, None, "'Styopa is fine, he fell asleep.' Once Styopa is fine he fell asleep, Barinov can finally tell German what he means."),
    (12, None, "'Strange, he usually does not sleep right now.' Adding that strange he usually does not sleep right now fills in the missing piece for Barinov."),
    (13, None, '\'Above all, do not worry.\' Kostya tells Barinov that above all do not worry without dressing it up. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
]
