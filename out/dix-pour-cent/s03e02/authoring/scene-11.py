# Authoring module for dix-pour-cent s03e02 scene 11 (cues 621-677).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e02/authoring/scene-11.py --out overhear-content/out/dix-pour-cent/s03e02/scene-11.json

ID = "dix-pour-cent-s03e02-scene-11"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 11
TITLE = "L'invitation au dîner  (The Dinner Invitation)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 621-677. In the ASK agency offices, Hicham notices Andrea's stress and jaw tension, "
    "inviting Andrea and Colette to dinner to propose updating their coparenting pact."
)

INTRO = (
    "Noticing that Andrea is clenching her teeth from physical stress, agency boss Hicham invites her and Colette to a gastronomic dinner. "
    "He reveals that he wants to revisit their coparenting agreement before the baby is born. "
    "Listen to the scene in French first."
)

STORY = [
    ("hicham", "Tes problèmes de stress ne s'arrangent pas.",
     "Your stress problems are not getting better.",
     [(621, "problèmes de bruxisme")], ""),
    ("lea", "De quoi tu te mêles, Hicham?",
     "What business is it of yours, Hicham?",
     [(626, "de quoi je me mêle")], ""),
    ("hicham", "Je vous invite à dîner ce soir.",
     "I am inviting you to dinner tonight.",
     [(629, "invite à dîner ce soir")], ""),
    ("lea", "Pourquoi organiser un dîner ce soir?",
     "Why organize a dinner tonight?",
     [(630, "Ce soir"), (634, "Pourquoi ce soir")], ""),
    ("hicham", "Je réserve une table à vingt heures.",
     "I am reserving a table at eight o'clock.",
     [(632, "Je réserve")], ""),
    ("lea", "Qu'est-ce qui se passe, exactement?",
     "What is going on, exactly?",
     [(635, "Qu'est-ce qui se passe")], ""),
    ("lea", "Il y a un problème particulier?",
     "Is there a particular problem?",
     [(636, "Y a un problème")], ""),
    ("hicham", "Non, non, il n'y a aucun problème.",
     "No, no, there is no problem at all.",
     [(637, "Non, non, aucun")], ""),
    ("hicham", "J'ai envie de bien manger, c'est tout.",
     "I just feel like eating well, that is all.",
     [(638, "J'ai envie de bien manger")], ""),
    ("hicham", "On va réviser notre pacte parental.",
     "We are going to revise our parental pact.",
     [(640, "réviser notre pacte")], ""),
    ("lea", "Quoi? Non, notre pacte est parfait!",
     "What? No, our pact is perfect!",
     [(641, "Quoi")], ""),
    ("hicham", "Il lui faut une petite mise à jour.",
     "It just needs a small update.",
     [(644, "mise à jour")], ""),
    ("hicham", "Je compte vraiment sur vous deux.",
     "I am really counting on you two.",
     [(645, "Je compte sur vous")], ""),
    ("lea", "Colette et moi serons là ce soir.",
     "Colette and I will be there tonight.",
     [(629, "Colette"), (645, "sur vous")], ""),
    ("hicham", "Parfait, nous allons bien dîner ensemble!",
     "Perfect, we are going to dine well together!",
     [(638, "bien manger"), (645, "sur vous")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Your stress problems are not getting better.' Hicham comments on Andrea's physical strain. "
     "The negative pronominal verb indicates ongoing symptoms."),
    (1, None,
     "'What business is it of yours, Hicham?' Andrea sharply rejects his unsolicited advice. "
     "The idiomatic reflexive construction expresses boundary defense."),
    (2, None,
     "'I am inviting you to dinner tonight.' Hicham extends a sudden dinner invitation. "
     "The present tense verb announces his plans."),
    (3, None,
     "'Why organize a dinner tonight?' Andrea suspects a hidden motive behind his proposal. "
     "The interrogative adverb questions his sudden timing."),
    (4, None,
     "'I am reserving a table at eight o'clock.' He insists on making the restaurant booking. "
     "The transitive verb specifies the evening schedule."),
    (5, None,
     "'What is going on, exactly?' Andrea presses him for immediate clarification. "
     "The common question phrase demands direct truth."),
    (6, None,
     "'Is there a particular problem?' She checks if an agency crisis has erupted. "
     "The existential structure queries possible trouble."),
    (7, None,
     "'No, no, there is no problem at all.' Hicham reassures her of his peaceful intentions. "
     "The negative determiner emphasizes total calm."),
    (8, None,
     "'I just feel like eating well, that is all.' He offers a lighthearted superficial excuse. "
     "The verbal idiom expresses casual desire."),
    (9, None,
     "'We are going to revise our parental pact.' Hicham reveals the true purpose of the dinner. "
     "The near future construction introduces important legal discussions."),
    (10, None,
     "'What? No, our pact is perfect!' Andrea opposes renegotiating their signed terms. "
     "The exclamation and adjective affirm complete satisfaction."),
    (11, None,
     "'It just needs a small update.' He downplays the scope of the proposed amendments. "
     "The impersonal verbal idiom conveys modest necessity."),
    (12, None,
     "'I am really counting on you two.' Hicham urges both expectant mothers to attend. "
     "The prepositional verb emphasizes personal reliance."),
    (13, None,
     "'Colette and I will be there tonight.' Andrea accepts the dinner invitation reluctantly. "
     "The future verb confirms their scheduled presence."),
    (14, None,
     "'Perfect, we are going to dine well together!' Hicham looks forward to their evening gathering. "
     "The near future verb highlights shared dining.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Determined to alter the parental agreement before the birth, Hicham arranges a fateful restaurant dinner with Andrea and Colette. "
    "Listen to the conversation once more in French."
)

CLOSING = ("lea", "Je n'aime pas du tout cette idée.")
