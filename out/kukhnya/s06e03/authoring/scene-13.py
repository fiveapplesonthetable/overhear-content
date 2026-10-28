# Authoring module for kukhnya-s06e03-scene-13.
ID = 'kukhnya-s06e03-scene-13'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 3
SCENE = 13
TITLE = "Новоселье с родителями Насти  (Housewarming with Nastya's Parents)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.03'
SOURCE_FILE = 'sources/kukhnya/s06/e03.ru.srt'
INTRO = 'Kostya returns from the store complaining about the expensive neighborhood shops, only to find that Nastya has invited her parents over to celebrate their housewarming.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Tension simmers at the dinner table as Kostya insists on serving the food and drink he paid for himself. Until next time!'
CLOSING = ('kostya', 'До завтра!')
STORY = [
    ('kostya', 'Странный район твой папа выбрал.', 'Your dad picked a strange neighborhood.', [(213, 'твой папа выбрал')], 'adapted'),
    ('kostya', 'Хлеб в магазине очень дорогой.', 'Bread at the store is very expensive.', [(214, 'Хлеб в магазине')], 'adapted'),
    ('nastya', 'Нормальные здесь магазины, и очереди нет.', 'The stores here are fine, and there is no line.', [(216, 'Нормальные здесь магазины'), (218, 'И очереди')], 'adapted'),
    ('nastya', 'Костик, я родителей позвала отметить сюрприз.', 'Kostik, I invited my parents over to celebrate the surprise.', [(219, 'Костик, я родителей позвала'), (220, 'Сюрприз такой отметить')], 'adapted'),
    ('guest', 'Телевизор в гостиную еще не успели купить?', 'Have you not managed to buy a TV for the living room yet?', [(221, 'в гостиную не успели купить')], 'adapted'),
    ('guest', 'Ничего, я куплю вам новый телевизор.', 'That is alright, I will buy you a new TV.', [(222, 'Ничего, я куплю вам')], 'adapted'),
    ('kostya', 'Не надо, спасибо, мы сами купим.', 'No need, thank you, we will buy it ourselves.', [(223, 'Не надо спасибо, мы сами купим')], 'exact'),
    ('kostya', 'Это же наш дом, и на стол здесь накрывать будем мы.', 'After all, this is our home, and we will set the table here.', [(228, 'Это же наш дом. И на стол здесь накрывать будем мы')], 'exact'),
    ('guest', 'Коньяк, может быть, наш выпьем?', 'Maybe we should drink our cognac?', [(230, 'может быть, наш выпьем?')], 'adapted'),
    ('kostya', 'Нет, я сам купил коньяк.', 'No, I bought cognac myself.', [(231, 'Я купил')], 'adapted'),
    ('kostya', 'Хороший регион, и коньяк этот тоже хороший.', 'It is a good region, and this cognac is good too.', [(234, 'Хороший регион. И коньяк этот тоже хороший')], 'exact'),
    ('kostya', 'И людям обычным по карману.', 'And affordable for ordinary people.', [(235, 'И людям обычным по карману')], 'exact'),
]
WALK = [
    (0, None, "'Your dad picked a strange neighborhood.' Around the room and situation, Kostya sets a calm, everyday tone with the guest."),
    (1, None, "'Bread at the store is very expensive.' Explaining that bread at the store is very expensive lays the cards on the table for the guest."),
    (2, None, "'The stores here are fine, and there is no line.' Nastya mentions that the stores here are fine and there is no line so the guest sees what is at stake."),
    (3, None, "'Kostik, I invited my parents over to celebrate the surprise.' Over the situation and the moment, Nastya answers the guest without a second thought."),
    (4, None, '\'Have you not managed to buy a TV for the living room yet?\' Asking whether Kostya not managed to buy a for the living room yet is how the guest puts Kostya on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (5, None, '\'That is alright, I will buy you a new TV.\' The guest explains that that is alright he will buy Kostya a new, keeping his voice calm and direct. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (6, None, "'No need, thank you, we will buy it ourselves.' Needing thank the guest they will buy it themselves moves the conversation forward without extra drama."),
    (7, None, '\'After all, this is our home, and we will set the table here.\' Noting that after all this is their home and they will set the table here keeps Kostya\'s side of the story simple and clear. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (8, None, '\'Maybe we should drink our cognac?\' The guest asks whether maybe they should drink their cognac, refusing to let the point slide. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (9, None, "'No, I bought cognac myself.' Admitting that he bought cognac himself shows Kostya being honest for a change."),
    (10, None, "'It is a good region, and this cognac is good too.' Saying that it is a good region and this cognac is good is how Kostya sets the tone with the guest."),
    (11, None, "'And affordable for ordinary people.' With the kitchen and truth in play, Kostya keeps this short reply brisk and direct."),
]
