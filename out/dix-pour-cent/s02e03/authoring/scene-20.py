# Authoring module for dix-pour-cent s02e03 scene 20 (cues 496-531).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-20.py --out out/dix-pour-cent/s02e03/scene-20.json

ID = "dix-pour-cent-s02e03-scene-20"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 20
TITLE = "Une fête grandiose  (A Grandiose Party)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo", "herve": "emilie"}
LABELS = {"lea": "Camille", "hicham": "Hicham", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 496-531. Hervé and Camille present their modest birthday plans for Hicham's ten-year-old son Elvis. "
    "Furious at his ex-wife and determined to win his son's admiration, Hicham rejects the simple laser game "
    "and demands a massive, celebrity-filled celebration at a real castle."
)

INTRO = (
    "In Hicham's office, Hervé and Camille unveil their plans for Elvis's tenth birthday party. "
    "To their surprise, Hicham angrily dismisses their ideas and demands a luxury celebration on a breathtaking scale. "
    "Listen to the scene in French first."
)

STORY = [
    ("herve", "On a préparé l'anniversaire d'Elvis.",
     "We planned Elvis's birthday party.",
     [(496, "Alors, l'anniversaire d'Elvis"), (498, "Les parents de Ferdinand et Elliot les laisseront venir")], ""),
    ("lea", "On a réservé deux sessions de laser game.",
     "We booked two laser game sessions.",
     [(499, "J'ai réservé un laser game. Deux sessions")], ""),
    ("herve", "Et un gâteau géant avec des bonbons!",
     "And a giant cake with candy!",
     [(501, "j'ai commandé un gâteau bonbons extra-large")], ""),
    ("hicham", "Vous croyez vraiment que ça suffit?",
     "Do you really think that is enough?",
     [(502, "Qu'est-ce que vous avez fait")], ""),
    ("lea", "C'est amusant pour des enfants de dix ans.",
     "It's fun for ten-year-old children.",
     [(510, "Donc pour les dix ans du gamin")], ""),
    ("hicham", "La mère d'Elvis me pourrit la vie!",
     "Elvis's mother is ruining my life!",
     [(508, "On divorce, elle me pourrit la vie")], ""),
    ("hicham", "Je veux la meilleure fête du monde!",
     "I want the best party in the world!",
     [(511, "je veux la meilleure fête qui soit")], ""),
    ("hicham", "On oublie le laser game et les bonbons.",
     "We forget the laser game and the candies.",
     [(513, "Alors on s'en fout du gâteau bonbons"), (514, "et d'un laser game à la con")], ""),
    ("hicham", "Je veux une fête grandiose, les amis!",
     "I want a grandiose party, friends!",
     [(515, "Je veux une grande fête"), (516, "Une fête d'enfer, les gars")], ""),
    ("herve", "Une fête grandiose? Quel genre d'endroit?",
     "A grandiose party? What kind of place?",
     [(517, "D'accord")], ""),
    ("hicham", "Je veux un château avec un grand parc!",
     "I want a castle with a large park!",
     [(517, "Je veux un château avec son parc")], ""),
    ("lea", "Un château? Mais c'est énorme!",
     "A castle? But that is huge!",
     [(518, "Notez")], ""),
    ("hicham", "Notez tout: des fontaines et de la musique.",
     "Note everything: fountains and music.",
     [(519, "Je veux des fontaines de limonade"), (520, "de la musique, et je veux que ce soit grandiose")], "") ,
    ("herve", "Et qui sont les personnes invitées?",
     "And who are the invited guests?",
     [(521, "J'ai dressé une liste d'invités")], ""),
    ("hicham", "Toute l'agence et de grandes célébrités!",
     "The whole agency and big celebrities!",
     [(522, "Toute l'agence"), (523, "Oui, je veux que mon fils sache ce que je fais")], ""),
    ("lea", "D'accord, nous allons organiser cela.",
     "All right, we will organize that.",
     [(528, "Faites venir Julien Doré et Norman")], "")
]

OPENER = "Let's examine how Hicham pushes for an extravagant birthday celebration."

WALK = [
    (0, None,
     "'We planned Elvis's birthday party.' Hervé announces proudly. "
     "The compound past a préparé comes from préparer."),
    (1, None,
     "'We booked two laser game sessions.' Camille presents the main activity. "
     "The numeral deux qualifies the feminine plural sessions."),
    (2, None,
     "'And a giant cake with candy!' Hervé adds with cheerful enthusiasm. "
     "The adjective géant means gigantic or giant."),
    (3, None,
     "'Do you really think that is enough?' Hicham scoffs disdainfully. "
     "The verb suffire means to suffice or be enough."),
    (4, None,
     "'It's fun for ten-year-old children.' Camille defends the kid-friendly plan. "
     "The adjective amusant means entertaining or fun."),
    (5, None,
     "'Elvis's mother is ruining my life!' Hicham vents his personal frustration. "
     "The colloquial verb pourrir means to rot or ruin."),
    (6, None,
     "'I want the best party in the world!' Hicham demands an extraordinary event. "
     "The superlative la meilleure fête means the best party."),
    (7, None,
     "'We forget the laser game and the candies.' He cancels their initial proposal instantly. "
     "The verb oublier means to forget or leave aside."),
    (8, None,
     "'I want a grandiose party, friends!' Hicham sets his extravagant vision. "
     "The adjective grandiose means magnificent or spectacular."),
    (9, None,
     "'A grandiose party? What kind of place?' Hervé asks cautiously. "
     "The noun phrase quel genre de means what sort of."),
    (10, None,
     "'I want a castle with a large park!' Hicham reveals his lavish ambition. "
     "The noun château means castle or grand manor."),
    (11, None,
     "'A castle? But that is huge!' Camille gasps at the scale. "
     "The adjective énorme means enormous or massive."),
    (12, None,
     "'Note everything: fountains and music.' Hicham rattles off extravagant features. "
     "The imperative notez directs them to take notes."),
    (13, None,
     "'And who are the invited guests?' Hervé checks the guest list. "
     "The feminine plural participle invitées functions as an adjective modifying personnes."),
    (14, None,
     "'The whole agency and big celebrities!' Hicham wants a star-studded spectacle. "
     "The noun célébrité means celebrity."),
    (15, None,
     "'All right, we will organize that.' Camille accepts the daunting challenge. "
     "The immediate future allons organiser combines aller with the infinitive.")
]

TRANSITION = "Now let's listen to Hicham's ambitious demands once more at normal speed."

OUTRO = (
    "Faced with Hicham's immense ambitions, Camille and Hervé must now pull off the ultimate party "
    "with a real castle and celebrity guests. Listen to the entire exchange once more in French."
)

CLOSING = ("lea", "D'accord, nous allons organiser cela.")
