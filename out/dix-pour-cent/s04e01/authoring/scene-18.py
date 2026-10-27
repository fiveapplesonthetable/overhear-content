# Authoring module for dix-pour-cent s04e01 scene 18 (cues 890-897).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-18.py --out out/dix-pour-cent/s04e01/scene-18.json

ID = "dix-pour-cent-s04e01-scene-18"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 18
TITLE = "Sur le tapis rouge  (On the Red Carpet)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mimie": "emilie", "gabriel": "theo"}
LABELS = {"lea": "Charlotte", "mimie": "Mimie", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 890-897. At the Césars ceremony, Charlotte Gainsbourg graciously invites Mimie Mathy onto the red carpet "
    "for the photocall, while Gabriel proudly steps aside to let them shine together."
)

INTRO = (
    "At the prestigious Cesars ceremony, Charlotte Gainsbourg warmly invites Mimie Mathy onto the red carpet. "
    "As photographers clamor for photos, Gabriel steps aside so that the two actresses can share the glamorous spotlight. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Mimie, viens faire des photos avec moi!",
     "Mimie, come take photos with me!",
     [(894, "Viens avec moi")], "Charlotte calls Mimie to join her"),
    ("mimie", "Tu es vraiment sûre, Charlotte?",
     "Are you really sure, Charlotte?",
     [(895, "Bien sûr")], "Mimie checks her generous invitation"),
    ("lea", "Bien sûr, nous formons une équipe.",
     "Of course, we are a team.",
     [(894, "soit vues ensemble")], "Charlotte emphasizes solidarity"),
    ("gabriel", "Les photographes attendent votre arrivée!",
     "The photographers are waiting for your arrival!",
     [(891, "Par ici")], "Gabriel notes the media excitement"),
    ("mimie", "C'est un moment magique pour moi.",
     "It is a magical moment for me.",
     [(890, "drôle de sensation")], "Mimie shares her joyful wonder"),
    ("lea", "Tu mérites toute cette belle attention.",
     "You deserve all this fine attention.",
     [(890, "croit en moi")], "Charlotte validates her talent"),
    ("gabriel", "Je vous laisse briller ensemble!",
     "I leave you to shine together!",
     [(897, "Je vous laisse")], "Gabriel gives them center stage"),
    ("lea", "Regarde vers les caméras, Mimie.",
     "Look toward the cameras, Mimie.",
     [(894, "photocall")], "Charlotte guides her on the carpet"),
    ("mimie", "Je n'ai pas l'habitude de ça.",
     "I am not used to this.",
     [(890, "n'ai pas l'habitude")], "Mimie admits her modest modesty"),
    ("lea", "Souris, tu es magnifique ce soir!",
     "Smile, you are stunning tonight!",
     [(896, "Salut, Mimie")], "Charlotte boosts her confidence"),
    ("gabriel", "Cette montée des marches est superbe.",
     "This red carpet arrival is superb.",
     [(888, "le tapis rouge")], "Gabriel watches proudly"),
    ("mimie", "Merci mille fois pour ce geste.",
     "Thank you a thousand times for this gesture.",
     [(893, "Merci")], "Mimie expresses deep gratitude"),
    ("lea", "Le cinéma adore ta belle énergie.",
     "Cinema loves your wonderful energy.",
     [(889, "aux Césars")], "Charlotte compliments her warmth"),
    ("gabriel", "Profitez pleinement de votre grand succès!",
     "Enjoy your great success to the fullest!",
     [(897, "Je vous laisse")], "Gabriel celebrates their triumph")
]

WALK = [
    (0, None,
     "'Mimie, come take photos with me!' Charlotte welcomes Mimie warmly onto the red carpet. "
     "The imperative 'viens faire' invites someone to participate."),
    (1, None,
     "'Are you really sure, Charlotte?' Mimie asks with humble disbelief. "
     "The adjective 'sure' checks for certainty."),
    (2, None,
     "'Of course, we are a team.' Charlotte reaffirms their mutual respect. "
     "The noun 'equipe' conveys shared solidarity."),
    (3, None,
     "'The photographers are waiting for your arrival!' Gabriel points toward the flashing cameras. "
     "The present verb 'attendent' describes the waiting media press."),
    (4, None,
     "'It is a magical moment for me.' Mimie takes in the glamorous setting. "
     "The adjective 'magique' highlights an enchanting experience."),
    (5, None,
     "'You deserve all this fine attention.' Charlotte praises Mimie's artistic achievements. "
     "The verb 'merites' denotes rightful earning of honor."),
    (6, None,
     "'I leave you to shine together!' Gabriel steps back to give them full visibility. "
     "The verbal idiom 'je vous laisse' politely excuses oneself."),
    (7, None,
     "'Look toward the cameras, Mimie.' Charlotte shares helpful tips for the photocall. "
     "The preposition 'vers' indicates direction toward an object."),
    (8, None,
     "'I am not used to this.' Mimie reflects on the rare burst of gala spotlight. "
     "The verbal phrase 'avoir l'habitude de' means to be accustomed to."),
    (9, None,
     "'Smile, you are stunning tonight!' Charlotte reassures her co-star with enthusiasm. "
     "The imperative 'souris' offers encouragement before the flashing lenses."),
    (10, None,
     "'This red carpet arrival is superb.' Gabriel admires their shared public grace. "
     "The noun phrase 'montee des marches' refers to the iconic red carpet procession."),
    (11, None,
     "'Thank you a thousand times for this gesture.' Mimie thanks Charlotte for sharing the limelight. "
     "The expression 'merci mille fois' conveys heartfelt thanks."),
    (12, None,
     "'Cinema loves your wonderful energy.' Charlotte celebrates Mimie's enduring popular appeal. "
     "The feminine noun 'energie' commends vitality and spirit."),
    (13, None,
     "'Enjoy your great success to the fullest!' Gabriel encourages both actresses to relish the glory. "
     "The adverb 'pleinement' means fully or to the maximum.")
]

OUTRO = (
    "With generous warmth, Charlotte Gainsbourg and Mimie Mathy turn the red carpet into a moment of pure solidarity. "
    "Watching from the sidelines, Gabriel knows ASK has achieved a memorable public triumph. "
    "Now let's listen to the scene one last time in French."
)

CLOSING = ("gabriel", "Profitez pleinement de votre grand succès!")
