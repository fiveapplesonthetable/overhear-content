# -*- coding: utf-8 -*-
ID = "kukhnya-s02e03-scene-15"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 3
SCENE = 15
TITLE = "Забытый салат  (The Forgotten Salad)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S2.03"
SOURCE_FILE = "sources/kukhnya/s02/e03.ru.dual.srt"

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
    "In the kitchen, Victoria complains that guests in the dining room have been waiting ages for their salad while Senya is nowhere to be found. "
    "Trying to help, Max grabs the bowl sitting on Senya's counter and puts it on the pass, unaware that it contains Senya's sliced leather belt."
)

OPENER = "Listen to Victoria and Max looking for the missing salad order in the kitchen."

STORY = [
    ("vika", "Макс, скажи, где сейчас Сеня?", "Max, tell me, where is Senya right now?", [(278, "Где Сеня?")], "Victoria rushes into the kitchen looking for Senya"),
    ("anya", "Он только что вышел из кухни.", "He just stepped out of the kitchen.", [(278, "Где Сеня?")], "Max looks around Senya's empty station"),
    ("vika", "Гости в зале ждут свой заказ!", "The guests in the hall are waiting for their order!", [(278, "Там у вас салат уже полдня ждут")], "Victoria complains about the delay"),
    ("vika", "Они ждут этот салат очень долго.", "They have been waiting for this salad for a very long time.", [(278, "салат уже полдня ждут")], "Victoria points to the order ticket"),
    ("anya", "Сеня уже давно приготовил салат.", "Senya prepared the salad a long time ago.", [(278, "салат")], "Max remembers seeing Senya chop the greens"),
    ("vika", "Тогда почему блюдо ещё на кухне?", "Then why is the dish still in the kitchen?", [(279, "на столик раздачи поставить")], "Victoria demands an explanation"),
    ("vika", "Ну что за странный человек!", "Well what a strange person!", [(279, "Что за человек?")], "Victoria is exasperated with Senya"),
    ("vika", "Разве трудно поставить тарелку на стол?", "Is it really hard to put the plate on the table?", [(279, "Трудно, что ли, на столик раздачи поставить")], "Victoria points toward the pass table"),
    ("anya", "Смотри, вот стоит какая-то тарелка.", "Look, here stands some plate.", [(279, "на столик")], "Max spots a bowl of salad on Senya's counter"),
    ("vika", "Наверное, это и есть наш салат.", "Probably this is our salad.", [(278, "салат")], "Victoria assumes the salad is for the guest"),
    ("anya", "Давай я быстро отнесу его официанту.", "Let me quickly take it to the waiter.", [(279, "поставить")], "Max picks up Senya's special belt salad by mistake"),
    ("vika", "Да, поставь его скорее на стол!", "Yes, put it on the table quickly!", [(279, "на столик раздачи поставить")], "Victoria hurries Max along"),
    ("anya", "Готово, теперь гости будут довольны.", "Done, now the guests will be satisfied.", [(278, "ждут")], "Max places the wrong salad on the pass"),
]

WALK = [
    (0, None, "'Max, tell me, where is Senya right now?' Victoria enters the kitchen looking for the cook."),
    (1, None, "'He just stepped out of the kitchen.' Max explains that Senya left his station a moment ago."),
    (2, None, "'The guests in the hall are waiting for their order!' Victoria stresses that the customers are getting impatient."),
    (3, None, "'They have been waiting for this salad for a very long time.' Russian uses the present tense for an action that started in the past and continues now."),
    (4, None, "'Senya prepared the salad a long time ago.' Max recalls seeing Senya make a salad earlier."),
    (5, None, "'Then why is the dish still in the kitchen?' Victoria wonders why it was never served."),
    (6, None, "'Well what a strange person!' This exclamatory phrase expresses frustration."),
    (7, None, "'Is it really hard to put the plate on the table?' Cooks must place finished dishes on the pass table for the waiters."),
    (8, None, "'Look, here stands some plate.' Max notices a finished salad sitting on Senya's counter."),
    (9, None, "'Probably this is our salad.' Neither of them realizes Senya mixed his leather belt into that bowl."),
    (10, None, "'Let me quickly take it to the waiter.' Max offers to carry the plate to the pass."),
    (11, None, "'Yes, put it on the table quickly!' Victoria tells him to hurry so the waiter can serve it."),
    (12, None, "'Done, now the guests will be satisfied.' Max unwittingly sends the belt salad out to the dining room."),
]

TRANSITION = "Now listen to Victoria and Max in the kitchen again."

OUTRO = "Thinking they have solved the delay, Max and Victoria accidentally send Senya's leather belt salad out to a guest."

CLOSING = ("anya", "Заказ уже готов и ждёт официанта!")
