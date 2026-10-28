# Authoring module for domashniy-arest-s01e04-scene-08.
ID = 'domashniy-arest-s01e04-scene-08'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 4
SCENE = 8
TITLE = "Новое предложение Паши  (Pasha's New Offer)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'pasha': 'Паша'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.04'
SOURCE_FILE = 'sources/domashniy-arest/s01/e04.ru.dual.srt'
INTRO = "Last time, at the job centre, Nina made Samson take a street job in a giant waffle-cone costume for seven hundred roubles a day. Meanwhile, in the investigator's room, the investigator leaves Arkady alone with his traitorous deputy Pasha, who has laid out cheese and fruit to make a new offer. Let's hear the conversation in Russian first; don't worry about catching every word."
OPENER = "Let's walk through it. As soon as the door closes behind the investigator, Arkady looks across the table at Pasha."
TRANSITION = "Now let's listen to the whole scene in the investigator's room again."
OUTRO = "So Pasha's attempt to gloat over the viral video backfires completely: Arkady decides to make Samson the people's candidate for mayor against Pasha. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('arkady', 'Ну, что ты хотел, Паша?', 'Well, what did you want, Pasha?', [(210, 'Ну'), (211, 'ты хотел')], "cue 211 'Че ты хотел?' -> 'что ты хотел, Паша?'"),
    ('pasha', 'Аркаша, у нас с тобой не по-человечески всё пошло.', "Arkasha, things didn't go right between us.", [(212, 'у нас с тобой не по-человечески все пошло')], "'Аркашенька' -> 'Аркаша'"),
    ('pasha', 'Я же до последнего тянул. Я не хотел.', "I held off until the last moment. I didn't want to.", [(215, 'Я же'), (215, 'до последнего тянул. Не хотел')], "colloquial 'с этой подставой' omitted"),
    ('arkady', 'Да ты что? Ты серьёзно? Иуда!', 'Really? Are you serious? Judas!', [(213, 'Да ты что'), (214, 'Ты серьезно'), (218, 'Иуда')], ''),
    ('pasha', 'Ладно. У меня к тебе новое предложение.', 'All right. I have a new offer for you.', [(219, 'Ладно. У меня к тебе новое предложение')], ''),
    ('pasha', 'Я тебе оставляю пять миллионов и условный срок.', "I'll leave you five million and a suspended sentence.", [(220, 'Я тебе оставляю пять')], "slang 'лямов и плюс условка' -> 'миллионов и условный срок'"),
    ('arkady', 'Пять миллионов — это вообще ни о чём.', 'Five million is nothing at all.', [(236, 'это вообще ни о чем')], "cue 236 '5 лямов' -> 'Пять миллионов'"),
    ('pasha', 'Я вижу, как тебе плохо. В тюрьме будет намного хуже, поверь.', 'But I can see how bad things are for you. In prison it will be much worse, believe me.', [(223, 'вижу, как тебе плохо'), (225, 'будет намного хуже, поверь')], "slang 'на зоне' -> 'В тюрьме'; crude lines 226-228 omitted"),
    ('pasha', 'Выйдешь ты через десять лет. А сейчас свобода, машины, море!', "Well, you'll get out in ten years, and then what? Right now there's freedom, cars, the sea!", [(230, 'выйдешь ты'), (235, 'сейчас свобода'), (235, 'машины, море')], "'из зоны' and crude 'Телки' omitted; '10' written out"),
    ('pasha', 'Над тобой вся страна смеётся! Все видели, как ты из окна летел.', 'The whole country is laughing at you! Everyone saw you fly out the window.', [(242, 'Над тобой вся страна'), (242, 'как ты из')], "slang 'ржет' -> 'смеётся', 'из окон летаешь' -> 'из окна летел'"),
    ('arkady', 'В смысле? А ты что, не знаешь?', "What do you mean? Wait, don't you know?", [(243, 'В смысле'), (244, 'А ты что, не')], "idiom 'не в курсе' -> 'не знаешь'"),
    ('pasha', 'Ты весь интернет порвал! Сосед твой — народный герой!', 'You broke the whole internet! Your neighbour is a national hero!', [(246, 'Ты весь интернет порвал'), (248, 'Сосед твой'), (248, 'народный герой')], "insult 'дебилушка' in cue 248 dropped"),
    ('arkady', 'Сколько там просмотров? Четыре миллиона просмотров!', 'How many views does it have? Four million views!', [(250, 'Сколько там просмотров'), (251, 'четыре')], "cue 251 'миллиона четыре' -> 'Четыре миллиона просмотров'"),
    ('arkady', 'Конец тебе, Паша! Знаешь, кто это?', "You're finished, Pasha! Do you know who this is?", [(252, 'тебе, Паша'), (253, 'Знаешь, кто это')], "obscene cue 252 cleaned to 'Конец тебе, Паша!'"),
    ('arkady', 'Это будущий мэр Синеозерска! Ну что, родной мой, за тебя!', 'That is the future mayor of Sineozersk! Well then, my dear friend, to you!', [(255, 'Будущий мэр'), (256, 'Ну что, родной мой, за тебя')], "cue 255 'Синей Озерска' -> 'Синеозерска'"),
]
WALK = [
    (0, None, "'Well, what did you want, Pasha?' Right then, Pasha puts on a warm, regretful voice."),
    (1, None, "'Arkasha, things didn't go right between us.' The long adverb in the middle literally means 'in a human way' or 'decently': things didn't go the decent way between us."),
    (2, None, "'I held off until the last moment. I didn't want to.' Pasha claims he delayed setting Arkady up as long as he could. Arkady mocks his crocodile tears."),
    (3, None, "'Really? Are you serious? Judas!' In the show Arkady says it sounds like Judas apologising to Christ. Pasha drops the act and gets down to business."),
    (4, None, "'All right. I have a new offer for you.' Remember that in episode two Pasha wanted all forty million; now he sweetens the deal."),
    (5, None, "'I'll leave you five million and a suspended sentence.' Five million roubles out of Arkady's forty million, plus no prison time if Arkady hands over the rest."),
    (6, None, "'Five million is nothing at all.' Literally 'about nothing at all' — a common colloquial phrase for something worthless or tiny. Pasha tries to scare him with prison."),
    (7, 'Я вижу, как тебе плохо.', "'I can see how bad things are for you.' In response, Arkady is sitting there with a bandaged head and ear."),
    (7, 'В тюрьме будет намного хуже, поверь.', "'In prison it will be much worse, believe me.' The comparative word means 'worse', and the word before it means 'much' or 'by far'."),
    (8, 'Выйдешь ты через десять лет.', "'You'll get out in ten years.' With time expressions, the preposition before 'ten years' means 'in' or 'after'."),
    (8, 'А сейчас свобода, машины, море!', "'Right now there's freedom, cars, the sea!' Then Pasha tries to humiliate him with the morning news."),
    (9, 'Над тобой вся страна смеётся!', "'The whole country is laughing at you!' The verb 'to laugh' takes the preposition 'over' plus the 'with/as' form: laughing over you."),
    (9, 'Все видели, как ты из окна летел.', "'Everyone saw you fly out the window.' That is the video Yulia filmed in episode one when Samson threw Arkady out of the ground-floor window. At first Arkady looks puzzled, then he realises what it means."),
    (10, None, "'What do you mean? Wait, don't you know?' In response, Pasha still thinks this is bad news for Arkady."),
    (11, None, "'You broke the whole internet! Your neighbour is a national hero!' Literally 'you tore up the whole internet'. And those words 'national hero' give Arkady a brilliant idea."),
    (12, None, "'How many views does it have? Four million views!' After 'four', the word for 'million' takes the 'of'-form singular, and 'views' is plural 'of' form. Arkady looks at the screen and grins."),
    (13, None, "'You're finished, Pasha! Do you know who this is?' Literally 'an end to you, Pasha'. He turns the phone screen toward Pasha."),
    (14, 'Это будущий мэр Синеозерска!', "'That is the future mayor of Sineozersk!' If Arkady cannot run for mayor himself from under house arrest, he will run his viral-hero neighbour Samson against Pasha!"),
    (14, 'Ну что, родной мой, за тебя!', "'Well then, my dear friend, to you!' Arkady raises his plastic cup in a mocking toast, leaving Pasha speechless."),
]
