# Authoring module for dix-pour-cent s02e02 scene 01 (cues 1-37).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-01.py --out out/dix-pour-cent/s02e02/scene-01.json

ID = "dix-pour-cent-s02e02-scene-01"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 1
TITLE = "Hicham rachète l'agence ASK  (Hicham Buys the ASK Agency)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "marcel", "mathias": "theo"}
LABELS = {"lea": "Andréa", "hicham": "Hicham", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-37. Wealthy businessman Hicham Janowski signs the deal buying 60 percent of ASK "
               "and toasts with the agents. Adapted for A1 French.")

INTRO = ("At the ASK agency, millionaire businessman Hicham Janowski has just finalized the buyout of the firm. "
         "Surrounded by champagne glasses, the partners welcome their new majority shareholder. "
         "Let's listen to the scene in French first.")

STORY = [
 ("mathias", "Monsieur Janowski, vous êtes actionnaire majoritaire d'ASK avec soixante pour cent.",
  "Mr. Janowski, you are majority shareholder of ASK with sixty percent.",
  [(9, "M. Janowski, vous êtes désormais"), (10, "actionnaire majoritaire d'ASK, avec")], "Spelled out percentage"),
 ("mathias", "Toutes nos félicitations.",
  "All our congratulations.",
  [(10, "Félicitations.")], "Added polite formula"),
 ("hicham", "Merci beaucoup à tous.",
  "Thank you very much to all.",
  [(11, "Merci.")], "Expanded short thank you"),
 ("hicham", "Quand j'étais gamin, je rêvais d'être acteur.",
  "When I was a kid, I dreamed of being an actor.",
  [(14, "Quand j'étais gamin, je rêvais d'être acteur.")], ""),
 ("hicham", "Je voulais être une vraie star.",
  "I wanted to be a real star.",
  [(16, "Je voulais être une star,")], "Added adjective 'vraie'"),
 ("hicham", "Vous vous occupez des acteurs, c'est votre domaine.",
  "You take care of the actors, that is your field.",
  [(22, "Vous vous occupez des acteurs, c'est pas mon domaine.")], "Affirmative adaptation"),
 ("hicham", "Je suis très heureux et enthousiaste d'être ici.",
  "I am very happy and enthusiastic to be here.",
  [(24, "que je suis heureux et enthousiaste d'être ici.")], "Main clause form"),
 ("hicham", "À votre santé!",
  "To your health!",
  [(25, "À votre santé.")], ""),
 ("lea", "Santé, monsieur Janowski.",
  "Cheers, Mr. Janowski.",
  [(26, "Santé.")], "Added formal address"),
 ("hicham", "Votre vrai nom, c'est Marteau?",
  "Your real name is Marteau?",
  [(27, "Votre vrai nom, c'est Marteau ?")], ""),
 ("lea", "Non, c'est juste un vieux surnom.",
  "No, it is just an old nickname.",
  [(28, "Non, c'est juste un surnom")], "Replaced vulgar phrase with 'un vieux surnom'"),
 ("lea", "Ici, mon nom c'est Martel, d'accord?",
  "Here, my name is Martel, okay?",
  [(30, "Ici, mon nom c'est Martel."), (31, "D'accord ?")], ""),
 ("hicham", "Je ne veux pas gâcher notre lune de miel.",
  "I do not want to ruin our honeymoon.",
  [(33, "Je ne veux pas gâcher notre lune de miel,")], ""),
 ("hicham", "Santé, Andréa Martel!",
  "Cheers, Andrea Martel!",
  [(34, "Andréa Martel."), (35, "Santé.")], ""),
]

OPENER = "Let's examine how Hicham introduces himself to his new partners."

WALK = [
 (0, None,
  "'Mr. Janowski, you are majority shareholder of ASK with sixty percent.' Mathias formally announces the new ownership stake."),
 (1, None,
  "'All our congratulations.' A plural polite expression of congratulations in professional life."),
 (2, None,
  "'Thank you very much to all.' A gracious response addressing the entire gathered agency team."),
 (3, None,
  "'When I was a kid, I dreamed of being an actor.' A compound past memory introduced by a temporal conjunction."),
 (4, None,
  "'I wanted to be a real star.' An imperfect verb expressing childhood ambition with a feminine noun."),
 (5, None,
  "'You take care of the actors, that is your field.' A pronominal verb indicating daily operational responsibility."),
 (6, None,
  "'I am very happy and enthusiastic to be here.' Two coordinated descriptive adjectives expressing excitement."),
 (7, None,
  "'To your health!' A classic celebratory toast raised to the company."),
 (8, None,
  "'Cheers, Mr. Janowski.' Andrea politely returns the toast using his formal surname."),
 (9, None,
  "'Your real name is Marteau?' Hicham teases his former classmate about an old childhood nickname."),
 (10, None,
  "'No, it is just an old nickname.' Andrea dismisses the childish moniker with a restrictive adverb."),
 (11, None,
  "'Here, my name is Martel, okay?' A firm boundary establishing her adult professional identity."),
 (12, None,
  "'I do not want to ruin our honeymoon.' A playful metaphor referring to their initial working relationship."),
 (13, None,
  "'Cheers, Andrea Martel!' Hicham seals the truce by addressing her with full respect."),
]

TRANSITION = "Now let's listen to the celebration toast again at full speed."

OUTRO = ("Hicham Janowski is now the majority owner of ASK. "
         "While the toast is polite, his arrival brings an ambitious and unpredictable new dynamic to the team.")

CLOSING = ("lea", "Merci, Hicham.")
