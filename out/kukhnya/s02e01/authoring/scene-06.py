# -*- coding: utf-8 -*-
ID = "kukhnya-s02e01-scene-06"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 6
TITLE = "Поиски коньяка  (Searching for Cognac)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "lui": "anja",
    "senya": "angelina",
}

LABELS = {
    "anya": "Виктор",
    "lui": "Луи",
    "senya": "Сеня",
}

INTRO = (
    "In the kitchen of Claude Monet, Chef Viktor is desperate for a drink after the new owner bans him from having alcohol. "
    "He searches Louis's pastry counter and stops Senya, confiscating a box of chocolates filled with cognac."
)

OPENER = "Listen to Chef Viktor searching the kitchen for hidden alcohol."

STORY = [
    ("anya", "Луи, что тут у тебя на столе?", "Louis, what do you have here on the table?", [(122, "что тут у тебя?")], "Viktor checks Louis's pastry station"),
    ("lui", "Ну, шеф, пожалуйста, тихо!", "Come on, chef, please, easy!", [(123, "Ну, шеф, ну! Тих")], "Louis tries to hide his ingredients"),
    ("anya", "Что в этой красивой бутылке?", "What is in this nice bottle?", [(124, "А какой кот?")], "Viktor inspects the bottle"),
    ("lui", "Мне нельзя ничего вам говорить.", "I am not allowed to tell you anything.", [(125, "Мне не можно говорить")], "Louis obeys the new owner's rule"),
    ("anya", "Быстро говори, что это такое!", "Tell me quickly what this is!", [(126, "Говори, какой кот")], "Viktor demands an answer from the pastry chef"),
    ("lui", "Это французский сироп для торта.", "It is French syrup for a cake.", [(127, "французская")], "Louis claims it is only for baking"),
    ("anya", "Сеня, ну-ка, стоять на месте!", "Senya, hold it right there!", [(128, "Ну-ка, стоять")], "Viktor spots Senya sneaking past"),
    ("anya", "Для кого эта коробка?", "Who is this box for?", [(129, "Это для кого?")], "Viktor points at the box in Senya's hands"),
    ("senya", "Так это подарок для вас, шеф!", "Well, this is a gift for you, chef!", [(130, "Так это, ну... Ну, шефу?")], "Senya nervously invents an excuse"),
    ("anya", "А, ну да, конечно, для шефа.", "Ah, right, of course, for the chef.", [(131, "А, ну да, для шефа")], "Viktor takes the box from him"),
    ("anya", "Ещё раз увижу такое — уволю!", "If I see this again, I will fire you!", [(132, "Еще раз увижу, уволил")], "Viktor warns Senya against hiding things"),
    ("senya", "Шеф, а какие там конфеты?", "Chef, and what kind of candies are in there?", [(133, "И конфетки?")], "Senya watches Viktor open the box"),
    ("anya", "Отличные конфеты с французским коньяком!", "Great candies with French cognac!", [(134, "С коньяком")], "Viktor happily eats the liquor-filled chocolates"),
]

WALK = [
    (0, None, "'Louis, what do you have here on the table?' Viktor approaches the pastry table looking for something to drink."),
    (1, None, "'Come on, chef, please, easy!' Louis tries to calm his boss down."),
    (2, None, "'What is in this nice bottle?' Viktor spots an interesting bottle on the counter."),
    (3, None, "'I am not allowed to tell you anything.' The new owner ordered the staff to keep alcohol away from Viktor."),
    (4, None, "'Tell me quickly what this is!' The imperative demands an immediate answer."),
    (5, None, "'It is French syrup for a cake.' Louis claims the bottle only contains sweet baking syrup."),
    (6, None, "'Senya, hold it right there!' Viktor catches Senya trying to sneak across the kitchen."),
    (7, None, "'Who is this box for?' The preposition with the genitive case asks who the recipient is."),
    (8, None, "'Well, this is a gift for you, chef!' Senya pretends the stolen box is a present for Viktor."),
    (9, None, "'Ah, right, of course, for the chef.' Viktor gladly accepts the excuse and takes the box."),
    (10, None, "'If I see this again, I will fire you!' Viktor warns Senya not to steal from the kitchen again."),
    (11, None, "'Chef, and what kind of candies are in there?' Senya is curious about the chocolates inside."),
    (12, None, "'Great candies with French cognac!' Viktor is delighted to find liquor inside the chocolates."),
]

TRANSITION = "Now listen to the whole kitchen search again without pauses."

OUTRO = "Even when every bottle in the kitchen is hidden, Chef Viktor manages to find cognac inside a box of chocolates."

CLOSING = ("anya", "Наконец-то я нашёл вкусный коньяк!")
