# Authoring module for dix-pour-cent s02e02 scene 25 (cues 834-857).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-25.py --out out/dix-pour-cent/s02e02/scene-25.json

ID = "dix-pour-cent-s02e02-scene-25"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 25
TITLE = "Moment de tendresse  (A Tender Moment)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 834-857. In Gabriel's office at ASK, Sofia Leprince shows Gabriel a video recording "
    "of a musical play where she performed. They share an intimate and tender conversation "
    "about her acting talent. Adapted for A1 French."
)

INTRO = (
    "In Gabriel's office at ASK, Sofia Leprince shows him a video recording of a musical play. "
    "As they watch her performance together, Gabriel is deeply moved by her singing and acting talent. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("gabriel", "Un prisonnier qui chante, c'est très original.",
     "A singing prisoner, that is very original.",
     [(836, "Un prisonnier qui chante. Très original.")], "Added c'est"),
    ("lea", "Ne faites pas attention à la robe.",
     "Do not pay attention to the dress.",
     [(837, "Ne faites pas attention à la robe,")], ""),
    ("lea", "C'est un court-métrage sans argent.",
     "It is a short film without money.",
     [(837, "c'est un court-métrage fauché.")], "Simplified fauché to sans argent"),
    ("gabriel", "Vous êtes encore son assistante?",
     "Are you still his assistant?",
     [(838, "Vous êtes son assistante.")], "Added encore"),
    ("lea", "Non, plus maintenant.",
     "No, not anymore.",
     [(838, "Plus maintenant.")], ""),
    ("lea", "Ce passage est drôle, regarde.",
     "This passage is funny, look.",
     [(839, "Ce passage est drôle, regardez")], "Adapted to familiar tu"),
    ("lea", "On fait ça plus tard?",
     "Shall we do this later?",
     [(850, "On fait ça plus tard ?")], ""),
    ("gabriel", "Non, continuons, ça va.",
     "No, let us continue, it is fine.",
     [(851, "Non, ça va.")], "Added continuons"),
    ("lea", "Tu as raté quelque chose d'important.",
     "You missed something important.",
     [(852, "Seulement vous avez raté quelque chose d'important.")], "Adapted to tu"),
    ("lea", "Je reviens un peu en arrière.",
     "I am going back a little.",
     [(853, "Je reviens en arrière.")], ""),
    ("lea", "On reprend ici, regarde bien.",
     "We resume here, watch closely.",
     [(853, "On reprend... ici.")], "Added regarde bien"),
    ("lea", "Ce passage est vraiment bien.",
     "This passage is really good.",
     [(854, "Ce passage est bien.")], "Added vraiment"),
    ("gabriel", "Ça va, Sofia?",
     "Are you okay, Sofia?",
     [(855, "Ça va ?")], ""),
    ("lea", "Oui, je suis émue.",
     "Yes, I am moved.",
     [(856, "Oui.")], "Added je suis émue"),
    ("gabriel", "C'est magnifique, Sofia.",
     "It is wonderful, Sofia.",
     [(857, "C'est magnifique, Sofia.")], ""),
    ("gabriel", "Tu es vraiment magnifique.",
     "You are really wonderful.",
     [(857, "Tu es magnifique.")], "Added vraiment"),
]

OPENER = "Let's examine how Gabriel and Sofia share a tender moment watching her tape."

WALK = [
    (0, None,
     "'A singing prisoner, that is very original.' Gabriel comments on the unusual premise of the film."),
    (1, None,
     "'Do not pay attention to the dress.' A polite negative imperative with the idiom faire attention a."),
    (2, None,
     "'It is a short film without money.' The compound noun court-metrage meaning a short movie."),
    (3, None,
     "'Are you still his assistant?' Gabriel asks about her previous administrative job."),
    (4, None,
     "'No, not anymore.' An elliptical negative response using plus maintenant."),
    (5, None,
     "'This passage is funny, look.' Sofia points out a humorous moment with an imperative."),
    (6, None,
     "'Shall we do this later?' An informal suggestion with the pronoun on."),
    (7, None,
     "'No, let us continue, it is fine.' Gabriel insists on continuing the viewing."),
    (8, None,
     "'You missed something important.' The compound past tense of rater meaning to miss."),
    (9, None,
     "'I am going back a little.' The spatial phrase en arriere meaning backward."),
    (10, None,
     "'We resume here, watch closely.' The verb reprendre used in the sense of resuming a video."),
    (11, None,
     "'This passage is really good.' An affirmative evaluation using the adverb vraiment."),
    (12, None,
     "'Are you okay, Sofia?' Gabriel checks on her feelings with a familiar question."),
    (13, None,
     "'Yes, I am moved.' A feminine past participle expressing tender emotion."),
    (14, None,
     "'It is wonderful, Sofia.' An appreciative evaluative adjective."),
    (15, None,
     "'You are really wonderful.' Gabriel addresses Sofia with sincere romantic admiration."),
]

TRANSITION = "Now let's listen to the whole discussion again without stopping."

OUTRO = (
    "Gabriel has watched Sofia's performance tape and is captivated by her talent and charm. "
    "Their bond deepens as Sofia realizes Gabriel truly believes in her."
)

CLOSING = ("lea", "Merci, Gabriel.")
