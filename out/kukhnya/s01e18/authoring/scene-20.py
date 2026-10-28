ID = "kukhnya-s01e18-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 20
TITLE = "Прощание  (Farewell)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja", "nagiyev": "angelina"}
LABELS = {"anya": "Федя", "senya": "Сеня", "nagiyev": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = "Scene 20"

INTRO = "Nagiyev gathers the kitchen staff to announce the mass firings. Senya and Fedya discuss the depressing situation. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("nagiyev", "Ребята, нам придётся расстаться с вами.",
     "Guys, we will have to part ways with you.",
     [(358, 'нам придётся расстаться с вами')], "adapted"),
    ("senya", "Куда вы собрались так рано?",
     "Where are you off to so early?",
     [], "new"),
    ("anya", "Нас уволили.",
     "We got fired.",
     [(366, 'Нас уволили')], "adapted"),
    ("senya", "Как уволили? Тебя тоже?",
     "How fired? You too?",
     [(367, 'Тебя, кстати, тоже')], "adapted"),
    ("anya", "Да, мы все уходим.",
     "Yes, we are all leaving.",
     [], "new"),
    ("senya", "А что сказал шеф?",
     "And what did the chef say?",
     [(369, 'а шеф')], "adapted"),
    ("anya", "Шеф ничего не сделал.",
     "The chef did nothing.",
     [], "new"),
    ("anya", "Мы часто шагаем в пропасть.",
     "We often walk into the abyss.",
     [(371, 'шагаем именно в пропасть')], "adapted"),
    ("senya", "Это из-за самоуверенности?",
     "Is this because of overconfidence?",
     [(372, 'самоуверенности')], "adapted"),
    ("anya", "Да, мы слишком много хотели.",
     "Yes, we wanted too much.",
     [], "new"),
    ("nagiyev", "Вот ваш расчёт.",
     "Here is your payout.",
     [(374, 'Вот расчет')], "adapted"),
    ("senya", "Только двадцать тысяч?",
     "Only twenty thousand?",
     [(375, '20 тысяч')], "adapted"),
    ("nagiyev", "Остальное будет в конце месяца.",
     "The rest will be at the end of the month.",
     [(376, 'Остальное в конце месяца')], "adapted"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Guys, we will have to part ways with you.' You'll hear 'the boys' all the time in the show, here connected with 'you'."),
    (1, None,
     "'Where are you off to so early?' The question word for 'where to' comes right at the start, followed directly by 'early'."),
    (2, None,
     "'We got fired.' Here 'us' sets up the idea, while 'to fire' comes at the end for emphasis. Senya answers straight away."),
    (3, None,
     "'How fired? You too?' In Russian, 'how' leads into 'too' in a very natural everyday phrasing."),
    (4, None,
     "'Yes, we are all leaving.' Fedya puts 'we' up front so the listener immediately catches the tone, followed by 'are leaving'."),
    (5, None,
     "'And what did the chef say?' Senya starts with 'what' and pairs it with 'said' to make the point clear. Then Fedya replies."),
    (6, None,
     "'The chef did nothing.' Fedya puts 'chef' up front so the listener immediately catches the tone, followed by 'nothing'."),
    (7, None,
     "'We often walk into the abyss.' You'll hear 'we' all the time in the show, here connected with 'to disappear'."),
    (8, None,
     "'Is this because of overconfidence?' There is no question word here — in Russian, rising intonation on 'overconfidence' is enough to make it a question. And Fedya jumps in."),
    (9, None,
     "'Yes, we wanted too much.' A compact expression built around 'we' and 'wanted'."),
    (10, None,
     "'Here is your payout.' The first content word means 'final pay', and 'final pay' rounds out the thought."),
    (11, None,
     "'Only twenty thousand?' A compact expression built around 'only' and 'thousand'. Dmitry answers straight away."),
    (12, None,
     "'The rest will be at the end of the month.' In Russian, 'remaining' leads into 'months' in a very natural everyday phrasing."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "The cooks receive their final meager payouts and prepare to leave the restaurant for good."
CLOSING = ("nagiyev", "Остальное будет в конце месяца.")
