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
    (0, None, "'Are you really leaving tomorrow already?' Senya quizzes evenly about what Mikhail just brought up."),
    (1, None, '\'He did not even warn anyone in advance.\' Senya speaks directly on the spot and leans on "predupredil" ("warned", a form of "predupredit") to give the remark its edge.'),
    (2, None, '\'Denis is leaving for Voronezh forever tomorrow.\' Senya steps in smoothly with Denis and puts the weight on "uyezzhayet" ("is leaving", from "uyezzhat") as the exchange unfolds.'),
    (3, None, "'A nice room is freeing up at Kostya's place now.' Senya pushes back openly watching Mikhail, shifting the mood of the conversation in a single beat."),
    (4, None, '\'Now this is truly very big news.\' Talking about the news in the exchange, Senya uses "deystvitelno" ("really, indeed") to carry the main weight of the thought.'),
    (5, None, '\'And who is going to play the piano?\' Answering smoothly in this beat, Mikhail puts the question word "kto" right at the start so Senya hears the focus immediately.'),
    (6, None, "'Alright, I did not understand anything right now.' Mikhail steps in bluntly facing Senya, to clear the air between them once and for all."),
    (7, None, '\'Denis, should I sit down at the grand piano myself?\' Addressing the grand piano during the talk, Mikhail centers the remark on "royal" ("grand piano") without any extra fuss.'),
    (8, None, '\'He is leaving us forever tomorrow.\' Senya continues promptly during the talk and centers the thought on "uyezzhayet" ("is leaving", from "uyezzhat") without wasting a word.'),
    (9, None, "'Could you not have told me earlier?' Mikhail asks straight out how Senya expects that to work in practice."),
    (10, None, '\'Fine, then let us go get your final pay now.\' Talking about the final pay in this beat, Mikhail centers the thought on "raschyotom" ("final pay, settlement", from "raschyot") without wasting a word.'),
    (11, None, '\'Wait, am I already completely fired?\' Holding firm openly at once, Denis adds "sovsem" ("completely, at all") so the statement leaves zero room for doubt.'),
]
