# Authoring module for dix-pour-cent s02e03 scene 01 (cues 1-31).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-01.py --out out/dix-pour-cent/s02e03/scene-01.json

ID = "dix-pour-cent-s02e03-scene-01"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 1
TITLE = "Norman s'entraîne à conduire  (Norman's Driving Practice)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Norman", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-31. Norman Thavaud and Gabriel Sarda prepare for Norman's driving test, "
               "but Norman struggles behind the wheel. Adapted for A1 French.")

INTRO = ("At the ASK agency, agent Gabriel Sarda escorts his young client, popular comedian Norman Thavaud, "
         "to a crucial driving lesson. Norman needs his driving license urgently for an upcoming film role, "
         "but his driving skills leave much to be desired. Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "On est dans les temps pour l'examen?",
  "Are we on time for the exam?",
  [(2, "On est dans les temps ?")], "Added explicit mention of exam"),
 ("lea", "Il faut se dépêcher, c'est loin.",
  "We must hurry, it is far.",
  [(3, "Faut se dépêcher. -C'est loin.")], "Added subject pronoun"),
 ("gabriel", "Ne t'inquiète pas, respire bien.",
  "Do not worry, breathe deeply.",
  [(16, "Ça va aller. Respire bien.")], "Added calming negative imperative"),
 ("lea", "Ça ne sert à rien d'être tendu.",
  "It is useless to be tense.",
  [(18, "Comme je disais, ça sert à rien d'être tendu.")], "Simplified speech"),
 ("gabriel", "Tu as oublié de parapher cette feuille.",
  "You forgot to initial this sheet.",
  [(6, "Désolé, vous avez oublié de parapher...")], "Adjusted pronoun to familiar address"),
 ("lea", "Attends, voilà, c'est bon maintenant.",
  "Wait, here, it is good now.",
  [(7, "-celle-là. -Attends."), (8, "C'est bon.")], "Combined short cue confirmations"),
 ("gabriel", "Très bien, on y va quand même.",
  "Very good, we go anyway.",
  [(11, "On y va quand même. D'accord.")], "Replaced accord with encouragement"),
 ("gabriel", "Bonne chance pour ton permis de conduire.",
  "Good luck for your driving license.",
  [(13, "-Bonne chance, Norman.")], "Specified driving license"),
 ("lea", "Merci Gabriel, je suis un peu stressé.",
  "Thank you Gabriel, I am a bit stressed.",
  [(13, "-Merci."), (20, "Je suis pas tendu du tout.")], "Added polite address and frank admission"),
 ("lea", "Est-ce que je continue tout droit?",
  "Do I continue straight ahead?",
  [(24, "-Je continue ?")], "Clarified driving question"),
 ("gabriel", "Norman, il faut passer en deuxième.",
  "Norman, you must shift into second gear.",
  [(25, "Norman, il faut passer en deuxième...")], "Kept driving instruction"),
 ("gabriel", "Attention, c'est la cinquième vitesse!",
  "Watch out, that is fifth gear!",
  [(27, "C'est la cinquième... Lâchez pas !")], "Specified gear noun"),
 ("gabriel", "N'appuie pas sur le frein et l'accélérateur.",
  "Do not press on the brake and the accelerator.",
  [(29, "N'appuyez pas"), (30, "sur le frein et l'accélérateur en même temps !")], "Shortened dual pedals instruction"),
 ("lea", "D'accord, je respire calmement.",
  "All right, I am breathing calmly.",
  [(28, "Respirez bien maintenant. Voilà.")], "Added first person reaction"),
]

OPENER = "Let's examine how Gabriel coaches Norman during the driving lesson."

WALK = [
 (0, None,
  "'Are we on time for the exam?' An interrogative phrase inquiring about their schedule."),
 (1, None,
  "'We must hurry, it is far.' An impersonal expression of necessity followed by distance."),
 (2, None,
  "'Do not worry, breathe deeply.' A reassuring negative imperative paired with a regular verb."),
 (3, None,
  "'It is useless to be tense.' A colloquial idiom expressing futility."),
 (4, None,
  "'You forgot to initial this sheet.' A compound past verb governing an infinitive."),
 (5, None,
  "'Wait, here, it is good now.' A series of short conversational particles confirming completion."),
 (6, None,
  "'Very good, we go anyway.' An encouraging adverbial opener with an idiomatic motion verb."),
 (7, None,
  "'Good luck for your driving license.' A classic wish of success specifying the driver's test."),
 (8, None,
  "'Thank you Gabriel, I am a bit stressed.' A courteous thanks followed by an adjective of emotional state."),
 (9, None,
  "'Do I continue straight ahead?' A standard interrogative formula asking for directional guidance."),
 (10, None,
  "'Norman, you must shift into second gear.' An impersonal modal verb followed by an ordinal gear number."),
 (11, None,
  "'Watch out, that is fifth gear!' An exclamatory warning pointing out a mechanical error."),
 (12, None,
  "'Do not press on the brake and the accelerator.' A negative imperative commanding pedal coordination."),
 (13, None,
  "'All right, I am breathing calmly.' An agreement token followed by an adverbial description of composure."),
]

TRANSITION = "Now let's listen to Norman's frantic driving practice again at full speed."

OUTRO = ("Norman tries his best behind the wheel, but his lack of driving experience makes Gabriel anxious. "
         "The upcoming film role requires a valid driver's license, raising the pressure on ASK.")

CLOSING = ("gabriel", "Respire, Norman!")
