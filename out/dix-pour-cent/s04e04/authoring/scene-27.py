# Authoring module for dix-pour-cent s04e04 scene 27 (cues 1239-1284).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e04/authoring/scene-27.py --out out/dix-pour-cent/s04e04/scene-27.json

ID = "dix-pour-cent-s04e04-scene-27"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 27
TITLE = "Une terrible nouvelle  (Terrible News)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "noemie": "emilie"}
LABELS = {"lea": "Camille", "noemie": "Noémie"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1239-1284. Over coffee at a Parisian bistro, Camille and Noemie vent their deep frustration at Mathias's "
    "lies and mockingly compare him to Jafar. Their laughter is abruptly cut short when a phone call from the hospital "
    "announces that Mathias has suffered a severe heart attack."
)

INTRO = (
    "In a Parisian cafe, Camille and Noemie share hot coffees while commiserating over their complicated relationships with Mathias. "
    "Mocking his sinister demeanor, the two women laugh about how much he resembles the villain Jafar, until an alarming phone call changes everything. "
    "Let's listen to the scene in French first."
)

OPENER = "Let's examine the dramatic turn of events line by line."

STORY = [
    ("noemie", "Mathias m'a menti en face hier.",
     "Mathias lied to my face yesterday.",
     [(1246, "Il m'a menti en face")], "Noemie fumes over his dishonest behavior"),
    ("lea", "Pour moi aussi, tout est terminé.",
     "For me too, everything is finished.",
     [(1247, "c'est terminé")], "Camille declares that she is done with him"),
    ("lea", "Je refuse sa reconnaissance de paternité.",
     "I refuse his recognition of paternity.",
     [(1253, "reconnaissance de paternité")], "Rejects his belated legal claim"),
    ("noemie", "Tu as raison de le rejeter.",
     "You are right to reject him.",
     [(1255, "T'as raison")], "Noemie supports her decision firmly"),
    ("lea", "Il ressemble vraiment au méchant Jafar!",
     "He truly looks like the villain Jafar!",
     [(1255, "il ressemble vraiment à Jafar")], "Camille laughs at his villainous aura"),
    ("noemie", "Il a déjà le regard traître!",
     "He already has the treacherous look!",
     [(1258, "Il a déjà le regard traître")], "Noemie points out his deceitful expression"),
    ("lea", "Ne le laissons plus rien gâcher.",
     "Let us not let him ruin anything anymore.",
     [(1262, "On ne le laisse pas gâcher")], "Resolves to protect their peace of mind"),
    ("noemie", "Attends, mon téléphone sonne sans arrêt.",
     "Wait, my phone is ringing without stopping.",
     [(1265, "Attends")], "Noemie notices a persistent incoming call"),
    ("noemie", "Allô? J'arrive tout de suite!",
     "Hello? I am coming right away!",
     [(1274, "J'arrive tout de suite")], "Answers the mysterious caller urgently"),
    ("lea", "Noémie, qu'est-ce qui se passe?",
     "Noemie, what is going on?",
     [(1277, "qu'est-ce qui se passe")], "Camille asks with growing concern"),
    ("noemie", "C'est Mathias, il est à l'hôpital!",
     "It is Mathias, he is at the hospital!",
     [(1280, "C'est Mathias"), (1281, "Il est à l'hôpital")], "Noemie announces in utter shock"),
    ("noemie", "Il a eu une crise cardiaque!",
     "He had a heart attack!",
     [(1281, "crise cardiaque")], "Reveals the terrifying medical emergency"),
    ("lea", "Mon Dieu, c'est une catastrophe!",
     "My God, this is a disaster!",
     [(1284, "Mon Dieu")], "Camille gasps in horror"),
    ("noemie", "Vite, on doit prendre un taxi!",
     "Quick, we must take a taxi!",
     [(1283, "On doit prendre un taxi")], "Urges Camille to leave immediately"),
]

WALK = [
    (0, None,
     "'Mathias lied to my face yesterday.' Noemie complains about his deceitful behavior. This conversational past tense combines a helper verb with the past participle for 'lied'."),
    (1, None,
     "'For me too, everything is finished.' Camille confirms that she has cut ties with him. The descriptive adjective for 'finished' agrees in gender and number with its noun."),
    (2, None,
     "'I refuse his recognition of paternity.' Camille stands firm against his paternal paperwork. Notice how 'refuse' leads directly into the noun meaning 'recognition'."),
    (3, None,
     "'You are right to reject him.' Noemie validates her strong stance. Noemie uses the casual singular 'you' with 'have', showing close familiarity."),
    (4, None,
     "'He truly looks like the villain Jafar!' Camille finds humor in his cartoonish villainy. Notice how 'looks like' leads directly into the noun meaning 'villain'."),
    (5, None,
     "'He already has the treacherous look!' Noemie jokes about his sly expression. Notice how 'has' leads directly into the noun meaning 'look'."),
    (6, None,
     "'Let us not let him ruin anything anymore.' Camille decides not to let bitterness control them. The clause hinges on the everyday verb meaning 'let'."),
    (7, None,
     "'Wait, my phone is ringing without stopping.' Noemie hears her mobile ring with a masked number. The verb meaning 'wait' pairs naturally with the noun for 'phone' in everyday conversation."),
    (8, None,
     "'Hello? I am coming right away!' Noemie speaks to the caller with sudden urgency. The clause hinges on the everyday verb meaning 'am coming'."),
    (9, None,
     "'Noemie, what is going on?' Camille notices the sudden panic in her friend's eyes. The clause hinges on the everyday verb meaning 'is happening'."),
    (10, None,
     "'It is Mathias, he is at the hospital!' Noemie delivers the startling announcement. The key noun here means 'hospital', anchored by its matching French article."),
    (11, None,
     "'He had a heart attack!' Noemie shares the shocking severity of his condition. This conversational past tense combines a helper verb with the past participle for 'had'."),
    (12, None,
     "'My God, this is a disaster!' Camille reacts with profound shock and fear. The key noun here means 'catastrophe', anchored by its matching French article."),
    (13, None,
     "'Quick, we must take a taxi!' Noemie demands that they hurry to his hospital room."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "After spending the morning venting their resentment toward Mathias, Camille and Noemie are thrown into sudden panic when a hospital call reveals that he has suffered a major heart attack. When you watch the episode, listen out for the expressions meaning 'lied' and 'face'. You'll catch them now. See you next time."
CLOSING = ("noemie", "C'est Mathias, il est à l'hôpital!")
