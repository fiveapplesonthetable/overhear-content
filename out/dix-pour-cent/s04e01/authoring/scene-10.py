# Authoring module for dix-pour-cent s04e01 scene 10 (cues 512-556).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e01/authoring/scene-10.py --out overhear-content/out/dix-pour-cent/s04e01/scene-10.json

ID = "dix-pour-cent-s04e01-scene-10"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 10
TITLE = "La crèche parentale  (The Cooperative Daycare)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 512-556. Andrea arrives late to an enrollment meeting at a cooperative daycare center, "
               "reacting with dismay to the communal cleaning and cooking tasks demanded of parents.")

INTRO = ("At the cooperative daycare center Les Coccinelles, Andrea rushes in late to join Colette for an intake interview. "
         "Expecting a standard childcare facility, Andrea is stunned to discover that parents must take turns cooking meals, "
         "changing diapers, and cleaning rooms. Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Pardon Colette, j'ai été retenue au travail.",
  "Sorry Colette, I was held up at work.",
  [(514, "Désolée, j'ai été retenue au travail.")], "Apologizing for late arrival"),
 ("colette", "Cette crèche parentale demande beaucoup de coopération.",
  "This parent daycare requires a lot of cooperation.",
  [(517, "la crèche Les Coccinelles, c'est avant tout la coopération.")], "Explaining collective philosophy"),
 ("lea", "Qu'est-ce que nous devons faire exactement ici?",
  "What must we do exactly here?",
  [(528, "Donc tout le monde participe :")], "Asking for specific duties"),
 ("colette", "Une demi-journée par semaine avec les enfants.",
  "Half a day a week with the children.",
  [(529, "une demi-journée par semaine pour s'occuper d'un groupe")], "Stating weekly time commitment"),
 ("lea", "S'occuper des repas et des changes?",
  "Taking care of meals and changes?",
  [(532, "Les repas, les changes")], "Questioning physical care chores"),
 ("colette", "Oui, et organiser des ateliers de cuisine.",
  "Yes, and organize cooking workshops.",
  [(533, "des ateliers nature, musique, cuisine.")], "Listing planned educational activities"),
 ("lea", "De la cuisine pour des petits bébés?",
  "Cooking for tiny babies?",
  [(534, "Cuisine ? Pour six bébés de 6 mois ?")], "Expressing disbelief at baby cooking"),
 ("colette", "Ils pétrissent de la pâte avec de la farine.",
  "They knead dough with flour.",
  [(536, "Ça consiste surtout à pétrir de la pâte et jouer dans la farine.")], "Clarifying sensory play"),
 ("lea", "On doit aussi nettoyer toute la maison?",
  "Do we also have to clean the whole house?",
  [(537, "On doit aussi faire le ménage ?")], "Asking about cleaning duties"),
 ("colette", "Arrête Andréa, nous n'avons rien trouvé d'autre.",
  "Stop Andrea, we found nothing else.",
  [(542, "Rappelle-toi qu'on est là parce qu'on n'a rien trouvé d'autre.")], "Reminding her of lack of options"),
 ("lea", "Je croyais payer pour une vraie aide.",
  "I thought we paid for real help.",
  [(540, "Désolée, je n'avais pas réalisé")], "Expressing private daycare expectations"),
 ("colette", "J'ai besoin de reprendre une vie normale.",
  "I need to return to a normal life.",
  [(547, "j'ai besoin de retrouver une vie normale.")], "Stressing need for personal recovery"),
 ("lea", "D'accord, je ferai des efforts pour nous.",
  "Okay, I will make efforts for us.",
  [(550, "Et on pourra avoir du temps pour nous.")], "Yielding to save family balance"),
 ("colette", "Merci, Flora sera très heureuse parmi eux.",
  "Thank you, Flora will be very happy among them.",
  [(549, "un tout petit peu d'amour pour les enfants des autres")], "Reassuring her about baby wellbeing"),
]

WALK = [
 (0, None,
  "'Sorry Colette, I was held up at work.' Andrea apologizes for her delayed arrival. "
  "The passive phrase 'ai ete retenue' indicates being detained by obligations."),
 (1, None,
  "'This parent daycare requires a lot of cooperation.' Colette introduces the cooperative model. "
  "The noun 'creche' designates an infant daycare center in France."),
 (2, None,
  "'What must we do exactly here?' Andrea asks for precise expectations. "
  "The interrogative phrase 'qu'est-ce que' asks what."),
 (3, None,
  "'Half a day a week with the children.' Colette details the mandatory parent shifts. "
  "The compound noun 'demi-journee' means a half-day."),
 (4, None,
  "'Taking care of meals and changes?' Andrea lists basic nursery tasks. "
  "The reflexive verbal idiom 's'occuper de' means to take care of."),
 (5, None,
  "'Yes, and organize cooking workshops.' Colette explains the participatory curriculum. "
  "The noun 'atelier' refers to a workshop or activity group."),
 (6, None,
  "'Cooking for tiny babies?' Andrea balks at the thought of culinary infants. "
  "The noun 'bebe' designates an infant."),
 (7, None,
  "'They knead dough with flour.' Colette clarifies the tactile activity. "
  "The verb 'petrir' means to knead bread or pastry dough."),
 (8, None,
  "'Do we also have to clean the whole house?' Andrea questions having to clean up. "
  "The verb 'nettoyer' means to clean."),
 (9, None,
  "'Stop Andrea, we found nothing else.' Colette insists on their lack of childcare alternatives. "
  "The negative phrase 'rien... d'autre' means nothing else."),
 (10, None,
  "'I thought we paid for real help.' Andrea expected outsourced nursery staff. "
  "The imperfect 'croyais' reflects a mistaken prior assumption."),
 (11, None,
  "'I need to return to a normal life.' Colette expresses her longing for routine and career. "
  "The verbal idiom 'avoir besoin de' expresses personal necessity."),
 (12, None,
  "'Okay, I will make efforts for us.' Andrea accepts the compromise for their couple. "
  "The future 'ferai' indicates a promise to make an effort."),
 (13, None,
  "'Thank you, Flora will be very happy among them.' Colette appreciates Andrea's concession. "
  "The preposition 'parmi' expresses inclusion among a group."),
]

OUTRO = ("Andrea agrees to the cooperative daycare chores so that Colette can finally return to work. "
         "Balancing demanding agency leadership with toddler duties will be Andrea's newest daily challenge. "
         "Now, let's review the scene one last time.")

CLOSING = ("colette", "Merci, Flora sera très heureuse parmi eux.")
