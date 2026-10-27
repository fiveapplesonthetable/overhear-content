# Authoring module for dix-pour-cent s03e06 scene 02 (cues 128-230).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e06/authoring/scene-02.py --out out/dix-pour-cent/s03e06/scene-02.json

ID = "dix-pour-cent-s03e06-scene-02"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 2
TITLE = "Panique et trahisons  (Panic and Betrayals)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "noemie": "emilie"}
LABELS = {"lea": "Andréa", "mathias": "Mathias", "noemie": "Noémie"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 128-230. Mathias prepares the party while Noemie urges him forward. Andrea and the team contemplate quitting. Adapted for A1 French.")

INTRO = ("In the bustling hallways of ASK, Mathias takes charge of organizing the agency's thirtieth anniversary celebration. "
         "While assistant Noemie helps him manage the practical details, Andrea and Gabriel struggle with the reality of his triumph. "
         "Disgusted by the atmosphere of mutual suspicion, the agents wonder if walking away is their only remaining option. "
         "Let's listen to the scene in French first.")

STORY = [
 ("mathias", "Nous servons uniquement du champagne ce soir.",
  "We are serving only champagne tonight.",
  [(147, "On avait dit champagne uniquement")], "Insisted on luxury drinks"),
 ("mathias", "Veuillez annuler ce bar à cocktails.",
  "Please cancel this cocktail bar.",
  [(151, "m'annuler le bar à cocktails")], "Ordered event change"),
 ("noemie", "Tout le monde connaît l'historique d'une photocopieuse!",
  "Everyone knows the log of a photocopier!",
  [(155, "qu'une photocopieuse, c'est un historique")], "Pointed out obvious mistake"),
 ("mathias", "Ce qui est fait est fait.",
  "What is done is done.",
  [(160, "ce qui est fait est fait")], "Dismissed past blunders"),
 ("noemie", "Vous êtes maintenant le grand patron.",
  "You are now the big boss.",
  [(163, "Vous êtes le patron")], "Acknowledged new authority"),
 ("noemie", "Nous devons regarder vers l'avenir.",
  "We must look toward the future.",
  [(164, "on se tourne vers l'avenir")], "Urged forward focus"),
 ("lea", "Je ne peux plus travailler avec lui.",
  "I can no longer work with him.",
  [(173, "je peux pas rester")], "Voiced moral refusal"),
 ("lea", "Nous devrions tous démissionner ensemble.",
  "We should all resign together.",
  [(212, "on démissionne")], "Proposed collective resignation"),
 ("noemie", "Mathias se retrouverait complètement seul.",
  "Mathias would find himself completely alone.",
  [(212, "on démissionne")], "Contemplated dramatic fallout"),
 ("lea", "C'est une trahison à tous les étages.",
  "It is betrayal on every floor.",
  [(228, "c'est la trahison à tous les étages")], "Denounced generalized disloyalty"),
 ("noemie", "Nos petites erreurs semblent insignifiantes désormais.",
  "Our little mistakes seem insignificant now.",
  [(227, "à côté de vos combines")], "Downplayed minor infractions"),
 ("lea", "Cette ambiance détruit toute notre équipe.",
  "This atmosphere is destroying our whole team.",
  [(228, "c'est la trahison à tous les étages")], "Lamented broken trust"),
 ("noemie", "Pourtant, Mathias adore cette lutte acharnée.",
  "Yet, Mathias loves this fierce struggle.",
  [(230, "j'ai l'impression que t'adores ça")], "Observed boss's appetite for conflict"),
 ("lea", "Je refuse de céder sans combattre.",
  "I refuse to give up without fighting.",
  [(173, "je peux pas rester")], "Resolved to mount resistance"),
]

OPENER = "Let's observe as Mathias plans the party while Andrea denounces the toxic rivalry."

WALK = [
 (0, None,
  "'We are serving only champagne tonight.' A firm directive demanding prestigious catering for the anniversary."),
 (1, None,
  "'Please cancel this cocktail bar.' An authoritative order dismissing casual party arrangements."),
 (2, None,
  "'Everyone knows the log of a photocopier!' An exasperated remark highlighting a foolish operational oversight."),
 (3, None,
  "'What is done is done.' A pragmatic dismissal refusing to dwell on past errors."),
 (4, None,
  "'You are now the big boss.' An encouraging statement affirming his newly won executive authority."),
 (5, None,
  "'We must look toward the future.' A positive exhortation focusing on upcoming corporate challenges."),
 (6, None,
  "'I can no longer work with him.' A sharp rejection expressing total loss of confidence in Mathias."),
 (7, None,
  "'We should all resign together.' A bold proposal suggesting collective resignation in protest."),
 (8, None,
  "'Mathias would find himself completely alone.' A thoughtful evaluation considering the consequence of a mass walkout."),
 (9, None,
  "'It is betrayal on every floor.' A bitter assessment describing pervasive intrigue within the agency."),
 (10, None,
  "'Our little mistakes seem insignificant now.' A candid comparison contrasting minor blunders with major power struggles."),
 (11, None,
  "'This atmosphere is destroying our whole team.' A regretful complaint noting the erosion of mutual trust."),
 (12, None,
  "'Yet, Mathias loves this fierce struggle.' An astute insight into the rival's relentless competitive drive."),
 (13, None,
  "'I refuse to give up without fighting.' A determined declaration resolving to fight back against the takeover."),
]

TRANSITION = "Now let's listen to Mathias and the agents again at full speed."

OUTRO = ("Tensions inside the agency reach an all-time high as preparations for the anniversary party continue. "
         "Rather than quietly conceding defeat to Mathias, Andrea resolves to find a counter-strategy before the night is over.")

CLOSING = ("lea", "La résistance commence maintenant.")
