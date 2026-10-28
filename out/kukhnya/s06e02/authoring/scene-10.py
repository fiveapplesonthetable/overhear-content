# Authoring module for kukhnya-s06e02-scene-10.
ID = 'kukhnya-s06e02-scene-10'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 10
TITLE = 'Катя отшивает обоих  (Katya Rejects Both of Them)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'katya': 'Катя', 'nikita': 'Никита'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'
INTRO = "At the party, Nikita asks to drink with Katya and gets a sarcastic toast about her mother's advice; moments later, Denis tries his luck and gets toasted as a runaway coward."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Still unaware that they are both pining for Katya, Nikita and Denis bond over their stubborn girlfriends. See you next time!'
CLOSING = ('denis', 'Пока!')
STORY = [
    ('nikita', 'Катя, я могу с тобой выпить?', 'Katya, may I have a drink with you?', [(160, 'Катя, я могу с тобой выпить?')], 'exact'),
    ('katya', 'Давай за мою маму и за ее мудрые советы.', "Let's drink to my mom and her wise advice.", [(161, 'Давай за мою маму и за ее мудрые советы')], 'exact'),
    ('katya', 'Ведь ты без них никуда, свободен.', 'After all, you are nowhere without them, dismissed.', [(162, 'Ведь ты без них никуда'), (163, 'Свободен')], 'adapted'),
    ('denis', 'Катя, привет.', 'Katya, hi.', [(164, 'Катя. Привет')], 'exact'),
    ('katya', 'Тоже выпить со мной хочешь, да?', 'You want to have a drink with me too, right?', [(165, 'Тоже выпить со мной хочешь, да?')], 'exact'),
    ('katya', 'За тех, которые сбегают, выпьешь?', 'To those who run away, will you drink?', [(167, 'которые сбегают'), (168, 'Выпьешь?')], 'adapted'),
    ('denis', 'Нет, за это не буду.', 'No, I will not drink to that.', [(168, 'Нет')], 'adapted'),
    ('katya', 'А я выпью, у тебя это очень хорошо получается.', 'Well I will drink, you are very good at that.', [(169, 'А я выпью'), (170, 'Ведь у тебя это очень хорошо получается')], 'adapted'),
    ('denis', 'Она права, я виноват.', 'She is right, I am at fault.', [(171, 'Она права, я виноват')], 'exact'),
    ('nikita', 'Это не повод так долго обижаться.', 'That is no reason to stay offended for so long.', [(172, 'не повод так долго обижаться')], 'adapted'),
    ('denis', 'Я не понял, она у нас работает?', 'I do not understand, does she work here with us?', [(174, 'Я не понял, она у нас работает?')], 'exact'),
    ('nikita', 'Моя тоже тут работает.', 'Mine works here too.', [(175, 'Моя тоже')], 'adapted'),
]
WALK = [
    (0, None, "'Katya, may I have a drink with you?' Wondering if may he has a drink with Denis shows Nikita caught off guard."),
    (1, None, '\'Let\'s drink to my mom and her wise advice.\' Drinking to her and her wise advice together is how Katya lays out the situation for Denis. Starting with "davay" is the everyday Russian way to say "come on, let us do this".'),
    (2, None, '\'After all, you are nowhere without them, dismissed.\' Claiming that after all Denis is nowhere without them dismissed sounds confident, even if Denis has doubts. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (3, None, "'Katya, hi.' With the truth and party in play, Denis keeps this short reply brisk and direct."),
    (4, None, '\'You want to have a drink with me too, right?\' Questioning whether Denis wants to have a drink with her too right is how Katya tests Denis\'s story. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (5, None, '\'To those who run away, will you drink?\' When Katya asks if to those who run away will Denis drinks, Denis has to answer fast. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (6, None, "'No, I will not drink to that.' Saying that he will not drink is how Denis sets the tone with Katya."),
    (7, None, '\'Well I will drink, you are very good at that.\' Once she will drink Denis is very good, Katya can finally tell Denis what she means. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (8, None, "'She is right, I am at fault.' Adding that she is right he is at fault fills in the missing piece for Katya."),
    (9, None, "'That is no reason to stay offended for so long.' Saying that that is no reason to stay offended for so long is how Nikita sets the tone with Denis."),
    (10, None, '\'I do not understand, does she work here with us?\' Over the work and the party, Denis presses Katya for a straight answer. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (11, None, "'Mine works here too.' Mentioning that his works here moves the talk in a new direction."),
]
