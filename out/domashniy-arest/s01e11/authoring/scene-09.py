ID = "domashniy-arest-s01e11-scene-09"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 9
TITLE = "Тревога Нины  (Nina's Anxiety)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "danya": "anja"}
LABELS = {"anya": "Нина", "danya": "Даниил"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 220-243. Nina is restless and agitated in Daniil's car because Samsonov has not called her. "
    "Knowing her husband's explosive nature, she suspects something terrible must have happened to him. "
    "Calling Daniil heartless for dismissing her fears, Nina insists on going home to check on Samsonov."
)

INTRO = (
    "In this scene, Nina sits nervously with Daniil, unable to calm down. "
    "She finds Samsonov's total silence deeply suspicious, expecting him either to rage or to beg for reconciliation. "
    "Despite Daniil's attempt to brush it off, Nina fears for her husband and decides to return home immediately. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("danya", "Почему ты сегодня такая раздражённая?",
     "Why are you so irritated today?",
     [(220, "А чему такая раздраженная")], ""),
    ("anya", "Мне очень странно, что он не звонит.",
     "It is very strange to me that he does not call.",
     [(221, "Мне странно, что он не звонит")], ""),
    ("danya", "О ком именно ты сейчас говоришь?",
     "Who exactly are you talking about now?",
     [(222, "Кто")], ""),
    ("anya", "Я говорю про своего мужа Ивана.",
     "I am talking about my husband Ivan.",
     [(223, "Муж мой")], ""),
    ("danya", "И что в этом такого странного?",
     "And what is so strange about that?",
     [(224, "А чему странно")], ""),
    ("anya", "Я же очень хорошо его знаю.",
     "I know him very well after all.",
     [(226, "Я его знаю")], ""),
    ("anya", "Обычно он должен или громко кричать.",
     "Usually he should either shout loudly.",
     [(227, "Он должен или орать")], ""),
    ("anya", "Или он должен просить прощения.",
     "Or he should ask for forgiveness.",
     [(227, "или умолять")], ""),
    ("anya", "А сейчас он почему-то просто молчит.",
     "And now for some reason he is simply silent.",
     [(229, "А он молчит")], ""),
    ("danya", "Вот и хорошо, что он молчит.",
     "Well it is good that he is silent.",
     [(230, "Хорошо, что молчит")], ""),
    ("anya", "А вдруг с ним что-то случилось?",
     "What if something happened to him?",
     [(231, "А вдруг с ним случилось что-то")], ""),
    ("danya", "Да перестань говорить глупую ерунду.",
     "Stop talking foolish nonsense.",
     [(237, "Да не говори ерунды")], ""),
    ("anya", "Какой же ты всё-таки бесчувственный человек!",
     "What a heartless person you are after all!",
     [(238, "Какой ты все-таки бесчувственный")], ""),
    ("anya", "Я поеду домой и проверю его!",
     "I will go home and check on him!",
     [(239, "Я так не могу"), (240, "Поеду проверю")], ""),
]

OPENER = (
    "Now let's examine Nina's growing anxiety line by line. "
    "Nina cannot relax because of Samsonov's uncharacteristic silence."
)

WALK = [
    (0, None,
     "'Why are you so irritated today?' Daniil notices Nina's visible anxiety."),
    (1, None,
     "'It is very strange to me that he does not call.' Nina uses a dative construction with an adverb."),
    (2, None,
     "'Who exactly are you talking about now?' The prepositional question asks for clarification."),
    (3, None,
     "'I am talking about my husband Ivan.' The preposition governs an accusative object."),
    (4, None,
     "'And what is so strange about that?' Daniil questions why Samsonov's silence is unusual."),
    (5, None,
     "'I know him very well after all.' The emphatic particle underlines her long familiarity."),
    (6, None,
     "'Usually he should either shout loudly.' The modal construction expresses expected behavior."),
    (7, None,
     "'Or he should ask for forgiveness.' The alternative infinitive denotes desperate pleading."),
    (8, None,
     "'And now for some reason he is simply silent.' The present tense verb marks unexpected quiet."),
    (9, None,
     "'Well it is good that he is silent.' The impersonal predicative clause welcomes the quiet."),
    (10, None,
     "'What if something happened to him?' The conjunction introduces anxious apprehension."),
    (11, None,
     "'Stop talking foolish nonsense.' The imperative verb dismisses her worrying thoughts."),
    (12, None,
     "'What a heartless person you are after all!' Nina reproaches Daniil for his lack of empathy."),
    (13, None,
     "'I will go home and check on him!' Nina decides to investigate in person."),
]

TRANSITION = "Now let's listen to Nina and Daniil's exchange once more without pauses."
OUTRO = (
    "Worried about her husband, Nina heads back to the communal flat to investigate. "
    "In the next scene, a bitter argument breaks out inside the FSB headquarters."
)
CLOSING = ("anya", "Я поеду домой и проверю его!")
