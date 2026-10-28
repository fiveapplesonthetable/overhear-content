# Authoring module for kukhnya-s06e13-scene-06.
ID = 'kukhnya-s06e13-scene-06'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 13
SCENE = 6
TITLE = 'Неожиданное увольнение  (An Unexpected Firing)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'mikhail': 'Михаил', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.13'
SOURCE_FILE = 'sources/kukhnya/s06/e13.ru.srt'
INTRO = 'Before Katya can respond emotionally, Senya and Fedya overhear that Denis is leaving for Voronezh tomorrow. Word spreads through the hallway, and Mikhail immediately takes Denis to accounting to fire him.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Denis's clever plan backfires immediately as Mikhail marches him off to sign his termination papers. See you next time!"
CLOSING = ('mikhail', 'До завтра!')
STORY = [
    ('senya', 'Ты что, реально уже завтра уезжаешь?', 'Are you really leaving tomorrow already?', [(81, 'реально завтра уезжаешь')], 'adapted'),
    ('senya', 'Он даже никого заранее не предупредил.', 'He did not even warn anyone in advance.', [(83, 'Даже не предупредил')], 'adapted'),
    ('senya', 'Денис завтра уезжает в Воронеж навсегда.', 'Denis is leaving for Voronezh forever tomorrow.', [(83, 'уезжает в Воронеж навсегда')], 'adapted'),
    ('senya', 'У Кости теперь хорошая комната освобождается.', "A nice room is freeing up at Kostya's place now.", [(84, 'комната освобождается')], 'adapted'),
    ('senya', 'Вот это действительно очень большие новости.', 'Now this is truly very big news.', [(86, 'Вот это новости')], 'adapted'),
    ('mikhail', 'А кто будет играть на пианино?', 'And who is going to play the piano?', [(87, 'кто будет играть на пианино')], 'adapted'),
    ('mikhail', 'Так, я сейчас ничего не понял.', 'Alright, I did not understand anything right now.', [(88, 'Я не понял')], 'adapted'),
    ('mikhail', 'Денис, мне самому за рояль сесть?', 'Denis, should I sit down at the grand piano myself?', [(89, 'за рояль самому сесть')], 'adapted'),
    ('senya', 'Он же завтра уезжает от нас навсегда.', 'He is leaving us forever tomorrow.', [(90, 'уезжает завтра навсегда')], 'adapted'),
    ('mikhail', 'А раньше нельзя было мне сказать?', 'Could you not have told me earlier?', [(91, 'раньше нельзя было сказать')], 'adapted'),
    ('mikhail', 'Ладно, тогда идём сейчас за расчётом.', 'Fine, then let us go get your final pay now.', [(92, 'идем за счет')], 'adapted'),
    ('denis', 'Подождите, я что, уже совсем уволен?', 'Wait, am I already completely fired?', [(93, 'Я что, уволен')], 'adapted'),
]
WALK = [
    (0, None, "'Are you really leaving tomorrow already?' Senya quizzes evenly before Denis can change the subject."),
    (1, None, '\'He did not even warn anyone in advance.\' Senya underscores one direct element for Mikhail: "predupredil" means "warned" (from "predupredit"), giving the line its exact edge.'),
    (2, None, "'Denis is leaving for Voronezh forever tomorrow.' Senya responds promptly before Denis, so Denis knows he is not just making small talk."),
    (3, None, "'A nice room is freeing up at Kostya's place now.' Senya holds firm openly with a sigh, steering the talk right where he wants it."),
    (4, None, '\'Now this is truly very big news.\' Senya grounds one pointed choice on cue: "deystvitelno" means "really, indeed", and it carries the main weight of what Senya is saying.'),
    (5, None, '\'And who is going to play the piano?\' Mikhail frames this statement without pause: putting the question word "kto" right at the front of the line lets Senya hear the point of the question on the very first beat.'),
    (6, None, "'Alright, I did not understand anything right now.' Mikhail fires back bluntly with a smile, before Denis can change the subject."),
    (7, None, '\'Denis, should I sit down at the grand piano myself?\' Mikhail leans on this vivid touch right here: "royal" means "grand piano", and it carries the main weight of what Mikhail is saying.'),
    (8, None, "'He is leaving us forever tomorrow.' Senya answers evenly to settle things, shifting the whole mood of the room in a single beat."),
    (9, None, "'Could you not have told me earlier?' Mikhail asks straight out how Senya expects that to work in practice."),
    (10, None, '\'Fine, then let us go get your final pay now.\' Mikhail favors this sharp detail for Denis: "raschyotom" means "final pay, settlement" (from "raschyot"), giving the line its exact edge.'),
    (11, None, '\'Wait, am I already completely fired?\' Denis makes this warning around Senya: adding "sovsem" ("completely, at all") pushes the statement all the way, leaving zero room for doubt.'),
]
