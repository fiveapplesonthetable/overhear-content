# Authoring module for dix-pour-cent s02e05 scene 08 (cues 221-257).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e05/authoring/scene-08.py --out out/dix-pour-cent/s02e05/scene-08.json

ID = "dix-pour-cent-s02e05-scene-08"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 8
TITLE = "Remplacer Guy Marchand  (Pulling Guy Out)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "mathias": "marcel"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 221-257. In the ASK conference room, Gabriel, Andréa, and Mathias discuss Guy Marchand's health "
               "and debate the economic decision to replace him before the shoot fails. "
               "Adapted for A1 French.")

INTRO = ("In the ASK conference room, Gabriel updates Andrea and Mathias on Guy Marchand's health. "
         "The team debates whether it is better to replace the veteran actor before the shoot collapses. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Alors, comment va notre cher Guy Marchand?",
  "So, how is our dear Guy Marchand?",
  [(223, "Alors, comment va Guy Marchand ?")], "Andrea asks for an update"),
 ("gabriel", "Le producteur ne veut plus continuer avec lui.",
  "The producer no longer wants to continue with him.",
  [(226, "Le producteur dit qu'il ne veut plus continuer avec Guy.")], "Gabriel shares the producer's decision"),
 ("gabriel", "La réalisatrice panique sur le tournage.",
  "The director is panicking on the film set.",
  [(227, "La réalisatrice le veut, mais elle panique.")], "Gabriel describes the director's anxiety"),
 ("mathias", "Ils tournent sans lui pour l'instant?",
  "Are they shooting without him for now?",
  [(230, "ils tournent sans lui pour l'instant")], "Mathias asks about the schedule"),
 ("gabriel", "Oui, mais ça ne peut pas durer.",
  "Yes, but that cannot go on.",
  [(231, "mais ça ne peut pas durer éternellement.")], "Gabriel warns it is unsustainable"),
 ("mathias", "J'ai d'excellents retours sur mon fils Hippolyte.",
  "I have excellent feedback about my son Hippolyte.",
  [(232, "J'ai d'excellents retours sur Hippolyte.")], "Mathias mentions his son"),
 ("lea", "Guy ne pourra jamais tenir huit semaines.",
  "Guy will never be able to hold on for eight weeks.",
  [(236, "Je ne pense pas qu'il puisse tenir huit semaines.")], "Andrea doubts Guy's endurance"),
 ("gabriel", "J'ai peur qu'on finisse par le griller.",
  "I am afraid we will end up burning him out.",
  [(238, "mais j'ai peur qu'on finisse par le griller.")], "Gabriel worries about Guy"),
 ("mathias", "Il est plus économique de le remplacer tôt.",
  "It is more economical to replace him early.",
  [(240, "Il est plus économique de le remplacer tôt")], "Mathias analyzes the finances"),
 ("lea", "Ces rôles sont précieux pour son âge.",
  "These roles are precious for his age.",
  [(243, "mais ces rôles sont précieux pour un acteur de son âge.")], "Andrea defends the veteran actor"),
 ("mathias", "Un film qui explose est mauvais pour tous.",
  "A movie that collapses is bad for everyone.",
  [(255, "Un film qui explose en plein vol, c'est mauvais pour lui comme pour nous.")], "Mathias warns of disaster"),
 ("lea", "Gabriel, c'est toi qui dois lui parler.",
  "Gabriel, you are the one who must speak to him.",
  [(256, "Alors, Gabriel, tu lui diras, hein ?")], "Andrea delegates the difficult talk"),
 ("gabriel", "D'accord, je vais lui annoncer la nouvelle.",
  "All right, I am going to break the news to him.",
  [(250, "D'accord."), (257, "Bien.")], "Gabriel accepts the painful task"),
]

OPENER = "Let's examine the partners' tense agency debate step by step to understand the business pressures on actors."

WALK = [
 (0, None,
  "'So, how is our dear Guy Marchand?' Andrea asks for news after Gabriel's check-in with the production."),
 (1, None,
  "'The producer no longer wants to continue with him.' Gabriel delivers the bad news from the producer."),
 (2, None,
  "'The director is panicking on the film set.' Gabriel explains that the director is losing confidence."),
 (3, None,
  "'Are they shooting without him for now?' Mathias checks how the production is coping with the absence."),
 (4, None,
  "'Yes, but that cannot go on.' Gabriel emphasizes that temporary schedule changes have limits."),
 (5, None,
  "'I have excellent feedback about my son Hippolyte.' Mathias notes that his son is performing well on set."),
 (6, None,
  "'Guy will never be able to hold on for eight weeks.' Andrea points out the unrealistic physical demands."),
 (7, None,
  "'I am afraid we will end up burning him out.' Gabriel fears that pushing the veteran actor will ruin his reputation."),
 (8, None,
  "'It is more economical to replace him early.' Mathias argues from a pragmatic financial perspective."),
 (9, None,
  "'These roles are precious for his age.' Andrea reminds them how rare major parts are for older actors."),
 (10, None,
  "'A movie that collapses is bad for everyone.' Mathias insists that a failed production damages all involved."),
 (11, None,
  "'Gabriel, you are the one who must speak to him.' Andrea instructs Gabriel to handle the sensitive conversation."),
 (12, None,
  "'All right, I am going to break the news to him.' Gabriel reluctantly agrees to talk to Guy."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Faced with the harsh realities of film production, the agents must balance financial risk against artistic loyalty. "
         "Let's review the key vocabulary and professional expressions from this scene.")

CLOSING = ("gabriel", "D'accord, je vais lui annoncer la nouvelle.")
