# Authoring module for dix-pour-cent s02e02 scene 11 (cues 336-354).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-11.py --out out/dix-pour-cent/s02e02/scene-11.json

ID = "dix-pour-cent-s02e02-scene-11"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 11
TITLE = "La piste de Luchini  (The Luchini Lead)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Andréa", "theo": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 336-354. Andréa tasks Hervé with finding intel on Fabrice Luchini to poach him. "
               "Hervé discovers Luchini frequents a gym in the first arrondissement, "
               "and vigorously coaches an unathletic Andréa on the workout equipment. "
               "Adapted for A1 French.")

INTRO = ("Determined to recruit prestigious actor Fabrice Luchini, Andrea interrogates Herve for useful intel. "
         "Herve discovers that Luchini works out at a local gym, prompting an intense and hilarious training session. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Tu as des infos sur Luchini?",
  "Do you have info on Luchini?",
  [(336, "Des infos sur Luchini ?")], "Added Tu as"),
 ("theo", "Il n'est pas en couple actuellement.",
  "He is not currently in a relationship.",
  [(337, "Il n'est pas en couple.")], "Added actuellement"),
 ("theo", "Il vient de s'installer dans un immeuble à Montmartre.",
  "He just moved into a building in Montmartre.",
  [(338, "Il vient de s'installer dans un immeuble à Montmartre")], ""),
 ("theo", "Et il est allergique à la noix de coco.",
  "And he is allergic to coconut.",
  [(340, "Et il est allergique à la noix de coco.")], ""),
 ("lea", "On ne prépare pas un homicide!",
  "We are not planning a homicide!",
  [(341, "On ne prépare pas un homicide.")], ""),
 ("theo", "Il s'entraîne dans une salle de sport.",
  "He works out at a gym.",
  [(342, "Il s'entraîne dans une salle")], "Adapted with de sport"),
 ("lea", "Bien! Quel jour, à quelle heure?",
  "Good! Which day, at what time?",
  [(343, "Bien ! Quel jour, à quelle heure ?")], ""),
 ("theo", "Aucune idée pour le moment.",
  "No idea for the moment.",
  [(344, "Aucune idée.")], "Added pour le moment"),
 ("lea", "Alors renseigne-toi vite!",
  "Then find out quickly!",
  [(345, "Alors renseigne-toi")], "Added vite, omitted vulgarity"),
 ("theo", "Tirez, relâchez! C'est un peu mou.",
  "Pull, release! It is a bit slack.",
  [(349, "Tirez, relâchez... C'est un peu mou.")], ""),
 ("lea", "Cette machine est trop lourde pour moi.",
  "This machine is too heavy for me.",
  [(350, "Trop lourd pour moi.")], "Expanded to complete sentence"),
 ("theo", "Je n'ai mis aucun poids!",
  "I did not put any weight on it!",
  [(350, "Je n'ai mis aucun poids !")], ""),
 ("lea", "La machine doit être cassée.",
  "The machine must be broken.",
  [(351, "Ça doit être cassé.")], "Adapted to la machine"),
 ("theo", "Transpirez ou ça ne sera pas crédible.",
  "Sweat or it will not look credible.",
  [(351, "Transpirez ou ça ne sera pas crédible.")], ""),
 ("theo", "Tu es aussi raide qu'un marteau!",
  "You are as stiff as a hammer!",
  [(352, "T'es aussi raide qu'un marteau.")], "Expanded T'es to Tu es"),
 ("theo", "Maintenant courez, chaque seconde compte! Allez!",
  "Now run, every second counts! Come on!",
  [(354, "Maintenant courez, chaque seconde compte ! Allez !")], ""),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Do you have info on Luchini?' Andrea asks Herve for background intelligence on the actor. "
  "The informal abbreviation 'infos' is commonly used in everyday speech for information."),
 (1, None,
  "'He is not currently in a relationship.' Herve begins his reconnaissance report. "
  "The expression 'etre en couple' describes being in a relationship or married."),
 (2, None,
  "'He just moved into a building in Montmartre.' Herve shares recent residential details. "
  "The recent past construction 'venir de' plus infinitive expresses something that just happened."),
 (3, None,
  "'And he is allergic to coconut.' Herve adds an obscure dietary detail. "
  "The adjective 'allergique a' governs the noun phrase introduced by the feminine article."),
 (4, None,
  "'We are not planning a homicide!' Andrea points out the absurdity of the trivia. "
  "The pronoun 'on' stands for we, negated with 'ne ... pas' around the present tense verb."),
 (5, None,
  "'He works out at a gym.' Herve reveals the vital operational lead. "
  "The pronominal verb 's'entrainer' means to work out or practice athletically."),
 (6, None,
  "'Good! Which day, at what time?' Andrea demands precise logistical details. "
  "The interrogative adjective 'quel' and 'quelle' agree with the masculine and feminine nouns."),
 (7, None,
  "'No idea for the moment.' Herve admits his intelligence has limits. "
  "The negative determiner 'aucune' emphasizes the complete absence of information."),
 (8, None,
  "'Then find out quickly!' Andrea orders him to dig deeper without delay. "
  "The reflexive imperative 'renseigne-toi' commands someone to find out or inquire."),
 (9, None,
  "'Pull, release! It is a bit slack.' Herve barks orders during the gym workout. "
  "The paired imperatives 'tirez' and 'relachez' describe rhythmic physical exercise."),
 (10, None,
  "'This machine is too heavy for me.' Andrea complains about the physical exertion. "
  "The adverb 'trop' intensifies the adjective 'lourde', agreeing with the feminine noun."),
 (11, None,
  "'I did not put any weight on it!' Herve reveals the machine is completely unloaded. "
  "The negative phrase 'ne ... aucun' negates the existence of any added weights."),
 (12, None,
  "'The machine must be broken.' Andrea excuses her complete lack of muscle strength. "
  "The modal verb 'devoir' conveys high probability when combined with the infinitive."),
 (13, None,
  "'Sweat or it will not look credible.' Herve insists on physical authenticity for the cover story. "
  "The imperative 'transpirez' pairs with the future tense 'ne sera pas' in the negative."),
 (14, None,
  "'You are as stiff as a hammer!' Herve critiques her rigid posture bluntly. "
  "The comparative structure 'aussi ... que' expresses an equality comparison with humour."),
 (15, None,
  "'Now run, every second counts! Come on!' Herve urges her onto the treadmill. "
  "The imperative 'courez' and the exclamation 'allez' drive the urgent pace."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Armed with Herve's gym discovery and an agonizing workout session, Andrea prepares to stage a chance encounter. "
         "Next, she will confront Fabrice Luchini directly on his home turf.")
CLOSING = ("theo", "Maintenant courez, chaque seconde compte! Allez!")
