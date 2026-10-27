# Authoring module for dix-pour-cent s01e04 scene 30 (cues 775-803).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e04/authoring/scene-30.py --out out/dix-pour-cent/s01e04/scene-30.json

ID = "dix-pour-cent-s01e04-scene-30"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 30
TITLE = "Tout pour l'UNICEF  (All for UNICEF)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Audrey", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 775-803. Feminine 'allée' and 'vue' restored for Audrey in cues 782 and 799; numbers in cues 790 "
               "and 800 ('dix mille', 'vingt mille', 'cent dix-sept') written out in words; 'M.' written out as "
               "'monsieur' in cue 789.")

INTRO = ("While Andréa and Colette are talking on the agency roof, Mathias has brought Audrey Fleurot to a big "
         "charity gala for UNICEF. After the tabloids printed photos of Audrey at the billionaire Kadropov's "
         "birthday party, Mathias has a plan to save her reputation—though it means giving away the very money she "
         "earned to pay her taxes. Listen to the scene in French first, and enjoy how Audrey handles it.")

STORY = [
 ("lea", "Vous êtes sûr que c'est la seule solution?",
  "Are you sure it's the only solution?",
  [(775, "que c'est la seule solution")], "Audrey speaks to Mathias; masculine 'sûr'"),
 ("mathias", "Faites-moi confiance, Audrey. Beyoncé a fait ça après son concert.",
  "Trust me, Audrey. Beyoncé did that after her concert.",
  [(775, "Faites-moi confiance, Audrey"), (777, "Beyoncé a fait ça après son concert")], "'pour Kadhafi' omitted"),
 ("lea", "Je veux vous dire combien je suis ravie d'être avec vous ce soir.",
  "I want to tell you how delighted I am to be with you tonight.",
  [(778, "Je veux vous dire combien je suis ravie d'être avec vous ce soir")], ""),
 ("lea", "Les médias peuvent être cruels.", "The media can be cruel.",
  [(779, "les médias peuvent être cruels")], "shortened from cue 779"),
 ("lea", "Je suis allée à cette soirée uniquement pour les enfants du monde entier.",
  "I went to that party purely for the children of the whole world.",
  [(782, "que je suis"), (782, "à cette soirée"), (783, "Uniquement pour les enfants"), (784, "du monde entier")],
  "feminine 'allée'"),
 ("lea", "J'ai le plaisir de donner toute la somme de monsieur Kadropov à l'UNICEF.",
  "I have the pleasure of giving the whole sum from Mr Kadropov to UNICEF.",
  [(787, "j'ai le plaisir de"), (788, "la somme"), (789, "Kadropov à l'UNICEF")],
  "'remettre la totalité de la somme que m'a versée M. Kadropov' simplified to A1"),
 ("lea", "Dix mille euros. Vingt mille euros, pardon. Vingt mille euros.",
  "Ten thousand euros. Twenty thousand euros, sorry. Twenty thousand euros.",
  [(790, "euros"), (790, "pardon")], "numbers written out in words"),
 ("mathias", "Vous avez oublié de signer.", "You forgot to sign.",
  [(792, "Vous avez oublié de signer")], "the UNICEF organiser's line given to Mathias (2-role limit)"),
 ("lea", "Pardon. Excusez-moi. Merci.", "Sorry. Excuse me. Thank you.",
  [(793, "Pardon. Excusez-moi"), (794, "Merci")], ""),
 ("lea", "Toujours aucune nouvelle de la nounou.", "Still no news from the nanny.",
  [(795, "Toujours aucune nouvelle de la nounou")], ""),
 ("mathias", "Bien, j'ai peut-être un film pour toi.",
  "Well, I may have a film for you.",
  [(797, "Bien, j'ai peut-être un film pour toi")], ""),
 ("lea", "Quoi?", "What?",
  [(798, "Quoi")], ""),
 ("mathias", "Michel Hazanavicius. Il t'a vue avec Kadropov.",
  "Michel Hazanavicius. He saw you with Kadropov.",
  [(799, "Michel Hazanavicius"), (799, "avec Kadropov")], "feminine 'vue'"),
 ("mathias", "Il te veut pour le prochain OSS cent dix-sept.",
  "He wants you for the next OSS one-one-seven.",
  [(800, "Il te veut pour le prochain OSS")], "'117' written out in words"),
 ("lea", "Mathias, c'est super!", "Mathias, that's great!",
  [(800, "Mathias, c'est super")], ""),
 ("mathias", "Tu vas pouvoir payer tes impôts.", "You'll be able to pay your taxes.",
  [(801, "Tu vas pouvoir payer tes impôts")], ""),
 ("lea", "Tu peux leur dire? J'ai peur de l'administration.",
  "Can you tell them? I'm scared of the tax office.",
  [(802, "Tu peux leur dire"), (802, "de l'administration")], "'J'ai une phobie' simplified to 'J'ai peur'"),
 ("mathias", "Je vais chercher du champagne.", "I'll go and get some champagne.",
  [(803, "Je vais chercher du champagne")], ""),
]

OPENER = ("Let's go through it step by step. Backstage before her speech, Audrey is still reluctant to part with "
          "her twenty thousand euros.")

WALK = [
 (0, None,
  "'Are you sure it's the only solution?' Even though Audrey and Mathias are old friends, in this opening exchange "
  "the subtitles use the polite 'vous'."),
 (1, None,
  "'Trust me, Audrey. Beyoncé did that after her concert.' Literally 'make confidence to me'. Mathias reassures "
  "her that giving the fee to charity will turn a scandal into good publicity."),
 (2, None,
  "'I want to tell you how delighted I am to be with you tonight.' Now Audrey is on stage at the microphone. "
  "The adjective for 'delighted' has a feminine ending."),
 (3, None,
  "'The media can be cruel.' The verb 'can' is in the plural form to match 'the media'."),
 (4, None,
  "'I went to that party purely for the children of the whole world.' On stage, Audrey almost slips and says "
  "'for my children', then quickly turns it into 'the children of the whole world'."),
 (5, None,
  "'I have the pleasure of giving the whole sum from Mr Kadropov to UNICEF.' A grand, formal sentence for the "
  "cameras."),
 (6, None,
  "'Ten thousand euros. Twenty thousand euros, sorry. Twenty thousand euros.' She tries to keep half the money, "
  "catches Mathias's eye, and reluctantly says the full twenty thousand."),
 (7, None,
  "'You forgot to sign.' Even when she hands over the giant cheque, she tries one last trick—leaving off her "
  "signature!"),
 (8, None,
  "'Sorry. Excuse me. Thank you.' She signs at last, to big applause."),
 (9, None,
  "'Still no news from the nanny.' Backstage with Mathias, she checks her phone and sighs."),
 (10, None,
  "'Well, I may have a film for you.' Notice how Mathias switches back to the friendly 'tu'."),
 (11, None,
  "'What?' One short question word."),
 (12, None,
  "'Michel Hazanavicius. He saw you with Kadropov.' The famous director of The Artist saw the tabloid photos too—and "
  "thought Audrey looked glamorous."),
 (13, None,
  "'He wants you for the next OSS one-one-seven.' That's the hit French spy-comedy series."),
 (14, None,
  "'Mathias, that's great!' After everything she went through today, a real starring role has landed in her lap."),
 (15, None,
  "'You'll be able to pay your taxes.' Literally 'you are going to be able to pay your taxes'."),
 (16, None,
  "'Can you tell them? I'm scared of the tax office.' Literally 'I have fear of the administration', a playful "
  "nod to a real French political scandal."),
 (17, None,
  "'I'll go and get some champagne.' Literally 'I am going to fetch some champagne'."),
]

TRANSITION = "Now let's hear the whole charity gala scene again."

OUTRO = ("Audrey has saved her reputation and won a big comedy role to pay off her taxes. Next we head back to ASK, "
         "where the news of Mathias's departure is about to have a surprising effect on the German buyer.")
CLOSING = ("lea", "Mathias, c'est super!")
