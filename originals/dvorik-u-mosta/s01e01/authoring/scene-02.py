# Authoring module for dvorik-u-mosta-s01e01-scene-02.
ID = 'dvorik-u-mosta-s01e01-scene-02'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 1
SCENE = 2
TITLE = 'Тёплые булочки и два звонка  (Warm Rolls and Two Rings)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'zoya': 'Зоя', 'matvey': 'Матвей'}
INTRO = 'Five minutes later, the warm scent of fresh bread drifts out from the breakfast corner. Morning baker Zoya carries a basket of hot rolls over to meet Kira and Matvey. Listen to the Russian scene first.'
OPENER = "Let's walk through their exchange piece by piece."
TRANSITION = "Now let's hear the whole conversation again from beginning to end."
OUTRO = 'Kira has a warm roll in her hand and a friendly ally in the café corner. You will hear those casual and polite greetings side by side in every episode. See you next time.'
CLOSING = ('zoya', 'Пока!')
STORY = [
    ('zoya', 'Привет! Ты, наверное, Кира? Я Зоя с кухни.', 'Hi! You must be Kira? I am Zoya from the kitchen.'),
    ('kira', 'Очень приятно, Зоя. Как чудесно пахнет!', 'Nice to meet you, Zoya. It smells wonderful!'),
    ('zoya', 'Свежие утренние булочки! Бери одну, пока она ещё тёплая.', 'Fresh morning rolls! Take one while it is still warm.'),
    ('kira', 'Спасибо! А мы здесь на ты?', "Thank you! Are we on casual 'you' terms here?"),
    ('zoya', 'Со мной всегда на ты! Оставь официальные слова для гостей.', 'With me, always! Leave formal words for the guests.'),
    ('matvey', 'Зоя со всей нашей улицей говорит как со старыми друзьями.', 'Zoya talks to our whole street like old friends.'),
    ('zoya', 'Потому что хороший кофе и тёплый хлеб делают людей добрыми!', 'Because good coffee and warm bread make people kind!'),
    ('kira', 'Что это за звонок? Кто-то позвонил два раза!', 'What was that bell? Somebody rang twice!'),
    ('matvey', 'Там никого нет. Это звонок из четвёртого номера.', 'Nobody is there. That is the buzzer from room four.'),
    ('zoya', 'Даже когда комната пустая, старый провод звонит дважды.', 'Even when the room is empty, the old wire rings twice.'),
    ('kira', 'Значит, дом сам говорит нам привет?', 'So the house says hello to us on its own?'),
    ('zoya', 'Точно! Ты уже совсем своя.', 'Exactly! You already fit right in.'),
]
WALK = [
    (0, None, ["'Hi! You must be Kira? I am Zoya from the kitchen.' Zoya opens with ", (None, 'Привет!'), " — the friendly 'hi' reserved for peers and friends, never formal guests."]),
    (1, None, ["'Nice to meet you, Zoya. It smells wonderful!' When meeting someone, ", (None, 'Очень приятно,'), " literally says 'very pleasant' and works just like 'nice to meet you'."]),
    (2, None, ["'Fresh morning rolls! Take one while it is still warm.' That little time word ", (None, 'ещё'), " means 'still', telling Kira the roll hasn't cooled down yet."]),
    (3, None, ["'Thank you! Are we on casual you terms here?' Russians explicitly ask ", (None, 'на ты?'), " — literally 'onto casual you?' — when checking whether to drop formal speech with coworkers."]),
    (4, None, ["'With me, always! Leave formal words for the guests.' Zoya answers with the casual command ", (None, 'Оставь'), " meaning 'leave', sealing their friendly footing right away."]),
    (5, None, ["'Zoya talks to our whole street like old friends.' Matvey teases her warmth: ", (None, 'со старыми друзьями.'), " pads the little word for 'with' using an extra vowel to ease the consonant cluster."]),
    (6, None, ["'Because good coffee and warm bread make people kind!' Notice ", (None, 'хороший кофе'), ' — even though the word for coffee ends in a vowel, standard Russian treats it as masculine.']),
    (7, None, ["'What was that bell? Somebody rang twice!' Adding an indefinite tail onto 'who' creates ", (None, 'Кто-то'), " meaning 'somebody', when you heard the ring without seeing a person."]),
    (8, None, ["'Nobody is there. That is the buzzer from room four.' Russian expresses absence with ", (None, 'никого нет.'), " — literally 'of nobody there-is-not'."]),
    (9, None, ["'Even when the room is empty, the old wire rings twice.' Compact and crisp, ", (None, 'дважды.'), " packs 'two times' into a single spoken word."]),
    (10, None, ["'So the house says hello to us on its own?' Placing ", (None, 'сам'), " right beside 'house' means 'by itself', giving the old building a playful personality."]),
    (11, None, ["'Exactly! You already fit right in.' Calling someone ", (None, 'своя.'), " literally calls her 'one of ours' — high praise on a newcomer's first morning."]),
]
