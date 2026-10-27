# Authoring module for dix-pour-cent s02e05 scene 06 (cues 158-188).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e05/authoring/scene-06.py --out out/dix-pour-cent/s02e05/scene-06.json

ID = "dix-pour-cent-s02e05-scene-06"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 6
TITLE = "L'agent junior en priorité  (Junior Agent Priority)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 158-188. In Gabriel's office, Andréa vents about Guy Marchand's deteriorating health "
               "before discussing the recruitment of a junior agent with Gabriel. "
               "Adapted for A1 French.")

INTRO = ("In Gabriel's office, Andrea is anxious after visiting Guy Marchand's doctor. "
         "Trying to shift focus to agency business, she asks Gabriel about recruiting a junior agent, but encounters unexpected hesitation. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Je sors de chez le médecin de Guy.",
  "I have just come from Guy's doctor.",
  [(159, "Je sors de chez le médecin de Guy.")], "Andrea shares the context"),
 ("lea", "La santé de Guy est une catastrophe.",
  "Guy's health is a disaster.",
  [(159, "C'est une catastrophe")], "Andrea describes the medical update"),
 ("gabriel", "Tu veux me parler d'autre chose?",
  "Do you want to talk about something else?",
  [(164, "Tu veux quoi ?"), (165, "Parler.")], "Gabriel asks what is on her mind"),
 ("lea", "Oui, au sujet de l'agent junior.",
  "Yes, about the junior agent.",
  [(168, "Un junior.")], "Andrea introduces the topic"),
 ("lea", "Est-ce que tu en veux un?",
  "Do you want one?",
  [(169, "T'en veux un ou pas ?")], "Andrea asks for Gabriel's stance"),
 ("gabriel", "Prendre un junior ne me fait pas peur.",
  "Taking on a junior does not scare me.",
  [(172, "ça ne me fait pas peur de... de prendre un junior.")], "Gabriel clarifies"),
 ("lea", "Ton avis compte beaucoup pour moi.",
  "Your opinion means a lot to me.",
  [(174, "ton avis compte beaucoup pour moi.")], "Andrea values his input"),
 ("gabriel", "Ce n'est pas ma priorité en ce moment.",
  "It is not my priority right now.",
  [(177, "une de mes priorités en ce moment.")], "Gabriel demurs"),
 ("lea", "Tu veux un garçon ou une fille?",
  "Do you want a boy or a girl?",
  [(178, "Tu veux un garçon ou une fille ?")], "Andrea asks about preferences"),
 ("gabriel", "Les deux me vont très bien.",
  "Both suit me very well.",
  [(179, "Les deux, ça me va, non ?")], "Gabriel stays neutral"),
 ("lea", "Tu crois que ça va te rendre faible?",
  "Do you think that will make you look weak?",
  [(184, "Tu crois que ça va te rendre faible ?")], "Andrea challenges his reserve"),
 ("gabriel", "Je ne suis pas comme ça, Andréa.",
  "I am not like that, Andrea.",
  [(186, "Je ne suis pas comme ça, Andréa.")], "Gabriel defends his openness"),
 ("gabriel", "Maintenant, j'ai beaucoup de travail.",
  "Right now, I have a lot of work.",
  [(187, "J'ai du travail.")], "Gabriel wraps up the talk"),
]

OPENER = "Let's examine Andrea and Gabriel's private office discussion step by step to explore professional boundaries and vulnerabilities."

WALK = [
 (0, None,
  "'I have just come from Guy's doctor.' Andrea explains where she has been earlier that morning."),
 (1, None,
  "'Guy's health is a disaster.' Andrea worries about her veteran actor client's serious medical condition."),
 (2, None,
  "'Do you want to talk about something else?' Gabriel senses she needs to vent about other pressing agency matters."),
 (3, None,
  "'Yes, about the junior agent.' Andrea brings up the ongoing debate over expanding the team."),
 (4, None,
  "'Do you want one?' Andrea seeks Gabriel's honest view on bringing in fresh blood."),
 (5, None,
  "'Taking on a junior does not scare me.' Gabriel insists he is not insecure about mentoring a younger colleague."),
 (6, None,
  "'Your opinion means a lot to me.' Andrea reminds him that she considers him her core partner at ASK."),
 (7, None,
  "'It is not my priority right now.' Gabriel admits he is preoccupied with his own demanding clients."),
 (8, None,
  "'Do you want a boy or a girl?' Andrea asks if he has any demographic preference for the hire."),
 (9, None,
  "'Both suit me very well.' Gabriel stays open-minded with no preference for either."),
 (10, None,
  "'Do you think that will make you look weak?' Andrea probes whether showing stress makes him feel vulnerable."),
 (11, None,
  "'I am not like that, Andrea.' Gabriel asserts that he is not guarded or competitive toward her."),
 (12, None,
  "'Right now, I have a lot of work.' Gabriel closes the discussion to return to his pressing tasks."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Andrea and Gabriel navigate professional challenges and personal vulnerabilities as the agency faces major changes. "
         "Let's review the workplace and emotional vocabulary from this scene.")

CLOSING = ("gabriel", "Maintenant, j'ai beaucoup de travail.")
