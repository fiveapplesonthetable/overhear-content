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
    (0, None, '\'Come on, get to work.\' Pointing to the work before Nastya, Kostya centers the thought on "pristupay" ("get to, start", from "pristupat") without wasting a word.'),
    (1, None, '\'Nastya, why do we need someone else\'s apartment?\' Turning to the flat in the exchange, Kostya puts the question word "zachem" right at the start so Nastya hears the focus immediately.'),
    (2, None, "'We were going to do renovations in our own place.' Kostya speaks up calmly beside Nastya, refusing to let the moment slip past."),
    (3, None, '\'That is right, this apartment is for Max.\' Mentioning the flat in the exchange, Nastya chooses "kvartira" ("flat") so Max gets the point right away.'),
    (4, None, '\'He got upset when you told him.\' Looking over smoothly at once, the "-sya" ending on "rasstroilsya" ("got upset") marks an action that unfolds mutually or turns back on the speaker.'),
    (5, None, "'Listen, I found an interesting apartment.' Max cuts in calmly with a smile, leaving no doubt about where he stands."),
    (6, None, '\'And we already found an apartment for you.\' Focusing on the flat around Max, Nastya puts the weight on "kvartiru" ("flat", from "kvartira") as the exchange unfolds.'),
    (7, None, '\'Here are the keys, there is a very nice renovation there.\' Stressing how good things are around Max, Nastya links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (8, None, "'And most importantly, it is paid through the end of the year.' Nastya speaks up sharply with Max, so Max knows she is not just making small talk."),
    (9, None, '\'Oh, awesome, thank you so much!\' Underscoring the cool beside Nastya, Max centers the thought on "bolshoye" ("big, very much", from "bolshoy") without wasting a word.'),
    (10, None, '\'Except this is Vika\'s apartment.\' Returning to the flat in this beat, Kostya links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (11, None, "'Are you kidding me? Maybe I should move in with Nagiyev?' Max checks bluntly before Kostya can change the subject."),
]
