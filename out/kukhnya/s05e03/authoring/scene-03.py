# Authoring module for kukhnya-s05e03-scene-03.
ID = 'kukhnya-s05e03-scene-03'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 3
SCENE = 3
TITLE = "Наследство мужа и командировка в Питер  (The Husband's Inheritance and the St. Petersburg Trip)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.03'
SOURCE_FILE = 'sources/kukhnya/s05/e03.ru.srt'
INTRO = 'Stunned that Eleonora owns the hotel, Barinov accuses Katya of knowing and declares he is quitting, while Eleonora asks Katya to fly to St. Petersburg tomorrow for a hotel event. Listen to the conversation.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that sets Eleonora's plot in motion to send Katya out of town. Notice the comparative structure 'more a musician than a cook'. Until next time!"
CLOSING = ('katya', 'Увидимся!')
STORY = [
    ('barinov', 'Катя, ты об этом знала?', 'Katya, did you know about this?', [(33, 'Ты знала?')], 'adapted'),
    ('eleonora', 'Она ничего об этом не знала.', 'She knew nothing about it.', [(33, 'Она ничего не знала')], 'adapted'),
    ('barinov', 'Значит, это лично твой план?', 'So this is your personal plan?', [(34, 'Значит, это лично твой план?')], 'verbatim'),
    ('eleonora', 'Успокойся, тебя нанимал мой муж.', 'Calm down, my husband hired you.', [(35, 'Успокойся'), (36, 'мой муж')], 'adapted'),
    ('eleonora', 'Он оставил мне этот отель.', 'He left me this hotel.', [(37, 'он оставил мне отель')], 'adapted'),
    ('barinov', 'Очередной муж от тебя сбежал?', 'Did another husband run away from you?', [(38, 'муж от тебя сбежал')], 'adapted'),
    ('barinov', 'Прими мои поздравления, дорогая.', 'Accept my congratulations, my dear.', [(39, 'Мои поздравления')], 'adapted'),
    ('barinov', 'Он так бежал, что гостиницу забыл.', 'He ran so fast that he forgot the hotel.', [(39, 'что гостиницу забыл')], 'adapted'),
    ('eleonora', 'Вообще-то он недавно умер.', 'Actually, he died recently.', [(40, 'Он умер')], 'adapted'),
    ('barinov', 'Ищите себе другого шефа.', 'Look for another head chef for yourselves.', [(42, 'Ищите себе другого шефа')], 'verbatim'),
    ('katya', 'Мама, ну останови его!', 'Mom, please stop him!', [(44, 'Мам, останови его')], 'adapted'),
    ('katya', 'Денис очень хороший парень.', 'Denis is a very good guy.', [(46, 'Денис хороший парень')], 'adapted'),
    ('katya', 'Но он больше музыкант, чем повар.', 'But he is more of a musician than a cook.', [(47, 'он больше музыкант, чем повар')], 'adapted'),
    ('eleonora', 'То есть он не определился до сих пор?', 'So he still has not made up his mind?', [(48, 'он не определился до сих пор?')], 'verbatim'),
    ('katya', 'Мы договорились: ты не вмешиваешься в мою жизнь.', 'We agreed: you do not interfere in my life.', [(49, 'договорились'), (50, 'не вмешиваешься в мою'), (50, 'жизнь')], 'adapted'),
    ('eleonora', 'Завтра у нас важное мероприятие.', 'Tomorrow we have an important event.', [(52, 'Завтра у нас'), (52, 'мероприятие')], 'adapted'),
    ('eleonora', 'Там наш главный повар заболел.', 'Our head cook there got sick.', [(53, 'повар заболел')], 'adapted'),
    ('eleonora', 'Твоя кухня могла бы спасти положение.', 'Your cuisine could save the situation.', [(54, 'кухня'), (54, 'спасти положение')], 'adapted'),
]
WALK = [
    (0, None, '\'Katya, did you know about this?\' By checking whether Eleonora knows about this, Barinov presses Eleonora for a straight answer. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (1, None, "'She knew nothing about it.' Eleonora tells Barinov that she knew nothing about it without dressing it up."),
    (2, None, '\'So this is your personal plan?\' Questioning whether this is Eleonora\'s personal plan is how Barinov tests Eleonora\'s story. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (3, None, '\'Calm down, my husband hired you.\' Here calming down her husband hired Barinov sets up the next turn in their exchange. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (4, None, "'He left me this hotel.' Eleonora reminds Barinov that he left her this hotel before the moment passes."),
    (5, None, '\'Did another husband run away from you?\' Checking whether another husband run away from Eleonora cuts straight through the tension between Barinov and Eleonora. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (6, None, "'Accept my congratulations, my dear.' Explaining that Eleonora should accept his congratulations his dear lays the cards on the table for Eleonora."),
    (7, None, "'He ran so fast that he forgot the hotel.' Barinov mentions that he ran so fast that he forgot the hotel so Eleonora sees what is at stake."),
    (8, None, "'Actually, he died recently.' Between the trip and the work, Eleonora gives Barinov a quick, grounded response."),
    (9, None, "'Look for another head chef for yourselves.' With the trip and truth in play, Barinov keeps this short reply brisk and direct."),
    (10, None, "'Mom, please stop him!' Over the shift and the trip, Katya lets her real feelings show."),
    (11, None, "'Denis is a very good guy.' Realizing that Denis is a very good guy changes how Katya handles the situation."),
    (12, None, "'But he is more of a musician than a cook.' Noting that he is more of a musician than a cook keeps Katya's side of the story simple and clear."),
    (13, None, "'So he still has not made up his mind?' Eleonora asks whether he still has not made up his mind, refusing to let the point slide."),
    (14, None, '\'We agreed: you do not interfere in my life.\' Admitting that they agreed Barinov does not interfere in her life shows Katya being honest for a change. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (15, None, '\'Tomorrow we have an important event.\' Saying that tomorrow they have an important event is how Eleonora sets the tone with Barinov. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (16, None, "'Our head cook there got sick.' Once their head cook there got sick, Eleonora can finally tell Barinov what she means."),
    (17, None, '\'Your cuisine could save the situation.\' Adding that Barinov\'s cuisine could save the situation fills in the missing piece for Barinov. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
]
