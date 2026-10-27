# Authoring module for dix-pour-cent s04e06 scene 16 (cues 735-822).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e06/authoring/scene-16.py --out out/dix-pour-cent/s04e06/scene-16.json

ID = "dix-pour-cent-s04e06-scene-16"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 16
TITLE = "Confrontation au supermarché  (Confrontation at the Supermarket)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "elise": "emilie"}
LABELS = {"lea": "Andréa", "elise": "Élise"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 735-822. In a crowded supermarket aisle, Andrea corners Elise Formain amidst family groceries, "
    "accusing her rival of manipulating producer Igor to choke off funding for Xavier Beauvois's film."
)

INTRO = (
    "Tracking rival agent Elise Formain to a Parisian supermarket, Andrea finds her maneuvering a shopping cart while buying supplies for her three children. "
    "Andrea wastes no time confronting Elise over her secretive romance with producer Igor and her behind-the-scenes efforts to torpedo ASK's production. "
    "Let's listen to their confrontation in French first."
)

OPENER = "Let's look at Andrea confronting Elise in the supermarket aisle step by step."

STORY = [
    ("lea", "Tu me fais venir ici pour tes courses?",
     "Are you making me come here for your groceries?",
     [(735, "porter tes courses")], "Andrea questions meeting in a supermarket aisle"),
    ("elise", "J'ai trois enfants à nourrir, Andréa.",
     "I have three children to feed, Andrea.",
     [(736, "J'ai trois enfants")], "Elise justifies multitasking during her busy day"),
    ("lea", "Alors viens me parler franchement maintenant.",
     "Then come speak to me frankly now.",
     [(741, "Qu'est-ce que tu veux")], "Andrea demands an honest conversation"),
    ("elise", "Qu'est-ce que tu veux de moi?",
     "What do you want from me?",
     [(741, "Qu'est-ce que tu veux")], "Elise feigns innocence among the shelves"),
    ("lea", "Tu bloques le film de Beauvois!",
     "You are blocking Beauvois's film!",
     [(746, "bloques le financement du film de Beauvois")], "Andrea directly levels the accusation"),
    ("elise", "Igor est libre de choisir ses projets.",
     "Igor is free to choose his projects.",
     [(745, "Igor")], "Elise defends her producer boyfriend's choices"),
    ("lea", "Tu manipules Igor contre notre agence.",
     "You are manipulating Igor against our agency.",
     [(746, "bloques le financement")], "Andrea calls out her underhanded sabotage"),
    ("elise", "Ce scénario est trop sombre et risqué.",
     "This script is too dark and risky.",
     [(746, "bloques le financement")], "Elise criticizes the movie's commercial prospects"),
    ("lea", "Jean Reno a accepté le rôle principal!",
     "Jean Reno accepted the lead role!",
     [(746, "bloques le financement")], "Andrea reveals her unexpected masterstroke"),
    ("elise", "Jean Reno? Tu te moques de moi?",
     "Jean Reno? Are you kidding me?",
     [(746, "bloques le financement")], "Elise is visibly taken aback by the revelation"),
    ("lea", "Non, il a signé avec nous aujourd'hui.",
     "No, he signed with us today.",
     [(746, "bloques le financement")], "Andrea confirms the actor's solid commitment"),
    ("elise", "Alors Igor devra revoir sa position.",
     "Then Igor will have to review his position.",
     [(745, "Igor")], "Elise realizes she has lost this strategic round"),
    ("lea", "Ne sous-estime jamais notre détermination, Élise.",
     "Never underestimate our determination, Elise.",
     [(746, "bloques le financement")], "Andrea delivers a stern parting warning"),
    ("elise", "Nous verrons qui gagne cette bataille.",
     "We will see who wins this battle.",
     [(746, "bloques le financement")], "Elise promises the corporate war is far from over"),
]

WALK = [
    (0, None,
     "'Are you making me come here for your groceries?' Andrea expresses exasperation at the location."),
    (1, None,
     "'I have three children to feed, Andrea.' Elise cites motherhood to explain her rushed schedule."),
    (2, None,
     "'Then come speak to me frankly now.' Andrea insists that they stop playing games."),
    (3, None,
     "'What do you want from me?' Elise asks what brought Andrea all the way to the store."),
    (4, None,
     "'You are blocking Beauvois's film!' Andrea directly confronts her with the obstruction."),
    (5, None,
     "'Igor is free to choose his projects.' Elise attempts to shield her partner from blame."),
    (6, None,
     "'You are manipulating Igor against our agency.' Andrea reveals that she sees right through the plot."),
    (7, None,
     "'This script is too dark and risky.' Elise falls back on conventional industry objections."),
    (8, None,
     "'Jean Reno accepted the lead role!' Andrea drops the bombshell that changes the balance of power."),
    (9, None,
     "'Jean Reno? Are you kidding me?' Elise struggles to mask her sudden astonishment."),
    (10, None,
     "'No, he signed with us today.' Andrea confirms that the contract is sealed."),
    (11, None,
     "'Then Igor will have to review his position.' Elise concedes that the film can no longer be ignored."),
    (12, None,
     "'Never underestimate our determination, Elise.' Andrea warns her rival not to count ASK out."),
    (13, None,
     "'We will see who wins this battle.' Elise signals that their rivalry will continue until the end."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Cornering Elise Formain in a grocery aisle, Andrea calls out her sabotage of Xavier Beauvois's film and delivers a stunning blow by revealing that Jean Reno has officially signed on as lead actor."
CLOSING = ("lea", "Ne sous-estime jamais notre détermination, Élise.")
