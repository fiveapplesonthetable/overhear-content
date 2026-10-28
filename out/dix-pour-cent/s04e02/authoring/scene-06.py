# Authoring module for dix-pour-cent s04e02 scene 06 (cues 338-359).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e02/authoring/scene-06.py --out out/dix-pour-cent/s04e02/scene-06.json

ID = "dix-pour-cent-s04e02-scene-06"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 6
TITLE = "La promotion de Noémie  (Noémie's Promotion)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "justine": "emilie", "mathias": "marcel"}
LABELS = {"lea": "Noémie", "justine": "Justine", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 338-359. At Mathias's new production firm, Noemie asserts her new executive role "
               "amid office gossip and awkward workplace affection.")

INTRO = ("At lunch in Mathias Barneville's new production offices, Noemie meets her new colleagues. "
         "She clarifies that she is no longer an assistant but a development executive, before Mathias greets her warmly. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("justine", "Fais attention quand Vincent parle à midi.",
     "Watch out when Vincent speaks at lunchtime.",
     [(342, "C'est Vincent, fais attention, quand il parle")], "Justine gives Noemie some cafeteria advice"),
    ("lea", "Pourquoi? Quel est son problème?",
     "Why? What is his problem?",
     [(343, "Pas juste un tunnel")], "Noemie asks for clarification"),
    ("justine", "Il a une mauvaise haleine terrible!",
     "He has terrible bad breath!",
     [(343, "un tunnel de mauvaise haleine.")], "Justine explains the uncomfortable truth"),
    ("lea", "Merci beaucoup pour cette mise en garde.",
     "Thank you very much for this warning.",
     [(345, "Merci pour la mise en garde.")], "Noemie appreciates the friendly alert"),
    ("justine", "Entre assistants, il faut se serrer les coudes.",
     "Between assistants, we must stick together.",
     [(346, "Nous les assistants, il faut se serrer les coudes.")], "Justine assumes solidarity among support staff"),
    ("lea", "Mais je ne suis plus une assistante!",
     "But I am no longer an assistant!",
     [(347, "Je ne suis plus l'assistante de Mathias.")], "Noemie corrects her politely but firmly"),
    ("justine", "Ah bon? Quel poste occupes-tu maintenant?",
     "Really? What job do you hold now?",
     [(348, "Non ?")], "Justine expresses surprise at the clarification"),
    ("lea", "Je suis responsable du développement des projets.",
     "I am head of project development.",
     [(350, "sa Responsable du Développement.")], "Noemie proudly states her official executive title"),
    ("justine", "Félicitations pour cette belle promotion rapide!",
     "Congratulations on this fine quick promotion!",
     [(352, "félicitations.")], "Justine offers formal congratulations"),
    ("justine", "Certains disent que tu as été propulsée.",
     "Some people say that you were fast-tracked.",
     [(354, "propulsée")], "Justine hints at hallway gossip about favoritism"),
    ("lea", "Je travaille dur depuis des années.",
     "I have been working hard for years.",
     [(349, "pendant six ans, chez ASK.")], "Noemie defends her credentials and experience"),
    ("mathias", "Bon appétit chérie, passe une bonne journée!",
     "Enjoy your lunch darling, have a good day!",
     [(358, "Bon appétit, chérie !")], "Mathias strolls by and addresses her with intimate affection"),
    ("lea", "Merci monsieur Barneville, bon appétit aussi.",
     "Thank you Mr. Barneville, enjoy your lunch too.",
     [(359, "Merci, monsieur Barneville.")], "Noemie adopts a strictly formal tone in front of coworkers"),
]

OPENER = "Let's explore Noemie and Justine's office conversation line by line."

WALK = [
    (0, None,
     "'Watch out when Vincent speaks at lunchtime.' Justine alerts Noemie about an eccentric coworker in the dining hall. The verb meaning 'pay' pairs naturally with the noun for 'attention' in everyday conversation."),
    (1, None,
     "'Why? What is his problem?' Noemie questions what makes this colleague difficult to talk to. The key noun here means 'problem?', anchored by its matching French article."),
    (2, None,
     "'He has terrible bad breath!' Justine warns her about Vincent's unpleasant breath. Notice how 'has' leads directly into the noun meaning 'breath'."),
    (3, None,
     "'Thank you very much for this warning.' Noemie receives the office tip with good humor. The key noun here means 'thank you', anchored by its matching French article."),
    (4, None,
     "'Between assistants, we must stick together.' Justine expresses mutual solidarity among company assistants. The verb meaning 'is necessary' pairs naturally with the noun for 'assistants' in everyday conversation."),
    (5, None,
     "'But I am no longer an assistant!' Noemie clarifies that her status has fundamentally changed. The key noun here means 'assistant!', anchored by its matching French article."),
    (6, None,
     "'Really? What job do you hold now?' Justine asks about her actual responsibilities in the company. This conversational past tense combines a helper verb with the past participle for 'do you occupy'."),
    (7, None,
     "'I am head of project development.' Noemie announces her promotion to Head of Development. The key noun here means 'head', anchored by its matching French article."),
    (8, None,
     "'Congratulations on this fine quick promotion!' Justine offers polite words while registering the news. The adjective meaning 'fine' takes its feminine form here to match the noun it describes."),
    (9, None,
     "'Some people say that you were fast-tracked.' Justine admits that rumors circulate regarding Mathias's favoritism. The informal 'you' form around 'say' marks a direct, personal relationship."),
    (10, None,
     "'I have been working hard for years.' Noemie reminds her of six intense years proving her skills at ASK. The verb meaning 'have been working' pairs naturally with the noun for 'years.' in everyday conversation."),
    (11, None,
     "'Enjoy your lunch darling, have a good day!' Mathias walks past and uses a pet name in public. Notice how 'have' leads directly into the noun meaning 'appetite'."),
    (12, None,
     "'Thank you Mr. Barneville, enjoy your lunch too.' Noemie quickly responds with formal deference to maintain boundaries. The descriptive adjective for 'good' agrees in gender and number with its noun."),
]

TRANSITION = "Now let's listen to Noemie's workplace exchange once more from start to finish."

OUTRO = ("Noemie navigates new professional responsibilities and office rumors at Mathias's production company. "
         "Let's review the key workplace vocabulary from this scene.")

CLOSING = ("lea", "Merci monsieur Barneville, bon appétit aussi.")
