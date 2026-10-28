# Authoring module for kukhnya-s03e01-scene-17.
ID = 'kukhnya-s03e01-scene-17'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 1
SCENE = 17
TITLE = 'Неожиданная новость  (Unexpected News)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.01'
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'
INTRO = "While Nastya's father is in the restroom, he overhears his partners scheming to cheat him with a duplicate contract, and when Nastya runs out to warn him, Kostya blurts out their biggest secret."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes Scene Seventeen. Listen for Kostya stepping forward to tell Nastya's stunned father that he is about to become a grandfather. Until next time!"
CLOSING = ('kostya', 'Хорошего дня!')
STORY = [
    ('guest', 'У нас есть дубликаты. Сейчас подпишем.', 'We have duplicate copies. We will sign now.', [(297, 'У нас есть дубликаты. Сейчас подпишем')], ''),
    ('guest', 'Хорошо, я вас за столиком жду.', 'Good, I am waiting for you at the table.', [(298, 'Хорошо, я вас за столиком жду')], ''),
    ('guest', 'Зачем шампанское попросил?', 'Why did you ask for champagne?', [(299, 'Зачем шампанское попросил')], ''),
    ('guest', 'Не мог подождать, пока подпишем?', "Couldn't you wait until we signed?", [(300, 'Не мог подождать, пока подпишем')], ''),
    ('guest', 'А если он заметит?', 'And what if he notices?', [(302, 'А если он заметит')], ''),
    ('guest', 'Ничего он не заметит. Мне он доверяет.', "He won't notice anything. He trusts me.", [(304, 'Ничего он не заметит'), (304, 'он доверяет')], 'adapted'),
    ('guest', 'Сейчас всё подпишем, и бизнес наш.', 'We will sign everything now, and the business is ours.', [(305, 'Сейчас все подпишем. И бизнес наш')], ''),
    ('guest', 'Давайте уже второй экземпляр.', 'Give me the second copy already.', [(306, 'Давайте уже второй экземпляр')], ''),
    ('nastya', 'Папа, они хотят тебя обмануть!', 'Dad, they want to cheat you!', [(308, 'тебя обмануть')], 'adapted'),
    ('guest', 'Ты что, беременна?', 'What, are you pregnant?', [(310, 'Ты что, беременна')], ''),
    ('kostya', 'Да, она беременна, вы станете дедушкой!', 'Yes, she is pregnant, you will become a grandfather!', [(311, 'Да. Она беременна, вы станете дедушкой')], ''),
    ('kostya', 'Мы скоро поженимся. Честное слово.', 'We are getting married soon. Word of honor.', [(313, 'скоро поженимся'), (314, 'Честное слово')], 'adapted'),
]
WALK = [
    (0, None, '\'We have duplicate copies. We will sign now.\' Saying that they have duplicate copies is how the guest sets the tone with Kostya. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (1, None, '\'Good, I am waiting for you at the table.\' Once good he is waiting for Kostya at the table, the guest can finally tell Kostya what he means. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (2, None, "'Why did you ask for champagne?' Asking why Kostya asks for champagne is how the guest puts Kostya on the spot."),
    (3, None, '\'Couldn\'t you wait until we signed?\' Here asking whether not Kostya waits until they signed shows the guest looking for the real truth. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (4, None, '\'And what if he notices?\' Asking whether what if he notices puts Kostya right on the defensive. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (5, None, "'He won't notice anything. He trusts me.' Mentioning that he will not notice anything moves the talk in a new direction."),
    (6, None, "'We will sign everything now, and the business is ours.' The guest reminds Kostya that they will sign everything now and the business is before the moment passes."),
    (7, None, '\'Give me the second copy already.\' Adding that Kostya should give him the second copy already fills in the missing piece for Kostya. Starting with "davay" is the everyday Russian way to say "come on, let us do this".'),
    (8, None, "'Dad, they want to cheat you!' Around the moment and contract, Nastya makes her point loud and clear."),
    (9, None, '\'What, are you pregnant?\' Wondering what Kostya pregnant is cuts straight through the tension between the guest and Kostya. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (10, None, '\'Yes, she is pregnant, you will become a grandfather!\' Once she is pregnant the guest will become a grandfather, Kostya makes sure the guest hears every word. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (11, None, "'We are getting married soon. Word of honor.' Pointing out that they are getting married soon gives the guest a sobering reality check."),
]
