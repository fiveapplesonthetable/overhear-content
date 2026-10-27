# -*- coding: utf-8 -*-
ID = "kukhnya-s02e01-scene-09"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 9
TITLE = "Звонок другу  (Calling a Friend)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
}

LABELS = {
    "anya": "Макс",
    "kostya": "Костя",
}

INTRO = (
    "Stranded outside after Victoria walks away, Max pulls out his phone and calls his best friend Kostya at the bar. "
    "He confesses that his attempt to talk to Victoria failed and begs Kostya to come outside and rescue him."
)

OPENER = "Listen to Max calling Kostya for help after getting stuck outside."

STORY = [
    ("anya", "Алло, Костя, ты меня слышишь?", "Hello, Kostya, can you hear me?", [(140, "Алло, Костян")], "Max calls his best friend on the phone"),
    ("kostya", "Да, Макс, что у тебя случилось?", "Yes, Max, what happened to you?", [(140, "Алло, Костян")], "Kostya answers from behind the bar"),
    ("anya", "У меня сейчас большая проблема.", "I have a big problem right now.", [(140, "Алло, Костян")], "Max admits his plan backfired"),
    ("kostya", "Ты уже поговорил с Викой?", "Did you already talk with Vika?", [(140, "Костян")], "Kostya asks how the apology went"),
    ("anya", "Я хотел с ней серьёзно поговорить.", "I wanted to talk with her seriously.", [(140, "Алло")], "Max explains his intention"),
    ("anya", "Но она просто развернулась и ушла!", "But she just turned around and left!", [(140, "Костян")], "Max tells Kostya that Vika walked away"),
    ("kostya", "Ну и возвращайся обратно на кухню.", "Well then come back to the kitchen.", [(140, "Алло, Костян")], "Kostya tells him to get back to work"),
    ("anya", "В том-то и дело, что не могу!", "That is the thing, I cannot!", [(140, "Алло")], "Max reveals he is stuck"),
    ("kostya", "Почему ты не можешь прийти?", "Why can you not come?", [(140, "Костян")], "Kostya is puzzled"),
    ("anya", "Потому что я потерял маленький ключ.", "Because I lost a small key.", [(140, "Алло, Костян")], "Max confesses his predicament"),
    ("kostya", "Какой ещё ключ ты потерял?", "What key did you lose?", [(140, "Костян")], "Kostya asks for details"),
    ("anya", "Костя, срочно выходи ко мне на улицу!", "Kostya, come out to the street to me urgently!", [(140, "Алло, Костян")], "Max begs Kostya to rescue him"),
    ("kostya", "Ладно, жди там, сейчас приду.", "Fine, wait there, I will come right now.", [(140, "Костян")], "Kostya agrees to help his friend"),
]

WALK = [
    (0, None, "'Hello, Kostya, can you hear me?' Max greets his friend on the phone."),
    (1, None, "'Yes, Max, what happened to you?' Kostya hears the panic in Max's voice."),
    (2, None, "'I have a big problem right now.' Max admits he is in trouble."),
    (3, None, "'Did you already talk with Vika?' Kostya knows Max was trying to apologize to Victoria."),
    (4, None, "'I wanted to talk with her seriously.' Max explains what he tried to do."),
    (5, None, "'But she just turned around and left!' Both past-tense verbs describe Victoria's quick exit."),
    (6, None, "'Well then come back to the kitchen.' Kostya advises him to return to his shift."),
    (7, None, "'That is the thing, I cannot!' This conversational phrase highlights the main problem."),
    (8, None, "'Why can you not come?' Kostya does not understand why Max is still outside."),
    (9, None, "'Because I lost a small key.' Max admits he cannot unlock himself."),
    (10, None, "'What key did you lose?' Kostya is confused by Max's explanation."),
    (11, None, "'Kostya, come out to the street to me urgently!' Max begs his friend to hurry outside."),
    (12, None, "'Fine, wait there, I will come right now.' Kostya agrees to come and help him out."),
]

TRANSITION = "Now listen to the phone call between Max and Kostya again."

OUTRO = "Only a loyal friend like Kostya will drop his work at the bar to rescue Max from his latest blunder."

CLOSING = ("anya", "Спасибо, друг, я очень тебя жду!")
