# Authoring module for dix-pour-cent s03e02 scene 02 (cues 123-197).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-02.py --out out/dix-pour-cent/s03e02/scene-02.json

ID = "dix-pour-cent-s03e02-scene-02"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 2
TITLE = "Un homme normal  (A Normal Man)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Monica", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 123-197. Monica Bellucci tells Gabriel she is weary of being treated as a trophy "
               "and longs to date an ordinary, authentic man. Adapted for A1 French.")

INTRO = ("At the ASK offices, Italian screen icon Monica Bellucci meets with her dedicated agent Gabriel Sarda. "
         "Behind her glamorous public image, Monica confides her fatigue with predatory suitors and yearns to meet an authentic, ordinary companion. "
         "Let's listen to their honest conversation in French first.")

STORY = [
 ("lea", "J'ai adoré tourner ce film en Australie.",
  "I loved shooting this movie in Australia.",
  [(134, "J'ai adoré tourner ces films d'horreur en Australie.")], "Shared international filming joy"),
 ("gabriel", "C'était un rôle très différent pour toi.",
  "It was a very different role for you.",
  [(135, "j'ai sorti quelque chose de différent de moi, tu vois ?")], "Noted acting contrast"),
 ("lea", "Oui, mais ma vie privée est difficile.",
  "Yes, but my private life is difficult.",
  [(196, "mon problème, c'est qu'il n'y a que ce genre de mec qui ose m'approcher.")], "Admitted romantic isolation"),
 ("gabriel", "Une star comme toi a beaucoup d'admirateurs!",
  "A star like you has many admirers!",
  [(196, "qui ose m'approcher.")], "Remarked on widespread admiration"),
 ("lea", "Les hommes me voient seulement comme un trophée.",
  "Men see me only as a trophy.",
  [(194, "C'est pas une femme qu'il cherche."), (195, "C'est un trophée.")], "Criticized superficial suitors"),
 ("gabriel", "Tu intimides peut-être beaucoup de prétendants.",
  "You perhaps intimidate many suitors.",
  [(197, "Les autres, je sais pas, ils se cachent.")], "Suggested suitors are intimidated"),
 ("lea", "Je veux simplement rencontrer un homme normal.",
  "I simply want to meet a normal man.",
  [(194, "C'est pas une femme qu'il cherche.")], "Expressed simple romantic wish"),
 ("gabriel", "Qu'est-ce qu'un homme normal pour toi?",
  "What is a normal man for you?",
  [(194, "C'est pas une femme qu'il cherche.")], "Inquired about definition of normal"),
 ("lea", "Un homme simple, travailleur et attentionné.",
  "A simple, hardworking, and caring man.",
  [(194, "C'est pas une femme qu'il cherche.")], "Listed grounded qualities"),
 ("gabriel", "Un homme qui ne connaît pas le cinéma?",
  "A man who does not know cinema?",
  [(196, "ce genre de mec")], "Pondered outsider to film world"),
 ("lea", "Exactement, quelqu'un qui m'aime pour moi-même.",
  "Exactly, someone who loves me for myself.",
  [(195, "C'est un trophée.")], "Affirmed desire for genuine love"),
 ("gabriel", "Ce genre d'homme existe sûrement à Paris.",
  "That kind of man surely exists in Paris.",
  [(197, "ils se cachent.")], "Encouraged hope in Paris"),
 ("lea", "Alors aide-moi à le trouver, Gabriel!",
  "Then help me find him, Gabriel!",
  [(196, "mon problème")], "Enlisted agent matchmaking help"),
 ("gabriel", "C'est une mission originale pour un agent!",
  "That is an original mission for an agent!",
  [(196, "mon problème")], "Accepted novel challenge"),
]

OPENER = "Let's see how Monica describes her romantic aspirations to Gabriel."

WALK = [
 (0, None,
  "'I loved shooting this movie in Australia.' An enthusiastic past statement recalling international film work."),
 (1, None,
  "'It was a very different role for you.' An appreciative observation noting artistic versatility."),
 (2, None,
  "'Yes, but my private life is difficult.' An adversative transition shifting from career to personal dilemmas."),
 (3, None,
  "'A star like you has many admirers!' A complimentary generalization acknowledging worldwide celebrity appeal."),
 (4, None,
  "'Men see me only as a trophy.' A candid critique describing superficial male attention."),
 (5, None,
  "'You perhaps intimidate many suitors.' An empathetic speculation explaining romantic hesitation."),
 (6, None,
  "'I simply want to meet a normal man.' A straightforward desire formula wishing for grounded romance."),
 (7, None,
  "'What is a normal man for you?' An open interrogative exploring personal definitions of normalcy."),
 (8, None,
  "'A simple, hardworking, and caring man.' Descriptive adjectives highlighting unpretentious human virtues."),
 (9, None,
  "'A man who does not know cinema?' A relative clause probing detachment from show business."),
 (10, None,
  "'Exactly, someone who loves me for myself.' An enthusiastic confirmation desiring unconditional love."),
 (11, None,
  "'That kind of man surely exists in Paris.' An encouraging assertion supporting romantic hope in the capital."),
 (12, None,
  "'Then help me find him, Gabriel!' A playful imperative enlisting agent assistance in love."),
 (13, None,
  "'That is an original mission for an agent!' An amused exclamatory evaluation welcoming an unconventional task."),
]

TRANSITION = "Now let's listen to Monica and Gabriel again at full speed."

OUTRO = ("Monica Bellucci reveals the human vulnerability beneath her cinematic icon status, seeking a grounded romantic partner. "
         "Gabriel takes on the sweet yet unexpected challenge of helping his star client find ordinary happiness.")

CLOSING = ("lea", "Merci pour ton écoute, Gabriel.")
