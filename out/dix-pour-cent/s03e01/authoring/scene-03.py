# Authoring module for dix-pour-cent s03e01 scene 03 (cue 57).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-03.py --out out/dix-pour-cent/s03e01/scene-03.json

ID = "dix-pour-cent-s03e01-scene-03"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 3
TITLE = "Un verre d'eau  (A Glass of Water)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cue 57. Gabriel returns with a glass of water for Andréa as her contraction passes, "
               "urging her to slow down her work pace for her health. Adapted for A1 French.")

INTRO = ("Catching her breath in her office chair, pregnant agent Andrea receives a glass of water from loyal colleague Gabriel. "
         "As her physical discomfort subsides, Gabriel urges her to moderate her intense working schedule for her child's sake. "
         "Let's listen to their intimate conversation in French first.")

STORY = [
 ("gabriel", "Voici ton verre d'eau fraîche, Andréa.",
  "Here is your glass of fresh water, Andrea.",
  [(55, "Je reviens tout de suite.")], "Offered fresh water"),
 ("lea", "C'est bon, la contraction est passée.",
  "It is fine, the contraction has passed.",
  [(57, "C'est bon, c'est passé.")], "Confirmed pain subsided"),
 ("gabriel", "Bois un peu d'eau, doucement.",
  "Drink a little water, gently.",
  [(53, "juste un verre d'eau.")], "Advised gentle drinking"),
 ("lea", "Merci Gabriel, je me sens déjà mieux.",
  "Thank you Gabriel, I already feel better.",
  [(57, "C'est bon, c'est passé.")], "Expressed physical relief"),
 ("gabriel", "Tu as souvent de telles douleurs?",
  "Do you often have such pains?",
  [(52, "des fois, j'ai des contractions.")], "Inquired about pain frequency"),
 ("lea", "Parfois, quand je marche trop vite.",
  "Sometimes, when I walk too fast.",
  [(52, "des fois, j'ai des contractions.")], "Attributed pain to rushing"),
 ("gabriel", "Tu devrais vraiment ralentir le rythme.",
  "You should really slow down the pace.",
  [(61, "c'est pas une raison pas de te reposer, là.")], "Recommended slowing pace"),
 ("lea", "Impossible avec tous mes rendez-vous importants!",
  "Impossible with all my important meetings!",
  [(42, "fait bien partie des comptes de l'année ?")], "Defended busy agenda"),
 ("gabriel", "La santé de ton bébé passe avant.",
  "The health of your baby comes first.",
  [(61, "pas de te reposer, là.")], "Prioritized baby health"),
 ("lea", "Je le sais bien, mon cher Gabriel.",
  "I know it well, my dear Gabriel.",
  [(57, "C'est bon, c'est passé.")], "Conceded friendly point"),
 ("gabriel", "Promets-moi de te reposer ce soir.",
  "Promise me to rest tonight.",
  [(61, "te reposer, là.")], "Asked for rest promise"),
 ("lea", "D'accord, je vais rentrer plus tôt.",
  "All right, I am going to go home earlier.",
  [(60, "Ouais, moi non plus.")], "Agreed to leave early"),
 ("gabriel", "Je surveillerai ton départ du bureau.",
  "I will keep an eye on your departure from the office.",
  [(61, "te reposer")], "Offered protective oversight"),
 ("lea", "Tu es vraiment un ami formidable!",
  "You are truly a wonderful friend!",
  [(56, "Ouais, super.")], "Celebrated close friendship"),
]

OPENER = "Let's observe how Gabriel expresses protective concern for Andrea's wellbeing."

WALK = [
 (0, None,
  "'Here is your glass of fresh water, Andrea.' A helpful presentative introducing refreshing water."),
 (1, None,
  "'It is fine, the contraction has passed.' A reassuring compound past statement confirming relief."),
 (2, None,
  "'Drink a little water, gently.' A caring imperative advising calm hydration."),
 (3, None,
  "'Thank you Gabriel, I already feel better.' A grateful pronominal expression of physical improvement."),
 (4, None,
  "'Do you often have such pains?' An inverted question inquiring about recurring symptoms."),
 (5, None,
  "'Sometimes, when I walk too fast.' A temporal adverbial clause explaining physical exertion."),
 (6, None,
  "'You should really slow down the pace.' A conditional modal advising professional restraint."),
 (7, None,
  "'Impossible with all my important meetings!' An elliptical exclamation defending a demanding schedule."),
 (8, None,
  "'The health of your baby comes first.' A priority assertion advocating maternal care."),
 (9, None,
  "'I know it well, my dear Gabriel.' A concession acknowledging sincere advice."),
 (10, None,
  "'Promise me to rest tonight.' A protective imperative requesting domestic rest."),
 (11, None,
  "'All right, I am going to go home earlier.' An agreeing near-future commitment to rest."),
 (12, None,
  "'I will keep an eye on your departure from the office.' A friendly future promise of protective oversight."),
 (13, None,
  "'You are truly a wonderful friend!' A warm complimentary exclamation celebrating steadfast friendship."),
]

TRANSITION = "Now let's listen to Gabriel and Andrea again at full speed."

OUTRO = ("Gabriel secures a promise from Andrea to head home early, showing how deep friendship endures beneath agency rivalries. "
         "Andrea recovers her strength, ready to tackle the rest of the day with renewed care.")

CLOSING = ("gabriel", "Prends bien soin de toi, Andréa.")
