# Authoring module for dix-pour-cent s03e01 scene 13 (cues 306-382).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e01/authoring/scene-13.py --out overhear-content/out/dix-pour-cent/s03e01/scene-13.json

ID = "dix-pour-cent-s03e01-scene-13"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 13
TITLE = "Le personnage du Déserteur  (The Deserter Character)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jean": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Andréa", "jean": "Jean Dujardin", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 306-382. In his trailer, Jean Dujardin refuses to begin his next film shoot as a banker, "
    "having lost himself in his 1870 deserter persona and signed the contract as Émile Berthier."
)

INTRO = (
    "Visiting actor Jean Dujardin in his secluded trailer, agents Andrea and Gabriel find him still completely immersed in his 1870 deserter role. "
    "As they urge him to prepare for his next film role as a banker, they discover that he even signed his new production contract as Emile Berthier. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Jean, tu es là?",
     "Jean, are you there?",
     [(307, "Jean"), (312, "Oui")], ""),
    ("lea", "Tu es très marqué par ton rôle.",
     "You are very marked by your role.",
     [(313, "très marqué par ton rôle dans le Déserteur")], ""),
    ("jean", "J'ai jamais vécu ça avant, jamais!",
     "I have never experienced this before, never!",
     [(315, "J'ai jamais vécu ça avant")], ""),
    ("lea", "Ils t'attendent pour le tournage.",
     "They are waiting for you for the shoot.",
     [(316, "ils t'attendent pour le tournage")], ""),
    ("gabriel", "Tu dois jouer un banquier moderne.",
     "You have to play a modern banker.",
     [(317, "jouer un banquier")], ""),
    ("jean", "Franchement, là, je peux pas!",
     "Honestly, right now, I cannot!",
     [(319, "Franchement, là, je peux pas")], ""),
    ("jean", "Je peux pas enchaîner comme ça.",
     "I cannot follow on like that.",
     [(320, "Je peux pas enchaîner comme ça")], ""),
    ("jean", "J'ai passé six mois dans la forêt.",
     "I spent six months in the forest.",
     [(322, "six mois dans la forêt")], ""),
    ("jean", "Je suis allé à l'os de l'humain.",
     "I went down to bare human bone.",
     [(324, "Je suis allé à l'os")], ""),
    ("jean", "Je refuse le bruit et les gens!",
     "I refuse the noise and people!",
     [(326, "avec le bruit, les gens")], ""),
    ("gabriel", "Mais tu n'as pas signé ton contrat?",
     "But have you not signed your contract?",
     [(330, "t'as même pas signé ton contrat")], ""),
    ("jean", "Si, j'ai signé mon contrat!",
     "Yes, I signed my contract!",
     [(331, "Si, je l'ai signé")], ""),
    ("lea", "Tu as signé Émile Berthier!",
     "You signed Emile Berthier!",
     [(332, "T'as signé Émile Berthier")], ""),
    ("lea", "C'est ton personnage, Jean.",
     "That is your character, Jean.",
     [(334, "C'est ton personnage, Jean")], ""),
    ("lea", "Ce n'est pas toi!",
     "It is not you!",
     [(335, "C'est pas toi")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Jean, are you there?' Andrea checks on her reclusive star client. "
     "The direct address seeks his attention."),
    (1, None,
     "'You are very marked by your role.' Andrea gently observes his deep emotional exhaustion. "
     "The past participle indicates lasting psychological impact."),
    (2, None,
     "'I have never experienced this before, never!' Jean emphasizes the unprecedented intensity of the shoot. "
     "The repeated negative adverb highlights extreme feelings."),
    (3, None,
     "'They are waiting for you for the shoot.' Andrea reminds him of his upcoming film commitment. "
     "The transitive verb stresses professional obligation."),
    (4, None,
     "'You have to play a modern banker.' Gabriel describes the civilized character waiting for him. "
     "The modal verb introduces his next acting assignment."),
    (5, None,
     "'Honestly, right now, I cannot!' Jean bluntly rejects taking on another film immediately. "
     "The negative modal verb expresses total inability."),
    (6, None,
     "'I cannot follow on like that.' He insists on taking a break before another production. "
     "The verbal phrase refers to jumping between projects."),
    (7, None,
     "'I spent six months in the forest.' Jean recalls his prolonged survivalist isolation. "
     "The temporal noun phrase underscores extended hardship."),
    (8, None,
     "'I went down to bare human bone.' He describes stripping away civilized identity for his role. "
     "The prepositional phrase evokes primal survival."),
    (9, None,
     "'I refuse the noise and people!' Jean shrinks from modern urban life and film sets. "
     "The transitive verb expresses visceral revulsion."),
    (10, None,
     "'But have you not signed your contract?' Gabriel asks about legal paperwork for the banking movie. "
     "The negative inverted question probes formal commitment."),
    (11, None,
     "'Yes, I signed my contract!' Jean insists that he already put pen to paper. "
     "The assertive affirmative particle disputes Gabriel's doubt."),
    (12, None,
     "'You signed Emile Berthier!' Andrea reveals that he used his character's fictional name. "
     "The proper noun phrase reveals deep method confusion."),
    (13, None,
     "'That is your character, Jean.' Andrea tries to bring the disoriented actor back to reality. "
     "The predicate noun distinguishes fiction from reality."),
    (14, None,
     "'It is not you!' She reminds him of his own true identity. "
     "The emphatic negative copula enforces psychological separation.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Struggling to separate reality from fiction after months in the woods, Jean Dujardin refuses to leave his intense deserter persona behind. "
    "Listen to the conversation once more in French."
)

CLOSING = ("jean", "Laissez-moi un peu de temps.")
