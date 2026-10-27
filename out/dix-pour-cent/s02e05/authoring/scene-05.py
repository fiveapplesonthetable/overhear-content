# Authoring module for dix-pour-cent s02e05 scene 05 (cues 137-157).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e05/authoring/scene-05.py --out out/dix-pour-cent/s02e05/scene-05.json

ID = "dix-pour-cent-s02e05-scene-05"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 5
TITLE = "La moustache de Gabin  (The Mustache)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo"}
LABELS = {"lea": "Camille", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 137-157. In the ASK hallway, Hervé teases Camille by calling her Jean Gabin. "
               "Camille confides that everyone at the agency treats her differently now that Mathias is known as her father. "
               "Adapted for A1 French.")

INTRO = ("In the hallway at ASK, Herve teases Camille following the explosive revelation about her parentage. "
         "Camille struggles with how her colleagues perceive her, while Herve tries to cheer her up with movie references. "
         "Let's listen to the scene in French first.")

STORY = [
 ("herve", "Arrête, Jean Gabin, c'est Camille!",
  "Stop it, Jean Gabin, it's Camille!",
  [(137, "Arrête, Jean Gabin, c'est Camille.")], "Herve teases Camille"),
 ("lea", "Ne lui en veux pas trop.",
  "Do not hold it against him too much.",
  [(139, "Ne lui en veux pas.")], "Camille defends her father"),
 ("herve", "Il te transfère sa haine pour Mathias.",
  "He transfers his hatred for Mathias to you.",
  [(140, "Il te transfère sa haine pour Mathias.")], "Herve analyzes the attitude"),
 ("lea", "C'est horrible, je suis devenue une autre.",
  "It is horrible, I have become someone else.",
  [(141, "c'est comme si j'étais devenue quelqu'un d'autre")], "Camille laments the change"),
 ("lea", "Personne à l'agence ne me reconnaît.",
  "Nobody at the agency recognizes me.",
  [(142, "et que personne ne me reconnaît.")], "Camille feels isolated"),
 ("herve", "C'est comme dans le film La Moustache.",
  "It is like in the movie The Mustache.",
  [(143, "Comme dans La Moustache.")], "Herve cites cinema"),
 ("herve", "Le type se rase, personne ne remarque.",
  "The guy shaves, nobody notices.",
  [(144, "Le mec se rase la moustache, personne ne le remarque.")], "Herve explains the plot"),
 ("lea", "Non, c'est exactement le contraire.",
  "No, it is exactly the opposite.",
  [(146, "C'est le contraire.")], "Camille disagrees"),
 ("lea", "Tout le monde pense que j'ai changé.",
  "Everyone thinks that I have changed.",
  [(147, "Tout le monde pense que j'ai changé, mais non.")], "Camille insists she is unchanged"),
 ("lea", "Que Mathias soit mon père ne change rien.",
  "Mathias being my father changes nothing.",
  [(148, "Que Mathias soit mon père ne change rien.")], "Camille asserts her identity"),
 ("herve", "C'est plutôt comme dans Blade Runner.",
  "It is rather like in Blade Runner.",
  [(150, "C'est plutôt comme Blade Runner.")], "Herve offers another comparison"),
 ("herve", "Quand on découvre que c'est un réplicant.",
  "When you find out that he is a replicant.",
  [(151, "Quand tu découvres que lui aussi est un réplicant")], "Herve jokes about androids"),
 ("herve", "On t'aime quand même, Camillette!",
  "We love you anyway, Camillette!",
  [(153, "mais on l'aime quand même. On t'aime quand même.")], "Herve reassures her warmly"),
]

OPENER = "Let's examine how Herve and Camille discuss her new status step by step to understand the humor and emotion."

WALK = [
 (0, None,
  "'Stop it, Jean Gabin, it's Camille!' Herve jokingly calls Camille by the legendary French actor's name."),
 (1, None,
  "'Do not hold it against him too much.' Camille urges Herve not to be too hard on the colleague venting frustration."),
 (2, None,
  "'He transfers his hatred for Mathias to you.' Herve points out how office resentment against Mathias falls on Camille."),
 (3, None,
  "'It is horrible, I have become someone else.' Camille describes feeling like an entirely different person."),
 (4, None,
  "'Nobody at the agency recognizes me.' Camille feels alienated by how differently her coworkers now treat her."),
 (5, None,
  "'It is like in the movie The Mustache.' Herve brings up a famous French film about unrecognized identity."),
 (6, None,
  "'The guy shaves, nobody notices.' Herve summarizes the absurd plot of the movie."),
 (7, None,
  "'No, it is exactly the opposite.' Camille corrects him, noting that in her case everyone imagines a huge change."),
 (8, None,
  "'Everyone thinks that I have changed.' Camille laments that people look past her actual personality."),
 (9, None,
  "'Mathias being my father changes nothing.' Camille insists that her relationship to Mathias does not alter who she is."),
 (10, None,
  "'It is rather like in Blade Runner.' Herve switches to a sci-fi reference about discovering an android identity."),
 (11, None,
  "'When you find out that he is a replicant.' Herve playfully compares Mathias's lineage to an artificial creation."),
 (12, None,
  "'We love you anyway, Camillette!' Herve uses an affectionate nickname to reassure Camille of his loyalty."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Herve uses humor and cinema references to cheer up Camille as she adjusts to life in the spotlight at ASK. "
         "Let's review the conversational phrases and vocabulary from this scene.")

CLOSING = ("herve", "On t'aime quand même, Camillette!")
