# Authoring module for kukhnya-s01e13-scene-19.
ID = 'kukhnya-s01e13-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 19
TITLE = 'Угнанная машина  (The Stolen Car)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена', 'fedya': 'Федя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Elena's car has disappeared from its place, and she storms into Barinov's kitchen to ask where it is. Barinov turns to Fedya for an answer. The Russian comes first."
OPENER = 'Line by line, to watch the plot come out.'
TRANSITION = 'Here is the whole hunt again.'
OUTRO = "So that is where the car went. Fedya took it, and Barinov's only question is about the mirror. More soon."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Постучаться не учили?', "Didn't they teach you to knock?", [], ''),
    ('elena', 'Я звоню в полицию.', 'I am calling the police.', [], ''),
    ('elena', 'Где моя машина?', 'Where is my car?', [], ''),
    ('barinov', 'Понятия не имею.', 'I have no idea.', [], ''),
    ('elena', 'Значит так, мне все это надоело.', 'That is it. I have had enough.', [(272, 'так')], ''),
    ('elena', 'Если через пять минут...', 'If in five minutes...', [(259, 'если')], ''),
    ('elena', 'моей машины не будет на месте...', 'my car is not back...', [(259, 'моей')], ''),
    ('elena', 'я заявляю об угоне.', 'I am reporting it stolen.', [(259, 'заявляю')], ''),
    ('elena', 'Вы меня хорошо поняли?', 'Do you understand me?', [(260, 'меня')], ''),
    ('elena', 'Все.', 'That is all.', [(260, 'все')], ''),
    ('barinov', 'Перед тем, как я тебя убью...', 'Before I kill you...', [(261, 'перед')], ''),
    ('barinov', 'ответь мне на вопрос.', 'answer one question.', [(261, 'ответь')], ''),
    ('barinov', 'Ты зачем увез машину?', 'Why did you take the car?', [(262, 'зачем')], ''),
    ('fedya', 'Шеф, у него не получилось приехать.', 'Boss, he could not make it.', [(262, 'шеф')], ''),
    ('fedya', 'Он сказал, чтобы я машину привез.', 'He told me to bring the car.', [(262, 'сказал')], ''),
    ('barinov', 'Как ты ее вообще завел?', 'How did you even start it?', [(261, 'как')], ''),
    ('fedya', 'Ну, чем открыл, тем и завел.', 'Well, whatever I used to unlock it, I used to start it.', [(264, 'чем')], ''),
    ('barinov', 'Ты зеркало починил?', 'Did you fix the mirror?', [(266, 'зеркало')], ''),
]
WALK = [
    (0, None, ["'Didn't they teach you to knock?' We can inspect the dialogue: ", ('barinov', 'Постучаться'), ' is to knock in the sense of knocking to be let in, and it is the usual Russian verb for knocking at a door. ', ('barinov', 'не'), ('barinov', 'учили'), " is didn't they teach, with nobody named."]),
    (1, None, ["'I am calling the police.' We will break down the sentence: ", ('elena', 'звоню'), ('elena', 'в'), ('elena', 'полицию'), ' is I phone to the police, with the direction preposition and ending.']),
    (2, None, ["'Where is my car?' Car is feminine, so Elena says ", ('elena', 'моя'), ', not the masculine form. Nobody bothers with an is in a question like this.']),
    (3, None, ["'I have no idea.' Now we can examine this line: ", ('barinov', 'Понятия'), ('barinov', 'не'), ('barinov', 'имею'), ' is a set phrase, saying idea I do not have. Russians say it all the time.']),
    (4, None, ["'That is it. I have had enough.' We can break down the phrase: ", ('elena', 'Значит'), ('elena', 'так'), ' is a brisk right, so. ', ('elena', 'надоело'), ' is neuter, it has bored, and ', ('elena', 'мне'), ' is to me, so she is saying she is sick of it all.']),
    (5, None, ["'If in five minutes...' The sentence stops in the middle, and the three dots show it. Elena lets the threat hang on the term ", ('elena', 'Если'), ', if, and carries on in the next line.']),
    (6, None, ["'my car is not back...' Now let's look at this part: ", ('elena', 'не'), ('elena', 'будет'), ' with the thing after it means will not be there. ', ('elena', 'моей'), ('elena', 'машины'), ' is of my car, so it means there will be no car of mine.']),
    (7, None, ["'I am reporting it stolen.' We will inspect this line: ", ('elena', 'заявляю'), ' is I declare or I report. ', ('elena', 'об'), ('elena', 'угоне'), ' is about the theft, a term used only for stolen vehicles.']),
    (8, None, ["'Do you understand me?' We will break down the speech: ", ('elena', 'поняли'), ' marks the polite plural, did you understand. ', ('elena', 'хорошо'), ' is well.']),
    (9, None, ["'That is all.' One word, ", ('elena', 'Все'), ', which Russians say to end a conversation. It is clear and firm.']),
    (10, None, ["'Before I kill you...' We can inspect this part: ", ('barinov', 'Перед'), ('barinov', 'тем'), ', ', ('barinov', 'как'), ' is a set expression for before. ', ('barinov', 'убью'), ' is I will kill, and it is a threat people make without meaning it.']),
    (11, None, ["'answer one question.' The order to answer wants on, so Russians answer on a question. Me becomes to me, ", ('barinov', 'мне'), '.']),
    (12, None, ["'Why did you take the car?' Barinov puts you first, you why took away, which makes it a telling-off. ", ('barinov', 'увез'), ' is the past of to take something away by vehicle, with the prefix meaning away.']),
    (13, None, ["'Boss, he could not make it.' We will focus on the speech: ", ('fedya', 'у'), ('fedya', 'него'), ('fedya', 'не'), ('fedya', 'получилось'), ' is with him it did not work out. ', ('fedya', 'приехать'), ' is to arrive by vehicle.']),
    (14, None, ["'He told me to bring the car.' Let us inspect the words: ", ('fedya', 'чтобы'), ' is so that, and Russian puts the following action in the past, so that I should bring. ', ('fedya', 'привез'), ' means bring by vehicle.']),
    (15, None, ["'How did you even start it?' Let us examine the phrase: ", ('barinov', 'завел'), ' is started, the verb for getting an engine going. At all, ', ('barinov', 'вообще'), ', here works like even.']),
    (16, None, ["'Well, whatever I used to unlock it, I used to start it.' Let's examine the dialogue: ", ('fedya', 'чем'), ' means with what and ', ('fedya', 'тем'), ' means with that, so with what I opened, with that I started. It is a clever, short way to dodge the question.']),
    (17, None, ["'Did you fix the mirror?' Now let's inspect this line: ", ('barinov', 'починил'), ' is fixed or mended. Barinov has the mirror, ', ('barinov', 'зеркало'), ', before the verb, the thing he cares about first.']),
]
