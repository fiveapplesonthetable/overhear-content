# Authoring module for kukhnya-s03e12-scene-02.
ID = 'kukhnya-s03e12-scene-02'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 12
SCENE = 2
TITLE = "Обострение у деда Кирилла  (Grandpa Kirill's Flare-Up)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.12'
SOURCE_FILE = 'sources/kukhnya/s03/e12.ru.srt'
INTRO = 'In the kitchen of Claude Monet, Chef Barinov scolds Max for arriving half an hour late. Max explains that their upstairs neighbor, retired officer Kirill Ilyich, threw soup on him during one of his seasonal flare-ups. Listen to the Russian dialogue first, and then we will go through every line.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Now you know the backstory of Kirill Ilyich, the one neighbor who refused to sell his apartment for any amount of money. See you next time!'
CLOSING = ('barinov', 'Увидимся!')
STORY = [
    ('barinov', 'Ты опоздал на полчаса.', 'You are half an hour late.', [(18, 'ты опоздал на полчаса')], 'adapted'),
    ('max', 'Он меня супом облил.', 'He poured soup all over me.', [(21, 'Он меня супом облил')], 'adapted'),
    ('barinov', 'Сеня, ты суп без мяса приготовил?', 'Senya, did you make the soup without meat?', [(22, 'суп без мяса приготовил')], 'adapted'),
    ('barinov', 'Ты же знаешь, деду только повод дать.', 'You know the old man only needs an excuse.', [(23, 'Ты же знаешь, деду только повод дать')], 'adapted'),
    ('senya', 'Шеф, это отличный куриный бульон.', 'Chef, this is an excellent chicken broth.', [(24, 'бульон')], 'adapted'),
    ('barinov', 'У деда Кирилла опять обострение.', 'Grandpa Kirill is having a flare-up again.', [(28, 'У деда Кирилла обострение')], 'adapted'),
    ('max', 'Кто-нибудь мне объяснит, что за дед Кирилл?', 'Will someone explain to me who Grandpa Kirill is?', [(29, 'Кто-нибудь мне объяснит, что за дед Кирилл')], 'adapted'),
    ('max', 'В нашем здании все квартиры раскуплены.', 'In our building all the apartments are bought up.', [(31, 'В нашем здании все квартиры')], 'adapted'),
    ('max', 'Осталась только квартира Кирилла Ильича.', 'Only the apartment of Kirill Ilyich remained.', [(33, 'квартиры Кирилла Ильича')], 'adapted'),
    ('max', 'Её пытались выкупить за большие деньги.', 'They tried to buy it out for big money.', [(34, 'пытались выкупить за большие деньги')], 'adapted'),
    ('max', 'Оказалось, деду Кириллу деньги не нужны.', 'It turned out Grandpa Kirill does not need money.', [(35, 'Оказалось, деду Кириллу деньги не нужны')], 'adapted'),
    ('max', 'А что ему нужно, никто не знает.', 'And nobody knows what he needs.', [(36, 'А что ему нужно, никто не знает')], 'adapted'),
]
WALK = [
    (0, None, "'You are half an hour late.' Answering smoothly right here, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (1, None, "'He poured soup all over me.' Max follows up wryly without any doubt, so Barinov knows he is not just making small talk."),
    (2, None, '\'Senya, did you make the soup without meat?\' Emphasizing the soup in the exchange, Barinov brings in "prigotovil" ("cooked", from "prigotovit") as the key Russian word here.'),
    (3, None, "'You know the old man only needs an excuse.' Barinov proceeds right away in their talk, testing Senya's reaction in the middle of the exchange."),
    (4, None, "'Chef, this is an excellent chicken broth.' Senya opens up quietly with a sigh, testing Barinov's reaction in the middle of the exchange."),
    (5, None, '\'Grandpa Kirill is having a flare-up again.\' Touching on a flare in front of Senya, Barinov uses "obostreniye" ("flare-up, relapse") to carry the main weight of the thought.'),
    (6, None, '\'Will someone explain to me who Grandpa Kirill is?\' Turning to the grandfather in front of Barinov, Max puts the question word "chto" right at the start so Barinov hears the focus immediately.'),
    (7, None, "'In our building all the apartments are bought up.' Max responds at once with a sigh, refusing to let the moment slip past."),
    (8, None, '\'Only the apartment of Kirill Ilyich remained.\' Highlighting the flat with Barinov, Max reaches for the Russian word "kvartira" ("flat") right at the heart of the line.'),
    (9, None, '\'They tried to buy it out for big money.\' Addressing the money in this beat, Max puts the weight on "bolshiye" ("big, serious", from "bolshoy") as the exchange unfolds.'),
    (10, None, "'It turned out Grandpa Kirill does not need money.' Max pushes back pointedly across the room, letting the remark speak for itself."),
    (11, None, '\'And nobody knows what he needs.\' Max speaks up promptly in this beat and uses "nuzhno" ("necessary") to carry the main weight of the thought.'),
]
