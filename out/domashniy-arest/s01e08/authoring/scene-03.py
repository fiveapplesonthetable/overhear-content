ID = "domashniy-arest-s01e08-scene-03"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 3
TITLE = "Куда пропал кандидат?  (Where Did the Candidate Go?)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "ilona": "angelina", "slavik": "anja"}
LABELS = {"anya": "Нина", "ilona": "Илона", "slavik": "Славик"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.08"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 47-61. Nina, Ilona, and young Slavik search frantically for candidate Ivan Samsonov after the smear video airs. "
    "ASR slips in cues 50 ('Морги его нет' -> 'В морге его нет'), 58 ('Лона' -> 'Илона'), and 59 ('Треть шутки' -> "
    "'Кроме шуток') are restored to grammatical Russian. Mild colloquialism 'блин' in cue 51 is omitted."
)

INTRO = (
    "In our last scene, acting mayor Pasha Osipenko recorded a smear video branding candidate Ivan Samsonov the grandson "
    "of a wartime collaborator. "
    "Now back at the communal apartment, Nina, campaign manager Ilona, and young Slavik realise that Samsonov has gone "
    "missing on the very eve of the decisive mayoral debates. "
    "Let's hear the scene in Russian first; don't worry about catching every word."
)

STORY = [
    ("anya", "Славик, выключи телевизор, пожалуйста!",
     "Slavik, turn off the television, please!",
     [(47, "Слав, да выключишь")], ""),
    ("slavik", "Да, мама. Я выключил.",
     "Yes, Mama. I turned it off.",
     [(48, "Да")], ""),
    ("anya", "Я позвонила в больницы. В морге его нет.",
     "I called the hospitals. He is not in the morgue.",
     [(49, "Спасибо"), (50, "Морги его нет")], "cue 50 restored to 'В морге его нет'"),
    ("ilona", "В каком смысле его нет?",
     "In what sense is he not there?",
     [(52, "В смысле")], ""),
    ("anya", "В том смысле, что его нигде нет!",
     "In the sense that he is nowhere to be found!",
     [(53, "В смысле, что его нигде нет")], ""),
    ("ilona", "Ну и что теперь делать?",
     "Well, and what are we to do now?",
     [(54, "Ну и что")], "'теперь делать' added"),
    ("anya", "Я не знаю, где он сейчас.",
     "I don't know where he is right now.",
     [(55, "Я не знаю, где он")], ""),
    ("ilona", "А в каких местах он обычно пьёт?",
     "And in what places does he usually drink?",
     [(56, "А в каких местах он обычно пьет")], ""),
    ("anya", "Я везде уже была!",
     "I have already been everywhere!",
     [(57, "Везде была")], ""),
    ("slavik", "Мама, надо звонить в полицию!",
     "Mama, we need to call the police!",
     [(58, "надо звонить в полицию")], ""),
    ("slavik", "Я серьёзно говорю, кроме шуток!",
     "I am speaking seriously, no joking!",
     [(59, "шутки")], "cue 59 garbled 'Треть шутки' -> 'кроме шуток'"),
    ("ilona", "Нет, в полицию нам звонить нельзя.",
     "No, we must not call the police.",
     [(60, "Нет, туда нам сейчас не надо")], ""),
    ("ilona", "Если кандидат в полиции, кампания проиграна!",
     "If the candidate is in the police station, the campaign is lost!",
     [], "added for context on campaign stakes"),
    ("anya", "Подождём ещё немного. Он должен вернуться!",
     "Let's wait a little longer. He must return!",
     [(61, "Подождем еще немного")], "'Он должен вернуться' added"),
]

OPENER = (
    "Now let's follow the frantic search for Samsonov line by line. "
    "Nina hangs up the kitchen telephone with a trembling hand."
)

WALK = [
    (0, None,
     "'Slavik, turn off the television, please!' Nina tells her son to shut off the embarrassing campaign broadcast."),
    (1, None,
     "'Yes, Mama. I turned it off.' Slavik answers obediently with a past masculine perfective verb."),
    (2, None,
     "'I called the hospitals. He is not in the morgue.' Nina lists the grim places she has already phoned."),
    (3, None,
     "'In what sense is he not there?' Ilona asks in surprise, using the prepositional case with 'sense'."),
    (4, None,
     "'In the sense that he is nowhere to be found!' The negative adverb means 'nowhere' for location."),
    (5, None,
     "'Well, and what are we to do now?' An infinitive question expressing helplessness."),
    (6, None,
     "'I don't know where he is right now.' Nina admits she has run out of ideas."),
    (7, None,
     "'And in what places does he usually drink?' Ilona tries to guess where a working-class man might drown his sorrows."),
    (8, None,
     "'I have already been everywhere!' The adverb means 'everywhere'."),
    (9, None,
     "'Mama, we need to call the police!' Slavik suggests calling law enforcement."),
    (10, None,
     "'I am speaking seriously, no joking!' The idiom with the preposition for 'besides' means 'all joking aside'."),
    (11, None,
     "'No, we must not call the police.' Ilona immediately vetos the idea with the adverb for 'prohibited'."),
    (12, None,
     "'If the candidate is in the police station, the campaign is lost!' The short passive participle marks the election effort as finished."),
    (13, None,
     "'Let's wait a little longer. He must return!' Nina hopes her husband will come to his senses soon."),
]

TRANSITION = "Now let's listen to the scene in the communal flat again without interruption."
OUTRO = (
    "While Samsonov wanders the town in despair, life in the communal flat goes on. "
    "Next we'll follow Marina and her son Lyosha to the clinic for a consultation about his surgery; see you there."
)
CLOSING = ("anya", "Подождём ещё немного. Он должен вернуться!")
