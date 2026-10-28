# Authoring module for kukhnya-s03e03-scene-05.
ID = 'kukhnya-s03e03-scene-05'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 3
SCENE = 5
TITLE = 'Взрыв на кухне  (Explosion in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.03'
SOURCE_FILE = 'sources/kukhnya/s03/e03.ru.srt'
INTRO = 'In the kitchen, Fedya and Senya compete to flirt with Katya over the cutting board until Chef Barinov pulls his daughter into his office and forbids her from flirting with his cooks.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes Scene Five. Notice how Katya's attempt to annoy her overprotective father backfires when Elena walks in right behind her. Until next time!"
CLOSING = ('katya', 'Пока!')
STORY = [
    ('katya', 'Неправильно режешь? Ну покажите как.', 'Cutting it wrong? Well, show me how.', [(72, 'Неправильно режешь'), (73, 'Ну покажите как')], 'adapted'),
    ('fedya', 'Ты думаешь, ей приятно, что мы её режем?', 'Do you think she likes that we are cutting her?', [(74, 'Ты думаешь, ей приятно, что мы ее'), (74, 'режем')], 'adapted'),
    ('katya', 'Не знаю насчёт камбалы, но мне очень приятно.', "I don't know about the flounder, but I find it very pleasant.", [(75, 'Не знаю насчет'), (75, 'но мне очень приятно')], 'adapted'),
    ('fedya', 'А я могу научить тебя правильно резать мясо.', 'And I can teach you how to cut meat properly.', [(76, 'А я могу научить тебя правильно резать мясо')], ''),
    ('fedya', 'Мясо любой дурак может порезать.', 'Any fool can cut meat.', [(77, 'Мясо любой дурак может порезать')], ''),
    ('fedya', 'Он вообще кроме рыбы ничего не может.', 'He cannot do anything at all except fish.', [(79, 'Он вообще кроме рыбы ничего не может')], ''),
    ('barinov', 'Екатерина, зайдите ко мне.', 'Yekaterina, come into my office.', [(80, 'Екатерина, зайдите ко мне')], ''),
    ('barinov', 'Это что за взрыв ты устроила на моей кухне?', 'What kind of explosion did you stage in my kitchen?', [(81, 'Это что за'), (81, 'взрыв ты'), (82, 'устроила на моей кухне')], 'adapted'),
    ('katya', 'Какой взрыв? Я просто вливаюсь в новый коллектив.', 'What explosion? I am simply blending into the new team.', [(82, 'Какой взрыв'), (83, 'Я просто вливаюсь в новый коллектив')], 'adapted'),
    ('katya', 'А можно меня не учить? Мне давно не пятнадцать лет.', "And can you not lecture me? I haven't been fifteen for a long time.", [(85, 'А можно меня не учить? Мне давно не')], 'adapted'),
    ('barinov', 'На моей кухне тебе всегда будет пятнадцать.', 'In my kitchen you will always be fifteen.', [(86, 'На моей кухне тебе всегда будет')], 'adapted'),
    ('barinov', 'Я тебе запрещаю! Куда пошла?', 'I forbid you! Where are you going?', [(87, 'запрещаю. Куда пошла')], 'adapted'),
]
WALK = [
    (0, None, '\'Cutting it wrong? Well, show me how.\' Replying naturally on the spot, Katya puts the question word "kak" right at the start so Fedya hears the focus immediately.'),
    (1, None, "'Do you think she likes that we are cutting her?' Fedya asks sharply why things suddenly took this turn between them."),
    (2, None, '\'I don\'t know about the flounder, but I find it very pleasant.\' Pointing to the flounder beside Fedya, Katya leans on "kambaly" ("flounder", a form of "kambala") to give the remark its edge.'),
    (3, None, "'And I can teach you how to cut meat properly.' Fedya counters boldly in their talk, refusing to let the moment slip past."),
    (4, None, "'Any fool can cut meat.' Fedya steps in right away around Katya, leaving no doubt about where he stands."),
    (5, None, '\'He cannot do anything at all except fish.\' Turning to the fish right here, Fedya brings in "voobshche" ("at all") to make the meaning unmistakable.'),
    (6, None, "'Yekaterina, come into my office.' Reacting boldly with Fedya, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (7, None, "'What kind of explosion did you stage in my kitchen?' Barinov checks deadpan how Katya expects that to work in practice."),
    (8, None, '\'What explosion? I am simply blending into the new team.\' Pointing to the staff in the exchange, Katya lands on "kollektiv" ("staff, collective") as the key everyday word here.'),
    (9, None, '\'And can you not lecture me? I haven\'t been fifteen for a long time.\' Looking over warmly with Barinov, Katya leans on "mozhno" ("it is possible, one may"), which carries the whole predicate in Russian without needing "it is".'),
    (10, None, "'In my kitchen you will always be fifteen.' Barinov cuts in steadily with a smile, watching Katya's face to see how the news lands."),
    (11, None, '\'I forbid you! Where are you going?\' Barinov proceeds sharply around Katya and lands on "zapreshchayu" ("forbid", built on "zapreshchat") to keep the statement grounded.'),
]
