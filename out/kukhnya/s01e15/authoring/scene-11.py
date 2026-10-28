ID = "kukhnya-s01e15-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 11
TITLE = "Чудо-исцеление  (Miraculous Healing)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "guest": "angelina"}
LABELS = {'anya': 'Лёва', 'leva': 'Виктор', 'guest': 'Федя'}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "In the kitchen, Leva manages the final orders of the night. Suddenly, Chef Victor reveals that his heart condition was completely faked just to force Leva back to work. Furious, Leva attacks him. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Федя, займись последним заказом.",
     "Fedya, take care of the last order.",
     [(265, 'Последний заказ треска по-бретонски, Федя, займись.')], "adapted"),
    ("anya", "Всё, кухня закрыта.",
     "That is it, the kitchen is closed.",
     [(266, 'Все, кухня закрыта.')], "adapted"),
    ("leva", "Я всегда говорил, что ты самый способный.",
     "I always said that you are the most capable.",
     [(268, 'А я всегда говорил, что из этих инвалидов ты, Лева, самый способный.')], "adapted"),
    ("anya", "Виктор Петрович, у вас больное сердце.",
     "Viktor Petrovich, you have a sick heart.",
     [(269, 'За тебя. Виктор Петрович, сердце, сердце.')], "adapted"),
    ("leva", "Сердце у меня в полном порядке.",
     "My heart is in perfect order.",
     [(270, 'Сердце у меня в порядке, и кухня тоже.')], "adapted"),
    ("anya", "Так вы меня обманули?",
     "So you tricked me?",
     [(272, 'Так вы что, меня обманули?')], "adapted"),
    ("leva", "А как ещё мне тебя вернуть?",
     "And how else could I bring you back?",
     [(273, 'А как бы еще я тебя дурака из твоих бабских обид вернул на кухню?')], "adapted"),
    ("anya", "Ах ты сволочь!",
     "Ah, you bastard!",
     [(276, 'Ах ты сволоча!')], "adapted"),
    ("leva", "Лёва, успокойся!",
     "Leva, calm down!",
     [(280, 'Лова, остынь мы с тобой в разных местовых категориях.')], "adapted"),
    ("anya", "Я тебе сейчас устрою приступ!",
     "I will give you an attack right now!",
     [(282, 'Я тебя сейчас устрою. Это приступ инвалид труда.')], "adapted"),
    ("leva", "Лёва, положи это на место!",
     "Leva, put that in its place!",
     [], "new"),
    ("anya", "Я убью тебя!",
     "I will kill you!",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Fedya, take care of the last order.' — Notice the proper name meaning 'Fedya' paired with the verb for 'to attend to, take care of, engage in'."),
    (1, None,
     "'That is it, the kitchen is closed.' — Notice the det meaning 'everything' paired with the noun for 'kitchen'."),
    (2, None,
     "'I always said that you are the most capable.' — Notice the pronoun meaning 'I' paired with the adverb for 'always'."),
    (3, None,
     "'Viktor Petrovich, you have a sick heart.' — Notice the proper name meaning 'Viktor' paired with the proper name for 'Petrovich'."),
    (4, None,
     "'My heart is in perfect order.' — Notice the noun meaning 'heart (a bad heart)' paired with the pronoun for 'me'."),
    (5, None,
     "'So you tricked me?' — Notice the pronoun meaning 'you' paired with the pronoun for 'me'."),
    (6, None,
     "'And how else could I bring you back?' — Notice the adverb meaning 'how' paired with the adverb for 'more, still'."),
    (7, None,
     "'Ah, you bastard!' — Notice the interjection meaning 'oh' paired with the pronoun for 'you'."),
    (8, None,
     "'Leva, calm down!' — Notice the proper name meaning 'Lyova' paired with the verb for 'calm down'."),
    (9, None,
     "'I will give you an attack right now!' — Notice the pronoun meaning 'I' paired with the pronoun for 'for you, to you'."),
    (10, None,
     "'Leva, put that in its place!' — Notice the proper name meaning 'Lyova' paired with the verb for 'put, place'."),
    (11, None,
     "'I will kill you!' — Notice the pronoun meaning 'I' paired with the verb for 'I'll kill (you)'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("anya", "Я убью тебя!")
