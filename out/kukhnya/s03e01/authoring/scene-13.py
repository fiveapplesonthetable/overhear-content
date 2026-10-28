# Authoring module for kukhnya-s03e01-scene-13.
ID = 'kukhnya-s03e01-scene-13'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 1
SCENE = 13
TITLE = 'Работа для всех  (Work for Everyone)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.01'
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'
INTRO = 'Back in the kitchen, Barinov happily calls out only classic orders while Katya stands with nothing to cook, so he and Fedya hand her a stack of dirty prep work.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that wraps up Scene Thirteen. Listen for Barinov's satisfaction as he calls out lamb, plums, and rabbit while Katya has zero orders. Until next time!"
CLOSING = ('barinov', 'До свидания!')
STORY = [
    ('barinov', 'Так, тогда как обычно.', 'Right, then as usual.', [(239, 'Так, тогда, ну, как обычно')], 'adapted'),
    ('barinov', 'Молочный ягнёнок на гриле.', 'Milk-fed lamb on the grill.', [(240, 'Молочный ягненок на гриле')], ''),
    ('barinov', 'Печёные сливы с ягодами.', 'Baked plums with berries.', [(241, 'Печеные сливы с ягодами')], ''),
    ('barinov', 'Кролик с розмарином.', 'Rabbit with rosemary.', [(242, 'Кролик с розмарином')], ''),
    ('barinov', 'Всем понятно?', 'Is that clear to everyone?', [(243, 'Всем понятно')], ''),
    ('fedya', 'Да, шеф!', 'Yes, Chef!', [(243, 'Да, шеф')], ''),
    ('barinov', 'Так, Екатерина.', 'Right, Yekaterina.', [(244, 'Так, Екатерина')], ''),
    ('barinov', 'Вы не должны стоять и бездельничать.', 'You must not stand around and loaf.', [(246, 'вы должны стоять и бездельничать')], 'adapted'),
    ('katya', 'Так нет же заказов.', 'But there are no orders.', [(247, 'Так нет же заказов')], ''),
    ('barinov', 'И что? Федя, пожалуйста.', 'So what? Fedya, please.', [(247, 'И что, Федя'), (248, 'Пожалуйста')], 'adapted'),
    ('barinov', 'У нас для всех работа найдётся.', 'We will find work for everyone here.', [(249, 'У нас для всех работа найдется')], ''),
    ('barinov', 'Вперёд!', 'Go ahead!', [(251, 'Вперед')], ''),
]
WALK = [
    (0, None, '\'Right, then as usual.\' Barinov chimes in boldly with Fedya and puts the emphasis on "obychno" ("usually") in the middle of the talk.'),
    (1, None, "'Milk-fed lamb on the grill.' Turning to the lamb in front of Fedya, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (2, None, "'Baked plums with berries.' Barinov replies right away with a nod, shifting the mood of the conversation in a single beat."),
    (3, None, '\'Rabbit with rosemary.\' Mentioning the rosemary in the exchange, Barinov lands on "rozmarinom" ("rosemary", built on "rozmarin") to keep the statement grounded.'),
    (4, None, '\'Is that clear to everyone?\' Barinov politely uses this acknowledgment in front of Fedya using "ponyatno" ("understood") — a single word meaning "clear, got it", showing the point has landed.'),
    (5, None, '\'Yes, Chef!\' Fedya warmly offers this direct affirmation to Barinov using "da" ("yes") — a crisp "da" ("yes") that confirms the point without extra words.'),
    (6, None, "'Right, Yekaterina.' Speaking warmly in the exchange, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
    (7, None, "'You must not stand around and loaf.' Barinov opens up at once in their talk, without trying to dress up how he really feels."),
    (8, None, "'But there are no orders.' Katya continues decisively with a smile, bringing things back to earth after the buildup."),
    (9, None, '\'So what? Fedya, please.\' Barinov politely directs this courtesy word with Fedya using "pozhaluysta" ("please") — the all-purpose Russian politeness word that covers both "please" and "you\'re welcome".'),
    (10, None, '\'We will find work for everyone here.\' Returning to the job in front of Katya, Barinov reaches for "u nas" ("by us, at our place") to talk about what they share.'),
    (11, None, "'Go ahead!' Barinov proceeds lightly without holding back, so Katya knows he is not just making small talk."),
]
