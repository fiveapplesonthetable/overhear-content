# Authoring module for dix-pour-cent s02e01 scene 21 (cues 641-660).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-21.py --out out/dix-pour-cent/s02e01/scene-21.json

ID = "dix-pour-cent-s02e01-scene-21"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 21
TITLE = "Virginie demande l'asile  (Virginie Asks for Asylum)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Virginie", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 641-660. Virginie Efira rushes into Gabriel's office at ASK, completely overwhelmed. "
    "Paparazzi are camped outside her sister's flat, so she desperately begs Gabriel to shelter her for a couple of days."
)

INTRO = (
    "Hounded by paparazzi who are camped outside her sister's apartment, actress Virginie Efira bursts into the agency. "
    "Desperate for peace and safety, she begs Gabriel to let her sleep at his place for a couple of nights. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "Je suis chez ma sœur, c'est l'horreur!",
     "I am at my sister's, it is horrible!",
     [(641, "Je suis chez ma sœur, c'est l'horreur !")], ""),
    ("lea", "Les paparazzi sont devant l'immeuble.",
     "The paparazzi are in front of the building.",
     [(642, "Les paparazzi sont campés dans l'immeuble d'en face")], ""),
    ("lea", "Ils attendent les enfants à l'école.",
     "They wait for the kids at school.",
     [(643, "Ils ont chopé les enfants à la sortie de l'école")], ""),
    ("lea", "En plus, son copain me regarde bizarrement.",
     "Plus, her boyfriend looks at me strangely.",
     [(644, "En plus son copain me lance des drôles de regards")], ""),
    ("gabriel", "Comment ça? Des regards de jugement?",
     "How so? Judgmental looks?",
     [(645, "Comment ça ? Des regards de jugement ?")], ""),
    ("lea", "Non, il me regarde trop. Je deviens parano.",
     "No, he stares at me too much. I am getting paranoid.",
     [(646, "Non, il me mate"), (647, "je suis devenue super parano")], "Cleaned colloquial phrasing"),
    ("lea", "Ma sœur est complètement bouleversée.",
     "My sister is completely overwhelmed.",
     [(648, "Ma sœur est effondrée")], ""),
    ("lea", "Je ne peux pas rester là-bas.",
     "I cannot stay over there.",
     [(650, "Je peux pas rester là")], ""),
    ("lea", "Je peux dormir chez toi deux nuits?",
     "Can I sleep at your place for two nights?",
     [(651, "Je peux dormir chez toi une nuit ou deux ?")], ""),
    ("gabriel", "Mon appartement est en plein travaux.",
     "My apartment is under renovation.",
     [(654, "Mon appartement est en travaux")], ""),
    ("lea", "Ça ne me dérange pas du tout.",
     "That does not bother me at all.",
     [(655, "Ça me dérange pas du tout")], ""),
    ("lea", "J'ai juste besoin d'un coin tranquille.",
     "I just need a quiet spot.",
     [(656, "j'ai juste besoin d'un placard tranquille")], ""),
    ("gabriel", "Qu'est-ce que tu veux dire par mon code?",
     "What do you mean by my door code?",
     [(657, "C'est quoi ton code ?"), (658, "Qu'est-ce que tu veux dire, mon code ?")], ""),
    ("lea", "J'ai juste un pyjama et des mouchoirs. Merci!",
     "I just have pajamas and tissues. Thank you!",
     [(659, "j'ai juste amené un pyjama et des kleenex"), (660, "Merci")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'I am at my sister's, it is horrible!' Virginie begins by explaining her awful living situation. "
     "The preposition chez indicates staying at someone's house or place."),
    (1, None,
     "'The paparazzi are in front of the building.' She describes the persistent reporters waiting outside. "
     "The preposition devant means in front of an entrance or building."),
    (2, None,
     "'They wait for the kids at school.' Photographers are even stalking young family members. "
     "The verb attendre is used here in the third-person plural present tense."),
    (3, None,
     "'Plus, her boyfriend looks at me strangely.' She feels awkward around her sister's partner as well. "
     "The connecting phrase en plus adds another frustrating element to the situation."),
    (4, None,
     "'How so? Judgmental looks?' Gabriel seeks clarification on what kind of looks she means. "
     "The phrase how so is used to ask for a clearer explanation."),
    (5, None,
     "'No, he stares at me too much. I am getting paranoid.' She admits the intense media pressure is getting to her. "
     "The adverb trop expresses an excessive degree."),
    (6, None,
     "'My sister is completely overwhelmed.' The whole family is suffering under the media intrusion. "
     "The past participle describes being deeply shaken or upset."),
    (7, None,
     "'I cannot stay over there.' Virginie realizes that remaining in the apartment has become impossible. "
     "The negative structure ne peux pas expresses an inability to act."),
    (8, None,
     "'Can I sleep at your place for two nights?' She asks Gabriel for temporary refuge. "
     "The modal verb peux asks for permission in an informal tone."),
    (9, None,
     "'My apartment is under renovation.' Gabriel tries to hesitate by mentioning the ongoing construction. "
     "The phrase en travaux refers to construction or remodeling work."),
    (10, None,
     "'That does not bother me at all.' She is willing to put up with dust and noise to escape the cameras. "
     "The phrase pas du tout emphasizes the total lack of objection."),
    (11, None,
     "'I just need a quiet spot.' Any small corner will suffice for her temporary hideout. "
     "The expression avoir besoin de means to need something essential."),
    (12, None,
     "'What do you mean by my door code?' Gabriel is surprised that she is already asking for access. "
     "The phrase qu'est-ce que tu veux dire asks for further explanation."),
    (13, None,
     "'I just have pajamas and tissues. Thank you!' Virginie accepts without waiting for him to object. "
     "The adverb juste means only or simply in this conversational context."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Virginie secures a temporary shelter away from the paparazzi. "
    "Remember the useful idiom for expressing a need: avoir besoin de."
)

CLOSING = ("lea", "Ça ne me dérange pas du tout.")
