# Authoring module for dix-pour-cent s04e03 scene 08 (cues 240-313).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e03/authoring/scene-08.py --out overhear-content/out/dix-pour-cent/s04e03/scene-08.json

ID = "dix-pour-cent-s04e03-scene-08"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 8
TITLE = "L'arrivée d'Élise  (Élise's Arrival)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "elise": "emilie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "elise": "Élise", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 277-313. Élise Formain arrives at ASK and gives a welcome speech. "
    "While Andréa tries to welcome her, Gabriel refuses to join in and bitterly proposes a toast to the death of their agency principles."
)

INTRO = (
    "Elise Formain arrives at the ASK agency following her departure from StarMedia. "
    "She gathers the team to deliver an ambitious welcome speech, hoping to smooth over past rivalries with Andrea Martel. "
    "However, an outraged Gabriel Sarda refuses to play along with the corporate welcome. "
    "Let's listen to their tense encounter in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("elise", "Merci à tous pour votre accueil chez ASK.",
     "Thank you all for your welcome at ASK.",
     [(279, "merci à tous de m'accueillir chez ASK")], "Élise thanks the ASK team"),
    ("lea", "Bienvenue parmi nous dans notre équipe.",
     "Welcome among us to our team.",
     [(278, "Élise, la parole est à toi")], "Andréa formally welcomes her"),
    ("elise", "J'ai une réputation un peu difficile.",
     "I have a somewhat difficult reputation.",
     [(281, "j'ai une certaine mauvaise réputation")], "Élise acknowledges her fierce image"),
    ("lea", "Ici, nous respectons le bon travail.",
     "Here, we respect good work.",
     [(299, "j'ai toujours admiré ton travail")], "Andréa values talent and competence"),
    ("elise", "Je veux travailler avec vous deux.",
     "I want to work with you two.",
     [(302, "on a beaucoup à apprendre l'un de l'autre")], "Élise proposes close collaboration"),
    ("elise", "Vous êtes de très bons agents.",
     "You are very good agents.",
     [(294, "d'excellents agents")], "Élise praises the partners"),
    ("gabriel", "Moi, je n'ai pas le temps.",
     "As for me, I do not have time.",
     [(310, "je n'ai pas le temps pour ça")], "Gabriel rejects the pleasantries"),
    ("lea", "Gabriel, reste un instant avec nous.",
     "Gabriel, stay a moment with us.",
     [(309, "Quant à toi, Gabriel")], "Andréa asks him to remain"),
    ("gabriel", "Je préfère retourner à mon bureau.",
     "I prefer to return to my office.",
     [(310, "J'ai du travail")], "Gabriel seeks an exit"),
    ("elise", "Nous pouvons quand même trinquer ensemble.",
     "We can still drink a toast together.",
     [(311, "Oui, je voudrais porter un toast")], "Élise tries to maintain harmony"),
    ("gabriel", "Je porte un toast très clair.",
     "I propose a very clear toast.",
     [(311, "Écoutez bien")], "Gabriel grabs a glass"),
    ("gabriel", "À la fin de nos principes!",
     "To the end of our principles!",
     [(312, "À la mort de nos principes !")], "Gabriel delivers a bitter toast"),
    ("elise", "Ton accueil est vraiment très direct!",
     "Your welcome is really very direct!",
     [(306, "C'est le moins qu'on puisse dire")], "Élise notes the sharp rebuke"),
    ("lea", "Pardon, nous sommes tous très fatigués.",
     "Excuse us, we are all very tired.",
     [(307, "Désolé")], "Andréa tries to smooth over the tension"),
]

WALK = [
    (0, None,
     "'Thank you all for your welcome at ASK.' Elise opens her speech with polite gratitude. "
     "The noun 'accueil' means welcome or reception."),
    (1, None,
     "'Welcome among us to our team.' Andrea greets the newcomer warmly on behalf of the agency. "
     "The preposition 'parmi' means among."),
    (2, None,
     "'I have a somewhat difficult reputation.' Elise frankly acknowledges her ruthless past at StarMedia. "
     "The adjective 'difficile' means difficult."),
    (3, None,
     "'Here, we respect good work.' Andrea emphasizes ASK's professional values. "
     "The verb 'respecter' means to respect."),
    (4, None,
     "'I want to work with you two.' Elise expresses her desire to collaborate with Andrea and Gabriel. "
     "The number 'deux' means two."),
    (5, None,
     "'You are very good agents.' Elise flatters the senior partners of ASK. "
     "The adjective 'bons' modifies the masculine plural noun 'agents'."),
    (6, None,
     "'As for me, I do not have time.' Gabriel coldly rejects her attempts at charm. "
     "The emphatic pronoun 'moi' stresses the subject."),
    (7, None,
     "'Gabriel, stay a moment with us.' Andrea tries to defuse the brewing conflict. "
     "The imperative 'reste' comes from the verb 'rester'."),
    (8, None,
     "'I prefer to return to my office.' Gabriel makes an excuse to leave the reception. "
     "The verb 'retourner' means to go back or return."),
    (9, None,
     "'We can still drink a toast together.' Elise attempts to maintain a convivial atmosphere. "
     "The verb 'trinquer' means to clink glasses or toast."),
    (10, None,
     "'I propose a very clear toast.' Gabriel steps forward with bitter sarcasm. "
     "The expression 'porter un toast' means to raise a toast."),
    (11, None,
     "'To the end of our principles!' Gabriel raises his glass in solemn protest against the buyout. "
     "The noun 'principes' means moral principles."),
    (12, None,
     "'Your welcome is really very direct!' Elise reacts with cool poise to Gabriel's blunt hostility. "
     "The adverb 'vraiment' means really."),
    (13, None,
     "'Excuse us, we are all very tired.' Andrea apologizes to cover for her partner's explosive outburst. "
     "The adjective 'fatigues' means tired."),
]

OUTRO = (
    "Gabriel delivers a scathing toast against Elise Formain before storming back to his desk. "
    "Caught between her defiant colleague and her powerful new associate, Andrea must find a way to navigate the tension. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("gabriel", "Nous n'avons plus aucun principe ici.")
