# Authoring module for dix-pour-cent s02e03 scene 21 (cues 532-561).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-21.py --out out/dix-pour-cent/s02e03/scene-21.json

ID = "dix-pour-cent-s02e03-scene-21"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 21
TITLE = "Méthodes de relaxation  (Relaxation Methods)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "herve": "marcel"}
LABELS = {"lea": "Norman", "gabriel": "Gabriel", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 532-561. Gabriel frets about Norman Thavaud passing his driving test for an upcoming Audiard movie. "
    "Hervé offers questionable remedies and pills, but Norman insists he is completely relaxed."
)

INTRO = (
    "In the corridors of ASK, agent Gabriel frets over young client Norman Thavaud, who is taking his driving test for the fourth time. "
    "While assistant Herve offers dubious remedies to calm his nerves, Norman stubbornly insists that he is in total control. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("gabriel", "J'ai peur qu'il rate son permis.",
     "I am afraid he will fail his driving test.",
     [(532, "J'ai peur qu'il rate son permis")], ""),
    ("herve", "Il ne sait pas conduire?",
     "Does he not know how to drive?",
     [(533, "-Il ne sait pas conduire ?")], ""),
    ("gabriel", "Si, mais il panique pendant l'examen.",
     "Yes, but he panics during the exam.",
     [(533, "-Si, c'est juste l'examen"), (534, "Il panique et se fige")], ""),
    ("gabriel", "Il ne peut pas tourner sans permis.",
     "He cannot film without a license.",
     [(535, "Il ne peut pas faire le film d'Audiard sans permis")], ""),
    ("herve", "J'ai quelque chose pour se détendre.",
     "I have something to relax.",
     [(547, "-Une taffe pour se détendre")], ""),
    ("gabriel", "Il ne peut pas fumer avant l'examen!",
     "He cannot smoke before the exam!",
     [(545, "Il peut pas fumer un joint avant son permis")], ""),
    ("herve", "Alors, j'ai ces pilules très efficaces.",
     "Then, I have these very effective pills.",
     [(549, "-Ou il y a ça"), (550, "mais légal et efficace")], ""),
    ("lea", "Regardez les effets secondaires sur Internet!",
     "Look at the side effects on the Internet!",
     [(552, "Regardez : réactions cutanées"), (555, "sur Internet")], ""),
    ("herve", "Ils racontent toujours n'importe quoi.",
     "They always say total nonsense.",
     [(555, "Ils racontent n'importe quoi sur Internet")], ""),
    ("lea", "Tout médicament a des effets indésirables.",
     "Every medication has undesirable effects.",
     [(557, "Tout médicament a des effets secondaires")], ""),
    ("lea", "Je n'en ai pas du tout besoin.",
     "I do not need it at all.",
     [(559, "J'en ai pas besoin")], ""),
    ("lea", "Je suis très calme et détendu.",
     "I am very calm and relaxed.",
     [(559, "je suis calme et détendu")], ""),
    ("herve", "Comme vous voulez, mon cher Norman.",
     "As you wish, my dear Norman.",
     [(560, "-Comme vous voulez")], ""),
    ("lea", "Attendez, j'ai oublié mon téléphone portable!",
     "Wait, I forgot my mobile phone!",
     [(561, "Attends, j'ai oublié mon téléphone")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'I am afraid he will fail his driving test.' Gabriel worries about his client's upcoming driving examination. "
     "The phrase avoir peur que introduces a clause about fear."),
    (1, None,
     "'Does he not know how to drive?' Herve questions the young internet celebrity's basic vehicle skills. "
     "The negative question expresses surprise."),
    (2, None,
     "'Yes, but he panics during the exam.' Gabriel clarifies that nerves are the real problem on the road. "
     "The affirmative word si contradicts a negative question."),
    (3, None,
     "'He cannot film without a license.' The prestigious film role requires him to drive legally on set. "
     "The preposition sans indicates lack or absence."),
    (4, None,
     "'I have something to relax.' Herve proposes an unconventional remedy to ease his tension. "
     "The reflexive infinitive se detendre means to unwind."),
    (5, None,
     "'He cannot smoke before the exam!' Gabriel immediately rejects any illicit substance before the test. "
     "The temporal preposition avant precedes the noun."),
    (6, None,
     "'Then, I have these very effective pills.' The assistant offers a legal pharmaceutical alternative instead. "
     "The plural demonstrative ces points to the tablets."),
    (7, None,
     "'Look at the side effects on the Internet!' Norman reads alarming medical warnings on his smartphone screen. "
     "The imperative regardez calls immediate attention."),
    (8, None,
     "'They always say total nonsense.' Herve dismisses online medical advice as wildly exaggerated. "
     "The phrase n'importe quoi means nonsense or rubbish."),
    (9, None,
     "'Every medication has undesirable effects.' Norman remains cautious about putting chemicals in his body. "
     "The indefinite determiner tout agrees with the singular noun."),
    (10, None,
     "'I do not need it at all.' The YouTuber insists that he can manage his stress naturally. "
     "The pronoun en replaces the prepositional phrase."),
    (11, None,
     "'I am very calm and relaxed.' He claims to feel completely peaceful despite his obvious anxiety. "
     "The adjective detendu describes a relaxed state."),
    (12, None,
     "'As you wish, my dear Norman.' Herve gracefully accepts his client's personal decision. "
     "The polite phrase comme vous voulez respects another person's choice."),
    (13, None,
     "'Wait, I forgot my mobile phone!' Norman panics at the last second as he prepares to depart. "
     "The past tense ai oublie indicates a recent realization."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Norman heads off to his driving test determined to rely on his own natural focus. "
    "Remember the useful French word for contradicting a negative question: si."
)

CLOSING = ("lea", "Attendez, j'ai oublié mon téléphone portable!")
