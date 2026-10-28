# Authoring module for kukhnya-s03e01-scene-16.
ID = 'kukhnya-s03e01-scene-16'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 1
SCENE = 16
TITLE = 'Бокал шампанского  (A Glass of Champagne)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.01'
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'
INTRO = "Delighted with his molecular lunch, Nastya's father prepares to sign the contract with his business partners and asks Max to pop a bottle of champagne right at the table."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "That brings Scene Sixteen to an end. Watch how Max's struggle with the champagne cork saves Nastya's father from signing the crooked contract. See you next time!"
CLOSING = ('max', 'Увидимся!')
STORY = [
    ('max', 'Вам понравилось?', 'Did you like it?', [(279, 'Вам понравилось')], ''),
    ('guest', 'Ты знаешь, вкусно.', 'You know, it is delicious.', [(280, 'Ты знаешь, вкусно')], ''),
    ('guest', 'Ну что, господа, подпишем?', 'Well then, gentlemen, shall we sign?', [(282, 'Ну что, господа, подпишем')], ''),
    ('guest', 'Конечно! Надо это обмыть.', 'Of course! We need to celebrate this with a drink.', [(283, 'Конечно'), (283, 'Надо это обмыть')], 'adapted'),
    ('guest', 'Шампанского!', 'Some champagne!', [(284, 'Шампанского')], ''),
    ('max', 'Я сейчас открою и принесу.', 'I will open it right now and bring it.', [(285, 'Я сейчас открою и принесу')], ''),
    ('guest', 'Что значит открою? Здесь открывай.', "What do you mean 'I will open it'? Open it here.", [(286, 'что значит открою? Здесь открывай')], 'adapted'),
    ('guest', 'И последняя подпись вот здесь.', 'And the last signature right here.', [(288, 'И последняя подпись вот здесь')], ''),
    ('max', 'Извините! Простите!', 'Excuse me! Forgive me!', [(291, 'Извините'), (292, 'Простите')], 'adapted'),
    ('max', 'Ваш ужин за наш счёт.', 'Your dinner is on the house.', [(292, 'Ваш ужин за наш счет')], ''),
    ('guest', 'А где у вас здесь туалет?', 'And where is the restroom here?', [(293, 'А где у вас здесь туалет')], ''),
    ('max', 'Я вас провожу.', 'I will show you the way.', [(294, 'я вас провожу')], 'adapted'),
]
WALK = [
    (0, None, '\'Did you like it?\' Max replies briskly on the spot and uses "ponravilos" ("pleased, was liked", from "ponravitsya") to make the point stick.'),
    (1, None, "'You know, it is delicious.' Holding firm openly during the talk, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (2, None, "'Well then, gentlemen, shall we sign?' The guest challenges evenly how Max expects that to work in practice."),
    (3, None, '\'Of course! We need to celebrate this with a drink.\' The guest smoothly speaks this confirmation without hesitation using "konechno" ("of course") — spoken with a soft "shn" sound in everyday Moscow Russian to mean "of course, certainly".'),
    (4, None, "'Some champagne!' Focusing on the champagne right here, spoken Russian compresses the whole thought into just 1 words, skipping the extra helper words English needs."),
    (5, None, "'I will open it right now and bring it.' Max replies openly beside the guest, steering the talk right where he wants it."),
    (6, None, '\'What do you mean \'I will open it\'? Open it here.\' The guest speaks sharply with Max and brings in "otkryvay" ("to open", from "otkryvat") as the key Russian word here.'),
    (7, None, '\'And the last signature right here.\' Talking about the last signature to Max, the guest uses "poslednyaya" ("last, final", from "posledniy") to make the point stick.'),
    (8, None, '\'Excuse me! Forgive me!\' Max gently voices this polite apology while facing the guest using "izvinite" ("excuse me") — the respectful form of "excuse me" or "sorry" used when stepping in or apologizing.'),
    (9, None, '\'Your dinner is on the house.\' Underscoring the counting on the spot, Max chooses "schyot" ("counting, account") so the guest gets the point right away.'),
    (10, None, '\'And where is the restroom here?\' Pressing on openly in the exchange, the guest links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (11, None, "'I will show you the way.' Max reacts warmly watching the guest, to clear the air between them once and for all."),
]
