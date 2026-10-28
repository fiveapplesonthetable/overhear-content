# Authoring module for kukhnya-s03e03-scene-14.
ID = 'kukhnya-s03e03-scene-14'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 3
SCENE = 14
TITLE = 'Кто на кухне главный  (Who Is Boss in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'rodion': 'Родион', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.03'
SOURCE_FILE = 'sources/kukhnya/s03/e03.ru.srt'
INTRO = 'Outside the fitness club, Vika calls Max and overhears him coaching Rodion Sergeyevich, while back at the restaurant Katya demands that her father tell the cooks the truth.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "That brings Scene Fourteen to a close. Watch how Barinov's refusal to back down pushes Katya to make an announcement to the entire kitchen. See you next time!"
CLOSING = ('rodion', 'До встречи!')
STORY = [
    ('max', 'Опаздываете, Родион Сергеевич!', 'You are late, Rodion Sergeyevich!', [(239, 'Родион Сергеевич')], 'adapted'),
    ('vika', 'Алло, Макс, почему ты не на работе?', "Hello, Max, why aren't you at work?", [(242, 'Алло, Макс, почему ты не на работе')], ''),
    ('max', 'Мы тут с Родионом Сергеевичем пытаемся кое-кого спасти от увольнения.', 'Rodion Sergeyevich and I are here trying to save someone from getting fired.', [(243, 'мы тут с'), (243, 'пытаемся кое-кого спасти от увольнения')], 'adapted'),
    ('vika', 'Даже не думай!', "Don't even think about it!", [(244, 'Даже не думай')], ''),
    ('max', 'Извини, не могу говорить. Кино сейчас начнётся.', 'Sorry, I cannot talk. The movie is about to start.', [(245, 'Извини, не могу говорить. Кино')], 'adapted'),
    ('vika', 'Алло, Макс! Идиоты.', 'Hello, Max! Idiots.', [(246, 'Алло, Макс'), (247, 'Идиоты')], 'adapted'),
    ('vika', 'Ангелина, мне нужно отъехать ненадолго.', 'Angelina, I need to step out for a short while.', [(248, 'Ангелина, мне нужно отъехать ненадолго')], ''),
    ('rodion', 'Я не понял, ты что творишь?', "I don't understand, what are you doing?", [(249, 'Я не понял, ты что творишь')], ''),
    ('vika', 'Сейчас же иди и скажи им правду, я требую!', 'Go right now and tell them the truth, I demand it!', [(251, 'Сейчас же иди и скажи им правду, я требую')], ''),
    ('rodion', 'Здесь могу требовать только я, потому что это моя кухня.', 'Only I can make demands here, because this is my kitchen.', [(252, 'Здесь могу требовать только я, потому что это моя кухня')], ''),
    ('rodion', 'И здесь будет только так, как я сказал.', 'And here things will only be the way I said.', [(253, 'И здесь будет только так, как я сказал')], ''),
    ('vika', 'Это мы ещё посмотрим!', 'We will see about that yet!', [(254, 'Это мы еще посмотрим')], ''),
]
WALK = [
    (0, None, "'You are late, Rodion Sergeyevich!' Following up boldly with Rodion, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (1, None, "'Hello, Max, why aren't you at work?' Vika prompts frankly to see how Max will answer on the spot."),
    (2, None, '\'Rodion Sergeyevich and I are here trying to save someone from getting fired.\' Highlighting the dismissal right here, Max chooses "uvolneniya" ("dismissal, resignation", from the root "uvolneniye") so Rodion hears the exact meaning.'),
    (3, None, "'Don't even think about it!' Holding firm dryly in front of Max, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (4, None, "'Sorry, I cannot talk. The movie is about to start.' Max opens up wryly across the room, to clear the air between them once and for all."),
    (5, None, '\'Hello, Max! Idiots.\' Turning to the idiot in front of Max, Vika centers the thought on "idioty" ("idiot, fool", from "idiot") without wasting a word.'),
    (6, None, '\'Angelina, I need to step out for a short while.\' Speaking openly in front of Rodion, Vika leans on "nuzhno" ("it is needed, one has to"), which carries the whole predicate in Russian without needing "it is".'),
    (7, None, "'I don't understand, what are you doing?' Rodion checks briskly what Vika is actually getting at here."),
    (8, None, '\'Go right now and tell them the truth, I demand it!\' Addressing the truth at once, Vika centers the thought on "pravdu" ("truth", from "pravda") without wasting a word.'),
    (9, None, '\'Only I can make demands here, because this is my kitchen.\' Touching on his kitchen in this beat, Rodion lands on "kukhnya" ("kitchen") as the key everyday word here.'),
    (10, None, "'And here things will only be the way I said.' Rodion opens up sharply beside Vika, bringing things back to earth after the buildup."),
    (11, None, '\'We will see about that yet!\' Vika cuts in sharply right here and lands on "posmotrim" ("have a look", built on "posmotret") to keep the statement grounded.'),
]
