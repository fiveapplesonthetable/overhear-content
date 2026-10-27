# Authoring module for dix-pour-cent s03e06 scene 28 (cues 1327-1362).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e06/authoring/scene-28.py --out overhear-content/out/dix-pour-cent/s03e06/scene-28.json

ID = "dix-pour-cent-s03e06-scene-28"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 28
TITLE = "Les nominations aux Césars  (The César Nominations)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "arlette": "emilie"}
LABELS = {"lea": "Sophia", "gabriel": "Gabriel", "arlette": "Arlette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 1327-1362. At 4 AM at ASK, Sophia answers the phone and discovers she is nominated "
               "for a Cesar Award. The agency rejoices and embraces a triumphant new beginning.")

INTRO = ("At four in the morning inside the darkened ASK agency, the reception phone begins ringing urgently. "
         "Sophia answers to receive life-changing news from the Cesar Academy, sparking celebration and hope for ASK's future. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("gabriel", "Sophia, tu décroches le téléphone?",
  "Sophia, will you pick up the phone?",
  [(1327, "Sophia"), (1329, "Tu décroches")], "Asking to answer phone"),
 ("lea", "Il est quatre heures du matin!",
  "It is four in the morning!",
  [(1330, "Il est 4h")], "Complaining about hour"),
 ("lea", "Allô, agence ASK, bonjour.",
  "Hello, ASK agency, good morning.",
  [(1333, "bonjour")], "Answering professionally"),
 ("lea", "La liste des nommés arrive?",
  "The nominees list is arriving?",
  [(1334, "liste des nommés")], "Listening to academy announcement"),
 ("lea", "Je suis nommée aux Césars?",
  "I am nominated for the Cesars?",
  [(1339, "nommée Sophia Leprince"), (1344, "nommée aux Césars")], "Expressing disbelief"),
 ("gabriel", "Félicitations ma chère Sophia!",
  "Congratulations my dear Sophia!",
  [(1343, "Félicitations")], "Congratulating actress"),
 ("arlette", "Dans mes bras, ma poulette!",
  "Into my arms, sweetheart!",
  [(1346, "Dans mes bras, ma poulette")], "Embracing warmly"),
 ("arlette", "C'est la vraie classe!",
  "That is true class!",
  [(1348, "c'est la classe")], "Praising achievement"),
 ("arlette", "Meilleur espoir féminin pour toi!",
  "Best Newcomer for you!",
  [(1347, "Meilleur espoir féminin")], "Announcing category"),
 ("lea", "Merci du fond du cœur.",
  "Thank you from the bottom of my heart.",
  [(1349, "Merci, Arlette")], "Expressing heartfelt gratitude"),
 ("gabriel", "Nous allons rebondir tous ensemble.",
  "We are going to bounce back together.",
  [(1354, "on va rebondir")], "Looking to future"),
 ("gabriel", "C'est tellement excitant maintenant.",
  "It is so exciting now.",
  [(1358, "c'est excitant")], "Sharing optimism"),
 ("arlette", "Quelque chose s'ouvre enfin ici.",
  "Something is finally opening up here.",
  [(1359, "quelque chose qui s'ouvre")], "Sensing new dawn"),
 ("gabriel", "C'est un tout nouveau départ!",
  "It is a brand new start!",
  [(1362, "C'est un nouveau départ")], "Celebrating fresh start"),
]

WALK = [
 (0, None,
  "'Sophia, will you pick up the phone?' Gabriel asks as the late-night telephone rings. "
  "The verb 'decrocher' specifically means to pick up the telephone receiver."),
 (1, None,
  "'It is four in the morning!' Sophia protests at being asked to answer calls at dawn. "
  "The time construction 'quatre heures du matin' denotes early morning."),
 (2, None,
  "'Hello, ASK agency, good morning.' Sophia answers with professional courtesy. "
  "The greeting 'allo' is used exclusively when answering the phone in France."),
 (3, None,
  "'The nominees list is arriving?' Sophia realizes the Cesar Academy is calling. "
  "The past participle 'nommes' acts as a noun referring to award nominees."),
 (4, None,
  "'I am nominated for the Cesars?' Sophia cannot believe her own ears. "
  "The proper noun 'Cesars' designates France's highest cinematic honors."),
 (5, None,
  "'Congratulations my dear Sophia!' Gabriel beams with uncontainable joy for his client. "
  "The plural noun 'felicitations' expresses praise and congratulations."),
 (6, None,
  "'Into my arms, sweetheart!' Arlette sweeps Sophia into an affectionate embrace. "
  "The affectionate term 'ma poulette' is an endearing colloquial term."),
 (7, None,
  "'That is true class!' Arlette expresses genuine admiration for the milestone. "
  "The colloquial noun 'la classe' describes outstanding style and elegance."),
 (8, None,
  "'Best Newcomer for you!' Arlette celebrates the prestigious category. "
  "The noun phrase 'meilleur espoir' designates the award for Most Promising Actress."),
 (9, None,
  "'Thank you from the bottom of my heart.' Sophia thanks her mentors tearfully. "
  "The idiom 'du fond du coeur' expresses deep gratitude."),
 (10, None,
  "'We are going to bounce back together.' Gabriel rallies the team spirit for the upcoming year. "
  "The verb 'rebondir' figuratively means to bounce back after setbacks."),
 (11, None,
  "'It is so exciting now.' Gabriel embraces the thrill of renewed agency momentum. "
  "The adjective 'excitant' denotes stimulating anticipation."),
 (12, None,
  "'Something is finally opening up here.' Arlette perceives the positive shift in ASK's fortunes. "
  "The reflexive verb 's'ouvrir' symbolizes fresh opportunities emerging."),
 (13, None,
  "'It is a brand new start!' Gabriel concludes with exuberance as a new dawn begins. "
  "The noun 'depart' in 'nouveau depart' signifies a fresh beginning."),
]

OUTRO = ("The celebratory cheers echo through the agency as dawn breaks over Paris. "
         "With Sophia's prestigious nomination and Andrea taking the helm, ASK enters an exciting new era. "
         "Now, let's review the scene one last time.")

CLOSING = ("gabriel", "C'est un tout nouveau départ!")
