# Authoring module for kukhnya-s01e08-scene-04.
ID = 'kukhnya-s01e08-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 4
TITLE = 'Смелое пари  (A Bold Bet)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Still in the studio and still live on camera, Elena Sokolova has heard enough from Barinov. She turns his insults into a bet: she will work a full shift in his kitchen at Claude Monet, and if she lasts, he pays for dinner. It's in Russian first."
OPENER = "Let's go back through the challenge. Elena sounds calm, and Barinov sounds very sure of himself."
TRANSITION = 'Now the whole bet again, start to finish.'
OUTRO = "A bet in Russian needs only a few words: davayte posporim, 'let's bet', dogovorilis, 'agreed', and a few svideteli, 'witnesses'. You've now heard all of them. See you next time."
CLOSING = ('elena', 'Пока!')
STORY = [
    ('elena', 'Виктор, вы ведёте себя очень грубо!', 'Viktor, you are behaving very rudely!', [(32, 'Вы какой-то женоненавистник')], ''),
    ('barinov', 'Я прекрасно отношусь ко всем женщинам.', 'I treat all women wonderfully.', [(33, 'Я прекрасно отношусь к женщинам'), (34, 'Я вообще люблю женщин')], ''),
    ('elena', 'Тогда почему вы так обижаете меня?', 'Then why do you insult me like that?', [], ''),
    ('barinov', 'Вы не сможете работать целый день.', 'You will not be able to work a whole day.', [(37, 'вы, например, на моей кухне и дня не продержались бы')], ''),
    ('elena', 'А давайте поспорим прямо сейчас!', 'Then let us bet right now!', [(38, 'А давайте заключим пари')], ''),
    ('barinov', 'О чём вы хотите спорить со мной?', 'What do you want to bet about with me?', [], ''),
    ('elena', 'Я отработаю полную смену на кухне.', 'I will work a full shift in the kitchen.', [(39, 'Вот если я продержусь на вашей кухне день')], ''),
    ('barinov', 'Мои повара быстро сломают вашу гордость.', 'My cooks will quickly break your pride.', [], ''),
    ('elena', 'Если я справлюсь, вы оплатите ужин!', 'If I cope, you will pay for dinner!', [(39, 'вы приглашайте меня на ужин')], ''),
    ('barinov', 'А если вы сбежите через час?', 'And if you run away after an hour?', [], ''),
    ('elena', 'Тогда вы выиграете наш главный спор.', 'Then you will win our main bet.', [], ''),
    ('barinov', 'Договорились, завтра жду вас на кухне!', 'Agreed, tomorrow I expect you in the kitchen!', [(41, 'Виктор, вы принимаете пари')], ''),
    ('elena', 'Все зрители будут свидетелями нашего спора.', 'All viewers will be witnesses of our bet.', [(40, 'Дорогие друзья, какой неожиданный поворот событий')], ''),
]
WALK = [
    (0, None, ["'Viktor, you are behaving very rudely!' To describe his behavior as rudely, she uses the word ", ('elena', 'грубо'), '.']),
    (1, None, ["'I treat all women wonderfully.' He defends his actions by saying he treats women ", ('barinov', 'прекрасно'), ', meaning wonderfully.']),
    (2, None, ["'Then why do you insult me like that?' She questions his behavior by asking why he ", ('elena', 'обижаете'), ', which means insults.']),
    (3, None, ["'You will not be able to work a whole day.' He doubts her endurance for a ", ('barinov', 'целый'), ' day, meaning a whole day.']),
    (4, None, ["'Then let us bet right now!' She boldly challenges him to bet by saying ", ('elena', 'поспорим'), '.']),
    (5, None, ["'What do you want to bet about with me?' He asks what she wants to ", ('barinov', 'спорить'), ', meaning bet, about.']),
    (6, None, ["'I will work a full shift in the kitchen.' Committing to the challenge, she promises to work a full ", ('elena', 'смену'), ', or shift.']),
    (7, None, ["'My cooks will quickly break your pride.' He confidently predicts his team will break her ", ('barinov', 'гордость'), ', meaning pride.']),
    (8, None, ["'If I cope, you will pay for dinner!' Setting the stakes, she insists he will ", ('elena', 'оплатите'), ', or pay, for dinner.']),
    (9, None, ["'And if you run away after an hour?' Mocking her resolve, he asks what happens if you ", ('barinov', 'сбежите'), ', meaning run away.']),
    (10, None, ["'Then you will win our main bet.' Admitting the risk, she says he might win their main ", ('elena', 'спор'), ', meaning bet.']),
    (11, None, ["'Agreed, tomorrow I expect you in the kitchen!' Accepting the terms, he seals the deal with ", ('barinov', 'Договорились'), ', meaning agreed.']),
    (12, None, ["'All viewers will be witnesses of our bet.' Knowing they are on television, she notes all the ", ('elena', 'зрители'), ', meaning viewers, are witnesses.']),
]