# Authoring module for domashniy-arest-s01e09-scene-01.
ID = 'domashniy-arest-s01e09-scene-01'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 9
SCENE = 1
TITLE = "Я не изменял тебе  (I Didn't Cheat on You)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.09'
SOURCE_FILE = 'sources/domashniy-arest/s01/e09.ru.dual.srt'
INTRO = "In this opening scene of episode nine, Ivan Samsonov and his wife Nina are in bed late at night arguing about his behavior at the political concert. Furious at rumors of infidelity, Samsonov insists he did nothing wrong and angrily threatens her with divorce, while Nina laughs off his dramatic threats. Let's listen to the scene in Russian first; don't worry about catching every word."
OPENER = "Now let's examine Ivan and Nina's midnight bedroom argument line by line. Ivan sits up in bed frowning in the dark."
TRANSITION = "Now let's listen to the entire bedroom argument again without interruption."
OUTRO = "Despite his angry divorce threats, Samsonov's bluster fails to intimidate his wife. See you next time!"
CLOSING = ('samson', 'Пока!')
STORY = [
    ('samson', 'Сколько раз тебе говорить?', 'How many times do I have to tell you?', [(1, 'Сколько раз')], ''),
    ('samson', 'Я просто сходил на концерт.', 'I just went to a concert.', [(1, 'я просто сходил'), (1, 'на концерт')], ''),
    ('samson', 'Я был там с одноклассником.', 'I was there with a classmate.', [(1, 'с одноклассником')], ''),
    ('samson', 'Я тебе не изменял!', "I didn't cheat on you!", [(2, 'Я тебя не изменял')], 'corrected grammar from dialectal тебя -> тебе'),
    ('nina', 'А люди говорят другое.', 'And people say otherwise.', [], 'added dialogue line'),
    ('samson', 'Мне всё равно, что ты думаешь!', "I don't care what you think!", [(3, 'Да мне'), (3, 'как ты считаешь')], 'slang пофиг softened to всё равно'),
    ('samson', 'Ты меня поняла?', 'Did you understand me?', [(3, 'поняла')], ''),
    ('samson', 'Я разведусь с тобой!', 'I will divorce you!', [(4, 'Я разведусь с тобой')], ''),
    ('samson', 'Тебе всё понятно?', 'Is everything clear to you?', [(4, 'понятно')], ''),
    ('nina', 'Самсон, ну всё, хватит.', "Samson, that's enough, stop it.", [(6, 'Самсон, ну все')], ''),
    ('nina', 'Не смеши меня, пожалуйста.', "Don't make me laugh, please.", [(6, 'не смеши меня')], ''),
    ('nina', 'Пойдём уже спать.', "Let's just go to sleep.", [(7, 'Пойдем спать')], ''),
    ('samson', 'Посмотрим, Нина. Посмотрим.', 'We will see, Nina. We will see.', [(8, 'Посмотрим')], ''),
]
WALK = [
    (0, None, "'How many times do I have to tell you?' Samsonov expresses exasperation."),
    (1, None, "'I just went to a concert.' Samsonov insists his night out was completely innocent, just a quick trip to the concert."),
    (2, None, "'I was there with a classmate.' He claims he was only hanging out there with an old friend from school."),
    (3, None, "'I didn't cheat on you!' Backed into a corner, he swears up and down that he stayed faithful to her."),
    (4, None, "'And people say otherwise.' Nina remains skeptical about his late-night whereabouts."),
    (5, None, "'I don't care what you think!' Literally, 'to me it is all the same' — he snaps that he couldn't care less what she believes."),
    (6, None, "'Did you understand me?' He barks a sharp check to make sure his threat is sinking in."),
    (7, None, "'I will divorce you!' Out of patience, Samsonov escalates the fight by threatening to end their marriage."),
    (8, None, "'Is everything clear to you?' Samsonov demands acknowledgment."),
    (9, None, "'Samson, that's enough, stop it.' Nina brushes off his outburst like a tired parent calming down a cranky child."),
    (10, None, "'Don't make me laugh, please.' She tells him to stop being ridiculous because she doesn't buy his tough act for a second."),
    (11, None, "'Let's just go to sleep.' Nina tries to defuse the midnight argument and turn off the light."),
    (12, None, "'We will see, Nina. We will see.' Stung by her laughter, he mutters a dark warning twice under his breath."),
]
