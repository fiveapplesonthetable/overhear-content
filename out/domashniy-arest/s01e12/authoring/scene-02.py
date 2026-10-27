ID = "domashniy-arest-s01e12-scene-02"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 12
SCENE = 2
TITLE = "Нападение на обитель  (Attack on the Monastery)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "grigory": "anja"}
LABELS = {"anya": "Константин", "grigory": "Отец Григорий"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.12"
SOURCE_FILE = "sources/domashniy-arest/s01/e12.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 29-37. Eight hundred years ago. Enemy invaders attack the monastery and set it on fire. "
    "Father Grigory orders monk Konstantin to flee and save the sacred manuscript."
)

INTRO = (
    "Suddenly, alarms echo through the monastery courtyard as enemy invaders break through the gates. "
    "Monk Konstantin urges Father Grigory to flee, but Father Grigory knows time has run out. "
    "He orders Konstantin to take the precious handwritten chronicle and hide it safely in the cellar. "
    "Let's listen to their tense exchange in Russian first."
)

STORY = [
    ("anya", "Господи, Иисусе Христе, спаси нас!",
     "Lord Jesus Christ, save us!",
     [(29, "Господи, судьи Христи")], "adapted"),
    ("anya", "Отец Григорий, нам надо бежать!",
     "Father Grigory, we must run!",
     [(30, "Бежим, отец Григорий, бежим")], ""),
    ("grigory", "Куда же нам теперь бежать?",
     "Where can we run now?",
     [(31, "Куда игра")], "adapted"),
    ("anya", "Враги уже ворвались в монастырь!",
     "The enemies have already broken into the monastery!",
     [], "new"),
    ("grigory", "Мы уже никуда не убежим.",
     "We won't escape anywhere now.",
     [(34, "Не уйдем мы")], "adapted"),
    ("anya", "Они поджигают наши деревянные стены!",
     "They are setting our wooden walls on fire!",
     [(41, "сожженного татарами монастыря")], "adapted"),
    ("grigory", "Спасай скорее священную книгу!",
     "Save the sacred book quickly!",
     [(35, "Иди, прячь книгу")], "adapted"),
    ("anya", "А как же вы, отец Григорий?",
     "And what about you, Father Grigory?",
     [(36, "А как же, отец Григорий")], ""),
    ("grigory", "Обо мне не думай сейчас.",
     "Don't think about me right now.",
     [], "new"),
    ("grigory", "Иди немедленно и прячь летопись!",
     "Go immediately and hide the chronicle!",
     [(37, "Иди, говорю")], "adapted"),
    ("anya", "Я спрячу её в каменном подвале!",
     "I will hide it in the stone cellar!",
     [], "new"),
    ("grigory", "Сохрани память для наших потомков!",
     "Preserve the memory for our descendants!",
     [(38, "А мы тут помним былое")], "adapted"),
    ("anya", "Я сберегу эту книгу навсегда!",
     "I will save this book forever!",
     [], "new"),
]

OPENER = "Now let's examine Father Grigory and Konstantin's escape conversation line by line."

WALK = [
    (0, None,
     "'Lord Jesus Christ, save us!' Konstantin cries out in terror with a traditional religious invocation."),
    (1, None,
     "'Father Grigory, we must run!' The monk urges immediate flight using a modal predicative with an infinitive."),
    (2, None,
     "'Where can we run now?' Father Grigory questions their chances using an interrogative adverb of direction."),
    (3, None,
     "'The enemies have already broken into the monastery!' Konstantin reports the breach using a perfective plural verb."),
    (4, None,
     "'We won't escape anywhere now.' Father Grigory recognizes the danger with a negative adverb and future verb."),
    (5, None,
     "'They are setting our wooden walls on fire!' Konstantin describes the fire using a present tense transitive verb."),
    (6, None,
     "'Save the sacred book quickly!' The elder gives a crucial command using an imperative verb."),
    (7, None,
     "'And what about you, Father Grigory?' Konstantin worries about his mentor with a conversational questioning particle."),
    (8, None,
     "'Don't think about me right now.' Father Grigory dismisses concern for himself using a negative imperative."),
    (9, None,
     "'Go immediately and hide the chronicle!' The elder insists on hiding the manuscript with paired imperatives."),
    (10, None,
     "'I will hide it in the stone cellar!' Konstantin vows to conceal the relic with a future perfective verb."),
    (11, None,
     "'Preserve the memory for our descendants!' Father Grigory emphasizes historical legacy with an imperative."),
    (12, None,
     "'I will save this book forever!' Konstantin makes a solemn promise using a future perfective verb."),
]

TRANSITION = "Now let's listen to the monastery attack scene again without interruption."
OUTRO = (
    "Konstantin runs to hide the priceless chronicle deep underground. "
    "In the next scene, modern citizens stand beside the sole surviving wall of that ancient monastery."
)
CLOSING = ("anya", "Я сберегу эту книгу навсегда!")
