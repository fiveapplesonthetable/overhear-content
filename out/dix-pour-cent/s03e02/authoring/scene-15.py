# Authoring module for dix-pour-cent s03e02 scene 15 (cues 776-794).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-15.py --out out/dix-pour-cent/s03e02/scene-15.json

ID = "dix-pour-cent-s03e02-scene-15"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 15
TITLE = "Un hérisson en boule  (A Curled-Up Hedgehog)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "andrea": "emilie"}
LABELS = {"lea": "Gabriel", "andrea": "Andréa"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 776-794. Continuing his phone call with Andréa from the taxi, Gabriel describes feeling like "
    "a timid hedgehog in front of Monica Bellucci and begs Andréa to let him sleep on her sofa."
)

INTRO = (
    "Still in the taxi, Gabriel continues describing his humiliating panic to Andrea. "
    "Convinced he ruined a golden opportunity with Monica Bellucci, he desperately seeks refuge for the night. "
    "Listen to the conversation in French first."
)

STORY = [
    ("lea", "J'étais comme un hérisson en boule!",
     "I was like a curled-up hedgehog!",
     [(775, "Un petit hérisson en boule, quoi.")], ""),
    ("andrea", "Tu exagères toujours tes émotions, Gabriel.",
     "You always exaggerate your emotions, Gabriel.",
     [(774, "Comme une merde.")], ""),
    ("lea", "Elle est tellement belle et sensuelle.",
     "She is so beautiful and sensual.",
     [(776, "Elle est tellement belle."), (777, "Elle est hypersensuelle.")], ""),
    ("andrea", "C'est une femme magnifique et gentille.",
     "She is a magnificent and kind woman.",
     [(776, "Elle est tellement belle.")], ""),
    ("lea", "J'ai tout gâché avec mes peurs!",
     "I ruined everything with my fears!",
     [(778, "Je te jure, j'ai tout gâché, là.")], ""),
    ("andrea", "Tu paniques pour un simple rendez-vous.",
     "You panic over a simple meeting.",
     [(778, "j'ai tout gâché")], ""),
    ("lea", "J'aurais pu être son homme idéal!",
     "I could have been her ideal man!",
     [(779, "Putain, c'était moi qui lui fallait.")], ""),
    ("andrea", "Où vas-tu dormir cette nuit alors?",
     "Where are you going to sleep tonight then?",
     [(786, "Tu m'ouvres le canapé, hein.")], ""),
    ("lea", "Je ne peux pas rentrer seul.",
     "I cannot go home alone.",
     [(786, "Tu m'ouvres le canapé")], ""),
    ("andrea", "Veux-tu venir chez moi ce soir?",
     "Do you want to come to my place tonight?",
     [(786, "Tu m'ouvres le canapé, hein.")], ""),
    ("lea", "Prépare ton canapé pour moi, Andréa!",
     "Prepare your sofa for me, Andrea!",
     [(786, "Tu m'ouvres le canapé, hein.")], ""),
    ("andrea", "Mon canapé est prêt pour toi.",
     "My sofa is ready for you.",
     [(786, "Tu m'ouvres le canapé, hein.")], ""),
    ("lea", "Merci, mon taxi arrive bientôt là-bas.",
     "Thank you, my taxi is arriving there soon.",
     [(780, "y a votre taxi qui est arrivé, là.")], ""),
    ("andrea", "Repose-toi bien pendant le trajet, Gabriel.",
     "Rest well during the trip, Gabriel.",
     [(787, "Salut.")], "")
]

OPENER = "Let us discover how Gabriel describes his insecurity to Andrea."

WALK = [
    (0, None,
     "'I was like a curled-up hedgehog!' Gabriel uses a self-deprecating animal metaphor. "
     "The preposition comme introduces the vivid comparison."),
    (1, None,
     "'You always exaggerate your emotions, Gabriel.' Andrea gently teases his dramatic nature. "
     "The adverb toujours modifies the verb exagères."),
    (2, None,
     "'She is so beautiful and sensual.' Gabriel recalls Monica's mesmerizing presence. "
     "The adverb tellement intensifies the adjectives."),
    (3, None,
     "'She is a magnificent and kind woman.' Andrea reinforces her admiration. "
     "The feminine adjective magnifique describes high elegance."),
    (4, None,
     "'I ruined everything with my fears!' Gabriel laments his missed chance. "
     "The compound past ai gâché comes from gâcher."),
    (5, None,
     "'You panic over a simple meeting.' Andrea offers a grounded perspective. "
     "The verb paniquer means to panic."),
    (6, None,
     "'I could have been her ideal man!' Gabriel mourns the lost possibility. "
     "The past conditional aurais pu expresses an unfulfilled potential."),
    (7, None,
     "'Where are you going to sleep tonight then?' Andrea inquires about his immediate shelter. "
     "The adverb alors concludes the inquiry."),
    (8, None,
     "'I cannot go home alone.' Gabriel reveals his vulnerability. "
     "The adjective seul expresses solitude."),
    (9, None,
     "'Do you want to come to my place tonight?' Andrea offers her hospitality. "
     "The preposition chez indicates someone's home."),
    (10, None,
     "'Prepare your sofa for me, Andrea!' Gabriel eagerly accepts the invitation. "
     "The imperative prépare addresses a close friend."),
    (11, None,
     "'My sofa is ready for you.' Andrea confirms her warm welcome. "
     "The adjective prêt agrees with the masculine noun canapé."),
    (12, None,
     "'Thank you, my taxi is arriving there soon.' Gabriel watches the street approach. "
     "The adverb bientôt indicates near future arrival."),
    (13, None,
     "'Rest well during the trip, Gabriel.' Andrea closes the late-night call kindly. "
     "The reflexive imperative repose-toi urges relaxation.")
]

TRANSITION = "Now let us listen to the phone conversation once more at normal pace."

OUTRO = (
    "Gabriel finds refuge with his closest friend after a humiliating encounter with a movie star. "
    "Listen to the scene once more in French."
)

CLOSING = ("andrea", "Mon canapé est prêt pour toi.")
