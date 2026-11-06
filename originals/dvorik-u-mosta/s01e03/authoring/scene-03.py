# Authoring module for dvorik-u-mosta-s01e03-scene-03.
ID = 'dvorik-u-mosta-s01e03-scene-03'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 3
SCENE = 3
TITLE = 'Тёплый свет лампы  (Left at the Landing)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'zoya': 'Зоя', 'yaroslav': 'Ярослав'}
INTRO = 'Ten minutes before eight, Kira, Zoya, and Yaroslav put the finishing touches on the third-floor room. Every detail matters before the soaked traveller arrives. Listen first.'
OPENER = "Let's go through those final ten minutes one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from beginning to end."
OUTRO = "The warm brass lamp is glowing just as the eight o'clock guest rings the downstairs bell. Next time, Roman steps out of the rain."
CLOSING = ('kira', 'Увидимся!')
STORY = [
    ('zoya', 'Заправь угол простыни покрепче, Кира! А вот и две мягкие подушки.', 'Tuck the sheet corner tighter, Kira! And here go the two soft pillows.'),
    ('kira', 'Готово! И синий коврик лёг прямо у кровати.', 'Done! And the blue rug settled right beside the bed.'),
    ('yaroslav', 'Куда повесить круглое зеркало? Слева от окна или справа?', 'Where should I hang the round mirror? Left of the window or right?'),
    ('kira', 'Справа у стола, там хороший свет.', 'On the right by the desk, the light is good there.'),
    ('zoya', 'Включаем латунную лампу Матвея... ой, какой тёплый жёлтый свет!', "Turning on Matvey's brass lamp... oh, what warm yellow light!"),
    ('yaroslav', 'Честно говоря, я почти хочу спать здесь сам сегодня ночью!', 'Honestly speaking, I almost want to sleep up here myself tonight!'),
    ('kira', 'Подождите — какую скидку мы предложим гостю за замену комнаты?', 'Wait — what discount will we offer the guest for changing rooms?'),
    ('yaroslav', 'Полцены за эту ночь и бесплатный завтрак всю неделю!', 'Half price for tonight and free breakfast all week!'),
    ('zoya', 'Щедро! Вы слышали звонок у ворот внизу?', 'Generous! Did you hear the gate bell downstairs?'),
    ('kira', 'Ровно восемь часов! Наш гость приехал!', "Eight o'clock sharp! Our guest has arrived!"),
    ('yaroslav', 'У меня сердце стучит! Кира, объясните вы — у вас спокойный и честный голос!', 'My heart is pounding! Kira, you explain — you have a calm and honest voice!'),
    ('kira', 'Положитесь на меня. Спускаемся вниз встречать гостя.', "Count on me. Let's go down to welcome our guest."),
]
WALK = [
    (0, None, ["'Tuck the sheet corner tighter, Kira! And here go the two soft pillows.' Exclaiming ", (None, 'А вот и'), " works just like 'and here are!' when placing the finishing touch."]),
    (1, None, ["'Done! And the blue rug settled right beside the bed.' Flat rugs and clothes 'lie down' into place: ", (None, 'лёг'), " literally says 'lay down'."]),
    (2, None, ["'Where should I hang the round mirror? Left of the window or right?' Location pair ", (None, 'Слева'), ' and ', (None, 'справа?'), " mean 'on the left' and 'on the right'."]),
    (3, None, "'On the right by the desk, the light is good there.' Short, decisive placement — Kira already thinks like a seasoned innkeeper."),
    (4, None, ["'Turning on Matvey's brass lamp... oh, what warm yellow light!' Admiring something aloud starts naturally with ", (None, 'какой тёплый'), " — 'what a warm...!'."]),
    (5, None, ["'Honestly speaking, I almost want to sleep up here myself tonight!' Notice ", (None, 'хочу спать'), " — 'I want' followed straight by 'to sleep'."]),
    (6, None, ["'Wait — what discount will we offer the guest for changing rooms?' Guests love the word ", (None, 'скидку'), " — built from 'throwing a bit off' the price."]),
    (7, None, ["'Half price for tonight and free breakfast all week!' Built from 'without payment', ", (None, 'бесплатный'), " means 'free of charge'."]),
    (8, None, ["'Generous! Did you hear the gate bell downstairs?' Down on a lower floor is ", (None, 'внизу?'), " — location 'downstairs', distinct from movement downward."]),
    (9, None, ["'Eight o'clock sharp! Our guest has arrived!' For 'on the dot' or 'sharp', put ", (None, 'Ровно'), ' right before the hour.']),
    (10, None, ["'My heart is pounding! Kira, you explain — you have a calm and honest voice!' A racing heart 'knocks' in Russian: ", (None, 'сердце стучит!'), ' uses the same sound word as knocking on a door.']),
    (11, None, ["'Count on me. Let's go down to welcome our guest.' Reassuring a nervous boss takes ", (None, 'Положитесь на меня.'), " — literally 'lean on me, rely on me'."]),
]
