# Authoring module for dix-pour-cent s04e06 scene 13 (cues 623-658).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e06/authoring/scene-13.py --out out/dix-pour-cent/s04e06/scene-13.json

ID = "dix-pour-cent-s04e06-scene-13"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 13
TITLE = "L'attente de Jean Reno  (Waiting for Jean Reno)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 623-658. In Andrea's office, Gabriel laments losing their last financier for Xavier Beauvois's screenplay, "
    "but their despair turns to hopeful excitement when Jean Reno agrees to visit ASK in person."
)

INTRO = (
    "In Andrea's office at ASK, tensions run high as Gabriel reports another devastating financing rejection for Xavier Beauvois's script. "
    "Just as their hopes seem completely dashed, unexpected news arrives that movie star Jean Reno is heading to the agency. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's look at Gabriel and Andrea preparing for their crucial meeting step by step."

STORY = [
    ("gabriel", "Je ne comprends pas son refus.",
     "I do not understand his refusal.",
     [(623, "Je ne comprends pas")], "Gabriel vents his frustration over the investor's decision"),
    ("lea", "Tu avais presque réussi à le convaincre?",
     "You had almost managed to convince him?",
     [(624, "presque réussi à le convaincre")], "Andrea asks about the negotiations"),
    ("gabriel", "Oui, et au dernier moment, il refuse.",
     "Yes, and at the last moment, he refuses.",
     [(624, "au dernier moment")], "Gabriel explains the sudden turnaround"),
    ("lea", "Il t'a donné une raison précise?",
     "Did he give you a specific reason?",
     [(625, "Il t'a donné une raison")], "Inquires about any formal explanation"),
    ("gabriel", "Non, il reste muet comme une tombe.",
     "No, he remains silent as a grave.",
     [(627, "comme une tombe")], "Describes the financier's stony silence"),
    ("lea", "Alors c'est terminé avec lui.",
     "Then it is over with him.",
     [(628, "c'est terminé maintenant")], "Andrea accepts that the deal is dead"),
    ("gabriel", "Laisse tomber, c'est trop tard.",
     "Forget it, it is too late.",
     [(631, "Laisse tomber")], "Gabriel advises against chasing him further"),
    ("lea", "Nous avons besoin d'un grand acteur.",
     "We need a great actor.",
     [(628, "c'est terminé maintenant")], "Stresses the necessity of star power"),
    ("gabriel", "Jean Reno sera bientôt là!",
     "Jean Reno will be here soon!",
     [(633, "Il est en route")], "Gabriel delivers the exciting update"),
    ("lea", "Jean Reno arrive vraiment à l'agence?",
     "Jean Reno is really coming to the agency?",
     [(634, "Sérieusement")], "Andrea reacts with astonished hope"),
    ("gabriel", "Oui, il est en route maintenant.",
     "Yes, he is on his way now.",
     [(633, "Il est en route")], "Confirms that the star is en route"),
    ("lea", "C'est notre dernière chance de survie.",
     "It is our last chance of survival.",
     [(634, "Sérieusement")], "Emphasizes what is at stake for the agency"),
    ("gabriel", "Il adore déjà le beau scénario.",
     "He already loves the beautiful script.",
     [(633, "Il est en route")], "Notes the actor's enthusiasm for the material"),
    ("lea", "Préparons son accueil avec grand soin.",
     "Let us prepare his welcome with great care.",
     [(634, "Sérieusement")], "Rallies to make an impeccable impression"),
]

WALK = [
    (0, None,
     "'I do not understand his refusal.' Gabriel expresses bewilderment at the financier's rejection."),
    (1, None,
     "'You had almost managed to convince him?' Andrea confirms how close they came to a deal."),
    (2, None,
     "'Yes, and at the last moment, he refuses.' Gabriel describes the investor pulling out abruptly."),
    (3, None,
     "'Did he give you a specific reason?' Andrea asks if any motive was provided."),
    (4, None,
     "'No, he remains silent as a grave.' Gabriel uses a vivid idiom to indicate total silence."),
    (5, None,
     "'Then it is over with him.' Andrea moves on from the lost opportunity."),
    (6, None,
     "'Forget it, it is too late.' Gabriel cautions against wasting further energy."),
    (7, None,
     "'We need a great actor.' Andrea identifies the key element needed to revive the film."),
    (8, None,
     "'Jean Reno will be here soon!' Gabriel announces that a legendary star is arriving."),
    (9, None,
     "'Jean Reno is really coming to the agency?' Andrea verifies the astonishing news."),
    (10, None,
     "'Yes, he is on his way now.' Gabriel reassures her that the actor is traveling to ASK."),
    (11, None,
     "'It is our last chance of survival.' Andrea stresses the existential stakes for the firm."),
    (12, None,
     "'He already loves the beautiful script.' Gabriel builds confidence ahead of the pitch."),
    (13, None,
     "'Let us prepare his welcome with great care.' Andrea prepares to give the star their utmost focus."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Crushed by another funding rejection, Andrea and Gabriel suddenly find new hope when legendary actor Jean Reno agrees to visit ASK to discuss Xavier Beauvois's screenplay."
CLOSING = ("gabriel", "Oui, il est en route maintenant.")
