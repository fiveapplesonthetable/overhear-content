ID = "dix-pour-cent-s01e06-scene-17"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 17
TITLE = "Je ne vous pardonnerai jamais  (I Will Never Forgive You)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "catherine": "emilie", "mathias": "marcel"}
LABELS = {"lea": "Andréa", "catherine": "Catherine", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"

INTRO = (
    "After Sofia tells Gabriel to remove her from his files, Mathias goes to Catherine's "
    "workplace to beg for five minutes to apologize, only to be coldly turned away. Back at "
    "ASK, Andréa calls François Berléand to convince him to attend Christophe Bel's birthday "
    "party that evening. Let's listen to the scene in French first; don't worry about catching every word."
)

STORY = [
    ("catherine", "Qu'est-ce que vous voulez?",
     "What do you want?",
     [(472, "Qu'est-ce que vous voulez")], ""),
    ("mathias", "Je veux juste vous parler. M'excuser.",
     "I just want to talk to you. To apologize.",
     [(473, "Je veux juste vous parler"), (473, "M'excuser")], ""),
    ("catherine", "Excusez-vous tant que vous voulez, je ne vous pardonnerai jamais.",
     "Apologize as much as you want, I will never forgive you.",
     [(474, "Excusez-vous tant que vous voulez, je ne vous pardonnerai jamais")], ""),
    ("mathias", "Cinq minutes seulement. Pourquoi vous êtes soudain si pressée?",
     "Just five minutes. Why are you suddenly in such a hurry?",
     [(475, "Cinq minutes seulement"), (476, "Pourquoi vous êtes soudain si pressée")], ""),
    ("catherine", "Je ne supporte plus ça.",
     "I can't stand this anymore.",
     [(477, "Je"), (477, "supporte plus ça")],
     "negation particle restored"),
    ("mathias", "Je m'inquiète pour vous.",
     "I'm worried about you.",
     [(478, "Je m'inquiète pour vous")], ""),
    ("catherine", "Vous avez peur pour votre agence?",
     "Are you afraid for your agency?",
     [(479, "Vous avez peur pour votre agence")], ""),
    ("mathias", "Non, chérie.",
     "No, darling.",
     [(481, "Non, chérie")], ""),
    ("catherine", "Ne m'appelez pas chérie! Jamais!",
     "Don't call me darling! Ever!",
     [(482, "pas"), (482, "chérie"), (482, "Jamais")],
     "formal 'appelez' used to match Catherine's vouvoiement in cues 472-479, guillemets removed"),
    ("lea", "On se retrouve là-bas. À quelle heure?",
     "We'll meet there. At what time?",
     [(485, "On se retrouve là-bas. À quelle heure")], ""),
    ("lea", "François, il t'a invité personnellement. Et là tu hésites?",
     "François, he invited you personally. And now you're hesitating?",
     [(487, "François, il t'a invité personnellement. Et là tu hésites")], ""),
    ("lea", "Ce n'est pas ce que tu voulais?",
     "Isn't that what you wanted?",
     [(488, "pas ce que tu voulais")],
     "spoken 'C'est pas' restored to 'Ce n'est pas'"),
    ("lea", "Pardon, François, je ne te suis pas.",
     "Sorry, François, I don't follow you.",
     [(493, "Pardon, François, je ne te suis pas")], ""),
    ("lea", "Bon, je serai là à vingt heures trente. On se retrouve dehors.",
     "Right, I'll be there at eight-thirty. We'll meet outside.",
     [(494, "Bon, je serai là à"), (494, "On se retrouve dehors")],
     "'20h30' written out as words"),
    ("lea", "Oui, Colette, c'est moi. Il s'est passé quelque chose au travail.",
     "Yes, Colette, it's me. Something came up at work.",
     [(496, "Colette, c'est moi"), (498, "Il s'est passé quelque chose")],
     "spoken 'Ouais' and 'au boulot' adapted to standard A1 'Oui' and 'au travail'"),
]

OPENER = "Let's go through it slowly. Mathias intercepts Catherine at her workplace."

WALK = [
    (0, None,
     "'What do you want?' Notice that Catherine addresses her own husband with the formal 'you' in front of her staff to keep him at a distance."),
    (1, None,
     "'I just want to talk to you. To apologize.' Mathias follows suit with the formal pronoun."),
    (2, None,
     "'Apologize as much as you want, I will never forgive you.' The verb is in the future tense, wrapped in the negative words for 'never'."),
    (3, "Cinq minutes seulement.",
     "'Just five minutes.' Literally 'five minutes only', he pleads to her."),
    (3, "Pourquoi vous êtes soudain si pressée?",
     "'Why are you suddenly in such a hurry?' The key word here means 'why', which Mathias combines with 'you'."),
    (4, None,
     "'I can't stand this anymore.' The negative words around the verb mean 'no longer' or 'not anymore'."),
    (5, None,
     "'I'm worried about you.' You'll hear 'I' all the time in the show, here connected with 'you'."),
    (6, None,
     "'Are you afraid for your agency?' Catherine suspects Mathias only cares about her father's money to buy out ASK."),
    (7, None,
     "'No, darling.' Mathias slips back into familiarity with her."),
    (8, None,
     "'Don't call me darling! Ever!' Catherine calls her assistant Sandra and walks away. Meanwhile at ASK, Andréa is on the phone with François."),
    (9, None,
     "'We'll meet there. At what time?' Christophe Bel sent François a text from Andréa's phone inviting him to his birthday party, and François says he doesn't feel like going."),
    (10, None,
     "'François, he invited you personally. And now you're hesitating?' In French, 'François' leads into 'hesitate' in a very natural everyday phrasing."),
    (11, None,
     "'Isn't that what you wanted?' François grumbles that he would have preferred a quiet lunch rather than a birthday party."),
    (12, None,
     "'Sorry, François, I don't follow you.' Here 'follow' is from the verb 'to follow', spelled the same as 'I am'."),
    (13, "Bon, je serai là à vingt heures trente.",
     "'Right, I'll be there at eight-thirty.' French uses the twenty-four-hour clock for evening appointments."),
    (13, "On se retrouve dehors.",
     "'We'll meet outside.' Literally 'we find each other again outside'."),
    (14, None,
     "'Yes, Colette, it's me. Something came up at work.' As soon as she hangs up with François, Andréa calls Colette to explain why she will be late for dinner with Colette's friends."),
]

TRANSITION = "Now let's hear the whole scene again from start to finish."

OUTRO = (
    "While Mathias is left alone after Catherine rejects his apology, Andréa heads out to meet "
    "François at Christophe Bel's birthday party. See you in the next scene."
)
CLOSING = ("lea", "On se retrouve dehors.")
