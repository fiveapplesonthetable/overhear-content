# Authoring module for kukhnya-s01e13-scene-21.
ID = 'kukhnya-s01e13-scene-21'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 21
TITLE = 'Разбитая машина  (The Crashed Car)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = 'Elena has found her car, and it is not in one piece. She stands next to it, assessing the damage while Barinov tries to talk her out of calling the police. First, the Russian.'
OPENER = 'Taking the damage report again, bit by bit.'
TRANSITION = 'Now the damage report, all together.'
OUTRO = "Elena says she will think about it, and that is all Barinov gets. 'Trying to help' and 'making things worse' make a pair worth keeping. Until the next one."
CLOSING = ('elena', 'Пока!')
STORY = [
    ('elena', 'Ну что, бампера нет...', 'Well, the bumper is gone...', [(291, 'что')], ''),
    ('elena', 'и фара разбита.', 'and the headlight is smashed.', [], ''),
    ('elena', 'Я в порядке, не я была за рулем.', 'I am fine. I was not driving.', [], ''),
    ('elena', 'Это длинная история...', 'It is a long story...', [], ''),
    ('elena', 'потом расскажу, ладно?', 'I will tell you later, okay?', [], ''),
    ('elena', 'Все, давай, пока.', 'All right, bye.', [(288, 'все')], ''),
    ('barinov', 'Да вы не переживайте, я все починю.', 'Do not worry, I will fix everything.', [(289, 'переживайте')], ''),
    ('barinov', 'Просто хотел как лучше.', 'I was only trying to help.', [(290, 'просто')], ''),
    ('elena', 'Я представляю, что бы было...', 'I can imagine what you would have done...', [(291, 'представляю')], ''),
    ('elena', 'если бы вы захотели как хуже.', 'if you meant to make things worse.', [(291, 'если')], ''),
    ('elena', 'Вы вообще понимаете...', 'Do you realize...', [(292, 'вообще')], ''),
    ('elena', 'что я могу написать заявление?', 'I could file a complaint?', [(291, 'что')], ''),
    ('elena', 'И вашего повара посадят.', 'And your chef could go to prison.', [(293, 'вашего')], ''),
    ('barinov', 'Понимаю.', 'I understand.', [(294, 'понимаю')], ''),
    ('barinov', 'Может быть, обойдемся без заявления?', 'Maybe we can settle this without a complaint?', [(295, 'может')], ''),
    ('elena', 'Я подумаю.', 'I will think about it.', [(296, 'подумаю')], ''),
]
WALK = [
    (0, None, ["'Well, the bumper is gone...' Russian says the bumper is missing, and the bumper changes to ", ('elena', 'бампера'), ' after ', ('elena', 'нет'), ". That negating word stands for 'there is not'."]),
    (1, None, ["'and the headlight is smashed.' Now let's consider this line: ", ('elena', 'фара'), ' is a car headlight. ', ('elena', 'разбита'), " is 'smashed', with an 'a' to match the headlight."]),
    (2, None, ["'I am fine. I was not driving.' Now let's focus on the sentence: ", ('elena', 'в'), ('elena', 'порядке'), ", meaning 'in order', stands for 'fine'. ", ('elena', 'за'), ('elena', 'рулем'), ', behind the wheel, is the standard way to say who was driving.']),
    (3, None, ["'It is a long story...' Now we can look at this part: ", ('elena', 'история'), " means 'story' and 'history', so you could use it for a school subject as well. ", ('elena', 'длинная'), ' has an ending to match the story.']),
    (4, None, ["'I will tell you later, okay?' The 'okay' is the particle ", ('elena', 'ладно'), ', which Russians use all the time. ', ('elena', 'расскажу'), ', I will tell, is a future action with no extra word.']),
    (5, None, ["'All right, bye.' We can focus on this part: ", ('elena', 'Все'), ', ', ('elena', 'давай'), ', ', ('elena', 'пока'), " is a chain of little words that Russians use to end a phone call. The last word is a casual 'bye'."]),
    (6, None, ["'Do not worry, I will fix everything.' The polite 'do not worry', ", ('barinov', 'не'), ('barinov', 'переживайте'), ', ends with a polite sound. ', ('barinov', 'починю'), ', I will fix, is from the same action as the one used earlier in the kitchen.']),
    (7, None, ["'I was only trying to help.' We will examine this line: ", ('barinov', 'хотел'), ('barinov', 'как'), ('barinov', 'лучше'), " is 'wanted as better', a famous phrase for good intentions. People often finish it with 'but it turned out as always'."]),
    (8, None, ["'I can imagine what you would have done...' The short term ", ('elena', 'бы'), " means 'would'. It turns 'what was' into 'what would have been'."]),
    (9, None, ["'if you meant to make things worse.' She plays on his phrase: ", ('elena', 'как'), ('elena', 'хуже'), " is 'as worse', the opposite of his 'trying to help'. ", ('elena', 'захотели'), " is 'you wanted'."]),
    (10, None, ["'Do you realize...' Let's examine the dialogue: ", ('elena', 'Вы'), ('elena', 'вообще'), ('elena', 'понимаете'), " is 'do you even understand', with the middle word adding the edge, as it did in the kitchen."]),
    (11, None, ["'that I could file a complaint?' Russians say ", ('elena', 'написать'), ('elena', 'заявление'), ", writing a statement, where English says 'file a complaint'. It is the thing you do at a police desk."]),
    (12, None, ["'And your chef could go to prison.' English says 'go to prison', and Russian says ", ('elena', 'посадят'), ", meaning 'they will seat'. The same action also means 'sit someone down' and 'plant a tree'."]),
    (13, None, ["'I understand.' One word, ", ('barinov', 'Понимаю'), '. Barinov is, for once, brief.']),
    (14, None, ["'Maybe we can settle this without a complaint?' We will analyze this part: ", ('barinov', 'без'), " makes the next word change its ending, so 'complaint' turns into ", ('barinov', 'заявления'), '. ', ('barinov', 'обойдемся'), ", we will manage, reads 'we will go around'."]),
    (15, None, ["'I will think about it.' It is a polite way of not saying yes. The prefix in ", ('elena', 'подумаю'), " means 'for a while'."]),
]
