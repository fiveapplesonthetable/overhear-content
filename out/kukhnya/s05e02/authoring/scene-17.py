# Authoring module for kukhnya-s05e02-scene-17.
ID = 'kukhnya-s05e02-scene-17'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 2
SCENE = 17
TITLE = 'Месть лжеревизору  (Payback for the Fake Inspector)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.02'
SOURCE_FILE = 'sources/kukhnya/s05/e02.ru.srt'
INTRO = 'Convinced that the guest in room 313 is just a freeloader who exploited them for two days, Chef Barinov and Mikhail barge into his suite to force-feed him coffee and steaks. Listen to the confrontation.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that captures Barinov and Mikhail's disastrous revenge in room 313. Notice how Barinov calls the guest 'Khlestakov' and 'revizor' after Gogol's famous play 'The Government Inspector'. Until next time!"
CLOSING = ('guest', 'Увидимся!')
STORY = [
    ('barinov', 'А вот и наш дорогой гость.', 'And here is our dear guest.', [(211, 'мой гость')], 'adapted'),
    ('barinov', 'Мы вам горячий кофе принесли.', 'We brought you hot coffee.', [(212, 'Мы вам кофе принесли')], 'adapted'),
    ('mikhail', 'Пожалуйста, вот ваш лучший кофе.', 'Here you go, here is your finest coffee.', [(215, 'Пожалуйста, ваш кофе')], 'adapted'),
    ('guest', 'Я не понял, что здесь происходит?', 'I do not understand, what is going on here?', [(216, 'я не понял, что здесь происходит?')], 'verbatim'),
    ('guest', 'Вы что творите, вы чего?', 'What are you doing, what is with you?', [(217, 'Да! Вы чего?')], 'adapted'),
    ('guest', 'Вы что, совсем с ума сошли?', 'Have you completely lost your minds?', [(218, 'Вы что, с ума сошли?')], 'verbatim'),
    ('barinov', 'Пей давай свой вкусный кофе!', 'Drink up your delicious coffee!', [(218, 'Поешь')], 'adapted'),
    ('guest', 'Что вы себе здесь позволяете?', 'What are you allowing yourselves here?', [(219, 'Что себе')], 'adapted'),
    ('mikhail', 'Витя, дай ему немного дышать.', 'Vitya, let him breathe a little.', [(219, 'Дай ему дышать')], 'adapted'),
    ('mikhail', 'Подожди, дай ему спокойно дышать.', 'Wait, let him breathe calmly.', [(220, 'Дай ему дышать')], 'adapted'),
    ('barinov', 'А куда пропал весь кофе?', 'And where did all the coffee go?', [(221, 'А там все кофе, а?')], 'adapted'),
    ('barinov', 'Держи этого хитрого ревизора!', 'Hold that clever inspector!', [(222, 'Держи ревизора')], 'adapted'),
]
WALK = [
    (0, None, "'And here is our dear guest.' Barinov tells the guest that here is their dear guest without dressing it up."),
    (1, None, '\'We brought you hot coffee.\' Because they brought the guest hot coffee, Barinov treats the matter as settled. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (2, None, "'Here you go, here is your finest coffee.' Explaining that here Barinov goes here is Barinov's finest coffee lays the cards on the table for Barinov."),
    (3, None, '\'I do not understand, what is going on here?\' When the guest asks if he does not understand what is going on here, Barinov has to answer fast. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (4, None, '\'What are you doing, what is with you?\' Here wondering what Barinov doing what is with Barinov is shows the guest looking for the real truth. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (5, None, "'Have you completely lost your minds?' Over the conversation and the inspector, the guest presses Barinov for a straight answer."),
    (6, None, '\'Drink up your delicious coffee!\' Here drinking up the guest\'s delicious coffee lets Barinov\'s real feelings break through. Starting with "davay" is the everyday Russian way to say "come on, let us do this".'),
    (7, None, '\'What are you allowing yourselves here?\' Asking what Barinov allowing yourselves here is is how the guest puts Barinov on the spot. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (8, None, "'Vitya, let him breathe a little.' Telling Barinov to let him breathe a little moves the conversation forward without extra drama."),
    (9, None, "'Wait, let him breathe calmly.' Because Barinov should let him breathe calmly, Mikhail treats the matter as settled."),
    (10, None, '\'And where did all the coffee go?\' Asking where all the coffee go cuts straight through the tension between Barinov and the guest. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (11, None, "'Hold that clever inspector!' Barinov insists that the guest should hold that clever inspector, leaving the guest no room to argue."),
]
