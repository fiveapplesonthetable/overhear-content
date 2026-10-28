# Authoring module for kukhnya-s02e03-scene-11.
ID = 'kukhnya-s02e03-scene-11'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 3
SCENE = 11
TITLE = 'Поездка домой  (Riding Home)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.03'
SOURCE_FILE = 'sources/kukhnya/s02/e03.ru.dual.srt'
INTRO = 'Outside the restaurant after their evening shift, Max tells Sasha not to worry because he can catch a cab home. Sasha insists on driving him herself, though she grows annoyed when Max asks why she seems upset.'
OPENER = 'Listen to Max and Sasha talking outside the restaurant before driving home.'
TRANSITION = "Now listen to the conversation between Max and Sasha again. Now let's listen to the whole conversation again from start to finish."
OUTRO = "Even though Sasha claims they are only friends, offering Max a ride home shows she still cares about him. Next time you watch the episode, listen for the Russian expressions for 'to worry' and 'strongly' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Да ты не волнуйся так сильно.', 'Do not worry so much.', [(181, 'Да ты не парься')], ''),
    ('max', 'Я сейчас быстро поймаю машину.', 'I will quickly catch a car right now.', [(182, 'Тачку сломлю')], ''),
    ('sasha', 'Я сама отвезу тебя до дома.', 'I will drive you home myself.', [(183, 'Саша, все нормально?')], ''),
    ('max', 'Саша, у тебя всё нормально?', 'Sasha, is everything alright with you?', [(183, 'Саша, все нормально?')], ''),
    ('sasha', 'Да, у меня всё хорошо.', 'Yes, everything is fine with me.', [(183, 'все нормально')], ''),
    ('max', 'Ты почему такая грустная весь вечер?', 'Why are you so sad all evening?', [(183, 'Саша, все нормально?')], ''),
    ('sasha', 'Ну вот ты опять начинаешь!', 'Well here you go starting again!', [(184, 'Ну ты опять')], ''),
    ('sasha', 'Мы же сегодня утром уже поговорили.', 'After all, we already talked this morning.', [(184, 'Ну мы же утром поговорили')], ''),
    ('max', 'Я просто хотел тебя спросить.', 'I just wanted to ask you.', [(183, 'все нормально')], ''),
    ('sasha', 'Мы с тобой просто хорошие друзья.', 'You and I are just good friends.', [(184, 'утром поговорили')], ''),
    ('max', 'Ладно, я тебя прекрасно понял.', 'Fine, I understood you very well.', [(181, 'Да ты не парься')], ''),
    ('sasha', 'Тогда садись скорее в машину.', 'Then get into the car quickly.', [(182, 'Тачку')], ''),
    ('max', 'Спасибо, что отвезёшь меня домой.', 'Thank you for driving me home.', [(183, 'Саша')], ''),
]
WALK = [
    (0, None, "'Do not worry so much.' Max leads with the direct command form meaning 'worry', followed by 'strongly'."),
    (1, None, "'I will quickly catch a car right now.' Here Max anchors the line on the word meaning 'now' and builds the thought around 'quickly' and 'to catch'."),
    (2, None, "'I will drive you home myself.' Sasha insists on giving him a ride in her car."),
    (3, None, "'Sasha, is everything alright with you?' Max uses the classic Russian possession phrasing — literally 'at you' rather than a verb meaning 'to have' around the word meaning 'fine'."),
    (4, None, "'Yes, everything is fine with me.' Sasha uses the classic Russian possession phrasing — literally 'at me' rather than a verb meaning 'to have' around the word meaning 'good'."),
    (5, None, "'Why are you so sad all evening?' Max wonders why she has been quiet all shift."),
    (6, None, "'Well here you go starting again!' Sasha is frustrated that he keeps bringing up their relationship."),
    (7, None, "'After all, we already talked this morning.' They agreed earlier not to complicate things between them."),
    (8, None, "'I just wanted to ask you.' Max puts the word for 'just' together with 'wanted' and 'to ask' in a crisp, natural spoken turn of phrase."),
    (9, None, "'You and I are just good friends.' Russian omits the present-tense verb 'to be' here, linking 'just' directly with 'good', combining 'just' with 'good' and 'friends'."),
    (10, None, "'Fine, I understood you very well.' The phrasing opens with 'perfectly' before bringing in 'understood?' to make the point clear."),
    (11, None, "'Then get into the car quickly.' Sasha leads with the direct command form meaning 'sit down', pairing it with 'back then' and 'quickly'."),
    (12, None, "'Thank you for driving me home.' Max appreciates the ride home."),
]
