# Authoring module for domashniy-arest-s01e03-scene-26.
ID = 'domashniy-arest-s01e03-scene-26'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 3
SCENE = 26
TITLE = 'Украденная собака  (The Stolen Dog)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'samson': 'Самсон', 'slavik': 'Славик'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.03'
SOURCE_FILE = 'sources/domashniy-arest/s01/e03.ru.dual.srt'
INTRO = "Still in the communal flat, a moment later. Just then, ten-year-old Slavik walks in carrying Judge Berg's tiny white dog under his arm. We'll hear the scene in Russian first; just listen for the mood and don't worry about catching every word."
OPENER = "Let's walk through the scene line by line. Slavik stops in the doorway, surprised to see his parents with Arkady tied to a chair."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = "So Slavik has delivered Judge Berg's beloved lapdog right into Arkady's hands, and Arkady is ready to make his phone call. You followed every step in Russian; well done. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('slavik', 'А что это вы здесь?', 'What are you doing in here?', [(898, 'это вы здесь')], "'А че' -> 'А что'"),
    ('samson', 'Да ничего, сынок. Всё нормально.', "Nothing, son. Everything's fine.", [(899, 'Да ничего, сынок'), (900, 'Все нормально')], ''),
    ('samson', 'А что это ты в квартиру принёс?', 'And what is that you brought into the flat?', [(901, 'это ты в'), (901, 'принес')], "cue 901 given to Samson (Nina has no voice); 'че' -> 'что', 'квартиру-то' -> 'квартиру'"),
    ('slavik', 'Дядя Аркаша попросил.', 'Uncle Arkasha asked me to.', [(902, 'Дядя Аркаша попросил')], ''),
    ('samson', 'Видишь, Аркаша, он собаку принёс тебе.', 'See, Arkasha, he brought you a dog.', [(903, 'видишь, Аркаша, собаку'), (903, 'тебе')], "cue 903 has the transcription slip 'принеси' for 'принёс'; 'он' added"),
    ('arkady', 'Слушайте, мне нужно одному остаться.', 'Listen, I need to be left alone.', [(904, 'Слушайте'), (904, 'мне нужно одному остаться')], "'а' dropped"),
    ('arkady', 'Мне нужно сосредоточиться.', 'I need to concentrate.', [(905, 'мне нужно сосредоточиться')], "'Оставьте,' dropped"),
    ('samson', 'Хорошо, давай, пойдём.', "All right, come on, let's go.", [(906, 'Хорошо, давай, пойдем')], ''),
    ('arkady', 'Славик, давай сюда собаку.', 'Slavik, hand over the dog.', [(909, 'Давай'), (909, 'собаку')], "'Славик, ... сюда' added"),
    ('slavik', 'А Лёля? Вы же обещали.', 'What about Lyolya? You promised.', [(910, 'А Леля'), (912, 'Обещали')], "'Вы же' added"),
    ('arkady', 'Да будет твоя Лёля, я сказал. Иди.', "You'll get your Lyolya, I said. Go on.", [(911, 'Да будет твоя Леля, я сказал. Иди')], ''),
    ('arkady', 'Что, малыш? Испугался?', 'What is it, little guy? Are you scared?', [(914, 'Что'), (915, 'Испугался')], "crude 'гнида' (914) -> 'малыш'"),
    ('arkady', 'Я сейчас выйду отсюда.', "I'm getting out of here right now.", [(916, 'Я сейчас выйду отсюда')], ''),
    ('arkady', 'Смотри сюда. А ты посиди потихонечку.', 'Look here. You just sit quietly for a bit.', [(921, 'Смотри сюда'), (922, 'потихонечку')], "'Посиди-ка' -> 'А ты посиди'"),
]
WALK = [
    (0, None, "'What are you doing in here?' Literally, 'and what is this you here?' Samson quickly covers for himself and Nina."),
    (1, None, "'Nothing, son. Everything's fine.' The word for 'son' is an affectionate diminutive, 'little son'. Then Samson spots the fluffy white bundle in the boy's arms."),
    (2, None, "'And what is that you brought into the flat?' After 'into', the word for 'flat' takes the object ending because something was carried inside. Slavik answers simply."),
    (3, None, "'Uncle Arkasha asked me to.' Russian children call adult neighbours and family friends 'Uncle' or 'Aunt' plus their short first name. Samson grins at Arkady."),
    (4, None, "'See, Arkasha, he brought you a dog.' The verb is past tense masculine, matching the boy. Arkady immediately sees his chance and wants the room cleared."),
    (5, None, "'Listen, I need to be left alone.' He uses the plural command 'listen' because he is speaking to both Samson and Nina. Literally, 'to me it is needed alone to remain'."),
    (6, None, "'I need to concentrate.' The self-action verb form at the end of the long verb means gathering yourself together: focusing your own mind. Samson doesn't argue."),
    (7, None, "'All right, come on, let's go.' He leads Nina out of the room. Before Slavik follows, Arkady calls for the dog."),
    (8, None, "'Slavik, hand over the dog.' Here the everyday word for 'come on' means 'give me'. Slavik holds on for a second to check their bargain."),
    (9, None, "'What about Lyolya? You promised.' He uses the plural past tense for 'promised', which is how Russian shows polite respect to one grown-up."),
    (10, None, "'You'll get your Lyolya, I said. Go on.' Literally, 'your Lyolya will be'. Once the door shuts, Arkady is alone with the judge's tiny dog and puts on a tough voice."),
    (11, None, "'What is it, little guy? Are you scared?' The verb for 'got scared' is masculine past tense, because the little dog is a boy."),
    (12, None, "'I'm getting out of here right now.' Russian uses the future-tense form with 'right now' for something about to happen any minute."),
    (13, None, "'Look here. You just sit quietly for a bit.' The prefix on 'sit' means 'for a little while', and the long adverb at the end is a soft diminutive for 'quietly'."),
]
