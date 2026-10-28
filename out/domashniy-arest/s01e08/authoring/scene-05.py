# Authoring module for domashniy-arest-s01e08-scene-05.
ID = 'domashniy-arest-s01e08-scene-05'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 5
TITLE = 'Вот танк государство может  (A Tank the State Can Handle)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'doctor': 'Доктор', 'lyosha': 'Лёша'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "Stepping out into the hospital corridor on his crutches, ten-year-old Lyosha stops the doctor to show him his broken toy tank, leading to a bitter and humorous exchange about what the state can and cannot fix. Let's listen in Russian first."
OPENER = "Now let's examine this poignant corridor conversation line by line. Lyosha leans on his forearm crutches and holds out his toy."
TRANSITION = "Now let's listen to the entire corridor conversation again in Russian."
OUTRO = "Lyosha's broken toy tank becomes a recurring symbol in the episode. See you next time!"
CLOSING = ('doctor', 'Пока!')
STORY = [
    ('lyosha', 'Доктор, подождите минутку, пожалуйста!', 'Doctor, wait a minute, please!', [], 'added opening request'),
    ('doctor', 'Что такое, малыш? У тебя что-то болит?', 'What is the matter, sweetie? Does something hurt you?', [], 'added doctor reaction'),
    ('lyosha', 'У меня танк сломался.', 'My tank broke.', [(80, 'У меня танк сломался')], ''),
    ('lyosha', 'Можете починить?', 'Can you fix it?', [(80, 'Можете починить')], ''),
    ('doctor', 'Танк? Ну-ка, покажи мне.', 'A tank? Let me see.', [(81, 'Танк? Ну-ка')], "'покажи мне' added"),
    ('doctor', 'Нет, брат, танк я не могу чинить.', 'No, buddy, I cannot fix tanks.', [(82, 'Нет, брат, танк я не могу чинить')], ''),
    ('doctor', 'Я ведь только людей лечу.', 'I only treat people, after all.', [(82, 'Я только людей')], "'лечу' supplied for elliptical phrase"),
    ('lyosha', 'А государство может починить танк?', 'And can the state fix a tank?', [(83, 'А государство может')], "'починить танк' added"),
    ('doctor', 'Вот танк государство точно может!', 'Now a tank — the state certainly can fix that!', [(84, 'Вот танк государство может')], "'точно' added for emphasis"),
    ('doctor', 'На танки у государства деньги всегда есть.', 'For tanks the state always has money.', [], 'added ironic contrast'),
    ('lyosha', 'Спасибо, доктор! Я сам попробую починить.', 'Thank you, Doctor! I will try to fix it myself.', [], 'added polite child reply'),
    ('doctor', 'Иди к маме, малыш! Не грусти.', "Go to your mama, sweetie! Don't be sad.", [], 'added encouraging doctor closing'),
]
WALK = [
    (0, None, "'Doctor, wait a minute, please!' Out in the corridor, Lyosha politely calls after the doctor using a soft, affectionate form of 'minute'."),
    (1, None, "'What is the matter, sweetie? Does something hurt you?' The doctor stops kindly in the hallway."),
    (2, None, "'My tank broke.' Literally, 'at me the tank broke itself' — instead of talking about his leg, the boy holds up his plastic toy."),
    (3, None, "'Can you fix it?' He asks with polite adult formality whether a surgeon can mend a broken toy."),
    (4, None, "'A tank? Let me see.' Playfully curious, the doctor says 'let's see' and leans down to inspect the little plastic tank."),
    (5, None, "'No, buddy, I cannot fix tanks.' The doctor addresses the boy warmly as 'brother' or 'buddy'."),
    (6, None, "'I only treat people, after all.' He gently explains his specialty: he mends people, not military hardware."),
    (7, None, "'And can the state fix a tank?' Lyosha remembers what his mother told him about the state helping."),
    (8, None, "'Now a tank — the state certainly can fix that!' The doctor gives a dry, ironic answer."),
    (9, None, "'For tanks the state always has money.' There is a bitter edge to the doctor's joke: the budget may run out of surgery quotas for children, but never for real tanks."),
    (10, None, "'Thank you, Doctor! I will try to fix it myself.' Lyosha takes his toy back with quiet determination to repair it on his own."),
    (11, None, "'Go to your mama, sweetie! Don't be sad.' The doctor sends the boy back to his mother with a gentle parting word."),
]
