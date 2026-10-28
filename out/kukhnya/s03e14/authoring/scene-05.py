# Authoring module for kukhnya-s03e14-scene-05.
ID = 'kukhnya-s03e14-scene-05'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 14
SCENE = 5
TITLE = 'Вызов на разговор и взятка  (Summoned for a Talk and a Bribe)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.14'
SOURCE_FILE = 'sources/kukhnya/s03/e14.ru.srt'
INTRO = 'At Table Seven, the driver and his tough friends order Max to step outside with them, so Max stalls by claiming he has a dish to finish stuffing. Meanwhile, Chef Barinov offers Stas one hundred thousand rubles to leave Katya. Listen first.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Stas happily pockets the money—wait until Katya finds out what her father just did! Until next time!'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('guest', 'О, а вот и наш герой пришёл.', 'Oh, and here comes our hero.', [(65, 'О, а вот и наш герой')], 'adapted'),
    ('guest', 'Присядешь с нами на дорожку?', 'Will you sit down with us for the road?', [(66, 'Присядешь на дорожку')], 'adapted'),
    ('max', 'Нам в зале не положено садиться.', 'We are not allowed to sit down in the dining room.', [(66, 'Нам вообще не положено садиться')], 'adapted'),
    ('guest', 'Ну тогда пойдём выйдем, приляжешь.', "Well then let's step outside and you can lie down.", [(67, 'Ну тогда пойдем выйдем, приляжешь')], 'adapted'),
    ('guest', 'Пойдём на улицу, разговор есть.', "Let's go outside, we have something to discuss.", [(68, 'Пойдем, разговор есть')], 'adapted'),
    ('max', 'Хорошо, только у меня там блюдо на кухне.', 'Alright, only I have a dish in the kitchen.', [(69, 'Хорошо, только у меня там блюдо')], 'adapted'),
    ('max', 'Я его сейчас дофарширую и сразу выйду.', 'I will finish stuffing it right now and come right out.', [(69, 'я его сейчас дофарширую, выйду')], 'adapted'),
    ('guest', 'Иди давай, мы тебя ждём на улице.', 'Go on then, we are waiting for you outside.', [(71, 'Иди давай, мы тебя ждем уже')], 'adapted'),
    ('max', 'Здорово, батя, зачем ты звонил?', 'Hey, pops, why did you call?', [(73, 'Здорово, батя')], 'adapted'),
    ('max', 'Вчера как-то неудобно у нас получилось.', 'Things turned out rather awkwardly between us yesterday.', [(75, 'вчера как-то неудобно получилось')], 'adapted'),
    ('barinov', 'Тебе нужны деньги, а мне нужна дочь.', 'You need money, and I need my daughter.', [(77, 'Тебе ж нужны деньги, а мне нужна дочь')], 'adapted'),
    ('max', 'Понял, а сколько здесь денег?', 'Got it, and how much money is here?', [(78, 'А сколько здесь')], 'adapted'),
    ('barinov', 'Здесь ровно сто тысяч рублей.', 'There is exactly one hundred thousand rubles here.', [(79, 'Сто тысяч')], 'adapted'),
    ('max', 'А у тебя ещё дочки есть?', 'Do you have any more daughters?', [(81, 'А у тебя еще дочки есть')], 'adapted'),
]
WALK = [
    (0, None, "'Oh, and here comes our hero.' Admitting that here comes their hero shows the guest being honest for a change."),
    (1, None, '\'Will you sit down with us for the road?\' By checking whether Barinov sits down with them for the road, the guest presses Barinov for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, "'We are not allowed to sit down in the dining room.' Once they are not allowed to sit down in the dining room, Max can finally tell Barinov what he means."),
    (3, None, "'Well then let's step outside and you can lie down.' Proposing that they step outside and Barinov can lie down is how the guest lays out the situation for Barinov."),
    (4, None, "'Let's go outside, we have something to discuss.' Noting that they should go outside they have something to discuss keeps the guest's side of the story simple and clear."),
    (5, None, "'Alright, only I have a dish in the kitchen.' Since Alright only he has a dish in the kitchen, Max does not waste words on excuses."),
    (6, None, "'I will finish stuffing it right now and come right out.' Mentioning that he will finish stuffing it right now and come right out moves the talk in a new direction."),
    (7, None, '\'Go on then, we are waiting for you outside.\' Because Barinov should go on then they are waiting for Barinov outside, the guest treats the matter as settled. Starting with "davay" is the everyday Russian way to say "come on, let us do this".'),
    (8, None, "'Hey, pops, why did you call?' When Max asks if pops why did Barinov calls, Barinov has to answer fast."),
    (9, None, '\'Things turned out rather awkwardly between us yesterday.\' Explaining that things turned out rather awkwardly between them yesterday lays the cards on the table for Barinov. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (10, None, '\'You need money, and I need my daughter.\' Barinov mentions that the guest needs money and he needs his daughter so the guest sees what is at stake. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (11, None, "'Got it, and how much money is here?' Wondering if got it and how much money is here shows Max caught off guard."),
    (12, None, "'There is exactly one hundred thousand rubles here.' Pointing out that there is exactly one hundred thousand rubles here gives the guest a sobering reality check."),
    (13, None, '\'Do you have any more daughters?\' By checking whether Barinov has any more daughters, Max presses Barinov for a straight answer. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
]
