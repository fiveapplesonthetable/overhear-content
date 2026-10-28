# Authoring module for kukhnya-s06e11-scene-08.
ID = 'kukhnya-s06e11-scene-08'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 11
SCENE = 8
TITLE = 'Деловой разговор с конкурентом  (Business Talk with a Rival)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.11'
SOURCE_FILE = 'sources/kukhnya/s06/e11.ru.srt'
INTRO = "After putting Valya's unpaid hotel room on his own tab, Barinov is shocked to see his brother sitting in the restaurant pitching oyster farms to Andrey Dyagilev. Barinov immediately calls Valya's cell phone and warns him not to drag a serious businessman into his schemes."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "While Barinov worries that his brother is conning Dyagilev, back in the kitchen Senya and Fedya discover the wallet dropped by Sveta's attacker. See you next time!"
CLOSING = ('barinov', 'Хорошего дня!')
STORY = [
    ('barinov', 'Посмотри, пожалуйста, второй номер уже оплачен?', 'Take a look, please, is the second room paid for already?', [(137, 'посмотри, пожалуйста'), (137, 'оплачен')], 'adapted'),
    ('barinov', 'Ладно, тогда просто запиши этот номер на меня.', 'Alright, then just put that room on my tab.', [(139, 'Запиши на меня')], 'adapted'),
    ('barinov', 'Андрей, здравствуйте, очень рад вас здесь видеть.', 'Andrey, hello, I am very glad to see you here.', [(140, 'Андрей, рад вас видеть. Здравствуйте')], 'adapted'),
    ('guest', 'А мы с вашим братом обсуждаем интересный проект.', 'And your brother and I are discussing an interesting project.', [(141, 'А мы вот как раз с вашим братом обсуждаем один очень интересный проект')], 'adapted'),
    ('guest', 'Вы, конечно же, слышали об устричных фермах?', 'You have, of course, heard about oyster farms?', [(142, 'Вы, конечно же, слышали об устричных фермах')], 'adapted'),
    ('guest', 'Извините меня на секунду, алло, я слушаю.', 'Excuse me for a second, hello, I am listening.', [(143, 'Извините. Секундочку'), (144, 'Алло, да, слушаю')], 'adapted'),
    ('barinov', 'Валя, скажи мне, что ты там творишь?', 'Valya, tell me, what are you doing over there?', [(145, 'Ты что творишь, а')], 'adapted'),
    ('barinov', 'Это серьёзный человек, не втягивай его в авантюры!', 'He is a serious person, do not drag him into risky ventures!', [(146, 'Это же серьезный человек. Не вздумай втягивать его в свои авантюры')], 'adapted'),
    ('guest', 'Витя, успокойся, никуда я его не втягиваю.', 'Vitya, calm down, I am not dragging him into anything.', [(148, 'Никуда я его не втягиваю')], 'adapted'),
    ('guest', 'Он сам очень заинтересовался моим новым проектом.', 'He himself became very interested in my new project.', [(149, 'Он сам заинтересовался')], 'adapted'),
    ('guest', 'Ведь это отличное и взаимовыгодное сотрудничество для нас.', 'After all, this is excellent and mutually beneficial cooperation for us.', [(151, 'Это взаимовыгодное сотрудничество')], 'adapted'),
    ('barinov', 'Ты помнишь, кто за тебя потом долг платил?', 'Do you remember who paid off the debt for you afterward?', [(154, 'А ты помнишь, кто за тебя потом долг платил')], 'adapted'),
    ('barinov', 'Короче, я очень надеюсь, что ты меня услышал!', 'In short, I really hope that you heard me!', [(155, 'Я надеюсь, ты меня услышал')], 'adapted'),
]
WALK = [
    (0, None, '\'Take a look, please, is the second room paid for already?\' Barinov puts that reply toward the guest: dropping in "pozhaluysta" ("please") keeps the request polite on the surface even in a brisk exchange.'),
    (1, None, "'Alright, then just put that room on my tab.' Barinov continues right away without holding back, bringing things back to earth after the buildup."),
    (2, None, '\'Andrey, hello, I am very glad to see you here.\' Barinov points to this sharp term on cue: "zdravstvuyte" means "hello", and it carries the main weight of what Barinov is saying.'),
    (3, None, "'And your brother and I are discussing an interesting project.' The guest follows up steadily in this moment, testing Barinov's reaction in the middle of the exchange."),
    (4, None, "'You have, of course, heard about oyster farms?' The guest asks deadpan as Barinov tries to explain the situation."),
    (5, None, '\'Excuse me for a second, hello, I am listening.\' The guest colors one practical choice in reply: "sekundu" means "second" (from "sekunda"), giving the line its exact edge.'),
    (6, None, '\'Valya, tell me, what are you doing over there?\' Barinov directs that reply in earnest: putting the question word "chto" right at the front of the line lets the guest hear the point of the question on the very first beat.'),
    (7, None, "'He is a serious person, do not drag him into risky ventures!' Barinov weighs in firmly with a smile, leaving no doubt about where he stands."),
    (8, None, '\'Vitya, calm down, I am not dragging him into anything.\' The guest focuses on one vivid expression right here: "uspokoysya" means "calm down" (from "uspokoitsya"), giving the line its exact edge.'),
    (9, None, '\'He himself became very interested in my new project.\' The guest puts this update briskly now: the "-sya" ending on "zainteresovalsya" ("became interested") turns the action inward or makes it happen between people naturally.'),
    (10, None, "'After all, this is excellent and mutually beneficial cooperation for us.' The guest proceeds lightly without a pause, steering the talk right where he wants it."),
    (11, None, '\'Do you remember who paid off the debt for you afterward?\' Barinov chooses one colorful touch right here: "pomnish" means "do you remember" (from "pomnit"), giving the line its exact edge.'),
    (12, None, '\'In short, I really hope that you heard me!\' Barinov points to this clear term in earnest: "uslyshal" means "heard" (from "uslyshat"), giving the line its exact edge.'),
]
