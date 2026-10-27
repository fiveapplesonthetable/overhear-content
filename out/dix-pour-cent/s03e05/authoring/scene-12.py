# Authoring module for dix-pour-cent s03e05 scene 12 (cues 388-407).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-12.py --out out/dix-pour-cent/s03e05/scene-12.json

ID = "dix-pour-cent-s03e05-scene-12"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 12
TITLE = "Dans le bureau du patron  (In the Boss's Office)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Camille", "theo": "Valentin"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 388-407. Valentin wanders into Mathias's grand office and teases Camille about running "
               "her own agency, before suggesting they rehearse his scene on the sofa. Adapted for A1 French.")

INTRO = ("Valentin slips into Mathias's luxurious corner office, marveling at the room and private bar. "
         "While Camille tries nervously to usher him out, Valentin proposes they rehearse his audition scene right there. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
 ("lea", "Valentin? Qu'est-ce que tu fais là-dedans?",
  "Valentin? What are you doing in there?",
  [(388, "Valentin ?"), (389, "Valentin ?")], "Surprised inquiry"),
 ("theo", "Oh, j'adore cette immense pièce lumineuse!",
  "Oh, I love this huge, luminous room!",
  [(391, "Oh celui-là j'adore")], "Admiring office"),
 ("lea", "Non, sors vite, c'est le bureau de Mathias!",
  "No, get out quickly, that is Mathias's office!",
  [(392, "Non mais sûrement pas c'est celui de mon patron ça")], "Urging departure"),
 ("theo", "Ce sera bientôt le tien, non?",
  "It will be yours soon, won't it?",
  [(396, "Mais attends ce sera bientôt le tien non ?")], "Teasing Camille"),
 ("theo", "Agence Camille Valentini, ça sonne très bien!",
  "Camille Valentini Agency, that sounds great!",
  [(398, "Agence Camille Valentini")], "Inventing agency name"),
 ("lea", "Arrête, Valentin, ne touche à rien.",
  "Stop it, Valentin, do not touch anything.",
  [(395, "Arrête Valentin"), (400, "Patouche")], "Warning against touching"),
 ("theo", "Regarde toutes ces belles bouteilles prestigieuses.",
  "Look at all these beautiful prestigious bottles.",
  [(399, "Les bouteilles")], "Admiring bar"),
 ("lea", "Mathias va être furieux s'il l'apprend.",
  "Mathias will be furious if he finds out.",
  [(392, "c'est celui de mon patron ça")], "Fearing boss's wrath"),
 ("theo", "Ne t'inquiète pas, on est tranquilles ici.",
  "Do not worry, we are safe and quiet here.",
  [(401, "Ça va"), (402, "On est tous les deux là")], "Reassuring Camille"),
 ("theo", "Assieds-toi confortablement sur ce canapé.",
  "Sit down comfortably on this sofa.",
  [(403, "T'étends toi")], "Inviting to sit"),
 ("theo", "Si on répétait ma scène de casting?",
  "What if we rehearsed my casting scene?",
  [(404, "On répète ma scène ?")], "Proposing rehearsal"),
 ("lea", "Tu veux répéter ta scène ici maintenant?",
  "You want to rehearse your scene here now?",
  [(405, "Là ici ?")], "Incredulous question"),
 ("theo", "Oui, nous sommes tous les deux prêts.",
  "Yes, both of us are ready.",
  [(406, "Bah ouais"), (407, "On est chaud là non ?")], "Affirming readiness"),
 ("lea", "D'accord, mais juste une seule fois alors.",
  "Okay, but just once then.",
  [(407, "On est chaud là non ?")], "Reluctant agreement"),
]

WALK = [
 (0, None,
  "'Valentin? What are you doing in there?' Camille discovers Valentin exploring. "
  "The compound adverb 'la-dedans' refers to the interior space."),
 (1, None,
  "'Oh, I love this huge, luminous room!' Valentin marvels at the luxurious office. "
  "The adjective 'lumineuse' describes good lighting."),
 (2, None,
  "'No, get out quickly, that is Mathias's office!' Camille panics at the intrusion. "
  "The imperative 'sors vite' urges him to leave."),
 (3, None,
  "'It will be yours soon, won't it?' Valentin teases Camille about her future. "
  "The tag question 'non' seeks playful agreement."),
 (4, None,
  "'Camille Valentini Agency, that sounds great!' Valentin invents her agency name. "
  "The verb 'sonner' means to sound."),
 (5, None,
  "'Stop it, Valentin, do not touch anything.' Camille warns him against snooping. "
  "The negative structure 'ne touche a rien' forbids handling objects."),
 (6, None,
  "'Look at all these beautiful prestigious bottles.' Valentin spots Mathias's private bar. "
  "The noun 'bouteilles' refers to liquor bottles."),
 (7, None,
  "'Mathias will be furious if he finds out.' Camille fears her boss's wrath. "
  "The adjective 'furieux' denotes intense anger."),
 (8, None,
  "'Do not worry, we are safe and quiet here.' Valentin tries to calm her anxieties. "
  "The adjective 'tranquille' means undisturbed or peaceful."),
 (9, None,
  "'Sit down comfortably on this sofa.' Valentin makes himself at home. "
  "The reflexive imperative 'assieds-toi' invites someone to take a seat."),
 (10, None,
  "'What if we rehearsed my casting scene?' Valentin proposes an impromptu rehearsal. "
  "The structure 'si on' with the imperfect suggests an activity."),
 (11, None,
  "'You want to rehearse your scene here now?' Camille reacts with incredulity. "
  "The verb 'repeter' means to rehearse."),
 (12, None,
  "'Yes, both of us are ready.' Valentin encourages her to participate. "
  "The adjective 'pret' expresses readiness."),
 (13, None,
  "'Okay, but just once then.' Camille relents under his charm. "
  "The adverbial phrase 'une seule fois' limits the rehearsal."),
]

OUTRO = ("Camille and Valentin sit down to rehearse, turning Mathias's private domain into an improvised rehearsal stage. "
         "Valentin's bold confidence and charm continue to pull Camille out of her comfort zone. "
         "Now, let's review the scene once more.")

CLOSING = ("theo", "Si on répétait ma scène de casting?")
