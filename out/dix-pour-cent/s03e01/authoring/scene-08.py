# Authoring module for dix-pour-cent s03e01 scene 08 (cues 161-172).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-08.py --out out/dix-pour-cent/s03e01/scene-08.json

ID = "dix-pour-cent-s03e01-scene-08"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 8
TITLE = "Comme dans The Revenant  (Like in The Revenant)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "maxime": "theo"}
LABELS = {"lea": "Andréa", "maxime": "Maxime"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 161-172. Andrea shows producer Maxime confidential footage of Jean Dujardin "
               "completely lost in his method acting, eating a raw rabbit in the forest. "
               "Adapted for A1 French.")

INTRO = ("Andrea plays confidential video rushes of Jean Dujardin acting like a feral beast in the wilderness. "
         "Producer Maxime watches in horror as Andrea compares Dujardin's extreme performance to Leonardo DiCaprio in The Revenant. "
         "Let's listen to the scene in French first.")

STORY = [
 ("maxime", "La réalisatrice crie que la prise est coupée!",
  "The director is shouting that the take is cut!",
  [(161, "Coupé."), (162, "Jean, c'est coupé.")], "Maxime reacts to the video"),
 ("lea", "Jean continue de jouer malgré l'ordre d'arrêter.",
  "Jean continues to act despite the order to stop.",
  [(163, "Jean, c'est coupé !")], "Andrea highlights his total immersion"),
 ("maxime", "Mais qu'est-ce qu'il mange dans cette scène?",
  "But what is he eating in this scene?",
  [(169, "Tu sais que le lapin, là...")], "Maxime watches in disbelief"),
 ("lea", "Il est comme un vrai démon sauvage!",
  "He is like a true wild demon!",
  [(166, "Il est démon.")], "Andrea praises the primal energy"),
 ("lea", "C'est à la hauteur de DiCaprio dans The Revenant.",
  "It is right up there with DiCaprio in The Revenant.",
  [(168, "C'est à la hauteur de DiCaprio dans un revenant.")], "Andrea makes the comparison"),
 ("maxime", "Attends, cet animal sauvage est bien réel?",
  "Wait, is this wild animal truly real?",
  [(170, "C'est un vrai lapin.")], "Maxime recoils in shock"),
 ("lea", "Oui, ce lapin est un vrai lapin sauvage.",
  "Yes, this rabbit is a real wild rabbit.",
  [(170, "C'est un vrai lapin.")], "Andrea confirms with pride"),
 ("maxime", "Il mange un animal cru devant la caméra?",
  "He eats a raw animal in front of the camera?",
  [(170, "C'est un vrai lapin.")], "Maxime is stunned by the extreme act"),
 ("lea", "Jean s'est totalement transformé pour ce grand rôle.",
  "Jean has totally transformed for this great role.",
  [(168, "C'est à la hauteur de DiCaprio")], "Andrea defends the extreme craft"),
 ("maxime", "C'est trop fou pour notre comédie familiale, Andréa.",
  "That is too crazy for our family comedy, Andrea.",
  [(171, "Bon, ça suffit, les conneries, Andrea.")], "Maxime draws the line"),
 ("maxime", "Alors dis-moi enfin où se cache Jean Dujardin.",
  "So tell me finally where Jean Dujardin is hiding.",
  [(172, "Il est où, du jardin, là ?")], "Maxime loses patience"),
 ("lea", "Il prend simplement quelques jours de repos mérité.",
  "He is simply taking a few days of well-deserved rest.",
  [(134, "Jean prend quelques jours de repos")], "Andrea reassures him smoothly"),
 ("maxime", "Je veux le voir demain dans mon bureau!",
  "I want to see him tomorrow in my office!",
  [(137, "Le tournage commence dans 15 jours.")], "Maxime sets an ultimatum"),
]

OPENER = "Let's examine how Maxime reacts to Dujardin's shocking performance step by step to explore extreme method acting."

WALK = [
 (0, None,
  "'The director is shouting that the take is cut!' Maxime watches the monitor as the director tries in vain to stop filming."),
 (1, None,
  "'Jean continues to act despite the order to stop.' Andrea shows that the star was too deeply immersed to hear."),
 (2, None,
  "'But what is he eating in this scene?' Maxime squints at the disturbing action on screen."),
 (3, None,
  "'He is like a true wild demon!' Andrea describes the fierce, untamed power of the actor's performance."),
 (4, None,
  "'It is right up there with DiCaprio in The Revenant.' Andrea compares the role to famous Hollywood survival drama."),
 (5, None,
  "'Wait, is this wild animal truly real?' Maxime asks with growing disgust whether prop effects were used."),
 (6, None,
  "'Yes, this rabbit is a real wild rabbit.' Andrea reveals that no special effects were involved."),
 (7, None,
  "'He eats a raw animal in front of the camera?' Maxime cannot believe the star went to such shocking lengths."),
 (8, None,
  "'Jean has totally transformed for this great role.' Andrea defends total immersion as the mark of a great artist."),
 (9, None,
  "'That is too crazy for our family comedy, Andrea.' Maxime worries that a feral star will ruin his mainstream movie."),
 (10, None,
  "'So tell me finally where Jean Dujardin is hiding.' Maxime demands the actor's immediate whereabouts."),
 (11, None,
  "'He is simply taking a few days of well-deserved rest.' Andrea tries to downplay the actor's ongoing breakdown."),
 (12, None,
  "'I want to see him tomorrow in my office!' Maxime delivers a firm ultimatum before walking out."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Andrea's attempt to impress producer Maxime with extreme method acting backfires as Dujardin's wild transformation alarms production. "
         "Let's review the key expressions and vocabulary from this scene.")

CLOSING = ("maxime", "Je veux le voir demain dans mon bureau!")
