# Authoring module for kukhnya-s03e12-scene-04.
ID = 'kukhnya-s03e12-scene-04'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 12
SCENE = 4
TITLE = 'Подарок с подвохом  (A Gift with a Catch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.12'
SOURCE_FILE = 'sources/kukhnya/s03/e12.ru.srt'
INTRO = "At the bar, Kostya asks Nastya why she took Vika's apartment keys when they are renovating their own flat. Nastya explains that the keys are for Max, who is thrilled until he finds out whose apartment it actually is. Listen to the Russian conversation first, and then we will break it down line by line."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Max flatly refuses to move into Vika's old apartment while Vika is living with Nagiyev. Moments later, Grandpa Kirill escalates his attack on the restaurant, forcing Nagiyev and Chef Barinov into action. See you next time!"
CLOSING = ('max', 'Всего хорошего!')
STORY = [
    ('kostya', 'Давай, приступай к работе.', 'Come on, get to work.', [(54, 'приступай к работе')], 'adapted'),
    ('kostya', 'Настя, нам зачем чужая квартира?', "Nastya, why do we need someone else's apartment?", [(55, 'Настя, нам зачем')], 'adapted'),
    ('kostya', 'Мы же в своей собирались ремонт делать.', 'We were going to do renovations in our own place.', [(56, 'Мы же в своей собирались ремонт делать')], 'adapted'),
    ('nastya', 'Ну правильно, это квартира для Макса.', 'That is right, this apartment is for Max.', [(57, 'Ну правильно, это для Макса')], 'adapted'),
    ('nastya', 'Он же расстроился, когда ты ему сказал.', 'He got upset when you told him.', [(58, 'он расстроился, когда ты ему сказал')], 'adapted'),
    ('max', 'Слушайте, я интересную квартиру нашёл.', 'Listen, I found an interesting apartment.', [(60, 'слушайте, я тут интересную квартиру')], 'adapted'),
    ('nastya', 'А мы тебе уже нашли квартиру.', 'And we already found an apartment for you.', [(62, 'А мы тебе нашли квартиру')], 'adapted'),
    ('nastya', 'Вот ключи, там очень хороший ремонт.', 'Here are the keys, there is a very nice renovation there.', [(64, 'Вот ключи. Там очень хороший ремонт')], 'adapted'),
    ('nastya', 'И главное, оплачено до конца года.', 'And most importantly, it is paid through the end of the year.', [(64, 'главное'), (65, 'оплачено до конца года')], 'adapted'),
    ('max', 'О, класс, большое вам спасибо!', 'Oh, awesome, thank you so much!', [(66, 'О, класс, спасибо')], 'adapted'),
    ('kostya', 'Только это квартира Вики.', "Except this is Vika's apartment.", [(68, 'Это квартира Вики')], 'adapted'),
    ('max', 'Вы что, издеваетесь? Может, мне к Нагиеву переехать?', 'Are you kidding me? Maybe I should move in with Nagiyev?', [(69, 'Вы что, издеваетесь'), (70, 'Может, мне сразу к Нагиеву переехать')], 'adapted'),
]
WALK = [
    (0, None, "'Come on, get to work.' Because Max should come on get to work, Kostya treats the matter as settled."),
    (1, None, '\'Nastya, why do we need someone else\'s apartment?\' Here asking why they need someone else apartment shows Kostya looking for the real truth. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, "'We were going to do renovations in our own place.' Kostya mentions that they were going to do renovations in their own place so Max sees what is at stake."),
    (3, None, "'That is right, this apartment is for Max.' Claiming that that is right this apartment is for Max sounds confident, even if Kostya has doubts."),
    (4, None, '\'He got upset when you told him.\' Pointing out that he got upset when Kostya told him gives Kostya a sobering reality check. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (5, None, "'Listen, I found an interesting apartment.' Max explains that he found an interesting apartment, keeping his voice calm and direct."),
    (6, None, "'And we already found an apartment for you.' Realizing that they already found an apartment for Kostya changes how Nastya handles the situation."),
    (7, None, "'Here are the keys, there is a very nice renovation there.' Noting that here are the keys there is a very nice renovation there keeps Nastya's side of the story simple and clear."),
    (8, None, "'And most importantly, it is paid through the end of the year.' Even though most importantly it is paid through the end of the year, Nastya keeps a steady face in front of Kostya."),
    (9, None, "'Oh, awesome, thank you so much!' Between the apartment and the plan, Max delivers a sharp reaction."),
    (10, None, '\'Except this is Vika\'s apartment.\' Saying that except this is Vika apartment is how Kostya sets the tone with Max. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (11, None, '\'Are you kidding me? Maybe I should move in with Nagiyev?\' By asking whether Kostya kidding him, Max presses Kostya for a straight answer. Notice how he sticks to the formal "you", keeping a professional line between them.'),
]
