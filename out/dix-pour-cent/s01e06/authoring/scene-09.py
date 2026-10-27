# Authoring module for dix-pour-cent s01e06 scene 09 (cues 229-266).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-09.py --out out/dix-pour-cent/s01e06/scene-09.json

ID = "dix-pour-cent-s01e06-scene-09"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 9
TITLE = "Le coup de poing  (The Punch)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "christophe": "theo", "francois": "marcel"}
LABELS = {"lea": "Andréa", "christophe": "Christophe", "francois": "François"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 229-266. Rehearsals of Dom Juan at the indoor pool reach a breaking point. "
               "Christophe Bel demands that François Berléand get closer to the water and insults his acting. "
               "When Christophe throws a tantrum, François loses his temper and punches him. "
               "Andréa rushes in to assess the damage. Adapted for A1 French.")

INTRO = ("Back at the theatre rehearsal hall, the pool staging of Dom Juan turns into a total disaster. "
         "Director Christophe Bel insists that Francois Berleand stand right at the edge of the water. "
         "Insults fly, tensions explode, and Francois does the unthinkable. "
         "Let's listen to the scene in French first.")

STORY = [
 ("christophe", "Depuis le début. Et plus près de l'eau.",
  "From the beginning. And closer to the water.",
  [(230, "Depuis le début."), (231, "Et plus près de l'eau.")], ""),
 ("francois", "Plus près? Comment? J'ai déjà les pieds mouillés!",
  "Closer? How? My feet are already wet!",
  [(232, "Plus près ?"), (233, "Comment ? J'ai déjà les pieds mouillés !")], ""),
 ("christophe", "François, débrouille-toi! Tu es comédien, fais quelque chose!",
  "François, manage on your own! You are an actor, do something!",
  [(234, "François, débrouille-toi."), (234, "T'es comédien, fais quelque chose !")], ""),
 ("francois", "Qu'est-ce que je peux vous dire? Je vous aime toutes les deux.",
  "What can I tell you? I love you both.",
  [(235, "Qu'est-ce que je peux vous dire ?")], "Simplified Dom Juan speech in 236 to A1"),
 ("christophe", "Non, ça ne va pas! Ça ne fonctionne pas!",
  "No, that will not do! That does not work!",
  [(239, "Non, ça ne va pas ! Ça ne fonctionne pas !")], ""),
 ("christophe", "Si tu n'es pas dans le bassin, ça ne marche pas.",
  "If you are not in the pool, it simply does not work.",
  [(240, "Si t'es pas dans le bassin avec elles, ça ne marche tout simplement pas.")], "Restored negative 'n''"),
 ("christophe", "Tu es raide, tu es comme un vieux beauf!",
  "You are stiff, you are like an old redneck!",
  [(241, "T'es comme ça, t'es raide, t'es comme un vieux beauf !")], ""),
 ("francois", "C'est du théâtre, pas les Jeux olympiques!",
  "This is theatre, not the Olympic Games!",
  [(245, "C'est du théâtre, pas les Jeux olympiques !")], ""),
 ("christophe", "Vous m'expliquez ce qu'est le théâtre? J'écoute!",
  "You are explaining to me what theatre is? I am listening!",
  [(247, "Vous m'expliquez ce qu'est le théâtre ? Très bien, j'écoute !")], ""),
 ("lea", "Christophe, s'il te plaît, calme-toi.",
  "Christophe, please, calm down.",
  [(248, "Christophe.")], "Extended intervention in A1"),
 ("christophe", "Je porte ce projet depuis des mois! Personne ne fait d'effort!",
  "I have been carrying this project for months! Nobody makes an effort!",
  [(252, "Je porte ce projet depuis des mois !"), (253, "Personne ne fait d'effort !")], ""),
 ("christophe", "Au secours! François?",
  "Help! François?",
  [(255, "Au secours ! François ?")], ""),
 ("francois", "Je suis désolé. Je ne l'ai pas fait exprès.",
  "I am sorry. I did not do it on purpose.",
  [(258, "Je suis désolé."), (259, "Je ne l'ai pas fait exprès.")], ""),
 ("lea", "Attendez. Qui a donné le coup de poing?",
  "Wait. Who threw the punch?",
  [(263, "Attendez."), (265, "Mais qui a donné le coup de poing ?")], ""),
 ("christophe", "Berléand! Il est parti!",
  "Berléand! He walked away!",
  [(266, "Berléand.")], "Added short context for drama"),
]

OPENER = "Let's break down this dramatic escalation line by line."

WALK = [
 (0, None,
  "'From the beginning. And closer to the water.' Christophe commands his actors with zero patience."),
 (1, None,
  "'Closer? How? My feet are already wet!' Francois complains about the dangerous conditions on stage."),
 (2, None,
  "'Francois, manage on your own! You are an actor, do something!' A colloquial imperative telling him to work it out."),
 (3, None,
  "'What can I tell you? I love you both.' Francois recites his lines as Dom Juan facing two peasant women."),
 (4, None,
  "'No, that will not do! That does not work!' Christophe cuts him off angrily."),
 (5, None,
  "'If you are not in the pool, it simply does not work.' The director refuses to compromise on his water concept."),
 (6, None,
  "'You are stiff, you are like an old redneck!' A direct insult mocking the older actor's physical stiffness."),
 (7, None,
  "'This is theatre, not the Olympic Games!' Francois snaps back with a witty cultural retort."),
 (8, None,
  "'You are explaining to me what theatre is? I am listening!' Christophe takes deep offence at being lectured."),
 (9, None,
  "'Christophe, please, calm down.' Andrea attempts to step between them before things get worse."),
 (10, None,
  "'I have been carrying this project for months! Nobody makes an effort!' The director loses all control of his temper."),
 (11, None,
  "'Help! Francois?' Suddenly a punch lands and Christophe cries out in shock from the floor."),
 (12, None,
  "'I am sorry. I did not do it on purpose.' Francois speaks in disbelief at his own violent outburst."),
 (13, None,
  "'Wait. Who threw the punch?' Andrea rushes in to understand who struck whom."),
 (14, None,
  "'Berleand! He walked away!' Christophe points at his star actor storming out of the theatre."),
]

TRANSITION = "Let's listen to this explosive confrontation one more time from start to finish."

OUTRO = ("Francois Berleand has punched his director, putting the entire production in jeopardy. "
         "In the next scene, Andrea and Camille will face the threat of an immediate lawsuit.")
CLOSING = ("lea", "Quelle catastrophe!")
