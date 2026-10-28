# Authoring module for domashniy-arest-s01e11-scene-03.
ID = 'domashniy-arest-s01e11-scene-03'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 11
SCENE = 3
TITLE = 'Согласие Нины  (Nina Says Yes)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.11'
SOURCE_FILE = 'sources/domashniy-arest/s01/e11.ru.dual.srt'
INTRO = "In this concluding scene of the nineteen-nineties flashback, Samson continues to wait patiently for Nina. Moved by his stubborn dedication, Nina steps back outside to talk to him once more. When Ivan asks her one last time if her answer might be yes, Nina smiles and accepts his proposal. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine Nina's decision to accept Samson's proposal line by line."
TRANSITION = "Now let's listen to their reconciliation once more without pause."
OUTRO = "Nina accepts Ivan's proposal, marking the beginning of their long and tumultuous marriage. Next comes the opening credits and the satirical theme song. See you next time!"
CLOSING = ('samson', 'Пока!')
STORY = [
    ('samson', 'Нина, ты вернулась ко мне назад?', 'Nina, did you come back to me?', [], 'transition from previous scene'),
    ('nina', 'Ты всё ещё стоишь на холоде.', 'You are still standing in the cold.', [], ''),
    ('samson', 'Я же обещал, что буду ждать.', 'I promised that I would wait.', [], ''),
    ('nina', 'Ты действительно совершенно неисправимый человек.', 'You are truly a completely incorrigible person.', [], ''),
    ('samson', 'Так может быть, всё-таки да?', 'So maybe after all it is yes?', [(54, 'так может все-таки да')], ''),
    ('nina', 'Ну хорошо, может быть и да!', 'Well alright, maybe it is yes!', [(55, 'Может и да')], ''),
    ('samson', 'Ты правда согласна стать моей женой?', 'Are you truly willing to become my wife?', [], ''),
    ('nina', 'Да, я согласна выйти за тебя.', 'Yes, I agree to marry you.', [], ''),
    ('samson', 'Тогда надевай скорее это кольцо!', 'Then put on this ring quickly!', [], ''),
    ('nina', 'Оно действительно очень красивое и блестит.', 'It really is very beautiful and shines.', [], ''),
    ('samson', 'Теперь мы вместе пойдём в ЗАГС.', 'Now we will go to the registry office together.', [], ''),
    ('nina', 'И подадим наше первое общее заявление.', 'And submit our first joint application.', [], ''),
    ('samson', 'Я обещаю быть самым лучшим мужем!', 'I promise to be the very best husband!', [], ''),
]
WALK = [
    (0, None, "'Nina, did you come back to me?' When the door opens again, Samson can hardly believe his sit-in actually worked."),
    (1, None, "'You are still standing in the cold.' She shakes her head at the sight of him shivering on the street."),
    (2, None, "'I promised that I would wait.' For Ivan, keeping his word is everything: he said he would stay, so he stayed."),
    (3, None, "'You are truly a completely incorrigible person.' Calling someone \"incorrigible\" in this tone is really a Russian way of saying \"you're impossible, and I give up\"."),
    (4, None, "'So maybe after all it is yes?' Sensing the opening, he tries his luck one more time. \"Vsyo-taki\" means \"after all\" or \"despite everything\"."),
    (5, None, "'Well alright, maybe it is yes!' She echoes his own \"maybe yes\" right back at him, and the smile gives her away."),
    (6, None, "'Are you truly willing to become my wife?' After being turned down inside the cafe, he needs to hear it stated plainly."),
    (7, None, "'Yes, I agree to marry you.' No more \"maybe\" this time: she gives him the clear yes he waited in the cold for."),
    (8, None, "'Then put on this ring quickly!' He wants that ring on her finger before she has a chance to think twice."),
    (9, None, "'It really is very beautiful and shines.' Once it is out of the pastry and on her hand, the ring actually looks lovely."),
    (10, None, "'Now we will go to the registry office together.' Remember why he picked this cafe in the first place: the registry office is right next door."),
    (11, None, "'And submit our first joint application.' Filing the marriage application together is the official first step for any Russian couple."),
    (12, None, "'I promise to be the very best husband!' Young Ivan means every word of it, which makes their bitter breakup years later all the more poignant."),
]
