# Authoring module for dix-pour-cent s04e01 scene 06 (cues 461-486).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-06.py --out out/dix-pour-cent/s04e01/scene-06.json

ID = "dix-pour-cent-s04e01-scene-06"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 6
TITLE = "La signature de Mathias  (Mathias's Signature)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "marcel", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "mathias": "Mathias", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 461-486. Mathias officially signs the shareholder agreement to leave ASK, delivering a solemn "
               "farewell speech while Andrea and Gabriel question his secretive future plans.")

INTRO = ("At the ASK agency, Mathias signs the final legal paperwork selling his shares and ending his tenure. "
         "As he delivers an emotional farewell speech, Andrea and Gabriel react with skeptical questions. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("mathias", "Voilà, le pacte d'actionnaires est signé.",
     "There, the shareholder agreement is signed.",
     [(461, "Il ne reste plus qu'à signer le pacte d'actionnaires.")], "Mathias completes the legal buyout documents"),
    ("mathias", "Puis-je dire quelques mots avant de partir?",
     "May I say a few words before leaving?",
     [(463, "Puis-je dire quelques mots ?")], "Mathias asks for permission to address the room"),
    ("lea", "Fais vite, nous avons beaucoup de travail.",
     "Make it quick, we have lots of work.",
     [(464, "Comme vous voulez.")], "Andrea shows impatience with his formal posturing"),
    ("mathias", "Mon départ s'est fait dans une ambiance hostile.",
     "My departure took place in a hostile atmosphere.",
     [(465, "mon départ s'est déroulé dans une atmosphère plutôt hostile.")], "Mathias remarks on the bitter tension during the split"),
    ("mathias", "Cette agence a été toute ma vie.",
     "This agency has been my whole life.",
     [(468, "Cette agence a tellement fait partie de moi")], "Mathias recalls his deep devotion to the firm"),
    ("mathias", "Pour moi, c'est un véritable crève-cœur.",
     "For me, it is a real heartbreak.",
     [(469, "ça a été un crève-cœur.")], "Mathias expresses genuine grief over stepping down"),
    ("lea", "Pour nous, c'est plutôt un soulagement.",
     "For us, it is rather a relief.",
     [(470, "C'est plutôt un soulagement, en ce qui me concerne.")], "Andrea counters bluntly from the partners' perspective"),
    ("gabriel", "C'est une blessure qui ne guérira jamais.",
     "It is a wound that will never heal.",
     [(471, "C'est une blessure qui ne guérira jamais, en ce qui me concerne.")], "Gabriel reflects on personal betrayal among partners"),
    ("mathias", "Je souhaite tout le meilleur à notre agence.",
     "I wish all the best to our agency.",
     [(472, "souhaiter tout le meilleur à l'Agence Samuel Kerr.")], "Mathias offers cordial parting wishes to ASK"),
    ("gabriel", "Où vas-tu maintenant? Tu ouvres une boîte?",
     "Where are you going now? Are you opening an agency?",
     [(475, "Où vas-tu ensuite ?"), (476, "Tu ouvres une agence ?")], "Gabriel presses him on rumors of a competing firm"),
    ("mathias", "Vous le saurez au bon moment.",
     "You will know at the right time.",
     [(478, "Vous le saurez en temps voulu.")], "Mathias remains deliberately elusive about his plans"),
    ("mathias", "Mon choix protège l'avenir de tout le monde.",
     "My choice protects everyone's future.",
     [(481, "ma décision était la plus")], "Mathias claims he acted in the best interest of the firm"),
    ("lea", "Bien sûr, on te croit sur parole!",
     "Of course, we believe your word!",
     [(483, "Ouais, on te croit vraiment.")], "Andrea delivers a sarcastic closing remark"),
]

OPENER = "Let's examine Mathias's farewell speech and his colleagues' reactions line by line."

WALK = [
    (0, None,
     "'There, the shareholder agreement is signed.' Mathias confirms that the legal transfer of his shares is finalized."),
    (1, None,
     "'May I say a few words before leaving?' Mathias asks his former partners for an opportunity to say goodbye."),
    (2, None,
     "'Make it quick, we have lots of work.' Andrea urges him to keep his statement brief so they can return to business."),
    (3, None,
     "'My departure took place in a hostile atmosphere.' Mathias notes the intense antagonism that accompanied the buyout."),
    (4, None,
     "'This agency has been my whole life.' Mathias reminds the team how deeply tied he was to ASK's history."),
    (5, None,
     "'For me, it is a real heartbreak.' Mathias characterizes the rupture as an emotional tragedy for himself."),
    (6, None,
     "'For us, it is rather a relief.' Andrea retorts that his departure lifts a heavy burden from the remaining staff."),
    (7, None,
     "'It is a wound that will never heal.' Gabriel highlights the lasting emotional scar left by Mathias's plotting."),
    (8, None,
     "'I wish all the best to our agency.' Mathias maintains a polite facade and offers well wishes to Samuel Kerr."),
    (9, None,
     "'Where are you going now? Are you opening an agency?' Gabriel demands to know if Mathias plans to start a rival enterprise."),
    (10, None,
     "'You will know at the right time.' Mathias conceals his next career move until the official launch."),
    (11, None,
     "'My choice protects everyone's future.' Mathias insists his buyout preserves the agency's stability."),
    (12, None,
     "'Of course, we believe your word!' Andrea mocks Mathias's lofty justifications with sharp irony."),
]

TRANSITION = "Now let's listen to Mathias's departure speech once more from start to finish."

OUTRO = ("Mathias leaves ASK after signing the buyout agreement, keeping his next career destination shrouded in mystery. "
         "Let's review the key professional departure terms from this scene.")

CLOSING = ("lea", "Bien sûr, on te croit sur parole!")
