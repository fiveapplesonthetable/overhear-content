# Authoring module for dix-pour-cent s02e03 scene 06 (cues 144-173).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-06.py --out out/dix-pour-cent/s02e03/scene-06.json

ID = "dix-pour-cent-s02e03-scene-06"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 6
TITLE = "Une chanteuse pour Julien  (A Singer for Julien)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 144-173. Gabriel tells Sofia that his client Julien Dore is looking for a singer for his musical film. "
               "Gabriel prepares her to meet him without revealing that she is his girlfriend or the agency receptionist. "
               "Adapted for A1 French.")

INTRO = ("In Gabriel's office, Gabriel excitedly tells Sofia that pop singer and client Julien Dore is arriving to discuss his musical movie. "
         "Seeking to launch Sofia's singing career, Gabriel coaches her to act like an established artist while keeping their personal life secret. "
         "Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "Julien Doré vient parler de son film.",
  "Julien Dore is coming to talk about his film.",
  [(144, "Julien Doré vient parler de son film.")], "Gabriel announces Julien's visit"),
 ("lea", "Tu veux me présenter à Julien Doré?",
  "You want to introduce me to Julien Dore?",
  [(145, "Je veux te le présenter."), (146, "Julien Doré ?")], "Sofia is surprised"),
 ("gabriel", "Il cherche une chanteuse pour son film.",
  "He is looking for a singer for his film.",
  [(148, "Il prépare son premier film."), (151, "Il cherche une chanteuse.")], "Gabriel explains the opportunity"),
 ("lea", "Charlotte Le Bon ne chante pas?",
  "Charlotte Le Bon does not sing?",
  [(149, "Charlotte Le Bon."), (153, "Charlotte Le Bon ne sait pas chanter ?")], "Sofia asks about the lead"),
 ("gabriel", "Non, elle chante très mal!",
  "No, she sings very badly!",
  [(153, "elle chante comme une casserole !")], "Gabriel laughs at Charlotte's singing"),
 ("gabriel", "Mais toi, mon amour, tu chantes à merveille.",
  "But you, my love, you sing wonderfully.",
  [(154, "Mais toi, mon amour..."), (155, "tu chantes à merveille.")], "Gabriel praises Sofia"),
 ("lea", "Il sait que je suis ta copine?",
  "Does he know that I am your girlfriend?",
  [(158, "Il sait que je suis ta copine ?")], "Sofia asks about their secret"),
 ("gabriel", "Non, tu es une cliente de l'agence.",
  "No, you are a client of the agency.",
  [(159, "Bien sûr que non."), (160, "tu étais cliente de l'agence.")], "Gabriel keeps it professional"),
 ("gabriel", "Ne te mets pas la pression, Sofia.",
  "Do not put pressure on yourself, Sofia.",
  [(164, "ne te mets pas la pression.")], "Gabriel reassures her"),
 ("lea", "Il sait que je suis réceptionniste?",
  "Does he know that I am a receptionist?",
  [(166, "Il sait que je suis réceptionniste ?")], "Sofia worries about her image"),
 ("gabriel", "Bien sûr que non, assieds-toi là.",
  "Of course not, sit down there.",
  [(167, "Bien sûr que non !"), (168, "assieds-toi sur le canapé.")], "Gabriel instructs her"),
 ("gabriel", "Tu aimes vraiment Julien Doré?",
  "Do you really like Julien Dore?",
  [(171, "Tu aimes Julien Doré ?")], "Gabriel asks"),
 ("lea", "Je l'adore, c'est pour ça que je panique!",
  "I adore him, that is why I am panicking!",
  [(172, "Je l'adore !"), (173, "C'est pour ça que je panique !")], "Sofia admits her nervousness"),
]

OPENER = "Let's examine how Gabriel coaches Sofia step by step to prepare for the meeting."

WALK = [
 (0, None,
  "'Julien Dore is coming to talk about his film.' Gabriel announces the impending arrival of his pop-star client."),
 (1, None,
  "'You want to introduce me to Julien Dore?' Sofia is amazed that Gabriel wants to set up a meeting."),
 (2, None,
  "'He is looking for a singer for his film.' Gabriel reveals that Julien needs a singing partner for his musical soundtrack."),
 (3, None,
  "'Charlotte Le Bon does not sing?' Sofia inquires about the film's lead actress."),
 (4, None,
  "'No, she sings very badly!' Gabriel humorously confesses that Charlotte has no musical talent."),
 (5, None,
  "'But you, my love, you sing wonderfully.' Gabriel affectionately praises Sofia's remarkable singing voice."),
 (6, None,
  "'Does he know that I am your girlfriend?' Sofia asks if Julien is aware of their romantic relationship."),
 (7, None,
  "'No, you are a client of the agency.' Gabriel explains that he presented her strictly as an agency talent."),
 (8, None,
  "'Do not put pressure on yourself, Sofia.' Gabriel encourages Sofia to relax before the audition."),
 (9, None,
  "'Does he know that I am a receptionist?' Sofia worries that her day job at ASK will undermine her credibility."),
 (10, None,
  "'Of course not, sit down there.' Gabriel directs her to sit on the couch and look like an established actress."),
 (11, None,
  "'Do you really like Julien Dore?' Gabriel asks about her opinion of the musician."),
 (12, None,
  "'I adore him, that is why I am panicking!' Sofia admits she is terrified precisely because she is such a big fan."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Gabriel prepares Sofia to impress Julien Dore while carefully guarding her dual identity as receptionist and girlfriend. "
         "Let's review the vocabulary and conversational expressions used in this dialogue.")

CLOSING = ("lea", "Je l'adore, c'est pour ça que je panique!")
