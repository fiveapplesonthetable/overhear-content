"""s01e09 scene 34: Тонкий ход (The Governor's speech / Osipenko's call)."""

ID = "domashniy-arest-s01e09-scene-34"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 34
TITLE = "Тонкий ход  (The Governor's Speech)"
LEVEL = "beginner"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "viktor": "anja",
}
LABELS = {
    "anya": "Осипенко",
    "viktor": "Виктор Степанович",
}
SOURCE_NAME = "Домашний арест, Сезон 1, Эпизод 9"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"
SOURCE_NOTE = "Cues 932-940. Osipenko calls Governor Viktor Stepanovich to flatter him and thank him for outsmarting Samsonov."

INTRO = (
    "Encouraged by the surge in his poll numbers, mayoral candidate Pavel Osipenko immediately "
    "phones Governor Viktor Stepanovich. Osipenko expresses extravagant gratitude, praising the "
    "governor's cunning political maneuver that discredited Samsonov in front of the electorate."
)

STORY = [
    ("anya", "Алло, Виктор Степанович, здравствуйте!",
     "Hello, Viktor Stepanovich, good day!",
     [(932, "Алло, Виктор Степанович, здравствуйте.")], "exact cue"),

    ("viktor", "Здравствуй, Павел. Чего тебе?",
     "Hello, Pavel. What do you want?",
     [(933, "Чего тебе?")], "adapted cue"),

    ("anya", "Это был очень тонкий ход!",
     "That was a very subtle move!",
     [(934, "Очень тонкий ход.")], "adapted cue"),

    ("anya", "Я всё понял, спасибо большое.",
     "I understood everything, thank you very much.",
     [(934, "Я все понял, спасибо.")], "adapted cue"),

    ("viktor", "И это всё, что ты скажешь?",
     "And is that all you will say?",
     [(935, "И все?")], "expanded cue"),

    ("anya", "Простите меня, пожалуйста, за глупость.",
     "Please forgive me for my foolishness.",
     [(936, "Простите меня, пожалуйста.")], "expanded cue"),

    ("viktor", "И всё?",
     "And that is all?",
     [(937, "И все?")], "exact cue"),

    ("anya", "Вы гений и выдающийся ум современности!",
     "You are a genius and the greatest mind of our time!",
     [(938, "вы гений, макиявели, выдающийся ум современности.")], "adapted cue"),

    ("viktor", "Хватит, не подлизывайся слишком сильно.",
     "Enough, do not flatter too much.",
     [(939, "Не перелизывай.")], "polite adaptation of cue"),

    ("viktor", "Ладно, борись дальше за власть.",
     "Alright, keep fighting for power.",
     [(940, "Ладно, борись давай")], "adapted cue"),

    ("anya", "Я обязательно выиграю эти выборы!",
     "I will definitely win these elections!",
     [], "added promise"),

    ("viktor", "Тогда работай усердно и не расслабляйся.",
     "Then work hard and do not relax.",
     [], "added command"),

    ("anya", "Спасибо за поддержку, Виктор Степанович!",
     "Thank you for the support, Viktor Stepanovich!",
     [], "added gratitude"),
]

OPENER = "Let's explore the sycophantic phone exchange between Osipenko and the powerful governor."

WALK = [
    (0, None,
     "'Hello, Viktor Stepanovich, good day!' A formal polite greeting over a telephone call."),
    (1, None,
     "'Hello, Pavel. What do you want?' A brusque question showing the governor's impatient attitude."),
    (2, None,
     "'That was a very subtle move!' Osipenko praises the governor's covert political manipulation."),
    (3, None,
     "'I understood everything, thank you very much.' Osipenko admits he finally grasps the cunning strategy."),
    (4, None,
     "'And is that all you will say?' The governor playfully pressures him for more groveling apologies."),
    (5, None,
     "'Please forgive me for my foolishness.' An apologetic request acknowledging past lack of foresight."),
    (6, None,
     "'And that is all?' A repeated prompt demanding even more flattering subservience."),
    (7, None,
     "'You are a genius and the greatest mind of our time!' High praise describing peerless intellectual brilliance."),
    (8, None,
     "'Enough, do not flatter too much.' An imperative warning against excessively shameless flattery."),
    (9, None,
     "'Alright, keep fighting for power.' The governor gives his curt blessing to continue the race."),
    (10, None,
     "'I will definitely win these elections!' Osipenko boldly predicts his eventual electoral victory."),
    (11, None,
     "'Then work hard and do not relax.' Pragmatic advice telling the candidate to stay vigilant."),
    (12, None,
     "'Thank you for the support, Viktor Stepanovich!' A respectful closing expression of gratitude."),
]

TRANSITION = "Now let's listen to the brief strategic phone call from start to finish once more."

OUTRO = "Osipenko puts down the receiver with renewed confidence, ready to press his advantage."

CLOSING = ("anya", "Спасибо за поддержку, Виктор Степанович!")
