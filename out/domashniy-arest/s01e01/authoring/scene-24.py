# Authoring module for domashniy-arest-s01e01-scene-24.
ID = 'domashniy-arest-s01e01-scene-24'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 24
TITLE = "Вот оно, твоё королевство  (There's Your Kingdom)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "Now Samson storms back into the flat, and Arkady has to tell him the truth: his wife and his deputy have taken everything. As always, the Russian first; don't worry about catching every word."
OPENER = "Let's go through it. Samson comes in looking for the car he was promised."
TRANSITION = "Right, let's hear the whole thing again."
OUTRO = 'So the promised flat and car have turned into a flooded bathroom. When you watch, listen for Samson shouting about the kingdom. See you next time!'
CLOSING = ('nina', 'Ну всё. Пока!')
STORY = [
    ('samson', 'Аркаша, где наша машина?', "Arkasha, where's our car?", [], 'new: links back to the keys being taken back (cues 912-914)'),
    ('arkady', 'Ваня, всё гораздо хуже. Меня обманули.', "Vanya, it's much worse than that. I've been cheated.", [(917, 'гораздо хуже'), (918, 'меня')], "'кинули' (slang) -> 'обманули'; 'Ваня' as address"),
    ('samson', 'Чего? Кто тебя обманул?', 'What? Who cheated you?', [(919, 'Чего')], "'Кто тебя обманул?' new"),
    ('arkady', 'У меня больше ничего нет.', 'I have nothing left.', [(920, 'У меня больше ничего нет')], ''),
    ('samson', 'А список? Квартира, машина, спа!', 'And the list? A flat, a car, a spa!', [(923, 'Квартира, машина, спа')], "'Ты на списку писал?' -> 'А список?'"),
    ('nina', 'Ванечка!', 'Vanechka!', [(924, 'Ванечка')], ''),
    ('arkady', 'Я тебе говорю: денег нет. Где я тебе возьму квартиру?', "I'm telling you: there's no money. Where am I supposed to get you a flat?", [(926, 'Я тебе говорю'), (927, 'Где я тебе возьму квартиру')], "'у меня ничего больше нет' -> 'денег нет'"),
    ('samson', 'Держи. Будешь чинить трубу.', "Here, take this. You're going to fix the pipe.", [(929, 'Держи'), (932, 'будешь чинить')], "'Стояк' -> 'трубу'; word order changed"),
    ('arkady', 'Зачем? Не буду я ничего чинить!', "What for? I'm not fixing anything!", [(930, 'Зачем')], "'Не буду я ничего чинить!' replaces Arkady's crude reply (cues 933-934)"),
    ('samson', 'Чего ты смотришь, Нина? Королева!', 'What are you staring at, Nina? Your Majesty!', [(935, 'Чего ты'), (936, 'Королева')], "'вылупилась' -> 'смотришь'; 'блин' dropped; 'Нина' added"),
    ('samson', 'Спа захотела? Вот оно, твоё королевство!', 'You wanted a spa? There it is, your kingdom!', [(937, 'захотела'), (937, 'Вот оно, твое королевство')], "'Спана' (garbled) -> 'Спа'"),
    ('arkady', 'Ваня, вода! Везде вода!', "Vanya, the water! There's water everywhere!", [], 'new: tells what happens on screen (Samson tears off the leaking pipe and floods the bathroom)'),
    ('nina', 'Ваня, я прошу тебя!', "Vanya, I'm begging you!", [(950, 'Ваня, я прошу тебя')], ''),
    ('nina', 'Это же общий туалет, Ваня!', 'This is a shared bathroom, Vanya!', [(951, 'Это же'), (951, 'туалет, Ваня')], "'общательный' (garbled) -> 'общий'"),
]
WALK = [
    (0, None, "'Arkasha, where's our car?' The word for 'our' is feminine, to match the car. Arkady has to admit the worst."),
    (1, 'Ваня, всё гораздо хуже.', "'Vanya, it's much worse than that.' In this moment, Vanya is Samson's real first name, the short form of Ivan. The word before 'worse' means 'much'."),
    (1, 'Меня обманули.', "'I've been cheated.' Literally, 'me they cheated'. Russians often say it this way, with 'they' and no subject at all. Samson doesn't get it."),
    (2, None, "'What? Who cheated you?' The first word is a rough, everyday way of saying 'what'. Arkady spells it out."),
    (3, None, "'I have nothing left.' Literally, 'at me no more nothing is'. Two negatives together are normal in Russian. Samson remembers the promises."),
    (4, None, "'And the list? A flat, a car, a spa!' That's the wish list they drew up together earlier, when Arkady moved in. Nina tries to calm him down."),
    (5, None, "'Vanechka!' An even softer form of Vanya, the way a wife says it when things are going wrong."),
    (6, 'Я тебе говорю: денег нет.', "'I'm telling you: there's no money.' After 'no', the word for money changes its ending. Then a question."),
    (6, 'Где я тебе возьму квартиру?', "'Where am I supposed to get you a flat?' Literally, 'where will I take a flat for you?'. Samson hands him something."),
    (7, None, "'Here, take this. You're going to fix the pipe.' He hands Arkady a tube of sealant. The second sentence is the simple future: 'you will' plus the verb 'to fix'. Arkady refuses."),
    (8, None, "'What for? I'm not fixing anything!' Again two negatives side by side, 'not' and 'nothing'. Now Samson turns on his wife."),
    (9, None, "'What are you staring at, Nina? Your Majesty!' He calls her 'queen', and he doesn't mean it as a compliment. Then he grabs the leaking pipe."),
    (10, None, "'You wanted a spa? There it is, your kingdom!' He tears the old pipe off, and water bursts into the bathroom. 'Wanted' ends in 'a' because he's talking to a woman."),
    (11, None, "'Vanya, the water! There's water everywhere!' The second sentence starts with 'everywhere', and again there's no verb at all. Nina begs her husband."),
    (12, None, "'Vanya, I'm begging you!' The verb is the same one that gives the polite word for 'please'. And she reminds him whose bathroom it is."),
    (13, None, "'This is a shared bathroom, Vanya!' The little word after 'this' adds emphasis, like 'after all'. Everyone in the flat uses this one bathroom."),
]
