# Authoring module for dix-pour-cent s04e02 scene 25 (cues 1104-1106).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e02/authoring/scene-25.py --out out/dix-pour-cent/s04e02/scene-25.json

ID = "dix-pour-cent-s04e02-scene-25"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 25
TITLE = "Le départ de Gabriel  (Gabriel's Departure)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "camille": "emilie"}
LABELS = {"lea": "Sofia", "camille": "Camille"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1104-1106. Camille gently reveals that Gabriel has just left with Sarah. "
    "Sofia hides her heartbreak with polite words, wishing Camille good night before slipping into the Paris evening."
)

INTRO = (
    "In the quiet agency hall, Camille breaks the news to Sofia that Gabriel has just left with Sarah. Sofia hides her heartbreak behind polite smiles as the night closes. Let's listen to the scene in French first."
)

STORY = [
    ("camille", "Il vient de partir avec Sarah.",
     "He just left with Sarah.",
     [(1104, "vient de partir avec Sarah")], "Camille speaks gently to Sofia"),
    ("camille", "Ils sont allés à Saint-Ouen ensemble.",
     "They went to Saint-Ouen together.",
     [(1104, "vient de partir avec Sarah")], ""),
    ("camille", "Il ne t'a pas prévenue?",
     "Didn't he tell you?",
     [(1104, "pas dit au revoir")], "Camille looks concerned"),
    ("camille", "Il n'a pas dit au revoir?",
     "Didn't he say goodbye?",
     [(1104, "pas dit au revoir")], ""),
    ("lea", "Bien sûr, bien sûr, c'est normal.",
     "Of course, of course, that is normal.",
     [(1105, "Bien sûr, bien sûr")], "Sofia forces a brave smile"),
    ("lea", "Il a le droit de sortir.",
     "He has the right to go out.",
     [(1105, "Bien sûr, bien sûr")], ""),
    ("camille", "Tu as l'air un peu triste.",
     "You look a little sad.",
     [(1105, "Bien sûr, bien sûr")], "Camille notices the sudden sadness in her eyes"),
    ("lea", "Non, tout va très bien, merci.",
     "No, everything is very fine, thank you.",
     [(1105, "Bien sûr, bien sûr")], "Shakes her head bravely"),
    ("lea", "Je suis heureuse pour lui.",
     "I am happy for him.",
     [(1105, "Bien sûr, bien sûr")], ""),
    ("camille", "Tu veux boire un verre ensemble?",
     "Do you want to have a drink together?",
     [(1105, "Bien sûr, bien sûr")], "Offers friendly comfort"),
    ("lea", "Non, je vais rentrer chez moi.",
     "No, I am going to go home.",
     [(1105, "Bien sûr, bien sûr")], "Declines with a polite nod"),
    ("lea", "La journée a été très longue.",
     "The day was very long.",
     [(1105, "Bien sûr, bien sûr")], ""),
    ("camille", "Prends bien soin de toi, Sofia.",
     "Take good care of yourself, Sofia.",
     [(1105, "Bien sûr, bien sûr")], "Camille squeezes her hand gently"),
    ("lea", "Bonne nuit, Camille, à bientôt.",
     "Good night, Camille, see you soon.",
     [(1105, "Bien sûr, bien sûr")], "Sofia turns and walks out into the Paris night"),
]

OPENER = "Let's examine how Sofia reacts to the painful news of Gabriel's departure line by line."

WALK = [
    (0, None,
     "'He just left with Sarah.' Camille reveals that Gabriel departed in company. The clause hinges on the everyday verb meaning 'comes'."),
    (1, None,
     "'They went to Saint-Ouen together.' Camille explains their destination for the night. This conversational past tense combines a helper verb with the past participle for 'gone'."),
    (2, None,
     "'Didn't he tell you?' Camille asks if Sofia received any advance message. The clause hinges on the everyday verb meaning 'has'."),
    (3, None,
     "'Didn't he say goodbye?' Camille wonders whether Gabriel bid Sofia farewell. In everyday spoken French, rising intonation on 'has' at the end is enough to turn the sentence into a question."),
    (4, None,
     "'Of course, of course, that is normal.' Sofia tries bravely to downplay her feelings. A short, idiomatic conversational reply that keeps the exchange moving naturally."),
    (5, None,
     "'He has the right to go out.' Sofia acknowledges his freedom to live his life. The verb meaning 'has' pairs naturally with the noun for 'right' in everyday conversation."),
    (6, None,
     "'You look a little sad.' Camille notices the sudden disappointment on her face. The descriptive adjective for 'sad' agrees in gender and number with its noun."),
    (7, None,
     "'No, everything is very fine, thank you.' Sofia insists that she is unaffected. The clause hinges on the everyday verb meaning 'goes'."),
    (8, None,
     "'I am happy for him.' Sofia offers generous words despite her inner hurt. A short, idiomatic conversational reply that keeps the exchange moving naturally."),
    (9, None,
     "'Do you want to have a drink together?' Camille gently offers friendly company. The verb meaning 'want' pairs naturally with the noun for 'drink' in everyday conversation."),
    (10, None,
     "'No, I am going to go home.' Sofia declines, preferring solitude. The clause hinges on the everyday verb meaning 'am going'."),
    (11, None,
     "'The day was very long.' Sofia excuses herself due to exhaustion. The verb meaning 'has' pairs naturally with the noun for 'day' in everyday conversation."),
    (12, None,
     "'Take good care of yourself, Sofia.' Camille offers warm and sympathetic support. The informal 'you' form around 'take' marks a direct, personal relationship."),
    (13, None,
     "'Good night, Camille, see you soon.' Sofia bids farewell before slipping into the night."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Confronted with the reality that Gabriel has moved on with Sarah, Sofia masks her sorrow with quiet dignity and heads home alone into the Paris night as the episode concludes. When you watch the episode, listen out for the expressions meaning 'comes' and 'leave'. You'll catch them now. See you next time."
CLOSING = ("lea", "Bien sûr, bien sûr, c'est normal.")
