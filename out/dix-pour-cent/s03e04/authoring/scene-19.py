# Authoring module for dix-pour-cent s03e04 scene 19 (cues 934-934).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-19.py --out out/dix-pour-cent/s03e04/scene-19.json

ID = "dix-pour-cent-s03e04-scene-19"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 19
TITLE = "Le mal de dos  (The Back Pain)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cue 934. Inside Noemie's apartment, Mathias winces from severe back pain caused by stressful nights at the office. "
    "Noemie shows genuine sympathy and serves him breakfast while Mathias reveals how vulnerable he feels without her."
)

INTRO = (
    "Inside Noemie's apartment, Mathias winces from severe back pain caused by stressful nights at the office. "
    "Noemie shows genuine sympathy and serves him breakfast while Mathias reveals how vulnerable he feels without her. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("lea", "Asseyez-vous Mathias, vous semblez souffrir.",
     "Sit down Mathias, you seem to be suffering.",
     [(934, "Avec mon dos")], "Noticed his obvious physical discomfort"),
    ("mathias", "Avec mon dos et tout, je...",
     "With my back and everything, I...",
     [(934, "Avec mon dos et tout, je...")], "Admitted his severe backache"),
    ("lea", "Votre dos vous fait encore mal?",
     "Is your back hurting you again?",
     [(934, "Avec mon dos")], "Asked about his recurring pain"),
    ("mathias", "Oui, ces nuits courtes sont terribles.",
     "Yes, these short nights are terrible.",
     [(934, "et tout")], "Blamed sleepless nights of work"),
    ("lea", "Vous devriez consulter un bon médecin.",
     "You should consult a good doctor.",
     [(934, "je...")], "Recommended proper medical advice"),
    ("mathias", "Le travail m'épuise complètement sans vous.",
     "Work exhausts me completely without you.",
     [(934, "je...")], "Admitted being exhausted alone"),
    ("lea", "Buvez au moins votre café chaud.",
     "At least drink your hot coffee.",
     [(934, "et tout")], "Encouraged him to drink coffee"),
    ("mathias", "Ce café me fait beaucoup de bien.",
     "This coffee does me a lot of good.",
     [(934, "je...")], "Felt grateful for the warm drink"),
    ("lea", "Vous refusez toujours d'écouter votre corps.",
     "You always refuse to listen to your body.",
     [(934, "Avec mon dos")], "Chided his stubborn workaholic habit"),
    ("mathias", "Je voulais seulement vous voir aujourd'hui.",
     "I only wanted to see you today.",
     [(934, "je...")], "Stated his true morning motivation"),
    ("lea", "Votre visite matinale me touche sincèrement.",
     "Your morning visit touches me sincerely.",
     [(934, "je...")], "Acknowledged her genuine emotional reaction"),
    ("mathias", "Pouvons-nous parler de notre avenir commun?",
     "Can we speak about our common future?",
     [(934, "je...")], "Brought up their mutual future"),
    ("lea", "Finissez d'abord vos délicieux croissants chauds.",
     "First finish your delicious warm croissants.",
     [(934, "et tout")], "Suggested eating breakfast first"),
    ("mathias", "Promettez-moi d'y réfléchir sérieusement, Noémie.",
     "Promise me to think about it seriously, Noemie.",
     [(934, "je...")], "Requested sincere future consideration")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Sit down Mathias, you seem to be suffering.' Noemie invites him to take a seat on the couch. "
     "The polite imperative verb begins the caring exchange."),
    (1, None,
     "'With my back and everything, I...' Mathias struggles to find words for his exhaustion. "
     "The colloquial prepositional phrase explains his physical limitation."),
    (2, None,
     "'Is your back hurting you again?' Noemie inquires about his chronic condition. "
     "The present verbal idiom asks directly about pain."),
    (3, None,
     "'Yes, these short nights are terrible.' Mathias describes his sleepless work schedule. "
     "The descriptive adjective emphasizes his accumulated exhaustion."),
    (4, None,
     "'You should consult a good doctor.' Noemie offers practical health counsel. "
     "The conditional modal verb expresses a gentle recommendation."),
    (5, None,
     "'Work exhausts me completely without you.' Mathias admits his vulnerability in the agency. "
     "The transitive verb conveys total depletion of energy."),
    (6, None,
     "'At least drink your hot coffee.' Noemie points to the steaming mug on the table. "
     "The imperative verb urges him to relax and warm up."),
    (7, None,
     "'This coffee does me a lot of good.' Mathias sips gratefully and feels immediate relief. "
     "The idiom with the verb expresses physical and emotional comfort."),
    (8, None,
     "'You always refuse to listen to your body.' Noemie gently reproaches his obstinate routine. "
     "The negative structure highlights his habit of overworking."),
    (9, None,
     "'I only wanted to see you today.' Mathias explains the true reason for dropping by. "
     "The past tense verb with the restrictive adverb underscores his personal longing."),
    (10, None,
     "'Your morning visit touches me sincerely.' Noemie confesses that his presence matters. "
     "The emotional verb conveys sincere appreciation."),
    (11, None,
     "'Can we speak about our common future?' Mathias steers the talk toward a professional reconciliation. "
     "The inverted modal question asks for an open dialogue."),
    (12, None,
     "'First finish your delicious warm croissants.' Noemie smiles and defers serious business. "
     "The imperative construction encourages enjoying the morning meal together."),
    (13, None,
     "'Promise me to think about it seriously, Noemie.' Mathias makes an earnest appeal before leaving. "
     "The imperative verb asks for thoughtful reflection.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "In her quiet living room, Noemie cares for an aching Mathias as he makes a heartfelt plea to reunite. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("mathias", "Promettez-moi d'y réfléchir sérieusement, Noémie.")
