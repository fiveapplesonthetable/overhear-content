# Authoring module for dix-pour-cent s03e06 scene 03 (cues 231-315).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e06/authoring/scene-03.py --out out/dix-pour-cent/s03e06/scene-03.json

ID = "dix-pour-cent-s03e06-scene-03"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 3
TITLE = "L'autre Isabelle  (The Other Isabelle)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "arlette": "emilie"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel", "arlette": "Arlette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 231-315. Andrea, Gabriel, and Arlette devise a daring plan to counter the Americans using a namesake of Isabelle Huppert. Adapted for A1 French.")

INTRO = ("Behind closed doors, Andrea, Gabriel, and Arlette brainstorm frantically to neutralize the American studio's lawsuit. "
         "Determined to break Mathias's leverage before he announces his takeover, Andrea conceives an audacious scheme: finding a namesake to claim she played the disputed role. "
         "When Arlette suggests casting the stranger as a ghost, an eccentric plan is born. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Mathias compte résoudre cette crise seul.",
  "Mathias intends to resolve this crisis alone.",
  [(231, "résoudre le Huppergate")], "Analyzed rival's strategic advantage"),
 ("lea", "Nous devons contrer les Américains avant lui.",
  "We must counter the Americans before him.",
  [(232, "contrer les Américains avant lui")], "Urged preemptive strategic strike"),
 ("gabriel", "Isabelle Huppert a signé une exclusivité stricte.",
  "Isabelle Huppert signed strict exclusivity.",
  [(234, "signé un contrat d'exclusivité")], "Recalled contractual impediment"),
 ("lea", "Et s'il existait une autre Isabelle?",
  "And what if another Isabelle existed?",
  [(237, "deux Isabelle Huppert")], "Posed inventive legal hypothesis"),
 ("gabriel", "Tu veux trouver une simple homonyme?",
  "You want to find a simple namesake?",
  [(244, "Une meuf qui s'appelle vraiment")], "Sought clarification on wild scheme"),
 ("gabriel", "J'ai trouvé deux personnes portant ce nom.",
  "I found two people bearing this name.",
  [(249, "une à Gentilly et l'autre à Épernay")], "Discovered real namesake candidates"),
 ("gabriel", "Mais le rôle était Marie de Médicis!",
  "But the role was Marie de' Medici!",
  [(257, "Marie de Médicis")], "Raised casting objection"),
 ("arlette", "L'homonyme peut jouer le personnage mort.",
  "The namesake can play the dead character.",
  [(269, "Marie de Médicis, mais morte")], "Formulated surreal creative compromise"),
 ("lea", "Son fantôme, c'est une idée brillante!",
  "Her ghost is a brilliant idea!",
  [(270, "son fantôme, c'est excellent")], "Enthusiastically embraced creative solution"),
 ("arlette", "C'est poétique et digne de Cocteau.",
  "It is poetic and worthy of Cocteau.",
  [(277, "c'est très cocteau")], "Praised artistic quality of ruse"),
 ("lea", "Nous devons tourner cette scène immédiatement.",
  "We must shoot this scene immediately.",
  [(284, "il faut écrire une scène")], "Called for urgent filming action"),
 ("gabriel", "Il faut terminer cela avant ce soir.",
  "We must finish this before tonight.",
  [(285, "Avant ce soir")], "Stressed strict evening deadline"),
 ("lea", "Nous préviendrons l'actrice si cela fonctionne.",
  "We will notify the actress if this works.",
  [(312, "On lui dira seulement si ça marche")], "Decided to keep star uninformed"),
 ("gabriel", "Au travail pour sauver notre agence!",
  "To work to save our agency!",
  [(285, "Avant ce soir")], "Rallied partners to execute scheme"),
]

OPENER = "Let's observe as Andrea, Gabriel, and Arlette plan an audacious counter-offensive."

WALK = [
 (0, None,
  "'Mathias intends to resolve this crisis alone.' A strategic observation identifying the rival's primary source of leverage."),
 (1, None,
  "'We must counter the Americans before him.' An urgent call to action demanding a preemptive strike."),
 (2, None,
  "'Isabelle Huppert signed strict exclusivity.' A sobering reminder of the legal barrier posed by the contract."),
 (3, None,
  "'And what if another Isabelle existed?' A provocative theoretical question opening up an unexpected loophole."),
 (4, None,
  "'You want to find a simple namesake?' A skeptical query seeking clarity on an improbable legal ruse."),
 (5, None,
  "'I found two people bearing this name.' A surprising factual update identifying two potential namesakes in phone registries."),
 (6, None,
  "'But the role was Marie de' Medici!' A practical objection highlighting the difficulty of casting a non-actor as a queen."),
 (7, None,
  "'The namesake can play the dead character.' An inspired creative compromise proposing to cast her as a deceased figure."),
 (8, None,
  "'Her ghost is a brilliant idea!' An ecstatic endorsement adopting the supernatural acting concept."),
 (9, None,
  "'It is poetic and worthy of Cocteau.' An artistic validation referencing celebrated cinema tradition."),
 (10, None,
  "'We must shoot this scene immediately.' A decisive operational order mandating an immediate emergency film shoot."),
 (11, None,
  "'We must finish this before tonight.' A temporal constraint emphasizing the deadline of the anniversary gala."),
 (12, None,
  "'We will notify the actress if this works.' A cautious protective decision shielding their star talent from unnecessary anxiety."),
 (13, None,
  "'To work to save our agency!' A passionate rally urging immediate collaborative action."),
]

TRANSITION = "Now let's listen to the trio elaborating their scheme again at full speed."

OUTRO = ("Armed with an eccentric yet ingenious plan, Andrea and Gabriel rush to film the mock scene before the party begins. "
         "If their desperate gamble succeeds, they will dismantle Mathias's leverage and protect ASK from financial devastation.")

CLOSING = ("lea", "Le fantôme va nous sauver.")
