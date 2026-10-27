# Authoring module for dix-pour-cent s02e06 scene 02 (cues 57-77).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-02.py --out out/dix-pour-cent/s02e06/scene-02.json

ID = "dix-pour-cent-s02e06-scene-02"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 2
TITLE = "Tenir la boutique  (Holding the Fort)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo", "herve": "marcel"}
LABELS = {"lea": "Arlette", "hicham": "Hicham", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 57-77. Arlette comforts an actress missing Cannes, while Hicham reminds Hervé "
               "of the importance of holding down the Paris office during the festival. Adapted for A1 French.")

INTRO = ("At the ASK offices in Paris, Arlette finishes a comforting phone call with an actress whose film missed the Cannes festival. "
         "Meanwhile, agency director Hicham organizes travel logistics and gives instructions to assistant Herve, who must stay behind. "
         "Let's listen to their conversation in French first.")

STORY = [
 ("lea", "Ne pleure pas pour Cannes, Fabienne.",
  "Do not cry over Cannes, Fabienne.",
  [(59, "Non, ne pleure pas, Fabienne.")], "Comforted upset caller"),
 ("lea", "Le festival d'Angoulême est très bien aussi.",
  "The Angouleme festival is very good too.",
  [(60, "mais le festival d'Angoulême, c'est bien aussi.")], "Suggested alternative festival"),
 ("hicham", "Vous êtes prêts pour le départ?",
  "Are you ready for the departure?",
  [(68, "Prêts, les enfants ?")], "Inquired about festival departure"),
 ("herve", "Moi, je reste à l'agence.",
  "Me, I am staying at the agency.",
  [(70, "l'autre reste ici.")], "Stated remaining in Paris"),
 ("hicham", "Le patron et Andréa vont à Cannes.",
  "The boss and Andrea are going to Cannes.",
  [(69, "Le petit va à Cannes,")], "Listed staff members traveling"),
 ("herve", "Mon karma est mauvais ce mois-ci.",
  "My karma is bad this month.",
  [(71, "Je sentais que mon karma était complètement de travers ce mois-ci.")], "Expressed personal disappointment"),
 ("lea", "Tu vas être maître à bord ici.",
  "You are going to be in charge here.",
  [(73, "Tu seras totalement maître à bord ici pendant deux semaines.")], "Encouraged leadership role"),
 ("herve", "L'année dernière, j'ai eu un seul appel.",
  "Last year, I had a single phone call.",
  [(75, "L'année dernière tu as eu un seul appel, c'était la dératisation.")], "Recalled past quiet summer"),
 ("hicham", "Il faut bien quelqu'un pour garder l'agence.",
  "Someone is really needed to guard the agency.",
  [(76, "Il faut bien que quelqu'un tienne la boutique.")], "Underlined organizational necessity"),
 ("lea", "Tenir la boutique est très important, Hervé.",
  "Holding the fort is very important, Herve.",
  [(76, "Il faut bien que quelqu'un tienne la boutique.")], "Validated assistant responsibility"),
 ("herve", "Deux semaines tout seul à Paris, c'est long.",
  "Two weeks all alone in Paris, that is long.",
  [(73, "pendant deux semaines.")], "Remarked on empty fortnight"),
 ("hicham", "Tu auras le calme pour bien travailler.",
  "You will have peace and quiet to work well.",
  [(73, "Tu seras totalement maître à bord ici")], "Framed calm as productive asset"),
 ("lea", "Nous te faisons confiance, mon cher Hervé.",
  "We trust you, my dear Herve.",
  [(73, "maître à bord ici")], "Affirmed agency trust"),
 ("herve", "D'accord, je vais surveiller les bureaux.",
  "All right, I am going to watch over the offices.",
  [(76, "tienne la boutique.")], "Accepted responsibility"),
]

OPENER = "Let's see how Arlette and Hicham motivate Herve to manage the Paris office."

WALK = [
 (0, None,
  "'Do not cry over Cannes, Fabienne.' A negative imperative comforting an upset artist."),
 (1, None,
  "'The Angouleme festival is very good too.' A consoling alternative pointing to another prestigious film event."),
 (2, None,
  "'Are you ready for the departure?' An inverted plural question reviewing festival preparations."),
 (3, None,
  "'Me, I am staying at the agency.' A stressed personal pronoun highlighting duty in Paris."),
 (4, None,
  "'The boss and Andrea are going to Cannes.' A compound subject noting the executive travel roster."),
 (5, None,
  "'My karma is bad this month.' A colloquial idiom expressing temporary professional misfortune."),
 (6, None,
  "'You are going to be in charge here.' A nautical metaphor signifying leadership during absence."),
 (7, None,
  "'Last year, I had a single phone call.' A past temporal memory recalling previous office solitude."),
 (8, None,
  "'Someone is really needed to guard the agency.' An impersonal necessity structure emphasizing essential presence."),
 (9, None,
  "'Holding the fort is very important, Herve.' A professional idiom encouraging responsible oversight."),
 (10, None,
  "'Two weeks all alone in Paris, that is long.' A duration assessment acknowledging quiet summer weeks."),
 (11, None,
  "'You will have peace and quiet to work well.' A reassuring future tense predicting calm productivity."),
 (12, None,
  "'We trust you, my dear Herve.' A sincere expression of team confidence and affection."),
 (13, None,
  "'All right, I am going to watch over the offices.' An accepting agreement undertaking office management."),
]

TRANSITION = "Now let's listen to Arlette, Hicham, and Herve again at full speed."

OUTRO = ("Herve reluctantly accepts his assignment to watch over the ASK agency while his colleagues travel south to Cannes. "
         "Arlette and Hicham ensure the office remains staffed and ready for incoming talent inquiries.")

CLOSING = ("herve", "Bon voyage à Cannes, patron.")
