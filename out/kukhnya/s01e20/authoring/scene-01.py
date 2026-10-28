# Authoring module for kukhnya-s01e20-scene-01.
ID = 'kukhnya-s01e20-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 1
TITLE = 'Утро после  (The Morning After)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = "Vika prepares coffee in the morning while Max searches for his old watch. Max does not realize it is Vika's birthday. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the exchange around The Morning After line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max remains completely unaware of Vika's special day, focusing only on his broken antique watch. Next time you watch the episode, listen for the Russian expressions for 'to be' and 'celebrate' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('vika', 'Я не буду отмечать день рождения.', 'I will not celebrate my birthday.', [(32, 'не буду я отмечать')], ''),
    ('vika', 'И дарить мне ничего не надо.', 'And there is no need to gift me anything.', [(34, 'дарить ничего не надо')], ''),
    ('vika', 'Может, мы просто посидим с Максом.', 'Maybe we will just sit with Max.', [(36, 'с Максом просто посидим')], ''),
    ('max', 'Я даже не знал про праздник.', 'I did not even know about the holiday.', [], ''),
    ('max', 'Я только проснулся.', 'I just woke up.', [(39, 'проснулся')], ''),
    ('vika', 'А я уже кофе сварила.', 'And I already brewed coffee.', [(41, 'кофе сварила')], ''),
    ('max', 'Доброе утро, спасибо за кофе.', 'Good morning, thank you for the coffee.', [(42, 'Доброе утро')], ''),
    ('max', 'А ты часы мои не видела?', 'And have you not seen my watch?', [(43, 'часы мои не видела')], ''),
    ('vika', 'А, ты вот про эти часы?', 'Ah, you mean this watch?', [(44, 'ты вот про эти')], ''),
    ('vika', 'Может, тебе купить новые?', 'Maybe buy you a new one?', [(45, 'тебе новые купить')], ''),
    ('vika', 'Эти часы уже еле ходят.', 'This watch already barely works.', [(45, 'уже еле ходят')], ''),
    ('max', 'Нет, это мой дедовский антиквариат.', "No, this is my grandfather's antique.", [(46, 'дедовский антиквариат')], ''),
]
WALK = [
    (0, None, "'I will not celebrate my birthday.' Vika declares her intention to skip the festivities."),
    (1, None, "'And there is no need to gift me anything.' Vika explicitly tells him not to buy her anything."),
    (2, None, "'Maybe we will just sit with Max.' Vika suggests a quiet alternative plan."),
    (3, None, "'I did not even know about the holiday.' Max admits his complete ignorance of the occasion."),
    (4, None, "'I just woke up.' Max uses his recent awakening as an excuse."),
    (5, None, "'And I already brewed coffee.' Vika points out she has already started the day's tasks."),
    (6, None, "'Good morning, thank you for the coffee.' Max greets her and shows appreciation for her effort."),
    (7, None, "'And have you not seen my watch?' Max casually shifts the topic to his missing item."),
    (8, None, "'Ah, you mean this watch?' Vika points out the item in question."),
    (9, None, "'Maybe buy you a new one?' Vika suggests replacing the old item."),
    (10, None, "'This watch already barely works.' Vika justifies her suggestion by noting its poor condition."),
    (11, None, "'No, this is my grandfather's antique.' Max defends the item due to its sentimental family value."),
]
