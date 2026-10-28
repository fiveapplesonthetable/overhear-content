# Authoring module for dix-pour-cent s03e05 scene 08 (cues 246-274).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-08.py --out out/dix-pour-cent/s03e05/scene-08.json

ID = "dix-pour-cent-s03e05-scene-08"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 8
TITLE = "La suite de la carrière  (The Next Career Move)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "camille": "emilie", "herve": "theo"}
LABELS = {"lea": "Sophia", "camille": "Camille", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 246-274. Sophia Leprince drops by ASK hoping to discuss her next career moves with Mathias. "
               "When Mathias rushes past, Camille and Herve try to reassure Sophia about fan reactions to her recent nude scene. Adapted for A1 French.")

INTRO = ("At the ASK agency, young actress Sophia Leprince arrives unannounced to get advice on future projects. "
         "Feeling ignored by Mathias, Sophia vents to Camille and Herve about public reactions to her film role. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("camille", "Bonjour Sophia, tu vas bien aujourd'hui?",
     "Hello Sophia, are you doing well today?",
     [(246, "Ça va, Sophia ?")], "Camille greets Sophia warmly"),
    ("lea", "Oui, je passais dans le quartier.",
     "Yes, I was passing through the neighborhood.",
     [(249, "je passais dans le quartier")], "Sophia offers an impromptu excuse"),
    ("camille", "Tu as un rendez-vous avec Mathias?",
     "Do you have an appointment with Mathias?",
     [(248, "T'as rendez-vous avec Mathias ?")], "Camille checks the agency schedule"),
    ("lea", "Je veux lui parler de ma carrière.",
     "I want to speak with him about my career.",
     [(255, "parler avec vous de la suite")], "Sophia expresses her career urgency"),
    ("lea", "Mais Mathias semble me fuir toujours.",
     "But Mathias always seems to avoid me.",
     [(266, "Mathias me fuit")], "Sophia shares her insecurity"),
    ("lea", "Je ne reçois aucune nouvelle proposition.",
     "I receive no new offers.",
     [(266, "Je reçois rien")], "Sophia fears missing out on scripts"),
    ("camille", "Il est juste très stressé en ce moment.",
     "He is just very stressed right now.",
     [(267, "il est parfois un peu rigidifié par le stress")], "Camille defends her busy father"),
    ("herve", "Nous recevons beaucoup de lettres de fans!",
     "We receive lots of fan letters!",
     [(268, "on reçoit plein de courrier")], "Herve tries to boost her spirits"),
    ("lea", "Ils veulent seulement des photos dédicacées!",
     "They only want autographed photos!",
     [(269, "ils veulent des photos de moi nue, dédicacées")], "Sophia points out the shallow fan mail"),
    ("lea", "Tout le monde parle de cette scène nue.",
     "Everyone talks about that nude scene.",
     [(271, "c'est que j'ai joué à poil")], "Sophia laments objectification"),
    ("herve", "Mais le public a vraiment adoré le film.",
     "But the audience truly loved the film.",
     [(273, "j'ai bien accroché")], "Herve underscores positive viewer response"),
    ("herve", "C'est plutôt élogieux pour une actrice!",
     "That is rather complimentary for an actress!",
     [(274, "C'est plutôt élogieux")], "Herve reframes the attention"),
    ("camille", "Tu vas bientôt décrocher un grand rôle!",
     "You will soon land a great role!",
     [(260, "attendre la bonne proposition")], "Camille offers sincere encouragement"),
]

OPENER = "Let's explore how Camille and Herve reassure Sophia about her career line by line."

WALK = [
    (0, None,
     "'Hello Sophia, are you doing well today?' Camille warmly greets the young actress at the agency entrance. Camille uses the casual singular 'you' with 'are going', showing close familiarity."),
    (1, None,
     "'Yes, I was passing through the neighborhood.' Sophia makes a casual excuse for dropping in unannounced. Notice how 'was passing' leads directly into the noun meaning 'neighborhood.'."),
    (2, None,
     "'Do you have an appointment with Mathias?' Camille checks whether Mathias is expecting her. The verb meaning 'have' pairs naturally with the noun for 'appointment' in everyday conversation."),
    (3, None,
     "'I want to speak with him about my career.' Sophia seeks strategic guidance for her upcoming roles. Notice how 'want' leads directly into the noun meaning 'career.'."),
    (4, None,
     "'But Mathias always seems to avoid me.' Sophia vents her anxiety that Mathias is neglecting her. The reflexive pronoun sits right in front of the verb for 'seems', turning the action back onto the subject."),
    (5, None,
     "'I receive no new offers.' Sophia worries about her career stalling after her movie release. Notice how 'receive' leads directly into the noun meaning 'offer.'."),
    (6, None,
     "'He is just very stressed right now.' Camille defends her father's preoccupied demeanor. The descriptive adjective for 'stressed' agrees in gender and number with its noun."),
    (7, None,
     "'We receive lots of fan letters!' Herve tries to cheer her up by pointing out her rising fame. Notice how 'receive' leads directly into the noun meaning 'letters'."),
    (8, None,
     "'They only want autographed photos!' Sophia complains that male fans focus exclusively on her appearance. The verb meaning 'want' pairs naturally with the noun for 'photos' in everyday conversation."),
    (9, None,
     "'Everyone talks about that nude scene.' Sophia laments being reduced to a single scandalous movie moment. Notice how 'speaks' leads directly into the noun meaning 'world'."),
    (10, None,
     "'But the audience truly loved the film.' Herve reminds her of the positive critical and viewer reception. This conversational past tense combines a helper verb with the past participle for 'loved'."),
    (11, None,
     "'That is rather complimentary for an actress!' Herve playfully frames the public attention as a compliment. In spoken French, the little word before 'it is' drops its final vowel and attaches with an apostrophe."),
    (12, None,
     "'You will soon land a great role!' Camille encourages Sophia to stay confident and patient. French forms the near future by pairing the present tense of 'to go' directly with 'to land'."),
]

TRANSITION = "Now let's listen to the agency conversation once more from start to finish."

OUTRO = ("Sophia confronts the reality of post-breakout fame while Camille and Herve provide essential emotional support. "
         "Let's review the key cinema and career vocabulary from this scene.")

CLOSING = ("camille", "Tu vas bientôt décrocher un grand rôle!")
