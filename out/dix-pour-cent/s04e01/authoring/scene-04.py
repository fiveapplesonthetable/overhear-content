# Authoring module for dix-pour-cent s04e01 scene 04 (cues 179-192).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-04.py --out out/dix-pour-cent/s04e01/scene-04.json

ID = "dix-pour-cent-s04e01-scene-04"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 4
TITLE = "La robe des César  (The César Dress)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "vendeur": "theo"}
LABELS = {"lea": "Noémie", "vendeur": "Le Vendeur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 179-192. Noemie shops for an eye-catching dress for the Cesar ceremony with a boutique stylist. Adapted for A1 French.")

INTRO = ("In a fashionable Parisian boutique, Noemie Leclerc shops for the ideal outfit to accompany Mathias Barneville to the prestigious Cesar ceremony. "
         "Dismissing conventional sobriety in favor of flamboyant seduction, she works with a confident boutique stylist to discover a dress matching her personality. "
         "Together, they celebrate a look that embraces contrast, boldness, and irresistible charm. "
         "Let's listen to the scene in French first.")

STORY = [
 ("vendeur", "C'est pour une fête d'anniversaire?",
  "Is it for a birthday party?",
  [(179, "C'est pour un anniversaire")], "Inquired about dress occasion"),
 ("lea", "Non, c'est pour la cérémonie des César.",
  "No, it is for the Cesar ceremony.",
  [(181, "La Cérémonie des César")], "Specified prestigious awards event"),
 ("vendeur", "J'ai habillé beaucoup de grandes actrices.",
  "I have dressed many great actresses.",
  [(182, "J'ai habillé beaucoup d'actrices")], "Boasted high-fashion styling credentials"),
 ("vendeur", "Voici une robe chic et sobre.",
  "Here is a chic and understated dress.",
  [(184, "Chic, sobre")], "Presented classic elegant dress"),
 ("lea", "Cette robe classique est plutôt ennuyeuse.",
  "This classic dress is rather boring.",
  [(186, "Mais surtout ennuyeux")], "Rejected traditional design as dull"),
 ("vendeur", "Vous habillez-vous pour impressionner le public?",
  "Do you dress to impress the public?",
  [(191, "pour impressionner ou pour séduire")], "Probed customer's styling intention"),
 ("lea", "Pour moi, c'est une question de séduction.",
  "For me, it is a matter of seduction.",
  [(192, "une question de séduction")], "Declared seductive fashion priority"),
 ("vendeur", "Je comprends, vous aimez les contrastes.",
  "I understand, you love contrasts.",
  [(196, "Flashy mais classe")], "Interpreted aesthetic preference"),
 ("vendeur", "Voici un modèle flashy et audacieux.",
  "Here is a flashy and daring design.",
  [(197, "Simple et audacieux")], "Recommended eye-catching vibrant outfit"),
 ("lea", "Cette tenue audacieuse est tellement moi!",
  "This daring outfit is so me!",
  [(200, "C'est tellement moi")], "Exclaimed instant delight with selection"),
 ("lea", "Une femme doit assumer ses contradictions.",
  "A woman must embrace her contradictions.",
  [(198, "assume ses contradictions")], "Articulated bold personal philosophy"),
 ("vendeur", "Elle vous donnera une allure inoubliable.",
  "It will give you an unforgettable look.",
  [(182, "J'ai habillé beaucoup d'actrices")], "Praised stunning transformative effect"),
 ("lea", "Mathias sera totalement sous le charme.",
  "Mathias will be totally charmed.",
  [(192, "une question de séduction")], "Anticipated partner's enthusiastic reaction"),
 ("vendeur", "Vous brillerez sur le tapis rouge.",
  "You will shine on the red carpet.",
  [(181, "La Cérémonie des César")], "Complimented star presence"),
]

OPENER = "Let's observe as Noemie selects a daring dress for the prestigious film gala."

WALK = [
 (0, None,
  "'Is it for a birthday party?' A courteous inquiry seeking the occasion for the new outfit."),
 (1, None,
  "'No, it is for the Cesar ceremony.' A proud specification identifying France's premier cinematic gala."),
 (2, None,
  "'I have dressed many great actresses.' An impressive claim showcasing the stylist's celebrity fashion credentials."),
 (3, None,
  "'Here is a chic and understated dress.' A polite proposal showcasing a conventional and understated garment."),
 (4, None,
  "'This classic dress is rather boring.' A frank rejection dismissing understated elegance as uninspiring."),
 (5, None,
  "'Do you dress to impress the public?' A discerning question exploring the shopper's true stylistic motives."),
 (6, None,
  "'For me, it is a matter of seduction.' A candid declaration prioritizing personal allure and romantic impact."),
 (7, None,
  "'I understand, you love contrasts.' An intuitive observation recognizing her taste for creative tension in style."),
 (8, None,
  "'Here is a flashy and daring design.' An enthusiastic suggestion presenting a vibrant and daring garment."),
 (9, None,
  "'This daring outfit is so me!' An elated endorsement recognizing the dress as an authentic reflection of her spirit."),
 (10, None,
  "'A woman must embrace her contradictions.' A spirited personal philosophy celebrating individuality and complex charm."),
 (11, None,
  "'It will give you an unforgettable look.' A professional compliment predicting a memorable aesthetic impact."),
 (12, None,
  "'Mathias will be totally charmed.' An affectionate remark anticipating her partner's delighted admiration."),
 (13, None,
  "'You will shine on the red carpet.' A flattering prediction foreseeing a dazzling entrance on cinema's biggest night."),
]

TRANSITION = "Now let's listen to Noemie and the stylist chatting again at full speed."

OUTRO = ("Finding a look that matches her playful confidence, Noemie leaves the boutique prepared to turn heads at the ceremony. "
         "Standing by Mathias in his new life, she intends to make their public appearance unforgettable.")

CLOSING = ("lea", "Je vais faire sensation.")
