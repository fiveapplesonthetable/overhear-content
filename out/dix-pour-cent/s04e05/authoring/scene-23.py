# Authoring module for dix-pour-cent s04e05 scene 23 (cues 849-877).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e05/authoring/scene-23.py --out out/dix-pour-cent/s04e05/scene-23.json

ID = "dix-pour-cent-s04e05-scene-23"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 23
TITLE = "Règlement de comptes  (Settling of Accounts)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "elise": "emilie"}
LABELS = {"lea": "Andrea", "elise": "Elise"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 849-877. Andrea confronts the traitorous Elise Formain over her ruthless raid on ASK's roster. "
    "When Elise dismisses the betrayal as mere business and mocks Andrea's emotional dedication to her clients, "
    "a devastated Andrea snaps and lunges at her in fury."
)

INTRO = (
    "Face to face in the empty agency corridor, Andrea corners Elise Formain after the catastrophic raid. "
    "Refusing to show remorse, Elise sneers at Andrea's sentimental devotion to her actors, pushing Andrea past her breaking point. "
    "Let's listen to their confrontation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Comment as-tu pu trahir notre agence?",
     "How could you betray our agency?",
     [(853, "Comment tu as pu faire une chose pareille?")], "Confronted the traitorous rival directly"),
    ("elise", "Ce sont seulement les affaires, Andréa.",
     "It is only business, Andréa.",
     [(854, "c'est juste des affaires")], "Shrugged off the betrayal with cold cynicism"),
    ("lea", "Tu as volé tous mes comédiens!",
     "You stole all my actors!",
     [(858, "Les talents que tu m'as volés")], "Accused her of corporate theft"),
    ("elise", "Pourquoi rendre cette situation si personnelle?",
     "Why make this situation so personal?",
     [(855, "Pourquoi tu en fais quelque chose de personnel?")], "Dismissed emotional investment in business"),
    ("lea", "J'ai passé des nuits à veiller.",
     "I spent nights staying awake.",
     [(859, "J'ai passé des nuits à les réconforter")], "Recalled her immense personal sacrifices"),
    ("elise", "Tu es beaucoup trop émotive, ma chère.",
     "You are far too emotional, my dear.",
     [(852, "Tu es tellement émotif")], "Mocked her heartfelt devotion"),
    ("lea", "J'ai perdu ma propre famille pour eux.",
     "I lost my own family for them.",
     [(860, "je perds même ma famille à cause d'eux")], "Revealed the devastating personal cost of her career"),
    ("elise", "C'est très touchant, mais c'est fini.",
     "It is very touching, but it is over.",
     [(864, "C'est très touchant")], "Brushed off the emotional confession"),
    ("lea", "Je suis fière de mon travail accompli.",
     "I am proud of my accomplished work.",
     [(863, "Je suis fière du travail qu'on a accompli")], "Affirmed her pride in nurturing genuine art"),
    ("elise", "Tu vas te sentir bien seule désormais.",
     "You are going to feel very lonely from now on.",
     [(867, "Tu risques de te sentir un peu seule")], "Taunted her rival with isolation"),
    ("lea", "Tu n'as aucun respect pour les artistes.",
     "You have no respect for the artists.",
     [(853, "Comment tu peux être aussi méprisable?")], "Condemned her purely transactional mindset"),
    ("elise", "Ils préfèrent tous signer avec moi.",
     "They all prefer to sign with me.",
     [(866, "Si tu cherches un agent")], "Flaunted her successful corporate poaching"),
    ("lea", "Répète ça en face si tu oses!",
     "Repeat that to my face if you dare!",
     [(868, "Qu'est-ce qui te prend")], "Snarled as her patience ran out"),
    ("elise", "Lâche-moi immédiatement le bras, arrête!",
     "Let go of my arm immediately, stop!",
     [(869, "Lâche-moi!"), (870, "Arrête! Arrête!")], "Screamed in terror as physical violence broke out"),
]

WALK = [
    (0, None,
     "'How could you betray our agency?' Andrea demands an explanation. "
     "The compound past with as-tu pu highlights her profound disbelief."),
    (1, None,
     "'It is only business, Andrea.' Elise offers a callous commercial excuse. "
     "The plural demonstrative ce sont les affaires detaches personal morality."),
    (2, None,
     "'You stole all my actors!' Andrea expresses outrage at the predatory raid. "
     "The compound past verb as volé accuses her directly of theft."),
    (3, None,
     "'Why make this situation so personal?' Elise questions her emotional reaction. "
     "The interrogative infinitive phrase rendre si personnelle deflects responsibility."),
    (4, None,
     "'I spent nights staying awake.' Andrea evokes her endless dedication to clients. "
     "The verb phrase passé des nuits emphasizes years of sleepless devotion."),
    (5, None,
     "'You are far too emotional, my dear.' Elise mocks her vulnerability. "
     "The patronizing address ma chère sharpens the insult."),
    (6, None,
     "'I lost my own family for them.' Andrea confesses her deepest domestic wound. "
     "The compound past verb ai perdu lays bare her personal sacrifice."),
    (7, None,
     "'It is very touching, but it is over.' Elise dismisses the heartbreak with a smirk. "
     "The paired phrases c'est très touchant and c'est fini close the door on sympathy."),
    (8, None,
     "'I am proud of my accomplished work.' Andrea refuses to feel shame for caring. "
     "The adjective phrase fière de mon travail asserts moral dignity."),
    (9, None,
     "'You are going to feel very lonely from now on.' Elise delivers a cruel parting shot. "
     "The adverb désormais underlines permanent isolation."),
    (10, None,
     "'You have no respect for the artists.' Andrea identifies the fundamental difference between them. "
     "The negative quantifier aucun respect underscores the lack of honor."),
    (11, None,
     "'They all prefer to sign with me.' Elise boasts of her commercial triumph. "
     "The verb préfèrent tout signer claims total victory."),
    (12, None,
     "'Repeat that to my face if you dare!' Andrea's temper explodes into fury. "
     "The challenge si tu oses dares her opponent to continue."),
    (13, None,
     "'Let go of my arm immediately, stop!' Elise panics as physical violence erupts. "
     "The urgent imperative lâche-moi signals sudden chaos."),
]

OUTRO = "Shaken and bruised, Elise wrenches herself free, leaving Andrea standing in the corridor amid the wreckage of her career. When you watch the episode, listen out for the expressions meaning 'been able' and 'to betray'. You'll catch them now. See you next time."
CLOSING = ("elise", "Lâche-moi immédiatement le bras, arrête!")
