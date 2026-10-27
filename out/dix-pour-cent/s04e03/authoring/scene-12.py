# Authoring module for dix-pour-cent s04e03 scene 12 (cues 523-527).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e03/authoring/scene-12.py --out overhear-content/out/dix-pour-cent/s04e03/scene-12.json

ID = "dix-pour-cent-s04e03-scene-12"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 12
TITLE = "La fin de la séance  (The End of the Shoot)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "camille": "emilie"}
LABELS = {"lea": "Sofia", "camille": "Camille"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 523-527. After an intense photo session, Sofia finishes her shoot and warmly thanks "
    "the studio crew. Camille commends her energy and professionalism, reassuring her that "
    "her talent speaks for itself."
)

INTRO = (
    "Sofia has just wrapped up her intense photoshoot at the studio. "
    "Pleased with the result, she steps off the set to thank the team and debrief with Camille. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Voilà, nous avons enfin terminé!",
     "There, we have finally finished!",
     [(523, "Là c'est mieux"), (525, "Voilà")], "Sofia wraps up her photoshoot"),
    ("camille", "C'était vraiment une séance formidable.",
     "It was truly a wonderful session.",
     [(524, "super")], "Camille praises the shoot"),
    ("lea", "Merci à toute l'équipe du studio!",
     "Thanks to the entire studio team!",
     [(527, "Merci")], "Sofia thanks the crew"),
    ("camille", "Le photographe a adoré ton énergie.",
     "The photographer loved your energy.",
     [(524, "super")], "Camille notes the photographer's praise"),
    ("lea", "Pardon pour mon retard au début.",
     "Sorry for my delay at the beginning.",
     [(526, "Oh, pardon")], "Sofia apologizes for starting late"),
    ("camille", "Ne t'inquiète pas pour ça.",
     "Do not worry about that.",
     [(526, "pardon")], "Camille brushes off the apology"),
    ("camille", "Tu as été très professionnelle aujourd'hui.",
     "You were very professional today.",
     [(524, "super")], "Camille compliments her conduct"),
    ("lea", "Tu crois que les photos sont belles?",
     "Do you think the photos are beautiful?",
     [(523, "Là c'est mieux")], "Sofia seeks reassurance"),
    ("camille", "Elles sont magnifiques, crois-moi.",
     "They are gorgeous, believe me.",
     [(524, "super")], "Camille reassures her client"),
    ("lea", "C'est grâce à ton soutien précieux.",
     "It is thanks to your valuable support.",
     [(527, "Merci")], "Sofia thanks her agent"),
    ("camille", "Je suis très fière de toi.",
     "I am very proud of you.",
     [(524, "super")], "Camille expresses pride"),
    ("lea", "Maintenant, nous pouvons prendre un café?",
     "Now, can we have a coffee?",
     [(527, "Merci")], "Sofia suggests a coffee break"),
    ("camille", "Oui, allons fêter cette belle journée!",
     "Yes, let's go celebrate this fine day!",
     [(524, "super")], "Camille happily agrees"),
    ("lea", "Je me sens enfin tranquille aujourd'hui.",
     "I feel peaceful at last today.",
     [(525, "Voilà")], "Sofia feels relieved and confident"),
]

WALK = [
    (0, None,
     "'There, we have finally finished!' Sofia breathes a sigh of relief as the photoshoot concludes. "
     "The adverb 'enfin' marks the completion of an effort."),
    (1, None,
     "'It was truly a wonderful session.' Camille applauds Sofia's performance in front of the lens. "
     "The adjective 'formidable' expresses high appreciation."),
    (2, None,
     "'Thanks to the entire studio team!' Sofia graciously acknowledges the stylists and technicians. "
     "The feminine noun 'equipe' refers to a work crew or team."),
    (3, None,
     "'The photographer loved your energy.' Camille shares the glowing feedback from the camera operator. "
     "The past tense 'a adore' conveys strong enthusiasm."),
    (4, None,
     "'Sorry for my delay at the beginning.' Sofia offers a polite apology for her hesitation earlier. "
     "The masculine noun 'retard' designates lateness or delay."),
    (5, None,
     "'Do not worry about that.' Camille tells her that minor bumps do not matter in the end. "
     "The pronominal verb 's'inquieter' is negated in the imperative."),
    (6, None,
     "'You were very professional today.' Camille commends Sofia's poised demeanor throughout the shoot. "
     "The feminine adjective 'professionnelle' describes expert conduct."),
    (7, None,
     "'Do you think the photos are beautiful?' Sofia seeks reassurance about the final portraits. "
     "The verb 'croire' asks for Camille's opinion."),
    (8, None,
     "'They are gorgeous, believe me.' Camille guarantees that the photographic images look stunning. "
     "The imperative 'crois-moi' invites total trust."),
    (9, None,
     "'It is thanks to your valuable support.' Sofia credits Camille for giving her emotional backing. "
     "The prepositional phrase 'grace a' means thanks to."),
    (10, None,
     "'I am very proud of you.' Camille expresses sincere pride in her client's growth and talent. "
     "The adjective 'fiere' is the feminine form of proud."),
    (11, None,
     "'Now, can we have a coffee?' Sofia proposes a quiet moment away from studio lights. "
     "The verb 'prendre' is commonly used for ordering or consuming a drink."),
    (12, None,
     "'Yes, let's go celebrate this fine day!' Camille enthusiastically welcomes the idea of a break. "
     "The verb 'feter' means to celebrate an accomplishment."),
    (13, None,
     "'I feel peaceful at last today.' Sofia leaves behind her rivalry and feels confident in her career. "
     "The adjective 'tranquille' conveys calm peace of mind."),
]

OUTRO = (
    "With the studio photoshoot successfully completed, Sofia and Camille head out together in high spirits. "
    "Sofia feels validated in her craft, knowing she can stand proudly on her own merits. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Merci pour tout, Camille!")
