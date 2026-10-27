# Authoring module for dix-pour-cent s04e05 scene 11 (cues 439-462).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e05/authoring/scene-11.py --out overhear-content/out/dix-pour-cent/s04e05/scene-11.json

ID = "dix-pour-cent-s04e05-scene-11"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 11
TITLE = "Répétition amoureuse  (Romantic Rehearsal)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 439-462. Gabriel shares his nervousness with Sofia about an upcoming date with his ex Sarah. "
    "Sofia suggests they rehearse the conversation together, but her intense roleplay turns into a genuine emotional confrontation."
)

INTRO = (
    "In Gabriel Sarda's office, Sofia Leprince finds Gabriel anxious about reconnecting with his ex-girlfriend Sarah. "
    "To help him prepare, Sofia offers to roleplay Sarah so Gabriel can rehearse his answers. "
    "However, the pretend rehearsal quickly stirs up unresolved feelings between the two former lovers. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("gabriel", "Sarah accepte de me revoir ce soir!",
     "Sarah agrees to see me again tonight!",
     [(439, "C'est Sarah."), (440, "Elle accepte de me revoir.")], "Gabriel announces the upcoming date"),
    ("lea", "C'est super, tu es content?",
     "That is great, are you happy?",
     [(441, "Merci.")], "Sofia smiles encouragingly"),
    ("gabriel", "J'ai peur de faire une erreur.",
     "I am afraid of making a mistake.",
     [(442, "J'espère que je ne vais pas tout rater, comme d'habitude.")], "Gabriel admits his lingering nervousness"),
    ("lea", "On va répéter ensemble comme au cinéma.",
     "We will rehearse together like in cinema.",
     [(443, "L'amour, c'est comme le cinéma, ça se répète."), (444, "On répète.")], "Sofia proposes acting out the scene"),
    ("lea", "Moi, je suis Sarah, action!",
     "Me, I am Sarah, action!",
     [(445, "Je suis Sarah, tu es Gabriel."), (447, "Action.")], "Sofia enters her role with dramatic energy"),
    ("lea", "Pourquoi tu as rompu avec moi?",
     "Why did you break up with me?",
     [(448, "Pourquoi tu m'as larguée pour ton ex?")], "Sofia fires an aggressive opening question"),
    ("gabriel", "Sarah ne va pas parler comme ça!",
     "Sarah will not speak like that!",
     [(449, "Elle va être aussi énervée que ça?")], "Gabriel protests the intense interrogation"),
    ("lea", "Tu as encore des sentiments pour Sofia?",
     "Do you still have feelings for Sofia?",
     [(450, "Réponds. Tu couches encore avec Sofia?")], "Sofia probes Gabriel's lingering attachments"),
    ("gabriel", "Non, c'est du passé entre nous.",
     "No, it is in the past between us.",
     [(451, "Non. Pas du tout. Il ne s'est rien passé.")], "Gabriel denies any active romantic connection"),
    ("lea", "Tu as hésité avant de répondre!",
     "You hesitated before answering!",
     [(452, "Tu as hésité. Pourquoi tu as hésité?")], "Sofia catches the subtle pause in his voice"),
    ("lea", "Promets-moi que tu ne l'aimes plus.",
     "Promise me that you no longer love her.",
     [(458, "Promets-moi que tu ne l'aimes pas."), (460, "Promets-moi... que tu ne l'aimes plus.")], "Sofia demands an emotional promise"),
    ("gabriel", "Sofia, on devrait s'arrêter là.",
     "Sofia, we should stop there.",
     [(461, "Écoute, je crois qu'on devrait s'arrêter là.")], "Gabriel breaks character with evident discomfort"),
    ("lea", "Tu parles à Sarah ou à moi?",
     "Are you talking to Sarah or to me?",
     [(462, "Tu parles à qui? À Sarah ou à moi?")], "Sofia asks pointedly where fiction ends"),
    ("gabriel", "Je ne sais plus du tout.",
     "I no longer know at all.",
     [(462, "Tu parles à qui? À Sarah ou à moi?")], "Gabriel confesses his total confusion"),
]

WALK = [
    (0, None,
     "'Sarah agrees to see me again tonight!' Gabriel shares his excitement. "
     "The verb phrase 'accepte de' means agrees to."),
    (1, None,
     "'That is great, are you happy?' Sofia asks while masking her true reaction. "
     "The adjective 'content' describes happiness."),
    (2, None,
     "'I am afraid of making a mistake.' Gabriel confesses his self-doubt. "
     "The idiom 'avoir peur de' expresses fear or apprehension."),
    (3, None,
     "'We will rehearse together like in cinema.' Sofia suggests a practical acting exercise. "
     "The verb 'repeter' means to rehearse or repeat."),
    (4, None,
     "'Me, I am Sarah, action!' Sofia adopts the character of Gabriel's date. "
     "The word 'action' signals the start of a take in filmmaking."),
    (5, None,
     "'Why did you break up with me?' Sofia begins the simulated confrontation. "
     "The compound past 'as rompu' comes from 'rompre', to break up."),
    (6, None,
     "'Sarah will not speak like that!' Gabriel objects to the hostile greeting. "
     "The near-future 'va parler' describes imminent speech."),
    (7, None,
     "'Do you still have feelings for Sofia?' Sofia uses the roleplay to question Gabriel about herself. "
     "The plural noun 'sentiments' refers to emotional feelings."),
    (8, None,
     "'No, it is in the past between us.' Gabriel claims that his past relationship is over. "
     "The noun 'passe' designates what has already happened."),
    (9, None,
     "'You hesitated before answering!' Sofia detects doubt in his immediate reply. "
     "The verb 'hesiter' signifies hesitating."),
    (10, None,
     "'Promise me that you no longer love her.' Sofia pushes for total reassurance. "
     "The imperative 'promets-moi' comes from 'promettre'."),
    (11, None,
     "'Sofia, we should stop there.' Gabriel recognizes that the exercise has gone too far. "
     "The conditional 'devrait' softens a recommendation."),
    (12, None,
     "'Are you talking to Sarah or to me?' Sofia challenges him to face his authentic emotions. "
     "The interrogative 'qui' asks whom."),
    (13, None,
     "'I no longer know at all.' Gabriel admits his helplessness in front of her. "
     "The phrase 'du tout' emphasizes the negative totality."),
]

OUTRO = (
    "What started as a lighthearted rehearsal leaves both Gabriel and Sofia unsettled by their true feelings. "
    "As the boundary between acting and real life dissolves, Gabriel must confront his romantic indecision. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("gabriel", "Je crois qu'on a fini de répéter!")
