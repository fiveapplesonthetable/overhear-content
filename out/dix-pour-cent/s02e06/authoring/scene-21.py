# Authoring module for dix-pour-cent s02e06 scene 21 (cues 562-598).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-21.py --out out/dix-pour-cent/s02e06/scene-21.json

ID = "dix-pour-cent-s02e06-scene-21"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 21
TITLE = "Le tapis rouge  (The Red Carpet)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo", "juliette": "emilie"}
LABELS = {"lea": "Andréa", "hicham": "Hicham", "juliette": "Juliette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 562-598. At the Cannes Film Festival red carpet, Andrea and Hicham meet with Juliette Binoche "
               "who suddenly suffers from intense stage fright and an urgent need to find a bathroom. "
               "Adapted for A1 French.")

INTRO = ("At the Cannes Film Festival, Andrea and Hicham arrive for the prestigious opening ceremony. "
         "Backstage, their star client Juliette Binoche suddenly experiences extreme stage fright and an urgent emergency. "
         "Let's listen to the scene in French first.")

STORY = [
 ("hicham", "Tu es très élégante ce soir, Andréa.",
  "You are very elegant tonight, Andrea.",
  [(580, "Très élégant")], "Hicham compliments Andrea"),
 ("lea", "Merci Hicham, toi aussi d'ailleurs.",
  "Thank you Hicham, you too by the way.",
  [(580, "Merci. Toi aussi.")], "Andrea returns the compliment"),
 ("hicham", "C'est mon premier Festival de Cannes.",
  "It is my first Cannes Film Festival.",
  [(574, "premier Festival de Cannes")], "Hicham notes his first festival"),
 ("lea", "Regarde toutes ces superbes robes!",
  "Look at all these gorgeous dresses!",
  [(568, "et les robes.")], "Andrea observes the dresses"),
 ("hicham", "Nous allons bientôt monter les marches.",
  "We are soon going to climb the steps.",
  [(573, "monter les marches.")], "Hicham looks forward to the stairs"),
 ("lea", "Allons rejoindre Juliette dans sa loge.",
  "Let us join Juliette in her dressing room.",
  [(582, "allons-y")], "Andrea suggests finding Juliette"),
 ("juliette", "J'ai un trac fou ce soir!",
  "I have crazy stage fright tonight!",
  [(593, "c'est le trac.")], "Juliette admits her nervousness"),
 ("lea", "Tout est parfait pour la cérémonie.",
  "Everything is perfect for the ceremony.",
  [(565, "Parfait.")], "Andrea reassures Juliette"),
 ("juliette", "J'ai un besoin urgent de faire pipi.",
  "I urgently need to pee.",
  [(594, "J'ai besoin de faire pipi.")], "Juliette states her emergency"),
 ("lea", "Là, juste avant de monter sur scène?",
  "There, right before going on stage?",
  [(595, "Là, maintenant ?")], "Andrea expresses disbelief at the timing"),
 ("juliette", "Oui, je vais vraiment éclater!",
  "Yes, I am really going to burst!",
  [(597, "Je vais éclater.")], "Juliette describes her urgency"),
 ("hicham", "Est-ce qu'on a encore le temps?",
  "Do we still have time?",
  [(596, "On a le temps ?")], "Hicham asks about timing"),
 ("lea", "Non, pas vraiment beaucoup de temps.",
  "No, not really a lot of time.",
  [(596, "Pas vraiment.")], "Andrea admits time is short"),
 ("lea", "D'accord, courons chercher des toilettes!",
  "All right, let us run to find a bathroom!",
  [(598, "d'accord.")], "Andrea leads the rush to find restrooms"),
]

OPENER = "Let's examine how Andrea and Hicham handle this backstage emergency step by step."

WALK = [
 (0, None,
  "'You are very elegant tonight, Andrea.' Hicham compliments Andrea as they arrive at the event."),
 (1, None,
  "'Thank you Hicham, you too by the way.' Andrea returns the compliment to her agency partner."),
 (2, None,
  "'It is my first Cannes Film Festival.' Hicham shares his excitement about attending the festival."),
 (3, None,
  "'Look at all these gorgeous dresses!' Andrea admires the glamorous fashion on the red carpet."),
 (4, None,
  "'We are soon going to climb the steps.' Hicham looks forward to walking up the famous Palais steps."),
 (5, None,
  "'Let us join Juliette in her dressing room.' Andrea suggests meeting their star client backstage."),
 (6, None,
  "'I have crazy stage fright tonight!' Juliette reveals her intense nervousness before the event."),
 (7, None,
  "'Everything is perfect for the ceremony.' Andrea reassures the actress that all preparations are set."),
 (8, None,
  "'I urgently need to pee.' Juliette confesses an urgent bodily need right before the start."),
 (9, None,
  "'There, right before going on stage?' Andrea is shocked by the terrible timing of the problem."),
 (10, None,
  "'Yes, I am really going to burst!' Juliette insists that she cannot wait any longer."),
 (11, None,
  "'Do we still have time?' Hicham asks if a quick detour is possible."),
 (12, None,
  "'No, not really a lot of time.' Andrea warns that the schedule is extremely tight."),
 (13, None,
  "'All right, let us run to find a bathroom!' Andrea agrees to rush backstage to locate a restroom."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("An unexpected panic strikes Juliette Binoche minutes before she must step onto the global stage. "
         "Andrea and Hicham must navigate the backstage corridors to avert disaster. "
         "Let's review the key expressions and vocabulary from this scene.")

CLOSING = ("lea", "D'accord, courons chercher des toilettes!")
