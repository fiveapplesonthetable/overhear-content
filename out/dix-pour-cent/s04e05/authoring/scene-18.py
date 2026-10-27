# Authoring module for dix-pour-cent s04e05 scene 18 (cue 743).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e05/authoring/scene-18.py --out overhear-content/out/dix-pour-cent/s04e05/scene-18.json

ID = "dix-pour-cent-s04e05-scene-18"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 18
TITLE = "La passerelle Debilly  (The Debilly Footbridge)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "vendeur": "theo"}
LABELS = {"lea": "Sigourney", "vendeur": "Le vendeur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cue 743. Sigourney Weaver strolls along the Debilly footbridge overlooking the Eiffel Tower, admiring the "
    "Parisian skyline and stopping to buy a miniature souvenir before her secret rendezvous."
)

INTRO = (
    "Sigourney Weaver takes a walk across the famous Debilly footbridge in Paris with the Eiffel Tower behind her. "
    "While waiting for her secret meeting, she stops to chat with a souvenir seller on the bridge. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Voici la passerelle Debilly à Paris.",
     "Here is the Debilly footbridge in Paris.",
     [(743, "DEBILY")], "Sigourney arrives at the footbridge"),
    ("lea", "Quelle vue magnifique sur la Seine!",
     "What a magnificent view over the Seine!",
     [], "Sigourney admires the river"),
    ("vendeur", "Bonjour madame! Regardez mes beaux souvenirs!",
     "Hello ma'am! Look at my beautiful souvenirs!",
     [], "A street vendor greets her"),
    ("lea", "Bonjour! Vous avez des tours Eiffel?",
     "Hello! Do you have Eiffel Towers?",
     [], "Sigourney looks at his display"),
    ("vendeur", "Oui, j'ai des petites miniatures.",
     "Yes, I have small miniatures.",
     [], "The vendor shows her the models"),
    ("lea", "Elles sont vraiment très mignonnes!",
     "They are really very cute!",
     [], "Sigourney smiles with delight"),
    ("vendeur", "Laquelle préférez-vous? La dorée?",
     "Which one do you prefer? The golden one?",
     [], "The vendor holds up a golden model"),
    ("lea", "Oui, je prends cette petite tour.",
     "Yes, I will take this little tower.",
     [], "Sigourney chooses the golden souvenir"),
    ("vendeur", "C'est cinq euros, s'il vous plaît.",
     "It is five euros, please.",
     [], "The vendor states the price"),
    ("lea", "Tenez, voici un billet de dix.",
     "Here, take a ten-euro bill.",
     [], "Sigourney hands him the money"),
    ("vendeur", "Merci beaucoup! Vous attendez quelqu'un?",
     "Thank you very much! Are you waiting for someone?",
     [], "The vendor gives her the change"),
    ("lea", "Oui, j'ai un rendez-vous secret.",
     "Yes, I have a secret meeting.",
     [], "Sigourney glances down the bridge"),
    ("vendeur", "Attention aux photographes sur le pont!",
     "Watch out for photographers on the bridge!",
     [], "The vendor warns her kindly"),
    ("lea", "Merci! Ah, le voilà qui arrive!",
     "Thank you! Ah, here he comes!",
     [], "Sigourney spots her guest approaching"),
]

WALK = [
    (0, None,
     "'Here is the Debilly footbridge in Paris.' Sigourney walks onto the pedestrian bridge over the river. "
     "The noun 'passerelle' denotes a footbridge or walkway."),
    (1, None,
     "'What a magnificent view over the Seine!' Sigourney admires the iconic Parisian panorama. "
     "The exclamative adjective 'quelle' introduces the feminine noun 'vue'."),
    (2, None,
     "'Hello ma'am! Look at my beautiful souvenirs!' A street vendor invites her to browse his items. "
     "The imperative 'regardez' means look at."),
    (3, None,
     "'Hello! Do you have Eiffel Towers?' Sigourney asks about miniature models of the monument. "
     "The question 'vous avez' asks do you have."),
    (4, None,
     "'Yes, I have small miniatures.' The seller displays his collection of tiny replicas. "
     "The noun 'miniatures' refers to small scale models."),
    (5, None,
     "'They are really very cute!' Sigourney is charmed by the little trinkets. "
     "The feminine plural adjective 'mignonnes' means cute or lovely."),
    (6, None,
     "'Which one do you prefer? The golden one?' The seller offers her a shiny gold version. "
     "The interrogative pronoun 'laquelle' means which one."),
    (7, None,
     "'Yes, I will take this little tower.' Sigourney makes her selection from the stand. "
     "The present tense 'je prends' is used to state a purchase choice."),
    (8, None,
     "'It is five euros, please.' The vendor tells her the cost of the souvenir. "
     "The polite phrase 's'il vous plait' means please."),
    (9, None,
     "'Here, take a ten-euro bill.' Sigourney hands over a banknote to pay. "
     "The imperative 'tenez' is used when handing something to someone."),
    (10, None,
     "'Thank you very much! Are you waiting for someone?' The vendor notices her looking down the walkway. "
     "The indefinite pronoun 'quelqu'un' means someone."),
    (11, None,
     "'Yes, I have a secret meeting.' Sigourney shares that she is meeting a mystery companion. "
     "The noun 'rendez-vous' means an appointment or meeting."),
    (12, None,
     "'Watch out for photographers on the bridge!' The seller points out paparazzi hiding nearby. "
     "The warning 'attention a' means watch out for."),
    (13, None,
     "'Thank you! Ah, here he comes!' Sigourney waves as her companion walks onto the bridge. "
     "The expression 'le voila' means there he is."),
]

OUTRO = (
    "Holding her new miniature Eiffel Tower, Sigourney walks forward to greet her guest on the bridge. "
    "Little does she know that hidden photographers are already snapping pictures of the meeting. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("vendeur", "Bonne journée à Paris!")
