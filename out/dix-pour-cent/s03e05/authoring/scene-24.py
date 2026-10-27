# Authoring module for dix-pour-cent s03e05 scene 24 (cues 1001-1025).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-24.py --out out/dix-pour-cent/s03e05/scene-24.json

ID = "dix-pour-cent-s03e05-scene-24"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 24
TITLE = "Au bord du précipice  (On the Edge of the Precipice)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1001-1025. In a quiet Parisian bar, Andrea enjoys her first night out since giving birth, having drinks with Hicham. "
    "Confronted by the mounting turmoil at ASK, they both admit that walking away right now would be a terrible mistake."
)

INTRO = (
    "In a quiet Parisian bar, Andrea enjoys her first night out since giving birth, having drinks with Hicham. "
    "Confronted by the mounting turmoil at ASK, they both admit that walking away right now would be a terrible mistake. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("hicham", "Tu as laissé Colette seule ce soir?",
     "Did you leave Colette alone tonight?",
     [(1004, "tu plantes ta femme")], "Inquired about her family evening"),
    ("lea", "Sa mère est présente à la maison.",
     "Her mother is present at the house.",
     [(1005, "sa mère à la maison")], "Explained the home babysitting support"),
    ("lea", "C'est ma première sortie depuis un mois.",
     "It is my first outing in a month.",
     [(1010, "Première sortie depuis un mois")], "Celebrated her brief evening freedom"),
    ("hicham", "Nous devons pourtant parler de l'agence.",
     "Yet we must talk about the agency.",
     [(1007, "il faut qu'on parle boulot"), (1011, "parle de l'agence")], "Steered the conversation toward agency matters"),
    ("lea", "Laisse-moi savourer mon verre deux minutes.",
     "Let me savor my drink two minutes.",
     [(1009, "deux minutes là")], "Asked for a brief relaxing pause"),
    ("hicham", "La situation chez ASK devient très critique.",
     "The situation at ASK is becoming critical.",
     [(1015, "chez la SK")], "Highlighted the fragile company climate"),
    ("lea", "Ce n'est plus le moment de partir.",
     "It is no longer the time to leave.",
     [(1016, "plus du tout le moment de partir")], "Admitted that leaving now is impossible"),
    ("hicham", "As-tu parlé de cela avec Mathias?",
     "Did you speak about that with Mathias?",
     [(1017, "parlé avec Mathias")], "Asked whether Mathias was consulted"),
    ("lea", "Non, mais je vois bien les problèmes.",
     "No, but I clearly see the problems.",
     [(1018, "je vois bien")], "Recognized the looming operational threats"),
    ("hicham", "Nous ne pouvons pas abandonner l'équipe.",
     "We cannot abandon the team.",
     [(1019, "on peut pas partir")], "Appealed to collective agency loyalty"),
    ("lea", "Je ne veux rien gâcher entre nous.",
     "I do not want to ruin anything between us.",
     [(1021, "pas trop envie de tout gâcher")], "Refused to destroy their mutual connection"),
    ("hicham", "Je suis profondément soulagé de t'entendre.",
     "I am deeply relieved to hear you.",
     [(1022, "je suis soulagé")], "Expressed huge emotional relief"),
    ("lea", "Nous étions vraiment au bord du précipice.",
     "We were truly on the edge of the cliff.",
     [(1025, "au bord du bord")], "Acknowledged the close brush with disaster"),
    ("hicham", "Finalement, personne ne veut sauter dans l'inconnu.",
     "Ultimately, nobody wants to jump into the unknown.",
     [(1025, "envie de sauter")], "Concluded that neither wishes to defect")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Did you leave Colette alone tonight?' Hicham asks Andrea about her domestic evening. "
     "The compound past question opens the informal bar conversation."),
    (1, None,
     "'Her mother is present at the house.' Andrea explains that family is helping at home. "
     "The simple descriptive sentence clarifies the babysitting situation."),
    (2, None,
     "'It is my first outing in a month.' Andrea savors a rare break from infant childcare. "
     "The temporal prepositional phrase highlights the long passage of time."),
    (3, None,
     "'Yet we must talk about the agency.' Hicham tries to address the crisis at ASK. "
     "The modal verb of obligation redirects attention to business."),
    (4, None,
     "'Let me savor my drink two minutes.' Andrea asks for a brief moment of quiet pleasure. "
     "The imperative verb requests a momentary pause before discussing problems."),
    (5, None,
     "'The situation at ASK is becoming critical.' Hicham outlines the acute stress at the agency. "
     "The linking verb with an adjective paints a grim picture."),
    (6, None,
     "'It is no longer the time to leave.' Andrea realizes walking away right now would be fatal. "
     "The negative temporal structure confirms a change of heart."),
    (7, None,
     "'Did you speak about that with Mathias?' Hicham checks if senior partners are aligned. "
     "The inverted compound past question asks about internal discussions."),
    (8, None,
     "'No, but I clearly see the problems.' Andrea observes the ongoing damage firsthand. "
     "The sensory verb emphasizes clear personal awareness."),
    (9, None,
     "'We cannot abandon the team.' Hicham appeals to their shared commitment to ASK. "
     "The modal construction rejects walking out on colleagues."),
    (10, None,
     "'I do not want to ruin anything between us.' Andrea acknowledges the value of their partnership. "
     "The negative verbal structure emphasizes preserving mutual trust."),
    (11, None,
     "'I am deeply relieved to hear you.' Hicham lets out a long sigh of emotional release. "
     "The passive construction conveys genuine reassurance."),
    (12, None,
     "'We were truly on the edge of the cliff.' Andrea looks back at their close brush with disaster. "
     "The imperfect verb with the prepositional idiom vividly evokes standing on a dangerous ledge."),
    (13, None,
     "'Ultimately, nobody wants to jump into the unknown.' Hicham sums up their collective decision to stay. "
     "The negative indefinite pronoun emphasizes unanimous hesitation.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "In a relaxed Parisian bar, Andrea and Hicham realize that staying together at ASK matters more than jumping into the void. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("hicham", "Finalement, personne ne veut sauter dans l'inconnu.")
