# Authoring module for kukhnya-s05e01-scene-04.
ID = 'kukhnya-s05e01-scene-04'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 1
SCENE = 4
TITLE = 'Мужской разговор и фрау Краус  (Man-to-Man Advice and Frau Kraus)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'mikhail': 'Михаил', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.01'
SOURCE_FILE = 'sources/kukhnya/s05/e01.ru.srt'
INTRO = 'While Denis asks Senya how to handle his jealousy over Katya, Chef Barinov pursues Mikhail into the hotel lobby where Mikhail is greeting Frau Kraus. Listen closely to the Russian dialogue.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that wraps up the lobby encounter with Frau Kraus. Pay attention to how Russian uses the infinitive with the dative pronoun for 'how should I react'. See you next time!"
CLOSING = ('mikhail', 'Хорошего дня!')
STORY = [
    ('denis', 'Давай по дороге обсудим.', "Let's discuss it on the way.", [(50, 'Давай по дороге обсудим')], 'verbatim'),
    ('denis', 'А как мне реагировать?', 'And how should I react?', [(51, 'а как мне реагировать?')], 'verbatim'),
    ('denis', 'Я же её люблю.', 'After all, I love her.', [(51, 'Я же ее люблю')], 'verbatim'),
    ('denis', 'Это нормально ревновать, нет?', 'Is it normal to be jealous, or not?', [(52, 'Это нормально ревновать, нет?')], 'verbatim'),
    ('senya', 'Конечно, это нормально.', 'Of course it is normal.', [(53, 'Конечно, нормально')], 'adapted'),
    ('senya', 'У них ревнуешь — плохо.', 'With them, if you are jealous, it is bad.', [(54, 'У них ревнуешь плохо')], 'verbatim'),
    ('denis', 'И как мне быть?', 'And what should I do?', [(56, 'И как быть?')], 'adapted'),
    ('senya', 'Возьми, подойди к нему.', 'Go ahead and walk up to him.', [(57, 'Возьми, подойди к нему')], 'verbatim'),
    ('mikhail', 'Пойми, Витя, завтра открытие.', 'Understand, Vitya, the opening is tomorrow.', [(60, 'Пойми, Витя, завтра открытие')], 'verbatim'),
    ('mikhail', 'Наш отель должен удивить гостей.', 'Our hotel must surprise the guests.', [(61, 'Наш отель должен удивить гостей')], 'verbatim'),
    ('senya', 'Ресторан наш не трогай.', 'Do not touch our restaurant.', [(63, 'Ресторан не трогай')], 'adapted'),
    ('mikhail', 'Как вы провели эту ночь?', 'How did you spend this night?', [(68, 'Как вы провели эту ночь?')], 'verbatim'),
    ('mikhail', 'О, вижу, что получили.', 'Oh, I see that you received it.', [(71, 'О, вижу, что получили')], 'verbatim'),
    ('mikhail', 'Он только что расстался с другом.', 'He just broke up with his friend.', [(75, 'Он только что расстался')], 'adapted'),
]
WALK = [
    (0, None, "'Let's discuss it on the way.' Discussing it on the way together moves the conversation forward without extra drama."),
    (1, None, '\'And how should I react?\' Asking how he react should is how Denis puts Mikhail on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, "'After all, I love her.' Denis mentions that after all he loves so Mikhail sees what is at stake."),
    (3, None, "'Is it normal to be jealous, or not?' By checking whether it normal to be jealous or not, Denis presses Mikhail for a straight answer."),
    (4, None, '\'Of course it is normal.\' Noting that it is normal keeps Senya\'s side of the story simple and clear. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (5, None, '\'With them, if you are jealous, it is bad.\' Even though with them if Denis is jealous it is bad, Senya keeps a steady face in front of Denis. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (6, None, "'And what should I do?' Here wondering what he does should shows Denis looking for the real truth."),
    (7, None, "'Go ahead and walk up to him.' Here telling Denis to go ahead and walk up to him sets up the next turn in their exchange."),
    (8, None, "'Understand, Vitya, the opening is tomorrow.' Since Denis should understand Vitya the opening is tomorrow, Mikhail does not waste words on excuses."),
    (9, None, "'Our hotel must surprise the guests.' Adding that their hotel must surprise the guests fills in the missing piece for Denis."),
    (10, None, "'Do not touch our restaurant.' Saying that do not touch their restaurant is how Senya sets the tone with Denis."),
    (11, None, '\'How did you spend this night?\' By wondering how Denis spends this night, Mikhail presses Denis for a straight answer. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (12, None, "'Oh, I see that you received it.' Mikhail explains that he sees that Denis received it, keeping his voice calm and direct."),
    (13, None, "'He just broke up with his friend.' Around the hotel and guest, Mikhail sets a calm, everyday tone with Denis."),
]
