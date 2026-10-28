# Authoring module for dix-pour-cent s04e05 scene 02 (cues 19-55).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e05/authoring/scene-02.py --out out/dix-pour-cent/s04e05/scene-02.json

ID = "dix-pour-cent-s04e05-scene-02"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 2
TITLE = "Arrivée à Paris  (Arrival in Paris)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "sigourney": "emilie"}
LABELS = {"lea": "Camille", "sigourney": "Sigourney"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 19-55. Camille greets Sigourney Weaver at the airport, "
               "who charms her by speaking French and demanding a quick detour to buy Parisian pastries.")

INTRO = ("Stepping in on short notice for an overwhelmed Andrea, Camille arrives at Roissy airport to greet Hollywood star Sigourney Weaver. "
         "The American actress delights Camille by greeting her in fluent French and immediately insisting on a detour to buy delicate Parisian pastries. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("lea", "Bienvenue à Paris, chère madame Weaver!",
     "Welcome to Paris, dear Madame Weaver!",
     [], "new: Camille greets the legendary actress at the arrival terminal"),
    ("sigourney", "Merci beaucoup, je suis ravie d'être ici.",
     "Thank you very much, I am delighted to be here.",
     [], "new: Sigourney warmly accepts the welcome"),
    ("lea", "Oh, mais vous parlez très bien français!",
     "Oh, but you speak French very well!",
     [(25, "Vous parlez français! Super!")], "Camille is pleasantly amazed by Sigourney's fluency"),
    ("sigourney", "J'adore parler français avec vous.",
     "I love speaking French with you.",
     [], "new: Sigourney smiles warmly as they walk to the car"),
    ("lea", "Andréa a un gros problème de nounou.",
     "Andrea has a big nanny problem.",
     [(23, "Elle a un problème de nounou.")], "Camille explains Andrea's unexpected absence"),
    ("sigourney", "Ce n'est pas un problème du tout.",
     "It is not a problem at all.",
     [(24, "Pas de problème.")], "Sigourney graciously dismisses any awkwardness"),
    ("lea", "Elle nous rejoindra directement à l'hôtel.",
     "She will join us directly at the hotel.",
     [(26, "Elle nous rejoindra à l'hôtel.")], "Camille outlines their scheduled meeting place"),
    ("sigourney", "Mais d'abord, j'ai un rendez-vous capital.",
     "But first, I have a vital appointment.",
     [(29, "J'ai un rendez-vous très important.")], "Sigourney announces a mandatory errand"),
    ("lea", "Un rendez-vous avec un grand réalisateur?",
     "An appointment with a great director?",
     [], "new: Camille wonders about a surprise film meeting"),
    ("sigourney", "Non, avec les meilleures pâtisseries parisiennes!",
     "No, with the best Parisian pastries!",
     [], "new: Sigourney laughs and names her culinary craving"),
    ("sigourney", "Je veux goûter toutes les saveurs.",
     "I want to taste every flavor.",
     [(33, "toutes les saveurs.")], "Sigourney scans the colorful pastry counters"),
    ("sigourney", "Des macarons à la fleur d'oranger!",
     "Orange blossom macarons!",
     [(34, "Fleur d'oranger.")], "Sigourney picks her top delicacy"),
    ("sigourney", "C'est ma gourmandise préférée à Paris.",
     "It is my favorite treat in Paris.",
     [(35, "Ma préférée!")], "Sigourney savors the traditional sweet"),
    ("lea", "Vous avez des goûts tout à fait exquis.",
     "You have truly exquisite tastes.",
     [], "new: Camille compliments her client's refined choices"),
]

OPENER = "Let's explore Camille and Sigourney's charming first encounter line by line."

WALK = [
    (0, None,
     "'Welcome to Paris, dear Madame Weaver!' Camille extends a warm French greeting to the distinguished Hollywood visitor. The adjective meaning 'dear' takes its feminine form here to match the noun it describes."),
    (1, None,
     "'Thank you very much, I am delighted to be here.' Sigourney expresses genuine happiness at returning to Paris. The clause hinges on the everyday verb meaning 'to be'."),
    (2, None,
     "'Oh, but you speak French very well!' Camille reacts with delightful surprise to the star's flawless accent. Camille uses the polite 'you' form alongside 'speak' to keep a respectful professional tone."),
    (3, None,
     "'I love speaking French with you.' Sigourney shares her long-standing affection for the French language and culture. The clause hinges on the everyday verb meaning 'love'."),
    (4, None,
     "'Andrea has a big nanny problem.' Camille politely excuses her agency director's unexpected morning absence. The descriptive adjective for 'big' agrees in gender and number with its noun."),
    (5, None,
     "'It is not a problem at all.' Sigourney displays total understanding and generosity toward working mothers. The key noun here means 'problem', anchored by its matching French article."),
    (6, None,
     "'She will join us directly at the hotel.' Camille coordinates the arrival plan at the prestigious Hotel de Crillon. The verb meaning 'will join' pairs naturally with the noun for 'hotel' in everyday conversation."),
    (7, None,
     "'But first, I have a vital appointment.' Sigourney playfully teases an essential stop before hotel check-in. The descriptive adjective for 'vital' agrees in gender and number with its noun."),
    (8, None,
     "'An appointment with a great director?' Camille wonders whether an unannounced filmmaker has summoned the actress. The descriptive adjective for 'great' agrees in gender and number with its noun."),
    (9, None,
     "'No, with the best Parisian pastries!' Sigourney reveals that sampling authentic French baked sweets is her top priority. The key noun here means 'pastries', anchored by its matching French article."),
    (10, None,
     "'I want to taste every flavor.' Sigourney inspects the vibrant vitrine filled with rainbow macarons. The verb meaning 'want' pairs naturally with the noun for 'flavors' in everyday conversation."),
    (11, None,
     "'Orange blossom macarons!' Sigourney specifically asks for orders her cherished floral-infused delicacy. The key noun here means 'macarons', anchored by its matching French article."),
    (12, None,
     "'It is my favorite treat in Paris.' Sigourney admits that traditional confectioneries remain her biggest weakness. The adjective meaning 'favorite' takes its feminine form here to match the noun it describes."),
    (13, None,
     "'You have truly exquisite tastes.' Camille happily escorts the satisfied star back toward the waiting car. The descriptive adjective for 'exquisite' agrees in gender and number with its noun."),
]

TRANSITION = "Now let's listen to Camille and Sigourney's exchange once more from start to finish."

OUTRO = ("Sigourney Weaver wins over Camille with her effortless charm, fluent French, and passion for Parisian pastries. "
         "Let's review the key vocabulary of travel, hospitality, and pastry delicacies from this scene.")

CLOSING = ("lea", "La star est absolument charmante.")
