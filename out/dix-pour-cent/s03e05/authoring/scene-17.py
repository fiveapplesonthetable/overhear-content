# Authoring module for dix-pour-cent s03e05 scene 17 (cues 738-772).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e05/authoring/scene-17.py --out overhear-content/out/dix-pour-cent/s03e05/scene-17.json

ID = "dix-pour-cent-s03e05-scene-17"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 17
TITLE = "Un nouveau rendez-vous  (A New Meeting)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo", "noemie": "emilie"}
LABELS = {"lea": "Camille", "herve": "Hervé", "noemie": "Noémie"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 738-772. At ASK, Camille books an important audition for actress Sophia Leprince, "
    "while Noémie reassures Mathias that Hicham's prolonged silence indicates the rival deal is failing."
)

INTRO = (
    "At the ASK agency, Camille Valentini lands an exciting movie audition for client Sophia Leprince. "
    "Meanwhile, Noemie calms Mathias's anxieties by pointing out that their boss's unusual silence means good news for their plans. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Oui, bonjour, c'est pour quel projet?",
     "Yes, hello, what project is it for?",
     [(753, "bonjour"), (756, "C'est pour quel projet")], ""),
    ("lea", "Sophia Leprince est une excellente comédienne.",
     "Sophia Leprince is an excellent actress.",
     [(754, "Sophia Leprince"), (755, "comédienne de chez nous")], ""),
    ("lea", "Attendez, je regarde son planning maintenant.",
     "Wait, I am checking her schedule now.",
     [(757, "je regarde son planning")], ""),
    ("lea", "Vous avez vraiment de la chance.",
     "You are truly in luck.",
     [(759, "vous avez de la chance")], ""),
    ("lea", "Un rendez-vous s'est libéré demain.",
     "An appointment opened up tomorrow.",
     [(760, "un rendez-vous qui s'est libéré")], ""),
    ("lea", "Très bien, je le note soigneusement.",
     "Very good, I note it down carefully.",
     [(761, "Très bien"), (762, "je le note")], ""),
    ("lea", "Merci beaucoup et au revoir, monsieur.",
     "Thank you very much and goodbye, sir.",
     [(764, "Merci au revoir")], ""),
    ("herve", "Tu as décroché ce rendez-vous?",
     "Did you land that appointment?",
     [(766, "choper un rendez-vous")], ""),
    ("lea", "Oui, un rendez-vous pour un film!",
     "Yes, an appointment for a feature film!",
     [(766, "pour demain pour un film")], ""),
    ("herve", "Ce n'est vraiment pas croyable!",
     "That is truly unbelievable!",
     [(767, "c'est pas vrai")], ""),
    ("noemie", "Si tout allait bien avec eux...",
     "If everything went well with them...",
     [(768, "bien passé avec les américains")], ""),
    ("noemie", "Hicham vous aurait appelé depuis longtemps.",
     "Hicham would have called you long ago.",
     [(769, "Hicham il vous aurait appelé depuis longtemps")], ""),
    ("noemie", "Il adore toujours se vanter.",
     "He always loves to brag.",
     [(770, "genre à fanfaronner")], ""),
    ("noemie", "Alors arrêtez de stresser comme ça.",
     "So stop stressing like that.",
     [(772, "arrêtez de stresser là")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Yes, hello, what project is it for?' Camille answers a call from a movie producer. "
     "The professional question inquires about the script."),
    (1, None,
     "'Sophia Leprince is an excellent actress.' She praises her client's acting talent. "
     "The affirmative statement promotes her artist."),
    (2, None,
     "'Wait, I am checking her schedule now.' Camille looks up the actress's diary. "
     "The present verb phrase manages the calendar."),
    (3, None,
     "'You are truly in luck.' She informs the caller of a rare opening. "
     "The encouraging expression creates professional enthusiasm."),
    (4, None,
     "'An appointment opened up tomorrow.' Camille offers an available casting slot. "
     "The past verb phrase announces an opportunity."),
    (5, None,
     "'Very good, I note it down carefully.' She records the meeting details. "
     "The confirming formula seals the appointment."),
    (6, None,
     "'Thank you very much and goodbye, sir.' Camille concludes the business phone call politely. "
     "The polite formula ends the conversation."),
    (7, None,
     "'Did you land that appointment?' Herve asks about the phone conversation. "
     "The enthusiastic question seeks confirmation."),
    (8, None,
     "'Yes, an appointment for a feature film!' Camille shares the exciting news with her colleague. "
     "The cheerful exclamation announces the success."),
    (9, None,
     "'That is truly unbelievable!' Herve celebrates her successful booking. "
     "The colloquial expression marks joyful surprise."),
    (10, None,
     "'If everything went well with them...' Noemie analyzes the American negotiations. "
     "The conditional clause questions the rival deal."),
    (11, None,
     "'Hicham would have called you long ago.' She points out the boss's silence. "
     "The past conditional verb notes the delay."),
    (12, None,
     "'He always loves to brag.' Noemie describes Hicham's boastful personality. "
     "The character observation provides reassurance."),
    (13, None,
     "'So stop stressing like that.' She urges her colleagues to stay calm. "
     "The imperative advice soothes office tension.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Confidence and quick thinking help agents navigate sudden opportunities and high-stakes rivalries at ASK. "
    "Listen to the conversation once more in French."
)

CLOSING = ("lea", "C'est une très bonne journée.")
