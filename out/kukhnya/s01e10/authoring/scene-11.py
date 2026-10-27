"""s01e10 scene 11: Вопрос у барной стойки (A Question at the Bar)."""

ID = "kukhnya-s01e10-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 11
TITLE = "Вопрос у барной стойки  (A Question at the Bar)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Вика", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = "Cue 87. Victoria approaches bartender Kostya at the bar counter to check on drink service and question Max's hurried departure."

INTRO = (
    "In the dining room near the bar counter, art director Victoria notices bartender Kostya finishing up his drink preparations. "
    "Having watched Max quickly slip away from the bar area, Victoria approaches Kostya to check if everything is ready and see what is going on. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Костя, ты закончил готовить напитки?",
     "Kostya, have you finished preparing the drinks?",
     [(87, "Все")], "checking on beverage orders"),
    ("kostya", "Да, все заказы уже готовы.",
     "Yes, all orders are already ready.",
     [(79, "Все, можешь забирать")], "confirming drink completion"),
    ("anya", "Почему Макс так быстро убежал отсюда?",
     "Why did Max run away from here so quickly?",
     [], "asking about his departure"),
    ("kostya", "Он просто очень спешил на кухню.",
     "He was simply in a big hurry to get to the kitchen.",
     [(81, "Сейчас надо поделать")], "offering a simple reason"),
    ("anya", "Мне кажется, он странно себя ведёт.",
     "It seems to me that he is behaving strangely.",
     [], "expressing intuition about Max"),
    ("kostya", "Макс всегда немного странный парень.",
     "Max is always a slightly strange guy.",
     [], "downplaying the observation"),
    ("anya", "Он ничего не говорил тебе обо мне?",
     "Did he not say anything to you about me?",
     [], "probing for private comments"),
    ("kostya", "Мы говорили только о нашей работе.",
     "We spoke only about our work.",
     [(85, "Давай попозже поговорим")], "insisting on professional topics"),
    ("anya", "Ты точно говоришь мне чистую правду?",
     "Are you definitely telling me the pure truth?",
     [], "questioning his honesty"),
    ("kostya", "Конечно, я никогда тебя не обманываю.",
     "Of course, I never deceive you.",
     [], "reassuring the director"),
    ("anya", "Хорошо, тогда я спрошу его сама.",
     "Fine, then I will ask him myself.",
     [], "deciding to investigate directly"),
    ("kostya", "Лучше сейчас не трогать его, Вика.",
     "It is better not to disturb him right now, Vika.",
     [], "advising caution"),
]

OPENER = "Let's examine the conversation between Victoria and the bartender at the counter line by line."

WALK = [
    (0, None,
     "'Kostya, have you finished preparing the drinks?' Victoria checks on beverage service with a past tense perfective verb."),
    (1, None,
     "'Yes, all orders are already ready.' Kostya confirms readiness using a plural subject and a short form adjective."),
    (2, None,
     "'Why did Max run away from here so quickly?' Victoria investigates Max's hasty exit with an interrogative adverb."),
    (3, None,
     "'He was simply in a big hurry to get to the kitchen.' Kostya explains the rush using an imperfective past verb."),
    (4, None,
     "'It seems to me that he is behaving strangely.' Victoria states her suspicion using an impersonal reflexive construction."),
    (5, None,
     "'Max is always a slightly strange guy.' Kostya deflects concern by characterizing his friend with an adjective and a noun."),
    (6, None,
     "'Did he not say anything to you about me?' Victoria asks directly using a negative pronoun and a prepositional phrase."),
    (7, None,
     "'We spoke only about our work.' The bartender maintains loyalty using a limiting particle and an imperfective verb."),
    (8, None,
     "'Are you definitely telling me the pure truth?' Victoria tests his sincerity with a descriptive accusative phrase."),
    (9, None,
     "'Of course, I never deceive you.' Kostya offers an emphatic denial with a negative adverb and a present tense verb."),
    (10, None,
     "'Fine, then I will ask him myself.' Victoria decides on direct action using a future tense verb and an emphatic pronoun."),
    (11, None,
     "'It is better not to disturb him right now, Vika.' Kostya suggests leaving Max alone with a comparative predicative."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Now you know how to talk about finished tasks, suspicious behavior, and honest answers in Russian. "
    "See you next time!"
)

CLOSING = ("kostya", "Лучше сейчас не трогать его, Вика.")
