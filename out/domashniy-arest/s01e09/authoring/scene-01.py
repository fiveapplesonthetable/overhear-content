ID = "domashniy-arest-s01e09-scene-01"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 1
TITLE = "Я не изменял тебе  (I Didn't Cheat on You)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nina": "angelina"}
LABELS = {"anya": "Самсон", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.09"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-8. Samsonov and Nina argue in bed late at night after the political concert. "
    "Samsonov insists he was faithful and threatens divorce, while Nina treats his anger as a joke. "
    "Colloquial slang 'пофиг' in cue 3 is softened to 'всё равно' for clean A1 retelling."
)

INTRO = (
    "In this opening scene of episode nine, Ivan Samsonov and his wife Nina are in bed late at night arguing about his "
    "behavior at the political concert. "
    "Furious at rumors of infidelity, Samsonov insists he did nothing wrong and angrily threatens her with divorce, while Nina "
    "laughs off his dramatic threats. "
    "Let's listen to the scene in Russian first; don't worry about catching every word."
)

STORY = [
    ("anya", "Сколько раз тебе говорить?",
     "How many times do I have to tell you?",
     [(1, "Сколько раз")], ""),
    ("anya", "Я просто сходил на концерт.",
     "I just went to a concert.",
     [(1, "я просто сходил"), (1, "на концерт")], ""),
    ("anya", "Я был там с одноклассником.",
     "I was there with a classmate.",
     [(1, "с одноклассником")], ""),
    ("anya", "Я тебе не изменял!",
     "I didn't cheat on you!",
     [(2, "Я тебя не изменял")], "corrected grammar from dialectal тебя -> тебе"),
    ("nina", "А люди говорят другое.",
     "And people say otherwise.",
     [], "added dialogue line"),
    ("anya", "Мне всё равно, что ты думаешь!",
     "I don't care what you think!",
     [(3, "Да мне"), (3, "как ты считаешь")], "slang пофиг softened to всё равно"),
    ("anya", "Ты меня поняла?",
     "Did you understand me?",
     [(3, "поняла")], ""),
    ("anya", "Я разведусь с тобой!",
     "I will divorce you!",
     [(4, "Я разведусь с тобой")], ""),
    ("anya", "Тебе всё понятно?",
     "Is everything clear to you?",
     [(4, "понятно")], ""),
    ("nina", "Самсон, ну всё, хватит.",
     "Samson, that's enough, stop it.",
     [(6, "Самсон, ну все")], ""),
    ("nina", "Не смеши меня, пожалуйста.",
     "Don't make me laugh, please.",
     [(6, "не смеши меня")], ""),
    ("nina", "Пойдём уже спать.",
     "Let's just go to sleep.",
     [(7, "Пойдем спать")], ""),
    ("anya", "Посмотрим, Нина. Посмотрим.",
     "We will see, Nina. We will see.",
     [(8, "Посмотрим")], ""),
]

OPENER = (
    "Now let's examine Ivan and Nina's midnight bedroom argument line by line. "
    "Ivan sits up in bed frowning in the dark."
)

WALK = [
    (0, None,
     "'How many times do I have to tell you?' Samsonov expresses exasperation using an infinitive construction."),
    (1, None,
     "'I just went to a concert.' The past masculine verb combines with the adverb for 'simply' or 'just'."),
    (2, None,
     "'I was there with a classmate.' Notice the instrumental case following the preposition for 'with'."),
    (3, None,
     "'I didn't cheat on you!' The verb for 'to be unfaithful' takes the dative case in standard Russian."),
    (4, None,
     "'And people say otherwise.' Nina remains skeptical about his late-night whereabouts."),
    (5, None,
     "'I don't care what you think!' The idiom with the dative pronoun literally means 'to me it is all the same'."),
    (6, None,
     "'Did you understand me?' A short past tense question checking whether she heard him."),
    (7, None,
     "'I will divorce you!' The future perfective verb indicates an intention to dissolve the marriage."),
    (8, None,
     "'Is everything clear to you?' Samsonov demands acknowledgment with the neuter predicative adjective."),
    (9, None,
     "'Samson, that's enough, stop it.' Nina dismisses his threat with a soothing particle combination."),
    (10, None,
     "'Don't make me laugh, please.' The negative imperative urges him not to act ridiculous."),
    (11, None,
     "'Let's just go to sleep.' Nina tries to defuse the midnight argument and turn off the light."),
    (12, None,
     "'We will see, Nina. We will see.' Samsonov repeats the future plural verb as a stubborn final warning."),
]

TRANSITION = "Now let's listen to the entire bedroom argument again without interruption."
OUTRO = (
    "Despite his angry divorce threats, Samsonov's bluster fails to intimidate his wife. "
    "Next the satirical opening title song sets the tone for the political chaos ahead; see you there."
)
CLOSING = ("anya", "Я разведусь с тобой!")
