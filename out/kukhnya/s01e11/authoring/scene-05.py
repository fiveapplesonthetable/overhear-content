"""Authoring module for Kukhnya s01e11 scene 05."""
from pathlib import Path

ID = "kukhnya-s01e11-scene-05"
TITLE = "В поисках критика  (In Search of the Critic)"
LEVEL = "A1"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 5

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "max": "anja",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Костя",
    "max": "Макс",
}

SOURCE_NAME = "Кухня s01e11"
SOURCE_FILE = Path("sources/kukhnya/s01/e11.ru.dual.srt")
SOURCE_NOTE = "Cues 66-70 at the restaurant bar."

INTRO = (
    "In this scene by the bar, Kostya and Max survey the dining room guests with keen detective curiosity. "
    "Knowing that a dreaded restaurant critic is visiting Claude Monet, the two friends analyze each customer's food and wine choices. "
    "Listen to their conversation in Russian first, and then we will examine each sentence."
)

OPENER = (
    "Now, let us examine the vocabulary and phrasing of this entertaining dining room investigation."
)

STORY = [
    ("anya", "Макс, смотри внимательно на зал!", "Max, look carefully at the dining room!", [], "new"),
    ("max", "Кто же из них может быть критиком?", "Which one of them could be the critic?", [(66, "Кто же из них может быть критиком?")], "verbatim"),
    ("anya", "Эти двое работают в соседнем банке.", "Those two work at the bank next door.", [(67, "работают в соседнем банке.")], "adapted: shortened"),
    ("max", "Да, они наши постоянные гости.", "Yes, they are our regular guests.", [(67, "Эти двое постоянные гости")], "adapted: shortened"),
    ("anya", "А тот мужчина у окна?", "And that man by the window?", [], "new"),
    ("max", "Он заказал рыбу и красное вино.", "He ordered fish and red wine.", [(68, "Рыба и красное вино.")], "adapted: added verb"),
    ("anya", "Нет, настоящий критик такого не закажет.", "No, a real critic will not order that.", [(69, "Нет.")], "adapted: expanded rationale"),
    ("max", "А парень за столиком номер три?", "What about the guy at table number three?", [], "new"),
    ("anya", "Он слишком молод для ресторанного критика.", "He is too young for a restaurant critic.", [(70, "Слишком молод")], "adapted: completed thought"),
    ("max", "Критики обычно сидят в одиночестве.", "Critics usually sit in solitude.", [], "new"),
    ("anya", "И записывают всё в блокнот.", "And write down everything in a notepad.", [], "new"),
    ("max", "Смотри, женщина за седьмым столиком!", "Look, the woman at table seven!", [], "new"),
    ("anya", "Она очень строго смотрит на меню.", "She is looking very strictly at the menu.", [], "new"),
    ("max", "Кажется, мы нашли нашего критика!", "It seems we found our critic!", [], "new"),
]

WALK = [
    (0, None, "'Max, look carefully at the dining room!' Kostya urges his friend to scan the tables."),
    (1, None, "'Which one of them could be the critic?' Max wonders as he observes the guests."),
    (2, None, "'Those two work at the bank next door.' Kostya identifies familiar neighborhood patrons of the bar."),
    (3, None, "'Yes, they are our regular guests.' Max rules them out based on past visits."),
    (4, None, "'And that man by the window?' Kostya points toward a solitary diner."),
    (5, None, "'He ordered fish and red wine.' Max evaluates the strange culinary combination."),
    (6, None, "'No, a real critic will not order that.' Kostya dismisses him for poor gastronomic pairing."),
    (7, None, "'What about the guy at table number three?' Max directs his attention to another table."),
    (8, None, "'He is too young for a restaurant critic.' Kostya doubts that a young person holds such authority."),
    (9, None, "'Critics usually sit in solitude.' Max shares his knowledge of food review behavior."),
    (10, None, "'And write down everything in a notepad.' Kostya adds another telltale sign of an undercover reviewer."),
    (11, None, "'Look, the woman at table seven!' Max spots a promising new candidate."),
    (12, None, "'She is looking very strictly at the menu.' Kostya observes the severe facial expression on her face."),
    (13, None, "'It seems we found our critic!' Max concludes excitedly after noticing her behavior."),
]

TRANSITION = (
    "Now, let us listen to the complete scene again to practice your comprehension."
)

OUTRO = (
    "A charming scene full of fun observations about restaurant habits and undercover reviewers."
)

CLOSING = ("anya", "Надо срочно предупредить нашего шефа!")
