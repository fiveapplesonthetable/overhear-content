# Authoring module for dix-pour-cent s04e05 scene 25 (cues 917).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e05/authoring/scene-25.py --out out/dix-pour-cent/s04e05/scene-25.json

ID = "dix-pour-cent-s04e05-scene-25"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 25
TITLE = "Le cœur qui bipe  (The Beeping Heart)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Camille", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cue 917. Preparing to leave the hospital, Mathias wears a heart monitor that beeps during an emotional moment, "
    "prompting him to joke warmly with Camille that he does not beep for just anyone."
)

INTRO = (
    "In his hospital room, Mathias finishes packing his belongings to return home after recovering from his cardiac emergency. "
    "Fitted with a medical monitor to track his heart rate, Mathias shares a tender and humorous moment with Camille. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's look at Mathias and Camille's warm conversation step by step."

STORY = [
    ("lea", "Mathias, tu es prêt à partir?",
     "Mathias, are you ready to leave?",
     [(917, "tout le monde")], "Camille asks gently as he packs his bag"),
    ("mathias", "Oui, les médecins me laissent sortir.",
     "Yes, the doctors are letting me leave.",
     [(917, "tout le monde")], "Mathias smiles with obvious relief"),
    ("lea", "Tu dois porter cet appareil cardiaque?",
     "You have to wear this heart monitor?",
     [(917, "tout le monde")], "Camille inspects the small medical device"),
    ("mathias", "Oui, pour surveiller mon rythme cardiaque.",
     "Yes, to monitor my heart rate.",
     [(917, "tout le monde")], "Explains the doctor's instructions"),
    ("lea", "Je suis si heureuse pour toi.",
     "I am so happy for you.",
     [(917, "tout le monde")], "Expresses her sincere joy"),
    ("mathias", "Écoute, l'appareil sonne déjà doucement!",
     "Listen, the device is already beeping softly!",
     [(917, "bipe")], "Notices the sudden electronic beep"),
    ("lea", "C'est parce que tu es ému!",
     "It is because you are moved!",
     [(917, "tout le monde")], "Camille teases him with a fond smile"),
    ("mathias", "Je ne bipe pas pour tout le monde.",
     "I don't beep for everyone.",
     [(917, "Je ne bipe pas pour tout le monde")], "Mathias jokes about his affection for her"),
    ("lea", "C'est la preuve de ton affection.",
     "It is proof of your affection.",
     [(917, "tout le monde")], "Camille smiles warmly at his playful confession"),
    ("mathias", "Tu comptes beaucoup pour moi, Camille.",
     "You mean a lot to me, Camille.",
     [(917, "tout le monde")], "Mathias speaks with genuine emotion"),
    ("lea", "Promets-moi de faire très attention.",
     "Promise me to be very careful.",
     [(917, "tout le monde")], "Urges him to take care of his health"),
    ("mathias", "Je vais enfin changer mes habitudes.",
     "I will finally change my habits.",
     [(917, "tout le monde")], "Resolves to live a calmer lifestyle"),
    ("lea", "Marchons ensemble vers la sortie maintenant.",
     "Let us walk together toward the exit now.",
     [(917, "tout le monde")], "Leads the way down the hospital corridor"),
    ("mathias", "Merci d'être là avec moi.",
     "Thank you for being here with me.",
     [(917, "tout le monde")], "Expresses heartfelt gratitude to his daughter"),
]

WALK = [
    (0, None,
     "'Mathias, are you ready to leave?' Camille checks if he is prepared to be discharged. Camille uses the casual singular 'you' with 'leave', showing close familiarity."),
    (1, None,
     "'Yes, the doctors are letting me leave.' Mathias confirms that his hospitalization is over. Notice how 'let' leads directly into the noun meaning 'doctors'."),
    (2, None,
     "'You have to wear this heart monitor?' Camille asks about the gadget clipped to his pocket. The descriptive adjective for 'cardiac' agrees in gender and number with its noun."),
    (3, None,
     "'Yes, to monitor my heart rate.' Mathias explains the medical monitoring device. The verb meaning 'monitor' pairs naturally with the noun for 'rhythm' in everyday conversation."),
    (4, None,
     "'I am so happy for you.' Camille celebrates his successful recovery. The informal 'you' form around 'this line' marks a direct, personal relationship."),
    (5, None,
     "'Listen, the device is already beeping softly!' Mathias points out the unexpected sound. Dropping the subject pronoun turns the verb for 'listen' into a direct, punchy command."),
    (6, None,
     "'It is because you are moved!' Camille playfully links his heartbeat to his emotions. A short, idiomatic conversational reply that keeps the exchange moving naturally."),
    (7, None,
     "'I don't beep for everyone.' Mathias delivers his charmingly self-deprecating line. The clause hinges on the everyday verb meaning 'beep'."),
    (8, None,
     "'It is proof of your affection.' Camille highlights the emotional significance of the moment. Camille uses the casual singular 'you' with 'proof', showing close familiarity."),
    (9, None,
     "'You mean a lot to me, Camille.' Mathias openly confesses his paternal attachment. The informal 'you' form around 'count' marks a direct, personal relationship."),
    (10, None,
     "'Promise me to be very careful.' Camille asks him to look after his well-being. Notice how 'promise me' leads directly into the noun meaning 'attention'."),
    (11, None,
     "'I will finally change my habits.' Mathias commits to abandoning his stressful routine. French forms the near future by pairing the present tense of 'to go' directly with 'change'."),
    (12, None,
     "'Let us walk together toward the exit now.' Camille guides him out of the hospital ward. Notice how 'let us walk' leads directly into the noun meaning 'exit'."),
    (13, None,
     "'Thank you for being here with me.' Mathias thanks her for standing faithfully by his side."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Leaving the hospital after his cardiac episode, Mathias shares a touching moment with Camille as his heart monitor beeps with emotional warmth, marking a new chapter in their relationship. When you watch the episode, listen out for the expressions meaning 'ready' and 'leave'. You'll catch them now. See you next time."
CLOSING = ("mathias", "Je ne bipe pas pour tout le monde.")
