# Authoring module for dix-pour-cent s04e01 scene 14 (cues 720-731).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e01/authoring/scene-14.py --out overhear-content/out/dix-pour-cent/s04e01/scene-14.json

ID = "dix-pour-cent-s04e01-scene-14"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 14
TITLE = "Le déménagement de bureau  (The Office Move)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 720-731. At ASK, Andréa catches Gabriel moving his boxes "
               "into the large corner office.")

INTRO = ("Arriving at the agency, Andrea finds Gabriel happily installing his personal belongings in the spacious office. "
         "Surprised by his boldness, she reacts with quick wit and playfully reorganizes the agency hierarchy. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("gabriel", "Excusez-moi, je dépose ce carton ici.",
  "Excuse me, I set this box down here.",
  [(720, "Excusez-moi")], "Placing box"),
 ("lea", "Gabriel! Mais qu'est-ce que tu fais?",
  "Gabriel! What are you doing?",
  [(722, "qu'est-ce que tu fais")], "Confronting colleague"),
 ("gabriel", "Tu vois bien, j'emménage aujourd'hui!",
  "You see well, I am moving in today!",
  [(723, "j'emménage")], "Declaring move"),
 ("lea", "C'est mon bureau officiel, Gabriel!",
  "This is my official office, Gabriel!",
  [(724, "Voilà")], "Reclaiming desk"),
 ("gabriel", "De toute façon, tu n'es jamais là.",
  "In any case, you are never here.",
  [(725, "tu n'es jamais là")], "Arguing absence"),
 ("lea", "Je dirige l'agence tout entière!",
  "I run the entire agency!",
  [(725, "tu n'es jamais là")], "Defending authority"),
 ("gabriel", "Tu appelles qui avec ce téléphone?",
  "Who are you calling with that phone?",
  [(726, "Tu appelles qui")], "Noticing call"),
 ("lea", "J'appelle le service juridique d'ASK.",
  "I am calling ASK legal department.",
  [(727, "Le service juridique")], "Threatening sanctions"),
 ("gabriel", "Tu veux vraiment me faire expulser?",
  "Do you really want to have me expelled?",
  [(727, "Le service juridique")], "Worrying about legal"),
 ("lea", "J'ai une bonne nouvelle pour toi.",
  "I have good news for you.",
  [(728, "J'ai une bonne nouvelle")], "Shifting tone"),
 ("gabriel", "Tu me donnes une belle promotion?",
  "Are you giving me a nice promotion?",
  [(729, "Je te promeus")], "Hoping for advancement"),
 ("lea", "Oui, je te promeus tout de suite!",
  "Yes, I promote you right away!",
  [(729, "Je te promeus")], "Confirming promotion"),
 ("gabriel", "Une vraie augmentation de salaire enfin?",
  "A real salary raise at last?",
  [(731, "D'étage")], "Asking about raise"),
 ("lea", "Non, pas de salaire, un changement d'étage!",
  "No, not salary, a change of floor!",
  [(731, "D'étage")], "Delivering punchline"),
]

WALK = [
 (0, None,
  "'Excuse me, I set this box down here.' Gabriel enters carrying office boxes. "
  "The verb 'deposer' means to set down or deposit."),
 (1, None,
  "'Gabriel! What are you doing?' Andrea catches him in the act of unpacking. "
  "The familiar interrogative 'qu'est-ce que tu fais' expresses exasperation."),
 (2, None,
  "'You see well, I am moving in today!' Gabriel announces his takeover proudly. "
  "The verb 'emmenager' means to move into a new space."),
 (3, None,
  "'This is my official office, Gabriel!' Andrea reclaims her executive domain. "
  "The adjective 'officiel' indicates authorized status."),
 (4, None,
  "'In any case, you are never here.' Gabriel points out Andrea's hectic schedule. "
  "The locution 'de toute facon' means anyway or in any case."),
 (5, None,
  "'I run the entire agency!' Andrea asserts her role as director of ASK. "
  "The feminine adjective 'entiere' emphasizes totality."),
 (6, None,
  "'Who are you calling with that phone?' Gabriel observes Andrea dialing a number. "
  "The interrogative 'qui' asks for the identity of the person called."),
 (7, None,
  "'I am calling ASK legal department.' Andrea pretends to initiate formal proceedings. "
  "The adjective 'juridique' relates to law and contracts."),
 (8, None,
  "'Do you really want to have me expelled?' Gabriel questions her drastic reaction. "
  "The causative construction 'faire expulser' indicates causing someone to be evicted."),
 (9, None,
  "'I have good news for you.' Andrea changes tactics with an ironic twist. "
  "The noun phrase 'bonne nouvelle' creates false anticipation."),
 (10, None,
  "'Are you giving me a nice promotion?' Gabriel hopes for professional advancement. "
  "The noun 'promotion' refers to career elevation."),
 (11, None,
  "'Yes, I promote you right away!' Andrea humorously confirms his promotion. "
  "The verb 'promouvoir' is conjugated as 'promeus' in the first person."),
 (12, None,
  "'A real salary raise at last?' Gabriel dreams of financial reward. "
  "The noun 'augmentation' signifies a pay increase."),
 (13, None,
  "'No, not salary, a change of floor!' Andrea delivers her sharp witty comeback. "
  "The noun 'etage' refers to a building floor level."),
]

OUTRO = ("Andrea skillfully reasserts her executive authority over Gabriel with trademark sharp humor. "
         "Their lively workplace banter shows that friendship and rivalries remain vibrant at ASK. "
         "Now, let's review the scene one last time.")

CLOSING = ("lea", "Non, pas de salaire, un changement d'étage!")
