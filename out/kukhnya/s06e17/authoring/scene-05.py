# Authoring module for kukhnya-s06e17-scene-05.
ID = 'kukhnya-s06e17-scene-05'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 17
SCENE = 5
TITLE = "Жена инспектора  (The Inspector's Wife)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'guest': 'Гость'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.17'
SOURCE_FILE = 'sources/kukhnya/s06/e17.ru.srt'
INTRO = "Fedya argues against opening the cooler door for fear of prison, when the inspector's wife suddenly arrives looking for her husband. Chef Barinov lies that he hasn't seen him and orders Fedya to keep an eye on her."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Chef Barinov sends Fedya to watch the inspector's wife, little suspecting that Fedya will misunderstand that instruction too. Until next time!"
CLOSING = ('fedya', 'До встречи!')
STORY = [
    ('fedya', 'Не открывайте эту дверь сейчас.', 'Do not open this door right now.', [(65, 'Не открывайте')], 'adapted'),
    ('fedya', 'Нас всех за это засудят.', 'They will prosecute all of us for this.', [(65, 'нас всех засудят')], 'adapted'),
    ('fedya', 'А мне в тюрьму нельзя.', 'And I cannot go to prison.', [(65, 'а мне в тюрьму нельзя')], 'adapted'),
    ('barinov', 'Открывайте, он же там замёрзнет.', 'Open up, he will freeze in there.', [(67, 'открывайте, он же'), (68, 'Самерзнет')], 'adapted'),
    ('guest', 'Здравствуйте, сюда заходил мой муж?', 'Hello, did my husband stop by here?', [(69, 'Здравствуйте. К вам не заходил мой муж')], 'adapted'),
    ('guest', 'Он хотел поговорить с шефом.', 'He wanted to speak with the chef.', [(70, 'Он собирался поговорить с')], 'adapted'),
    ('barinov', 'Нет, он сюда не заходил.', 'No, he did not come in here.', [(71, 'Нет, не заходил')], 'adapted'),
    ('fedya', 'Шеф, а если она запаникует?', 'Chef, what if she panics?', [(72, 'Шеф, а если она запаникует')], 'adapted'),
    ('fedya', 'Она же сразу полицию вызовет.', 'She will call the police right away.', [(72, 'и полицию вызовет')], 'adapted'),
    ('barinov', 'Надо тихо проследить за ней.', 'We need to quietly keep an eye on her.', [(73, 'Надо за ней проследить')], 'adapted'),
    ('barinov', 'Федя, его жена на тебе.', 'Fedya, his wife is your responsibility.', [(74, 'Федя, жена на тебе')], 'adapted'),
    ('barinov', 'А с ним попробуем договориться.', 'And we will try to reach an agreement with him.', [(76, 'мы попробуем договориться')], 'adapted'),
]
WALK = [
    (0, None, '\'Do not open this door right now.\' Pointing to the door at once, Fedya chooses "otkryvayte" ("open", from the root "otkryvat") so Barinov hears the exact meaning.'),
    (1, None, "'They will prosecute all of us for this.' Fedya chimes in honestly with Barinov, grounding the moment in plain reality."),
    (2, None, '\'And I cannot go to prison.\' Turning to the prison at once, Fedya chooses "tyurmu" ("prison", from the root "tyurma") so Barinov hears the exact meaning.'),
    (3, None, '\'Open up, he will freeze in there.\' Barinov fires back openly before Fedya and uses "otkryvayte" ("open", from "otkryvat") to make the point stick.'),
    (4, None, '\'Hello, did my husband stop by here?\' The guest calmly sends this formal greeting with Barinov using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (5, None, '\'He wanted to speak with the chef.\' The guest follows up boldly around Barinov and brings in "pogovorit" ("to talk") to make the meaning unmistakable.'),
    (6, None, '\'No, he did not come in here.\' Barinov cuts in promptly during the talk and reaches for the Russian word "zakhodil" ("went in", built from "zakhodit") right at the center of the line.'),
    (7, None, "'Chef, what if she panics?' Fedya probes openly where this conversation is heading next."),
    (8, None, '\'She will call the police right away.\' Turning to the police beside Barinov, Fedya uses "politsiyu" ("the police", from "politsiya") to make the point stick.'),
    (9, None, '\'We need to quietly keep an eye on her.\' Following up plainly on the spot, Barinov leans on "nado" ("it is necessary, one needs to"), which carries the whole predicate in Russian without needing "it is".'),
    (10, None, "'Fedya, his wife is your responsibility.' Barinov follows up calmly with a nod, watching Fedya's face to see how the news lands."),
    (11, None, '\'And we will try to reach an agreement with him.\' Barinov chimes in naturally at once and uses "dogovoritsya" ("to reach an agreement") to carry the main weight of the thought.'),
]
