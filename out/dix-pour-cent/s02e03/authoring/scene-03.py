# Authoring module for dix-pour-cent s02e03 scene 03 (cues 68-91).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-03.py --out out/dix-pour-cent/s02e03/scene-03.json

ID = "dix-pour-cent-s02e03-scene-03"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 3
TITLE = "Petit-déjeuner avec maman  (Breakfast with Mom)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "annick": "emilie"}
LABELS = {"lea": "Camille", "annick": "Annick"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 68-91. Camille and her mother Annick have breakfast in Paris. "
               "Annick asks about Mathias, and Camille rushes off to work. Adapted for A1 French.")

INTRO = ("In her small Parisian apartment, Camille Valentini has a hurried breakfast with her visiting mother, "
         "Annick. While Annick comments on celebrity hairstyles and asks about Camille's relationship with Mathias, "
         "Camille tries not to be late for work. Let's listen to the scene in French first.")

STORY = [
 ("annick", "Tu ne prends pas de petit-déjeuner?",
  "Are you not having breakfast?",
  [(68, "Pas de petit-déjeuner ?")], "Expanded to full question"),
 ("lea", "Maman, je suis très en retard.",
  "Mom, I am very late.",
  [(69, "Maman, je suis en retard.")], "Added intensive adverb"),
 ("annick", "Assieds-toi et mange un peu.",
  "Sit down and eat a little.",
  [(70, "Camille, assieds-toi, mange quelque chose.")], "Simplified eating imperative"),
 ("annick", "Qui coiffe cette pauvre actrice?",
  "Who styles this poor actress's hair?",
  [(72, "Qui coiffe Vanessa Paradis ?")], "Generalised celebrity reference"),
 ("lea", "Les agents ne s'occupent pas des coiffures.",
  "Agents do not deal with hairstyles.",
  [(75, "Les agents ne sont pas consultés pour les coiffures ?"), (76, "Pas vraiment, maman.")], "Transformed to declarative role explanation"),
 ("annick", "Dis-moi, Mathias est gentil avec toi?",
  "Tell me, is Mathias nice to you?",
  [(77, "Mathias est gentil avec toi ?")], "Added conversational marker"),
 ("lea", "Oui, il est bien plus gentil qu'avant.",
  "Yes, he is much nicer than before.",
  [(79, "Bien plus qu'avant.")], "Added full affirmative clause"),
 ("lea", "On se voit et on déjeune ensemble.",
  "We see each other and have lunch together.",
  [(80, "On se voit, on déjeune parfois...")], "Formulated paired daily actions"),
 ("lea", "Regarde, il m'a offert une jolie lampe.",
  "Look, he gave me a pretty lamp.",
  [(81, "Il m'a offert une lampe."), (82, "Elle est belle, non ?")], "Combined gift display"),
 ("annick", "C'est facile quand on est très riche.",
  "It is easy when one is very rich.",
  [(83, "C'est facile quand on est riche.")], "Added emphasis on wealth"),
 ("lea", "J'allume ta belle bougie tous les soirs.",
  "I light your lovely candle every evening.",
  [(84, "Maman, j'allume ta bougie à la lavande tous les soirs.")], "Simplified candle description"),
 ("annick", "J'aurais dû garder un enfant à la maison.",
  "I should have kept a child at home.",
  [(85, "J'aurais dû avoir plus d'enfants"), (86, "et en garder un à la maison.")], "Consolidated maternal regret"),
 ("lea", "Tu as un vrai don pour le drame.",
  "You have a real gift for drama.",
  [(88, "Tu as un don pour ça.")], "Clarified theatrical talent"),
 ("annick", "Fais bien attention sur ton vélo.",
  "Be very careful on your bicycle.",
  [(90, "Fais attention sur ton vélo.")], "Reinforced protective maternal warning"),
]

OPENER = "Let's examine how Annick and Camille discuss family and work over breakfast."

WALK = [
 (0, None,
  "'Are you not having breakfast?' A negative question expressing maternal concern."),
 (1, None,
  "'Mom, I am very late.' An adverb of degree emphasizing time pressure."),
 (2, None,
  "'Sit down and eat a little.' A coordinated pair of imperative verbs."),
 (3, None,
  "'Who styles this poor actress's hair?' An interrogative pronoun followed by a critical remark."),
 (4, None,
  "'Agents do not deal with hairstyles.' A pronominal verb defining professional scope."),
 (5, None,
  "'Tell me, is Mathias nice to you?' An introductory imperative prompting personal news."),
 (6, None,
  "'Yes, he is much nicer than before.' A comparative adverb construction showing improvement."),
 (7, None,
  "'We see each other and have lunch together.' Reciprocal pronominal actions in informal speech."),
 (8, None,
  "'Look, he gave me a pretty lamp.' A compound past verb showing a thoughtful gift."),
 (9, None,
  "'It is easy when one is very rich.' A cynical observation using an impersonal subject pronoun."),
 (10, None,
  "'I light your lovely candle every evening.' A temporal routine phrase reassuring her mother."),
 (11, None,
  "'I should have kept a child at home.' A past conditional expressing nostalgic maternal longing."),
 (12, None,
  "'You have a real gift for drama.' A playful observation acknowledging maternal melodrama."),
 (13, None,
  "'Be very careful on your bicycle.' An idiomatic imperative of caution for city cycling."),
]

TRANSITION = "Now let's listen to Camille and Annick's morning conversation again at full speed."

OUTRO = ("Annick's visit reminds Camille of her complicated family situation, as Mathias remains her secret father. "
         "Despite the maternal guilt, Camille hurries out the door to face another busy day at the agency.")

CLOSING = ("lea", "À ce soir, maman!")
