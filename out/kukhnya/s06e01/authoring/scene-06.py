# Authoring module for kukhnya-s06e01-scene-06.
ID = 'kukhnya-s06e01-scene-06'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 6
TITLE = 'Примирение матери и дочери  (Mother and Daughter Reconcile)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'eleonora': 'Элеонора', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'
INTRO = "Eleonora calls her daughter Katya into her suite and admits she was wrong to meddle in Katya's personal life, begging her to attend the wedding and make peace."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Katya accepts her mother's apology on one condition: that Eleonora never again interfere in her personal life. See you next time!"
CLOSING = ('katya', 'До завтра!')
STORY = [
    ('katya', 'Ты хотела меня видеть?', 'Did you want to see me?', [(82, 'Ты хотела меня видеть?')], 'exact'),
    ('eleonora', 'Да, садись.', 'Yes, sit down.', [(83, 'Да. Садись')], 'exact'),
    ('katya', 'Спасибо, я постою.', 'Thank you, I will stand.', [(84, 'Спасибо, я постою')], 'exact'),
    ('eleonora', 'Катя, я понимаю, ты обижена на меня.', 'Katya, I understand you are upset with me.', [(85, 'Катя, я понимаю, ты обижена на меня')], 'exact'),
    ('eleonora', 'Для меня это очень важно.', 'This is very important to me.', [(87, 'для меня это очень важно')], 'adapted'),
    ('katya', 'Извини, не могу, много работы.', 'Sorry, I cannot, there is a lot of work.', [(88, 'Извини, не могу. Много работы')], 'exact'),
    ('eleonora', 'Но я могу дать тебе выходной.', 'But I can give you a day off.', [(89, 'Но я могу дать тебе выходной')], 'exact'),
    ('eleonora', 'Я виновата, я вмешивалась в твою жизнь.', 'I am at fault, I interfered in your life.', [(94, 'Но я виновата. Я вмешивалась в твою жизнь')], 'adapted'),
    ('katya', 'Никита хороший парень, он мне очень нравится.', 'Nikita is a good guy, I really like him.', [(97, 'Никита хороший парень')], 'adapted'),
    ('katya', 'Но ничто не оправдывает его вранья.', 'But nothing excuses his lying.', [(99, 'Ничто не оправдывает его вранья')], 'adapted'),
    ('eleonora', 'Я тебя понимаю, потому что я люблю тебя.', 'I understand you, because I love you.', [(100, 'Я тебя понимаю'), (103, 'потому что я люблю тебя')], 'adapted'),
    ('eleonora', 'Очень люблю, мир?', 'I love you very much, peace?', [(104, 'Очень люблю'), (105, 'Мир')], 'adapted'),
]
WALK = [
    (0, None, '\'Did you want to see me?\' Checking whether Eleonora wants to see is how Katya puts Eleonora on the spot. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (1, None, "'Yes, sit down.' Even though Katya should sit down, Eleonora keeps a steady face in front of Katya."),
    (2, None, "'Thank you, I will stand.' Saying that she will stand is how Katya sets the tone with Eleonora."),
    (3, None, '\'Katya, I understand you are upset with me.\' Even though she understands Katya is upset, Eleonora keeps a steady face in front of Katya. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (4, None, "'This is very important to me.' Admitting that this is very important shows Eleonora being honest for a change."),
    (5, None, "'Sorry, I cannot, there is a lot of work.' Katya tells Eleonora that she cannot there is a lot of work without dressing it up."),
    (6, None, '\'But I can give you a day off.\' Since she can give Katya a day off, Eleonora does not waste words on excuses. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (7, None, "'I am at fault, I interfered in your life.' Eleonora mentions that she is at fault she interfered in Katya's life so Katya sees what is at stake."),
    (8, None, "'Nikita is a good guy, I really like him.' Saying that Nikita is a good guy she really likes him is how Katya sets the tone with Eleonora."),
    (9, None, "'But nothing excuses his lying.' Because nothing excuses his lying, Katya treats the matter as settled."),
    (10, None, "'I understand you, because I love you.' Adding that she understands Katya because she loves Katya fills in the missing piece for Katya."),
    (11, None, '\'I love you very much, peace?\' Wondering if she loves Katya very much peace shows Eleonora caught off guard. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
]
