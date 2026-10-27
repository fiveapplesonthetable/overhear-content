# -*- coding: utf-8 -*-
ID = "kukhnya-s02e01-scene-07"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 7
TITLE = "Серьёзный разговор  (A Serious Conversation)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "vika": "anja",
}

LABELS = {
    "anya": "Макс",
    "vika": "Вика",
}

INTRO = (
    "In the dining room of Claude Monet, Max tries to apologize to Victoria for his awful mistake. "
    "Victoria refuses to listen to him, so Max decides to take drastic action to make her stay and talk."
)

OPENER = "Listen to Max begging Victoria for a chance to explain himself."

STORY = [
    ("anya", "Вика, подожди меня одну минуту!", "Vika, wait for me for one minute!", [(135, "Вик, нам нужно поговорить")], "Max catches up to Victoria in the hall"),
    ("anya", "Нам очень нужно серьёзно поговорить.", "We really need to talk seriously.", [(135, "нам нужно поговорить")], "Max begs her for a conversation"),
    ("vika", "У меня сейчас много работы в зале.", "I have a lot of work in the hall right now.", [(135, "Мне не о чем с тобой разговаривать")], "Victoria refuses to stop working"),
    ("vika", "И мне не о чем с тобой говорить.", "And I have nothing to talk to you about.", [(135, "Мне не о чем с тобой разговаривать")], "Victoria coldly rejects Max"),
    ("anya", "Пожалуйста, выслушай меня хотя бы раз!", "Please listen to me at least once!", [(135, "нам нужно поговорить")], "Max pleads for a chance to explain"),
    ("vika", "Я уже всё видела своими глазами.", "I already saw everything with my own eyes.", [(135, "с тобой разговаривать")], "Victoria reminds him of his betrayal"),
    ("anya", "Это была ужасная и глупая ошибка.", "It was a terrible and foolish mistake.", [(136, "А я думаю, есть о чем")], "Max admits his guilt"),
    ("vika", "Оставь меня в покое, Максим.", "Leave me alone, Maxim.", [(135, "Мне не о чем")], "Victoria tries to walk past him"),
    ("anya", "Нет, я так просто не уйду!", "No, I will not leave so easily!", [(136, "А я думаю")], "Max blocks her path"),
    ("anya", "А я думаю, нам надо поговорить, Вика.", "And I think we need to talk, Vika.", [(136, "А я думаю, есть о чем, Вик")], "Max insists they have things to discuss"),
    ("vika", "Что ты делаешь у двери?", "What are you doing by the door?", [(136, "есть о чем, Вик")], "Victoria sees Max reaching for the exit"),
    ("anya", "Теперь ты точно меня спокойно выслушаешь.", "Now you will definitely listen to me calmly.", [(136, "А я думаю, есть о чем")], "Max prepares a desperate stunt"),
    ("vika", "Открой эту дверь прямо сейчас!", "Open this door right now!", [(135, "с тобой разговаривать")], "Victoria demands that he let her pass"),
]

WALK = [
    (0, None, "'Vika, wait for me for one minute!' Max stops Victoria in the restaurant hall."),
    (1, None, "'We really need to talk seriously.' The impersonal construction with the dative pronoun expresses strong necessity."),
    (2, None, "'I have a lot of work in the hall right now.' Victoria uses her duties as a reason not to speak with him."),
    (3, None, "'And I have nothing to talk to you about.' Victoria makes it clear she does not want to hear his excuses."),
    (4, None, "'Please listen to me at least once!' Max begs her to hear his side of the story."),
    (5, None, "'I already saw everything with my own eyes.' The instrumental plural emphasizes what she witnessed herself."),
    (6, None, "'It was a terrible and foolish mistake.' Max admits that what he did was completely wrong."),
    (7, None, "'Leave me alone, Maxim.' Using his full name shows how angry and distant Victoria feels."),
    (8, None, "'No, I will not leave so easily!' Max refuses to give up."),
    (9, None, "'And I think we need to talk, Vika.' Max insists that their relationship is worth discussing."),
    (10, None, "'What are you doing by the door?' Victoria notices Max blocking the way."),
    (11, None, "'Now you will definitely listen to me calmly.' Max believes he can force her to hear him out."),
    (12, None, "'Open this door right now!' Victoria angrily orders him to step aside."),
]

TRANSITION = "Now listen to the confrontation in the hall again."

OUTRO = "Max is determined to make Victoria listen, even if his impulsive plan only makes her angrier."

CLOSING = ("anya", "Вика, пожалуйста, просто послушай меня!")
