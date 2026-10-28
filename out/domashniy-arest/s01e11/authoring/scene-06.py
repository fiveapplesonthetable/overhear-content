# domashniy-arest/s01e11/scene-06.py
ID = "domashniy-arest-s01e11-scene-06"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 6
TITLE = "Визит президента  (The President's Visit)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"
VOICES = {"narrator": "sky", "aide": "angelina", "pasha": "anja"}
LABELS = {"aide": "Помощник", "pasha": "Паша"}
INTRO = "A moment later, acting mayor Pavel Yuryevich hears alarming political news from his campaign aide. The aide reports that the president is visiting the region to meet candidate Samsonov in person. Pavel realizes with dread that no meetings are planned with him or the regional governor. Let's listen to their conversation in Russian first."
STORY = [
    ("pasha", "Так, ещё раз внятно повторите.", "So, repeat that clearly once more.", [(105, 'еще раз внятно')], ""),
    ("aide", "Сам президент скоро приедет к нам.", "the president will arrive here soon.", [(106, 'Президент'), (108, 'решил заглянуть к нам')], ""),
    ("aide", "Он посетит аэродром в нашей области.", "He will visit an airfield in our region.", [(107, 'военный аэродром')], ""),
    ("aide", "Он хочет лично познакомиться с Иваном Самсоновым.", "He wants to meet Ivan Samsonov in person.", [(108, 'лично познакомиться с'), (108, 'Иваном Самсоновым')], ""),
    ("pasha", "Подождите, это вообще точная информация?", "Wait, is this information accurate at all?", [(109, 'эту информацию подтвердили')], ""),
    ("aide", "Мы связались с администрацией президента.", "We contacted the presidential administration.", [(109, 'Мы связались с администрацией президента')], ""),
    ("aide", "Там эту информацию официально подтвердили.", "There they officially confirmed this information.", [(109, 'там эту информацию подтвердили')], ""),
    ("pasha", "А со мной встреча будет?", "And will there be a meeting with me?", [(110, 'А со мной')], ""),
    ("aide", "Больше никаких визитов не запланировано.", "No further visits are planned.", [(111, 'Больше никаких визитов не запланировано')], ""),
    ("pasha", "А как же действующий губернатор?", "And what about the current governor?", [(113, 'губернатором')], ""),
    ("pasha", "Я тоже могу туда подъехать!", "I can drive over there too!", [(112, 'я тоже подъеду')], ""),
    ("aide", "Нет, с губернатором они тоже не встречаются.", "No, they are not meeting with the governor either.", [(113, 'Нет, с губернатором тоже не встречаются')], ""),
    ("aide", "Президент встретится только с Самсоновым.", "The president will meet only with Samsonov.", [(113, 'только с Самсоновым')], ""),
    ("pasha", "Это просто катастрофа для нашей кампании!", "This is simply a catastrophe for our campaign!", [], "Pavel panics over the exclusive presidential endorsement"),
]
OPENER = "Now let's examine Pavel's shocking political discovery line by line. His aide delivers the news of the upcoming presidential visit."
WALK = [
    (0, None, "'So, repeat that clearly once more.' Pavel demands a clear repetition."),
    (1, None, "'The president himself will arrive here soon.' The future verb indicates an imminent official arrival."),
    (2, None, "'He will visit an airfield in our region.' The location phrase specifies the geographic location."),
    (3, None, "'He wants to meet Ivan Samsonov in person.' The modal construction takes an 'with'-form object."),
    (4, None, "'Wait, is this information accurate at all?' Pavel questions the credibility of the sudden report."),
    (5, None, "'We contacted the presidential administration.' The self-action verb form verb governs an 'with'-form complement."),
    (6, None, "'There they officially confirmed this information.' The past plural verb indicates confirmation from officials."),
    (7, None, "'And will there be a meeting with me?' Pavel asks nervously."),
    (8, None, "'No further visits are planned.' The short passive form denotes completed scheduling."),
    (9, None, "'And what about the current governor?' Pavel brings up regional leadership with an emphatic particle."),
    (10, None, "'I can drive over there too!' The modal verb expresses Pavel's desperate eagerness to attend."),
    (11, None, "'No, they are not meeting with the governor either.' The reciprocal self-action verb form shows strict protocol."),
    (12, None, "'The president will meet only with Samsonov.' The restrictive particle emphasizes Samsonov's exclusive status."),
    (13, None, "'This is simply a catastrophe for our campaign!' Pavel laments the devastating blow to his chances."),
]
TRANSITION = "Now let's listen to Pavel and his aide's conversation once more without pauses."
OUTRO = "Shaken by the news, Pavel realizes that his opponent has secured the ultimate endorsement. See you next time!"
CLOSING = ("aide", "Пока!")
