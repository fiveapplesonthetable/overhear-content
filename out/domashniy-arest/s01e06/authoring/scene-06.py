# Authoring module for domashniy-arest-s01e06-scene-06.
ID = 'domashniy-arest-s01e06-scene-06'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 6
SCENE = 6
TITLE = 'Вмешаться в честный ход выборов?  (Interfere in the Honest Course of the Election?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'general': 'Генерал Круглов', 'lavrov': 'Лавров', 'zina': 'Зина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.06'
SOURCE_FILE = 'sources/domashniy-arest/s01/e06.ru.dual.srt'
INTRO = "As his assistant Zina serves him lunch at his desk, General Kruglov listens to Major Lavrov's report that Samsonov is gaining popularity and that Pasha Osipenko has collapsed with high blood pressure. Let's hear the Russian conversation first; don't worry about catching every word."
OPENER = "Let's walk through the video briefing and see how Major Lavrov gets permission to sabotage Samson's campaign."
TRANSITION = 'Now listen to the entire video briefing once more from start to finish.'
OUTRO = "With Moscow's blessing to discredit Samsonov, the officers begin plotting against the people's candidate, while back at the communal flat Arkady and Ilona search for a rich campaign sponsor. See you next time!"
CLOSING = ('general', 'Пока!')
STORY = [
    ('zina', 'Здравия желаю, товарищ генерал. Все на связи.', 'Good day, Comrade General. Everyone is on the line.', [(187, 'Здравия желаю'), (192, 'товарищ генерал'), (235, 'Все на связи')], 'combined greeting and connection check for Zina'),
    ('general', 'Я вижу, сегодня все в сборе. Ладно, давай, докладывай.', 'I see everyone is here today. Alright, go ahead, report.', [(190, 'Я вижу, сегодня все в сборе'), (195, 'Ладно'), (195, 'давай, докладывай')], ''),
    ('lavrov', 'Появились новые сложности. Тут кандидат из народа, Самсонов.', "New difficulties have appeared. There's a candidate from the people here, Samsonov.", [(197, 'Появились новые сложности'), (199, 'Тут кандидат из народа, Самсонов')], ''),
    ('lavrov', 'Он мэра в окно выбросил. Вы помните?', 'He threw the mayor out the window. Do you remember?', [(200, 'мэра в окно выбросил'), (201, 'Вы помните')], ''),
    ('general', 'Так, я всё помню.', 'Right, I remember everything.', [(202, 'Так, я все помню')], ''),
    ('lavrov', 'Он теперь набирает популярность. И Осипенко может проиграть выборы.', 'He is now gaining popularity. And Osipenko might lose the election.', [(203, 'он теперь набирает популярность'), (205, 'Осипенко'), (206, 'может проиграть выборы')], ''),
    ('general', 'И что?', 'And so?', [(207, 'И что')], ''),
    ('lavrov', 'Местные люди боятся давать деньги в наш кластер.', 'The local people are afraid to put money into our cluster.', [(209, 'местные'), (209, 'боятся'), (209, 'в наш'), (209, 'кластер')], "simplified 'местные элиты боятся вкладываться в наш выдуманный кластер' for A1"),
    ('lavrov', 'А Осипенко сейчас дома лежит. У него больное сердце.', 'And Osipenko is lying at home right now. He has a sick heart.', [(212, 'у него'), (212, 'дома лежит')], "simplified 'гипертонический криз' -> 'больное сердце' for A1"),
    ('general', 'Так, полковник, успокойся. Зина, дай вилку.', 'Easy, Colonel, calm down. Zina, give me a fork.', [(220, 'Так, полковник, успокойся'), (221, 'Зина, дай вилку')], ''),
    ('zina', 'Пожалуйста, товарищ генерал. Вот ваша вилка.', 'Here you go, Comrade General. Here is your fork.', [(222, 'Товарищ генерал')], 'Zina hands him the fork'),
    ('lavrov', 'Мы должны остановить этого народного кандидата. Тогда выиграет Осипенко.', "We must stop this people's candidate. Then Osipenko will win.", [(223, 'Мы должны'), (223, 'этого народного кандидата'), (224, 'выиграл'), (225, 'Осипенко')], "simplified 'дискредитировать' -> 'остановить' for A1"),
    ('general', 'Подожди. Ты предлагаешь вмешаться в честный ход выборов?', 'Wait. Are you proposing to interfere in the honest course of the election?', [(227, 'Подожди'), (228, 'Ты предлагаешь вмешаться в'), (228, 'ход выборов')], "fixed ASR 'частный' -> 'честный'"),
    ('lavrov', 'Да.', 'Yes.', [(229, 'Да')], ''),
    ('general', 'Отлично, занимайтесь! Все на связи.', 'Excellent, get on it! Everyone stay in touch.', [(230, 'Отлично, занимайтесь'), (235, 'Все на связи')], ''),
    ('lavrov', 'Есть! Спасибо, до свидания.', 'Yes, sir! Thank you, goodbye.', [(231, 'Есть. Спасибо, до свидания')], ''),
]
WALK = [
    (0, 'Здравия желаю, товарищ генерал.', "The briefing opens with the traditional military greeting literally wishing good health: 'Good day, comrade general.'"),
    (0, 'Все на связи.', "'Everyone is on the line.' Russian omits the present-tense verb 'to be', connecting 'everyone' directly with 'the line'."),
    (1, 'Я вижу, сегодня все в сборе.', "General Kruglov spots diminutive Lieutenant Lyova Sokolov sitting beside the others: 'I see everyone is assembled today.'"),
    (1, 'Ладно, давай, докладывай.', "After scolding Sokolov for missing previous meetings, the general turns to Major Lavrov: 'Alright, go ahead, report.'"),
    (2, 'Появились новые сложности.', "Lavrov begins gravely: 'New complications have appeared.'"),
    (2, 'Тут кандидат из народа, Самсонов.', "'There's a candidate from the people here, Samsonov.' The line opens with 'here' and lands on 'the people' at the end for emphasis."),
    (3, 'Он мэра в окно выбросил.', "He reminds the forgetful general who Samsonov is: 'He threw the mayor out the window.'"),
    (3, 'Вы помните?', "He checks politely: 'Do you remember?'"),
    (4, None, "Kruglov nods impatiently over his lunch plate: 'Right, I remember everything.'"),
    (5, 'Он теперь набирает популярность.', "Lavrov explains the problem: 'He is now gaining popularity.'"),
    (5, 'И Осипенко может проиграть выборы.', "'And Osipenko might lose the election.' The line opens with 'and' and lands on 'the election' at the end for emphasis."),
    (6, None, "The general asks why that matters to their sting operation: 'And so?'"),
    (7, None, "Lavrov explains that because Osipenko might lose, 'The businessmen are afraid to put money into the project.'"),
    (8, 'А Осипенко сейчас дома лежит.', "Worse still, after his restaurant meeting, 'And Osipenko is now lying at home.'"),
    (8, 'У него больное сердце.', "He adds gravely: 'He has a sick heart.'"),
    (9, 'Так, полковник, успокойся.', "When Colonel Mikhail Mikhailovich blurts out that they should just arrest everyone now, Kruglov waves him off: 'Okay, Colonel, calm down.'"),
    (9, 'Зина, дай вилку.', "Without missing a beat, the general calls to his secretary in Moscow: 'Zina, give me a fork.'"),
    (10, 'Пожалуйста, товарищ генерал.', "Zina steps up to his desk: 'Here you go, comrade general.'"),
    (10, 'Вот ваша вилка.', "She hands it to him with a nod: 'Here is your fork.'"),
    (11, 'Мы должны остановить этого народного кандидата.', "Lavrov presents his own plan: 'We must stop this people's candidate.'"),
    (11, 'Тогда выиграет Осипенко.', 'Then Osipenko will win, and the corrupt officials will invest their money.'),
    (12, 'Подожди.', 'General Kruglov pauses with his fork in hand: wait.'),
    (12, 'Ты предлагаешь вмешаться в честный ход выборов?', 'He asks with mock solemnity: are you proposing to interfere in the honest course of the election?'),
    (13, None, 'Lavrov answers plainly: yes.'),
    (14, 'Отлично, занимайтесь!', 'Kruglov beams with approval: excellent, get to work on it!'),
    (0, 'Все на связи.', 'After briefly confusing their town with another case in Khanty-Mansiysk, he signs off: everyone stay in touch.'),
    (15, None, 'Lavrov salutes: yes, sir! Thank you, goodbye — and Colonel Mikhail Mikhailovich immediately sends young Lyova Sokolov back to the archive.'),
]
