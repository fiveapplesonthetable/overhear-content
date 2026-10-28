# Authoring module for kukhnya-s05e01-scene-13.
ID = 'kukhnya-s05e01-scene-13'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 1
SCENE = 13
TITLE = "Война за кабинет Михаила  (War Over Mikhail's Office)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'mikhail': 'Михаил', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.01'
SOURCE_FILE = 'sources/kukhnya/s05/e01.ru.srt'
INTRO = "To retaliate against Mikhail for locking the kitchen restroom, Chef Barinov sends his staff to line up outside Mikhail's private office bathroom, sparking a fierce argument in front of Vika. Listen to the scene."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that brings the standoff outside Mikhail's office to a close. Notice Vika's exasperated suggestion to toss a coin to settle the feud. Until next time!"
CLOSING = ('vika', 'Пока!')
STORY = [
    ('barinov', 'О, доброе утро, шеф!', 'Oh, good morning, Chef!', [(208, 'О, доброе утро, шеф!')], 'verbatim'),
    ('barinov', 'Михаил сделает нам туалет, как просим.', 'Mikhail will give us a restroom as we ask.', [(209, 'сделает нам туалет, как мы просим')], 'adapted'),
    ('barinov', 'Шеф, я там совсем чуть-чуть.', 'Chef, I only need a tiny moment in there.', [(210, 'Шеф, я там совсем чуть-чуть')], 'verbatim'),
    ('mikhail', 'Пожалуйста, не волнуйтесь.', 'Please, do not worry.', [(213, 'Пожалуйста, не волнуйтесь')], 'verbatim'),
    ('mikhail', 'Сейчас мы всё быстро исправим.', 'Right now we will fix everything quickly.', [(213, 'Сейчас все исправим')], 'adapted'),
    ('mikhail', 'Что там, лифт сломался?', 'What is going on there, did the elevator break?', [(215, 'Что там, лифт сломался?')], 'verbatim'),
    ('vika', 'Нет, Михаил, там небольшая проблемка.', 'No, Mikhail, there is a little problem there.', [(216, 'там проблемка')], 'adapted'),
    ('barinov', 'Я проверяю, всё ли готово к открытию.', 'I am checking whether everything is ready for the opening.', [(219, 'проверяю, все ли готово к открытию')], 'verbatim'),
    ('barinov', 'Не хотите к нам присоединиться?', 'Would you not like to join us?', [(220, 'присоединиться?')], 'adapted'),
    ('mikhail', 'Мы так всех гостей потеряем!', 'We will lose all our guests like this!', [(222, 'мы гостей')], 'adapted'),
    ('barinov', 'Если хочешь их сохранить, не лезь!', 'If you want to keep them, stay out of my way!', [(223, 'Если ты хочешь их сохранить, не лезь')], 'adapted'),
    ('vika', 'Господи, да что же вы как дети?', 'Goodness, why are you acting like children?', [(225, 'Господи, да что же вы как дети?')], 'verbatim'),
    ('vika', 'Не можете договориться? Монетку бросьте.', 'Cannot reach an agreement? Toss a coin.', [(226, 'Не можете договориться? Монетку бросьте')], 'verbatim'),
]
WALK = [
    (0, None, "'Oh, good morning, Chef!' Around the shift and argument, Barinov makes his point loud and clear."),
    (1, None, "'Mikhail will give us a restroom as we ask.' Explaining that Mikhail will give them a restroom as they ask lays the cards on the table for Mikhail."),
    (2, None, "'Chef, I only need a tiny moment in there.' Barinov explains that he only needs a tiny moment in there, keeping his voice calm and direct."),
    (3, None, "'Please, do not worry.' Because do not worry, Mikhail treats the matter as settled."),
    (4, None, "'Right now we will fix everything quickly.' Noting that right now they will fix everything quickly keeps Mikhail's side of the story simple and clear."),
    (5, None, '\'What is going on there, did the elevator break?\' Wondering what going on there did the elevator break is cuts straight through the tension between Mikhail and Barinov. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (6, None, "'No, Mikhail, there is a little problem there.' Admitting that there is a little problem there shows Vika being honest for a change."),
    (7, None, "'I am checking whether everything is ready for the opening.' Admitting that he is checking whether everything is ready for the opening shows Barinov being honest for a change."),
    (8, None, '\'Would you not like to join us?\' By checking whether Mikhail not like to join them, Barinov presses Mikhail for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (9, None, "'We will lose all our guests like this!' Once they will lose all their guests like this, Mikhail makes sure Barinov hears every word."),
    (10, None, "'If you want to keep them, stay out of my way!' Declaring that if Mikhail wants to keep them stay out of his way brings Barinov's temper right to the surface. Russian puts the key word right up front so his emotion lands on the first beat."),
    (11, None, '\'Goodness, why are you acting like children?\' Vika asks whether goodness why are Barinov acting like children, refusing to let the point slide. Even in the middle of the drama, she keeps the polite plural "you" that workplace Russian expects.'),
    (12, None, "'Cannot reach an agreement? Toss a coin.' Asking whether cannot reach an agreement puts Barinov right on the defensive."),
]
