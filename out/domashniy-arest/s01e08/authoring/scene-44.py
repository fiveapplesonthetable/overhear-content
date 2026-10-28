# Authoring module for domashniy-arest-s01e08-scene-44.
ID = 'domashniy-arest-s01e08-scene-44'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 44
TITLE = "Видеть вас не хочу  (I Don't Want to See You)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "Last time in the hospital corridor, young Lyosha took his first steps without surgery, proving the Moscow specialist's diagnosis correct. Outside the ward, Arkady approaches Marina expecting her to fall into his arms in gratitude, but Marina is furious at his arrogance and credits Dr. Tenenbaum instead. Let's listen to the conversation in Russian first."
OPENER = "Let's break down Marina's angry rejection of Arkady outside the hospital room."
TRANSITION = "Now let's listen to Marina and Arkady's tense exchange once again."
OUTRO = "Even though Arkady organized Dr. Tenenbaum's consultation, Marina refuses to give him any credit and banishes him from her life. See you next time!"
CLOSING = ('marina', 'Пока!')
STORY = [
    ('arkady', 'Что, Марина, бить будете?', 'What, Marina, are you going to hit me?', [(1011, 'Что'), (1011, 'бить будете')], "'маманя' replaced with 'Марина'"),
    ('marina', 'Если вы подойдёте, я вызову полицию!', 'If you come near us, I will call the police!', [(1012, 'вы к нам подойдете')], "'позвоню друзьям' -> 'вызову полицию'"),
    ('marina', 'И вас посадят в тюрьму.', "And you'll end up in prison.", [(1013, 'И вас посадят в тюрьму')], ''),
    ('arkady', 'А почему вы такая злая?', 'Why are you so hostile?', [(1014, 'А чего злая такая')], "'чего' -> 'почему вы'"),
    ('arkady', 'Я между прочим вашего сына спас.', 'I saved your son, for the record.', [(1014, 'Я между прочим вашего сына спас')], ''),
    ('marina', 'Вы? Да вам плевать на моего ребёнка!', "You? You don't care about my child at all!", [(1015, 'Вы'), (1017, 'Да вам плевать на моего ребенка')], ''),
    ('marina', 'Это всё сделал доктор Тененбаум.', 'Dr. Tenenbaum did all of this.', [(1017, 'Это ваш доктор Тененбаум')], ''),
    ('marina', 'Чужой человек из Москвы не поленился.', 'A complete stranger from Moscow took the trouble.', [(1018, 'Чужой человек из Москвы. Не поленился')], ''),
    ('marina', 'Он сам позвонил и предупредил нас.', 'He called and warned us himself.', [(1018, 'звонился, предупредил')], "'да звонился' -> 'Он сам позвонил'"),
    ('marina', 'Потому что знал, что вам всё равно!', "Because he knew that you didn't care!", [(1019, 'Потому что знал, что вам')], "'плевать' -> 'всё равно'"),
    ('marina', 'Видеть вас больше не хочу.', "I don't want to see you anymore.", [(1019, 'Видеть вас не хочу')], "'больше' added"),
    ('arkady', 'То есть награды для меня не будет?', 'So there will be no reward for me, then?', [(1020, 'в награду не будет')], "'секса' replaced with 'награды'"),
    ('marina', 'Никакой награды не будет, Аркадий Борисович!', 'There will be no reward at all, Arkady Borisovich!', [(1021, 'не будет аркадий борисович')], 'cleaned for A1'),
    ('marina', 'Уходите отсюда навсегда!', 'Leave this place forever!', [], 'closing demand'),
]
WALK = [
    (0, None, "'What, Marina, are you going to hit me?' Arkady jokingly shrinks back as Marina steps out into the hallway."),
    (1, None, "'If you come near us, I will call the police!' Marina glares at him with utter disgust."),
    (2, None, "'And you'll end up in prison.' Literally, 'they will seat you in prison' — Russian uses that everyday word for locking someone up."),
    (3, None, "'Why are you so hostile?' Arkady cannot understand why she isn't showering him with kisses."),
    (4, None, "'I saved your son, for the record.' Notice the parenthetical Russian idiom meaning 'by the way' or 'for the record'."),
    (5, None, "'You? You don't care about my child at all!' Marina scoffs at his claim of heroism."),
    (6, None, "'Dr. Tenenbaum did all of this.' She gives full credit to the famous Moscow physician."),
    (7, None, "'A complete stranger from Moscow took the trouble.' In Russian, saying someone 'was not lazy' is a warm way to say they went out of their way to help."),
    (8, None, "'He called and warned us himself.' The doctor called hospital staff urgently to stop the surgery."),
    (9, None, "'Because he knew that you didn't care!' Marina believes Arkady only cares about his own selfish interests."),
    (10, None, "'I don't want to see you anymore.' She refuses to have anything more to do with him."),
    (11, None, "'So there will be no reward for me, then?' Even now, Arkady shamelessly fishes for a romantic favour."),
    (12, None, "'There will be no reward at all, Arkady Borisovich!' Marina firmly shuts down his advances."),
    (13, None, "'Leave this place forever!' She points down the corridor and turns her back on him."),
]
