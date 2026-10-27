# Authoring module for dix-pour-cent s03e02 scene 16 (cues 795-825).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-16.py --out out/dix-pour-cent/s03e02/scene-16.json

ID = "dix-pour-cent-s03e02-scene-16"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 16
TITLE = "La démission de Noémie  (Noémie's Resignation)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 795-825. At ASK the next morning, Noémie enters Mathias's office to announce that a headhunter "
    "offered her an attractive position in Boulogne, and that she is quitting the agency with immediate effect."
)

INTRO = (
    "The next morning at the ASK agency, assistant Noemie Leclerc steps into Mathias Barneville's office. "
    "Tired of workplace humiliation and feeling undervalued, Noemie has an unexpected announcement to make. "
    "Listen to their exchange in French first."
)

STORY = [
    ("mathias", "Entrez dans mon bureau, Noémie.",
     "Come into my office, Noémie.",
     [(796, "Entrez.")], ""),
    ("lea", "Je dois vous parler très sérieusement.",
     "I must talk to you very seriously.",
     [(801, "Pas continuer comme ça, mais oui, mais c'est pas possible.")], ""),
    ("mathias", "Votre comportement d'hier était très gênant.",
     "Your behavior yesterday was very embarrassing.",
     [(798, "C'est quoi, ce numéro que vous avez fait hier devant tout le monde ?"),
      (799, "C'était extrêmement gênant.")], ""),
    ("lea", "Un chasseur de têtes m'a contactée.",
     "A headhunter contacted me.",
     [(805, "chasseur de tête"), (806, "Il m'a repérée.")], ""),
    ("mathias", "Un chasseur de têtes pour vous?",
     "A headhunter for you?",
     [(805, "chasseur de tête")], ""),
    ("lea", "Mon profil est très recherché aujourd'hui.",
     "My profile is very sought after today.",
     [(807, "Oui, j'ai un profil qui est très demandé.")], ""),
    ("mathias", "Quelle proposition avez-vous reçue exactement?",
     "What offer did you receive exactly?",
     [(808, "Et il m'a fait une offre vraiment très intéressante.")], ""),
    ("lea", "J'ai reçu une offre très avantageuse.",
     "I received a very advantageous offer.",
     [(808, "Et il m'a fait une offre vraiment très intéressante.")], ""),
    ("mathias", "Où se trouve cette nouvelle entreprise?",
     "Where is this new company located?",
     [(811, "À Boulogne.")], ""),
    ("lea", "Ce nouveau poste est à Boulogne.",
     "This new post is in Boulogne.",
     [(811, "À Boulogne.")], ""),
    ("mathias", "Et quelle est votre décision finale?",
     "And what is your final decision?",
     [(812, "Et j'ai accepté, donc je pars, je quitte l'agence.")], ""),
    ("lea", "J'ai accepté et je quitte l'agence.",
     "I accepted and I am leaving the agency.",
     [(812, "Et j'ai accepté, donc je pars, je quitte l'agence.")], ""),
    ("mathias", "Quand partez-vous de notre équipe?",
     "When do you leave our team?",
     [(813, "Et ce serait quand ?")], ""),
    ("lea", "Je pars avec un effet immédiat!",
     "I leave with immediate effect!",
     [(814, "Avec effet immédiat, donc oui, maintenant.")], "")
]

OPENER = "Let us examine how Noemie delivers her sudden resignation to Mathias."

WALK = [
    (0, None,
     "'Come into my office, Noémie.' Mathias welcomes his assistant inside. "
     "The imperative entrez expresses a formal professional request."),
    (1, None,
     "'I must talk to you very seriously.' Noémie sets a solemn tone. "
     "The modal verb dois expresses an obligation."),
    (2, None,
     "'Your behavior yesterday was very embarrassing.' Mathias recalls the previous scene. "
     "The possessive determiner votre shows formal address."),
    (3, None,
     "'A headhunter contacted me.' Noémie announces external interest in her career. "
     "The noun phrase chasseur de têtes denotes a corporate recruiter."),
    (4, None,
     "'A headhunter for you?' Mathias reacts with disbelief. "
     "The preposition pour indicates the beneficiary."),
    (5, None,
     "'My profile is very sought after today.' Noémie asserts her professional value. "
     "The passive participle recherché agrees with profil."),
    (6, None,
     "'What offer did you receive exactly?' Mathias asks about specifics. "
     "The interrogative determiner quelle agrees with feminine proposition."),
    (7, None,
     "'I received a very advantageous offer.' Noémie confirms the appealing package. "
     "The feminine adjective avantageuse agrees with offre."),
    (8, None,
     "'Where is this new company located?' Mathias asks for location details. "
     "The reflexive verb se trouver indicates location."),
    (9, None,
     "'This new post is in Boulogne.' Noémie names the Parisian suburb. "
     "The preposition à precedes town names."),
    (10, None,
     "'And what is your final decision?' Mathias faces the inevitable outcome. "
     "The feminine adjective finale agrees with décision."),
    (11, None,
     "'I accepted and I am leaving the agency.' Noémie states her resignation plainly. "
     "The verb quitter takes a direct object."),
    (12, None,
     "'When do you leave our team?' Mathias asks about her departure schedule. "
     "The interrogative adverb quand asks when."),
    (13, None,
     "'I leave with immediate effect!' Noémie refuses any transitional delay. "
     "The phrase avec effet immédiat means effective immediately.")
]

TRANSITION = "Now let us listen to the tense confrontation once more at normal pace."

OUTRO = (
    "Noemie surprises Mathias with her decisive departure, breaking ties with the agency that took her for granted. "
    "Listen to the scene once more in French."
)

CLOSING = ("lea", "Je pars avec un effet immédiat!")
