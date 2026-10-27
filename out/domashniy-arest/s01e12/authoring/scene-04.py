ID = "domashniy-arest-s01e12-scene-04"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 12
SCENE = 4
TITLE = "Утечка из кабинета  (Leak from the Office)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Паша", "vika": "Вика"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.12"
SOURCE_FILE = "sources/domashniy-arest/s01/e12.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 74-90. Leaked secret surveillance footage from the mayor's office goes viral online. "
    "Pavel realizes his forgotten hidden camera caused the scandal, while Vika packs her bags to leave him."
)

INTRO = (
    "Local television broadcasts shocking leaked footage recorded by a hidden camera inside the mayor's office. "
    "Pavel panics upon realizing that he installed the secret camera himself a year ago to catch office thieves. "
    "Seeing that the political campaign is ruined and the public is laughing at them, Vika packs her bags to abandon him. "
    "Let's listen to their panicked argument in Russian first."
)

STORY = [
    ("anya", "В новостях снова говорят про выборы.",
     "The news is talking about the elections again.",
     [(74, "Выборная эпопея в Синеозерске продолжается")], "adapted"),
    ("anya", "Кто-то опубликовал секретное видео в интернете!",
     "Someone published a secret video on the internet!",
     [(75, "Опубликованные сегодня кадры с камер наблюдения")], "adapted"),
    ("vika", "Это же кадры из твоего кабинета!",
     "These are clips from your office!",
     [(75, "в кабинете мэра")], "adapted"),
    ("anya", "Я совсем забыл про скрытую камеру.",
     "I completely forgot about the hidden camera.",
     [(80, "Я забыл совсем, что у меня там камера")], "adapted"),
    ("vika", "Зачем ты вообще её туда поставил?",
     "Why did you put it there in the first place?",
     [(81, "Ее год назад поставил")], "adapted"),
    ("anya", "Я хотел поймать воров на работе.",
     "I wanted to catch thieves at work.",
     [(81, "чтобы узнать, кто мне какая ворует")], "adapted"),
    ("vika", "Теперь над нами смеётся весь город!",
     "Now the whole city is laughing at us!",
     [(77, "повеселили пользователей интернета")], "adapted"),
    ("anya", "Нам нужно срочно что-то придумать.",
     "We need to come up with something urgently.",
     [(83, "Надо что-то делать")], "adapted"),
    ("vika", "Здесь больше нечего ловить, Паша.",
     "There is nothing left to gain here, Pasha.",
     [(88, "Больше здесь ловить нечего")], ""),
    ("anya", "Вика, куда ты сейчас собираешься?",
     "Vika, where are you going right now?",
     [(87, "А ты куда собралась-то")], ""),
    ("vika", "Я собираю свои вещи и ухожу.",
     "I am packing my things and leaving.",
     [(89, "Уйди")], "adapted"),
    ("anya", "Пожалуйста, не бросай меня одного!",
     "Please don't abandon me alone!",
     [], "new"),
    ("vika", "Твоя политическая карьера уже закончилась.",
     "Your political career is already over.",
     [], "new"),
]

OPENER = "Now let's examine Pavel and Vika's office dispute line by line."

WALK = [
    (0, None,
     "'The news is talking about the elections again.' Pavel notices the media broadcast using an impersonal third-person verb."),
    (1, None,
     "'Someone published a secret video on the internet!' Pavel announces the leak with an indefinite pronoun."),
    (2, None,
     "'These are clips from your office!' Vika identifies the location using the genitive case of a possessive pronoun."),
    (3, None,
     "'I completely forgot about the hidden camera.' Pavel admits his blunder with an intensifying adverb and past verb."),
    (4, None,
     "'Why did you put it there in the first place?' Vika questions his logic using a past masculine transitive verb."),
    (5, None,
     "'I wanted to catch thieves at work.' Pavel explains his original motive with a modal past verb and infinitive."),
    (6, None,
     "'Now the whole city is laughing at us!' Vika laments the humiliation using a reflexive verb with a prepositional phrase."),
    (7, None,
     "'We need to come up with something urgently.' Pavel seeks a rapid solution with a predicative and infinitive."),
    (8, None,
     "'There is nothing left to gain here, Pasha.' Vika uses a common Russian idiom meaning no prospects remain."),
    (9, None,
     "'Vika, where are you going right now?' Pavel asks anxiously using a reflexive present tense verb."),
    (10, None,
     "'I am packing my things and leaving.' Vika declares her departure with paired first-person present verbs."),
    (11, None,
     "'Please don't abandon me alone!' Pavel pleads desperately with an imperative verb and polite particle."),
    (12, None,
     "'Your political career is already over.' Vika delivers a ruthless final assessment using a past reflexive verb."),
]

TRANSITION = "Now let's listen to Pavel and Vika's quarrel again without interruption."
OUTRO = (
    "Vika leaves Pavel to deal with the public relations disaster by himself. "
    "In the next scene, Samson comforts Nina in their communal apartment."
)
CLOSING = ("vika", "Твоя политическая карьера уже закончилась.")
