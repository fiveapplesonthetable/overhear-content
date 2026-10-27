# -*- coding: utf-8 -*-
ID = "kukhnya-s02e03-scene-11"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 3
SCENE = 11
TITLE = "Поездка домой  (Riding Home)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S2.03"
SOURCE_FILE = "sources/kukhnya/s02/e03.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "sasha": "anja",
}

LABELS = {
    "anya": "Макс",
    "sasha": "Саша",
}

INTRO = (
    "Outside the restaurant after their evening shift, Max tells Sasha not to worry because he can catch a cab home. "
    "Sasha insists on driving him herself, though she grows annoyed when Max asks why she seems upset."
)

OPENER = "Listen to Max and Sasha talking outside the restaurant before driving home."

STORY = [
    ("anya", "Да ты не волнуйся так сильно.", "Do not worry so much.", [(181, "Да ты не парься")], "Max tells Sasha not to worry outside"),
    ("anya", "Я сейчас быстро поймаю машину.", "I will quickly catch a car right now.", [(182, "Тачку сломлю")], "Max says he can hail a cab"),
    ("sasha", "Я сама отвезу тебя до дома.", "I will drive you home myself.", [(183, "Саша, все нормально?")], "Sasha insists on giving him a ride"),
    ("anya", "Саша, у тебя всё нормально?", "Sasha, is everything alright with you?", [(183, "Саша, все нормально?")], "Max notices that Sasha looks upset"),
    ("sasha", "Да, у меня всё хорошо.", "Yes, everything is fine with me.", [(183, "все нормально")], "Sasha replies curtly"),
    ("anya", "Ты почему такая грустная весь вечер?", "Why are you so sad all evening?", [(183, "Саша, все нормально?")], "Max asks about her mood"),
    ("sasha", "Ну вот ты опять начинаешь!", "Well here you go starting again!", [(184, "Ну ты опять")], "Sasha gets annoyed by his questions"),
    ("sasha", "Мы же сегодня утром уже поговорили.", "After all, we already talked this morning.", [(184, "Ну мы же утром поговорили")], "Sasha reminds him of their morning talk"),
    ("anya", "Я просто хотел тебя спросить.", "I just wanted to ask you.", [(183, "все нормально")], "Max tries to explain himself"),
    ("sasha", "Мы с тобой просто хорошие друзья.", "You and I are just good friends.", [(184, "утром поговорили")], "Sasha insists they are only friends"),
    ("anya", "Ладно, я тебя прекрасно понял.", "Fine, I understood you very well.", [(181, "Да ты не парься")], "Max drops the subject"),
    ("sasha", "Тогда садись скорее в машину.", "Then get into the car quickly.", [(182, "Тачку")], "Sasha unlocks her car"),
    ("anya", "Спасибо, что отвезёшь меня домой.", "Thank you for driving me home.", [(183, "Саша")], "Max gets into the passenger seat"),
]

WALK = [
    (0, None, "'Do not worry so much.' Max tries to put Sasha at ease after work."),
    (1, None, "'I will quickly catch a car right now.' Max offers to hail a taxi on the street."),
    (2, None, "'I will drive you home myself.' Sasha insists on giving him a ride in her car."),
    (3, None, "'Sasha, is everything alright with you?' Max notices the tension in her voice."),
    (4, None, "'Yes, everything is fine with me.' Sasha brushes off his concern."),
    (5, None, "'Why are you so sad all evening?' Max wonders why she has been quiet all shift."),
    (6, None, "'Well here you go starting again!' Sasha is frustrated that he keeps bringing up their relationship."),
    (7, None, "'After all, we already talked this morning.' They agreed earlier not to complicate things between them."),
    (8, None, "'I just wanted to ask you.' Max says he was only checking on her."),
    (9, None, "'You and I are just good friends.' Sasha reminds him of the boundary they set."),
    (10, None, "'Fine, I understood you very well.' Max accepts her answer."),
    (11, None, "'Then get into the car quickly.' Sasha motions toward the car door."),
    (12, None, "'Thank you for driving me home.' Max appreciates the ride home."),
]

TRANSITION = "Now listen to the conversation between Max and Sasha again."

OUTRO = "Even though Sasha claims they are only friends, offering Max a ride home shows she still cares about him."

CLOSING = ("anya", "Поехали скорее домой отдыхать!")
