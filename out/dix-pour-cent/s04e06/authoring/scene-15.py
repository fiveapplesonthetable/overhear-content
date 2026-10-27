# Authoring module for dix-pour-cent s04e06 scene 15 (cues 675-734).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e06/authoring/scene-15.py --out out/dix-pour-cent/s04e06/scene-15.json

ID = "dix-pour-cent-s04e06-scene-15"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 15
TITLE = "Prêt à couler ensemble  (Ready to Sink Together)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jean": "theo"}
LABELS = {"lea": "Andréa", "jean": "Jean"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 675-734. Touched by Andrea's fearless honesty, Jean Reno joyfully commits to starring in Xavier Beauvois's film, "
    "declaring that he is thrilled to sink with ASK just as his character did in The Big Blue."
)

INTRO = (
    "Following Andrea's startling admission that ASK is on the brink of collapse, the office falls silent as they await Jean Reno's verdict. "
    "To their astonishment, the veteran actor responds with infectious enthusiasm, inspired by their passion and uncompromising authenticity. "
    "Let's listen to their exchange in French first."
)

OPENER = "Let's look at Jean Reno's passionate decision to join the project step by step."

STORY = [
    ("lea", "Ça fait du bien de dire la vérité.",
     "It feels good to tell the truth.",
     [(675, "Ça fait du bien de dire la vérité")], "Andrea exhales with relief after coming clean"),
    ("jean", "Absolument, la sincérité est essentielle.",
     "Absolutely, sincerity is essential.",
     [(676, "Absolument")], "Jean warmly agrees with her attitude"),
    ("jean", "Je suis totalement partant pour le film!",
     "I am totally on board for the film!",
     [(677, "Je suis partant")], "Announces his enthusiastic commitment"),
    ("lea", "Vous acceptez malgré tous nos problèmes?",
     "You accept despite all our problems?",
     [(677, "Je suis partant")], "Andrea asks in happy disbelief"),
    ("jean", "Je suis ravi de couler avec vous!",
     "I am delighted to sink with you!",
     [(678, "Je suis ravi de couler avec vous")], "Jean embraces the high-stakes artistic gamble"),
    ("lea", "Votre réaction est incroyable, Jean!",
     "Your reaction is incredible, Jean!",
     [(678, "Je suis ravi de couler avec vous")], "Marvels at his generous spirit"),
    ("jean", "Mon personnage suivait son rêve autrefois.",
     "My character followed his dream in the past.",
     [(680, "Mon personnage suivait son rêve")], "Recalls his iconic cinema role"),
    ("jean", "Il plongeait jusqu'au bout de sa passion.",
     "He dived to the very end of his passion.",
     [(681, "sa passion jusqu'au bout")], "Describes following passion to the limit"),
    ("lea", "Comme dans Le Grand Bleu!",
     "Like in The Big Blue!",
     [(679, "Le Grand Bleu")], "Andrea immediately connects with the reference"),
    ("jean", "Ce nouveau scénario ressemble à cet esprit.",
     "This new script resembles that spirit.",
     [(683, "quelque chose de ça")], "Jean finds the same bold spirit in Beauvois's work"),
    ("lea", "Vous sauvez le projet de Xavier!",
     "You are saving Xavier's project!",
     [(683, "quelque chose de ça")], "Andrea celebrates his game-changing backing"),
    ("jean", "Nous allons créer une œuvre magnifique.",
     "We are going to create a magnificent work.",
     [(683, "quelque chose de ça")], "Jean envisions a memorable cinematic triumph"),
    ("lea", "Merci mille fois pour votre confiance.",
     "Thank you a thousand times for your trust.",
     [(683, "quelque chose de ça")], "Expresses deep gratitude on behalf of ASK"),
    ("jean", "À bientôt pour le tournage, Andréa!",
     "See you soon for filming, Andrea!",
     [(684, "À bientôt")], "Jean says goodbye with a warm smile"),
]

WALK = [
    (0, None,
     "'It feels good to tell the truth.' Andrea reflects on the relief of total honesty."),
    (1, None,
     "'Absolutely, sincerity is essential.' Jean validates that authenticity matters above all."),
    (2, None,
     "'I am totally on board for the film!' Jean commits enthusiastically to the leading role."),
    (3, None,
     "'You accept despite all our problems?' Andrea is stunned by his willingness to take the risk."),
    (4, None,
     "'I am delighted to sink with you!' Jean humorously declares his solidarity with the struggling agency."),
    (5, None,
     "'Your reaction is incredible, Jean!' Andrea expresses her boundless excitement."),
    (6, None,
     "'My character followed his dream in the past.' Jean reminisces about his defining cinematic role."),
    (7, None,
     "'He dived to the very end of his passion.' Jean speaks of uncompromising artistic dedication."),
    (8, None,
     "'Like in The Big Blue!' Andrea references the legendary film that made him a global star."),
    (9, None,
     "'This new script resembles that spirit.' Jean finds an equivalent emotional pull in this screenplay."),
    (10, None,
     "'You are saving Xavier's project!' Andrea celebrates how his involvement rescues the movie."),
    (11, None,
     "'We are going to create a magnificent work.' Jean rallies her with confidence in their joint creative venture."),
    (12, None,
     "'Thank you a thousand times for your trust.' Andrea pours out her profound appreciation."),
    (13, None,
     "'See you soon for filming, Andrea!' Jean concludes their meeting on an uplifting and affectionate note."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Inspired by Andrea's unvarnished truthfulness, Jean Reno signs onto Xavier Beauvois's film, cheerfully agreeing to sink or swim with ASK in the romantic spirit of The Big Blue."
CLOSING = ("jean", "Je suis ravi de couler avec vous!")
