# domashniy-arest/s01e09/scene-18.py
ID = "domashniy-arest-s01e09-scene-18"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 18
TITLE = "Верните мои документы!  (Return My Documents!)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест S01E09"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"
VOICES = {"narrator": "sky", "pasha": "anja", "guard": "angelina"}
LABELS = {"pasha": "Паша", "guard": "Охранник"}
INTRO = "Pavel Osipenko pushes past the security guards and storms angrily into the regional administration office to demand his campaign documents back from Boris."
STORY = [
    ("guard", "Сюда нельзя входить без пропуска.", "You cannot enter here without a pass.", [], "new guard line"),
    ("pasha", "Отпусти ты меня немедленно!", "Let go of me immediately!", [(568, 'Отпусти ты меня!'), (570, 'Отпусти, я сказал!')], "adapted cues 568 and 570"),
    ("pasha", "Привет, Паша! Чего ты хотел?", "Hi, Pasha! What did you want?", [(573, 'Привет, Паша! Чего хотел?')], "adapted cue 573"),
    ("pasha", "Вы мне ещё привет говорите?", "You are still saying hello to me?", [(574, 'Вы мне еще приветкаете, да? Не стыдно?')], "adapted cue 574"),
    ("pasha", "Вам совсем не стыдно?", "Aren't you ashamed at all?", [(574, 'Не стыдно?')], ""),
    ("pasha", "Что тебе нужно, спрашиваю?", "What do you need, I am asking?", [(575, 'Чего хотел, спрашиваю?')], "adapted cue 575"),
    ("pasha", "Вы меня жестоко обманули.", "You cruelly deceived me.", [(576, 'Вы меня обманули и кинули.')], "adapted cue 576"),
    ("pasha", "Я вам не маленький мальчик!", "I am not a little boy to you!", [(576, 'Я вам что, пацан, что ли?')], "adapted cue 576"),
    ("pasha", "Быстро верните мне мои документы.", "Quickly return my documents to me.", [(577, 'А ну-ка быстро вернули мне мои документы.')], "adapted cue 577"),
    ("pasha", "Верните все три папки!", "Return all three folders!", [(578, 'Все три папки.')], "adapted cue 578"),
    ("pasha", "Паша, документы уже в архиве.", "Pasha, the documents are already in the archive.", [(579, 'Паша, документы все в архиве.')], "adapted cue 579"),
    ("pasha", "Вернуть ничего невозможно.", "It is impossible to return anything.", [(580, 'вернуть ничего невозможно.')], ""),
    ("pasha", "Ты подлый человек, Боря!", "You are a despicable man, Borya!", [(581, 'Скотина! Боря!')], "adapted cue 581"),
    ("pasha", "Охрана, уведите его отсюда!", "Security, take him away from here!", [(584, 'Уберите макаку эту!')], "adapted cue 584"),
    ("guard", "Пойдёмте на выход, гражданин.", "Let's head to the exit, citizen.", [], "new guard reaction"),
]
OPENER = "Now let's see how Pavel Osipenko demands the return of his secret documents."
WALK = [
    (1, None, "'Let go of me immediately!' This phrase demands release from physical restraint."),
    (3, None, "'You are still saying hello to me?' Osipenko is offended by the casual greeting after being betrayed."),
    (8, None, "'Quickly return my documents to me.' This phrase calls for the immediate return of his property."),
    (11, None, "'It is impossible to return anything.' The descriptive phrase word indicates that the requested action cannot be done."),
    (13, None, "'Security, take him away from here!' Boris summons the guards to escort his former ally out."),
]
TRANSITION = "Let's listen to the heated argument once again from the beginning."
OUTRO = "Boris has the guards remove Osipenko from the office. See you next time!"
CLOSING = ("pasha", "Пока!")
