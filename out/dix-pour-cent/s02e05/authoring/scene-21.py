# Authoring module for dix-pour-cent s02e05 scene 21 (cues 643-674).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e05/authoring/scene-21.py --out out/dix-pour-cent/s02e05/scene-21.json

ID = "dix-pour-cent-s02e05-scene-21"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 21
TITLE = "Je suis enceinte  (I'm Pregnant)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo"}
LABELS = {"lea": "Andréa", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 643-674. Andréa catches up to Hicham during his morning jog to tell him that she is pregnant "
    "with his child and asks for a few minutes to talk before his flight to London."
)

INTRO = (
    "On a quiet Parisian street, Andrea intercepts Hicham during his morning jog to deliver shocking news. "
    "Hesitant to meet casually, she reveals that she is pregnant with his child and needs to talk. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("hicham", "Qu'est-ce que tu fais là, Andréa?",
     "What are you doing here, Andrea?",
     [(643, "Qu'est-ce que tu fais là ? Tu m'attendais ?")], ""),
    ("lea", "Attends juste une petite minute.",
     "Wait just one little minute.",
     [(645, "-Wait."), (646, "Juste une minute.")], ""),
    ("hicham", "Je fais mon dernier tour.",
     "I am doing my last lap.",
     [(645, "-C'est mon dernier tour.")], ""),
    ("lea", "Je dois te demander quelque chose.",
     "I must ask you something.",
     [(647, "Je veux te demander quelque chose.")], ""),
    ("hicham", "On peut boire un verre ensemble?",
     "Can we have a drink together?",
     [(649, "Un verre. Quand tu veux.")], ""),
    ("lea", "Pourquoi est-ce qu'on se verrait?",
     "Why should we see each other?",
     [(653, "Pourquoi est-ce qu'on se retrouverait ?")], ""),
    ("hicham", "Pour parler calmement, c'est tout.",
     "To talk calmly, that is all.",
     [(654, "Pour parler. C'est tout.")], ""),
    ("lea", "Tu veux encore me séduire?",
     "Do you want to seduce me again?",
     [(659, "me séduire encore et m'embrasser encore")], ""),
    ("hicham", "Non, ce n'est pas vrai!",
     "No, that is not true!",
     [(661, "-Non, c'est pas vrai !")], ""),
    ("lea", "Je suis enceinte, Hicham.",
     "I am pregnant, Hicham.",
     [(661, "-Je suis enceinte.")], ""),
    ("hicham", "Quoi? Tu es vraiment sérieuse?",
     "What? Are you really serious?",
     [(662, "Quoi ?")], ""),
    ("lea", "Je devais absolument te le dire.",
     "I absolutely had to tell you.",
     [(663, "Tu es la seule personne à qui je devais vraiment le dire.")], ""),
    ("hicham", "Quatre minutes, ça te suffit?",
     "Are four minutes enough for you?",
     [(671, "Quatre minutes, ça suffit ?")], ""),
    ("lea", "Oui, c'est largement suffisant.",
     "Yes, that is more than enough.",
     [(672, "Oui, même moins.")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'What are you doing here, Andrea?' Hicham stops his jogging to question her unexpected presence. "
     "The interrogative phrase qu'est-ce que asks for information."),
    (1, None,
     "'Wait just one little minute.' Andrea urgently asks for a moment of his undivided attention. "
     "The imperative attends requests someone to pause."),
    (2, None,
     "'I am doing my last lap.' The executive explains that he is concluding his workout. "
     "The adjective dernier precedes the masculine noun tour."),
    (3, None,
     "'I must ask you something.' She insists that she has an important topic to bring up. "
     "The modal verb dois expresses an obligation or need."),
    (4, None,
     "'Can we have a drink together?' Hicham proposes meeting more casually over drinks. "
     "The idiom boire un verre means to have a drink."),
    (5, None,
     "'Why should we see each other?' Andrea remains skeptical of his motives after their past encounter. "
     "The question word pourquoi asks for a reason or purpose."),
    (6, None,
     "'To talk calmly, that is all.' He promises that he only wishes to converse peacefully. "
     "The adverb calmement modifies the infinitive parler."),
    (7, None,
     "'Do you want to seduce me again?' She confronts him directly about his flirtatious tendencies. "
     "The verb seduire means to charm or entice."),
    (8, None,
     "'No, that is not true!' Hicham firmly denies having romantic designs on her. "
     "The negative structure ce n'est pas vrai refutes a claim."),
    (9, None,
     "'I am pregnant, Hicham.' Andrea drops the life-changing bombshell without preamble. "
     "The adjective enceinte means pregnant."),
    (10, None,
     "'What? Are you really serious?' Stunned by the revelation, he struggles to process the news. "
     "The feminine adjective serieuse agrees with the female speaker."),
    (11, None,
     "'I absolutely had to tell you.' She feels an ethical responsibility to inform the father. "
     "The imperfect devais denotes a strong past obligation."),
    (12, None,
     "'Are four minutes enough for you?' He abruptly pivots to managing the conversation within his schedule. "
     "The verb suffit means is sufficient or enough."),
    (13, None,
     "'Yes, that is more than enough.' Andrea accepts the brief window to outline her stance. "
     "The adverb largement means broadly or amply."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Stunned by Andrea's pregnancy revelation, Hicham grants her a few brief minutes before heading to London. "
    "Notice how the feminine adjective agrees with the speaker: je suis enceinte."
)

CLOSING = ("lea", "Oui, c'est largement suffisant.")
