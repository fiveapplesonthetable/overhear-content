# Authoring module for dix-pour-cent s03e06 scene 17 (cues 902-914).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e06/authoring/scene-17.py --out overhear-content/out/dix-pour-cent/s03e06/scene-17.json

ID = "dix-pour-cent-s03e06-scene-17"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 17
TITLE = "Aveux mutuels  (Mutual Confessions)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Catherine", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 902-914. In a quiet corridor at the anniversary party, Catherine and Mathias have an honest talk "
    "about their marriage, discovering that both of them have fallen in love with someone else."
)

INTRO = (
    "In a quiet corridor at the anniversary party, Catherine and Mathias have an honest talk about their marriage. "
    "Both admit that they have fallen in love with someone else, marking a tender end to their years together. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "On ne s'entend pas du tout ici.",
     "We cannot hear each other at all here.",
     [(896, "On s'entend pas")], ""),
    ("mathias", "Viens, allons dans mon bureau tranquille.",
     "Come, let us go into my quiet office.",
     [(897, "aller dans mon bureau")], ""),
    ("lea", "Je ne suis pas à l'aise, Mathias.",
     "I am not comfortable, Mathias.",
     [(898, "pas à l'aise ici, Mathias")], ""),
    ("lea", "Je ne peux plus faire semblant.",
     "I can no longer pretend.",
     [(899, "plus à faire semblant")], ""),
    ("mathias", "Nous essayons de nous parler calmement.",
     "We are trying to speak to each other calmly.",
     [(900, "ça va aller")], ""),
    ("lea", "Disons-nous la vérité pour une fois.",
     "Let us tell each other the truth for once.",
     [(901, "se dire la vérité")], ""),
    ("lea", "Il y a quelqu'un d'autre maintenant.",
     "There is someone else now.",
     [(902, "Il y a quelqu'un d'autre")], ""),
    ("mathias", "C'est toi qui me dis cela?",
     "Are you the one telling me that?",
     [(903, "C'est toi qui viens de")], ""),
    ("mathias", "Moi aussi, j'ai rencontré quelqu'un.",
     "I too have met someone.",
     [(904, "j'ai rencontré quelqu'un")], ""),
    ("lea", "Toi aussi, c'est vrai?",
     "You too, is that true?",
     [(905, "Toi aussi")], ""),
    ("lea", "Alexandre m'a rejointe en Inde.",
     "Alexandre joined me in India.",
     [(910, "Alexandre, donc il m'a rejointe en Inde")], ""),
    ("lea", "Et toi, c'est une vraie rencontre?",
     "And you, is it a real connection?",
     [(911, "Et toi, c'est qui"), (912, "une vraie rencontre")], ""),
    ("mathias", "Oui, c'est une histoire très importante.",
     "Yes, it is a very important relationship.",
     [(912, "une vraie rencontre")], ""),
    ("lea", "Alors, notre mariage est bien terminé.",
     "So, our marriage is truly over.",
     [(908, "t'as raison")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'We cannot hear each other at all here.' Catherine complains about the loud music at the party. "
     "The negative structure emphasizes the noise."),
    (1, None,
     "'Come, let us go into my quiet office.' Mathias invites his wife to step aside for a private chat. "
     "The imperative verb suggests seclusion."),
    (2, None,
     "'I am not comfortable, Mathias.' She hesitates to step into his professional domain. "
     "The personal adjective conveys emotional unease."),
    (3, None,
     "'I can no longer pretend.' Catherine admits that she cannot keep up false appearances. "
     "The negative phrase signals a turning point."),
    (4, None,
     "'We are trying to speak to each other calmly.' Mathias attempts to comfort his stressed spouse. "
     "The present tense seeks peaceful dialogue."),
    (5, None,
     "'Let us tell each other the truth for once.' She urges complete honesty between them. "
     "The imperative verb calls for mutual openness."),
    (6, None,
     "'There is someone else now.' Catherine confesses that she has fallen in love. "
     "The simple statement reveals a life change."),
    (7, None,
     "'Are you the one telling me that?' Mathias reacts with gentle surprise to her confession. "
     "The emphatic cleft sentence questions her words."),
    (8, None,
     "'I too have met someone.' He reciprocates with his own honest confession. "
     "The stressed pronoun reveals shared feelings."),
    (9, None,
     "'You too, is that true?' Catherine wonders if she heard him correctly. "
     "The short question confirms their shared reality."),
    (10, None,
     "'Alexandre joined me in India.' She mentions the partner she reconnected with abroad. "
     "The past tense explains her new bond."),
    (11, None,
     "'And you, is it a real connection?' Catherine asks about his new relationship with warmth. "
     "The interrogative phrase seeks genuine reassurance."),
    (12, None,
     "'Yes, it is a very important relationship.' Mathias confirms his deep feelings for Noemie. "
     "The strong adjective validates his new path."),
    (13, None,
     "'So, our marriage is truly over.' Both partners acknowledge the closure of their shared journey. "
     "The past participle recognizes the peaceful end.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "With quiet dignity and mutual understanding, Catherine and Mathias close one chapter and prepare for new beginnings. "
    "Listen to the conversation once more in French."
)

CLOSING = ("mathias", "Nous restons amis pour toujours.")
