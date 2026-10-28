# Authoring module for dix-pour-cent s04e06 scene 26 (cue 1041).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e06/authoring/scene-26.py --out out/dix-pour-cent/s04e06/scene-26.json

ID = "dix-pour-cent-s04e06-scene-26"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 26
TITLE = "Le panneau d'ASK  (The ASK Sign)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cue 1041. Standing at the entrance of ASK, Gabriel and Andrea look at the glass doors "
    "bearing the name Agence Samuel Kerr, paying tribute to their shared history before locking up."
)

INTRO = (
    "Standing by the agency entrance, Andrea and Gabriel pause in front of the glass doors bearing the famous Samuel Kerr lettering. "
    "Remembering their late mentor and the ten intense years of cinema history created within these walls, they prepare to close the door for the very last time. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine Gabriel and Andrea facing the agency entrance step by step."

STORY = [
    ("lea", "Arrête-toi un instant devant la porte.", "Stop for a moment in front of the door.",
     [(1041, "AGENCE SAMUEL KERR")], ""),
    ("gabriel", "Regarde les lettres sur la vitre.", "Look at the letters on the glass.",
     [(1041, "AGENCE SAMUEL KERR")], ""),
    ("lea", "Agence Samuel Kerr.", "Samuel Kerr Agency.",
     [(1041, "AGENCE SAMUEL KERR")], ""),
    ("gabriel", "Samuel serait très fier de nous.", "Samuel would be very proud of us.",
     [(1041, "AGENCE SAMUEL KERR")], ""),
    ("lea", "Nous avons sauvé tellement de films.", "We saved so many films.",
     [(1041, "AGENCE SAMUEL KERR")], ""),
    ("gabriel", "Et nous avons aimé nos acteurs.", "And we loved our actors.",
     [(1041, "AGENCE SAMUEL KERR")], ""),
    ("lea", "Même quand ils étaient difficiles!", "Even when they were difficult!",
     [(1041, "AGENCE SAMUEL KERR")], ""),
    ("gabriel", "Surtout quand ils étaient difficiles!", "Especially when they were difficult!",
     [(1041, "AGENCE SAMUEL KERR")], ""),
    ("lea", "Est-ce que tu as des regrets?", "Do you have any regrets?",
     [(1041, "AGENCE SAMUEL KERR")], ""),
    ("gabriel", "Non, aucun regret ce soir.", "No, no regret tonight.",
     [(1041, "AGENCE SAMUEL KERR")], ""),
    ("lea", "L'histoire d'ASK se termine ici.", "The story of ASK ends here.",
     [(1041, "AGENCE SAMUEL KERR")], ""),
    ("gabriel", "Mais notre amitié reste intacte.", "But our friendship remains intact.",
     [(1041, "AGENCE SAMUEL KERR")], ""),
    ("lea", "Fermons cette porte pour toujours.", "Let us close this door forever.",
     [(1041, "AGENCE SAMUEL KERR")], ""),
    ("gabriel", "Une nouvelle page commence.", "A new page begins.",
     [(1041, "AGENCE SAMUEL KERR")], ""),
]

WALK = [
    (0, None,
     "'Stop for a moment in front of the door.' Andrea pauses before the entrance of the floor. The verb meaning 'stop' pairs naturally with the noun for 'instant' in everyday conversation."),
    (1, None,
     "'Look at the letters on the glass.' Gabriel points to the golden sign on the door. Notice how 'look at' leads directly into the noun meaning 'letters'."),
    (2, None,
     "'Samuel Kerr Agency.' Andrea reads the iconic name aloud to him. The key noun here means 'agency', anchored by its matching French article."),
    (3, None,
     "'Samuel would be very proud of us.' Gabriel remembers that their mentor loved them. The clause hinges on the everyday verb meaning 'would be'."),
    (4, None,
     "'We saved so many films.' Andrea recalls the work that they accomplished. This conversational past tense combines a helper verb with the past participle for 'saved'."),
    (5, None,
     "'And we loved our actors.' Gabriel adds that they cared for every client. The verb meaning 'have' pairs naturally with the noun for 'actors' in everyday conversation."),
    (6, None,
     "'Even when they were difficult!' Andrea laughs as she remembers their battles. The clause hinges on the everyday verb meaning 'were'."),
    (7, None,
     "'Especially when they were difficult!' Gabriel smiles with fond affection for them. Dropping the subject pronoun turns the verb for 'were' into a direct, punchy command."),
    (8, None,
     "'Do you have any regrets?' Andrea asks if he feels any sorrow. Notice how 'is it' leads directly into the noun meaning 'regret'."),
    (9, None,
     "'No, no regret tonight.' Gabriel affirms that he is at peace with it. The key noun here means 'regret', anchored by its matching French article."),
    (10, None,
     "'The story of ASK ends here.' Andrea accepts that the chapter is closed. The reflexive pronoun sits right in front of the verb for 'ends', turning the action back onto the subject."),
    (11, None,
     "'But our friendship remains intact.' Gabriel reassures her of their enduring bond. The verb meaning 'remains' pairs naturally with the noun for 'friendship' in everyday conversation."),
    (12, None,
     "'Let us close this door forever.' Andrea turns the key in the lock. The verb meaning 'let us close' pairs naturally with the noun for 'door' in everyday conversation."),
    (13, None,
     "'A new page begins.' Gabriel looks to the future with hope."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Before closing the doors forever, Andrea and Gabriel pause with deep respect before the ASK logo, proud of their shared history and ready for the future. When you watch the episode, listen out for the expressions meaning 'stop' and 'instant'. You'll catch them now. See you next time."
CLOSING = ("gabriel", "Une nouvelle page commence.")
