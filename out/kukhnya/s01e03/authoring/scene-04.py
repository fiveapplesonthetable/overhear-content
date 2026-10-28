# Authoring module for kukhnya-s01e03-scene-04.
ID = 'kukhnya-s01e03-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = "Опасный разговор  (A Dangerous Conversation)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "vadim": "anja", "anya": "alisa"}
LABELS = {"vadim": "Вадим", "anya": "Макс"}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = 'Outside restaurant Claude Monet in the third episode. A stern prosecutor named Vadim confronts Max and demands to know who Vika is dating. Listen to their tense conversation in Russian first, and then we will break it down together.'
OPENER = "Let's examine this threatening interrogation step by step."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'That is our fourth scene. In Kukhnya, running into an angry prosecutor is the last thing Max needed. See you next time!'
CLOSING = ("anya", "До встречи!")
STORY = [
    ('vadim', 'Слышь, малой, есть разговор.', 'Listen, kid, I want to talk.', [(132, 'разговор есть')], ''),
    ('anya', 'Что вам нужно?', 'What do you need?', [], ''),
    ('vadim', 'Тут у вас работает Вика.', 'Vika works here with you.', [(133, 'Тут у вас работает Вика')], ''),
    ('vadim', 'Виктория Сергеевна.', 'Viktoria Sergeyevna.', [(133, 'Виктория Сергеевна')], ''),
    ('vadim', 'С кем она тут встречается?', 'Who is she seeing here?', [(134, 'с кем она у вас тут встречается')], ''),
    ('vadim', 'Ну, почему молчим?', 'Well, why are we silent?', [], ''),
    ('anya', 'Почему я должен отвечать?', 'Why should I answer?', [(136, 'я тебе должен отвечать')], ''),
    ('vadim', 'Не хочешь отвечать здесь?', "Don't want to answer here?", [(137, 'Не хочешь отвечать здесь')], ''),
    ('vadim', 'Ответишь у меня в прокуратуре.', "You'll answer in my prosecutor's office.", [(138, 'у меня в прокуратуре')], ''),
    ('vadim', 'Ты меня понял?', 'Did you understand me?', [(139, 'Понял')], ''),
    ('anya', 'Понял, всё понял.', 'Understood, understood everything.', [(140, 'Понял, понял')], ''),
    ('anya', 'Она ни с кем не встречается.', 'She is not seeing anyone.', [(141, 'она здесь ни с кем не встречается')], ''),
    ('vadim', 'Ну, смотри у меня.', 'Well, you watch yourself.', [(142, 'Ну, смотри')], ''),
    ('anya', 'Надо срочно предупредить всех.', 'Must urgently warn everyone.', [(160, 'Надо предупредить')], ''),
]
WALK = [
    (0, None, "'Listen, kid, I want to talk.' A gruff stranger corners Max outside the restaurant."),
    (1, None, "'What do you need?' Max responds cautiously to the aggressive tone."),
    (2, None, "'Vika works here with you.' the speaker uses the classic Russian possession phrasing — literally 'at you' rather than a verb meaning 'to have', pairing it with 'here' and 'works'."),
    (3, None, "'Viktoria Sergeyevna.' Russian omits the present-tense verb 'to be' here, linking 'Viktoria' directly with 'Sergeyevna', combining 'Viktoria' with 'Sergeyevna'."),
    (4, None, "'Who is she seeing here?' the speaker puts the word for 'here' together with 'is dating' in a crisp, natural spoken turn of phrase."),
    (5, None, "'Well, why are we silent?' Here the speaker anchors the line on the word meaning 'why' and builds the thought around 'are silent'."),
    (6, None, "'Why should I answer?' The phrasing opens with 'why' before bringing in 'must' and 'to answer' to make the point clear."),
    (7, None, "'Don't want to answer here?' , combining 'want' with 'to answer' and 'here'."),
    (8, None, "'You'll answer in my prosecutor's office.' , combining 'will answer' with 'prosecutor's office'."),
    (9, None, "'Did you understand me?' the speaker turns a statement into a question purely through rising intonation on the word meaning 'understood' to make the point directly in conversation."),
    (10, None, "'Understood, understood everything.' Max delivers a punchy conversational reaction built around the Russian word meaning 'understood'."),
    (11, None, "'She is not seeing anyone.' Max protects Vika and himself with a firm denial."),
    (12, None, "'Well, you watch yourself.' the speaker uses the classic Russian possession phrasing — literally 'at me' rather than a verb meaning 'to have', followed by 'watch'."),
    (13, None, "'Must urgently warn everyone.' Here Max anchors the line on the word meaning 'necessary' and builds the thought around 'urgently' and 'to warn'."),
]
