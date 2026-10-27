ID = "domashniy-arest-s01e12-scene-03"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 12
SCENE = 3
TITLE = "Стена монастыря  (The Monastery Wall)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "builder": "anja"}
LABELS = {"anya": "Профессор", "builder": "Строитель"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.12"
SOURCE_FILE = "sources/domashniy-arest/s01/e12.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 38-65. In the present day, a university history professor brings his students to the ancient surviving "
    "wall of Sineozersk monastery. A commercial developer arrives to demolish it for a new shopping mall, sparking fury."
)

INTRO = (
    "In the present day, a university history professor lectures his students before an ancient stone wall. "
    "This wall is the only surviving remnant of the medieval monastery burned down eight hundred years ago. "
    "Suddenly, a construction crew arrives with orders to tear down the historic monument to build a shopping center. "
    "Let's listen to their confrontation in Russian first."
)

STORY = [
    ("anya", "Эта стена — наш главный исторический памятник.",
     "This wall is our main historical monument.",
     [(40, "Эта стена – это настоящий памятник")], "adapted"),
    ("anya", "Она осталась от древнего монастыря.",
     "It remained from an ancient monastery.",
     [(41, "осталось от сожженного татарами монастыря")], "adapted"),
    ("anya", "Здесь была написана великая летопись.",
     "A great chronicle was written here.",
     [(39, "подлинник повести временных лет")], "adapted"),
    ("anya", "Каждый студент должен помнить историю.",
     "Every student must remember history.",
     [(42, "привожу своих студентов")], "adapted"),
    ("anya", "Что вы здесь делаете, гражданин?",
     "What are you doing here, citizen?",
     [(50, "Вы что здесь делаете")], ""),
    ("builder", "Я собираюсь сносить эту старую стену.",
     "I am going to demolish this old wall.",
     [(53, "Стену сносить буду")], "adapted"),
    ("anya", "Как вы можете разрушать историю?",
     "How can you destroy history?",
     [(56, "Как строить? Да это же")], "adapted"),
    ("builder", "Мы построим здесь большой торговый центр.",
     "We will build a big shopping center here.",
     [(55, "Торговый центр тут буду строить")], "adapted"),
    ("anya", "Это же наше национальное достояние!",
     "This is our national heritage!",
     [(57, "Это же историческое достояние")], "adapted"),
    ("builder", "У меня есть официальное разрешение на снос.",
     "I have official permission for demolition.",
     [], "new"),
    ("builder", "Все ваши вопросы задавайте в мэрию!",
     "Address all your questions to the mayor's office!",
     [(60, "все вопросы в мэрию")], "adapted"),
    ("anya", "Это настоящий произвол городских властей!",
     "This is true arbitrariness by city authorities!",
     [(64, "Беспредел")], "adapted"),
    ("anya", "Мэр города разрушает наши памятники!",
     "The city mayor is destroying our monuments!",
     [(65, "Мэр-вандал")], "adapted"),
    ("builder", "Отойдите в сторону от техники!",
     "Step aside away from the equipment!",
     [(62, "Вот идите, давайте")], "adapted"),
]

OPENER = "Now let's examine the professor and builder's dispute line by line."

WALK = [
    (0, None,
     "'This wall is our main historical monument.' The professor introduces the landmark with a demonstrative pronoun."),
    (1, None,
     "'It remained from an ancient monastery.' The historian explains its origin with a past feminine reflexive verb."),
    (2, None,
     "'A great chronicle was written here.' The professor mentions the monastery book using a short passive participle."),
    (3, None,
     "'Every student must remember history.' The speaker uses a modal short adjective with an infinitive verb."),
    (4, None,
     "'What are you doing here, citizen?' The professor addresses the newcomer with formal polite pronouns."),
    (5, None,
     "'I am going to demolish this old wall.' The contractor announces his intention using a reflexive verb."),
    (6, None,
     "'How can you destroy history?' The professor expresses shock using a modal verb with an infinitive."),
    (7, None,
     "'We will build a big shopping center here.' The builder describes the commercial project in the future tense."),
    (8, None,
     "'This is our national heritage!' The professor defends the monument with an emphatic particle and neuter noun."),
    (9, None,
     "'I have official permission for demolition.' The contractor asserts legal authority with a genitive construction."),
    (10, None,
     "'Address all your questions to the mayor's office!' The builder redirects complaints with an imperative."),
    (11, None,
     "'This is true arbitrariness by city authorities!' The professor condemns the action using an emphatic adjective."),
    (12, None,
     "'The city mayor is destroying our monuments!' The academic blames the local mayor with a present tense verb."),
    (13, None,
     "'Step aside away from the equipment!' The worker warns the crowd using a prefixed imperative verb."),
]

TRANSITION = "Now let's listen to the monastery wall confrontation again without interruption."
OUTRO = (
    "Outraged citizens protest against the demolition ordered by the mayor's administration. "
    "In the next scene, political turmoil erupts inside the mayor's team."
)
CLOSING = ("anya", "Это настоящий произвол городских властей!")
