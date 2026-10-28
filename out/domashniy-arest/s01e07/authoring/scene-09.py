# domashniy-arest/s01e07/scene-09.py
ID = "domashniy-arest-s01e07-scene-09"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 9
TITLE = "Сырное фондю  (Cheese Fondue)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"
VOICES = {"narrator": "sky", "samson": "anja", "nina": "angelina"}
LABELS = {"samson": "Самсон", "nina": "Нина"}
INTRO = "Last time, Governor Viktor Stepanovich threatened to abandon Pasha Osipenko after Samsonov's poll ratings caught up with his. Meanwhile, Samsonov comes home to the communal flat with sweets for the weekend, only to find Nina and the children laughing over a board game with polite lawyer Danya. Let's listen in Russian first."
STORY = [
    ("samson", "Привет, Ваня!", "Hi, Vanya!", [(355, 'Привет'), (355, 'Вань')], ""),
    ("samson", "Привет. А что тут происходит?", "Hi. And what is going on here?", [(356, 'Привет'), (357, 'А что тут происходит')], ""),
    ("nina", "Это отличная игра! Хочешь с нами поиграть? Бери карты.", "It's a great game! Do you want to play with us? Take some cards.", [(359, 'игра'), (361, 'Хочешь с нами поиграть? Бери карты')], ""),
    ("samson", "Да нет, не хочу играть. Я думал, выходные проведу с семьёй.", "No, I don't want to play. I thought I'd spend the weekend with my family.", [(362, 'Да нет, не хочу'), (362, 'Не хочу играть'), (363, 'я думал'), (363, 'выходные проведу с семьей')], ""),
    ("samson", "Вот детям конфет купил. А семья и без меня хорошо время проводит!", "I bought sweets for the kids here. Yet the family is having a good time without me!", [(365, 'детям'), (367, 'семья и без меня хорошо время проводит')], ""),
    ("samson", "Даня, а ты что тут делаешь?", "Danya, what are you doing here?", [(369, 'а ты что тут делаешь')], "cue 368 'Дань' -> 'Даня'"),
    ("samson", "Я к Аркадию Борисовичу пришёл.", "I came to see Arkady Borisovich.", [(370, 'Я к Аркадию'), (371, 'Борисовичу')], "cue 372 ASR 'решил' -> 'пришёл'"),
    ("samson", "Жену свою вижу, детей своих вижу. А Аркадия Борисовича тут не вижу!", "I see my wife, I see my kids. But I don't see Arkady Borisovich here!", [(375, 'жену свою вижу'), (376, 'детей своих вижу'), (377, 'Аркадия Борисовича не вижу')], ""),
    ("samson", "Его на скорой увезли.", "They took him away in an ambulance.", [(380, 'скорой увезли')], "cue 380 ASR 'И вон нас с скорой увезли' -> 'Его на скорой увезли'"),
    ("samson", "Я знаю! Хочешь, сейчас и тебя туда увезут?", "I know! Do you want them to take you there right now too?", [(382, 'Хочешь, сейчас'), (382, 'тебя туда увезут')], ""),
    ("nina", "Самсонов, успокойся! Аркаша был занят. И мы пригласили Даню чай попить.", "Samsonov, calm down! Arkasha was busy. And we invited Danya for tea.", [(384, 'Аркаша был занят, мы пригласили Даню чай попить')], "'остынь' -> 'успокойся'"),
    ("samson", "Ладно, я, пожалуй, пойду. Пока, Нина!", "Alright, I think I'll get going. Bye, Nina!", [(386, 'Ладно, я, пожалуй, пойду'), (391, 'пока')], ""),
    ("samson", "Давай, иди! А завтра он что принесёт? Сырное фондю?", "Go on, go! And what is he bringing tomorrow? Cheese fondue?", [(388, 'Давай'), (393, 'Он завтра'), (393, 'фондю')], "Slavik's explanation of fondue in 393-396 folded in"),
    ("samson", "Он будет у меня заикаться тоненьким голоском! Я тебе всё сказал!", "He'll be stammering in a tiny voice when I'm done with him! I've told you everything!", [(399, 'Будет заикаться тоненьким голоском'), (402, 'Я тебе все сказал')], "crude threats in 397-398 and 'блин' in 399 omitted"),
    ("nina", "Только тронь его пальцем! Мы всегда рады видеть Даню здесь.", "Just lay a finger on him! We are always glad to see Danya here.", [(400, 'Только тронь его'), (403, 'всегда рады здесь')], "crude threat in 401 omitted"),
    ("samson", "Я тебя предупредил!", "I've warned you!", [(404, 'Я тебя предупредил')], ""),
    ("nina", "Я тебя тоже предупредила!", "I've warned you too!", [(405, 'Я тебя тоже предупредила')], ""),
]
OPENER = "Let's walk through it. Since moving into a campaign hotel suite on Ilona's orders, Samsonov has missed his family, and he walks in to find Danya sitting at his table."
WALK = [
    (0, None, "'Hi, Vanya!' Danya greets him cheerfully over the board-game cards. Samsonov frowns."),
    (1, None, "'Hi. And what is going on here?' Nina smiles and holds up a deck of picture cards."),
    (2, None, "'It's a great game! Do you want to play with us? Take some cards.' Samsonov sulks in the doorway."),
    (3, None, "'No, I don't want to play. I thought I'd spend the weekend with my family.' He sets down the bags he brought."),
    (4, None, "'I bought sweets for the kids here. Yet the family is having a good time without me!' Then he glares directly at Danya."),
    (5, None, "'Danya, what are you doing here?' Danya explains politely."),
    (6, None, "'I came to see Arkady Borisovich.' Notice the preposition with the 'to/for' form for visiting a person. Samsonov looks around the room with heavy sarcasm."),
    (7, None, "'I see my wife, I see my kids. But I don't see Arkady Borisovich here!' Danya points out why Arkady isn't here."),
    (8, None, "'They took him away in an ambulance.' Samsonov steps closer to Danya."),
    (9, None, "'I know! Do you want them to take you there right now too?' Nina immediately intervenes."),
    (10, None, "'Samsonov, calm down! Arkasha was busy. And we invited Danya for tea.' Sensing the tension, Danya stands up."),
    (11, None, "'Alright, I think I'll get going. Bye, Nina!' Once Danya leaves, young Slavik mentions that Danya promised to bring a fondue pot tomorrow so they can dip bread into melted cheese."),
    (12, None, "'Go on, go! And what is he bringing tomorrow? Cheese fondue?' Samsonov is furious."),
    (13, None, "'He'll be stammering in a tiny voice when I'm done with him! I've told you everything!' Nina stands her ground."),
    (14, None, "'Just lay a finger on him! We are always glad to see Danya here.' Notice the singular command 'just touch him' used as a warning: 'don't you dare touch him!'"),
    (15, None, "'I've warned you!' Masculine past tense from Samsonov."),
    (16, None, "'I've warned you too!' And feminine past tense with the '-a' ending from Nina."),
]
TRANSITION = "Now let's hear the whole family argument in the Samsonovs' room again."
OUTRO = "So Samsonov's jealousy over polite lawyer Danya and his cheese fondue is boiling over — and tonight he will turn to Sun Tzu's Art of War for advice. See you next time!"
CLOSING = ("nina", "Пока!")
