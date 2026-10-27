# Authoring module for dix-pour-cent s02e02 scene 03 (cues 105-129).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-03.py --out out/dix-pour-cent/s02e02/scene-03.json

ID = "dix-pour-cent-s02e02-scene-03"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 3
TITLE = "En route pour l'audition  (On the Way to the Audition)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 105-129. Gabriel rushes Sofia Leprince to an audition and tries to help her "
               "understand her character. Adapted for A1 French.")

INTRO = ("At the ASK reception desk, Gabriel greets his client Sofia Leprince as they prepare for an important casting call. "
         "With the audition appointment only minutes away, Sofia asks anxious questions about her character and the script. "
         "Let's listen to their conversation in French first.")

STORY = [
 ("lea", "Bonjour Gabriel, désolée pour mon retard.",
  "Hello Gabriel, sorry for my delay.",
  [(105, "Bonjour."), (110, "Au fait, désolée pour ça.")], "Adapted apology for being late"),
 ("gabriel", "Pose ton sac, on y va!",
  "Put your bag down, let's go!",
  [(111, "Pose ton sac, on y va.")], ""),
 ("gabriel", "On est très en retard pour ton audition.",
  "We are very late for your audition.",
  [(112, "On est en retard,")], "Added intensifier and destination"),
 ("lea", "J'ai une seule question sur le texte.",
  "I have just one question about the text.",
  [(113, "Une seule question...")], "Framed as complete sentence"),
 ("lea", "Je n'ai pas lu tout le scénario.",
  "I have not read the entire script.",
  [(114, "Je n'ai pas lu tout le scénario.")], ""),
 ("lea", "Je ne suis pas sûre du personnage.",
  "I am not sure about the character.",
  [(115, "Je ne suis pas sûre du personnage.")], ""),
 ("gabriel", "C'est une jeune secrétaire jolie et sexy.",
  "She is a young, pretty, and sexy secretary.",
  [(118, "C'est juste une jeune secrétaire jolie et sexy.")], "Simplified 'juste une'"),
 ("gabriel", "Elle croise son patron et décide de le séduire.",
  "She runs into her boss and decides to seduce him.",
  [(119, "Elle croise son patron et décide de le séduire.")], ""),
 ("lea", "Draguer son patron dans une boucherie?",
  "Hitting on her boss in a butcher shop?",
  [(122, "Draguer son patron dans une boucherie ?")], ""),
 ("lea", "En plus, il pourrait être son père!",
  "Besides, he could be her father!",
  [(123, "En plus, il pourrait être son père...")], ""),
 ("gabriel", "Sofia, ne complique pas les choses.",
  "Sofia, do not complicate things.",
  [(125, "trouve un autre boulot.")], "Adapted advice"),
 ("gabriel", "On perd du temps, allons-y maintenant.",
  "We are wasting time, let us go now.",
  [(121, "Allons-y."), (126, "On perd du temps.")], ""),
 ("lea", "D'accord, je suis prête.",
  "Okay, I am ready.",
  [(129, "D'accord.")], "Added affirmation"),
 ("gabriel", "Respire et montre ton plus grand sourire.",
  "Breathe and show your biggest smile.",
  [(116, "avec un grand sourire")], "Encouraging closing advice"),
]

OPENER = "Let's examine how Gabriel prepares Sofia for her casting session."

WALK = [
 (0, None,
  "'Hello Gabriel, sorry for my delay.' Sofia greets her agent with a polite apology for running late."),
 (1, None,
  "'Put your bag down, let's go!' Gabriel gives urgent directions to get moving without delay."),
 (2, None,
  "'We are very late for your audition.' An emphatic statement about their tight schedule."),
 (3, None,
  "'I have just one question about the text.' A polite request for clarification before rushing out."),
 (4, None,
  "'I have not read the entire script.' A negative compound past statement explaining her lack of preparation."),
 (5, None,
  "'I am not sure about the character.' An expression of doubt regarding how to play the role."),
 (6, None,
  "'She is a young, pretty, and sexy secretary.' Gabriel gives a very simple summary of the role."),
 (7, None,
  "'She runs into her boss and decides to seduce him.' A brief overview of the plot action in the scene."),
 (8, None,
  "'Hitting on her boss in a butcher shop?' Sofia expresses disbelief at the bizarre audition setting."),
 (9, None,
  "'Besides, he could be her father!' A conditional observation highlighting the age difference."),
 (10, None,
  "'Sofia, do not complicate things.' A reassuring imperative advising her to keep it simple."),
 (11, None,
  "'We are wasting time, let us go now.' An urgent reminder that they must leave immediately."),
 (12, None,
  "'Okay, I am ready.' A calm confirmation that she is prepared to face the director."),
 (13, None,
  "'Breathe and show your biggest smile.' Friendly advice on stage presence from her supportive agent."),
]

TRANSITION = "Now let's listen to their conversation in the lobby again without pausing."

OUTRO = ("Gabriel rushes Sofia to the casting appointment despite her doubts about the script. "
         "In the next scene, Sofia will have to face a demanding casting director.")

CLOSING = ("lea", "C'est parti!")
