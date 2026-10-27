# Authoring module for dix-pour-cent s03e05 scene 28 (cues 1058-1091).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e05/authoring/scene-28.py --out overhear-content/out/dix-pour-cent/s03e05/scene-28.json

ID = "dix-pour-cent-s03e05-scene-28"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 28
TITLE = "La trahison révélée  (The Betrayal Revealed)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "marcel"}
LABELS = {"lea": "Mathias", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 1058-1091. A devastated Hicham bursts into Mathias's office after hearing the voicemail "
               "about Andrea and Gabriel's rogue agency. Mathias seizes the moment to offer buying him out.")

INTRO = ("In Mathias's office at ASK, an incandescent Hicham storms in waving his phone in shock. "
         "Having heard the secret voicemail, Hicham is shattered by Andrea and Gabriel's betrayal, while Mathias tactfully positions himself. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("hicham", "Qu'est-ce que tu fais, là?",
  "What are you doing here?",
  [(1059, "qu'est-ce que tu fais, là")], "Demanding answers"),
 ("lea", "Mais calme-toi, s'il te plaît.",
  "Calm down, please.",
  [(1060, "calme-toi")], "Urging calm"),
 ("hicham", "C'est quoi ce terrible bordel?",
  "What kind of terrible mess is this?",
  [(1065, "ce bordel")], "Expressing outrage"),
 ("hicham", "Andréa veut partir avec Gabriel?",
  "Andrea wants to leave with Gabriel?",
  [(1066, "Elle veut partir"), (1067, "Avec Gabriel")], "Confirming defectors"),
 ("hicham", "Monter une autre agence concurrente?",
  "Start another competing agency?",
  [(1068, "monter une autre agence")], "Expressing disbelief"),
 ("hicham", "Ce n'est pas possible!",
  "This cannot be possible!",
  [(1070, "pas possible")], "Refusing to believe"),
 ("hicham", "Je suis complètement écœuré aujourd'hui.",
  "I am completely disgusted today.",
  [(1071, "Je suis écoeuré")], "Confessing revulsion"),
 ("lea", "Je te comprends parfaitement, Hicham.",
  "I understand you perfectly, Hicham.",
  [(1072, "Je comprends")], "Showing sympathy"),
 ("lea", "Ma proposition tient toujours, sache-le.",
  "My offer still stands, know that.",
  [(1080, "proposition que je t'ai faite"), (1081, "ça tient toujours")], "Bringing back offer"),
 ("hicham", "Tu veux acheter mes parts?",
  "You want to buy out my shares?",
  [(1083, "Acheter mes parts")], "Inquiring about buyout"),
 ("lea", "Je veux te libérer enfin.",
  "I want to free you at last.",
  [(1084, "Te libérer")], "Framing as liberation"),
 ("lea", "Tes associés te trahissent lâchement.",
  "Your partners betray you cowardly.",
  [(1087, "associés qui te trahissent")], "Driving wedge"),
 ("hicham", "Et avec toi, ce sera différent?",
  "And with you, it will be different?",
  [(1089, "ce serait différent")], "Questioning trustworthiness"),
 ("lea", "ASK, c'est mon agence.",
  "ASK is my agency.",
  [(1090, "Aiska, c'est chez moi")], "Asserting true home"),
]

WALK = [
 (0, None,
  "'What are you doing here?' Hicham storms into Mathias's office demanding answers. "
  "The inverted question expresses agitated disbelief."),
 (1, None,
  "'Calm down, please.' Mathias tries to soothe his furious partner. "
  "The imperative 'calme-toi' urges composure."),
 (2, None,
  "'What kind of terrible mess is this?' Hicham demands an explanation of the chaos. "
  "The colloquial French noun 'bordel' describes complete disarray."),
 (3, None,
  "'Andrea wants to leave with Gabriel?' Hicham confirms the identities of the defecting agents. "
  "The verb 'partir' means to leave or depart."),
 (4, None,
  "'Start another competing agency?' Hicham cannot believe they plan to set up a rival company. "
  "The verb 'monter' here means to found or set up."),
 (5, None,
  "'This cannot be possible!' Hicham reacts with sheer disbelief to the revelation. "
  "The adjective 'possible' describes potential reality."),
 (6, None,
  "'I am completely disgusted today.' Hicham confesses his deep personal revulsion at their disloyalty. "
  "The adjective 'ecoeure' expresses profound disgust."),
 (7, None,
  "'I understand you perfectly, Hicham.' Mathias adopts a sympathetic tone to gain his confidence. "
  "The adverb 'parfaitement' means thoroughly or completely."),
 (8, None,
  "'My offer still stands, know that.' Mathias brings back his buyout proposal. "
  "The verbal idiom 'tenir toujours' means to remain valid."),
 (9, None,
  "'You want to buy out my shares?' Hicham clarifies Mathias's intentions. "
  "The noun 'parts' denotes company ownership shares."),
 (10, None,
  "'I want to free you at last.' Mathias frames the buyout as liberating Hicham from unwanted stress. "
  "The verb 'liberer' means to release or free."),
 (11, None,
  "'Your partners betray you cowardly.' Mathias drives a wedge between Hicham and his associates. "
  "The adverb 'lachement' means cowardly or deceitfully."),
 (12, None,
  "'And with you, it will be different?' Hicham questions whether Mathias is truly trustworthy. "
  "The future tense 'ce sera' looks ahead to prospective ownership."),
 (13, None,
  "'ASK is my agency.' Mathias asserts his deep emotional and historical bond to ASK. "
  "The possessive determiner 'mon' claims rightful leadership."),
]

OUTRO = ("Mathias recognizes that Hicham's heartbreak creates the perfect opening to regain command of ASK. "
         "The agency's delicate balance of power has completely shattered in an instant. "
         "Now, let's review the scene one last time.")

CLOSING = ("lea", "ASK, c'est mon agence.")
