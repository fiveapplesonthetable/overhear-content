# Authoring module for kukhnya-s01e16-scene-02.
ID = 'kukhnya-s01e16-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 2
TITLE = 'Случайный звонок  (An Accidental Call)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'inspector': 'Инспектор', 'nagiyev': 'Нагиев', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'The inspector is still in the dining room at Claude Monet, now hunting for the one extinguisher that is actually hanging where it should. Then the owner, Dmitry Nagiyev, walks in and asks him straight out why this restaurant. Listen for the moment the inspector lets slip who called him.'
OPENER = 'Now back to the hunt for the extinguisher, slowly.'
TRANSITION = 'And the whole visit once more, at the speed they really talk.'
OUTRO = "So the tip came from the restaurant next door, and the inspector is coming back tomorrow. Listen out for the little word that means 'here you are' or 'there it is', because Vika uses it and Russians say it constantly. See you next time!"
CLOSING = ('nagiyev', 'До свидания!')
STORY = [
    ('inspector', 'Где ваш огнетушитель?', 'Where is your fire extinguisher?', [(10, 'А где огнетушитель?')], ''),
    ('vika', 'Он висел здесь в прошлый раз.', 'It was hanging here last time.', [(11, 'Он же висел у вас в прошлый раз.')], ''),
    ('inspector', 'Вы что, смеётесь надо мной?', 'Are you laughing at me?', [(12, 'Вы что, издеваетесь, что ли?')], ''),
    ('inspector', 'Этот не подходит.', 'This one is not suitable.', [(14, 'Не годим.')], ''),
    ('vika', 'Вот нормальный огнетушитель.', 'Here is a normal fire extinguisher.', [(15, 'Браку! Ну вот, нормальный огнетушитель.')], ''),
    ('inspector', 'А где его пломба?', 'And where is its seal?', [(16, 'А пломба где?')], ''),
    ('nagiyev', 'Добрый день.', 'Good afternoon.', [], ''),
    ('nagiyev', 'Можно узнать одну вещь?', 'May I know one thing?', [(19, 'А можно узнать, чем вызван столь бурный интерес к пожарной безопасности моего')], ''),
    ('nagiyev', 'Почему у вас такой интерес к моему ресторану?', 'Why are you so interested in my restaurant?', [(20, 'ресторана? Можно.')], ''),
    ('inspector', 'Мы боремся с плохим руководством.', 'We are fighting with bad management.', [(21, 'Интерес вызван борьбой с халатностью руководства,')], ''),
    ('inspector', 'Был звонок моему начальнику.', 'There was a call to my boss.', [(22, 'а также с безобразным состоянием пожарной техники и звонком моему')], ''),
    ('inspector', 'Из соседнего ресторана.', 'From the neighboring restaurant.', [(23, 'начальнику из соседнего ресторана.')], ''),
    ('nagiyev', 'Всё понятно.', 'Everything is clear.', [(25, 'Понятно.')], ''),
    ('inspector', 'Ну что, до завтра.', 'Well then, until tomorrow.', [(26, 'Ну что, до завтра.')], ''),
]
WALK = [
    (0, None, "'Where is your fire extinguisher?' 'Vash', 'your', is the polite form. It stays as plain 'vash' because 'ognetushitel' is a masculine word."),
    (1, None, "'It was hanging here last time.' 'Visel', 'was hanging', ends in a bare '-l' because the extinguisher is masculine; for a feminine thing it would be 'visela'. 'V proshly raz', 'last time', is literally 'in the past time'."),
    (2, None, "'Are you laughing at me?' Russian laughs 'over' someone: 'smeyatsya nad'. Before 'mnoy', 'me', 'nad' gets an extra o and becomes 'nado mnoy'."),
    (3, None, "'This one is not suitable.' 'Podkhodit', 'suits', is literally 'walks up to', as if the thing comes up to the mark. It's also what you say about clothes that fit."),
    (4, None, "'Here is a normal fire extinguisher.' 'Vot', 'here it is', is what you say when you point at something, and nothing more than the thing itself needs to follow."),
    (5, None, "'And where is its seal?' 'Ego', 'its', is spelled with a g but said 'yevo'. 'Plomba', the seal on the extinguisher, is also the Russian word for a tooth filling."),
    (6, None, "'Good afternoon.' 'Dobry den' is literally 'kind day', the polite greeting from late morning until evening."),
    (7, None, "'May I find out one thing?' 'Mozhno', 'it is possible', is the simplest way to ask permission: 'mozhno' plus the action, here 'uznat', 'to find out'."),
    (8, None, "'Why are you so interested in my restaurant?' Russian takes an interest 'toward' something, with 'k', and after 'k', 'moy restoran' becomes 'moemu restoranu'."),
    (9, None, "'We are fighting bad management.' 'Rukovodstvo', 'management', is built from 'ruka', 'hand', and 'vodit', 'to lead'. And you fight 'with' something in Russian: 'boremsya s'."),
    (10, None, "'There was a call to my boss.' 'Zvonok', 'a call', comes from 'zvonit', 'to ring', and it is also the word for a doorbell or a school bell."),
    (11, None, "'From the neighboring restaurant.' 'Sosedny', 'neighboring', comes from 'sosed', 'neighbor'. After 'iz', 'from', it becomes 'sosednego', which is said 'sosednevo'."),
    (12, None, "'Everything is clear.' 'Ponyatno' is built on 'ponyat', 'to understand', so it is literally 'understandable'. It's the usual reply for 'I see' or 'got it'."),
    (13, None, "'Well then, until tomorrow.' 'Do zavtra', 'until tomorrow', is a set goodbye. Swap in another time and it still works, as in 'do vechera', 'until this evening'."),
]
