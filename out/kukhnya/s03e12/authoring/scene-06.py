# Authoring module for kukhnya-s03e12-scene-06.
ID = 'kukhnya-s03e12-scene-06'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 12
SCENE = 6
TITLE = 'Прапорщик Задов и деньги  (Ensign Zadov and Money)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.12'
SOURCE_FILE = 'sources/kukhnya/s03/e12.ru.srt'
INTRO = "Upstairs at Kirill Ilyich's door, Dmitry Nagiyev introduces himself and offers peace. Unfortunately, the retired officer recognizes Nagiyev from his comedic television role as Ensign Zadov and takes grave offense when Nagiyev offers him money. Listen to their exchange in Russian first."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Offering cash to a proud retired officer who already hates Nagiyev's television character turns out to be a painful mistake. See you next time!"
CLOSING = ('nagiyev', 'До свидания!')
STORY = [
    ('guest', 'Что тебе надо?', 'What do you want?', [(92, 'тебе надо')], 'adapted'),
    ('nagiyev', 'Здравствуйте, меня Дмитрий зовут.', 'Hello, my name is Dmitry.', [(92, 'Меня Дмитрий зовут')], 'adapted'),
    ('guest', 'Так, ты мне знаком.', 'Well, you look familiar to me.', [(93, 'Так, так')], 'adapted'),
    ('guest', 'Это ты, что ли, прапорщик?', 'Wait, are you that warrant officer?', [(94, 'Это ты, что ли, прапорщик')], 'adapted'),
    ('nagiyev', 'Молодец, узнал меня.', 'Well done, you recognized me.', [(96, 'Молодец')], 'adapted'),
    ('nagiyev', 'Я тебе мир предлагаю.', 'I am offering you peace.', [(97, 'Я тебе мир предлагаю')], 'adapted'),
    ('guest', 'Какой ещё тебе мир?', 'What kind of peace for you?', [(98, 'Какой тебе мир')], 'adapted'),
    ('guest', 'Ты всех русских прапорщиков опозорил!', 'You disgraced all Russian warrant officers!', [(99, 'Ты всех русских прапорщиков опозорил')], 'adapted'),
    ('guest', 'Ты всю русскую армию опозорил!', 'You disgraced the entire Russian army!', [(100, 'всю русскую армию')], 'adapted'),
    ('nagiyev', 'Я к тебе правда с миром пришёл.', 'I truly came to you in peace.', [(102, 'Я к тебе, правда, с миром пришел')], 'adapted'),
    ('nagiyev', 'Я просто тебе хотел денег предложить.', 'I just wanted to offer you some money.', [(103, 'Я просто тебе хотел денег предложить')], 'adapted'),
    ('guest', 'Денег мне решил предложить?', 'You decided to offer me money?', [(104, 'Денег'), (105, 'Денег')], 'adapted'),
]
WALK = [
    (0, None, "'What do you want?' By asking what Nagiyev wants, the guest presses Nagiyev for a straight answer. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (1, None, "'Hello, my name is Dmitry.' Explaining that his name is Dmitry lays the cards on the table for the guest."),
    (2, None, '\'Well, you look familiar to me.\' The guest mentions that Nagiyev looks familiar to him so Nagiyev sees what is at stake. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (3, None, '\'Wait, are you that warrant officer?\' Here asking whether Nagiyev that warrant officer shows the guest looking for the real truth. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (4, None, "'Well done, you recognized me.' Between the conversation and the peace, Nagiyev gives the guest a quick, grounded response."),
    (5, None, '\'I am offering you peace.\' Here being offering the guest peace sets up the next turn in their exchange. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (6, None, '\'What kind of peace for you?\' Over the exchange and the peace, the guest presses Nagiyev for a straight answer. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (7, None, "'You disgraced all Russian warrant officers!' Between the exchange and the kitchen, the guest delivers a sharp reaction."),
    (8, None, '\'You disgraced the entire Russian army!\' Around the exchange and moment, the guest makes his point loud and clear. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (9, None, '\'I truly came to you in peace.\' Admitting that he truly came to the guest in peace shows Nagiyev being honest for a change. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (10, None, "'I just wanted to offer you some money.' Saying that he just wanted to offer the guest some money is how Nagiyev sets the tone with the guest."),
    (11, None, '\'You decided to offer me money?\' Wondering if Nagiyev decided to offer him money shows the guest caught off guard. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
]
