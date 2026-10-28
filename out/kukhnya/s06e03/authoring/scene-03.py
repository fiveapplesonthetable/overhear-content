# Authoring module for kukhnya-s06e03-scene-03.
ID = 'kukhnya-s06e03-scene-03'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 3
SCENE = 3
TITLE = "Подарок от отца Насти  (A Gift from Nastya's Father)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.03'
SOURCE_FILE = 'sources/kukhnya/s06/e03.ru.srt'
INTRO = "Across town, Nastya's wealthy father shows Kostya and Nastya a spacious apartment that a friend abroad is supposedly renting for next to nothing—before privately handing Kostya the ownership papers."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Forced to keep his father-in-law's lavish gift a secret from Nastya, Kostya immediately begins to feel uncomfortable inside the new home. Until next time!"
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('guest', 'Ну вот, заходите.', 'Well here we are, come on in.', [(40, 'Ну вот, заходите')], 'exact'),
    ('kostya', 'А друг ваш этот не обманет нас?', 'And will this friend of yours not cheat us?', [(43, 'А друг ваш этот не обманет нас?')], 'exact'),
    ('guest', 'Плевал он на ваши деньги.', 'He does not care about your money.', [(45, 'Плевал он на ваши деньги')], 'exact'),
    ('guest', 'Главное, чтобы за квартирой смотрели, пока он за границей.', 'The main thing is that you look after the apartment while he is abroad.', [(46, 'Главное, чтобы за квартирой смотрели, пока он за границей')], 'exact'),
    ('nastya', 'Папа, скажи честно, он в тюрьме?', 'Dad, tell me honestly, is he in prison?', [(47, 'скажи честно, он в тюрьме?')], 'adapted'),
    ('guest', 'Нет, он уехал жить на море.', 'No, he moved away to live by the sea.', [(48, 'уехал жить')], 'adapted'),
    ('guest', 'Я вам эту квартиру дарю.', 'I am giving you this apartment as a gift.', [(50, 'квартиру дарю')], 'adapted'),
    ('kostya', 'Спасибо, квартиру?', 'Thank you, the apartment?', [(50, 'Спасибо'), (51, 'Квартиру?')], 'adapted'),
    ('guest', 'Ты ей только ничего не говори.', 'Just do not say anything to her.', [(52, 'ты не говори')], 'adapted'),
    ('guest', 'Ты же ее знаешь, откажется.', 'You know her, she will refuse it.', [(53, 'Ты же ее знаешь, откажется')], 'exact'),
    ('nastya', 'Вы чего тут шепчетесь?', 'What are you two whispering about here?', [(55, 'Вы чего?')], 'adapted'),
    ('kostya', 'Так твой папа нам блендер подарил.', 'Your dad just gave us a blender as a gift.', [(56, 'Так твой папа нам блендер подарил')], 'exact'),
]
WALK = [
    (0, None, "'Well here we are, come on in.' The guest replies calmly around Kostya, refusing to let the moment slip past."),
    (1, None, '\'And will this friend of yours not cheat us?\' Emphasizing the friend before the guest, Kostya chooses "drug" ("friend") so the guest gets the point right away.'),
    (2, None, "'He does not care about your money.' The guest steps in earnestly watching Kostya, watching Kostya's face to see how the news lands."),
    (3, None, "'The main thing is that you look after the apartment while he is abroad.' The guest weighs in briskly with a sigh, making his position completely clear."),
    (4, None, '\'Dad, tell me honestly, is he in prison?\' Mentioning the prison beside the guest, Nastya puts the weight on "tyurme" ("prison", from "tyurma") as the exchange unfolds.'),
    (5, None, '\'No, he moved away to live by the sea.\' Underscoring the sea with Nastya, the guest centers the thought on "uyekhal" ("left, went away", from "uyekhat") without wasting a word.'),
    (6, None, "'I am giving you this apartment as a gift.' The guest pushes back wryly without any doubt, testing Kostya's reaction in the middle of the exchange."),
    (7, None, '\'Thank you, the apartment?\' Kostya quietly speaks this word of thanks while facing the guest using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
    (8, None, '\'Just do not say anything to her.\' Stepping in quietly right here, the guest pairs the negative word with "ne" ("not"), since Russian naturally doubles its negatives for emphasis.'),
    (9, None, "'You know her, she will refuse it.' The guest speaks up earnestly on the spot, steering the talk right where he wants it."),
    (10, None, '\'What are you two whispering about here?\' Nastya chimes in pointedly at once and leans on "shepchetes" ("whisper to each other", a form of "sheptatsya") to give the remark its edge.'),
    (11, None, "'Your dad just gave us a blender as a gift.' Kostya chimes in decisively toward Nastya, letting the remark speak for itself."),
]
