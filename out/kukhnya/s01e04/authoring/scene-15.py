ID = "kukhnya-s01e04-scene-15"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 15
TITLE = "Обед для персонала  (Staff Lunch)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (The Kitchen) S1.4"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"

INTRO = (
    "In Chef Barinov's office, the head chef corners young cook Max Lavrov to check if the staff lunch has been prepared. "
    "Caught lying by the polygraph results, Max tries flattery by declaring the chef is like a father to him, before being ordered back to the kitchen. "
    "Let's listen to their conversation in Russian."
)

STORY = [
    ("chef", "Лавров, подойди сюда прямо сейчас.",
     "Lavrov, come here right now.",
     [(180, "соседний ресторан")], "calling him"),
    ("anya", "Шеф, я могу уже идти на кухню?",
     "Chef, can I already go to the kitchen?",
     [(188, "я могу идти")], "asking permission"),
    ("chef", "Подожди! Ты приготовил обед для поваров?",
     "Wait! Did you cook lunch for the cooks?",
     [(190, "ты обед приготовил")], "demanding check"),
    ("anya", "Да, конечно, я всё уже сделал.",
     "Yes, of course, I already made everything.",
     [(191, "Да")], "claiming done"),
    ("chef", "Точно всё готово? Ты не обманываешь меня?",
     "Is everything definitely ready? You aren't deceiving me?",
     [(193, "мне врешь")], "skeptical"),
    ("anya", "Ну, почти приготовил, осталось совсем немного.",
     "Well, almost cooked, very little is left.",
     [(192, "Почти приготовил")], "backtracking"),
    ("chef", "Ты опять врёшь мне в лицо!",
     "You are lying to my face again!",
     [(193, "мне врешь")], "accusing"),
    ("anya", "Шеф, я никогда не вру вам.",
     "Chef, I never lie to you.",
     [(195, "никогда не обману")], "protesting innocence"),
    ("chef", "Детектор лжи показывает совсем другое!",
     "The lie detector shows something completely different!",
     [(196, "полюбуйтесь")], "pointing to device"),
    ("anya", "Эта глупая машина просто сломалась.",
     "This stupid machine simply broke.",
     [(194, "да что")], "excusing"),
    ("anya", "Шеф, вы для меня как родной отец.",
     "Chef, you are like my own father to me.",
     [(197, "вы для меня"), (198, "Как отец")], "flattering"),
    ("chef", "Быстро беги на кухню и корми людей!",
     "Quickly run to the kitchen and feed people!",
     [(189, "Вали отсюда")], "ordering away"),
    ("anya", "Слушаюсь, шеф, я сделаю всё моментально.",
     "Understood, chef, I will do everything instantly.",
     [(195, "не обману")], "hastening away"),
]

OPENER = (
    "Let's examine the dialogue sentence by sentence. "
    "Notice the workplace confrontations, kitchen idioms, and comic excuses."
)

WALK = [
    (0, "Лавров, подойди сюда прямо сейчас.",
     "'Lavrov, come here right now.' Direct address with perfective imperative and reinforced temporal adverb."),
    (1, "Шеф, я могу уже идти на кухню?",
     "'Chef, can I already go to the kitchen?' Modal question with directional prepositional phrase."),
    (2, "Подожди! Ты приготовил обед для поваров?",
     "'Wait! Did you cook lunch for the cooks?' Imperative followed by past transitive question with prepositional recipient."),
    (3, "Да, конечно, я всё уже сделал.",
     "'Yes, of course, I already made everything.' Affirmative assertion with generalized neuter pronoun and past perfective verb."),
    (4, "Точно всё готово? Ты не обманываешь меня?",
     "'Is everything definitely ready? You aren't deceiving me?' Emphatic question with short neuter adjective and negated present transitive verb."),
    (5, "Ну, почти приготовил, осталось совсем немного.",
     "'Well, almost cooked, very little is left.' Conversational qualification with past intransitive verb and quantitative neuter adverb."),
    (6, "Ты опять врёшь мне в лицо!",
     "'You are lying to my face again!' Accusatory present verb governing dative pronoun and idiomatic prepositional phrase."),
    (7, "Шеф, я никогда не вру вам.",
     "'Chef, I never lie to you.' Polite address with negative temporal adverb governing negated present verb and formal dative pronoun."),
    (8, "Детектор лжи показывает совсем другое!",
     "'The lie detector shows something completely different!' Compound subject noun phrase with present verb governing generalized substantive adjective."),
    (9, "Эта глупая машина просто сломалась.",
     "'This stupid machine simply broke.' Demonstrative feminine subject with qualitative adjective and past reflexive verb."),
    (10, "Шеф, вы для меня как родной отец.",
     "'Chef, you are like my own father to me.' Emotional vocative address with prepositional relationship and comparative family idiom."),
    (11, "Быстро беги на кухню и корми людей!",
     "'Quickly run to the kitchen and feed people!' Manner adverb with coordinated imperatives governing directional and direct object complements."),
    (12, "Слушаюсь, шеф, я сделаю всё моментально.",
     "'Understood, chef, I will do everything instantly.' Formal military formula of obedience with future perfective verb and rapid manner adverb."),
]

TRANSITION = "Now let's listen to the entire exchange one more time at normal speed."

OUTRO = (
    "Max narrowly escapes Chef Barinov's wrath and sprints back to the stoves to finish cooking staff lunch. "
    "Great work practicing lively conversational Russian!"
)

CLOSING = ("anya", "Слушаюсь, шеф, я сделаю всё моментально.")
