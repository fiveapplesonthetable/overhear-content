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
    (0, None, "'Did you like it?' Asking whether the guest likes it cuts straight through the tension between Max and the guest."),
    (1, None, '\'You know, it is delicious.\' Once it is delicious, the guest can finally tell Max what he means. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (2, None, '\'Well then, gentlemen, shall we sign?\' Around the shift and point, the guest wants to know where Max really stands. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (3, None, "'Of course! We need to celebrate this with a drink.' By needing to celebrate this with a drink, the guest raises the stakes in the room at once."),
    (4, None, "'Some champagne!' With the moment and contract at stake, the guest reacts without holding back. Russian puts the key word right up front so his emotion lands on the first beat."),
    (5, None, "'I will open it right now and bring it.' Mentioning that he will open it right now and bring it moves the talk in a new direction."),
    (6, None, "'What do you mean 'I will open it'? Open it here.' Here asking what Max means will open it shows the guest looking for the real truth."),
    (7, None, "'And the last signature right here.' Around the plan and work, the guest sets a calm, everyday tone with Max."),
    (8, None, "'Excuse me! Forgive me!' Here telling the guest to forgive him lets Max's real feelings break through. Russian puts the key word right up front so his emotion lands on the first beat."),
    (9, None, "'Your dinner is on the house.' Max mentions that the guest's dinner is on the house so the guest sees what is at stake."),
    (10, None, '\'And where is the restroom here?\' Here wondering where the restroom here is shows the guest looking for the real truth. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (11, None, '\'I will show you the way.\' Pointing out that he will show the guest the way gives the guest a sobering reality check. Notice how he sticks to the formal "you", keeping a professional line between them.'),
]
