# Authoring module for dix-pour-cent s03e06 scene 20 (cues 981-1006).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e06/authoring/scene-20.py --out out/dix-pour-cent/s03e06/scene-20.json

ID = "dix-pour-cent-s03e06-scene-20"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 20
TITLE = "Le sosie d'Isabelle  (Isabelle's Double)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "noemie": "emilie"}
LABELS = {"lea": "Corinne", "noemie": "Noémie"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 981-1006. At the ASK anniversary party, Corinne introduces herself to Noémie "
    "and admits she was the ghost double for Isabelle Huppert, sending Noémie into a panic."
)

INTRO = (
    "At the ASK anniversary party, Corinne arrives and strikes up a conversation with Noemie. "
    "Corinne innocently reveals that she acted as the secret double for Isabelle Huppert, causing Noemie to panic over what the producers might discover. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Bonsoir, je cherche les organisateurs.",
     "Good evening, I am looking for the organizers.",
     [(981, "Bonsoir")], "Corinne politely introduces herself"),
    ("noemie", "Bonsoir, je suis Noémie, assistante.",
     "Good evening, I am Noemie, assistant.",
     [(983, "Je suis Noémie")], "Noemie introduces herself warmly"),
    ("lea", "C'est moi le fameux fantôme.",
     "I am the famous ghost.",
     [(991, "c'est moi le fantôme")], "Corinne reveals her secret identity"),
    ("noemie", "Vous êtes le double d'Isabelle?",
     "Are you Isabelle's double?",
     [(988, "je sais qui vous êtes")], "Noemie realizes who she is"),
    ("lea", "Oui, j'ai fait de mon mieux.",
     "Yes, I did my best.",
     [(992, "fait ce que j'ai pu")], "Corinne explains her modest contribution"),
    ("noemie", "Vous êtes une actrice de théâtre?",
     "Are you a theater actress?",
     [(993, "pas mon métier")], "Noemie asks about her profession"),
    ("lea", "Non, je suis une simple infirmière.",
     "No, I am an ordinary nurse.",
     [(993, "pas mon métier")], "Corinne reveals her true job"),
    ("noemie", "Vous n'êtes pas comédienne professionnelle?",
     "You are not a professional actress?",
     [(993, "pas mon métier")], "Noemie gasps at the revelation"),
    ("lea", "Pas du tout, c'était un dépannage.",
     "Not at all, it was a favor.",
     [(994, "leur rends du service")], "Corinne clarifies the friendly arrangement"),
    ("noemie", "Vous savez qui nous sommes vraiment?",
     "Do you know who we really are?",
     [(988, "je sais qui vous êtes")], "Noemie checks her awareness"),
    ("lea", "Oui, je sais tout maintenant.",
     "Yes, I know everything now.",
     [(1005, "elle savait tout")], "Corinne confirms she understands"),
    ("noemie", "C'est une catastrophe pour l'agence!",
     "This is a disaster for the agency!",
     [(1000, "On a un problème")], "Noemie fears an exposure scandal"),
    ("lea", "Je viens juste pour la fête.",
     "I just came for the party.",
     [(998, "Noémie")], "Corinne reassures her of peaceful intent"),
    ("noemie", "Attendez ici, je cherche Andréa!",
     "Wait here, I am finding Andrea!",
     [(999, "Attends, Andréa")], "Noemie rushes to alert Andrea")
]

WALK = [
    (0, None,
     "'Good evening, I am looking for the organizers.' Corinne arrives at the celebration. "
     "The present verb 'cherche' indicates what she is looking for."),
    (1, None,
     "'Good evening, I am Noemie, assistant.' Noemie politely presents her role at the agency. "
     "The verb 'suis' identifies her name and position."),
    (2, None,
     "'I am the famous ghost.' Corinne refers to her stand-in film role. "
     "The phrase 'c'est moi' emphasizes personal identity."),
    (3, None,
     "'Are you Isabelle's double?' Noemie connects the clues immediately. "
     "The noun 'double' designates an on-screen stand-in."),
    (4, None,
     "'Yes, I did my best.' Corinne describes her earnest effort on the set. "
     "The idiom 'faire de son mieux' means to do one's best."),
    (5, None,
     "'Are you a theater actress?' Noemie inquires about her dramatic training. "
     "The noun 'actrice' specifies a stage performer."),
    (6, None,
     "'No, I am an ordinary nurse.' Corinne reveals her true day job in hospital care. "
     "The feminine noun 'infirmiere' refers to a registered nurse."),
    (7, None,
     "'You are not a professional actress?' Noemie expresses growing astonishment. "
     "The negative structure 'ne... pas' questions her professional status."),
    (8, None,
     "'Not at all, it was a favor.' Corinne clarifies that she helped out as a favor. "
     "The noun 'depannage' colloquially means helping out in a pinch."),
    (9, None,
     "'Do you know who we really are?' Noemie checks how much Corinne understands. "
     "The verb 'savez' questions her awareness of the agency."),
    (10, None,
     "'Yes, I know everything now.' Corinne states that she grasps the whole picture. "
     "The adverb 'maintenant' marks the present state of knowledge."),
    (11, None,
     "'This is a disaster for the agency!' Noemie panics over the high legal stakes. "
     "The noun 'catastrophe' expresses complete institutional panic."),
    (12, None,
     "'I just came for the party.' Corinne clarifies that she has no malicious intent. "
     "The adverb 'juste' restricts her motive to celebration."),
    (13, None,
     "'Wait here, I am finding Andrea!' Noemie rushes off to warn her boss. "
     "The imperative 'attendez' instructs Corinne to stay put.")
]

OUTRO = (
    "Noemie leaves Corinne in the party crowd as panic spreads through ASK. "
    "With the secret double now mingling openly at the anniversary, Andrea will have to act fast. "
    "Now let's listen to the scene one last time in French."
)

CLOSING = ("noemie", "Attendez ici, je cherche Andréa!")
