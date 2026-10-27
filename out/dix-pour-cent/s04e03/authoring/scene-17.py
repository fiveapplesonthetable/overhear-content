# Authoring module for dix-pour-cent s04e03 scene 17 (cues 799-852).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e03/authoring/scene-17.py --out out/dix-pour-cent/s04e03/scene-17.json

ID = "dix-pour-cent-s04e03-scene-17"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 17
TITLE = "Une invitée inattendue  (An Unexpected Guest)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noemie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 799-852. Mathias and Noemie frantically prepare dinner for producer Igor de Serisy, "
    "only for Igor to arrive with his mistress Claire instead of his wife. In the kitchen, "
    "Noemie scolds Mathias for the lack of respect, but Mathias reminds her of their own romantic beginnings."
)

INTRO = (
    "In their apartment kitchen, Mathias and Noemie scramble to prepare dinner for producer Igor de Serisy. "
    "When Igor arrives accompanied not by his wife but by his young mistress Claire, Noemie and Mathias exchange tense whispers about loyalty, respect, and their own romantic past. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Qu'est-ce que tu fais là?",
     "What are you doing there?",
     [(799, "Qu'est-ce que tu fais")], "Asked about his frantic kitchen prep"),
    ("mathias", "Je prépare du riz en plus.",
     "I am preparing extra rice.",
     [(804, "Et du riz en plus")], "Explained the revised dinner menu"),
    ("lea", "Et pour le plat principal?",
     "And for the main course?",
     [(803, "Qu'est-ce qu'on va manger")], "Worried about the missing meat dish"),
    ("mathias", "On va servir beaucoup de vin.",
     "We will serve plenty of wine.",
     [(805, "servir beaucoup de vin")], "Counted on wine to save the evening"),
    ("lea", "Igor arrive avec une invitée surprise.",
     "Igor is arriving with a surprise guest.",
     [(811, "Bonsoir"), (816, "Je suis Claire")], "Announced the unexpected company"),
    ("mathias", "Ce n'est pas sa femme Béatrice?",
     "Is it not his wife Beatrice?",
     [(836, "Tu as dû avoir Béatrice"), (837, "la femme d'Igor")], "Checked who arrived at the door"),
    ("lea", "Non, c'est sa maîtresse Claire.",
     "No, it is his mistress Claire.",
     [(840, "c'était pas sa femme"), (847, "avec sa maîtresse")], "Confirmed the identity of the guest"),
    ("mathias", "Il faut rester calmes et polis.",
     "We must stay calm and polite.",
     [(844, "passer une super soirée")], "Urged composure before their guest"),
    ("lea", "Où est le respect là-dedans?",
     "Where is the respect in that?",
     [(847, "Où est le respect là-dedans")], "Challenged the producer's blatant disrespect"),
    ("mathias", "Nous ne pouvons pas juger l'adultère.",
     "We cannot sit in judgment of adultery.",
     [(848, "faire la morale sur l'adultère")], "Reflected on their own romantic past"),
    ("lea", "Notre histoire était totalement différente!",
     "Our story was totally different!",
     [(849, "c'était totalement différent")], "Defended the purity of their romance"),
    ("mathias", "Nous avons souffert nous aussi.",
     "We suffered as well.",
     [(850, "on s'est battues la coulpe"), (851, "On a pleuré dans le bain")], "Recalled their painful secret beginnings"),
    ("lea", "Nous étions romantiques et sincères.",
     "We were romantic and sincere.",
     [(852, "On était romantiques")], "Insisted on the nobility of their bond"),
    ("mathias", "Alors sourions pour sauver la soirée.",
     "Then let us smile to save the evening.",
     [(844, "passer une super soirée")], "Encouraged a brave face for the dinner"),
]

WALK = [
    (0, None,
     "'What are you doing there?' Noemie notices Mathias frantically moving around the kitchen. "
     "The interrogative phrase opens the scene with curiosity."),
    (1, None,
     "'I am preparing extra rice.' Mathias adjusts his dinner plans on the fly. "
     "The present verb 'prepare' shows quick problem-solving."),
    (2, None,
     "'And for the main course?' Noemie inquires about the rest of the meal. "
     "The prepositional phrase introduces the next culinary question."),
    (3, None,
     "'We will serve plenty of wine.' Mathias counts on alcohol to cover the missing dish. "
     "The near future structure conveys pragmatic optimism."),
    (4, None,
     "'Igor is arriving with a surprise guest.' Noemie reveals who just appeared at their door. "
     "The noun phrase signals an unexpected arrival."),
    (5, None,
     "'Is it not his wife Beatrice?' Mathias whispers in astonishment. "
     "The negative interrogative questions the identity of the companion."),
    (6, None,
     "'No, it is his mistress Claire.' Noemie clarifies the awkward social reality. "
     "The descriptive noun identifies Igor's companion."),
    (7, None,
     "'We must stay calm and polite.' Mathias reminds her to maintain professional courtesy. "
     "The impersonal expression urges hospitality."),
    (8, None,
     "'Where is the respect in that?' Noemie criticizes the lack of basic propriety. "
     "The interrogative challenges the blatant disrespect."),
    (9, None,
     "'We cannot sit in judgment of adultery.' Mathias acknowledges their own complicated history. "
     "The modal verb phrase urges humility."),
    (10, None,
     "'Our story was totally different!' Noemie passionately defends their past romance. "
     "The emphatic exclamation highlights her personal convictions."),
    (11, None,
     "'We suffered as well.' Mathias remembers the guilt and heartache they experienced together. "
     "The compound past evokes genuine emotion."),
    (12, None,
     "'We were romantic and sincere.' Noemie insists that their feelings were noble and pure. "
     "The imperfect tense describes an authentic emotional state."),
    (13, None,
     "'Then let us smile to save the evening.' Mathias offers a warm concluding reassurance. "
     "The imperative verb rallies their spirits for the guests."),
]

OUTRO = "Mathias and Noemie return to their living room, united in humor and ready to host an unforgettable dinner party."
CLOSING = ("mathias", "Alors sourions pour sauver la soirée.")
