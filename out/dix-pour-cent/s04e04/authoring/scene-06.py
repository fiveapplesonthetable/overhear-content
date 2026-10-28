# Authoring module for dix-pour-cent s04e04 scene 06 (cues 449-468).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e04/authoring/scene-06.py --out overhear-content/out/dix-pour-cent/s04e04/scene-06.json

ID = "dix-pour-cent-s04e04-scene-06"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 6
TITLE = "Le débriefing de Camille  (Camille's Debrief)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo"}
LABELS = {"lea": "Camille", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 449-468. Returning to her desk after a mysterious business lunch, Camille is grilled by an inquisitive Hervé. "
    "She pulls a deadpan prank about a scandalous romance before laughing it off and taking a well-earned nap."
)

INTRO = (
    "Returning to her desk after a confidential business lunch, Camille is immediately questioned by Herve. "
    "To tease her nosy colleague, Camille pretends the meal ended in a wild romantic encounter. "
    "Let's listen to their playful banter in French first."
)

OPENER = "Let's explore Camille and Herve's entertaining exchange line by line."
TRANSITION = "Now let's listen to Camille and Herve's full conversation once again from start to finish."

STORY = [
    ("herve", "Alors, tu as passé un bon moment?",
     "So, did you have a good time?",
     [(449, "T'as passé un bon moment ?")], "Hervé eagerly grills Camille about her lunch"),
    ("lea", "Oui, notre déjeuner était vraiment super.",
     "Yes, our lunch was really great.",
     [(450, "Super.")], "Camille smiles warmly about the meeting"),
    ("herve", "Il voulait te parler de quoi?",
     "What did he want to talk to you about?",
     [(451, "Il voulait quoi ?")], "Hervé probes for hidden motives"),
    ("lea", "Il voulait apprendre à me connaître.",
     "He wanted to get to know me.",
     [(453, "mieux se connaître")], "Camille recounts their general conversation"),
    ("herve", "Rien de plus professionnel ou secret?",
     "Nothing more professional or secret?",
     [(458, "C'est tout ?")], "Hervé suspects deeper agency intrigue"),
    ("lea", "Il apprécie beaucoup ma franchise directe.",
     "He really appreciates my direct frankness.",
     [(454, "ma franchise")], "Camille highlights his positive reaction"),
    ("herve", "Et après, que s'est-il passé?",
     "And afterwards, what happened?",
     [(459, "après ça")], "Hervé leans in for spicy office gossip"),
    ("lea", "Nous avons fini dans les toilettes!",
     "We ended up in the restrooms!",
     [(461, "aux toilettes")], "Camille delivers an outrageous deadpan prank"),
    ("herve", "Quoi? Ce n'est pas possible!",
     "What? That is not possible!",
     [(462, "je rigole !")], "Hervé is genuinely horrified and stunned"),
    ("lea", "Regarde ta tête, je rigole seulement!",
     "Look at your face, I am only joking!",
     [(462, "je rigole !")], "Camille bursts out laughing at his face"),
    ("herve", "Tu m'as fait tellement peur!",
     "You scared me so much!",
     [(463, "en vrai")], "Hervé breathes a huge sigh of relief"),
    ("lea", "Il écoute simplement mes avis utiles.",
     "He simply listens to my useful advice.",
     [(464, "mon avis")], "Camille shares the sincere truth"),
    ("herve", "C'est une excellente nouvelle pour toi.",
     "That is excellent news for you.",
     [(465, "aussi simple que ça")], "Hervé congratulates her professional growth"),
    ("lea", "Maintenant, je fais une petite sieste!",
     "Now, I am taking a short nap!",
     [(466, "Micro-sieste")], "Camille rests her head on her desk"),
]

WALK = [
    (0, None,
     "'So, did you have a good time?' Herve eagerly questions Camille about her lunch. The informal 'you' form around 'have' marks a direct, personal relationship."),
    (1, None,
     "'Yes, our lunch was really great.' Camille happily confirms the success of the meeting. The verb meaning 'was' pairs naturally with the noun for 'lunch' in everyday conversation."),
    (2, None,
     "'What did he want to talk to you about?' Herve fishes for confidential business details. The reflexive pronoun sits right in front of the verb for 'wanted', turning the action back onto the subject."),
    (3, None,
     "'He wanted to get to know me.' Camille describes their casual introductory conversation. The clause hinges on the everyday verb meaning 'wanted'."),
    (4, None,
     "'Nothing more professional or secret?' Herve suspects that he is hiding deeper agency politics. The descriptive adjective for 'professional' agrees in gender and number with its noun."),
    (5, None,
     "'He really appreciates my direct frankness.' Camille highlights his praise for her honesty. The adjective meaning 'direct.' takes its feminine form here to match the noun it describes."),
    (6, None,
     "'And afterwards, what happened?' Herve leans in expecting juicy romantic gossip. This conversational past tense combines a helper verb with the past participle for 'happened?'."),
    (7, None,
     "'We ended up in the restrooms!' Camille deadpans an outrageous scandalous lie. The verb meaning 'have' pairs naturally with the noun for 'restrooms!' in everyday conversation."),
    (8, None,
     "'What? That is not possible!' Herve reacts with absolute shock and horror. The descriptive adjective for 'possible!' agrees in gender and number with its noun."),
    (9, None,
     "'Look at your face, I am only joking!' Camille bursts into laughter at his gullible reaction. The informal 'you' form around 'look at' marks a direct, personal relationship."),
    (10, None,
     "'You scared me so much!' Herve breathes a sigh of relief after the joke. Herve uses the casual singular 'you' with 'have', showing close familiarity."),
    (11, None,
     "'He simply listens to my useful advice.' Camille reveals that he truly values her perspective. Notice how 'listens to' leads directly into the noun meaning 'opinions'."),
    (12, None,
     "'That is excellent news for you.' Herve congratulates her on earning his genuine respect. The adjective meaning 'excellent' takes its feminine form here to match the noun it describes."),
    (13, None,
     "'Now, I am taking a short nap!' Camille rests her head on her desk to recharge. The adjective meaning 'little' takes its feminine form here to match the noun it describes."),
]

OUTRO = (
    "After playfully teasing Herve with an outrageous prank, Camille revels in her growing professional standing and settles down for a quick power nap. "
    "Let's review the key vocabulary from this scene."
)

CLOSING = ("lea", "Maintenant, je fais une petite sieste!")
