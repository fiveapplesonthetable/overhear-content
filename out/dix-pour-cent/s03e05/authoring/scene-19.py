# Authoring module for dix-pour-cent s03e05 scene 19 (cues 783-792).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e05/authoring/scene-19.py --out overhear-content/out/dix-pour-cent/s03e05/scene-19.json

ID = "dix-pour-cent-s03e05-scene-19"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 19
TITLE = "Fausse déception  (Feigned Disappointment)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "hicham": "marcel"}
LABELS = {"lea": "Noémie", "mathias": "Mathias", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 783-792. In his office, Mathias takes a phone call from Hicham and puts on "
    "a masterful display of fake dismay over Solaris signing the rival co-production deal."
)

INTRO = (
    "In his office at ASK, Mathias receives a phone call from Hicham. "
    "Hicham announces that Solaris has signed the rival co-production deal. "
    "Mathias feigns total devastation while Noemie listens in secrecy. "
    "Listen to the scene in French first."
)

STORY = [
    ("mathias", "Allô, Hicham? Comment vas-tu?",
     "Hello, Hicham? How are you doing?",
     [(783, "Allo")], ""),
    ("hicham", "Ils ont signé hier soir le contrat.",
     "They signed the contract yesterday evening.",
     [(784, "signé hier soir le deal")], ""),
    ("mathias", "Ce n'est pas vrai, c'est signé?",
     "It is not true, it is signed?",
     [(784, "Non c'est pas vrai")], ""),
    ("hicham", "Oui, le deal de coproduction est fait.",
     "Yes, the co-production deal is done.",
     [(784, "deal de copro avec Solaris")], ""),
    ("mathias", "Je ne savais pas du tout cela.",
     "I did not know that at all.",
     [(785, "je savais pas du tout")], ""),
    ("mathias", "Franchement, je suis totalement consterné.",
     "Frankly, I am totally dismayed.",
     [(786, "Je suis consterné")], ""),
    ("mathias", "C'est vraiment une terrible malchance.",
     "It is really terrible bad luck.",
     [(787, "C'est vraiment pas de chance")], ""),
    ("hicham", "Nous avons perdu ce projet ensemble.",
     "We lost this project together.",
     [(788, "ce qu'on peut faire de plus")], ""),
    ("mathias", "Je ne vois rien d'autre à faire.",
     "I see nothing else to do.",
     [(788, "vois vraiment pas ce qu'on peut faire")], ""),
    ("mathias", "Je suis vraiment navré, Hicham.",
     "I am truly sorry, Hicham.",
     [(790, "Vraiment navré Hicham")], ""),
    ("hicham", "Merci, on se voit demain au bureau.",
     "Thank you, see you tomorrow at the office.",
     [(791, "à demain")], ""),
    ("mathias", "Oui, à demain. Salut, Hicham.",
     "Yes, see you tomorrow. Bye, Hicham.",
     [(791, "Ouais toi aussi à demain"), (792, "Salut")], ""),
    ("lea", "Il a tout cru sans hésiter?",
     "He believed everything without hesitating?",
     [(790, "navré Hicham")], ""),
    ("mathias", "Absolument, notre secret est bien gardé.",
     "Absolutely, our secret is well kept.",
     [(792, "Salut")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Hello, Hicham? How are you doing?' Mathias answers the phone with polite calm. "
     "The casual greeting masks his secret agenda."),
    (1, None,
     "'They signed the contract yesterday evening.' Hicham delivers the bad news about the rival deal. "
     "The past tense reports the signing."),
    (2, None,
     "'It is not true, it is signed?' Mathias feigns complete disbelief. "
     "The question displays manufactured shock."),
    (3, None,
     "'Yes, the co-production deal is done.' Hicham confirms the deal with Solaris. "
     "The short confirmation expresses defeat."),
    (4, None,
     "'I did not know that at all.' Mathias denies any prior knowledge. "
     "The emphatic negative phrase reinforces his innocent facade."),
    (5, None,
     "'Frankly, I am totally dismayed.' He exaggerates his emotional distress. "
     "The adverb emphasizes his fake grief."),
    (6, None,
     "'It is really terrible bad luck.' Mathias laments the supposed stroke of misfortune. "
     "The strong adjective intensifies the regret."),
    (7, None,
     "'We lost this project together.' Hicham mourns their mutual loss. "
     "The plural pronoun stresses agency solidarity."),
    (8, None,
     "'I see nothing else to do.' Mathias claims total helplessness. "
     "The negative structure closes off further action."),
    (9, None,
     "'I am truly sorry, Hicham.' He offers condolences to his rival boss. "
     "The courteous adjective sounds completely genuine."),
    (10, None,
     "'Thank you, see you tomorrow at the office.' Hicham thanks him and ends the call. "
     "The farewell sets up tomorrow's meeting."),
    (11, None,
     "'Yes, see you tomorrow. Bye, Hicham.' Mathias says goodbye and hangs up. "
     "The quick farewell concludes the fake call."),
    (12, None,
     "'He believed everything without hesitating?' Noemie asks if the boss fell for the trick. "
     "The prepositional phrase highlights the deceit."),
    (13, None,
     "'Absolutely, our secret is well kept.' Mathias smiles with triumph. "
     "The passive construction reassures his accomplice.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Mathias's cunning act keeps Hicham completely in the dark about his secret maneuvers. "
    "Listen to the conversation once more in French."
)

CLOSING = ("mathias", "Notre plan fonctionne à la perfection.")
