# Authoring module for dvorik-u-mosta-s01e06-scene-01.
ID = 'dvorik-u-mosta-s01e06-scene-01'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 6
SCENE = 1
TITLE = 'У железных ворот  (At the Iron Gate)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'roman': 'Роман', 'gleb': 'Глеб', 'kira': 'Кира'}
INTRO = 'Out under the shade tree at the Bridge Courtyard Inn in St Petersburg, older brother Gleb stands stiffly in his grey coat across from Roman as Kira sets down a hot teapot and steps back. Listen to the whole scene first.'
OPENER = "Let's walk through the brothers' first conversation in three years."
TRANSITION = 'Now listen to the whole scene again from start to finish.'
OUTRO = "Gleb recognized Roman's handwriting in two seconds and came anyway! Next time, they open the white paper parcel under the courtyard tree."
CLOSING = ('kira', 'До встречи!')
STORY = [
    ('gleb', 'Значит, человек с вещью от дедушки — это всё время был ты, Роман.', 'So the person with something from Grandfather was you all along, Roman.'),
    ('roman', 'Здравствуй, Глеб. Спасибо, что ты сегодня пришёл.', 'Hello, Gleb. Thank you for coming today.'),
    ('gleb', 'Я узнал твой ровный почерк на этой открытке за две секунды.', 'I recognized your neat handwriting on that postcard in two seconds.'),
    ('roman', 'Подожди — ты знал, что открытка от меня, и всё равно пришёл?', 'Wait — you knew the postcard was from me and came anyway?'),
    ('gleb', 'Конечно, пришёл. Зачем ты прятался за таинственной запиской?', 'Of course I came. Why did you hide behind a mysterious note?'),
    ('roman', 'Потому что боялся, что ты ещё сердишься. Я скучал по тебе эти три года.', 'Because I was afraid you were still angry. I missed you these three years.'),
    ('gleb', 'Три упрямых года... честно говоря, младший брат, я тоже по тебе скучал.', 'Three stubborn years... honestly, little brother, I missed you too.'),
    ('kira', 'Извините, господа — вот горячий чай, а тёплый лимонный пирог уже несут.', 'Excuse me, gentlemen — here is hot tea, and warm lemon cake is already on the way.'),
    ('gleb', 'Лимонный пирог? Стоп — откуда здесь знают про пятничный лимонный пирог?', 'Lemon cake? Hold on — how do they know here about Friday lemon cake?'),
    ('roman', 'Садись, Глеб, снимай тяжёлое пальто и посмотри на этот синий чемодан.', 'Sit down, Gleb, take off your heavy coat, and look at this blue suitcase.'),
    ('gleb', 'Неужели это старый тёмно-синий чемодан из мастерской дедушки?', "Could that really be the old dark-blue suitcase from Grandfather's workshop?"),
    ('kira', 'Не спешите, пожалуйста — весь дворик в вашем распоряжении.', 'Take your time, please — the whole courtyard is at your disposal.'),
]
WALK = [
    (0, None, ["'So the person with something from Grandfather was you all along, Roman.' Continuous ", (None, 'всё время'), " literally says 'all the time' — meaning 'all along'."]),
    (1, None, ["'Hello, Gleb. Thank you for coming today.' Singular ", (None, 'Здравствуй,'), ' greets one close person with quiet, heartfelt warmth.']),
    (2, None, ["'I recognized your neat handwriting on that postcard in two seconds.' Handwriting on paper is ", (None, 'почерк'), ' — built from drawing lines with a pen.']),
    (3, None, ["'Wait — you knew the postcard was from me and came anyway?' Notice ", (None, 'всё равно'), " meaning 'all the same, anyway' despite every doubt."]),
    (4, None, ["'Of course I came. Why did you hide behind a mysterious note?' Asking 'for what purpose?' uses ", (None, 'Зачем'), " rather than 'because of what?'."]),
    (5, None, ["'Because I was afraid you were still angry. I missed you these three years.' Missing someone warmly takes ", (None, 'скучал по тебе'), " — 'ached with longing for you'."]),
    (6, None, ["'Three stubborn years... honestly, little brother, I missed you too.' Speaking frankly opens with ", (None, 'честно говоря,'), " — 'speaking honestly'."]),
    (7, None, ["'Excuse me, gentlemen — here is hot tea, and warm lemon cake is already on the way.' Polite ", (None, 'уже несут.'), " literally says 'they are already carrying it over'."]),
    (8, None, ["'Lemon cake? Hold on — how do they know here about Friday lemon cake?' Asking 'from where do they know?' uses ", (None, 'откуда'), " — 'from what source?'."]),
    (9, None, ["'Sit down, Gleb, take off your heavy coat, and look at this blue suitcase.' Inviting a brother to take off his coat uses ", (None, 'снимай'), ' — friendly everyday request form.']),
    (10, None, ["'Could that really be the old dark-blue suitcase from Grandfather's workshop?' Disbelieving wonder starts with ", (None, 'Неужели'), " — 'can it really be?!'."]),
    (11, None, ["'Take your time, please — the whole courtyard is at your disposal.' Welcoming ", (None, 'Не спешите,'), " gently tells guests 'do not hurry'."]),
]
