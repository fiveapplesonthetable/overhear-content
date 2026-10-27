# Authoring module for dix-pour-cent s02e06 scene 07 (cues 134-157).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-07.py --out out/dix-pour-cent/s02e06/scene-07.json

ID = "dix-pour-cent-s02e06-scene-07"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 7
TITLE = "Ouvrir l'appétit  (Sharpens My Appetite)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo"}
LABELS = {"lea": "Andréa", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 134-157. Outside Andrea's apartment after dinner, Hicham notices Andrea's hearty appetite "
               "and comments on the subtle changes brought on by her early pregnancy. "
               "Adapted for A1 French.")

INTRO = ("Outside Andrea's apartment building after dinner, Hicham gently probes Andrea about her pregnancy and future plans. "
         "Andrea feels conflicted about becoming a mother while managing top clients at the Cannes festival. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Merci pour ce très bon dîner, Hicham.",
  "Thank you for this very good dinner, Hicham.",
  [(134, "Merci pour le dîner.")], "Andrea thanks Hicham for dinner"),
 ("hicham", "Je ne t'ai jamais vue manger autant!",
  "I have never seen you eat so much!",
  [(135, "Je ne t'ai jamais vue manger comme ça.")], "Hicham remarks on her appetite"),
 ("lea", "Être avec toi m'ouvre l'appétit.",
  "Being with you whets my appetite.",
  [(136, "Être avec toi m'ouvre l'appétit.")], "Andrea deflects with humor"),
 ("hicham", "Ce n'est pas plutôt la grossesse?",
  "Is it not rather the pregnancy?",
  [(137, "C'est pas plutôt la grossesse ?")], "Hicham mentions the pregnancy"),
 ("lea", "Non, je ne crois pas vraiment.",
  "No, I do not really think so.",
  [(138, "Non, je ne crois pas. Et toi ?")], "Andrea downplays the effect"),
 ("lea", "Est-ce que j'ai beaucoup grossi?",
  "Have I gained a lot of weight?",
  [(141, "-J'ai grossi ?")], "Andrea asks about her body"),
 ("hicham", "Non, mais cette grossesse t'a changée.",
  "No, but this pregnancy has changed you.",
  [(142, "ça t'a changée d'une certaine façon.")], "Hicham observes gently"),
 ("hicham", "Tu es plus calme et très rayonnante.",
  "You are calmer and very radiant.",
  [(143, "Tu es plus calme, plus rayonnante.")], "Hicham compliments her"),
 ("lea", "Mes seins ne sont pas très rayonnants!",
  "My breasts are not very radiant!",
  [(144, "Mes seins ne sont pas vraiment rayonnants !")], "Andrea reacts with self-mockery"),
 ("hicham", "Je reconnais bien ta rue maintenant.",
  "I recognize your street well now.",
  [(146, "Oui, je reconnais ta rue.")], "Hicham notes the familiar spot"),
 ("hicham", "Tu t'inquiètes pour le futur bébé?",
  "Are you worried about the future baby?",
  [(151, "Tu t'inquiètes ?")], "Hicham expresses concern"),
 ("lea", "Je ne sais pas ce que je ferai.",
  "I do not know what I will do.",
  [(155, "Je ne sais pas ce que je vais faire.")], "Andrea admits uncertainty"),
 ("lea", "On se verra à mon retour de Cannes.",
  "We will see each other on my return from Cannes.",
  [(156, "On se voit à mon retour de Cannes ?")], "Andrea postpones the discussion"),
]

OPENER = "Let's examine Andrea and Hicham's intimate street conversation step by step to explore romantic ambiguity and parenthood."

WALK = [
 (0, None,
  "'Thank you for this very good dinner, Hicham.' Andrea thanks him politely as they arrive outside her home."),
 (1, None,
  "'I have never seen you eat so much!' Hicham teases her about clearing her plate with unusual gusto."),
 (2, None,
  "'Being with you whets my appetite.' Andrea offers a playful excuse for eating heartily."),
 (3, None,
  "'Is it not rather the pregnancy?' Hicham directly brings up her developing condition."),
 (4, None,
  "'No, I do not really think so.' Andrea avoids dwelling on medical symptoms."),
 (5, None,
  "'Have I gained a lot of weight?' Andrea checks self-consciously if physical changes are already obvious."),
 (6, None,
  "'No, but this pregnancy has changed you.' Hicham reassures her with affectionate honesty."),
 (7, None,
  "'You are calmer and very radiant.' Hicham notices a softer and warmer demeanor in her."),
 (8, None,
  "'My breasts are not very radiant!' Andrea jokes about the uncomfortable physical transformations."),
 (9, None,
  "'I recognize your street well now.' Hicham recalls past visits to her apartment block."),
 (10, None,
  "'Are you worried about the future baby?' Hicham asks if she feels anxious about impending motherhood."),
 (11, None,
  "'I do not know what I will do.' Andrea confesses her deep uncertainty about the road ahead."),
 (12, None,
  "'We will see each other on my return from Cannes.' Andrea defers major life decisions until after the festival."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Hicham and Andrea share a tender moment on the Parisian pavement as pregnancy forces Andrea to reconsider her priorities before Cannes. "
         "Let's review the key vocabulary from this scene.")

CLOSING = ("lea", "On se verra à mon retour de Cannes.")
