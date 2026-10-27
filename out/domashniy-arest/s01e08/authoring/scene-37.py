"""Scene 37 — Ivan in Woods (s01e08, 00:50:15–00:51:09)."""

ID = "domashniy-arest-s01e08-scene-37"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 37
TITLE = "Иван в лесу  (Ivan in Woods)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.08"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 835-850. Arkady is absent -> anya = Иван (alisa), voice = Голос (anja). "
    "Drunk hallucinations and colloquial slang adapted to clean A1 Russian."
)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "voice": "anja",
}

LABELS = {
    "anya": "Иван",
    "voice": "Голос",
}

INTRO = (
    "In the snowy pine forest on the edge of town that afternoon. Shaken by the smear campaign "
    "alleging his grandfather was a fascist collaborator, Ivan wandered into the woods alone. "
    "Intoxicated and distressed, he begins hallucinating and arguing with disembodied voices "
    "in the trees before staggering back home. Let's listen to the scene in Russian first."
)

STORY = [
    ("voice", "Иван, перестань винить себя во всём!",
     "Ivan, stop blaming yourself for everything!",
     [(835, "себя грызть. Ты ни в чем не виноват")],
     "'себя грызть' -> 'перестань винить себя' for clean A1"),
    ("anya",  "Ты ничего не понимаешь!",
     "You don't understand anything!",
     [(836, "Ты что, этого не понимаешь"), (837, "Да ты не понимаешь")], ""),
    ("anya",  "Я предатель и внук фашиста!",
     "I am a traitor and the grandson of a fascist!",
     [(838, "Я фашист, полицай")], "'полицай' -> 'предатель и внук фашиста'"),
    ("voice", "Это неправда! У тебя сегодня важные дебаты.",
     "That is not true! You have an important debate today.",
     [(841, "У тебя там дебаты")], ""),
    ("anya",  "В моих генах живёт зло.",
     "Evil lives in my genes.",
     [(839, "У меня гены")], ""),
    ("anya",  "Здесь в снегу сидят крокодилы!",
     "Here in the snow sit crocodiles!",
     [(840, "тут крокодилы")], ""),
    ("voice", "Пойдём скорее на телевизионную студию!",
     "Let's go quickly to the television studio!",
     [(842, "Пошли")], ""),
    ("anya",  "Стоять! Кто стреляет в лесу?",
     "Freeze! Who is shooting in the forest?",
     [(843, "Стоять"), (845, "стрелер")], ""),
    ("anya",  "Оставьте меня в покое!",
     "Leave me alone!",
     [(847, "Да пошли вы все лесом")], "idiomatic 'лесом' -> clean 'в покое'"),
    ("voice", "Посмотри вокруг, здесь никого нет.",
     "Look around, there is no one here.",
     [(848, "Ух ты")], ""),
    ("anya",  "У меня разбита губа и болит голова.",
     "My lip is cut and my head hurts.",
     [(849, "Что с губой")], ""),
    ("anya",  "Я иду спать на чердак.",
     "I am going to sleep in the attic.",
     [(850, "папаша на чердаке")], ""),
    ("anya",  "Передайте Нине, что я дома.",
     "Tell Nina that I am at home.",
     [(850, "Маме вашей передайте")], ""),
]

OPENER = "Let's go through the scene line by line. First, an imaginary voice echoes through the snowy trees."

WALK = [
    (0, None,
     "'Ivan, stop blaming yourself for everything!' The opening imperative command expresses an urgent plea to cease self-blame."),
    (1, None,
     "'You don't understand anything!' In Russian, double negative structures are standard and grammatically required."),
    (2, None,
     "'I am a traitor and the grandson of a fascist!' Ivan repeats the painful slander broadcast by his political opponents."),
    (3, None,
     "'That is not true! You have an important debate today.' The internal voice reminds him of his public campaign duties."),
    (4, None,
     "'Evil lives in my genes.' In his intoxicated state, Ivan believes his moral flaws were inherited from his grandfather."),
    (5, None,
     "'Here in the snow sit crocodiles!' Cold air and heavy drinking cause Ivan to hallucinate wild animals among the trees."),
    (6, None,
     "'Let's go quickly to the television studio!' The urgent phrase pushes him toward the critical live broadcast."),
    (7, None,
     "'Freeze! Who is shooting in the forest?' In his delirium, Ivan imagines wartime enemies lurking behind the snowy pines."),
    (8, None,
     "'Leave me alone!' Ivan uses an idiom meaning to go away into the woods and leave him in peace."),
    (9, None,
     "'Look around, there is no one here.' The hallucination fades as Ivan realizes the quiet forest is completely empty."),
    (10, None,
     "'My lip is cut and my head hurts.' Physical discomfort pulls him back toward cold reality."),
    (11, None,
     "'I am going to sleep in the attic.' Ivan chooses the dusty communal attic as a hiding place from shame."),
    (12, None,
     "'Tell Nina that I am at home.' Even in despair, he thinks of his estranged wife waiting in the apartment."),
]

TRANSITION = "Now let's hear the whole scene once more, from start to finish."
OUTRO = (
    "Next time, Arkady races to the municipal hospital to prevent Lyoshka's surgery before "
    "it is too late. Well done following this poignant monologue in Russian. See you in the next scene."
)
CLOSING = ("anya", "Я иду спать на чердак.")
