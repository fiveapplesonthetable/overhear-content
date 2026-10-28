# Authoring module for dix-pour-cent s03e06 scene 05 (cues 343-362).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e06/authoring/scene-05.py --out out/dix-pour-cent/s03e06/scene-05.json

ID = "dix-pour-cent-s03e06-scene-05"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 5
TITLE = "Fille de traître  (Traitor's Daughter)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "noemie": "emilie", "herve": "theo"}
LABELS = {"lea": "Camille", "noemie": "Noémie", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 343-362. In the ASK offices, Camille, Noemie, and Herve clash over Mathias's betrayal "
               "and agency loyalty before uniting to clean up the space for the anniversary party. Adapted for A1 French.")

INTRO = ("At the ASK agency, tensions flare between assistants and junior agents ahead of the thirtieth anniversary gala. "
         "Camille, Noemie, and Herve argue about betrayal and family loyalty before putting differences aside to clean the office. "
         "Let's listen to their exchange in French first.")

STORY = [
    ("lea", "Fille de traître, voilà ce qu'il pense.",
     "Traitor's daughter, that is what he thinks.",
     [(343, "Fille de traître, c'est ça qu'il aurait dû écrire.")], "Camille feels targeted by colleagues"),
    ("noemie", "Il faut parfois se salir les mains.",
     "One must sometimes get one's hands dirty.",
     [(345, "faut savoir se salir les mains")], "Noemie defends tough business realities"),
    ("herve", "Tu es pathétique à le défendre ainsi!",
     "You are pathetic defending him like that!",
     [(348, "Tu sais que tu deviens pathétique")], "Herve lashes out at Noemie"),
    ("noemie", "Et vous avec vos petites manigances?",
     "And what about you with your little schemes?",
     [(349, "avec vos petites bidouilles.")], "Noemie turns the accusation around"),
    ("noemie", "On a tous un cadavre dans le placard!",
     "We all have a skeleton in the closet!",
     [(350, "un petit cadavre dans le placard")], "Noemie reminds everyone of past secrets"),
    ("herve", "Mais nous n'avons trahi personne!",
     "But we never betrayed anyone!",
     [(352, "nous, on a trahi personne.")], "Herve claims moral integrity"),
    ("lea", "Moi, je croyais que nous étions amis.",
     "I believed that we were friends.",
     [(355, "Je croyais qu'on était amis.")], "Camille mourns their broken unity"),
    ("noemie", "Mathias cherche seulement à sauver son avenir.",
     "Mathias is only looking to save his future.",
     [(345, "accomplir de grandes choses")], "Noemie highlights Mathias's desperation"),
    ("herve", "Il n'y a plus rien à dire.",
     "There is nothing left to say.",
     [(358, "il y a plus rien à dire.")], "Herve steps away from the confrontation"),
    ("herve", "C'est à moi de tout ranger ici.",
     "It is up to me to tidy up everything here.",
     [(360, "C'est à moi de m'en occuper.")], "Herve starts cleaning the agency desks"),
    ("lea", "Attends Hervé, nous allons t'aider.",
     "Wait Herve, we are going to help you.",
     [(362, "On va t'aider.")], "Camille offers immediate assistance"),
    ("noemie", "Oui, préparons cette soirée ensemble.",
     "Yes, let's prepare this evening together.",
     [(359, "Allez-y, les filles.")], "Noemie reconciles with the assistants"),
    ("herve", "Merci les filles, rangeons ces dossiers.",
     "Thank you ladies, let's put away these files.",
     [(362, "On va t'aider.")], "Herve welcomes their teamwork"),
]

OPENER = "Let's explore how Camille, Noemie, and Herve navigate workplace conflict line by line."

WALK = [
    (0, None,
     "'Traitor's daughter, that is what he thinks.' Camille feels stung by office accusations against her father. In spoken French, the little word before 'thinks.' drops its final vowel and attaches with an apostrophe."),
    (1, None,
     "'One must sometimes get one's hands dirty.' Noemie defends Mathias's aggressive maneuvers to secure his position. The reflexive pronoun sits right in front of the verb for 'must', turning the action back onto the subject."),
    (2, None,
     "'You are pathetic defending him like that!' Herve criticizes Noemie's unconditional loyalty to Mathias. The clause hinges on the everyday verb meaning 'defending'."),
    (3, None,
     "'And what about you with your little schemes?' Noemie reminds Herve of the junior agents' own plotting. The formal 'you' pronoun sets a courteous, professional distance around 'schemes?'."),
    (4, None,
     "'We all have a skeleton in the closet!' Noemie points out that nobody at ASK is completely blameless. Notice how 'have' leads directly into the noun meaning 'skeleton'."),
    (5, None,
     "'But we never betrayed anyone!' Herve insists on a moral distinction between their actions and Mathias's buyout. The two-part French negation brackets the verb for 'have' on both sides."),
    (6, None,
     "'I believed that we were friends.' Camille laments the damage done to their close workplace friendships. Notice how 'thought' leads directly into the noun meaning 'friends.'."),
    (7, None,
     "'Mathias is only looking to save his future.' Noemie explains Mathias's motivations under heavy pressure. The verb meaning 'is seeking' pairs naturally with the noun for 'future.' in everyday conversation."),
    (8, None,
     "'There is nothing left to say.' Herve attempts to end the painful argument. In spoken French, the little word before 'say.' drops its final vowel and attaches with an apostrophe."),
    (9, None,
     "'It is up to me to tidy up everything here.' Herve prepares to clean the messy offices alone. The clause hinges on the everyday verb meaning 'it is'."),
    (10, None,
     "'Wait Herve, we are going to help you.' Camille refuses to let her friend clean in isolation. Camille uses the casual singular 'you' with 'wait', showing close familiarity."),
    (11, None,
     "'Yes, let's prepare this evening together.' Noemie joins in solidarity before the arrival of guests. The verb meaning 'let's prepare' pairs naturally with the noun for 'party' in everyday conversation."),
    (12, None,
     "'Thank you ladies, let's put away these files.' Herve accepts their help with genuine relief. Notice how 'let's put away' leads directly into the noun meaning 'girls'."),
]

TRANSITION = "Now let's listen to the assistants' reconciliation once more from start to finish."

OUTRO = ("Camille, Noemie, and Herve overcome workplace resentments to prepare the agency for ASK's major anniversary. "
         "Let's review the key loyalty and reconciliation vocabulary from this scene.")

CLOSING = ("herve", "Merci les filles, rangeons ces dossiers.")
