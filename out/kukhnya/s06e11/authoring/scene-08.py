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
    (0, None, "'Take a look, please, is the second room paid for already?' Confirming how second things are during the talk, Barinov keeps normal statement word order here, turning the line into a question for the guest purely through rising pitch."),
    (1, None, "'Alright, then just put that room on my tab.' Pointing to the number in this moment, Barinov brings the exchange with the guest back to practical reality."),
    (2, None, '\'Andrey, hello, I am very glad to see you here.\' Barinov follows up boldly beside the guest and reaches for the Russian word "zdravstvuyte" ("hello") right at the heart of the line.'),
    (3, None, '\'And your brother and I are discussing an interesting project.\' Making clear how interesting things are with Barinov, the guest centers the remark on "interesnyy" ("interesting") without any extra fuss.'),
    (4, None, "'You have, of course, heard about oyster farms?' The guest asks deadpan where this conversation is heading next."),
    (5, None, '\'Excuse me for a second, hello, I am listening.\' Emphasizing a second right here, the guest chooses "sekundu" ("second", from the root "sekunda") so Barinov hears the exact meaning.'),
    (6, None, '\'Valya, tell me, what are you doing over there?\' Answering quietly right here, Barinov puts the question word "chto" right at the start so the guest hears the focus immediately.'),
    (7, None, "'He is a serious person, do not drag him into risky ventures!' Barinov counters firmly across the room, testing the guest's reaction in the middle of the exchange."),
    (8, None, '\'Vitya, calm down, I am not dragging him into anything.\' The guest proceeds promptly around Barinov and lands on "uspokoysya" ("calm down", built on "uspokoitsya") to keep the statement grounded.'),
    (9, None, '\'He himself became very interested in my new project.\' Turning to the project around Barinov, the "-sya" ending on "zainteresovalsya" ("became interested") marks an action that unfolds mutually or turns back on the speaker.'),
    (10, None, "'After all, this is excellent and mutually beneficial cooperation for us.' The guest counters lightly with a nod, watching Barinov's face to see how the news lands."),
    (11, None, '\'Do you remember who paid off the debt for you afterward?\' Discussing the debt on the spot, Barinov chooses "pomnish" ("do you remember", from the root "pomnit") so the guest hears the exact meaning.'),
    (12, None, "'In short, I really hope that you heard me!' Barinov counters steadily with a smile, steering the talk right where he wants it."),
]
