# -*- coding: utf-8 -*-
ID = "kukhnya-s02e01-scene-08"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 8
TITLE = "Побег Вики  (Vika's Escape)"
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
    "Outside the restaurant, Max chains himself in a foolish attempt to prove his devotion and force Victoria to talk. "
    "Instead of being moved, Victoria calls him a complete fool and walks away, leaving him stuck alone."
)

OPENER = "Listen to Victoria reacting to Max's ridiculous stunt outside Claude Monet."

STORY = [
    ("anya", "Видишь, теперь я никуда не уйду.", "See, now I am not going anywhere.", [(137, "Ну ты придурок")], "Max shows off his desperate stunt outside"),
    ("vika", "Макс, что это у тебя на руке?", "Max, what is that on your hand?", [(137, "Ну ты придурок")], "Victoria stares at his wrist in disbelief"),
    ("anya", "Я сделал это только ради тебя!", "I did this only for your sake!", [(138, "Ты куда, Вик?")], "Max hopes she will be impressed"),
    ("vika", "Ну ты просто полный дурак!", "You are just a complete fool!", [(137, "Ну ты придурок")], "Victoria calls his plan idiotic"),
    ("anya", "Зато теперь у нас есть время.", "At least now we have time.", [(138, "Вик, ты куда?")], "Max thinks she has to stay with him"),
    ("vika", "У меня нет времени на твои глупости.", "I have no time for your nonsense.", [(137, "ты придурок")], "Victoria refuses to play along"),
    ("anya", "Подожди, не уходи от меня!", "Wait, do not walk away from me!", [(138, "Ты куда, Вик?")], "Max realizes Victoria is turning around"),
    ("vika", "Сиди здесь один со своими идеями.", "Sit here alone with your ideas.", [(137, "Ну ты придурок")], "Victoria walks off down the street"),
    ("anya", "Ты куда идёшь, Вика?", "Where are you going, Vika?", [(138, "Ты куда, Вик?")], "Max calls out as she leaves"),
    ("anya", "Вика, ну ты куда пошла?", "Vika, well where did you go?", [(138, "Вик, ты куда?")], "Max panics because he cannot follow her"),
    ("vika", "Я иду обратно на свою работу!", "I am going back to my work!", [(138, "Ты куда, Вик?")], "Victoria heads back toward the restaurant"),
    ("anya", "Стой, пожалуйста, вернись ко мне!", "Stop, please come back to me!", [(139, "Стой!")], "Max shouts after her desperately"),
    ("anya", "Не оставляй меня тут одного!", "Do not leave me here alone!", [(139, "Стой!")], "Max is left stranded outside"),
]

WALK = [
    (0, None, "'See, now I am not going anywhere.' Max proudly shows that he has locked himself in place."),
    (1, None, "'Max, what is that on your hand?' Victoria looks at the lock on his wrist in shock."),
    (2, None, "'I did this only for your sake!' The preposition with the genitive pronoun means 'for your sake'."),
    (3, None, "'You are just a complete fool!' Victoria is completely unimpressed by his dramatic gesture."),
    (4, None, "'At least now we have time.' Max assumes she will stay and talk with him."),
    (5, None, "'I have no time for your nonsense.' Victoria refuses to waste a single minute on his prank."),
    (6, None, "'Wait, do not walk away from me!' Max panics as Victoria turns her back."),
    (7, None, "'Sit here alone with your ideas.' Victoria leaves him to deal with the consequences himself."),
    (8, None, "'Where are you going, Vika?' Max calls out as she walks away."),
    (9, None, "'Vika, well where did you go?' Unable to move from the spot, Max watches her disappear."),
    (10, None, "'I am going back to my work!' Victoria returns to the restaurant."),
    (11, None, "'Stop, please come back to me!' The imperative begs her to stop and return."),
    (12, None, "'Do not leave me here alone!' Max is trapped outside by his own foolish plan."),
]

TRANSITION = "Now listen to the entire scene outside the restaurant again."

OUTRO = "Max's grand romantic gesture backfires completely, leaving him trapped outside while Victoria goes back to work."

CLOSING = ("anya", "Вика, стой, не уходи так быстро!")
