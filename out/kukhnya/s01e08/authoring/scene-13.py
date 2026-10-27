"""s01e08 scene 13: Тайник на складе (Hiding Place in the Storeroom)."""

ID = "kukhnya-s01e08-scene-13"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 13
TITLE = "Тайник на складе  (Hiding Place in the Storeroom)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "sasha": "anja", "vika": "angelina"}
LABELS = {"anya": "Макс", "sasha": "Саша", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"
SOURCE_NOTE = "Cues 139-162. Max and Sasha hide Nagiyev's dog in the vegetable storeroom when Vika suddenly interrupts them."

INTRO = (
    "In the quiet vegetable storeroom of Claude Monet, Max and Sasha scramble to hide Dmitry Nagiyev's unconscious dog among sacks of potatoes. "
    "Desperate to conceal the animal until nightfall, they use fragrant cilantro before art director Victoria walks in unexpectedly. "
    "Let's listen to their nervous conversation in Russian."
)

STORY = [
    ("anya", "Вот, положи её сюда.", "Here, put her here.",
     [(139, "сюда давай")], ""),
    ("sasha", "Пусть она полежит здесь до вечера.", "Let her lie here until evening.",
     [(140, "Пусть пока до вечера здесь полежит")], ""),
    ("anya", "Мы вынесем её ночью.", "We will carry her out at night.",
     [(140, "вынесем ее")], ""),
    ("sasha", "Возьми свежую кинзу.", "Take the fresh cilantro.",
     [(141, "Так, кинза")], ""),
    ("sasha", "Она легко перебьёт любой запах.", "It will easily cover any odor.",
     [(142, "Она так пахнет, если что, запах перебьет")], ""),
    ("anya", "Помоги мне поднять этот мешок.", "Help me lift this sack.",
     [(148, "Давай помогай")], ""),
    ("sasha", "Положи собаку глубже за картошку.", "Put the dog deeper behind the potatoes.",
     [(152, "Засовывай сюда"), (153, "Глубже засовывай")], ""),
    ("vika", "А чем вы тут занимаетесь?", "And what are you doing here?",
     [(154, "А чем вы тут занимаетесь?")], ""),
    ("sasha", "Я просто ищу чистые скатерти.", "I am just looking for clean tablecloths.",
     [(156, "Я скатерти ищу")], ""),
    ("vika", "Скатерти на овощном складе?", "Tablecloths in the vegetable storeroom?",
     [(157, "скатерти на овощном складе")], ""),
    ("vika", "Макс, почему ты не на кухне?", "Max, why aren't you in the kitchen?",
     [(159, "почему не на рабочем месте")], ""),
    ("anya", "У меня сегодня законный выходной.", "I have a legitimate day off today.",
     [(160, "А у меня выходной")], ""),
    ("vika", "Быстро уходите, это вам не мотель.", "Leave quickly, this is no motel for you.",
     [(162, "заканчивайте здесь фритюриться, это вам не мотель")], ""),
]

OPENER = "Let's explore how Max and Sasha attempt to conceal their secret in the restaurant storeroom."

WALK = [
    (1, None,
     "'Let her lie here until evening.' The introductory hortative particle expresses third-person permission and resignation for the characters."),
    (4, None,
     "'It will easily cover any odor.' The future tense perfective verb demonstrates completed future action, paired with an accusative direct object."),
    (9, None,
     "'Tablecloths in the vegetable storeroom?' Victoria expresses skeptical disbelief through an elliptical question in the prepositional case."),
    (12, None,
     "'Leave quickly, this is no motel for you.' A firm imperative followed by a humorous colloquial dismissal."),
]

TRANSITION = "Now, let's listen to the storeroom conversation once more."

OUTRO = (
    "Now you know how to talk about hiding items, giving excuses, and handling unexpected workplace interruptions in Russian. "
    "Listen for these practical expressions in the upcoming scenes."
)

CLOSING = ("anya", "Нам очень повезло в этот раз.")
