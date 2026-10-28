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
    (0, None, "'Hello, Katya, things turned out foolishly between us.' Explaining that things turned out foolishly between them lays the cards on the table for German."),
    (1, None, "'I cannot talk right now, bye.' Adding that she cannot talk right now bye fills in the missing piece for Barinov."),
    (2, None, "'Excuse me, please, go ahead.' Going ahead is how Katya lays out the situation for Barinov."),
    (3, None, "'You already worked in our restaurant.' Pointing out that Barinov already worked in their restaurant gives Barinov a sobering reality check."),
    (4, None, '\'Moreover, that was quite recently.\' German explains that moreover that was quite recently, keeping his voice calm and direct. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (5, None, "'Yes, that is all true, I worked here.' Realizing that that is all true she worked here changes how Katya handles the situation."),
    (6, None, "'Back then I worked under my father.' Noting that back then she worked under her father keeps Katya's side of the story simple and clear."),
    (7, None, "'He was the head chef here back then.' Even though he was the head here back then, Katya keeps a steady face in front of Barinov."),
    (8, None, '\'Then you resigned of your own accord.\' Over the phone and the conversation, German answers Barinov without a second thought. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (9, None, "'May I find out the reason for this wish?' Wondering if may he finds out the reason for this wish shows German caught off guard."),
    (10, None, "'We simply did not get along in character.' Once they simply did not get along in character, Katya can finally tell Barinov what she means."),
    (11, None, '\'That is not surprising, come with me.\' Adding that that is not surprising come with him fills in the missing piece for Barinov. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
]
