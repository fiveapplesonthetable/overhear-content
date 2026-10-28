# Authoring module for domashniy-arest-s01e11-scene-06.
ID = 'domashniy-arest-s01e11-scene-06'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 11
SCENE = 6
TITLE = "Визит президента  (The President's Visit)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'aide': 'Помощник', 'pasha': 'Паша'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.11'
SOURCE_FILE = 'sources/domashniy-arest/s01/e11.ru.dual.srt'
INTRO = "A moment later, acting mayor Pavel Yuryevich hears alarming political news from his campaign aide. The aide reports that the president is visiting the region to meet candidate Samsonov in person. Pavel realizes with dread that no meetings are planned with him or the regional governor. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine Pavel's shocking political discovery line by line. His aide delivers the news of the upcoming presidential visit."
TRANSITION = "Now let's listen to Pavel and his aide's conversation once more without pauses."
OUTRO = 'Shaken by the news, Pavel realizes that his opponent has secured the ultimate endorsement. See you next time!'
CLOSING = ('aide', 'Пока!')
STORY = [
    ('pasha', 'Так, ещё раз внятно повторите.', 'So, repeat that clearly once more.', [(105, 'еще раз внятно')], ''),
    ('aide', 'Сам президент скоро приедет к нам.', 'the president will arrive here soon.', [(106, 'Президент'), (108, 'решил заглянуть к нам')], ''),
    ('aide', 'Он посетит аэродром в нашей области.', 'He will visit an airfield in our region.', [(107, 'военный аэродром')], ''),
    ('aide', 'Он хочет лично познакомиться с Иваном Самсоновым.', 'He wants to meet Ivan Samsonov in person.', [(108, 'лично познакомиться с'), (108, 'Иваном Самсоновым')], ''),
    ('pasha', 'Подождите, это вообще точная информация?', 'Wait, is this information accurate at all?', [(109, 'эту информацию подтвердили')], ''),
    ('aide', 'Мы связались с администрацией президента.', 'We contacted the presidential administration.', [(109, 'Мы связались с администрацией президента')], ''),
    ('aide', 'Там эту информацию официально подтвердили.', 'There they officially confirmed this information.', [(109, 'там эту информацию подтвердили')], ''),
    ('pasha', 'А со мной встреча будет?', 'And will there be a meeting with me?', [(110, 'А со мной')], ''),
    ('aide', 'Больше никаких визитов не запланировано.', 'No further visits are planned.', [(111, 'Больше никаких визитов не запланировано')], ''),
    ('pasha', 'А как же действующий губернатор?', 'And what about the current governor?', [(113, 'губернатором')], ''),
    ('pasha', 'Я тоже могу туда подъехать!', 'I can drive over there too!', [(112, 'я тоже подъеду')], ''),
    ('aide', 'Нет, с губернатором они тоже не встречаются.', 'No, they are not meeting with the governor either.', [(113, 'Нет, с губернатором тоже не встречаются')], ''),
    ('aide', 'Президент встретится только с Самсоновым.', 'The president will meet only with Samsonov.', [(113, 'только с Самсоновым')], ''),
    ('pasha', 'Это просто катастрофа для нашей кампании!', 'This is simply a catastrophe for our campaign!', [], 'Pavel panics over the exclusive presidential endorsement'),
]
WALK = [
    (0, None, "'So, repeat that clearly once more.' Pavel is so rattled by what he just heard that he makes his assistant say it all over again."),
    (1, None, "'The president himself will arrive here soon.' Across town at city hall, the same news lands like a bomb rather than a gift."),
    (2, None, "'He will visit an airfield in our region.' It is a quick stopover at the local airfield, not a grand tour of the city."),
    (3, None, "'He wants to meet Ivan Samsonov in person.' Out of everyone in the province, the head of state asked for the ordinary guy from the communal flat."),
    (4, None, "'Wait, is this information accurate at all?' Pavel is grasping at straws, hoping the whole report is just a rumor."),
    (5, None, "'We contacted the presidential administration.' His assistant has already checked straight with Moscow."),
    (6, None, "'There they officially confirmed this information.' No rumor, no mistake: the visit is locked in."),
    (7, None, "'And will there be a meeting with me?' Notice how small Pavel sounds here, asking if there is a slot for him too."),
    (8, None, "'No further visits are planned.' That cold bureaucratic reply leaves Pavel completely out in the cold."),
    (9, None, "'And what about the current governor?' Surely the regional boss isn't being skipped too! \"A kak zhe\" is how Russians ask \"and what about...?\""),
    (10, None, "'I can drive over there too!' Now Pavel is ready to crash the airfield uninvited just to get in the frame."),
    (11, None, "'No, they are not meeting with the governor either.' Even the governor is shut out, which shows how tightly Moscow is stage-managing this stop."),
    (12, None, "'The president will meet only with Samsonov.' \"Only with Samsonov\" is the nightmare line for Pavel's entire campaign."),
    (13, None, "'This is simply a catastrophe for our campaign!' One handshake at the airfield is enough to wipe out Pavel's lead overnight."),
]
