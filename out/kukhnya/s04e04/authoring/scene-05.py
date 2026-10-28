# Authoring module for kukhnya-s04e04-scene-05.
ID = 'kukhnya-s04e04-scene-05'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 4
SCENE = 5
TITLE = 'Дудка из морковки  (The Carrot Flute)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'german': 'Герман', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.04'
SOURCE_FILE = 'sources/kukhnya/s04/e04.ru.srt'
INTRO = 'In the storage room of Claude Monet, German Mikhailovich hears music and finds Denis playing a handmade flute carved out of a carrot, leading to an immediate disciplinary task. Listen to their exchange in Russian.'
OPENER = "Let's break this conversation down line by line."
TRANSITION = 'Now listen to the full Russian exchange again with everything in place.'
OUTRO = 'That completes German catching Denis with the carrot flute and assigning him two sacks of potatoes. Notice how Russian expresses deadlines with prepositions. Until next time!'
CLOSING = ('denis', 'До завтра!')
STORY = [
    ('german', 'Простите, пожалуйста, что такое?', 'Excuse me, please, what is this?', [(67, 'Простите, пожалуйста, что такое?')], ''),
    ('german', 'Поразительно. Это вы сами сделали? Из морковки?', 'Astonishing. Did you make this yourself? Out of a carrot?', [(68, 'Поразительно. Это вы сами сделали?'), (69, 'Из морковки?')], ''),
    ('denis', 'Да. Спасибо.', 'Yes. Thank you.', [(69, 'Да.'), (71, 'Спасибо.')], ''),
    ('german', 'Всю морковку почистили, ещё дудку сделали. Молодец.', 'You peeled all the carrots and even made a flute. Well done.', [(74, 'Всю морковку почистили, еще'), (74, 'сделали.'), (75, 'Молодец.')], ''),
    ('german', 'Вам не составит большого труда почистить мешок картошки.', 'It will not be much trouble for you to peel a sack of potatoes.', [(76, 'вам...'), (77, 'не составит большого труда почистить мешок картошки.')], ''),
    ('german', 'Вам лучше два. Два мешка. До вечера справитесь?', 'Better make it two for you. Two sacks. Will you manage by evening?', [(79, 'Вам лучше два.'), (80, 'Два мешка. До вечера справитесь?')], ''),
    ('denis', 'Шеф, я до вечера не успею.', "Chef, I won't finish in time by evening.", [(81, 'Шеф, я до вечера не успею.')], ''),
    ('german', 'Успеете. Вы очень талантливы.', 'You will finish in time. You are very talented.', [(81, 'Успеете.'), (82, 'Вы очень талантливы.')], ''),
    ('german', 'А не успеете — пойдёте вон.', "And if you don't finish in time, out you go.", [(83, 'А не успеете,'), (83, 'вон.')], ''),
    ('lyova', 'Герман Михайлович, а для чего нам нужно столько картошки?', 'German Mikhailovich, why do we need so many potatoes?', [(85, 'Герман Михайлович, а для чего нам нужно столько картошки?')], ''),
    ('german', 'В целях воспитания. Тунеядства я не потерплю.', 'For educational purposes. I will not tolerate slacking.', [(87, 'В целях воспитания.'), (88, 'я не потерплю.')], ''),
    ('lyova', 'Мне тоже не нравится.', 'I do not like this either.', [(89, 'Мне тоже не нравится.')], ''),
]
WALK = [
    (0, None, '\'Excuse me, please, what is this?\' Over the shift and the exchange, German presses Denis for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (1, None, '\'Astonishing. Did you make this yourself? Out of a carrot?\' Asking whether Denis makes this themselves is how German puts Denis on the spot. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (2, None, "'Yes. Thank you.' Here telling German to thank German sets up the next turn in their exchange."),
    (3, None, "'You peeled all the carrots and even made a flute. Well done.' Realizing that Denis peeled all the carrots and even made a flute changes how German handles the situation."),
    (4, None, '\'It will not be much trouble for you to peel a sack of potatoes.\' Noting that it will not be much trouble for Denis to peel a sack of potatoes keeps German\'s side of the story simple and clear. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (5, None, "'Better make it two for you. Two sacks. Will you manage by evening?' With the moment and exchange hanging in the air, German puts Denis on the spot."),
    (6, None, "'Chef, I won't finish in time by evening.' Admitting that he will not finish in time by evening shows Denis being honest for a change."),
    (7, None, '\'You will finish in time. You are very talented.\' Saying that Denis will finish in time is how German sets the tone with Denis. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (8, None, "'And if you don't finish in time, out you go.' Once if Denis does not finish in time out Denis goes, German can finally tell Denis what he means."),
    (9, None, "'German Mikhailovich, why do we need so many potatoes?' Asking why they need so many potatoes is how Lyova puts Denis on the spot. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (10, None, "'For educational purposes. I will not tolerate slacking.' With the work and exchange in play, German keeps this short reply brisk and direct."),
    (11, None, "'I do not like this either.' Since he does not like this either, Lyova does not waste words on excuses."),
]
