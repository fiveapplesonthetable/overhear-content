# Authoring module for dix-pour-cent s04e04 scene 14 (cues 927-949).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e04/authoring/scene-14.py --out overhear-content/out/dix-pour-cent/s04e04/scene-14.json

ID = "dix-pour-cent-s04e04-scene-14"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 14
TITLE = "Une étoile montante  (A Rising Star)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo"}
LABELS = {"lea": "Véro", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 927-949. After wrapping an intense scene on set, Hervé is showered with praise "
    "for his deeply moving performance. In his dressing room, makeup artist Véro secretly "
    "reveals that the director is considering him for a substantial role in her next film."
)

INTRO = (
    "In his dressing room after an emotional day of filming, Hervé chats with makeup artist Vero. "
    "Impressed by his natural acting talent, Vero shares an exciting rumor she overheard from the film director. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Hervé, je suis très occupée aujourd'hui.",
     "Hervé, I am very busy today.",
     [(939, "Hervé"), (940, "Je suis débordée")], "Véro enters Hervé's dressing room"),
    ("lea", "Tout est prêt dans ta loge.",
     "Everything is ready in your dressing room.",
     [(941, "Tout est dans ta loge")], "Véro points to the makeup supplies"),
    ("herve", "Bien sûr Véro, pas de souci.",
     "Of course Véro, no problem.",
     [(941, "Bien sûr, Véro")], "Hervé happily obliges"),
    ("lea", "Tu étais encore extraordinaire sur le plateau!",
     "You were amazing again on the set!",
     [(940, "sur le plateau"), (942, "extraordinaire aujourd'hui")], "Véro praises his acting"),
    ("herve", "Merci, c'était vraiment très intense.",
     "Thank you, it was truly very intense.",
     [(943, "C'était très intense")], "Hervé reflects on the shoot"),
    ("herve", "Mais le tournage passe tellement vite.",
     "But the shoot goes by so fast.",
     [(943, "ça passe tellement vite")], "Hervé wishes it lasted longer"),
    ("herve", "Je veux encore profiter de ça.",
     "I still want to enjoy this.",
     [(944, "le temps d'en profiter")], "Hervé savors the experience"),
    ("lea", "Écoute, j'ai un grand secret.",
     "Listen, I have a big secret.",
     [(945, "Je devrais pas te dire ça")], "Véro leans in with news"),
    ("lea", "Ta carrière d'acteur continue peut-être!",
     "Your acting career continues perhaps!",
     [(945, "ta carrière"), (945, "peut-être pas terminée")], "Véro hints at future work"),
    ("herve", "Quoi? Qu'est-ce que tu dis?",
     "What? What are you saying?",
     [(946, "Quoi")], "Hervé is astonished"),
    ("lea", "Valérie pense à toi maintenant.",
     "Valerie is thinking of you now.",
     [(947, "elle pensait à toi")], "Véro mentions the director"),
    ("lea", "Elle prépare son prochain grand film.",
     "She is preparing her next big film.",
     [(947, "son prochain film")], "Véro explains the project"),
    ("lea", "Elle veut te donner un vrai rôle!",
     "She wants to give you a real role!",
     [(948, "un petit rôle")], "Véro reveals it is a substantial role"),
    ("herve", "C'est le plus beau jour!",
     "It is the most beautiful day!",
     [(949, "Mon étoile montante")], "Hervé is overjoyed"),
]

WALK = [
    (0, None,
     "'Hervé, I am very busy today.' Vero pops into the room while juggling several tasks on set. "
     "The feminine adjective 'occupee' means busy."),
    (1, None,
     "'Everything is ready in your dressing room.' She lets him know that the makeup remover is laid out. "
     "In theater and film, 'loge' designates a performer's dressing room."),
    (2, None,
     "'Of course Vero, no problem.' Hervé is happy to remove his own makeup without fuss. "
     "The casual phrase 'pas de souci' means no worries or no problem."),
    (3, None,
     "'You were amazing again on the set!' Vero compliments his moving performance in front of the crew. "
     "The noun 'plateau' refers to a film set."),
    (4, None,
     "'Thank you, it was truly very intense.' Hervé is still emotional from acting out the dramatic scene. "
     "The adjective 'intense' is identical in French and English."),
    (5, None,
     "'But the shoot goes by so fast.' Hervé wishes his time as an actor did not end so quickly. "
     "The masculine noun 'tournage' means film shoot."),
    (6, None,
     "'I still want to enjoy this.' He wants to savor every moment on set before returning to agency desk work. "
     "The verb 'profiter de' means to enjoy or make the most of."),
    (7, None,
     "'Listen, I have a big secret.' Vero lowers her voice to share confidential gossip from the crew. "
     "The imperative 'ecoute' calls for close attention."),
    (8, None,
     "'Your acting career continues perhaps!' Vero hints that this small part might lead to more roles. "
     "The adverb 'peut-etre' means maybe or perhaps."),
    (9, None,
     "'What? What are you saying?' Hervé widens his eyes in disbelief and excitement. "
     "The verb 'dis' comes from 'dire', meaning to say."),
    (10, None,
     "'Valerie is thinking of you now.' Vero reveals that the film director was praising Hervé earlier. "
     "The construction 'penser a' takes a stressed pronoun like 'toi'."),
    (11, None,
     "'She is preparing her next big film.' The director is already planning her upcoming feature project. "
     "The adjective 'prochain' means next."),
    (12, None,
     "'She wants to give you a real role!' Vero adds that the director has a major part in mind for him. "
     "The adjective 'vrai' placed before a noun means real or genuine."),
    (13, None,
     "'It is the most beautiful day!' Hervé beams with joy at the prospect of becoming a real movie star. "
     "The superlative 'le plus beau' means the most beautiful or best."),
]

OUTRO = (
    "Thrilled by Vero's secret news, Hervé gazes into the dressing room mirror like a true cinema star. "
    "His brief adventure on a movie set may be the beginning of an unexpected new calling. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Bravo, ma nouvelle grande étoile!")
