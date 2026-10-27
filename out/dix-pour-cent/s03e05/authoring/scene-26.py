# Authoring module for dix-pour-cent s03e05 scene 26 (cues 1054-1056).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-26.py --out out/dix-pour-cent/s03e05/scene-26.json

ID = "dix-pour-cent-s03e05-scene-26"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 26
TITLE = "La trahison découverte  (The Betrayal Discovered)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo"}
LABELS = {"lea": "Arlette", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1054-1056. Returning late to ASK, Hicham discovers documents proving that Andrea and Gabriel are preparing to launch a rival agency. "
    "Distraught and furious, he searches the darkened corridors for Arlette to confront this devastating betrayal."
)

INTRO = (
    "Returning late to ASK, Hicham discovers documents proving that Andrea and Gabriel are preparing to launch a rival agency. "
    "Distraught and furious, he searches the darkened corridors for Arlette to confront this devastating betrayal. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("hicham", "Arlette, où êtes-vous dans ce couloir?",
     "Arlette, where are you in this corridor?",
     [(1054, "Arlette"), (1055, "Arlette")], "Called out in the empty office corridor"),
    ("lea", "Je suis là Hicham, que se passe-t-il?",
     "I am here Hicham, what is happening?",
     [(1056, "Arlette")], "Answered calmly from her doorway"),
    ("hicham", "Regardez ce document choquant sur mon bureau!",
     "Look at this shocking document on my desk!",
     [(1056, "Arlette")], "Presented the intercepted paperwork in disbelief"),
    ("lea", "Pourquoi êtes-vous dans un état pareil?",
     "Why are you in such a state?",
     [(1056, "Arlette")], "Inquired about his visible agitation"),
    ("hicham", "Andréa et Gabriel préparent une trahison totale!",
     "Andrea and Gabriel are preparing a total betrayal!",
     [(1056, "Arlette")], "Announced the staggering betrayal"),
    ("lea", "De quelle trahison parlez-vous exactement?",
     "Which betrayal are you talking about exactly?",
     [(1056, "Arlette")], "Asked for precise facts without panic"),
    ("hicham", "Ils créent secrètement leur propre agence concurrente.",
     "They are secretly creating their own rival agency.",
     [(1056, "Arlette")], "Revealed their planned breakaway firm"),
    ("lea", "Ces projets circulent souvent dans ce métier.",
     "These plans often circulate in this business.",
     [(1056, "Arlette")], "Maintained veteran composure about industry gossip"),
    ("hicham", "Et moi qui voulais sauver notre entreprise!",
     "And I who wanted to save our company!",
     [(1056, "Arlette")], "Recalled his own selfless commitment to ASK"),
    ("lea", "Respirez calmement avant de prendre une décision.",
     "Breathe calmly before making a decision.",
     [(1056, "Arlette")], "Counseled emotional temperance and patience"),
    ("hicham", "Je suis profondément écœuré par leur hypocrisie.",
     "I am deeply sickened by their hypocrisy.",
     [(1056, "Arlette")], "Expressed raw personal revulsion"),
    ("lea", "La colère est toujours mauvaise conseillère, Hicham.",
     "Anger is always a bad counselor, Hicham.",
     [(1056, "Arlette")], "Offered a classic piece of wisdom"),
    ("hicham", "Je ne leur pardonnerai jamais ce coup.",
     "I will never forgive them this blow.",
     [(1056, "Arlette")], "Swore unforgiving retribution"),
    ("lea", "Demain matin, nous écouterons leurs explications.",
     "Tomorrow morning, we will listen to their explanations.",
     [(1056, "Arlette")], "Proposed a measured confrontation in daylight")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Arlette, where are you in this corridor?' Hicham calls out in the darkened agency. "
     "The interrogative sentence with the proper noun searches the empty hallway."),
    (1, None,
     "'I am here Hicham, what is happening?' Arlette steps forward with seasoned serenity. "
     "The present pronominal question asks about the emergency."),
    (2, None,
     "'Look at this shocking document on my desk!' Hicham waves the damning legal papers. "
     "The urgent imperative verb draws attention to the evidence."),
    (3, None,
     "'Why are you in such a state?' Arlette observes his trembling fury. "
     "The interrogative adverb with the adjective probes his extreme distress."),
    (4, None,
     "'Andrea and Gabriel are preparing a total betrayal!' Hicham reveals the conspiracy. "
     "The transitive verb with the strong noun expresses acute betrayal."),
    (5, None,
     "'Which betrayal are you talking about exactly?' Arlette seeks specific details before judging. "
     "The interrogative adjective phrase calls for concrete facts."),
    (6, None,
     "'They are secretly creating their own rival agency.' Hicham explains their corporate treachery. "
     "The adverb modifying the verb describes their covert project."),
    (7, None,
     "'These plans often circulate in this business.' Arlette shrugs with cynical experience. "
     "The present verb describes frequent agency rumors."),
    (8, None,
     "'And I who wanted to save our company!' Hicham contrasts his generosity with their deceit. "
     "The exclamatory relative clause highlights the tragic irony."),
    (9, None,
     "'Breathe calmly before making a decision.' Arlette advises emotional control. "
     "The imperative construction urges restraint in the heat of anger."),
    (10, None,
     "'I am deeply sickened by their hypocrisy.' Hicham describes his profound disgust. "
     "The past participle with the adverb conveys severe emotional nausea."),
    (11, None,
     "'Anger is always a bad counselor, Hicham.' Arlette shares a timeless proverb. "
     "The proverbial statement warns against rash executive retribution."),
    (12, None,
     "'I will never forgive them this blow.' Hicham vows that this wound will not heal. "
     "The future negative construction promises enduring consequences."),
    (13, None,
     "'Tomorrow morning, we will listen to their explanations.' Arlette urges patience until dawn. "
     "The temporal phrase defers the confrontation until a calmer hour.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "In the quiet agency corridors, Hicham confronts Arlette with the crushing proof that his closest agents plan to desert him. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("lea", "Demain matin, nous écouterons leurs explications.")
