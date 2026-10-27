# Authoring module for dix-pour-cent s02e03 scene 29 (cues 733-800).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-29.py --out out/dix-pour-cent/s02e03/scene-29.json

ID = "dix-pour-cent-s02e03-scene-29"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 29
TITLE = "Garde à vue pour Norman et Gabriel  (In Custody for Norman and Gabriel)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "officer": "marcel"}
LABELS = {"lea": "Norman", "gabriel": "Gabriel", "officer": "Le policier"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 733-800. Gabriel rushes to the police station where Norman Thavaud is held in a sobering-up cell "
    "after speeding without his license. Terrified of failing in Jacques Audiard's new film, Norman begs Gabriel "
    "to cancel the role; Gabriel fakes a voicemail, argues with the officer, and gets locked up as well."
)

INTRO = (
    "Following a chaotic birthday joyride, YouTuber Norman Thavaud is taken to the police station for speeding without his driver's license. "
    "Gabriel rushes to the station, only to find a panicked Norman desperate to abandon his dream role in Jacques Audiard's upcoming film. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("gabriel", "Bonsoir. Que se passe-t-il?", "Good evening. What is going on?",
     [(733, "Bonsoir. Que se passe-t-il")], "Gabriel arrives at the police station"),
    ("officer", "M. Norman Thavaud roulait en excès de vitesse.", "Mr. Norman Thavaud was speeding.",
     [(736, "M. Norman Thavaud"), (737, "qui roulait en excès de vitesse")], ""),
    ("officer", "Le juge pourrait lui retirer le permis.", "The judge could take away his license.",
     [(754, "Le juge pourrait lui retirer le permis")], ""),
    ("gabriel", "Puis-je le voir?", "May I see him?",
     [(757, "Puis-je le voir")], ""),
    ("officer", "Par ici. Il est en cellule de dégrisement.", "This way. He is in the sobering-up cell.",
     [(758, "Par ici. Il est en cellule de dégrisement")], ""),
    ("gabriel", "Tu joues à quoi? Tu ne veux plus faire le film?", "What are you playing at? You don't want to do the film anymore?",
     [(760, "Tu joues à quoi"), (761, "Tu ne veux plus faire le film")], "confronting Norman in the cell"),
    ("lea", "Il pense déjà que je suis un loser.", "He already thinks that I am a loser.",
     [(764, "Il pense déjà que je suis un loser")], ""),
    ("gabriel", "Arrête, il t'a casté, tu l'as convaincu.", "Stop it, he cast you, you convinced him.",
     [(765, "Arrête, il t'a casté, tu l'as convaincu")], ""),
    ("lea", "Il n'est pas de mon monde, pas mon univers.", "He is not from my world, not my universe.",
     [(767, "Il n'est pas de mon monde, pas mon univers")], ""),
    ("lea", "Je vais me ridiculiser.", "I am going to make a fool of myself.",
     [(768, "Je vais me ridiculiser")], ""),
    ("lea", "Appelle-le, annule et qu'on en finisse.", "Call him, cancel and let's get it over with.",
     [(776, "Appelle-le, annule et qu'on en finisse")], ""),
    ("gabriel", "Bonjour Jacques. C'est Gabriel Sarda.", "Hello Jacques. It is Gabriel Sarda.",
     [(783, "Bonjour Jacques"), (784, "C'est Gabriel Sarda")], "pretending to leave a voicemail for Audiard"),
    ("gabriel", "Norman ne veut pas faire votre film.", "Norman does not want to do your movie.",
     [(784, "Norman"), (785, "il ne veut pas faire votre film")], ""),
    ("officer", "Ne haussez pas la voix!", "Do not raise your voice!",
     [(790, "ne haussez pas la voix")], "the officer intervenes"),
    ("officer", "Vous avez bu?", "Have you been drinking?",
     [(793, "Vous avez bu")], ""),
    ("gabriel", "On m'embarque aussi?", "Are you locking me up too?",
     [(794, "On m'embarque aussi")], ""),
    ("lea", "Je suis un raté.", "I am a failure.",
     [(798, "Je suis un raté")], ""),
    ("gabriel", "Pas du tout. Vous avez été casté dans un film d'Audiard.", "Not at all. You were cast in an Audiard movie.",
     [(799, "Pas du tout. Vous avez été casté dans un film d'Audiard")], ""),
]

OPENER = "Let's walk through the tense police station encounter step by step."

WALK = [
    (0, None,
     "'Good evening. What is going on?' The inversion 'se passe-t-il' asks what is happening."),
    (1, None,
     "'Mr. Norman Thavaud was speeding.' The imperfect 'roulait' describes the ongoing driving."),
    (2, None,
     "'The judge could take away his license.' The conditional 'pourrait' expresses future possibility."),
    (3, None,
     "'May I see him?' The formal inversion 'puis-je' asks polite permission."),
    (4, None,
     "'This way. He is in the sobering-up cell.' The fixed phrase 'par ici' indicates direction."),
    (5, None,
     "'What are you playing at? You don't want to do the film anymore?' Gabriel expresses utter disbelief."),
    (6, None,
     "'He already thinks that I am a loser.' The adverb 'deja' means already."),
    (7, None,
     "'Stop it, he cast you, you convinced him.' Gabriel urges Norman to trust his talent."),
    (8, None,
     "'He is not from my world, not my universe.' Norman fears the prestigious cinema world."),
    (9, None,
     "'I am going to make a fool of myself.' The reflexive verb 'se ridiculiser' means to look foolish."),
    (10, None,
     "'Call him, cancel and let's get it over with.' Two urgent imperatives command immediate cancellation."),
    (11, None,
     "'Hello Jacques. It is Gabriel Sarda.' Gabriel pretends to dial the famous director."),
    (12, None,
     "'Norman does not want to do your movie.' The negation 'ne... pas' frames Norman's refusal."),
    (13, None,
     "'Do not raise your voice!' The negative imperative warns Gabriel against shouting."),
    (14, None,
     "'Have you been drinking?' The compound past tense uses the auxiliary verb 'avoir'."),
    (15, None,
     "'Are you locking me up too?' The pronoun 'on' represents the police officers."),
    (16, None,
     "'I am a failure.' Norman sinks into self-pity on the cell bench."),
    (17, None,
     "'Not at all. You were cast in an Audiard movie.' Gabriel encourages his despondent young star."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "After feigning a cancellation call to Audiard and clashing with the police officer, Gabriel finds himself locked inside the drunk tank alongside his anxious client."
CLOSING = ("gabriel", "Vous avez été casté dans un film d'Audiard.")
