# Authoring module for kukhnya-s01e16-scene-01.
ID = 'kukhnya-s01e16-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 1
TITLE = 'Пожарная тревога  (Fire Alarm)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'inspector': 'Инспектор', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'A strict fire safety inspector visits Claude Monet and points out numerous violations in the kitchen. Victoria tries to argue that they passed all previous inspections, but the inspector is not convinced. Let us listen to their conversation in Russian first.'
OPENER = 'Now let us examine the conversation line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "A fire inspector visits the kitchen of Claude Monet, criticizing the lack of visible fire extinguishers and giving Chef Barinov two days to fix the violations. Next time you watch the episode, listen for the Russian expressions for 'very' and 'bad' — you will catch every word right away. See you next time!"
CLOSING = ('vika', 'Пока!')
STORY = [
    ('inspector', 'У вас очень плохая картина по безопасности.', 'You have a very bad picture regarding safety.', [(1, 'У вас тут просто удручающая картина по технике пожарной безопасности.')], ''),
    ('vika', 'У нас всё в порядке.', 'Everything is fine with us.', [(2, 'Да все же в порядке.')], ''),
    ('vika', 'Мы прошли все проверки.', 'We passed all inspections.', [(2, 'Мы прошли все проверки.')], ''),
    ('inspector', 'Как вы прошли проверки?', 'How did you pass the inspections?', [(3, 'Ну как вы прошли проверки?')], ''),
    ('inspector', 'У вас нет огнетушителей на кухне.', 'You have no fire extinguishers in the kitchen.', [(3, 'Когда у вас на кухне даже огнетушителей нет.')], ''),
    ('vika', 'У нас есть один.', 'We have one.', [(4, 'Да он есть, под собки висит.')], ''),
    ('vika', 'Он висит под столом.', 'It is hanging under the table.', [(4, 'под собки висит.')], ''),
    ('inspector', 'Он должен висеть в трёх метрах.', 'It must hang within three meters.', [(5, 'А должен висеть в трех метрах от предполагаемого места возможного пожара.')], ''),
    ('inspector', 'От места возможного пожара.', 'From the place of a possible fire.', [(5, 'от предполагаемого места возможного пожара.')], ''),
    ('vika', 'Это не проблема.', 'This is not a problem.', [], ''),
    ('inspector', 'Это очень большая проблема.', 'This is a very big problem.', [], ''),
    ('inspector', 'Ох, как всё плохо.', 'Oh, how bad everything is.', [(6, 'Ох-ох-ох.')], ''),
    ('inspector', 'Я даю вам два дня на исправление.', 'I give you two days for correction.', [(7, 'Даю два дня на исправление ситуации.')], ''),
    ('vika', 'Мы всё сделаем.', 'We will do everything.', [], ''),
]
WALK = [
    (0, None, "'Your safety situation looks really bad.' The official bluntly criticizes the restaurant's current condition."),
    (1, None, "'Everything is fine with us.' Vika immediately defends their setup, insisting there are no issues."),
    (2, None, "'We passed all inspections.' She backs up her claim by mentioning their previous successful evaluations."),
    (3, None, "'How did you pass the inspections?' The official sounds skeptical, questioning how they ever managed to get approved."),
    (4, None, "'You have no fire extinguishers in the kitchen.' Pointing out a glaring violation, the inspector notes the missing equipment."),
    (5, None, "'We have one.' Vika quickly corrects him, claiming they do possess the required item."),
    (6, None, "'It is hanging under the table.' She specifies its awkward location to prove she knows where it is."),
    (7, None, "'It must hang within three meters.' The official corrects her, stating the exact distance rule for the equipment."),
    (8, None, "'From the place of a possible fire.' He finishes his thought by explaining the safety rationale behind the measurement."),
    (9, None, "'This is not a problem.' Vika tries to downplay the severity of the rule break."),
    (10, None, "'This is a very big problem.' Pushing back firmly, the official emphasizes how serious the violation actually is."),
    (11, None, "'Oh, how bad everything is.' He sighs in exasperation at the sheer number of issues he is finding."),
    (12, None, "'I give you two days for correction.' Setting a strict deadline, he offers a brief window to fix the mess."),
    (13, None, "'We will do everything.' Vika promises swift action to resolve all the complaints."),
]
