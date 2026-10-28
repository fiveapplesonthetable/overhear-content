"""s01e13 scene 03: Пешком до работы (Walking to Work)."""

ID = "kukhnya-s01e13-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 3
TITLE = "Пешком до работы  (Walking to Work)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "max": "anja",
}
LABELS = {
    "anya": "Вика",
    "max": "Макс",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = "sources/kukhnya/s01/e13.ru.dual.srt"

INTRO = (
    "Driving to work together in the morning, Victoria pulls over a block away from Claude Monet and asks Max to walk the rest of the way on foot. "
    "Wary of workplace gossip, Victoria insists on keeping their secret relationship under wraps, while Max playfully teases her about ruining his reputation. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("anya", "Макс, останови машину возле этого угла.",
     "Max, stop the car near this corner.",
     [], "asking to stop"),
    ("max", "Почему здесь? Ресторан находится дальше.",
     "Why here? The restaurant is located further.",
     [(42, "Это почему?")], "asking why"),
    ("anya", "Давай дальше ты пойдёшь пешком.",
     "Let us have you walk the rest on foot.",
     [(41, "Давай отсюда ты дойдешь пешком.")], "suggesting walk"),
    ("max", "Ты не хочешь ехать со мной?",
     "You do not want to ride with me?",
     [], "probing motive"),
    ("anya", "Коллеги не должны видеть нас вместе.",
     "Colleagues should not see us together.",
     [(43, "если мы боимся на работе вместе.")], "explaining caution"),
    ("max", "Ты боишься глупых слухов на работе?",
     "Are you afraid of silly rumors at work?",
     [], "naming gossip"),
    ("anya", "Это вызовет лишние вопросы на кухне.",
     "This will cause unnecessary questions in the kitchen.",
     [], "fearing questions"),
    ("max", "Ты абсолютно права, дорогая.",
     "You are completely right, darling.",
     [(44, "ты права.")], "agreeing with irony"),
    ("max", "Это может испортить мою важную репутацию.",
     "This could ruin my important reputation.",
     [(44, "Это может нанести серьезный урон моей репутации.")], "teasing with bravado"),
    ("anya", "Макс, ты серьёзно так думаешь?",
     "Max, do you seriously think so?",
     [(45, "ты уверен, что все это правильно?")], "asking dryly"),
    ("max", "Я просто шучу, успокойся.",
     "I am just joking, calm down.",
     [], "reassuring her"),
    ("anya", "Тогда выходи быстрее, я спешу.",
     "Then get out faster, I am in a hurry.",
     [], "rushing departure"),
    ("max", "Хорошо, увидимся на кухне, администратор!",
     "All right, see you in the kitchen, administrator!",
     [], "waving goodbye"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "Макс, останови машину возле этого угла.",
     "'Max, stop the car near this corner.' — imperative verb governing an accusative noun and genitive location."),
    (2, "Давай дальше ты пойдёшь пешком.",
     "'Let us have you walk the rest on foot.' — hortative particle with a future motion verb and adverb of manner."),
    (4, "Коллеги не должны видеть нас вместе.",
     "'Colleagues should not see us together.' — plural modal adjective governing an infinitive and pronoun."),
    (5, "Ты боишься глупых слухов на работе?",
     "'Are you afraid of silly rumors at work?' — second person singular reflexive verb governing genitive plural."),
    (6, "Это вызовет лишние вопросы на кухне.",
     "'This will cause unnecessary questions in the kitchen.' — future perfective transitive verb with direct object."),
    (7, "Ты абсолютно права, дорогая.",
     "'You are completely right, darling.' — short feminine adjective with an intensifying degree adverb."),
    (8, "Это может испортить мою важную репутацию.",
     "'This could ruin my important reputation.' — modal verb with perfective infinitive and possessive object."),
    (10, "Я просто шучу, успокойся.",
     "'I am just joking, calm down.' — present tense imperfective verb paired with a reflexive imperative."),
    (11, "Тогда выходи быстрее, я спешу.",
     "'Then get out faster, I am in a hurry.' — imperative of motion followed by a present state verb."),
    (12, "Хорошо, увидимся на кухне, администратор!",
     "'All right, see you in the kitchen, administrator!' — conversational farewell with a playful vocational title."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around walking to work, and for the words meaning 'stop!' and 'car'. You'll catch them now. See you next time."
CLOSING = ("max", "Хорошо, увидимся на кухне, администратор!")
