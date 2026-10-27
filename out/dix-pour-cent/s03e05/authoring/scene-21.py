# Authoring module for dix-pour-cent s03e05 scene 21 (cues 829-830).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-21.py --out out/dix-pour-cent/s03e05/scene-21.json

ID = "dix-pour-cent-s03e05-scene-21"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 21
TITLE = "Un moment de paix  (A Moment of Peace)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "colette": "Colette", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 829-830. Hicham visits Andréa's apartment late in the evening to hold baby Flora peacefully. "
    "Colette walks in surprised, but Hicham reassures her that he comes without conflict, and the three share a quiet moment of peace."
)

INTRO = (
    "At Andrea's apartment, Hicham visits to hold baby Flora peacefully. "
    "When Colette walks in surprised, Hicham reassures her that he comes without conflict, and the three parents share a rare quiet moment of domestic peace. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("hicham", "Je ne viens pas parler boulot.",
     "I am not coming to talk business.",
     [(826, "pas là pour parler boulot")], "Hicham sets aside agency tensions"),
    ("lea", "Alors, que veux-tu ce soir, Hicham?",
     "So, what do you want tonight, Hicham?",
     [(825, "trop tard pour parler boulot")], "Andrea questions his late arrival"),
    ("hicham", "Je voudrais juste voir le bébé.",
     "I would just like to see the baby.",
     [(827, "voir un peu la petite")], "Hicham expresses his paternal longing"),
    ("hicham", "Puis-je la prendre dans mes bras?",
     "May I hold her in my arms?",
     [(828, "garder un peu comme ça")], "Hicham gently asks permission"),
    ("lea", "D'accord, tiens bien sa tête.",
     "All right, hold her head well.",
     [(828, "garder un peu comme ça")], "Andrea gives practical motherly guidance"),
    ("hicham", "Elle est tellement belle et calme.",
     "She is so beautiful and calm.",
     [(828, "garder un peu comme ça")], "Hicham marvels at his newborn daughter"),
    ("lea", "Elle s'endort paisiblement avec toi.",
     "She falls asleep peacefully with you.",
     [(828, "garder un peu comme ça")], "Andrea notices the baby's serenity"),
    ("colette", "Bonjour, qu'est-ce que vous faites là?",
     "Hello, what are you doing here?",
     [(829, "Qu'est-ce que vous faites")], "Colette walks into the room startled"),
    ("lea", "Colette, regarde, nous sommes calmes.",
     "Colette, look, we are calm.",
     [(830, "On kiffe")], "Andrea de-escalates any potential worry"),
    ("hicham", "On kiffe ce joli moment ensemble.",
     "We are enjoying this lovely moment together.",
     [(830, "On kiffe")], "Hicham describes their shared peaceful mood"),
    ("colette", "C'est une surprise très inattendue.",
     "It is a very unexpected surprise.",
     [(829, "Qu'est-ce que vous faites")], "Colette observes the tranquil scene"),
    ("hicham", "Je ne veux aucun conflit, Colette.",
     "I want no conflict, Colette.",
     [(826, "pas là pour parler boulot")], "Hicham extends an olive branch"),
    ("lea", "Nous voulons le bonheur de Flora.",
     "We want Flora's happiness.",
     [(827, "voir un peu la petite")], "Andrea speaks for their collective child"),
    ("colette", "C'est un beau moment de paix.",
     "It is a beautiful moment of peace.",
     [(830, "On kiffe")], "Colette accepts the warm harmony")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'I am not coming to talk business.' Hicham clarifies his personal intentions right away. "
     "The negative present verb excludes professional disputes."),
    (1, None,
     "'So, what do you want tonight, Hicham?' Andrea asks why he stopped by so late. "
     "The interrogative inversion inquires about his evening purpose."),
    (2, None,
     "'I would just like to see the baby.' Hicham confesses his simple paternal wish. "
     "The conditional polite verb expresses a gentle request."),
    (3, None,
     "'May I hold her in my arms?' Hicham asks to cradle his newborn daughter. "
     "The formal inverted modal verb respectfully asks permission."),
    (4, None,
     "'All right, hold her head well.' Andrea grants permission with careful instructions. "
     "The imperative verb advises supporting the infant's neck."),
    (5, None,
     "'She is so beautiful and calm.' Hicham is deeply moved by the child's stillness. "
     "The coordinated adjectives express tender emotional awe."),
    (6, None,
     "'She falls asleep peacefully with you.' Andrea acknowledges their natural bond. "
     "The reflexive verb with an adverb describes the baby settling down."),
    (7, None,
     "'Hello, what are you doing here?' Colette reacts with surprise upon entering. "
     "The interrogative phrase questions the unexpected gathering."),
    (8, None,
     "'Colette, look, we are calm.' Andrea reassures her partner instantly. "
     "The imperative verb draws attention to their peaceful composure."),
    (9, None,
     "'We are enjoying this lovely moment together.' Hicham uses slang to describe the quiet joy. "
     "The colloquial verb denotes appreciating a serene moment."),
    (10, None,
     "'It is a very unexpected surprise.' Colette takes in the tender scene. "
     "The predicate adjective acknowledges the unexpected truce."),
    (11, None,
     "'I want no conflict, Colette.' Hicham reassures Colette of his goodwill. "
     "The negative determiner promises an end to legal fighting."),
    (12, None,
     "'We want Flora's happiness.' Andrea unites all three parents behind one goal. "
     "The plural subject verb affirms their shared devotion to Flora."),
    (13, None,
     "'It is a beautiful moment of peace.' Colette embraces the peaceful domestic truce. "
     "The appreciative noun phrase confirms mutual acceptance.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "In a rare quiet evening, Andrea, Colette, and Hicham find unexpected harmony around baby Flora. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("colette", "C'est un beau moment de paix.")
