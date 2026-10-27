# Authoring module for dix-pour-cent s02e02 scene 29 (cues 943-973).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-29.py --out out/dix-pour-cent/s02e02/scene-29.json

ID = "dix-pour-cent-s02e02-scene-29"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 29
TITLE = "Le grand frisson de Mathias  (Mathias's Big Thrill)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "serveur": "marcel"}
LABELS = {"lea": "Noémie", "mathias": "Mathias", "serveur": "Le serveur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 943-973. Following his alcohol blackout, Mathias meets assistant Noémie at a quiet Parisian restaurant. "
    "Relieved to find him safe, Noémie admits her frantic worries before their private conversation takes an "
    "unexpectedly romantic and secretive turn, heading off into the Parisian night together."
)

INTRO = (
    "Following his alarming alcohol blackout after the previous night's celebrations, Mathias meets assistant Noemie at a quiet Parisian restaurant. "
    "Relieved to find him safe and sound, Noemie admits her frantic worries before their private conversation takes an unexpectedly romantic and secretive turn. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "Mathias! Qu'est-ce que tu fais là?", "Mathias! What are you doing here?",
     [(943, "Mathias"), (943, "Qu'est-ce que tu fais là")], "Noémie sees Mathias at the restaurant"),
    ("lea", "Oh, je suis tellement désolée...", "Oh, I am so sorry...",
     [(944, "Oh, je suis tellement désolée")], ""),
    ("mathias", "Laisse, Noémie.", "Don't worry, Noémie.",
     [(947, "Laisse, Noémie")], ""),
    ("lea", "J'étais tellement inquiète.", "I was so worried.",
     [(948, "J'étais tellement inquiète")], ""),
    ("lea", "J'ai appelé tous les hôpitaux, puis les pompiers.", "I called all the hospitals, then the firefighters.",
     [(949, "J'ai appelé tous les hôpitaux, puis les pompiers")], ""),
    ("lea", "Tu dois me prendre pour une folle.", "You must take me for a crazy person.",
     [(951, "Tu dois me prendre pour une folle")], ""),
    ("mathias", "Comme tu viens d'une famille de bâtisseurs, tu peux tout réparer.", "Since you come from a family of builders, you can fix everything.",
     [(952, "Comme tu viens d'une famille de bâtisseurs"), (953, "tu peux tout réparer")], ""),
    ("lea", "Nathalie Baye a appelé.", "Nathalie Baye called.",
     [(955, "Nathalie Baye a appelé")], ""),
    ("lea", "Je lui ai dit qu'on avait un accord pour son contrat.", "I told her we had an agreement for her contract.",
     [(956, "Je lui ai dit qu'on avait un accord pour son contrat")], ""),
    ("mathias", "Oui, merci.", "Yes, thank you.",
     [(958, "Oui, merci")], ""),
    ("serveur", "J'en ai vu de toutes les couleurs. Mais pas comme vous.", "I have seen all sorts of things. But not like you.",
     [(959, "J'en ai vu de toutes les couleurs"), (960, "Mais pas comme vous")], "the waiter observes the lovers at the table"),
    ("serveur", "Des amants qui font semblant de trinquer au lieu de s'embrasser?", "Lovers pretending to toast instead of kissing?",
     [(961, "Des amants"), (962, "qui font semblant de trinquer au lieu de s'embrasser")], ""),
    ("serveur", "Je n'ai jamais vu ça!", "I have never seen that!",
     [(963, "Je n'ai jamais vu ça")], ""),
    ("mathias", "Chut!", "Hush!",
     [(966, "Chut")], ""),
    ("lea", "Oh, Mathias...", "Oh, dear Mathias...",
     [(967, "Oh, Mathias")], ""),
    ("mathias", "Le grand frisson. Allons-y, maintenant.", "The big thrill. Let's go now.",
     [(970, "Le grand frisson"), (971, "Allons-y, maintenant")], ""),
]

OPENER = "Let's walk through the secret dinner of Mathias and Noemie step by step."

WALK = [
    (0, None,
     "'Mathias! What are you doing here?' Noemie is stunned to see Mathias at the restaurant."),
    (1, None,
     "'Oh, I am so sorry...' The feminine adjective 'desolee' agrees with Noemie."),
    (2, None,
     "'Don't worry, Noemie.' The imperative 'laisse' tells her to let the matter go."),
    (3, None,
     "'I was so worried.' The imperfect 'etais' describes Noemie's state of mind."),
    (4, None,
     "'I called all the hospitals, then the firefighters.' Noemie lists her desperate emergency calls."),
    (5, None,
     "'You must take me for a crazy person.' The idiom 'prendre pour' means to take someone for something."),
    (6, None,
     "'Since you come from a family of builders, you can fix everything.' Mathias compliments her resourcefulness."),
    (7, None,
     "'Nathalie Baye called.' The compound past tense uses the auxiliary verb 'avoir'."),
    (8, None,
     "'I told her we had an agreement for her contract.' The indirect pronoun 'lui' refers to Nathalie Baye."),
    (9, None,
     "'Yes, thank you.' Mathias thanks his loyal assistant for managing the client."),
    (10, None,
     "'I have seen all sorts of things. But not like you.' The idiom 'en voir de toutes les couleurs' means to have seen it all."),
    (11, None,
     "'Lovers pretending to toast instead of kissing?' The phrase 'faire semblant de' means to pretend."),
    (12, None,
     "'I have never seen that!' The negation 'ne... jamais' wraps around the auxiliary verb."),
    (13, None,
     "'Hush!' Mathias shushes the chatty waiter with a quiet interjection."),
    (14, None,
     "'Oh, dear Mathias...' Noemie gazes at Mathias with fond affection."),
    (15, None,
     "'The big thrill. Let's go now.' The imperative 'allons-y' urges them to leave together."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Mathias and Noemie share a tender romantic secret away from the pressures of the agency, heading off into the Parisian night together."
CLOSING = ("mathias", "Allons-y, maintenant.")
