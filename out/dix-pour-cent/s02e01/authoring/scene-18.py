# Authoring module for dix-pour-cent s02e01 scene 18 (cues 486-500).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-18.py --out out/dix-pour-cent/s02e01/scene-18.json

ID = "dix-pour-cent-s02e01-scene-18"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 18
TITLE = "L'idée lumineuse d'Andréa  (Andréa's Bright Idea)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 486-500. Andréa realizes that millionaire tech founder Hicham Janowski is the perfect investor "
    "to save ASK from bankruptcy. She runs after his sports car and asks for a ride to the film set."
)

INTRO = (
    "Outside the wine-tasting reception in Burgundy, Andréa Martel has a sudden revelation. "
    "Hicham Janowski, her former high-school classmate, has just sold his company for two hundred "
    "million euros. She convinces Gabriel that Hicham could be the savior ASK desperately needs, "
    "then sprints across the courtyard to catch him. Listen to the scene in French first."
)

STORY = [
    ("lea", "Ce type, c'est la poule aux œufs d'or.",
     "This guy is the golden goose.",
     [(486, "Ce type, c'est la poule aux œufs d'or")], ""),
    ("lea", "Il a vendu son site pour deux cents millions.",
     "He sold his website for two hundred million.",
     [(487, "Il a vendu son site pour")], "Spelled out number for A1"),
    ("lea", "Tu m'écoutes, Gabriel?",
     "Are you listening to me, Gabriel?",
     [(487, "Tu m'écoutes, Gabriel")], ""),
    ("gabriel", "Oui, mais pourquoi investirait-il chez nous?",
     "Yes, but why would he invest in us?",
     [(488, "Oui, mais pourquoi il investirait chez nous")], ""),
    ("lea", "Sa mère m'a dit qu'il divorce.",
     "His mother told me that he is getting divorced.",
     [(489, "Sa mère m'a dit qu'il divorce")], ""),
    ("lea", "Il cherche un nouveau projet.",
     "He is looking for a new project.",
     [(490, "Il cherche un nouveau terrain de jeu")], "Simplified metaphor for A1"),
    ("lea", "Je vais lui parler, il est prêt.",
     "I am going to speak to him, he is ready.",
     [(491, "Je vais le tâter, il est mûr")], "Cleaned idiom for A1"),
    ("gabriel", "Lui parler comment?",
     "Speak to him how?",
     [(492, "Le tâter comment")], ""),
    ("lea", "Nous étions de très bons amis au lycée.",
     "We were very good friends in high school.",
     [(493, "On était genre meilleurs potes au lycée")], "Simplified slang 'potes'"),
    ("lea", "Regarde! Attends!",
     "Look! Wait!",
     [(494, "Attends")], "Omitted swear word 'merde'"),
    ("lea", "Hicham, attends!",
     "Hicham, wait!",
     [(495, "Hicham, attends")], ""),
    ("hicham", "Alors, Andréa... tu as couru pour me dire au revoir?",
     "So, Andréa... you ran to say goodbye to me?",
     [(496, "Alors, Marteau"), (496, "t'as couru pour dire au revoir")], "Normalized high-school nickname"),
    ("lea", "Tu vas où?",
     "Where are you going?",
     [(497, "Tu vas où")], ""),
    ("hicham", "À l'aéroport de Dole.",
     "To Dole airport.",
     [(498, "L'aéroport de Dole")], ""),
    ("lea", "Tu peux me déposer au tournage? C'est sur la route.",
     "Can you drop me off at the shoot? It's on the way.",
     [(499, "Tu peux me déposer au tournage"), (499, "C'est sur la route")], ""),
    ("lea", "Léa Seydoux te remerciera en personne. Promis.",
     "Léa Seydoux will thank you in person. Promised.",
     [(500, "Léa Seydoux te remerciera en personne. Promis")], ""),
]

OPENER = "Let's explore Andréa's spontaneous pitch line by line."

WALK = [
    (0, None,
     "'This guy is the golden goose.' Andréa spots a massive financial opportunity. "
     "The French expression literally says the hen with golden eggs."),
    (1, None,
     "'He sold his website for two hundred million.' She shares the incredible news with Gabriel. "
     "The passé composé uses the auxiliary verb to have."),
    (2, None,
     "'Are you listening to me, Gabriel?' She snaps her colleague's attention back to her plan. "
     "The direct object pronoun precedes the verb."),
    (3, None,
     "'Yes, but why would he invest in us?' Gabriel remains cautious and skeptical. "
     "The conditional mood expresses a hypothetical action."),
    (4, None,
     "'His mother told me that he is getting divorced.' Andréa reveals her insider intelligence. "
     "The verb for divorce is used in the present tense."),
    (5, None,
     "'He is looking for a new project.' She notes that he needs a fresh challenge. "
     "The verb to look for takes a direct object without a preposition."),
    (6, None,
     "'I am going to speak to him, he is ready.' Andréa decides to make her move immediately. "
     "The near future combines to go with an infinitive."),
    (7, None,
     "'Speak to him how?' Gabriel wonders what leverage she could possibly have. "
     "Notice the indirect object pronoun placed before the verb."),
    (8, None,
     "'We were very good friends in high school.' She reminds Gabriel of their past bond. "
     "The imperfect tense describes an ongoing past relationship."),
    (9, None,
     "'Look! Wait!' Seeing Hicham's car about to leave, she shouts urgently. "
     "The imperative commands are short and punchy."),
    (10, None,
     "'Hicham, attends!' She calls after him as he starts his engine. "
     "The imperative form of to wait uses the regular second-person ending."),
    (11, None,
     "'So, Andréa... you ran to say goodbye to me?' Hicham rolls down his window with a teasing smirk. "
     "The question uses the conversational past tense."),
    (12, None,
     "'Where are you going?' Andréa quickly checks his destination. "
     "The question places the interrogative word at the end."),
    (13, None,
     "'To Dole airport.' Hicham explains that he is heading back to his private jet. "
     "The preposition specifies the airport destination."),
    (14, None,
     "'Can you drop me off at the shoot? It's on the way.' She maneuvers her way into his sports car. "
     "The phrase déposer someone means to drop someone off."),
    (15, None,
     "'Léa Seydoux will thank you in person. Promised.' She sweetens the ride with a star encounter. "
     "The future simple expresses a confident promise."),
]

TRANSITION = "Now let's listen to the entire dialogue once more from beginning to end."

OUTRO = (
    "Andréa has managed to slip into Hicham's passenger seat, setting up the perfect moment to pitch ASK. "
    "Remember the classic idiom for a goldmine: la poule aux œufs d'or."
)

CLOSING = ("lea", "Ce type, c'est la poule aux œufs d'or.")
