# Authoring module for dix-pour-cent s02e01 scene 09 (cues 196-269).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-09.py --out out/dix-pour-cent/s02e01/scene-09.json

ID = "dix-pour-cent-s02e01-scene-09"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 9
TITLE = "L'agent de façade  (The Front Agent)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "mathias": "marcel"}
LABELS = {"lea": "Virginie", "gabriel": "Gabriel", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 196-269. Virginie Efira arrives at ASK in panic after being kicked out by Ramzy Bedia. "
               "Mathias and Gabriel try to protect both actors by having Gabriel temporarily act as Virginie's agent. "
               "Adapted for A1 French.")

INTRO = ("At the ASK offices, actress Virginie Efira arrives in complete distress. "
         "Scandalous magazine photos showed her kissing an old flame in Brussels, and her partner Ramzy Bedia "
         "immediately threw her out of their apartment. Now Mathias and Gabriel must manage the crisis. "
         "Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "Virginie, bonjour! Merci d'être là.",
  "Virginie, hello! Thank you for being here.",
  [(196, "Virginie, bonjour !"), (197, "Merci d'être là.")], ""),
 ("lea", "Il m'a donné trente minutes pour faire ma valise.",
  "He gave me thirty minutes to pack my suitcase.",
  [(200, "Il m'a donné 30 minutes pour faire ma valise.")], "Spelled out number 30"),
 ("lea", "Aucune de mes affaires ne va ensemble.",
  "None of my clothes match.",
  [(201, "Aucune de mes affaires ne va ensemble.")], ""),
 ("gabriel", "Tu aurais dû lui parler.",
  "You should have spoken to him.",
  [(204, "Tu aurais dû lui parler.")], ""),
 ("lea", "C'était rien, juste un au revoir très affectueux.",
  "It was nothing, just a very affectionate goodbye.",
  [(205, "C'était rien, juste un au revoir."), (206, "Un au revoir très affectueux,")], ""),
 ("lea", "Ce type ne compte pas, c'est une vieille histoire.",
  "That guy does not matter, it is an old story.",
  [(211, "Ce type ne compte pas"), (212, "C'est une très vieille flamme.")], "Simplified 'très vieille flamme' to 'vieille histoire'"),
 ("lea", "J'ai tout gâché! Comment on paie le loyer maintenant?",
  "I ruined everything! How do we pay the rent now?",
  [(224, "J'ai tout gâché."), (225, "Comment on paie le loyer ?")], ""),
 ("gabriel", "Il faut être raisonnables. Mathias va trouver une solution.",
  "We must be reasonable. Mathias will find a solution.",
  [(227, "Il faut être raisonnables."), (228, "Mathias va trouver une solution.")], ""),
 ("mathias", "Virginie, calme-toi. On s'en occupe.",
  "Virginie, calm down. We are handling it.",
  [(245, "on s'en occupe.")], "Added calm greeting"),
 ("mathias", "Les paparazzi sont en bas, ils vous attendent.",
  "The paparazzi are downstairs, they are waiting for you.",
  [(246, "Les paparazzi sont en bas !"), (247, "Ils m'ont dans leur viseur !")], "Simplified cue 247"),
 ("mathias", "Voilà ce qu'on va faire.",
  "Here is what we are going to do.",
  [(255, "Bien, voilà ce qu'on va faire.")], ""),
 ("gabriel", "Je serai en quelque sorte ton agent par intérim.",
  "I will be your interim agent in a way.",
  [(257, "Je serai en quelque sorte une agente par intérim.")], "Adjusted gender to agent"),
 ("mathias", "Un arrangement temporaire, juste une façade.",
  "A temporary arrangement, just a facade.",
  [(259, "Un arrangement temporaire. Juste une façade.")], ""),
 ("lea", "D'abord mon mec me quitte, maintenant mon agent!",
  "First my boyfriend leaves me, now my agent!",
  [(260, "D'abord mon mec me plaque, maintenant mon agent.")], "Softened 'me plaque' to 'me quitte'"),
 ("mathias", "Ne le prends pas comme ça. Gabriel et moi travaillons ensemble.",
  "Do not take it like that. Gabriel and I work together.",
  [(262, "Ne le prends pas comme ça. Gabriel et moi"), (263, "travaillons en étroite collaboration.")], "Simplified collaboration"),
 ("gabriel", "On va arranger ça, on te le promet.",
  "We are going to fix this, we promise you.",
  [(268, "on va arranger de belles façades."), (269, "On vous le promet.")], ""),
]

OPENER = "Let's examine how Gabriel and Mathias try to reassure a panicked actress."

WALK = [
 (0, None,
  "'Virginie, hello! Thank you for being here.' Gabriel greets his client warmly as she arrives."),
 (1, None,
  "'He gave me thirty minutes to pack my suitcase.' Notice the compound past tense describing Ramzy's ultimatum."),
 (2, None,
  "'None of my clothes match.' A feminine indefinite pronoun followed by a negative verb."),
 (3, None,
  "'You should have spoken to him.' A past conditional expression of advice or regret."),
 (4, None,
  "'It was nothing, just a very affectionate goodbye.' An imperfect description followed by a common greeting noun."),
 (5, None,
  "'That guy does not matter, it is an old story.' The verb for counting or mattering in the negative."),
 (6, "J'ai tout gâché!",
  "'I ruined everything!' A strong past tense exclamation of regret."),
 (6, "Comment on paie le loyer maintenant?",
  "'How do we pay the rent now?' An informal present tense question using the pronoun meaning we."),
 (7, None,
  "'We must be reasonable. Mathias will find a solution.' Gabriel urges patience while invoking Mathias's authority."),
 (8, None,
  "'Virginie, calm down. We are handling it.' An imperative followed by the pronominal verb for taking care of a problem."),
 (9, None,
  "'The paparazzi are downstairs, they are waiting for you.' The spatial adverb meaning downstairs."),
 (10, None,
  "'Here is what we are going to do.' A classic presentative phrase introducing a plan of action."),
 (11, None,
  "'I will be your interim agent in a way.' The simple future tense of the verb to be."),
 (12, None,
  "'A temporary arrangement, just a facade.' Mathias clarifies the diplomatic nature of the split."),
 (13, None,
  "'First my boyfriend leaves me, now my agent!' Virginie sums up her terrible morning with dark humour."),
 (14, None,
  "'Do not take it like that. Gabriel and I work together.' A reassuring negative imperative."),
 (15, None,
  "'We are going to fix this, we promise you.' A near-future promise ending on a supportive note."),
]

TRANSITION = "Now let's listen to the whole discussion again without stopping."

OUTRO = ("Gabriel has agreed to become Virginie's public agent while Mathias represents Ramzy. "
         "In the next scene, Mathias will try to talk some sense into Ramzy himself.")
CLOSING = ("lea", "Merci, Gabriel.")
