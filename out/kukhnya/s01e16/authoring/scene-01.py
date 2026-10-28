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
INTRO = "Welcome to Kukhnya, the Russian comedy set in Claude Monet, a smart Moscow restaurant where Chef Barinov rules the kitchen. Today a fire inspector arrives and finds fault with everything he sees, while Vika, the art director, tries to keep her cool. First you'll hear it in Russian, and you don't need to catch every word."
OPENER = "Let's go back through it slowly."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Two days is the inspector's deadline, and he doesn't sound like a man who bends. When you watch, listen for the little word that means 'there isn't', because the inspector uses it again and again. See you next time!"
CLOSING = ('vika', 'Пока!')
STORY = [
    ('inspector', 'У вас очень плохая картина по безопасности.', 'You have a very bad picture regarding safety.', [(1, 'У вас тут просто удручающая картина по технике пожарной безопасности.')], ''),
    ('vika', 'У нас всё в порядке.', 'Everything is fine with us.', [(2, 'Да все же в порядке.')], ''),
    ('vika', 'Мы прошли все проверки.', 'We passed all inspections.', [(2, 'Мы прошли все проверки.')], ''),
    ('inspector', 'Как вы прошли проверки?', 'How did you pass the inspections?', [(3, 'Ну как вы прошли проверки?')], ''),
    ('inspector', 'У вас нет огнетушителей на кухне.', 'You have no fire extinguishers in the kitchen.', [(3, 'Когда у вас на кухне даже огнетушителей нет.')], ''),
    ('vika', 'У нас есть один.', 'We have one.', [(4, 'Да он есть, под собки висит.')], ''),
    ('vika', 'Он висит в подсобке.', 'It is hanging in the back room.', [(4, 'под собки висит.')], ''),
    ('inspector', 'Он должен висеть в трёх метрах.', 'It must hang within three meters.', [(5, 'А должен висеть в трех метрах от предполагаемого места возможного пожара.')], ''),
    ('inspector', 'От места возможного пожара.', 'From the place of a possible fire.', [(5, 'от предполагаемого места возможного пожара.')], ''),
    ('vika', 'Это не проблема.', 'This is not a problem.', [], ''),
    ('inspector', 'Это очень большая проблема.', 'This is a very big problem.', [], ''),
    ('inspector', 'Ох, как всё плохо.', 'Oh, how bad everything is.', [(6, 'Ох-ох-ох.')], ''),
    ('inspector', 'Я даю вам два дня на исправление.', 'I give you two days for correction.', [(7, 'Даю два дня на исправление ситуации.')], ''),
    ('vika', 'Мы всё сделаем.', 'We will do everything.', [], ''),
]
WALK = [
    (0, None, "'You have a very bad picture regarding safety.' Russian says 'at you' where English says 'you have', so the line starts with the small word for 'at' and Russian's 'you', formal. The Russian for 'picture' is used here for the overall state of things, as when we say the picture looks bleak."),
    (1, None, "'Everything is fine with us.' Same 'at us' pattern as before. The last part is literally 'in order', and Russians say it all day long when they mean 'all good'."),
    (2, None, "'We passed all inspections.' The word is the one for walking through something, so the idea is 'we walked through all the checks'. Its past form ends in 'li' for 'we', and 'all' also takes a plural form."),
    (3, None, "'How did you pass the inspections?' Same word again, with Russian's 'how' in front. The inspector says 'you' in the polite form, so he's cold but correct. The tone does the rest: he doesn't believe a word."),
    (4, None, "'You have no fire extinguishers in the kitchen.' 'There isn't' is short and blunt, and the thing that's missing changes its ending after it. The word for the extinguisher is 'fire' plus 'put out' plus 'er', so it's exactly what it says."),
    (5, None, "'We have one.' Here is the opposite of the last line: the Russian for 'there is' instead of 'there isn't'. Russian's 'one' is the same one you count with."),
    (6, None, "'It is hanging in the back room.' The back room is a very Russian little word, for the storeroom behind the kitchen. 'In' plus an ending on the room tells you where it hangs, and the Russian for 'hangs' is the one the inspector picks up next."),
    (7, None, "'It must hang within three meters.' Russian's 'must' changes with whoever is the subject, and here it's the masculine form because the extinguisher is masculine in Russian. The second word stays in its dictionary form, 'to hang', and 'three meters' wears a plural ending."),
    (8, None, "'From the place of a possible fire.' This is a pile-up of the 'of' form: place, possible, fire all end in the matching ending. 'Fire' here is the destructive one, not the one for a campfire."),
    (9, None, "'This is not a problem.' Vika shrugs it off. The small word for 'not' sits right in front of what it denies, and the Russian for 'problem' is one you already know from English."),
    (10, None, "'This is a very big problem.' Russian's 'big' ends in 'aya' because 'problem' is feminine in Russian, just like the Russian for 'bad' did in the first line. 'Very' is the same word as before."),
    (11, None, "'Oh, how bad everything is.' The first sound is just a sigh, like 'ugh'. Russian's 'bad' has no 'aya' this time, because it describes a whole situation instead of a noun."),
    (12, None, "'I give you two days for correction.' 'I give' is one word, with the ending that means 'I'. 'Day' changes after 'two', and the Russian for 'correction' comes from the verb 'to fix'."),
    (13, None, "'We will do everything.' This looks like the present, but it's the kind of word that means one finished job, so it points to the future. It's the right thing to promise, even if Vika isn't sure how."),
]
