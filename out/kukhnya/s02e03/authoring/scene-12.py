# -*- coding: utf-8 -*-
ID = "kukhnya-s02e03-scene-12"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 3
SCENE = 12
TITLE = "Деньги на квартиру  (Money for the Apartment)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S2.03"
SOURCE_FILE = "sources/kukhnya/s02/e03.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "sasha": "anja",
    "kostya": "angelina",
}

LABELS = {
    "anya": "Макс",
    "sasha": "Саша",
    "kostya": "Костя",
}

INTRO = (
    "When they arrive at the apartment, Sasha hands Max the money he needs for rent before saying goodbye. "
    "Inside, Kostya is amazed that Max has his share of the rent and teases him when he learns the cash came from Sasha."
)

OPENER = "Listen to Sasha helping Max with rent and Kostya's reaction inside the apartment."

STORY = [
    ("sasha", "Я слышала, тебе очень нужны деньги.", "I heard you really need money.", [(185, "Я слышала, тебе нужны были деньги")], "Sasha speaks to Max in the hallway"),
    ("sasha", "Тебе ведь надо платить за квартиру.", "After all, you need to pay for the apartment.", [(185, "деньги на квартиру")], "Sasha knows he owes rent to Kostya"),
    ("sasha", "Вот, пожалуйста, возьми эти деньги.", "Here, please, take this money.", [(186, "Вот, возьми")], "Sasha hands him the cash"),
    ("sasha", "Ну ладно, я пойду домой, пока!", "Alright, I will go home, bye!", [(187, "Ну ладно, я пойду. Пока")], "Sasha turns to leave"),
    ("anya", "До завтра, спасибо тебе, Саша!", "Until tomorrow, thank you, Sasha!", [(188, "До завтра"), (189, "Спасибо, Саша")], "Max thanks her warmly"),
    ("kostya", "Ну что, Саша уже уехала?", "So, did Sasha already leave?", [(190, "Че, уехала?")], "Kostya comes into the room"),
    ("anya", "Да, у меня сегодня нет настроения.", "Yes, I am not in a good mood today.", [(190, "Да че-то настроения нет")], "Max feels awkward about taking her money"),
    ("anya", "Возьми на столе деньги за квартиру.", "Take the money for the apartment on the table.", [(191, "Возьми, вон, на столе")], "Max points to the cash on the table"),
    ("kostya", "Ух ты, откуда столько денег?", "Whoa, where is so much money from?", [(192, "Ух ты")], "Kostya is surprised by the full rent payment"),
    ("kostya", "Ты продал своё дорогое кольцо?", "Did you sell your expensive ring?", [(193, "Ты че, кольцо продал?")], "Kostya guesses how Max got the cash"),
    ("anya", "Да нет, мне Саша сейчас дала.", "No, Sasha just gave it to me.", [(193, "Да нет"), (194, "сейчас дала")], "Max admits Sasha lent him the money"),
    ("kostya", "Нормально, ты очень хорошо устроился!", "Nice, you have set yourself up very well!", [(194, "Нормально"), (195, "ты хорошо устроился")], "Kostya teases his roommate"),
    ("anya", "Костя, перестань шутить надо мной!", "Kostya, stop joking about me!", [(196, "Слушай")], "Max tells Kostya to stop teasing"),
]

WALK = [
    (0, None, "'I heard you really need money.' Sasha knows Max has been struggling to pay his share of the rent."),
    (1, None, "'After all, you need to pay for the apartment.' The particle adds a gentle reminder."),
    (2, None, "'Here, please, take this money.' Sasha generously offers him the cash."),
    (3, None, "'Alright, I will go home, bye!' Sasha leaves before Max can refuse."),
    (4, None, "'Until tomorrow, thank you, Sasha!' Max is grateful for her kindness."),
    (5, None, "'So, did Sasha already leave?' Kostya checks if their guest has gone."),
    (6, None, "'Yes, I am not in a good mood today.' Max feels embarrassed about borrowing money from Sasha."),
    (7, None, "'Take the money for the apartment on the table.' Max hands over his half of the rent."),
    (8, None, "'Whoa, where is so much money from?' Kostya did not expect Max to have the money ready."),
    (9, None, "'Did you sell your expensive ring?' Kostya wonders if Max sold the ring he bought earlier."),
    (10, None, "'No, Sasha just gave it to me.' Max honestly tells him where the money came from."),
    (11, None, "'Nice, you have set yourself up very well!' Kostya jokes that Max has a very convenient arrangement."),
    (12, None, "'Kostya, stop joking about me!' Max is not amused by Kostya's teasing."),
]

TRANSITION = "Now listen to the whole apartment scene again."

OUTRO = "Sasha bails Max out with his rent money, giving Kostya plenty of material to tease his best friend."

CLOSING = ("anya", "Главное, что я заплатил за квартиру!")
