# Authoring module for dix-pour-cent s03e06 scene 11 (cues 519-584).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e06/authoring/scene-11.py --out overhear-content/out/dix-pour-cent/s03e06/scene-11.json

ID = "dix-pour-cent-s03e06-scene-11"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 11
TITLE = "Le tournage du fantôme  (Filming the Ghost)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "isabelle": "emilie", "director": "theo"}
LABELS = {"lea": "Camille", "isabelle": "Isabelle", "director": "Le réalisateur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 519-584. In a quiet outdoor setting, Camille oversees an amateur ghost scene shoot "
               "featuring lookalike hospital nurse Isabelle, coping with artsy director demands and comedic filming blunders.")

INTRO = ("In a public park, Camille coordinates a makeshift filming session with lookalike Isabelle playing a queen's ghost. "
         "The pretentious young director gives extravagant artistic instructions, but the novice actress repeatedly wanders off-camera, "
         "creating amusing chaos on set. Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("director", "Cette scène intime doit rester très spectaculaire.",
  "This intimate scene must remain very spectacular.",
  [(524, "parce que c'est intime et en même temps, je veux que ce soit spectaculaire.")], "Setting pretentious artistic tone"),
 ("lea", "Nous avons seulement une heure pour tourner.",
  "We only have one hour to shoot.",
  [(529, "on n'a qu'une heure et demie, là.")], "Reminding strict time limit"),
 ("director", "Isabelle, avance lentement vers ce grand arbre.",
  "Isabelle, walk slowly toward this big tree.",
  [(532, "Sofia, tu vas te mettre près de l'arbre, s'il te plaît.")], "Giving blocking instruction"),
 ("isabelle", "Je marche avec les yeux bien fermés?",
  "Do I walk with my eyes tightly closed?",
  [(547, "c'est vous qui m'avez demandé de faire le fantôme les yeux fermés.")], "Clarifying bizarre direction"),
 ("director", "Oui, silence complet sur le plateau, action!",
  "Yes, complete silence on the set, action!",
  [(543, "Action.")], "Calling for action"),
 ("director", "Coupez! Mais vous marchez hors du cadre!",
  "Cut! But you are walking out of frame!",
  [(549, "Bah, là, vous faites un fantôme hors champ, donc...")], "Stopping take in exasperation"),
 ("isabelle", "Pardon, je ne vois rien les yeux fermés.",
  "Sorry, I see nothing with closed eyes.",
  [(548, "Moi, je sais pas où faut m'arrêter.")], "Defending practical difficulty"),
 ("lea", "Gardez les yeux ouverts, s'il vous plaît.",
  "Keep your eyes open, please.",
  [(552, "Gardez les yeux ouverts, mais arrêtez-vous au bon endroit.")], "Intervening constructively"),
 ("director", "On recommence tout de suite au départ!",
  "We are restarting right away from the mark!",
  [(551, "Remettez-vous au départ et tant pis.")], "Calling for immediate reset"),
 ("isabelle", "Attendez, mon téléphone sonne dans mon sac.",
  "Wait, my phone is ringing in my bag.",
  [(560, "Oh ! Eh, on coupe les portables ?")], "Interrupting the take"),
 ("director", "C'est une blague? Coupez ce portable!",
  "Is this a joke? Turn off that mobile phone!",
  [(560, "on coupe les portables ?")], "Expressing artistic fury"),
 ("isabelle", "C'est ma collègue Gladys de l'hôpital.",
  "It is my colleague Gladys from the hospital.",
  [(563, "Oui, Gladys, tout se passe bien ?")], "Explaining nurse duty call"),
 ("lea", "Mettez votre téléphone en mode avion, Isabelle.",
  "Put your phone on airplane mode, Isabelle.",
  [(567, "On se met en mode avion, maintenant, Isabelle ?")], "Resolving noise disruption"),
 ("director", "Allez, tout le monde en place, action!",
  "Come on, everyone in position, action!",
  [(569, "Action.")], "Resuming filming take"),
]

WALK = [
 (0, None,
  "'This intimate scene must remain very spectacular.' The director outlines his vision. "
  "The adjective 'spectaculaire' expresses grand visual ambition."),
 (1, None,
  "'We only have one hour to shoot.' Camille urges focus on the ticking clock. "
  "The adverb 'seulement' indicates tight schedule constraints."),
 (2, None,
  "'Isabelle, walk slowly toward this big tree.' The director positions his ghost. "
  "The preposition 'vers' indicates movement toward a landmark."),
 (3, None,
  "'Do I walk with my eyes tightly closed?' Isabelle checks the unusual instruction. "
  "The past participle 'fermes' functions here as a descriptive adjective."),
 (4, None,
  "'Yes, complete silence on the set, action!' The director calls for silence before filming. "
  "The noun phrase 'silence complet' commands total quiet."),
 (5, None,
  "'Cut! But you are walking out of frame!' The director cuts the botched take. "
  "The prepositional phrase 'hors du cadre' means outside the camera frame."),
 (6, None,
  "'Sorry, I see nothing with closed eyes.' Isabelle points out the obvious physical reality. "
  "The negative phrase 'ne vois rien' expresses complete blindness."),
 (7, None,
  "'Keep your eyes open, please.' Camille provides sensible and practical guidance. "
  "The imperative 'gardez' gives a polite operational instruction."),
 (8, None,
  "'We are restarting right away from the mark!' The director orders a rapid reset. "
  "The locution 'tout de suite' indicates immediate resumption."),
 (9, None,
  "'Wait, my phone is ringing in my bag.' An incoming ringtone shatters the set quiet. "
  "The verb 'sonner' means to ring."),
 (10, None,
  "'Is this a joke? Turn off that mobile phone!' The director loses patience with interruptions. "
  "The colloquial noun 'portable' refers to a mobile phone."),
 (11, None,
  "'It is my colleague Gladys from the hospital.' Isabelle reveals her genuine medical day job. "
  "The noun 'hopital' denotes her real workplace."),
 (12, None,
  "'Put your phone on airplane mode, Isabelle.' Camille prevents further interruptions. "
  "The technical phrase 'mode avion' designates airplane mode on phones."),
 (13, None,
  "'Come on, everyone in position, action!' The director restarts the take with renewed energy. "
  "The expression 'en place' instructs everyone to assume their marks."),
]

OUTRO = ("Camille navigates the quirky clash between an amateur nurse actress and a fussy director. "
         "Despite ringing phones and misplaced steps, the team readies the scene for another take. "
         "Now, let's review the scene one last time.")

CLOSING = ("director", "Allez, tout le monde en place, action!")
