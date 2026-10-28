# Authoring module for kukhnya-s04e13-scene-08.
ID = 'kukhnya-s04e13-scene-08'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 13
SCENE = 8
TITLE = "Донесение Сени  (Senya's Tip-Off)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.13'
SOURCE_FILE = 'sources/kukhnya/s04/e13.ru.srt'
INTRO = "Never one to miss a chance to stir up trouble for a reward, Senya hurries over to Chef Barinov with fresh intelligence from Claude Monet. When he reveals that Katya has joined German Land's kitchen brigade, Barinov explodes and storms straight next door."
OPENER = "Let's examine how Senya bargains with Chef Barinov and delivers the news about Katya."
TRANSITION = 'Now listen to the entire tip-off scene between Senya and Chef Barinov at natural speed.'
OUTRO = "Terrified of Katya's temper, Senya begs Chef Barinov not to reveal who ratted her out. Next, we watch Barinov barge into Claude Monet to confront his daughter. See you next time!"
CLOSING = ('senya', 'Всего хорошего!')
STORY = [
    ('senya', 'Шеф, у меня для вас информация.', 'Chef, I have information for you.', [(80, 'Шеф, у меня для')], 'adapted'),
    ('barinov', 'Выкладывай быстро, о чём идёт речь?', 'Spill it quickly, what is it about?', [(81, 'Выкладывай. А счет Кати.')], 'adapted'),
    ('senya', 'Это важная новость насчёт вашей Кати.', 'This is important news regarding your Katya.', [(81, 'Выкладывай. А счет Кати.')], 'adapted'),
    ('senya', 'Она вам об этом не сказала.', 'She did not tell you about this.', [(82, 'Ты так и знал,')], 'adapted'),
    ('senya', 'А что мне за это будет?', 'And what will I get for this?', [(83, 'Ксения, не тайми. Что')], 'adapted'),
    ('barinov', 'Сеня, не томи, давай говори уже!', 'Senya, do not drag it out, speak up already!', [(84, 'По башке тебе будет.')], 'adapted'),
    ('senya', 'Ладно, только вам это не понравится.', 'All right, only you will not like this.', [(85, 'Ладно, только вам это')], 'adapted'),
    ('barinov', 'Ты что, издеваешься надо мной?', 'Are you making fun of me or what?', [(86, 'Лох, как не понравится.')], 'adapted'),
    ('senya', 'Она теперь под его покровительством.', 'She is now under his protection.', [(88, 'Ну, в смысле, она')], 'adapted'),
    ('senya', 'Ваша Катя устроилась работать в Моне.', 'Your Katya got a job working at Monet.', [(89, 'Устроилась в манэ.')], 'adapted'),
    ('barinov', 'Ну и как она так могла?', 'Well, how could she do that?', [(91, 'Ты как она могла,')], 'adapted'),
    ('senya', 'Шеф, вы куда сейчас идёте?', 'Chef, where are you going right now?', [(93, 'Шеф, вы куда, шеф?')], 'adapted'),
    ('senya', 'Только не говорите, что я рассказал!', 'Just do not say that I told you!', [(94, 'Вы только не говорите,')], 'adapted'),
]
WALK = [
    (0, None, '\'Chef, I have information for you.\' Here having information for Barinov sets up the next turn in their exchange. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (1, None, '\'Spill it quickly, what is it about?\' Wondering if spill it quickly what is it shows Barinov caught off guard. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, "'This is important news regarding your Katya.' Claiming that this is important news regarding Barinov's Katya sounds confident, even if Barinov has doubts."),
    (3, None, '\'She did not tell you about this.\' Pointing out that she did not tell Barinov about this gives Barinov a sobering reality check. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (4, None, '\'And what will I get for this?\' Wondering what he gets for this will cuts straight through the tension between Senya and Barinov. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (5, None, "'Senya, do not drag it out, speak up already!' Saying that do not drag it out speak up already is how Barinov takes charge of the moment."),
    (6, None, '\'All right, only you will not like this.\' Noting that all right only Barinov will not like this keeps Senya\'s side of the story simple and clear. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (7, None, '\'Are you making fun of me or what?\' By checking whether Senya making fun of him, Barinov presses Senya for a straight answer. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (8, None, "'She is now under his protection.' Admitting that she is now under his protection shows Senya being honest for a change."),
    (9, None, '\'Your Katya got a job working at Monet.\' Saying that Barinov\'s Katya got a job working at Monet is how Senya sets the tone with Barinov. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (10, None, '\'Well, how could she do that?\' Here wondering how she do could shows Barinov looking for the real truth. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (11, None, "'Chef, where are you going right now?' By asking where Barinov going right now is, Senya presses Barinov for a straight answer."),
    (12, None, "'Just do not say that I told you!' Saying that just do not say that he told Barinov is how Senya takes charge of the moment. Russian puts the key word right up front so his emotion lands on the first beat."),
]
