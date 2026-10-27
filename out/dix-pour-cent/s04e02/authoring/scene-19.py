# Authoring module for dix-pour-cent s04e02 scene 19 (cues 1024-1034).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e02/authoring/scene-19.py --out out/dix-pour-cent/s04e02/scene-19.json

ID = "dix-pour-cent-s04e02-scene-19"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 19
TITLE = "Le prix du métier  (The Price of the Trade)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Élise", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1024-1034. On a late-night phone call, Élise Formet confirms that Dany Boon will sign with Mathias. "
    "Despite securing the star, Mathias feels disillusioned when Élise questions the cynicism and manipulation of their trade."
)

INTRO = (
    "Late at night, Elise Formet calls Mathias Barneville to deliver major industry news. "
    "While confirming that superstar Dany Boon has agreed to sign, Elise confronts Mathias on the cynical maneuvering required to win, forcing him to reflect on the nature of their business. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Allô Mathias? Oui, c'est enfin fait.",
     "Hello Mathias? Yes, it is finally done.",
     [(1024, "Allô"), (1024, "c'est fait")], "Elise announces the completed deal"),
    ("mathias", "Dany Boon va signer chez nous?",
     "Is Dany Boon signing with us?",
     [(1025, "signer avec vous")], "Mathias seeks definitive confirmation"),
    ("lea", "Oui, il a accepté notre offre.",
     "Yes, he accepted our offer.",
     [(1025, "signer avec vous")], "Elise confirms the agreement"),
    ("mathias", "C'est une très bonne nouvelle, merci.",
     "That is very good news, thank you.",
     [(1026, "pas l'air ravi")], "Mathias offers restrained satisfaction"),
    ("lea", "Tu n'as pas l'air très ravi.",
     "You do not seem very thrilled.",
     [(1026, "pas l'air ravi")], "Elise senses his underlying fatigue"),
    ("mathias", "Je suis fatigué par ces négociations.",
     "I am tired from these negotiations.",
     [(1026, "ce que vous vouliez")], "Mathias admits emotional exhaustion"),
    ("lea", "Tu n'as jamais honte de manipuler?",
     "Are you never ashamed of manipulating?",
     [(1027, "jamais honte"), (1029, "manipuler les gens")], "Elise raises a moral challenge"),
    ("mathias", "Honte de quoi? D'obtenir des contrats?",
     "Ashamed of what? Of getting contracts?",
     [(1028, "Honte de quoi")], "Mathias defends professional necessity"),
    ("lea", "De manipuler tous nos amis artistes?",
     "Of manipulating all our artist friends?",
     [(1029, "manipuler les gens")], "Elise points to the human cost"),
    ("mathias", "C'est notre métier, nous l'avons choisi.",
     "It is our job, we chose it.",
     [(1032, "C'est notre métier"), (1032, "on l'a choisi")], "Mathias rationalizes the compromise"),
    ("lea", "Ce métier détruit nos belles amitiés.",
     "This profession destroys our good friendships.",
     [(1031, "vraie question")], "Elise laments the personal toll"),
    ("mathias", "Les affaires demandent de la dureté.",
     "Business demands toughness.",
     [(1032, "notre métier")], "Mathias states the reality of their industry"),
    ("lea", "Je t'envoie les contrats signés demain.",
     "I will send you signed contracts tomorrow.",
     [(1033, "envoyez les contrats demain")], "Elise closes on practical terms"),
    ("mathias", "D'accord, bonne soirée à toi, Élise.",
     "All right, good evening to you, Elise.",
     [(1034, "D'accord")], "Mathias ends the call solemnly")
]

WALK = [
    (0, None,
     "'Hello Mathias? Yes, it is finally done.' Elise delivers the long-awaited news. "
     "The telephone greeting 'allo' opens a phone call."),
    (1, None,
     "'Is Dany Boon signing with us?' Mathias asks about the star client's signature. "
     "The near-future 'va signer' denotes an imminent agreement."),
    (2, None,
     "'Yes, he accepted our offer.' Elise confirms the client's consent. "
     "The compound past verb 'a accepte' notes formal agreement."),
    (3, None,
     "'That is very good news, thank you.' Mathias expresses measured appreciation. "
     "The noun phrase 'bonne nouvelle' celebrates positive development."),
    (4, None,
     "'You do not seem very thrilled.' Elise detects a lack of genuine joy. "
     "The verbal idiom 'avoir l'air' means to appear or seem."),
    (5, None,
     "'I am tired from these negotiations.' Mathias admits the weariness of endless wrangling. "
     "The past participle 'fatigue' conveys physical and mental strain."),
    (6, None,
     "'Are you never ashamed of manipulating?' Elise confronts him with an uncomfortable moral truth. "
     "The verbal phrase 'avoir honte de' means to feel ashamed of."),
    (7, None,
     "'Ashamed of what? Of getting contracts?' Mathias defends his business results. "
     "The infinitive 'obtenir' designates securing tangible outcomes."),
    (8, None,
     "'Of manipulating all our artist friends?' Elise highlights the betrayal of personal relationships. "
     "The verb 'manipuler' denotes using subtle deceit."),
    (9, None,
     "'It is our job, we chose it.' Mathias reminds her of the rules of the agency trade. "
     "The compound past 'avons choisi' affirms deliberate career choice."),
    (10, None,
     "'This profession destroys our good friendships.' Elise mourns the erosion of authentic bonds. "
     "The transitive verb 'detruit' conveys destructive damage."),
    (11, None,
     "'Business demands toughness.' Mathias explains the uncompromising demands of corporate survival. "
     "The noun 'durete' refers to firmness and emotional resolve."),
    (12, None,
     "'I will send you signed contracts tomorrow.' Elise returns to immediate paperwork tasks. "
     "The present verb 'envoie' marks prompt document dispatch."),
    (13, None,
     "'All right, good evening to you, Elise.' Mathias concludes the conversation pensively. "
     "The polite closing 'bonne soiree' wishes a pleasant night.")
]

OUTRO = (
    "Though victorious in securing Dany Boon, Mathias is left alone with the bitter truth of Elise's words. "
    "In the cutthroat world of Parisian talent representation, triumph often comes at the price of personal integrity. "
    "Now let's listen to the scene one last time in French."
)

CLOSING = ("mathias", "D'accord, bonne soirée à toi, Élise.")
