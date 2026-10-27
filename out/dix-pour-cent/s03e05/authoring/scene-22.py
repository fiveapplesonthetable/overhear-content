# Authoring module for dix-pour-cent s03e05 scene 22 (cues 831-935).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-22.py --out out/dix-pour-cent/s03e05/scene-22.json

ID = "dix-pour-cent-s03e05-scene-22"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 22
TITLE = "L'accord de Béatrice  (Béatrice's Agreement)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "pascal": "theo"}
LABELS = {"lea": "Béatrice", "pascal": "Pascal"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 831-935. On the film set, Béatrice Dalle confronts director Pascal over the shutdown caused by her refusal to shoot a nude scene. "
    "Pascal admits he panicked out of creative anxiety, and proposes an alternative where the character gently bites her ear, which Béatrice adores."
)

INTRO = (
    "On the film set, Beatrice Dalle confronts director Pascal over the shutdown caused by her refusal to shoot a nude scene. "
    "Pascal admits he panicked out of creative anxiety, and proposes an alternative where the character gently bites her ear, which Beatrice adores. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("pascal", "Ce blocage me rend complètement fou!",
     "This stalemate makes me completely crazy!",
     [(835, "rend dingue")], "Pascal vents his extreme frustration"),
    ("lea", "Je refuse cette scène de nudité.",
     "I refuse this nude scene.",
     [(853, "scène nue")], "Beatrice stands firmly by her boundary"),
    ("pascal", "J'ai passé six ans à écrire.",
     "I spent six years writing.",
     [(837, "six ans à l'écrire")], "Pascal emphasizes his immense investment"),
    ("lea", "J'ai mis trente ans à refuser!",
     "It took me thirty years to refuse!",
     [(864, "savoir dire non")], "Beatrice cites her hard-won autonomy"),
    ("lea", "Quand je dis non, c'est non!",
     "When I say no, it means no!",
     [(866, "quand je dis non c'est non")], "Beatrice establishes absolute boundaries"),
    ("pascal", "La vérité, c'est que j'ai paniqué.",
     "The truth is that I panicked.",
     [(870, "j'ai flippé")], "Pascal confesses his creative insecurity"),
    ("pascal", "Je ne savais pas comment tourner.",
     "I did not know how to film.",
     [(868, "comment la faire")], "Pascal admits his lack of inspiration"),
    ("lea", "Alors tu cherches quoi au juste?",
     "So what are you looking for exactly?",
     [(873, "cherches quoi")], "Beatrice inquires about the scene's core"),
    ("pascal", "Je cherche un geste très fort.",
     "I am looking for a very powerful gesture.",
     [(874, "truc fort")], "Pascal describes his artistic intent"),
    ("pascal", "Le personnage veut garder votre souvenir.",
     "The character wants to keep your memory.",
     [(875, "garder quelque chose")], "Pascal explains the emotional motivation"),
    ("pascal", "Il mange un petit bout d'oreille!",
     "He eats a tiny piece of ear!",
     [(883, "tout petit bout")], "Pascal proposes a shocking, poetic idea"),
    ("lea", "Il me mange l'oreille, vraiment?",
     "He eats my ear, really?",
     [(885, "bouffe l'oreille")], "Beatrice seeks clarification on the proposal"),
    ("pascal", "Oui, pour emporter une part de toi.",
     "Yes, to take away a part of you.",
     [(884, "emporter avec lui")], "Pascal explains the romantic symbolism"),
    ("lea", "C'est une idée géniale, j'adore!",
     "That is a brilliant idea, I love it!",
     [(888, "adore")], "Beatrice enthusiastically gives her full approval")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'This stalemate makes me completely crazy!' Pascal vents over the delayed production. "
     "The causative verbal phrase expresses overwhelming frustration."),
    (1, None,
     "'I refuse this nude scene.' Beatrice calmly reiterates her non-negotiable stance. "
     "The present transitive verb asserts personal bodily agency."),
    (2, None,
     "'I spent six years writing.' Pascal reminds her of his lengthy script development. "
     "The compound past verb measures years of creative labor."),
    (3, None,
     "'It took me thirty years to refuse!' Beatrice responds with her career-long journey. "
     "The temporal phrase underscores how long it took to learn self-protection."),
    (4, None,
     "'When I say no, it means no!' Beatrice establishes an unambiguous boundary. "
     "The conditional clause affirms definitive consent."),
    (5, None,
     "'The truth is that I panicked.' Pascal drops his defensive anger and speaks honestly. "
     "The compound past colloquial verb admits sudden professional terror."),
    (6, None,
     "'I did not know how to film.' Pascal confesses his creative blockage on set. "
     "The negative imperfect verb reveals his underlying artistic doubt."),
    (7, None,
     "'So what are you looking for exactly?' Beatrice opens a constructive dialogue. "
     "The interrogative phrase invites him to articulate his artistic goal."),
    (8, None,
     "'I am looking for a very powerful gesture.' Pascal clarifies what the scene needs. "
     "The present verb with an intensified adjective defines his vision."),
    (9, None,
     "'The character wants to keep your memory.' Pascal explains the lover's obsession. "
     "The modal verb with an infinitive expresses sentimental longing."),
    (10, None,
     "'He eats a tiny piece of ear!' Pascal pitches an audacious poetic alternative. "
     "The vivid present verb suggests raw, unconventional intimacy."),
    (11, None,
     "'He eats my ear, really?' Beatrice checks the provocative concept. "
     "The surprised question tests the unconventional visual idea."),
    (12, None,
     "'Yes, to take away a part of you.' Pascal describes the poetic motive. "
     "The purpose clause explains the dramatic logic behind the act."),
    (13, None,
     "'That is a brilliant idea, I love it!' Beatrice embraces the radical creativity. "
     "The enthusiastic verb confirms her artistic commitment to the film.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "Transforming an impasse into a creative breakthrough, Beatrice Dalle and Pascal find artistic harmony without compromise. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("lea", "C'est une idée géniale, j'adore!")
