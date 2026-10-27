# -*- coding: utf-8 -*-
ID = "kukhnya-s02e01-scene-10"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 10
TITLE = "Пропавшая бутылка  (The Missing Bottle)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "lyova": "anja",
}

LABELS = {
    "anya": "Виктор",
    "lyova": "Лёва",
}

INTRO = (
    "In his office at Claude Monet, Chef Viktor discovers that the bottle of whiskey he bought yesterday has vanished. "
    "He summons his sous-chef Lyova, who nervously tells him that drinking is bad for his health and offers him tea instead."
)

OPENER = "Listen to Chef Viktor confronting Lyova about his missing bottle of whiskey."

STORY = [
    ("anya", "Лёва, быстро иди в мой кабинет!", "Lyova, come quickly to my office!", [(141, "Лева!")], "Viktor shouts for his sous-chef", [], ""),
    ("anya", "Я вчера купил дорогую бутылку виски.", "Yesterday I bought an expensive bottle of whiskey.", [(142, "Я вчера купил бутылку виски")], "Viktor looks inside his empty cabinet", [], ""),
    ("anya", "Скажи мне, где она сейчас?", "Tell me, where is it right now?", [(143, "Где она?")], "Viktor demands to know where his bottle went", [], ""),
    ("lyova", "Виктор Петрович, не нужно вам сегодня пить.", "Viktor Petrovich, you should not drink today.", [(143, "Виктор Петрович, не нужно вам пить")], "Lyova nervously advises his boss", [], ""),
    ("anya", "Что значит мне не нужно пить?", "What does it mean that I should not drink?", [(144, "Что значит не нужно?")], "Viktor is outraged by the remark", [], ""),
    ("lyova", "Ну, просто вам не нужно это.", "Well, you simply do not need this.", [(144, "Ну, не нужно")], "Lyova repeats his excuse timidly", [], ""),
    ("lyova", "Это же очень вредно для здоровья.", "After all, it is very harmful for your health.", [(145, "Это же вредно")], "Lyova claims he is worried about Viktor's health", [], ""),
    ("anya", "Понятно, ты слушаешь нашу новую хозяйку.", "I see, you are listening to our new owner.", [(145, "Понятно", [], ""), (147, "нового хозяина")], "Viktor realizes Kristina ordered Lyova to hide the whiskey", [], ""),
    ("anya", "Тебе нравится выполнять её глупые приказы?", "Do you like following her foolish orders?", [(146, "Ну и какая она на вкус?")], "Viktor mocks Lyova's obedience", [], ""),
    ("lyova", "Шеф, это только ради вашей пользы!", "Chef, this is only for your benefit!", [(148, "Это для вашего же блага")], "Lyova insists he is trying to help", [], ""),
    ("lyova", "Давайте лучше вместе попьём горячего чаю?", "Let us have some hot tea together instead?", [(149, "Давайте лучше чаю попьем")], "Lyova offers a cup of tea instead of whiskey", [], ""),
    ("anya", "Какого ещё чаю на моей кухне?", "What tea in my kitchen?", [(150, "Чаю?")], "Viktor scoffs at the offer of tea", [], ""),
    ("anya", "Уходи отсюда со своим зелёным чаем!", "Get out of here with your green tea!", [(150, "Да пошел ты своим")], "Viktor chases Lyova out of his office", [], ""),
]

WALK = [
    (0, None, "'Lyova, come quickly to my office!' Viktor calls his sous-chef into his office."),
    (1, None, "'Yesterday I bought an expensive bottle of whiskey.' Viktor explains that he left a new bottle in his cabinet."),
    (2, None, "'Tell me, where is it right now?' Viktor demands to know who took his whiskey."),
    (3, None, "'Viktor Petrovich, you should not drink today.' Lyova addresses the chef politely while refusing to return the bottle."),
    (4, None, "'What does it mean that I should not drink?' Viktor cannot believe his own sous-chef is lecturing him."),
    (5, None, "'Well, you simply do not need this.' Lyova tries to stand firm despite being afraid of Viktor."),
    (6, None, "'After all, it is very harmful for your health.' The emphatic particle highlights the health warning."),
    (7, None, "'I see, you are listening to our new owner.' Viktor realizes that Lyova is obeying Kristina's strict ban."),
    (8, None, "'Do you like following her foolish orders?' Viktor is furious that his staff fears the new owner more than him."),
    (9, None, "'Chef, this is only for your benefit!' Lyova insists that hiding the alcohol is for Viktor's own good."),
    (10, None, "'Let us have some hot tea together instead?' Lyova suggests a harmless alternative."),
    (11, None, "'What tea in my kitchen?' Viktor is insulted by the suggestion of drinking tea."),
    (12, None, "'Get out of here with your green tea!' Viktor angrily sends Lyova back to the kitchen."),
]

TRANSITION = "Now listen to the argument between Viktor and Lyova again."

OUTRO = "With even his loyal sous-chef Lyova enforcing the new owner's alcohol ban, Viktor is driven out of his mind."

CLOSING = ("anya", "В моём ресторане спрятали весь алкоголь!")
