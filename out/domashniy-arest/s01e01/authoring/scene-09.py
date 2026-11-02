# Authoring module for domashniy-arest-s01e01-scene-09.
ID = 'domashniy-arest-s01e01-scene-09'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 9
TITLE = 'Я хочу на море!  (I Want to Go to the Sea!)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nina': 'Нина', 'samson': 'Самсон', 'yulia': 'Юля'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "Now we're in the communal flat, in the Samsonovs' small room. Last time, over his morning coffee, Arkady turned down Pasha's big factory deal. Meanwhile Samson, who quit his job yesterday on Arkady's word, is on the phone to his old boss, trying to get it back, while his wife Nina listens. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's go through it together. Samson is calling his old boss, the man he was so rude to yesterday."
TRANSITION = "Let's hear the whole family scene once more."
OUTRO = "That's all for this scene: a lost job, a leaking pipe, and a dream of the sea. Listen out for Nina's 'I want to go to the sea' when you watch. See you next time!"
CLOSING = ('nina', 'Всё, пока!')
STORY = [
    ('samson', 'Николай Филиппович, простите меня, пожалуйста. Я сам не знаю, как это произошло.', "Nikolai Filippovich, please forgive me. I don't know myself how it happened.", [(374, 'простите меня'), (375, 'я сам не знаю, как это произошло')], "'ради бога' -> 'пожалуйста'"),
    ('samson', 'Я вчера ел маринованные грибы. Может, один гриб был плохой.', 'Yesterday I ate pickled mushrooms. Maybe one mushroom was bad.', [(376, 'Я вчера')], "adapted from cues 376-377 ('грибов маринованных хватанул', 'какой-то галлюциногенный попался')"),
    ('nina', 'Тише!', 'Quiet!', [(378, 'Тише')], ''),
    ('samson', 'А что вы так грубо разговариваете?', 'Why are you talking so rudely?', [(380, 'так грубо разговариваете')], "'чего ... сразу' -> 'что'"),
    ('nina', 'Самсонов, ну я же просила!', 'Samsonov, I asked you not to!', [(381, 'Самсонов, ну я же просила')], ''),
    ('samson', 'Ну что, довольна? Теперь новую работу искать.', 'Well, happy now? Now I have to look for a new job.', [(384, 'Ну что, довольна'), (388, 'Теперь новую работу искать')], ''),
    ('nina', 'Тебе же предложили работу. Что, плохая работа?', 'But you were offered a job. What, is it a bad job?', [(391, 'тебе же предложили работу'), (393, 'Что, плохая работа')], "'что ли' dropped"),
    ('samson', 'Подожди, Нин, ты не поняла. Это же стыдно!', "Wait, Nina, you don't get it. It's shameful!", [(394, 'Подожди, Нин, ты не')], "slang 'врубилась' -> 'поняла'; 'Это же стыдно!' new, replacing the crude cue 395"),
    ('nina', 'Ну и что такого?', 'So what?', [(396, 'Ну и что такого')], ''),
    ('nina', 'Юле бы дублёнку купили, Славику бы ноутбук.', 'We could have bought Yulia a sheepskin coat, and Slavik a laptop.', [(402, 'бы дубленку купили'), (403, 'Славику бы ноутбук')], "'Юльке' -> 'Юле'"),
    ('samson', 'Нин, ты что?', "Nina, what's got into you?", [(405, 'Нин, ты')], "'чего гонишься' (slang) -> 'что'"),
    ('nina', 'Меня уже тошнит от этой коммуналки! У нас труба уже неделю течёт.', "I'm sick of this communal flat! Our pipe has been leaking for a week now.", [(415, 'меня уже'), (415, 'тошнит от этой коммуналки'), (416, 'уже неделю течет')], "'вот' dropped; 'стояк' (riser pipe) -> 'труба'"),
    ('samson', 'Я купил герметик. Всё будет нормально.', "I've bought sealant. Everything will be fine.", [(417, 'я купил герметик'), (417, 'все будет')], "slang 'пучком' -> 'нормально'"),
    ('nina', 'Нормально? Она через неделю снова потечёт!', "Fine? It'll be leaking again in a week!", [(418, 'через неделю снова потечет')], "'Пучком!' -> 'Нормально?'; 'он' (стояк) -> 'она' (труба)"),
    ('nina', 'Я уже не могу готовить, стирать, убирать. Я хочу на море!', "I can't take the cooking, washing and cleaning any more. I want to go to the sea!", [(419, 'я уже не могу'), (420, 'готовить'), (421, 'стирать, убирать'), (422, 'А я хочу на море')], "cues 419-422 joined, 'вот это вот' dropped; 'А' dropped from 'А я хочу на море'"),
    ('nina', 'Я хочу нормально жить! Я хочу биде, понимаешь?', 'I want to live like a normal person! I want a bidet, do you understand?', [(423, 'Я хочу нормально жить'), (424, 'хочу, понимаешь')], "cue 424 'Беде' (misheard) -> 'биде'"),
    ('yulia', 'Мам, а что такое биде?', "Mum, what's a bidet?", [(426, 'Мам'), (427, 'Что такое')], "'а' added; cue 427 'беде' -> 'биде'"),
    ('nina', 'В интернете посмотри.', 'Look it up on the internet.', [], "after cue 428 ('Google it')"),
]
WALK = [
    (0, 'Николай Филиппович, простите меня, пожалуйста.', "'Nikolai Filippovich, please forgive me.' He addresses the boss by first name and patronymic, begging pardon with formal \"prostite menya\"."),
    (0, 'Я сам не знаю, как это произошло.', "'I don't know myself how it happened.' \"Sam\" means 'myself' for a male speaker (remember Vika's \"sama\" earlier!), and \"proizoshlo\" means 'it happened'. Then he invents an excuse."),
    (1, None, "'Yesterday I ate pickled mushrooms. Maybe one mushroom was bad.' \"Yel\" is 'ate' and \"griby\" are 'mushrooms' — blaming pickled fungi for yesterday's outburst! Nina wants him quiet."),
    (2, None, "'Quiet!' Literally, 'more quietly' — \"tishe!\" is Russian's everyday 'keep your voice down!'. Still, the boss isn't friendly, and Samson loses his temper."),
    (3, None, "'Why are you talking so rudely?' Even while snapping \"tak grubo\" ('so rudely'), Samson sticks to polite \"razgovarivayete\" with his boss. Nina is in despair."),
    (4, None, "'Samsonov, I asked you not to!' Calling her own husband by his surname \"Samsonov\" shows how furious she is, and \"prosila\" ('asked') carries the female '-a' ending. The call ends badly."),
    (5, 'Ну что, довольна?', "'Well, happy now?' Short \"dovolna?\" ('satisfied?') ends in '-a' because he's asking Nina, who pushed him to make peace with Arkady."),
    (5, 'Теперь новую работу искать.', "'Now I have to look for a new job.' Literally, 'now a new job to search for' — \"iskat\" ('to look for') stands on its own to express a chore ahead."),
    (6, None, "'But you were offered a job. What, is it a bad job?' Literally, 'to you they offered work' — \"tebe zhe predlozhili rabotu\". She means Arkady's offer."),
    (7, None, "'Wait, Nina, you don't get it. It's shameful!' \"Stydno\" means 'it's embarrassing' or 'shameful' — referring to the humiliating kiss Arkady demanded. Nina isn't impressed."),
    (8, None, "'So what?' \"Nu i chto takogo?\" is a brisk, everyday shrug for 'so what's the big deal?'. Then she starts to dream."),
    (9, None, "'We could have bought Yulia a sheepskin coat, and Slavik a laptop.' Tiny \"by\" ('would have') turns the line into wistful daydreaming, while \"Yule\" and \"Slaviku\" mean 'for Yulia' and 'for Slavik'."),
    (10, None, "'Nina, what's got into you?' clipping \"Nina\" to \"Nin\" before \"ty chto?\" ('what are you on about?') shows how shocked Samson is. Now Nina lets everything out."),
    (11, 'Меня уже тошнит от этой коммуналки!', "'I'm sick of this communal flat!' \"Menya toshnit ot...\" literally means 'it makes me nauseous from...' — visceral Russian for 'I'm sick to death of it!'."),
    (11, 'У нас труба уже неделю течёт.', "'Our pipe has been leaking for a week now.' Russian uses present \"techyot\" ('is leaking') with \"uzhe nedelyu\" ('already a week') where English says 'has been leaking'."),
    (12, None, "'I've bought sealant. Everything will be fine.' \"Germetik\" is bathroom sealant, followed by optimistic \"vsyo budet normalno\". Nina throws that right back at him."),
    (13, None, "'Fine? It'll be leaking again in a week!' \"Ona\" ('she') means 'it' here because \"truba\" ('pipe') is feminine, and \"potechyot\" warns 'it'll start leaking again!'."),
    (14, 'Я уже не могу готовить, стирать, убирать.', "'I can't take the cooking, washing and cleaning any more.' Three household chores in a row — \"gotovit\" ('cook'), \"stirat\" ('wash clothes'), \"ubirat\" ('clean up') — all follow \"ne mogu\"."),
    (14, 'Я хочу на море!', "'I want to go to the sea!' Russian needs no 'to go' here: \"ya khochu na more!\" — literally 'I want onto the sea!' — says it all."),
    (15, None, "'I want to live like a normal person! I want a bidet, do you understand?' \"Ponimayesh?\" ('do you understand?') caps her dream of escaping the shared flat for a real bathroom with a \"bide\"."),
    (16, None, "'Mum, what's a bidet?' \"Chto takoye...?\" is the universal Russian question for asking what any unfamiliar word or thing means. Nina's answer is very modern."),
    (17, None, "'Look it up on the internet.' \"V internete posmotri\" puts 'on the internet' first and \"posmotri\" ('have a look') at the end for punch."),
]
