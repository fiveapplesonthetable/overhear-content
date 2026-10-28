# Authoring module for kukhnya-s03e01-scene-04.
ID = 'kukhnya-s03e01-scene-04'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 1
SCENE = 4
TITLE = 'Конная прогулка  (The Horseback Ride)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.01'
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'
INTRO = 'Meanwhile in the corridor, Kostya asks Nastya what her parents said about her pregnancy, only to learn she is still hiding the news from her father. Listen to the full conversation in Russian first, and then we will walk through every line together.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "That concludes the corridor conversation. Listen for Kostya's disbelief when Nastya has to turn down her father's horseback riding invitation. See you next time!"
CLOSING = ('kostya', 'Всего хорошего!')
STORY = [
    ('kostya', 'Что твои родители сказали?', 'What did your parents say?', [(49, 'Что твои родители сказали')], ''),
    ('nastya', 'Да так, ничего.', 'Oh, nothing much.', [(50, 'Да так, ничего')], ''),
    ('nastya', 'Я ещё не сказала.', "I haven't told them yet.", [(51, 'Я еще не сказала')], ''),
    ('kostya', 'Когда скажешь?', 'When will you tell them?', [(52, 'Когда скажешь')], ''),
    ('max', 'Шеф, будете искать молекулярного повара?', 'Chef, will you look for a molecular cook?', [(53, 'шеф, будете искать молекулярного повара')], 'adapted'),
    ('max', 'Все равно ты пойдешь со мной.', 'You will go out with me anyway.', [(56, 'Все равно ты пойдешь со мной')], 'adapted'),
    ('nastya', 'Завтра скажу.', 'I will tell them tomorrow.', [(57, 'Завтра скажу')], ''),
    ('nastya', 'Нет, папа, я не могу.', 'No, Dad, I cannot.', [(58, 'я не могу')], 'adapted'),
    ('nastya', 'Я уже брала выходные.', 'I already took days off.', [(59, 'Я уже брала выходные')], ''),
    ('nastya', 'Я не поеду на конную прогулку.', 'I am not going on a horseback ride.', [(60, 'я не поеду с тобой на конную прогулку')], 'adapted'),
    ('nastya', 'Все, ладно, мне пора. Пока.', 'Alright, I have to go. Bye.', [(61, 'Все, ладно, мне пора. Пока')], ''),
    ('kostya', 'Настя, какая конная прогулка?', 'Nastya, what horseback ride?', [(62, 'Настя, какая конная прогулка')], ''),
]
WALK = [
    (0, None, "'What did your parents say?' Wondering what Max's parents say cuts straight through the tension between Kostya and Max."),
    (1, None, "'Oh, nothing much.' Between the shift and the news, Nastya gives Kostya a quick, grounded response."),
    (2, None, "'I haven't told them yet.' Admitting that she has not told them yet shows Nastya being honest for a change."),
    (3, None, "'When will you tell them?' By wondering when Max tells them will, Kostya presses Max for a straight answer."),
    (4, None, '\'Chef, will you look for a molecular cook?\' Asking whether Kostya looks for a molecular cook cuts straight through the tension between Max and Kostya. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (5, None, '\'You will go out with me anyway.\' Mentioning that Kostya will go out with him anyway moves the talk in a new direction. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (6, None, "'I will tell them tomorrow.' Nastya reminds Kostya that she will tell them tomorrow before the moment passes."),
    (7, None, "'No, Dad, I cannot.' Because dad she cannot, Nastya treats the matter as settled."),
    (8, None, "'I already took days off.' Explaining that she already took days off lays the cards on the table for Kostya."),
    (9, None, "'I am not going on a horseback ride.' Here being not going on a horseback ride sets up the next turn in their exchange."),
    (10, None, "'Alright, I have to go. Bye.' Claiming that Alright she has to go sounds confident, even if Kostya has doubts. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (11, None, '\'Nastya, what horseback ride?\' Around the call and phone, Kostya wants to know where Max really stands. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
]
