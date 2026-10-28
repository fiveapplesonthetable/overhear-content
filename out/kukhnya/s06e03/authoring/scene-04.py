# Authoring module for kukhnya-s06e03-scene-04.
ID = 'kukhnya-s06e03-scene-04'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 3
SCENE = 4
TITLE = 'Вызов на футбольный матч  (Challenge to a Football Match)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'nikita': 'Никита', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.03'
SOURCE_FILE = 'sources/kukhnya/s06/e03.ru.srt'
INTRO = 'Back in the hotel courtyard, Nikita tells Denis he might as well go home since Nagiyev is filming all day, and the bored chefs challenge the waiters to a game of football.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Stung by Nikita's taunt in front of Katya, Denis joins the football match while disaster strikes on Nagiyev's film set inside. See you next time!"
CLOSING = ('denis', 'До свидания!')
STORY = [
    ('nikita', 'Нагиев сегодня кино снимает.', 'Nagiyev is filming a movie today.', [(58, 'Нагиев кино снимает')], 'adapted'),
    ('nikita', 'Работы не будет, можешь идти домой.', 'There will be no work, you can go home.', [(59, 'не будет. Так что можешь домой')], 'adapted'),
    ('denis', 'Тебя забыл спросить.', 'I forgot to ask you.', [(60, 'Тебя забыл спросить')], 'exact'),
    ('denis', 'Да сколько можно?', 'How much longer can this go on?', [(62, 'Сколько можно')], 'adapted'),
    ('senya', 'Извините, мы нечаянно.', 'Sorry, we did it accidentally.', [(63, 'Извините, мы нечаянно')], 'exact'),
    ('senya', 'Слушай, кино Нагиева, и канализация засорилась.', "Listen, Nagiyev's movie is here, and the plumbing got clogged.", [(64, 'кино Нагиева и канализация засорилась')], 'adapted'),
    ('senya', 'Не думаю, что это просто так.', 'I do not think that is a coincidence.', [(65, 'Не думаю')], 'adapted'),
    ('senya', 'Я тут подумал, может, в футбол сыграем?', 'I was just thinking, maybe we should play football?', [(66, 'я тут подумал'), (67, 'может, в футбол сыграем?')], 'adapted'),
    ('denis', 'Не хочу я играть.', 'I do not want to play.', [(68, 'Не хочу')], 'adapted'),
    ('nikita', 'Да он просто испугался.', 'Why, he just got scared.', [(69, 'Да он просто испугался')], 'exact'),
    ('denis', 'Ладно, давай сыграем.', "Fine, let's play.", [(70, 'Давай, сыграем')], 'adapted'),
    ('senya', 'А подайте мяч, пожалуйста.', 'Pass the ball, please.', [(71, 'А подайте мяч, пожалуйста')], 'exact'),
]
WALK = [
    (0, None, "'Nagiyev is filming a movie today.' Because Nagiyev is filming a movie today, Nikita treats the matter as settled."),
    (1, None, "'There will be no work, you can go home.' Mentioning that there will be no work Denis can go home moves the talk in a new direction."),
    (2, None, '\'I forgot to ask you.\' Denis mentions that he forgot to ask Nikita so Nikita sees what is at stake. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (3, None, "'How much longer can this go on?' Asking whether how much longer can this go puts Nikita right on the defensive."),
    (4, None, "'Sorry, we did it accidentally.' Pointing out that they did it accidentally gives Denis a sobering reality check."),
    (5, None, "'Listen, Nagiyev's movie is here, and the plumbing got clogged.' Senya explains that Nagiyev movie is here and the plumbing got clogged, keeping his voice calm and direct."),
    (6, None, "'I do not think that is a coincidence.' Realizing that he does not think that is a coincidence changes how Senya handles the situation."),
    (7, None, '\'I was just thinking, maybe we should play football?\' Senya asks whether he was just thinking maybe they should play football, refusing to let the point slide. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (8, None, "'I do not want to play.' With the point and match in play, Denis keeps this short reply brisk and direct."),
    (9, None, "'Why, he just got scared.' Admitting that why he just got scared shows Nikita being honest for a change."),
    (10, None, '\'Fine, let\'s play.\' Saying that fine let them play is how Denis sets the tone with Nikita. Starting with "davay" is the everyday Russian way to say "come on, let us do this".'),
    (11, None, "'Pass the ball, please.' Here passing the ball please sets up the next turn in their exchange."),
]
