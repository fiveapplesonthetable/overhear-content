# Authoring module for kukhnya-s04e18-scene-05.
ID = 'kukhnya-s04e18-scene-05'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 18
SCENE = 5
TITLE = 'Акула из арбуза  (The Watermelon Shark)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.18'
SOURCE_FILE = 'sources/kukhnya/s04/e18.ru.srt'
INTRO = "During a busy shift in the kitchen, molecular cuisine specialist Katya hurries over to Denis's station. She asked him to prepare simple watermelon pulp for a guest's order, but Denis has carved an elaborate surprise instead. Let's listen to their exchange in Russian."
OPENER = "Now let's look at Katya and Denis's conversation over the watermelon carving line by line."
TRANSITION = "Let's hear their brief kitchen exchange again from beginning to end."
OUTRO = 'Katya is annoyed that customers are waiting for their order while Denis plays romantic games during work hours. Notice the nouns meaning watermelon, shark, and mood in their dialogue. Until next time!'
CLOSING = ('denis', 'До завтра!')
STORY = [
    ('katya', 'Денис, я же срочно просила арбуз.', 'Denis, I urgently asked for watermelon.', [(48, 'Денис, я же срочно просила мякоть арбуза')], 'adapted'),
    ('katya', 'Мне нужна только мякоть арбуза.', 'I only need the watermelon pulp.', [(48, 'мякоть арбуза')], 'adapted'),
    ('denis', 'Катюша, у меня всё уже готово.', 'Katyusha, I have everything ready already.', [(49, 'Катюш, все готово')], 'adapted'),
    ('denis', 'Но достать её придётся тебе самой.', 'But you will have to get it out yourself.', [(49, 'Но достать тебе придется ее')], 'adapted'),
    ('denis', 'Тебе нужно победить эту акулу.', 'You need to defeat this shark.', [(50, 'акулы')], 'adapted'),
    ('katya', 'Ты зачем сделал эту акулу?', 'Why did you make this shark?', [(50, 'акулы')], 'adapted'),
    ('katya', 'Слушай, Денис, люди ждут заказ.', 'Listen, Denis, people are waiting for the order.', [(50, 'Слушай, Денис, ну люди ждут заказ')], 'adapted'),
    ('denis', 'Это же очень красивая акула.', 'But it is a very beautiful shark.', [(50, 'акулы')], 'adapted'),
    ('denis', 'Я хотел поднять тебе настроение.', 'I wanted to lift your spirits.', [(51, 'Я просто хотел поднять тебе настроение')], 'adapted'),
    ('katya', 'У нас сейчас много работы.', 'We have a lot of work right now.', [], 'new'),
    ('katya', 'Ладно, спасибо, ты мне поднял настроение.', 'All right, thanks, you lifted my spirits.', [(52, 'Спасибо, поднял')], 'adapted'),
    ('denis', 'Я сейчас быстро всё нарежу.', 'I will slice everything up quickly right now.', [], 'new'),
]
WALK = [
    (0, None, "'Denis, I urgently asked for watermelon.' Mentioning that she urgently asked for watermelon moves the talk in a new direction."),
    (1, None, "'I only need the watermelon pulp.' Katya reminds Denis that she only needs the watermelon pulp before the moment passes."),
    (2, None, "'Katyusha, I have everything ready already.' Because someone he has everything ready already, Denis treats the matter as settled."),
    (3, None, '\'But you will have to get it out yourself.\' Explaining that Katya will have to get it out themselves lays the cards on the table for Katya. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (4, None, '\'You need to defeat this shark.\' Denis mentions that Katya needs to defeat this shark so Katya sees what is at stake. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (5, None, "'Why did you make this shark?' By asking why Denis makes this shark, Katya presses Denis for a straight answer."),
    (6, None, "'Listen, Denis, people are waiting for the order.' Pointing out that people are waiting for the order gives Denis a sobering reality check."),
    (7, None, '\'But it is a very beautiful shark.\' Denis explains that it is a very beautiful shark, keeping his voice calm and direct. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (8, None, "'I wanted to lift your spirits.' Realizing that he wanted to lift Katya's spirits changes how Denis handles the situation."),
    (9, None, '\'We have a lot of work right now.\' Noting that they have a lot of work right now keeps Katya\'s side of the story simple and clear. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (10, None, '\'All right, thanks, you lifted my spirits.\' Even though all right thanks Denis lifted her spirits, Katya keeps a steady face in front of Denis. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (11, None, "'I will slice everything up quickly right now.' Admitting that he will slice everything up quickly right now shows Denis being honest for a change."),
]
