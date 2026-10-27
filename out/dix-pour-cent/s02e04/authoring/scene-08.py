# Authoring module for dix-pour-cent s02e04 scene 08 (cues 192-230).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-08.py --out out/dix-pour-cent/s02e04/scene-08.json

ID = "dix-pour-cent-s02e04-scene-08"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 8
TITLE = "La vérité sur Hartman  (The Truth About Hartman)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "camille": "emilie"}
LABELS = {"lea": "Andréa", "camille": "Camille"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 192-230. Late at night in the office, Andréa confesses to Camille that four years ago "
               "she threw away a script by director Hartman intended for Isabelle Adjani, and asks Camille to sabotage their upcoming meeting. "
               "Adapted for A1 French.")

INTRO = ("Late in the evening at ASK, Andrea pulls Camille into a private office to make a desperate confession. "
         "Having thrown away an acclaimed director's screenplay years earlier, Andrea enlists Camille's help to prevent a catastrophic career scandal. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Ferme la porte et assieds-toi là.",
  "Close the door and sit down there.",
  [(192, "Ferme la porte."), (194, "Assieds-toi.")], "Andrea insists on secrecy"),
 ("camille", "Merci Andréa, je finissais mes dossiers.",
  "Thanks Andrea, I was finishing my files.",
  [(195, "Merci d'être resté."), (196, "j'avais des trucs à finir.")], "Camille sits down"),
 ("lea", "Je suis dans une situation terrible, Camille.",
  "I am in a terrible situation, Camille.",
  [(197, "Je suis dans la merde, Camille. Vraiment dans la merde.")], "Andrea confesses distress"),
 ("lea", "Tu es la seule personne de confiance.",
  "You are the only trustworthy person.",
  [(198, "Tu es la seule personne ici en qui j'ai entièrement confiance")], "Andrea praises Camille"),
 ("lea", "Je n'ai pas rappelé Isabelle Adjani.",
  "I have not called Isabelle Adjani back.",
  [(200, "Je n'ai pas rappelé Isabelle Adjani.")], "Andrea reveals the dilemma"),
 ("camille", "Pourquoi n'as-tu pas appelé Isabelle?",
  "Why didn't you call Isabelle?",
  [(203, "Pourquoi tu as fait ça ?")], "Camille asks"),
 ("lea", "J'ai jeté le scénario à la poubelle!",
  "I threw the script in the trash!",
  [(202, "j'ai jeté le scénario d'Amour Éternel directement à la poubelle.")], "Andrea confesses"),
 ("lea", "C'était il y a quatre ans.",
  "That was four years ago.",
  [(201, "il y a quatre ans")], "Andrea gives timeline"),
 ("lea", "C'est la pire bourde de ma carrière.",
  "It is the worst blunder of my career.",
  [(207, "La pire bourde de ma carrière.")], "Andrea admits guilt"),
 ("camille", "Est-ce que la situation est irrattrapable?",
  "Is the situation truly beyond repair?",
  [(210, "C'est vraiment irrattrapable ?")], "Camille evaluates"),
 ("lea", "Isabelle et Hartman ne doivent pas se voir.",
  "Isabelle and Hartman must not see each other.",
  [(216, "Donc ils ne doivent pas se rencontrer.")], "Andrea sets objective"),
 ("lea", "J'ai besoin de toi pour bloquer ça.",
  "I need you to block that.",
  [(218, "C'est pour ça que j'ai besoin de toi."), (219, "Pour mettre des bâtons dans les roues.")], "Andrea asks for help"),
 ("camille", "D'accord Andréa, je vais t'aider.",
  "All right Andrea, I will help you.",
  [(224, "C'est bon."), (225, "Je le fais.")], "Camille agrees"),
]

OPENER = "Let's examine how Andrea confides her biggest professional mistake to Camille step by step."

WALK = [
 (0, None,
  "'Close the door and sit down there.' Andrea ensures maximum privacy before revealing her secret."),
 (1, None,
  "'Thanks Andrea, I was finishing my files.' Camille explains why she was still working late at the agency."),
 (2, None,
  "'I am in a terrible situation, Camille.' Andrea admits she is in deep trouble regarding a major star client."),
 (3, None,
  "'You are the only trustworthy person.' Andrea expresses full confidence in Camille's discretion and loyalty."),
 (4, None,
  "'I have not called Isabelle Adjani back.' Andrea reveals she has been avoiding returning Isabelle Adjani's calls."),
 (5, None,
  "'Why didn't you call Isabelle?' Camille wonders what could make Andrea avoid her most prestigious client."),
 (6, None,
  "'I threw the script in the trash!' Andrea confesses that she trashed director Hartman's original screenplay."),
 (7, None,
  "'That was four years ago.' Andrea explains that the reckless decision happened years in the past."),
 (8, None,
  "'It is the worst blunder of my career.' Andrea recognizes that the mistake could ruin her professional reputation."),
 (9, None,
  "'Is the situation truly beyond repair?' Camille asks if there is any diplomatic way to fix the error."),
 (10, None,
  "'Isabelle and Hartman must not see each other.' Andrea explains that an in-person meeting will expose her lie immediately."),
 (11, None,
  "'I need you to block that.' Andrea tasks Camille with secretly derailing the scheduled encounter."),
 (12, None,
  "'All right Andrea, I will help you.' Camille agrees to stand by Andrea and help sabotage the meeting."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Andrea shares her darkest career secret with Camille, forging a deep alliance that puts Camille in a delicate undercover role. "
         "Let's review the key vocabulary and expressions from this dramatic scene.")

CLOSING = ("camille", "D'accord Andréa, je vais t'aider.")
