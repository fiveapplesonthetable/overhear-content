# Authoring module for dix-pour-cent s02e01 scene 20 (cues 550-640).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-20.py --out out/dix-pour-cent/s02e01/scene-20.json

ID = "dix-pour-cent-s02e01-scene-20"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 20
TITLE = "Le caprice d'Hicham  (Hicham's Whim)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo", "karine": "emilie"}
LABELS = {"lea": "Andréa", "hicham": "Hicham", "karine": "Karine"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 550-640. Arriving on the Burgundy film set, Hicham generously offers his luxury car to save the shoot, "
    "but throws a sudden tantrum when the crew refuses to cast his cousin as the on-screen driver."
)

INTRO = (
    "Andréa brings Hicham onto the chaotic film set of Léa Seydoux's latest movie. "
    "When a key vehicle breaks down, Hicham generously volunteers his own sports car to help. "
    "However, his impulsive demands quickly clash with the reality of film production. "
    "Listen to the scene in French first."
)

STORY = [
    ("hicham", "Je peux jeter un œil?",
     "Can I take a look around?",
     [(551, "Je peux jeter un œil")], ""),
    ("lea", "C'est un film institutionnel pour ASK.",
     "This is a major film for ASK.",
     [(553, "C'est un film institutionnel pour ASK")], ""),
    ("lea", "On a le réalisateur et l'actrice principale, Léa Seydoux.",
     "We have the director and the lead actress, Léa Seydoux.",
     [(554, "On a le réalisateur"), (556, "et l'actrice principale, Léa Seydoux")], ""),
    ("karine", "Léa est rentrée à l'hôtel.",
     "Léa went back to the hotel.",
     [(561, "moi c'est Karine"), (562, "Léa est rentrée à l'hôtel")], ""),
    ("karine", "C'est difficile depuis hier. Quand la voiture a lâché, on a dû s'arrêter.",
     "It has been hard since yesterday. When the car gave up, we had to stop.",
     [(599, "depuis hier"), (602, "Quand la voiture a lâché")], "Cleaned vulgar language"),
    ("hicham", "Vous pourriez utiliser ma voiture?",
     "Could you use my car?",
     [(605, "Vous pourriez utiliser ma voiture")], ""),
    ("hicham", "Même style, même couleur.",
     "Same style, same color.",
     [(606, "Même style, même couleur")], ""),
    ("karine", "Pourquoi pas? C'est super!",
     "Why not? That's great!",
     [(608, "Pourquoi pas"), (611, "C'est super")], ""),
    ("karine", "Il nous la faudrait encore quelques jours.",
     "We would need it for a couple more days.",
     [(613, "il nous la faudrait encore quelques jours")], ""),
    ("hicham", "Pas de problème, avec plaisir.",
     "No problem, with pleasure.",
     [(614, "Pas de problème, avec plaisir")], ""),
    ("hicham", "J'ai une idée. Mon cousin Saïd, c'est lui qui conduit dans le film.",
     "I have an idea. My cousin Saïd, he's the one who drives in the film.",
     [(619, "J'ai une idée"), (620, "Dans le film"), (627, "Mon cousin")], ""),
    ("karine", "Non, Hicham, ce n'est pas comme ça que ça marche.",
     "No, Hicham, that's not how it works.",
     [(621, "Non, Hicham, c'est pas comme ça que ça marche")], "Restored 'ne' for standard French"),
    ("karine", "On a déjà un acteur professionnel.",
     "We already have a professional actor.",
     [(622, "On a déjà"), (624, "un acteur professionnel")], ""),
    ("hicham", "Mon cousin s'en sortira très bien.",
     "My cousin will do very well.",
     [(627, "il s'en sortira très bien")], ""),
    ("hicham", "Bon, laissez tomber. Au revoir!",
     "Okay, forget it. Goodbye!",
     [(630, "Bon, laissez tomber"), (632, "Au revoir")], ""),
    ("karine", "Il est fou ce mec.",
     "The guy's crazy.",
     [(637, "Il est fou ce mec")], ""),
    ("lea", "Non, attendez, Hicham! Hicham!",
     "No, wait, Hicham! Hicham!",
     [(634, "Non, attendez, Hicham"), (639, "Hicham")], ""),
]

OPENER = "Let's examine how Hicham's volatile personality plays out on set."

WALK = [
    (0, None,
     "'Can I take a look around?' Hicham asks eagerly as they arrive on the set. "
     "The idiom jeter un œil literally means to throw an eye."),
    (1, None,
     "'This is a major film for ASK.' Andréa proudly introduces the high-profile project. "
     "The demonstrative pronoun c'est introduces the predicate noun."),
    (2, None,
     "'We have the director and the lead actress, Léa Seydoux.' She lists the prestigious talent. "
     "The adjective principale follows the noun it modifies."),
    (3, None,
     "'Léa went back to the hotel.' Karine, the production assistant, explains the star's absence. "
     "Because Léa is female, the past participle rentrée takes an extra e."),
    (4, None,
     "'It has been hard since yesterday. When the car gave up, we had to stop.' The crew faces major delays. "
     "The preposition depuis indicates an action continuing from the past."),
    (5, None,
     "'Could you use my car?' Hicham steps forward with a generous offer. "
     "The conditional form vous pourriez makes a polite suggestion."),
    (6, None,
     "'Same style, same color.' He points out that his sports car is an exact visual match. "
     "The adjective même precedes the noun when it means same."),
    (7, None,
     "'Why not? That's great!' Karine is thrilled by the unexpected solution. "
     "The phrase pourquoi pas expresses enthusiastic agreement."),
    (8, None,
     "'We would need it for a couple more days.' She explains the filming schedule. "
     "The conditional structure il faudrait expresses a requirement."),
    (9, None,
     "'No problem, with pleasure.' Hicham basks in playing the generous patron. "
     "The prepositional phrase avec plaisir is a polite confirmation."),
    (10, None,
     "'I have an idea. My cousin Saïd, he's the one who drives in the film.' He suddenly adds an impossible condition. "
     "The cleft sentence c'est lui qui emphasizes the subject."),
    (11, None,
     "'No, Hicham, that's not how it works.' Karine firmly pushes back. "
     "The phrase comme ça means like that or in that way."),
    (12, None,
     "'We already have a professional actor.' The production must respect union rules and continuity. "
     "The adverb déjà sits right after the verb."),
    (13, None,
     "'My cousin will do very well.' Hicham refuses to take no for an answer. "
     "The future simple s'en sortira expresses certainty."),
    (14, None,
     "'Okay, forget it. Goodbye!' Offended at not getting his way, Hicham abruptly storms off. "
     "The imperative phrase laissez tomber means drop it or forget it."),
    (15, None,
     "'The guy's crazy.' Karine stares in shock as the billionaire walks away. "
     "The colloquial noun mec means guy or bloke."),
    (16, None,
     "'No, wait, Hicham! Hicham!' Andréa chases after him in desperation. "
     "The imperative form attendez calls out for him to stop."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Hicham proved that while he has immense resources, his temper and whims are a force of nature. "
    "Remember the everyday expression for letting something drop: laisser tomber."
)

CLOSING = ("karine", "Il est fou ce mec.")
