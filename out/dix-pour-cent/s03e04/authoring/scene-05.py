# Authoring module for dix-pour-cent s03e04 scene 05 (cues 221-255).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-05.py --out out/dix-pour-cent/s03e04/scene-05.json

ID = "dix-pour-cent-s03e04-scene-05"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 5
TITLE = "Affaire de famille  (A Family Matter)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "marcel", "herve": "theo"}
LABELS = {"lea": "Camille", "mathias": "Mathias", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 221-255. Mathias questions Camille about loyalty and trust within the agency, "
               "prompting Camille to check with Herve whether Mathias suspects anything. Adapted for A1 French.")

INTRO = ("At the ASK agency, Mathias Barneville takes his daughter Camille aside to speak about family trust and loyalty. "
         "Feeling uneasy after his questioning, Camille immediately runs to Herve to find out if Mathias knows their secret. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("mathias", "L'agence est ma deuxième famille.",
     "The agency is my second family.",
     [(221, "L'agence, c'est ma deuxième famille.")], "Mathias sets an emotional tone"),
    ("mathias", "Et toi, tu es ma famille ici.",
     "And you are my family here.",
     [(222, "tu es ma famille")], "Mathias underscores their personal bond"),
    ("lea", "Ah oui? Et pourquoi dis-tu ça?",
     "Oh yes? And why do you say that?",
     [(223, "Ah ouais ?"), (225, "pourquoi tu dis ça.")], "Camille senses something unusual"),
    ("mathias", "Je dois pouvoir avoir confiance en toi.",
     "I must be able to trust you.",
     [(232, "confiance en toi.")], "Mathias demands total loyalty"),
    ("lea", "Bien sûr, tu peux avoir confiance.",
     "Of course, you can trust me.",
     [(229, "Bien sûr.")], "Camille offers swift reassurance"),
    ("lea", "Pardon, mais j'ai beaucoup de travail.",
     "Sorry, but I have a lot of work.",
     [(236, "j'ai plein de boulot")], "Camille cuts the meeting short"),
    ("mathias", "Oui, oui, va travailler.",
     "Yes, yes, go to work.",
     [(237, "Oui, oui.")], "Mathias lets her go"),
    ("lea", "Hervé, je crois que mon père se doute.",
     "Herve, I think my father suspects something.",
     [(242, "Je crois qu'il se doute.")], "Camille rushes to Herve's desk"),
    ("herve", "Comment ça? Il t'a dit quoi exactement?",
     "What do you mean? What did he say exactly?",
     [(243, "Il t'a dit quoi, exactement ?")], "Herve asks for specifics"),
    ("lea", "Il m'a parlé de fidélité à l'agence.",
     "He spoke to me about agency loyalty.",
     [(247, "du mal à l'agence.")], "Camille recounts the warning"),
    ("herve", "C'est bon, il ne sait rien.",
     "It is fine, he knows nothing.",
     [(248, "il sait rien.")], "Herve dismisses her fear"),
    ("herve", "Il ne tourne jamais autour du pot.",
     "He never beats around the bush.",
     [(250, "tourner autour du pot.")], "Herve explains Mathias's direct style"),
    ("herve", "C'est un grand parano, ton père!",
     "Your father is a total paranoid!",
     [(254, "C'est un grand parano, ton père.")], "Herve makes light of the situation"),
]

OPENER = "Let's explore how Mathias questions Camille and how Herve reacts line by line."

WALK = [
    (0, None,
     "'The agency is my second family.' Mathias reminds Camille that their professional bond runs very deep. In spoken French, the little word before 'the agency' drops its final vowel and attaches with an apostrophe."),
    (1, None,
     "'And you are my family here.' Mathias emphasizes that their personal relationship is what truly matters. Mathias uses the casual singular 'you' with 'family', showing close familiarity."),
    (2, None,
     "'Oh yes? And why do you say that?' Camille asks why her father suddenly brings up their loyalty. The clause hinges on the everyday verb meaning 'do you say'."),
    (3, None,
     "'I must be able to trust you.' Mathias tests whether Camille is keeping secrets from him. The verb meaning 'must' pairs naturally with the noun for 'trust' in everyday conversation."),
    (4, None,
     "'Of course, you can trust me.' Camille reassures him without revealing Andrea's secret plans. The verb meaning 'can' pairs naturally with the noun for 'trust.' in everyday conversation."),
    (5, None,
     "'Sorry, but I have a lot of work.' Camille makes a quick excuse to escape the tense conversation. Notice how the short vowel drops before a vowel sound around 'I have', making the phrase flow smoothly as one unit."),
    (6, None,
     "'Yes, yes, go to work.' Mathias lets her leave but remains suspicious about the office atmosphere. The clause hinges on the everyday verb meaning 'go'."),
    (7, None,
     "'Herve, I think my father suspects something.' Camille confides her growing anxiety to her close colleague. The reflexive pronoun sits right in front of the verb for 'think', turning the action back onto the subject."),
    (8, None,
     "'What do you mean? What did he say exactly?' Herve asks for specific details about the conversation. In spoken French, the little word before 'has [to] you' drops its final vowel and attaches with an apostrophe."),
    (9, None,
     "'He spoke to me about agency loyalty.' Camille explains Mathias's pointed comments about family and trust. This conversational past tense combines a helper verb with the past participle for 'spoken'."),
    (10, None,
     "'It is fine, he knows nothing.' Herve tries to calm her nerves with pragmatic reassurance. Notice how the short vowel drops before a vowel sound around 'it is', making the phrase flow smoothly as one unit."),
    (11, None,
     "'He never beats around the bush.' Herve points out that Mathias always confronts problems directly. The verb meaning 'turns' pairs naturally with the noun for 'pot.' in everyday conversation."),
    (12, None,
     "'Your father is a total paranoid!' Herve laughs off the encounter as typical senior agent paranoia. The descriptive adjective for 'great' agrees in gender and number with its noun."),
]

TRANSITION = "Now let's listen to the full conversation once more to reinforce the key phrases."

OUTRO = ("Camille manages to dodge Mathias's probing questions, while Herve reassures her about her father's suspicious nature. "
         "Let's review the essential vocabulary from this exchange.")

CLOSING = ("herve", "C'est un grand parano, ton père!")
