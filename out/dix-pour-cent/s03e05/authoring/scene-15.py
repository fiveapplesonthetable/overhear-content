# Authoring module for dix-pour-cent s03e05 scene 15 (cues 622-728).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e05/authoring/scene-15.py --out overhear-content/out/dix-pour-cent/s03e05/scene-15.json

ID = "dix-pour-cent-s03e05-scene-15"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 15
TITLE = "La colère de Béatrice  (Béatrice's Fury)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "beatrice": "emilie"}
LABELS = {"lea": "Andréa", "beatrice": "Béatrice"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 622-649. Furious over director Birag's underhanded demands, Béatrice Dalle refuses to return to the film set, "
    "threatening to let the production sue her. Andréa warns that ASK is financially liable for the contract, "
    "but promises she will never abandon Béatrice and will find a solution. Adapted for A1 French."
)

INTRO = (
    "Furious and pacing inside her dressing room trailer, iconic actress Beatrice Dalle vows never to return to the set. "
    "When Andrea explains that a lawsuit could ruin the agency, Beatrice fears she is being abandoned. "
    "Let's listen to their intense conversation in French first."
)

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
    ("beatrice", "Je pense toujours à ce réalisateur Birag.",
     "I think constantly about this director Birag.",
     [(622, "je pense à Birag")], "Expressing obsession"),
    ("beatrice", "Cette histoire me met vraiment les nerfs!",
     "This situation really gets on my nerves!",
     [(623, "ça me fout les nerfs")], "Venting frustration"),
    ("lea", "Mais nous devons retourner sur le plateau.",
     "But we must return to the set.",
     [(624, "va falloir y retourner")], "Urging return to filming"),
    ("beatrice", "Non, je n'y retournerai pas du tout.",
     "No, I will not return at all.",
     [(625, "Non j'y retournerai pas")], "Refusing adamantly"),
    ("beatrice", "Ils peuvent me faire un grand procès!",
     "They can bring a big lawsuit against me!",
     [(626, "Ils ont qu'à me faire un procès")], "Daring production to sue"),
    ("beatrice", "Je n'ai rien, je ne suis pas solvable.",
     "I have nothing, I am not solvent.",
     [(627, "je suis pas solvable")], "Pointing out insolvency"),
    ("lea", "Béatrice, les amendes vont retomber sur ASK.",
     "Beatrice, the fines will fall back on ASK.",
     [(629, "ça va retomber sur nous sur S.K.")], "Warning of financial liability"),
    ("beatrice", "Est-ce que tu es sérieuse, Andréa?",
     "Are you serious, Andrea?",
     [(630, "Tu es sérieuse ?")], "Questioning seriousness"),
    ("lea", "Notre agence est responsable des contrats signés.",
     "Our agency is liable for signed contracts.",
     [(631, "on est responsable des contrats que tu signes")], "Explaining legal duty"),
    ("beatrice", "Alors, est-ce que tu me lâches?",
     "So, are you abandoning me?",
     [(634, "Tu me lâches ?")], "Fearing abandonment"),
    ("lea", "Non Béatrice, je ne te lâche jamais!",
     "No Beatrice, I never abandon you!",
     [(635, "Non Béatrice je te lâche pas")], "Reassuring star client"),
    ("lea", "Je suis toujours à fond derrière toi.",
     "I am always completely behind you.",
     [(636, "Je suis à fond derrière toi")], "Affirming unwavering loyalty"),
    ("lea", "Nous allons trouver une solution ensemble aujourd'hui.",
     "We are going to find a solution together today.",
     [(637, "on va trouver une solution")], "Promising joint solution"),
    ("beatrice", "D'accord, je te fais entièrement confiance, Andréa.",
     "Alright, I trust you completely, Andrea.",
     [(648, "tu penses à un truc ?"), (649, "Peut-être")], "Placing trust in agent"),
]

WALK = [
    (0, None,
     "'I think constantly about this director Birag.' Beatrice fumes over her director's deception. "
     "The adverb 'toujours' indicates continuous thought."),
    (1, None,
     "'This situation really gets on my nerves!' Beatrice vents her boiling irritation. "
     "The colloquial phrase 'les nerfs' conveys deep agitation."),
    (2, None,
     "'But we must return to the set.' Andrea gently reminds her of contractual reality. "
     "The noun 'plateau' refers to a film set or soundstage."),
    (3, None,
     "'No, I will not return at all.' Beatrice digs in her heels stubbornly. "
     "The adverbial pronoun 'y' refers back to the film set."),
    (4, None,
     "'They can bring a big lawsuit against me!' Beatrice dares the producers to sue her. "
     "The masculine noun 'proces' means legal trial or lawsuit."),
    (5, None,
     "'I have nothing, I am not solvent.' Beatrice points out she has no assets to seize. "
     "The financial adjective 'solvable' means solvent."),
    (6, None,
     "'Beatrice, the fines will fall back on ASK.' Andrea explains the harsh economic fallout for the agency. "
     "The verb 'retomber' means to fall back on."),
    (7, None,
     "'Are you serious, Andrea?' Beatrice is stunned by the collective exposure. "
     "The feminine adjective 'serieuse' questions authenticity."),
    (8, None,
     "'Our agency is liable for signed contracts.' Andrea details their professional obligations. "
     "The adjective 'responsable' denotes legal liability."),
    (9, None,
     "'So, are you abandoning me?' Beatrice asks out of sudden vulnerability. "
     "The verb 'lacher' colloquially means to let down or abandon."),
    (10, None,
     "'No Beatrice, I never abandon you!' Andrea fiercely reassures her iconic client. "
     "The negative adverb 'jamais' promises lifelong loyalty."),
    (11, None,
     "'I am always completely behind you.' Andrea affirms total solidarity. "
     "The idiom 'a fond' means wholeheartedly or all the way."),
    (12, None,
     "'We are going to find a solution together today.' Andrea pivots constructively toward a resolution. "
     "The noun 'solution' means resolution or answer."),
    (13, None,
     "'Alright, I trust you completely, Andrea.' Beatrice relents and places her faith in Andrea. "
     "The phrase 'faire confiance' means to trust."),
]

OUTRO = (
    "Andrea reaffirms the deep bond of trust that connects an agent with an artist. "
    "By promising unwavering support, she restores Beatrice's morale while searching for a way out of the legal trap. "
    "Now let's listen to the scene once more."
)

CLOSING = ("lea", "Je suis toujours à fond derrière toi.")
