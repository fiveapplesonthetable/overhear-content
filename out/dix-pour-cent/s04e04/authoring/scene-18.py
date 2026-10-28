# Authoring module for dix-pour-cent s04e04 scene 18 (cues 1028-1033).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e04/authoring/scene-18.py --out out/dix-pour-cent/s04e04/scene-18.json

ID = "dix-pour-cent-s04e04-scene-18"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 18
TITLE = "Trahison par courriel  (Betrayal by Email)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Camille", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1028-1033. After agreeing to sign the paternity recognition papers, Camille discovers private emails "
    "on Mathias's computer showing he plotted to deceive and discard director Ulrika. Crushed by his manipulation, "
    "Camille rejects his excuses and storms out."
)

INTRO = (
    "In Mathias's office, Camille waits while he retrieves two glasses to celebrate their signed paternity papers. "
    "Glancing at his open computer screen, Camille reads an email revealing Mathias's ruthless plot to mislead and replace director Ulrika. "
    "Let's listen to their confrontation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("mathias", "J'ai apporté deux verres pour trinquer.",
     "I brought two glasses to toast.",
     [(1026, "On trinque ?")], "Returned with glasses for a celebratory drink"),
    ("lea", "Je viens de lire tes courriels.",
     "I have just read your emails.",
     [(1029, "J'AI FAIT DES PROMESSES À ULRIKA")], "Confronted him with his private messages"),
    ("mathias", "Qu'est-ce que tu racontes là?",
     "What are you saying there?",
     [(1033, "Camille ?")], "Expressed sudden confusion and alarm"),
    ("lea", "Tu veux décourager Ulrika en secret.",
     "You want to discourage Ulrika secretly.",
     [(1030, "MAIS JE COMPTE LA DÉCOURAGER")], "Exposed his scheme to undermine the director"),
    ("mathias", "Ce n'est pas ce que tu crois!",
     "It is not what you think!",
     [(1033, "Camille ?")], "Attempted an instinctive defensive excuse"),
    ("lea", "Tu as signé la reconnaissance pour ça?",
     "Did you sign the acknowledgment for that?",
     [(1028, "RECONNAISSANCE DE PATERNITÉ")], "Questioned the real motive behind his paternity claim"),
    ("mathias", "Non, je voulais seulement te protéger.",
     "No, I only wanted to protect you.",
     [(1027, "Laisse-moi voir")], "Insisted on his paternal intentions"),
    ("lea", "Tu manipules tout le monde ici!",
     "You manipulate everyone here!",
     [(1031, "ON PEUT LA REMPLACER")], "Denounced his cynical workplace games"),
    ("mathias", "Écoute-moi deux minutes, je t'en prie.",
     "Listen to me for two minutes, please.",
     [(1033, "Camille ?")], "Pleaded for an opportunity to explain"),
    ("lea", "Je ne veux plus rien entendre.",
     "I do not want to hear anything anymore.",
     [(1033, "Camille ?")], "Refused to listen to further justifications"),
    ("mathias", "Ne pars pas comme ça, Camille!",
     "Do not leave like that, Camille!",
     [(1033, "Camille ?")], "Begged her to remain in the office"),
    ("lea", "Je rentre chez moi immédiatement.",
     "I am going home immediately.",
     [(1033, "Camille ?")], "Announced her abrupt departure"),
    ("mathias", "Laisse-moi au moins t'expliquer tout ça.",
     "Let me at least explain all that to you.",
     [(1033, "Camille ?")], "Tried one last appeal to reason"),
    ("lea", "C'est terminé entre nous, monsieur Barneville.",
     "It is over between us, Mr. Barneville.",
     [(1033, "Camille ?")], "Formally broke off their personal connection"),
]

WALK = [
    (0, None,
     "'I brought two glasses to toast.' Mathias walks in ready to celebrate. "
     "The compound past verb 'apporte' introduces his gesture."),
    (1, None,
     "'I have just read your emails.' Camille confronts him with cold clarity. "
     "The recent past construction viens de lire marks her sudden discovery."),
    (2, None,
     "'What are you saying there?' Mathias senses the sudden tension in the room. "
     "The interrogative phrase questions her words."),
    (3, None,
     "'You want to discourage Ulrika secretly.' Camille reveals what was on the screen. "
     "The verb phrase 'veux decourager' cites his covert intention."),
    (4, None,
     "'It is not what you think!' Mathias tries to deflect the accusation. "
     "The common French phrase ce n'est pas ce que tu crois serves as a defense."),
    (5, None,
     "'Did you sign the acknowledgment for that?' Camille challenges his honesty. "
     "The noun phrase la reconnaissance targets his parental filing."),
    (6, None,
     "'No, I only wanted to protect you.' Mathias attempts to reassure his daughter. "
     "The imperfect verb voulais softens his explanation."),
    (7, None,
     "'You manipulate everyone here!' Camille rejects his excuses with anger. "
     "The present verb manipules identifies his repeated deception."),
    (8, None,
     "'Listen to me for two minutes, please.' Mathias pleads for a brief conversation. "
     "The polite imperative formula je t'en prie requests her patience."),
    (9, None,
     "'I do not want to hear anything anymore.' Camille shuts down the conversation. "
     "The negative structure ne veux plus rien emphasizes finality."),
    (10, None,
     "'Do not leave like that, Camille!' Mathias panics as she grabs her coat. "
     "The negative imperative ne pars pas shows his desperation."),
    (11, None,
     "'I am going home immediately.' Camille steps toward the door. "
     "The adverb 'immediatement' highlights her resolve to leave."),
    (12, None,
     "'Let me at least explain all that to you.' Mathias makes a final plea. "
     "The phrase au moins seeks a small concession."),
    (13, None,
     "'It is over between us, Mr. Barneville.' Camille uses his formal surname to mark the break. "
     "The adjective 'termine' signals the painful rupture of their relationship."),
]

OUTRO = "Camille walks out of the building, leaving Mathias standing alone in his empty office. When you watch the episode, listen out for the expressions meaning 'brought' and 'glasses'. You'll catch them now. See you next time."
CLOSING = ("lea", "C'est terminé entre nous, monsieur Barneville.")
