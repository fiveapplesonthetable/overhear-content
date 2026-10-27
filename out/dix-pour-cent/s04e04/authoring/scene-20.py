# Authoring module for dix-pour-cent s04e04 scene 20 (cues 1144-1149).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e04/authoring/scene-20.py --out out/dix-pour-cent/s04e04/scene-20.json

ID = "dix-pour-cent-s04e04-scene-20"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 20
TITLE = "L'échappée en trottinette  (The Scooter Escape)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sandrine", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1144-1149. While waiting for a taxi after her disastrous comedy gig, Sandrine spots an electric scooter "
    "on the street. Despite Gabriel's frantic protests about danger and lack of a helmet, she speeds away into the Parisian night."
)

INTRO = (
    "On the sidewalk outside the comedy club, Gabriel tries to hail a taxi to take his stressed actress home. "
    "Instead, Sandrine spots a parked electric scooter and decides to make a reckless midnight getaway through the streets of Paris. "
    "Let's listen to their chaotic exchange in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("gabriel", "Le taxi arrive dans deux minutes.",
     "The taxi is arriving in two minutes.",
     [(1142, "je vais t'en commander un")], "Announced the incoming ride"),
    ("lea", "Regarde ces trottinettes électriques là-bas!",
     "Look at those electric scooters over there!",
     [(1145, "elles sont incroyables")], "Spotted an unexpected alternative transport"),
    ("gabriel", "Ne t'approche pas de ces engins.",
     "Do not go near those contraptions.",
     [(1147, "Non, non, non")], "Warned her away from the vehicles"),
    ("lea", "Elles ont l'air tellement amusantes!",
     "They look so much fun!",
     [(1145, "elles sont incroyables")], "Marveled at the scooters"),
    ("gabriel", "C'est bien trop dangereux la nuit.",
     "It is far too dangerous at night.",
     [(1148, "Sandrine !")], "Argued against nighttime riding"),
    ("lea", "C'est le moyen parfait pour rentrer.",
     "It is the perfect way to get home.",
     [(1144, "Tu rentres ?")], "Justified her impulsive travel choice"),
    ("gabriel", "Tu n'as même pas de casque!",
     "You do not even have a helmet!",
     [(1147, "Non, non, non")], "Pointed out the glaring safety violation"),
    ("lea", "Je sais parfaitement conduire ce soir.",
     "I know how to drive perfectly tonight.",
     [(1146, "Attends, Gabriel")], "Brushed off his safety warnings"),
    ("gabriel", "S'il te plaît, monte dans la voiture.",
     "Please get into the car.",
     [(1142, "Je vais t'en commander un")], "Urged her to stick to the planned taxi"),
    ("lea", "Je veux sentir le vent frais.",
     "I want to feel the fresh wind.",
     [(1145, "elles sont incroyables")], "Longed for breezy freedom"),
    ("gabriel", "Sandrine, descends immédiatement de là!",
     "Sandrine, get down from there immediately!",
     [(1148, "Sandrine !")], "Ordered her off the footboard"),
    ("lea", "Attrape-moi si tu peux, mon cher!",
     "Catch me if you can, my dear!",
     [(1149, "Non !")], "Teased him playfully as she accelerated"),
    ("gabriel", "Non, non, non, reviens ici!",
     "No, no, no, come back here!",
     [(1148, "Non, non, non… Allez… Sandrine !"), (1149, "Non !")], "Shouted after her down the avenue"),
    ("lea", "À demain matin à l'agence!",
     "See you tomorrow morning at the agency!",
     [(1144, "Tu rentres ?")], "Waved goodbye as she vanished into traffic"),
]

WALK = [
    (0, None,
     "'The taxi is arriving in two minutes.' Gabriel checks his phone for the car's arrival. "
     "The present tense with dans deux minutes signals an imminent arrival."),
    (1, None,
     "'Look at those electric scooters over there!' Sandrine's eyes light up with sudden mischief. "
     "The imperative verb regarde directs attention across the street."),
    (2, None,
     "'Do not go near those contraptions.' Gabriel immediately senses trouble. "
     "The negative imperative ne t'approche pas forbids reckless behavior."),
    (3, None,
     "'They look so much fun!' Sandrine steps toward the parked two-wheelers. "
     "The idiomatic phrase ont l'air describes their appealing appearance."),
    (4, None,
     "'It is far too dangerous at night.' Gabriel pleads with common sense. "
     "The adverbial expression bien trop dangereux emphasizes the severe risk."),
    (5, None,
     "'It is the perfect way to get home.' Sandrine unlocks a scooter with her smartphone. "
     "The noun phrase le moyen parfait declares her mind made up."),
    (6, None,
     "'You do not even have a helmet!' Gabriel highlights the total lack of protection. "
     "The adverb même intensifies the safety hazard."),
    (7, None,
     "'I know how to drive perfectly tonight.' Sandrine steps confidently onto the platform. "
     "The adverb parfaitement conveys bold self-assurance."),
    (8, None,
     "'Please get into the car.' Gabriel gestures toward the approaching cab. "
     "The polite imperative monte dans la voiture urges compliance."),
    (9, None,
     "'I want to feel the fresh wind.' Sandrine savors the evening breeze on her face. "
     "The sensory verb phrase sentir le vent frais expresses joyful abandon."),
    (10, None,
     "'Sandrine, get down from there immediately!' Gabriel rushes forward to grab the handlebars. "
     "The urgent imperative descends immédiatement demands immediate obedience."),
    (11, None,
     "'Catch me if you can, my dear!' Sandrine squeezes the throttle and glides away. "
     "The playful challenge attrape-moi si tu peux mocks his desperate sprint."),
    (12, None,
     "'No, no, no, come back here!' Gabriel shouts as he watches her zip down the boulevard. "
     "The repeated negative particle non conveys total helplessness."),
    (13, None,
     "'See you tomorrow morning at the agency!' Sandrine's voice echoes down the dark Parisian street. "
     "The farewell formula à demain matin cheerful concludes her nocturnal escape."),
]

OUTRO = "Gabriel watches Sandrine disappear down the avenue on her scooter, shaking his head in amused disbelief."
CLOSING = ("lea", "À demain matin à l'agence!")
