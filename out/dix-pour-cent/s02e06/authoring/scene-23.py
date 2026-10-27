# Authoring module for dix-pour-cent s02e06 scene 23 (cues 622-646).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-23.py --out out/dix-pour-cent/s02e06/scene-23.json

ID = "dix-pour-cent-s02e06-scene-23"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 23
TITLE = "Enivré par le pouvoir  (Intoxicated by Power)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gillieres": "theo"}
LABELS = {"lea": "Juliette", "gillieres": "Gillières"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 622-646. Backstage at the Palais, Jean-Denis Gillieres corners Juliette Binoche, "
               "confessing his intense infatuation, but Juliette skillfully defuses the situation with wit. "
               "Adapted for A1 French.")

INTRO = ("Backstage before the opening ceremony, wealthy businessman Gillieres corners Juliette Binoche. "
         "He confesses an overwhelming attraction, but Juliette uses her quick wit to outsmart him. "
         "Let's listen to the scene in French first.")

STORY = [
 ("gillieres", "Je voulais te souhaiter bonne chance.",
  "I wanted to wish you good luck.",
  [(622, "te souhaiter bonne chance.")], "Gillieres offers good wishes"),
 ("gillieres", "Tu es magnifique, tu me rends fou!",
  "You are magnificent, you drive me crazy!",
  [(624, "tu me rends fou !")], "Gillieres expresses attraction"),
 ("gillieres", "Le pouvoir que tu as m'enivre!",
  "The power you have intoxicates me!",
  [(625, "Le pouvoir que tu as m'enivre.")], "Gillieres describes fascination"),
 ("lea", "Merci Jean-Denis, mais sois bien raisonnable.",
  "Thank you Jean-Denis, but be quite sensible.",
  [(628, "Non, mais...")], "Juliette sets boundaries"),
 ("gillieres", "Tu ne veux pas de moi?",
  "Do you not want me?",
  [(629, "Tu ne veux pas ?")], "Gillieres questions her reluctance"),
 ("lea", "Si, mais pas de cette manière.",
  "Yes, but not this way.",
  [(630, "Si, mais...")], "Juliette deflects gently"),
 ("lea", "Je ne veux rien partager.",
  "I do not want to share anything.",
  [(631, "te partager avec ta femme.")], "Juliette evokes his marriage"),
 ("lea", "Donne-moi ton téléphone portable, voyons!",
  "Give me your cell phone, come on!",
  [(632, "Donne-moi ton téléphone")], "Juliette asks for his phone"),
 ("gillieres", "Pourquoi veux-tu mon téléphone portable?",
  "Why do you want my cell phone?",
  [(632, "ton téléphone")], "Gillieres wonders why she asks"),
 ("lea", "Nous allons appeler ta femme Caroline!",
  "We are going to call your wife Caroline!",
  [(632, "on va l'appeler."), (633, "Caroline")], "Juliette threatens to call his wife"),
 ("gillieres", "Attends, parlons plutôt après la fête.",
  "Wait, let us talk rather after the party.",
  [(636, "Après la cérémonie.")], "Gillieres backs off"),
 ("lea", "Oui, après la grande cérémonie officielle.",
  "Yes, after the big official ceremony.",
  [(636, "Après la cérémonie.")], "Juliette agrees to delay"),
 ("gillieres", "C'est bien plus sage ainsi.",
  "It is much wiser this way.",
  [(637, "c'est mieux.")], "Gillieres accepts the postponement"),
 ("lea", "À tout à l'heure, cher ami!",
  "See you later, dear friend!",
  [(637, "À tout à l'heure")], "Juliette takes her leave"),
]

OPENER = "Let's examine how Juliette skillfully defuses the advances of Gillieres step by step."

WALK = [
 (0, None,
  "'I wanted to wish you good luck.' Gillieres approaches Juliette backstage before her entrance."),
 (1, None,
  "'You are magnificent, you drive me crazy!' Gillieres expresses his overwhelming attraction to the star."),
 (2, None,
  "'The power you have intoxicates me!' Gillieres is captivated by Juliette's aura and authority."),
 (3, None,
  "'Thank you Jean-Denis, but be quite sensible.' Juliette politely deflects his improper advances."),
 (4, None,
  "'Do you not want me?' Gillieres presses his case despite her hesitation."),
 (5, None,
  "'Yes, but not this way.' Juliette maintains her dignity while rejecting the proposition."),
 (6, None,
  "'I do not want to share anything.' Juliette reminds him of his personal commitments."),
 (7, None,
  "'Give me your cell phone, come on!' Juliette cleverly proposes calling his spouse."),
 (8, None,
  "'Why do you want my cell phone?' Gillieres suddenly grows nervous at her unexpected request."),
 (9, None,
  "'We are going to call your wife Caroline!' Juliette uses wit to defuse the awkward situation."),
 (10, None,
  "'Wait, let us talk rather after the party.' Gillieres quickly backs down from his insistence."),
 (11, None,
  "'Yes, after the big official ceremony.' Juliette agrees to postpone any discussion safely."),
 (12, None,
  "'It is much wiser this way.' Gillieres accepts the polite retreat with relief."),
 (13, None,
  "'See you later, dear friend!' Juliette bids him farewell and returns to her duties."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Juliette Binoche masterfully defuses an uncomfortable confrontation with humor and sharp presence of mind. "
         "Let's review the key expressions and vocabulary from this scene.")

CLOSING = ("lea", "À tout à l'heure, cher ami!")
