# Authoring module for dix-pour-cent s02e01 scene 10 (cues 270-284).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-10.py --out out/dix-pour-cent/s02e01/scene-10.json

ID = "dix-pour-cent-s02e01-scene-10"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 10
TITLE = "Ramzy boycotte la promotion  (Ramzy Boycotts the Promotion)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "ramzy": "marcel"}
LABELS = {"lea": "Camille", "mathias": "Mathias", "ramzy": "Ramzy"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 270-284. Inside the ASK elevator, Mathias desperately tries to persuade Ramzy Bedia "
               "to participate in promotional interviews with his ex-partner Virginie. "
               "Mathias attempts philosophical arguments about fidelity, but Ramzy angrily storms out on the first floor. "
               "Adapted for A1 French.")

INTRO = ("Inside the elevator at ASK, Mathias rides down with an enraged Ramzy Bedia. "
         "Their romantic comedy is opening in theatres, but Ramzy flatly refuses to appear next to Virginie Efira "
         "for promotional interviews or press photos. Mathias tries every philosophical trick to change his mind. "
         "Let's listen to the scene in French first.")

STORY = [
 ("ramzy", "Je ne veux pas la voir.",
  "I do not want to see her.",
  [(270, "Je ne veux pas la voir.")], ""),
 ("ramzy", "Les interviews, les photos pour le film, c'est hors de question.",
  "Interviews, photos for the film, it is out of the question.",
  [(271, "Les interviews, les photos promo pour le film... hors de question.")], ""),
 ("mathias", "Sans promotion, le film va être un échec.",
  "Without promotion, the film is going to be a failure.",
  [(272, "Sans promotion, le film va faire un flop.")], "Simplified 'faire un flop' to 'être un échec'"),
 ("mathias", "C'est mauvais pour tout le monde.",
  "It is bad for everyone.",
  [(272, "C'est mauvais pour tout le monde.")], ""),
 ("ramzy", "Ce qu'elle a fait est impardonnable.",
  "What she did is unforgivable.",
  [(273, "Désolé, ce qu'elle a fait est impardonnable.")], ""),
 ("mathias", "Ça dépend de ton école de pensée.",
  "That depends on your school of thought.",
  [(274, "Ça dépend de votre école."), (276, "École de pensée")], ""),
 ("ramzy", "Quelle école de pensée?",
  "What school of thought?",
  [(275, "Quelle école ?")], ""),
 ("mathias", "Ton corps t'appartient. On ne possède pas quelqu'un.",
  "Your body belongs to you. You do not own someone.",
  [(277, "Genre on ne possède pas quelqu'un, ton corps t'appartient.")], ""),
 ("mathias", "L'infidélité n'existe pas vraiment.",
  "Infidelity does not really exist.",
  [(278, "L'infidélité n'existe pas. Ni la fidélité.")], ""),
 ("mathias", "Tu pourrais promouvoir la paix et le progrès!",
  "You could promote peace and progress!",
  [(280, "Tu pourrais promouvoir la paix, le progrès")], ""),
 ("ramzy", "Non! Pas du tout!",
  "No! Not at all!",
  [(281, "Non ?")], "Added strong refusal"),
 ("lea", "Bonjour, Ramzy! Bonne journée!",
  "Hello, Ramzy! Have a nice day!",
  [(283, "Bonne journée, Ramzy !")], ""),
 ("ramzy", "Au revoir.",
  "Goodbye.",
  [], "Short parting line"),
 ("mathias", "Il refuse tout, Camille.",
  "He refuses everything, Camille.",
  [], "Mathias reacts to Camille"),
 ("lea", "Il ne veut vraiment pas faire la promotion?",
  "Does he really not want to do the promotion?",
  [], "Camille questions Mathias"),
 ("mathias", "Rien du tout. C'est une catastrophe.",
  "Nothing at all. It is a disaster.",
  [], "Mathias conclusion"),
]

OPENER = "Let's observe Mathias trying to save a movie campaign with high-minded philosophy."

WALK = [
 (0, None,
  "'I do not want to see her.' Ramzy sets an absolute boundary with a direct object pronoun."),
 (1, None,
  "'Interviews, photos for the film, it is out of the question.' A useful everyday idiom for an absolute refusal."),
 (2, None,
  "'Without promotion, the film is going to be a failure.' Mathias warns about the financial stakes with near future."),
 (3, None,
  "'It is bad for everyone.' The adjective for bad followed by a preposition."),
 (4, None,
  "'What she did is unforgivable.' A relative clause followed by a strong negative adjective."),
 (5, None,
  "'That depends on your school of thought.' Mathias switches to philosophical persuasion."),
 (6, None,
  "'What school of thought?' Ramzy asks sceptically with an interrogative determiner."),
 (7, None,
  "'Your body belongs to you. You do not own someone.' Two core principles of modern autonomy."),
 (8, None,
  "'Infidelity does not really exist.' A provocative statement using regular negation."),
 (9, None,
  "'You could promote peace and progress!' Mathias reaches for lofty ideals using the conditional form."),
 (10, None,
  "'No! Not at all!' Ramzy rejects the argument completely."),
 (11, None,
  "'Hello, Ramzy! Have a nice day!' Camille cheerfully greets the client as the elevator doors open."),
 (12, None,
  "'Goodbye.' Ramzy mutters a curt farewell as he storms off into the corridor."),
 (13, None,
  "'He refuses everything, Camille.' Mathias sighs with deep frustration."),
 (14, None,
  "'Does he really not want to do the promotion?' Camille asks for confirmation."),
 (15, None,
  "'Nothing at all. It is a disaster.' Mathias sums up the hopeless situation."),
]

TRANSITION = "Let's listen to this hilarious elevator exchange one more time."

OUTRO = ("Mathias's philosophical speech did not convince Ramzy at all. "
         "In the next scene, we will head over to Andrea's office as she plans an unwanted family trip.")
CLOSING = ("mathias", "On trouvera une autre idée.")
