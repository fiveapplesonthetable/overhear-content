ID = "kukhnya-s01e15-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 2
TITLE = "Лишний сосед  (An Extra Roommate)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja", "nastya": "angelina"}
LABELS = {"anya": "Макс", "kostya": "Костя", "nastya": "Настя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues 6-14. Max enters bedroom, Nastya demands he moves out."

INTRO = "Max enters the bedroom inviting Kostya and Nastya to the cinema, driving Nastya to her limit. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("nastya", "Это моя мочалка, а это Костина.",
     "This is my loofah, and this one is Kostya's.",
     [(6, "Это моя мочалка, а это Костина.")], "adapted"),
    ("anya", "Слышь, народ, давай в кино сходим?",
     "Hey, guys, let us go to the cinema?",
     [(7, "Слышь, народ, давай в кино сходим")], "adapted"),
    ("kostya", "Макс, мы спим уже давно.",
     "Max, we have been sleeping for a long time.",
     [(8, "Макс, мы спим")], "adapted"),
    ("nastya", "Да. Точнее, мы спали.",
     "Yes. More precisely, we were sleeping.",
     [(9, "Да. Точнее, спали")], "adapted"),
    ("anya", "Ну, давай попозже сходим вместе.",
     "Well, let us go later together.",
     [(10, "Ну, давай попозже сходим")], "adapted"),
    ("kostya", "Ты же видишь, что мы отдыхаем.",
     "You see that we are resting.",
     [], "new"),
    ("nastya", "Иди спать, пожалуйста, Макс!",
     "Go to sleep, please, Max!",
     [(11, "Спать")], "adapted"),
    ("anya", "Ну, понятно, я ухожу к себе.",
     "Well, understood, I am going to my room.",
     [(12, "Ну, понятно")], "adapted"),
    ("nastya", "Всё, я так больше не могу!",
     "That is it, I cannot take this anymore!",
     [(13, "Все. Я так больше не могу.")], "adapted"),
    ("kostya", "Настя, успокойся, он просто наш друг.",
     "Nastya, calm down, he is just our friend.",
     [], "new"),
    ("nastya", "Он постоянно заходит в нашу комнату!",
     "He constantly walks into our room!",
     [], "new"),
    ("nastya", "Я хочу, чтобы Макс съехал отсюда!",
     "I want Max to move out of here!",
     [(14, "Я хочу, чтоб Макс съехал")], "adapted"),
]

OPENER = "Let's break down this tense discussion."

WALK = [
    (0, None,
     "'This is my loofah, and this one is Kostya's.' -- She shows the new bathroom items to him."),
    (1, None,
     "'Hey, guys, let us go to the cinema?' -- Max invites the couple to a film screening."),
    (2, None,
     "'Max, we have been sleeping for a long time.' -- Kostya tells him that they are in bed."),
    (3, None,
     "'Yes. More precisely, we were sleeping.' -- Nastya points out that he woke them up."),
    (4, None,
     "'Well, let us go later together.' -- Max suggests that they can watch it in the evening."),
    (5, None,
     "'You see that we are resting.' -- Kostya asks him to show some respect for their sleep."),
    (6, None,
     "'Go to sleep, please, Max!' -- Nastya angrily demands that he leave their room immediately."),
    (7, None,
     "'Well, understood, I am going to my room.' -- Max realizes that he should leave them alone."),
    (8, None,
     "'That is it, I cannot take this anymore!' -- Nastya bursts out with frustration after he leaves."),
    (9, None,
     "'Nastya, calm down, he is just our friend.' -- Kostya tries to pacify her with gentle words."),
    (10, None,
     "'He constantly walks into our room!' -- She explains that she needs personal space and privacy."),
    (11, None,
     "'I want Max to move out of here!' -- She demands that Kostya make his buddy find another place."),
]

TRANSITION = "Now let's listen to the scene again without interruption."
OUTRO = "Nastya makes it clear to Kostya that Max cannot stay in their apartment any longer."
CLOSING = ("nastya", "Я хочу, чтобы Макс съехал отсюда!")
