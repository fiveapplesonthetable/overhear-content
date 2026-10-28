# Authoring module for domashniy-arest-s01e02-scene-25.
ID = 'domashniy-arest-s01e02-scene-25'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 2
SCENE = 25
TITLE = "Я не передумаю  (I Won't Change My Mind)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'lavrov': 'Лавров', 'marina': 'Марина', 'zavarzin': 'Заварзин'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.02'
SOURCE_FILE = 'sources/domashniy-arest/s01/e02.ru.dual.srt'
INTRO = "Meanwhile, at the communal flat, Marina has two visitors. Last time, Arkady talked her little son Lyosha into handing over five hundred roubles from his piggy bank, and now two security-service agents from Moscow, Major Lavrov and Captain Zavarzin, are knocking on her door. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's take it slowly. Marina opens the door, and the older of the two men introduces them both, very properly."
TRANSITION = "Now let's listen to the whole visit again, from the knock on the door."
OUTRO = "That's the end of this one: listen out for her promise not to change her mind, and keep it in mind, because the card is still on her table. See you next time!"
CLOSING = ('marina', 'До свидания.')
STORY = [
    ('lavrov', 'Марина Сергеевна, майор Лавров. Это капитан Заварзин.', 'Marina Sergeyevna, Major Lavrov. This is Captain Zavarzin.', [(796, 'Марина Сергеевна'), (796, 'майор Лавров'), (797, 'Капитан Заварзин')], "Marina's garbled surname and the agency's initials dropped; 'Это' added"),
    ('marina', 'Я знаю, зачем вы пришли.', "I know why you've come.", [], "a simple stand-in for cue 798 ('So, someone has reported me?')"),
    ('lavrov', 'Не понял.', "I don't follow.", [(799, 'Не понял')], ''),
    ('marina', 'Я это говорила, про Крым. Можете меня арестовать, я готова.', "I did say it, about Crimea. You can arrest me, I'm ready.", [(800, 'Я это говорила'), (804, 'можете меня'), (806, 'я готова')], "the political statement itself (802-803) is left out; 'арестовывать' -> 'арестовать'; 'про Крым' added"),
    ('zavarzin', 'Толя, она совсем странная.', "Tolya, she's really strange.", [(809, 'Толя'), (809, 'она совсем')], "slang 'куку' (nuts) -> 'странная'"),
    ('lavrov', 'Да, но лучше, чем бабушка.', 'Yes, but better than the old lady.', [(811, 'Лучше, чем')], "'бабка' -> 'бабушка'; 'Да, но' added; the reply given to Lavrov (speakers unclear)"),
    ('marina', 'Вы зря теряете время. Шпионить для вас я не буду.', "You're wasting your time. I'm not going to spy for you.", [(829, 'Вы зря теряете время'), (830, 'Шпионить')], "'на вашу людоедскую контору ... не собираюсь' -> 'для вас ... не буду'"),
    ('lavrov', 'Поймите, этот человек берёт взятки.', 'You must understand, this man takes bribes.', [(832, 'Поймите, этот человек')], "'взяточник' (bribe-taker) -> 'берёт взятки'"),
    ('marina', 'Ну, его и посадят. Что вы от него ещё хотите?', "Well, then they'll put him in prison. What more do you want from him?", [(833, 'его и посадят'), (836, 'Что вы от него еще хотите')], 'cues 834-835 (about Russian prisons) left out'),
    ('zavarzin', 'Чтобы он вернул деньги, которые украл.', 'For him to give back the money he stole.', [(837, 'Чтобы он вернул деньги, которые украл')], 'given to Zavarzin (speaker unclear)'),
    ('marina', 'А кто их получит? Те, кто сидит повыше?', 'And who will get it? The people who sit higher up?', [(838, 'повыше')], "cue 838 simplified ('so that the same sort, who sit higher up, can loot it?')"),
    ('lavrov', 'А вашу работу вернуть можно. И мы хорошо платим.', 'But we can get your job back for you. And we pay well.', [(846, 'вашу работу вернуть можно')], "'А' kept; second sentence is a plain version of cues 847-848; Crimea joke (844-845) and torture line (840) left out"),
    ('zavarzin', 'Купите ребёнку приставку.', 'Buy your child a games console.', [(849, 'Купите ребенку')], "'PSP' -> 'приставку' (Cyrillic only)"),
    ('marina', 'Вы что, за нами следите?', 'What, are you watching us?', [(850, 'Вы что, за нами следите')], ''),
    ('zavarzin', 'Да все дети хотят приставку.', 'Come on, all children want a games console.', [(852, 'все дети хотят')], "'Господи' -> 'Да'; 'PSP' -> 'приставку'"),
    ('marina', 'Нет. Я не продаюсь.', "No. I'm not for sale.", [], "a clean stand-in for cues 853-854 ('I won't sell myself for your silver', 'I'm not a snitch')"),
    ('lavrov', 'Возьмите, пожалуйста. На случай, если передумаете.', 'Please take this. In case you change your mind.', [(855, 'возьмите, пожалуйста'), (855, 'на случай, если передумаете')], 'the business card is left to the narrator'),
    ('marina', 'Я не передумаю.', "I won't change my mind.", [(856, 'Я не передумаю')], ''),
]
WALK = [
    (0, 'Марина Сергеевна, майор Лавров.', "'Marina Sergeyevna, Major Lavrov.' He uses her first name and her father's name, the formal way, and then his own rank and surname. Then he points to his colleague."),
    (0, 'Это капитан Заварзин.', "'This is Captain Zavarzin.' The little word in front means 'this is', the easiest way to introduce someone. Marina is not surprised at all."),
    (1, None, "'I know why you've come.' She is sure someone has reported her for her opinions. The word for 'came' is in the plural here, because she is using the polite form of 'you'. The major is puzzled."),
    (2, None, "'I don't follow.' Major Lavrov puts 'understood' up front and finishes with 'understood' to make the point unmistakable."),
    (3, 'Я это говорила, про Крым.', "'I did say it, about Crimea.' She once said in public what she thinks about Crimea, and she believes this visit is the price. Her action word ends in the feminine form, because she is a woman. And she isn't backing down."),
    (3, 'Можете меня арестовать, я готова.', "'You can arrest me, I'm ready.' The arrest word is easy to recognise. The agents step aside for a moment, and Zavarzin whispers to his partner."),
    (4, None, "'Tolya, she's really strange.' In this moment, Tolya is a friendly short form of the major's first name. Lavrov has his answer ready."),
    (5, None, "'Yes, but better than the old lady.' The last word normally means 'grandmother', but it is also how people talk about any old woman. They seem to have had another neighbour in mind as an informer. Then they explain what they want, and Marina's answer is quick."),
    (6, 'Вы зря теряете время.', "'You're wasting your time.' The second word means 'for nothing', 'in vain'. Then she says exactly what she won't do."),
    (6, 'Шпионить для вас я не буду.', "'I'm not going to spy for you.' The action word is the spy word you can probably guess. Putting it first makes it sound stronger, like 'spying for you, that I won't do'. The major tries to explain."),
    (7, None, "'You must understand, this man takes bribes.' The man is Arkady, of course. The action word is the ordinary action word 'to take', and the last word means 'bribes'. Marina is not impressed."),
    (8, 'Ну, его и посадят.', "'Well, then they'll put him in prison.' The action word literally means 'they'll sit him down', which is the everyday way of saying 'they'll lock him up'. Then she asks what else they want."),
    (8, 'Что вы от него ещё хотите?', "'What more do you want from him?' The small word in the middle means 'more', or 'else'. Zavarzin answers."),
    (9, None, "'For him to give back the money he stole.' The first word means 'so that', and the action word after it, 'give back', is in the past form, as it always is after that word. Marina has her doubts about where the money would go."),
    (10, None, "'And who will get it? The people who sit higher up?' She means the bosses, the people with higher posts. Notice the same idea of sitting: you sit high up in power, and you get sat down in prison. Then the agents change their tune."),
    (11, 'А вашу работу вернуть можно.', "'But we can get your job back for you.' Literally 'your job, it's possible to return'. Marina has just been fired from the university, so this is a real temptation. And there's more."),
    (11, 'И мы хорошо платим.', "'And we pay well.' A short, clear offer of money. Then Zavarzin adds something very personal."),
    (12, None, "'Buy your child a games console.' The action word is the polite command, 'buy'. Marina and her son are saving for exactly this, so it gives her a shock."),
    (13, None, "'What, are you watching us?' The action word means 'to follow', 'to keep watch on', and it goes with a little word meaning 'behind', literally 'you follow behind us'. Zavarzin brushes it off."),
    (14, None, "'Come on, all children want a games console.' The word for 'all' comes before 'children', just as in English. Marina doesn't take the bait."),
    (15, None, "'No. I'm not for sale.' The action word means 'to sell oneself': the little ending on it means 'oneself'. The major holds out his card anyway."),
    (16, None, "'Please take this. In case you change your mind.' Again the polite command form, and the polite 'please'. Marina has the last word."),
    (17, None, "'I won't change my mind.' The action word is in the future here, 'I will not change my mind'. She sounds very sure, but the card stays behind. Meanwhile, on the building site, Samson has been showing off by carrying heavy radiators, until his boss makes the whole crew help."),
]
