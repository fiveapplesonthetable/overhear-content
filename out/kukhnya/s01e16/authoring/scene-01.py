# Authoring module for kukhnya-s01e16-scene-01.
ID = 'kukhnya-s01e16-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 1
TITLE = "Пожарная тревога  (Fire Alarm)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "inspector": "angelina"}
LABELS = {"inspector": "Инспектор"}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'A strict fire safety inspector visits Claude Monet and points out numerous violations in the kitchen. Victoria tries to argue that they passed all previous inspections, but the inspector is not convinced. Let us listen to their conversation in Russian first.'
OPENER = 'Now let us examine the conversation line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "A fire inspector visits the kitchen of Claude Monet, criticizing the lack of visible fire extinguishers and giving Chef Barinov two days to fix the violations. Next time you watch the episode, listen for the Russian expressions for 'very' and 'bad' — you will catch every word right away. See you next time!"
CLOSING = ("inspector", "Пока!")
STORY = [
    ('inspector', 'У вас очень плохая картина по безопасности.', 'You have a very bad picture regarding safety.', [(1, 'У вас тут просто удручающая картина по технике пожарной безопасности.')], ''),
    ('inspector', 'У нас всё в порядке.', 'Everything is fine with us.', [(2, 'Да все же в порядке.')], ''),
    ('inspector', 'Мы прошли все проверки.', 'We passed all inspections.', [(2, 'Мы прошли все проверки.')], ''),
    ('inspector', 'Как вы прошли проверки?', 'How did you pass the inspections?', [(3, 'Ну как вы прошли проверки?')], ''),
    ('inspector', 'У вас нет огнетушителей на кухне.', 'You have no fire extinguishers in the kitchen.', [(3, 'Когда у вас на кухне даже огнетушителей нет.')], ''),
    ('inspector', 'У нас есть один.', 'We have one.', [(4, 'Да он есть, под собки висит.')], ''),
    ('inspector', 'Он висит под столом.', 'It is hanging under the table.', [(4, 'под собки висит.')], ''),
    ('inspector', 'Он должен висеть в трёх метрах.', 'It must hang within three meters.', [(5, 'А должен висеть в трех метрах от предполагаемого места возможного пожара.')], ''),
    ('inspector', 'От места возможного пожара.', 'From the place of a possible fire.', [(5, 'от предполагаемого места возможного пожара.')], ''),
    ('inspector', 'Это не проблема.', 'This is not a problem.', [], ''),
    ('inspector', 'Это очень большая проблема.', 'This is a very big problem.', [], ''),
    ('inspector', 'Ох, как всё плохо.', 'Oh, how bad everything is.', [(6, 'Ох-ох-ох.')], ''),
    ('inspector', 'Я даю вам два дня на исправление.', 'I give you two days for correction.', [(7, 'Даю два дня на исправление ситуации.')], ''),
    ('inspector', 'Мы всё сделаем.', 'We will do everything.', [], ''),
]
WALK = [
    (0, None, "'Your safety situation looks really bad.' Notice how this combines 'very much' with 'bad' and 'painting'."),
    (1, None, "'Everything is fine with us.' Vika uses the classic Russian possession phrasing — literally 'at us' rather than a verb meaning 'to have' around the word meaning 'order'."),
    (2, None, "'We passed all inspections.' Vika uses the action verb meaning 'to go through' to focus on the single completed result, pairing it with 'check'."),
    (3, None, "'How did you pass the inspections?' the inspector expresses this naturally by combining the word for 'how' with 'to go through' and 'check'."),
    (4, None, "'You have no fire extinguishers in the kitchen.' , combining 'fire extinguisher' with 'kitchen'."),
    (5, None, "'We have one.' Vika uses the classic Russian possession phrasing — literally 'at us' rather than a verb meaning 'to have', combining 'there is' with 'one'."),
    (6, None, "'It is hanging under the table.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (7, None, "'It must hang within three meters.' the inspector expresses this naturally by combining the word for 'has to' with 'to hang' and 'three'."),
    (8, None, "'From the place of a possible fire.' Russian omits the present-tense verb 'to be' here, linking 'places' directly with 'possible', combining 'places' with 'possible' and 'fire'."),
    (9, None, "'This is not a problem.' Vika delivers a punchy one-word reaction built around the Russian word meaning 'problem'."),
    (10, None, "'This is a very big problem.' Russian omits the present-tense verb 'to be' here, linking 'very much' directly with 'large', combining 'very much' with 'large' and 'problem'."),
    (11, None, "'Oh, how bad everything is.' Russian omits the present-tense verb 'to be' here, linking 'oh' directly with 'how', combining 'oh' with 'how' and 'badly'."),
    (12, None, "'I give you two days for correction.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (13, None, "'We will do everything.' Vika delivers a punchy one-word reaction built around the Russian word meaning 'we'll do'."),
]
