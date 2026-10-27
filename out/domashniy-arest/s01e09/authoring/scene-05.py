ID = "domashniy-arest-s01e09-scene-05"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 5
TITLE = "По-мужски секунд десять  (Like a Real Man for Ten Seconds)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "arkady": "anja"}
LABELS = {"anya": "Самсон", "arkady": "Аркадий"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.09"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 149-160. Humiliated by Nina's mockery in front of the kids, Samsonov runs back to Arkady for advice. "
    "Arkady coaches him on how to deliver a silent, heavy 10-second masculine stare. "
    "Mild filler 'блин' in cue 152 and garbled ASR 'концы хозов' (в конце концов) in cue 153 are cleaned up."
)

INTRO = (
    "In our last scene, Nina turned Samsonov's suitcase drama into a hilarious comedy in front of their children. "
    "Stung by her ridicule, Samsonov runs straight back to Arkady's room demanding a tougher tactic to command respect, "
    "prompting Arkady to coach him in the silent psychological art of the ten-second stare. "
    "Let's listen to the scene in Russian first; don't worry about catching every word."
)

STORY = [
    ("anya", "Аркадий, ты ничего не понимаешь!",
     "Arkady, you don't understand anything!",
     [(149, "ты не понимаешь")], ""),
    ("anya", "Она просто унижает меня перед детьми!",
     "She is simply humiliating me in front of the children!",
     [(150, "Она меня просто унижает перед детьми")], ""),
    ("arkady", "Ну ты терпи. Не реагируй.",
     "Well, bear it. Don't react.",
     [(151, "ты терпи, не реагируй")], ""),
    ("anya", "Легко сказать, не реагируй!",
     "Easy to say, don't react!",
     [(152, "Не реагируй")], ""),
    ("anya", "Я мужчина или нет, в конце концов?",
     "Am I a man or not, after all?",
     [(153, "Я мужик или не мужик")], "garble 'концы хозов' -> 'в конце концов'"),
    ("anya", "Что я должен ей ответить?",
     "What should I answer her?",
     [(154, "должен ей сказать, ответить")], ""),
    ("arkady", "Ничего не говори. Посмотри на неё.",
     "Don't say anything. Look at her.",
     [(155, "Посмотри на нее")], ""),
    ("anya", "Как посмотреть? Объясни мне.",
     "Look how? Explain to me.",
     [(156, "Как")], ""),
    ("arkady", "Посмотри тяжело, пристально.",
     "Look heavily, intensely.",
     [(155, "пристально"), (157, "Тяжело")], ""),
    ("arkady", "По-мужски, секунд десять.",
     "Like a real man, for about ten seconds.",
     [(158, "По-мужски секунд десять")], ""),
    ("arkady", "Можешь даже в уме посчитать.",
     "You can even count in your head.",
     [(159, "Можешь даже в уме посчитать")], ""),
    ("anya", "Хорошо. Я всё понял!",
     "Alright. I understood everything!",
     [(160, "Хорошо, понял")], ""),
]

OPENER = (
    "Now let's examine Arkady's hilarious advice on male dominance line by line. "
    "Samsonov stands flustered by Arkady's bed while Arkady coaches him."
)

WALK = [
    (0, None,
     "'Arkady, you don't understand anything!' Samsonov vents his frustration at Arkady's failed advice."),
    (1, None,
     "'She is simply humiliating me in front of the children!' The verb describes being belittled before his family."),
    (2, None,
     "'Well, bear it. Don't react.' Arkady advises patience with two short imperative verbs."),
    (3, None,
     "'Easy to say, don't react!' An infinitive expression meaning 'it is easy to say'."),
    (4, None,
     "'Am I a man or not, after all?' The idiom means 'in the end' or 'after all'."),
    (5, None,
     "'What should I answer her?' Samsonov asks for concrete words to restore his dignity."),
    (6, None,
     "'Don't say anything. Look at her.' Arkady recommends maintaining complete silence."),
    (7, None,
     "'Look how? Explain to me.' Samsonov asks for specific technical instructions."),
    (8, None,
     "'Look heavily, intensely.' Two adverbs describing a stern, unblinking glare."),
    (9, None,
     "'Like a real man, for about ten seconds.' Notice the inverted numeral order indicating an approximate duration."),
    (10, None,
     "'You can even count in your head.' The prepositional phrase literally means 'in the mind'."),
    (11, None,
     "'Alright. I understood everything!' Samsonov heads back to execute the stare."),
]

TRANSITION = "Now let's listen to the coaching session again without interruption."
OUTRO = (
    "Armed with the ten-second stare, Samsonov marches back into the kitchen to confront Nina. "
    "Next we'll see whether Arkady's masculine glare actually works on his wife; see you there."
)
CLOSING = ("arkady", "По-мужски, секунд десять.")
