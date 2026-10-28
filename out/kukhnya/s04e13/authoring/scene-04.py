# Authoring module for kukhnya-s04e13-scene-04.
ID = 'kukhnya-s04e13-scene-04'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 13
SCENE = 4
TITLE = 'Собеседование у Германа  (Job Interview with German)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'german': 'Герман', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.13'
SOURCE_FILE = 'sources/kukhnya/s04/e13.ru.srt'
INTRO = "Realizing he was too harsh, Chef Barinov calls Katya to apologize, but she quickly hangs up. She is already sitting inside Claude Monet interviewing with Barinov's rival, the new head chef German Land, who is intrigued to learn that she is Viktor Barinov's daughter."
OPENER = "Let's look closely at how German interviews Katya and why he decides to hire her."
TRANSITION = 'Now listen to the complete interview scene from beginning to end.'
OUTRO = "Delighted to hire Chef Barinov's own daughter after she admits they clashed in character, German leads her into the kitchen. Next, we watch the Claude Monet cooks react to Katya's return. See you next time!"
CLOSING = ('german', 'До встречи!')
STORY = [
    ('barinov', 'Алло, Катя, глупо у нас получилось.', 'Hello, Katya, things turned out foolishly between us.', [(34, 'Алло, Катя, как-то глупо')], 'adapted'),
    ('katya', 'Я не могу сейчас говорить, пока.', 'I cannot talk right now, bye.', [(35, 'Я не могу сейчас')], 'adapted'),
    ('katya', 'Извините, пожалуйста, продолжайте.', 'Excuse me, please, go ahead.', [(36, 'Извините.')], 'adapted'),
    ('german', 'Вы уже работали в нашем ресторане.', 'You already worked in our restaurant.', [(37, 'Тут указано, что вы')], 'adapted'),
    ('german', 'Причём это было совсем недавно.', 'Moreover, that was quite recently.', [(38, 'Причем не так давно.')], 'adapted'),
    ('katya', 'Да, всё верно, я работала здесь.', 'Yes, that is all true, I worked here.', [(39, 'Да, все верно. Я')], 'adapted'),
    ('katya', 'Я тогда работала у своего отца.', 'Back then I worked under my father.', [(39, 'Да, все верно. Я')], 'adapted'),
    ('katya', 'Он тогда был здесь шеф-поваром.', 'He was the head chef here back then.', [(40, 'Он тогда был шеф-поваром.')], 'adapted'),
    ('german', 'Потом вы уволились по собственному желанию.', 'Then you resigned of your own accord.', [(43, 'Вы проработали у него')], 'adapted'),
    ('german', 'Можно узнать причину этого желания?', 'May I find out the reason for this wish?', [(45, 'Можно узнать мотив этого')], 'adapted'),
    ('katya', 'Мы просто не сошлись характерами.', 'We simply did not get along in character.', [(46, 'Ну, если коротко, мы')], 'adapted'),
    ('german', 'Это неудивительно, пойдёмте со мной.', 'That is not surprising, come with me.', [(47, 'Неудивительно. Пойдемте со мной.')], 'adapted'),
]
WALK = [
    (0, None, '\'Hello, Katya, things turned out foolishly between us.\' Barinov follows up dryly in the exchange and reaches for the Russian word "poluchilos" ("worked out", built from "poluchitsya") right at the center of the line.'),
    (1, None, '\'I cannot talk right now, bye.\' Katya responds promptly to Barinov and lands on "govorit" ("to talk") as the key everyday word here.'),
    (2, None, '\'Excuse me, please, go ahead.\' Katya naturally offers this polite apology while facing German using "izvinite" ("excuse me") — the respectful form of "excuse me" or "sorry" used when stepping in or apologizing.'),
    (3, None, '\'You already worked in our restaurant.\' Focusing on his restaurant in front of Katya, German brings in "restorane" ("restaurant", from "restoran") as the key Russian word here.'),
    (4, None, '\'Moreover, that was quite recently.\' Stepping in boldly to Katya, German adds "sovsem" ("completely, at all") so the statement leaves zero room for doubt.'),
    (5, None, "'Yes, that is all true, I worked here.' Katya opens up evenly around German, watching German's face to see how the news lands."),
    (6, None, '\'Back then I worked under my father.\' Turning to her father to German, Katya uses "rabotala" ("worked", from "rabotat") to make the point stick.'),
    (7, None, '\'He was the head chef here back then.\' Emphasizing the head in front of Barinov, Katya puts the weight on "shef-povarom" ("head chef", from "shef-povar") as the exchange unfolds.'),
    (8, None, "'Then you resigned of your own accord.' German speaks pointedly watching Katya, grounding the moment in plain reality."),
    (9, None, '\'May I find out the reason for this wish?\' Focusing on the wish before Katya, German chooses "zhelaniya" ("wish") so Katya gets the point right away.'),
    (10, None, '\'We simply did not get along in character.\' Dwelling on the character to German, Katya uses the little word "prosto" ("simply, just") to make the point sound effortless.'),
    (11, None, "'That is not surprising, come with me.' German opens up wryly with a shrug, so Katya knows he is not just making small talk."),
]
