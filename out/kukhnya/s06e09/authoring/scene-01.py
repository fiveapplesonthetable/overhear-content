# Authoring module for kukhnya-s06e09-scene-01.
ID = 'kukhnya-s06e09-scene-01'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 9
SCENE = 1
TITLE = 'Авария у отеля  (Accident Outside the Hotel)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'denis': 'Денис', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.09'
SOURCE_FILE = 'sources/kukhnya/s06/e09.ru.srt'
INTRO = "Welcome to Episode Nine of Kukhnya Season Six. Outside the hotel, Denis gets bumped by a reckless car and hurts his arm while choking on a piece of candy, and inside, Chef Barinov trades football banter with Elena's ex-husband Sasha ahead of tomorrow's big derby."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'After Denis is shaken up in the courtyard, Barinov is determined to win his football bet against Sasha. Until next time!'
CLOSING = ('barinov', 'Хорошего дня!')
STORY = [
    ('denis', 'Она машину совсем не заметила.', 'She did not notice the car at all.', [(1, 'Машину-то не заметила')], 'adapted'),
    ('barinov', 'Денис, дыши спокойно, сейчас вызовем скорую.', 'Denis, breathe calmly, we will call an ambulance now.', [(1, 'Денис, дыши'), (2, 'давай скорую')], 'adapted'),
    ('denis', 'Всё нормально, я просто конфетой подавился.', 'Everything is fine, I just choked on a candy.', [(3, 'нормально, я просто конфетой подавился')], 'adapted'),
    ('barinov', 'Алло, скорая, у нас тут авария.', 'Hello, ambulance, we have an accident here.', [(3, 'Алло, скорая, у нас тут ДТП')], 'adapted'),
    ('denis', 'И правая рука у меня сильно болит.', 'And my right arm hurts badly.', [(5, 'И рука у него болит')], 'adapted'),
    ('barinov', 'Что тут непонятного, приезжайте скорее.', 'What is unclear here, come quickly.', [(5, 'Что тут непонятного')], 'adapted'),
    ('sasha', 'Виктор, ты этот тонкий намёк понял?', 'Viktor, did you understand that subtle hint?', [(6, 'намек понял')], 'adapted'),
    ('barinov', 'Завтра ваша команда снова играет со Спартаком.', 'Tomorrow your team plays against Spartak again.', [(7, 'завтра играется Спартаком')], 'adapted'),
    ('sasha', 'Мы завтра ваших коней легко обыграем.', 'Tomorrow we will easily beat your horses.', [(9, 'Мы завтра ваших коней')], 'adapted'),
    ('barinov', 'Жалко, я твоего позора не увижу.', 'It is a pity I will not see your disgrace.', [(10, 'Жалко только я твоего позора не увижу')], 'adapted'),
    ('sasha', 'Я завтра утром женюсь, потом банкет.', 'I am getting married tomorrow morning, then the banquet.', [(11, 'Я завтра в 10 утра женюсь, потом банкет')], 'adapted'),
    ('barinov', 'Женись спокойно, а я поставил деньги.', 'Get married in peace, and I placed a bet.', [(12, 'Женись')], 'adapted'),
    ('sasha', 'Ой, это просто настоящий детский сад.', 'Oh, this is just a real kindergarten.', [(13, 'Ой, детский сад')], 'adapted'),
]
WALK = [
    (0, None, '\'She did not notice the car at all.\' Emphasizing the car in the exchange, Denis lands on "mashinu" ("car", built on "mashina") to keep the statement grounded.'),
    (1, None, '\'Denis, breathe calmly, we will call an ambulance now.\' Mentioning an ambulance at once, Barinov leans on "skoruyu" ("ambulance", a form of "skoraya") to give the remark its edge.'),
    (2, None, "'Everything is fine, I just choked on a candy.' Denis follows up sharply on the spot, watching Barinov's face to see how the news lands."),
    (3, None, '\'Hello, ambulance, we have an accident here.\' Pointing to the ambulance around Denis, Barinov chooses "skoraya" ("ambulance") so Denis gets the point right away.'),
    (4, None, "'And my right arm hurts badly.' Denis replies frankly in their talk, making his position completely clear."),
    (5, None, "'What is unclear here, come quickly.' Barinov responds briskly with Denis, making his position completely clear."),
    (6, None, '\'Viktor, did you understand that subtle hint?\' Focusing on the hint during the talk, Sasha centers the remark on "tonkiy" ("subtle, thin") without any extra fuss.'),
    (7, None, "'Tomorrow your team plays against Spartak again.' Barinov responds promptly watching Sasha, bringing things back to earth after the buildup."),
    (8, None, "'Tomorrow we will easily beat your horses.' Sasha jumps in decisively with Barinov, leaving no doubt about where she stands."),
    (9, None, '\'It is a pity I will not see your disgrace.\' Underscoring the disgrace around Sasha, Barinov brings in "pozora" ("disgrace", from "pozor") as the key Russian word here.'),
    (10, None, '\'I am getting married tomorrow morning, then the banquet.\' Addressing the banquet right here, Sasha chooses "banket" ("banquet") so Barinov gets the point right away.'),
    (11, None, "'Get married in peace, and I placed a bet.' Barinov replies decisively with a sigh, refusing to let the moment slip past."),
    (12, None, '\'Oh, this is just a real kindergarten.\' Explaining how real things are on the spot, Sasha brings in "nastoyashchiy" ("real, genuine") to make the meaning unmistakable.'),
]
