"""Scene 46 — What Kind of Infirmary Is This? (s01e08, 01:07:43–01:09:05)."""

ID = "domashniy-arest-s01e08-scene-46"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 46
TITLE = "Что у вас за лазарет?  (What Kind of Infirmary Is This?)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.08"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "nina": "angelina",
    "yulya": "anja",
}

LABELS = {
    "anya": "Самсон",
    "nina": "Нина",
    "yulya": "Юля",
}

INTRO = (
    "Last time in the surveillance van, Major Lavrov hatched a new scheme to investigate "
    "Marina's corrupt former lover Eduard Valentinovich. Back in the Samsonov flat, Nina "
    "returns from the hospital to find her family gathered around bruised Ivan, who proudly "
    "announces that a wartime veteran cleared his grandfather's name at the TV debate. "
    "Let's listen to the scene in Russian first."
)

STORY = [
    ("nina",  "Ну, что у вас здесь за лазарет?",
     "Well, what kind of infirmary do you have here?",
     [(1070, "Ну, что у вас здесь за лазарет")], ""),
    ("nina",  "Что с тобой случилось, Ваня?",
     "What happened to you, Vanya?",
     [(1071, "Что случилось-то")], "'с тобой... Ваня' added"),
    ("anya",  "Да не надо, ничего не болит!",
     "Don't worry, nothing hurts at all!",
     [(1073, "Да не надо, ничего не"), (1073, "ничего")], "'не щиплет' -> 'не болит'"),
    ("yulya", "Мама, мы на дебатах были!",
     "Mom, we were at the debate!",
     [(1074, "Мам, мы на дебатах были")], ""),
    ("yulya", "Там всё прошло очень хорошо.",
     "Everything went really well there.",
     [(1076, "Вот, всё хорошо")], "'прошло очень' added"),
    ("anya",  "Мы больше не полицаи, Нина!",
     "We're not collaborator police anymore, Nina!",
     [(1077, "Мы больше не полицаи")], "'Нина' added"),
    ("yulya", "Правда! Папа, расскажи про ветерана.",
     "Really! Dad, tell her about the veteran.",
     [(1078, "Правда"), (1079, "Про ветерана расскажи")], "'Папа' added"),
    ("anya",  "Да, на сцене был старый ветеран.",
     "Yes, there was an old veteran on the stage.",
     [(1080, "Да, там ветеран был")], "'на сцене... старый' added"),
    ("anya",  "Он знал моего деда на войне.",
     "He knew my grandfather during the war.",
     [], "retelling context"),
    ("anya",  "Мой дед был настоящим героем!",
     "My grandfather was a real hero!",
     [], "retelling context"),
    ("anya",  "А ты где была весь вечер?",
     "And where were you all evening?",
     [(1082, "А это где было-то")], "'весь вечер' added"),
    ("nina",  "Меня в больницу срочно вызвали.",
     "They urgently called me to the hospital.",
     [(1083, "В больнице срочно вызвали")], "'Меня' added"),
    ("nina",  "С Лёшей всё теперь в порядке.",
     "Everything is fine with Lyosha now.",
     [], "hospital context"),
    ("anya",  "Ну вот видишь, всё хорошо!",
     "Well, you see, everything is fine!",
     [(1085, "все нормально")], "'Ну вот видишь' added"),
]

OPENER = "Let's walk through how the Samsonov family rejoices after the TV debate."

WALK = [
    (0, None,
     "'Well, what kind of infirmary do you have here?' Nina walks into the living room and finds Ivan with bruised cheeks."),
    (1, None,
     "'What happened to you, Vanya?' She sees cotton pads and antiseptic bottles on the table."),
    (2, None,
     "'Don't worry, nothing hurts at all!' Ivan waves a hand dismissively, trying to look tough in front of his wife."),
    (3, None,
     "'Mom, we were at the debate!' Teenage Yulya rushes forward with bright eyes."),
    (4, None,
     "'Everything went really well there.' The children are thrilled by the dramatic turn of events on live television."),
    (5, None,
     "'We're not collaborator police anymore, Nina!' Ivan proudly announces that the slander campaign against his family collapsed."),
    (6, None,
     "'Really! Dad, tell her about the veteran.' Yulya urges her father to share the dramatic moment."),
    (7, None,
     "'Yes, there was an old veteran on the stage.' An elderly partisan stood up in the audience."),
    (8, None,
     "'He knew my grandfather during the war.' The veteran swore before the cameras that Ivan's grandfather was a partisan scout."),
    (9, None,
     "'My grandfather was a real hero!' Ivan beams with pride now that his family honor is restored."),
    (10, None,
     "'And where were you all evening?' Ivan asks why Nina wasn't watching the broadcast with them."),
    (11, None,
     "'They urgently called me to the hospital.' Nina explains she had to rush to help Marina and Lyosha."),
    (12, None,
     "'Everything is fine with Lyosha now.' She shares the good news that the boy avoided surgery and can walk."),
    (13, None,
     "'Well, you see, everything is fine!' Ivan smiles, convinced all their troubles are finally over."),
]

TRANSITION = "Now let's listen to the happy family conversation in the Samsonov flat once again."

OUTRO = (
    "With Ivan's grandfather publicly vindicated as a wartime hero and Lyosha walking, Ivan "
    "believes all his family problems are solved, unaware of what Nina is about to say."
)

CLOSING = ("anya", "Мы больше не полицаи, Нина!")
