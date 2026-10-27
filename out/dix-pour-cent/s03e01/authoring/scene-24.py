# Authoring module for dix-pour-cent s03e01 scene 24 (cues 1002-1018).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-24.py --out out/dix-pour-cent/s03e01/scene-24.json

ID = "dix-pour-cent-s03e01-scene-24"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 24
TITLE = "Sept mois  (Seven Months)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jean": "theo"}
LABELS = {"lea": "Andréa", "jean": "Jean"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 1002-1018. In her office, Andrea declines a drink, prompting Jean Dujardin to notice "
               "her pregnancy. Jean connects the seven months with his own role in Le Déserteur. Adapted for A1 French.")

INTRO = ("In her ASK office, Andrea Martel shares a quiet moment with star actor Jean Dujardin. "
         "When Jean offers her a drink, he suddenly notices her rounded belly and discovers that Andrea is seven months pregnant. "
         "Let's listen to their intimate conversation in French first.")

STORY = [
 ("jean", "Tu veux boire un verre de whisky?",
  "Do you want to drink a glass of whisky?",
  [(1004, "boire du whisky")], "Offered a glass of whisky"),
 ("lea", "Pas pour moi, ça va très bien.",
  "Not for me, I am doing fine.",
  [(1002, "Pas pour moi, ça va.")], "Declined drink politely"),
 ("jean", "Mais tu es enceinte, Andréa!",
  "Oh, but you are pregnant, Andrea!",
  [(1005, "t'es enceinte")], "Noticed pregnancy with surprise"),
 ("lea", "Oui, mais ce n'est pas grave.",
  "Yes, but it is no big deal.",
  [(1006, "c'est pas grave")], "Downplayed situation modestly"),
 ("jean", "Non, je t'assure, c'est formidable.",
  "No, I assure you, it is wonderful.",
  [(1008, "Non, je t'assure, c'est bien.")], "Offered warm reassurance"),
 ("lea", "Tu ne m'en veux pas trop?",
  "You are not too upset with me?",
  [(1009, "ça veut dire")], "Inquired about actor reaction"),
 ("jean", "Tu en es à combien de mois?",
  "How many months along are you?",
  [(1010, "T'en es à combien, là ?")], "Asked about gestation stage"),
 ("lea", "J'en suis déjà à sept mois.",
  "I am already at seven months.",
  [(1011, "7 mois.")], "Stated seven months progress"),
 ("jean", "C'était le début du tournage du Déserteur!",
  "That was the start of shooting The Deserter!",
  [(1013, "c'était le début du déserteur.")], "Recalled project timeline"),
 ("lea", "Oui, exactement à ce moment-là.",
  "Yes, exactly at that time.",
  [(1014, "C'est là où j'ai commencé")], "Confirmed timing of shoot"),
 ("jean", "C'est là que j'ai commencé à déserter.",
  "That is when I began to desert.",
  [(1015, "Déserter ?")], "Reflected on psychological retreat"),
 ("lea", "Tu étais trop immergé dans ton rôle.",
  "You were too immersed in your role.",
  [(1016, "Voilà.")], "Expressed empathy for method acting"),
 ("jean", "Je suis heureux pour toi, Andréa.",
  "I am happy for you, Andrea.",
  [(1017, "7 mois, oui.")], "Declared heartfelt joy for agent"),
 ("lea", "Merci Jean, cela me touche beaucoup.",
  "Thank you Jean, that touches me a lot.",
  [(1018, "Tiens.")], "Expressed gratitude for sincerity"),
]

OPENER = "Let's see how Jean reacts with surprise and warmth upon discovering Andrea's pregnancy."

WALK = [
 (0, None,
  "'Do you want to drink a glass of whisky?' A casual offer with the modal verb vouloir."),
 (1, None,
  "'Not for me, I am doing fine.' A polite refusal using the idiomatic expression for being fine."),
 (2, None,
  "'Oh, but you are pregnant, Andrea!' An astonished exclamation noticing her visible pregnancy."),
 (3, None,
  "'Yes, but it is no big deal.' A modest downplaying statement with the negation ce n'est pas."),
 (4, None,
  "'No, I assure you, it is wonderful.' A warm reassurance praising the joyful news."),
 (5, None,
  "'You are not too upset with me?' An insecure question about holding a grudge."),
 (6, None,
  "'How many months along are you?' An inquiry about the progression of her pregnancy."),
 (7, None,
  "'I am already at seven months.' A temporal statement indicating late pregnancy stage."),
 (8, None,
  "'That was the start of shooting The Deserter!' An imperfect tense recall linking dates together."),
 (9, None,
  "'Yes, exactly at that time.' An adverbial confirmation of the timeline."),
 (10, None,
  "'That is when I began to desert.' A reflective confession playing on the film title."),
 (11, None,
  "'You were too immersed in your role.' An empathetic observation on intense method acting."),
 (12, None,
  "'I am happy for you, Andrea.' A sincere declaration of heartfelt personal joy."),
 (13, None,
  "'Thank you Jean, that touches me a lot.' A grateful closing acknowledging his genuine warmth."),
]

TRANSITION = "Now let's listen to Jean and Andrea again at natural speed."

OUTRO = ("Jean connects the timeline of Andrea's pregnancy with the start of his grueling film shoot, understanding both their struggles. "
         "Their mutual honesty strengthens their bond before Jean prepares to leave the agency.")

CLOSING = ("jean", "Prends bien soin de toi et du bébé.")
