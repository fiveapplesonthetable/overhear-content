# Authoring module for dix-pour-cent s04e04 scene 28 (cues 1285-1287).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e04/authoring/scene-28.py --out out/dix-pour-cent/s04e04/scene-28.json

ID = "dix-pour-cent-s04e04-scene-28"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 28
TITLE = "Course vers l'hôpital  (Race to the Hospital)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "noemie": "emilie"}
LABELS = {"lea": "Camille", "noemie": "Noémie"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1285-1287. Out on the busy Paris street, Camille and Noemie desperately try to hail a taxi to reach "
    "the hospital where Mathias is fighting for his life after a heart attack."
)

INTRO = (
    "Rushing out of the cafe into the bustling Parisian streets, Camille and Noemie look anxiously for an available cab. "
    "Terrified for Mathias's life, the two women put aside all past grievances as they scramble to reach the hospital emergency room. "
    "Let's listen to the scene in French first."
)

OPENER = "Let's examine Camille and Noemie's urgent search for a taxi line by line."

STORY = [
    ("lea", "Taxi! Arrêtez-vous ici, s'il vous plaît!",
     "Taxi! Stop here, please!",
     [(1285, "Taxi !")], "Camille waves desperately at a passing vehicle"),
    ("noemie", "Taxi! Nous sommes très pressées!",
     "Taxi! We are in a great hurry!",
     [(1286, "Taxi !")], "Noemie shouts toward the busy boulevard"),
    ("lea", "Cette voiture passe sans ralentir.",
     "This car passes without slowing down.",
     [(1285, "Taxi !")], "Camille sighs as the first cab speeds past"),
    ("noemie", "Nous devons trouver une autre voiture.",
     "We must find another car.",
     [(1286, "Taxi !")], "Noemie scans the oncoming street traffic"),
    ("lea", "Mathias est en danger à l'hôpital.",
     "Mathias is in danger at the hospital.",
     [(1285, "Taxi !")], "Camille fears for her father's survival"),
    ("noemie", "J'ai tellement peur pour sa vie.",
     "I am so afraid for his life.",
     [(1286, "Taxi !")], "Noemie holds back tears of anxiety"),
    ("lea", "Garde ton calme avec moi, Noémie.",
     "Keep your calm with me, Noemie.",
     [(1285, "Taxi !")], "Camille reassures her trembling companion"),
    ("noemie", "Je ne veux pas le perdre.",
     "I do not want to lose him.",
     [(1286, "Taxi !")], "Confesses how much she still loves him"),
    ("lea", "Regarde là-bas, un taxi arrive enfin!",
     "Look over there, a taxi is finally arriving!",
     [(1285, "Taxi !")], "Camille spots an illuminated taxi roof sign"),
    ("noemie", "Chauffeur, allez vite à l'hôpital!",
     "Driver, go quickly to the hospital!",
     [(1286, "Taxi !")], "Noemie calls out as the vehicle pulls over"),
    ("lea", "Montons ensemble dans le taxi maintenant.",
     "Let us get into the taxi together now.",
     [(1285, "Taxi !")], "Camille opens the rear passenger door"),
    ("noemie", "Mathias va s'en sortir, j'espère.",
     "Mathias will pull through, I hope.",
     [(1286, "Taxi !")], "Noemie clings to hope in the back seat"),
    ("lea", "Nous serons bientôt avec lui.",
     "We will be with him soon.",
     [(1285, "Taxi !")], "Camille offers steady reassurance"),
    ("noemie", "Courage, arrivons vite à l'hôpital!",
     "Courage, let us arrive quickly at the hospital!",
     [(1286, "Taxi !")], "Noemie urges the driver into traffic"),
]

WALK = [
    (0, None,
     "'Taxi! Stop here, please!' Camille flags down a passing cab on the avenue. Notice how 'stop' leads directly into the noun meaning 'taxi'."),
    (1, None,
     "'Taxi! We are in a great hurry!' Noemie cries out to signal the urgency of their trip. The key noun here means 'taxi', anchored by its matching French article."),
    (2, None,
     "'This car passes without slowing down.' Camille laments that the driver ignored them. The verb meaning 'passes' pairs naturally with the noun for 'car' in everyday conversation."),
    (3, None,
     "'We must find another car.' Noemie looks around frantically for another ride. The verb meaning 'must' pairs naturally with the noun for 'car' in everyday conversation."),
    (4, None,
     "'Mathias is in danger at the hospital.' Camille acknowledges the gravity of his situation. The key noun here means 'danger', anchored by its matching French article."),
    (5, None,
     "'I am so afraid for his life.' Noemie reveals her overwhelming dread. Notice how 'have' leads directly into the noun meaning 'fear'."),
    (6, None,
     "'Keep your calm with me, Noemie.' Camille tries to keep her companion grounded. The verb meaning 'keep' pairs naturally with the noun for 'calm' in everyday conversation."),
    (7, None,
     "'I do not want to lose him.' Noemie admits her profound affection for Mathias. The clause hinges on the everyday verb meaning 'want'."),
    (8, None,
     "'Look over there, a taxi is finally arriving!' Camille notices a cab with an illuminated light. Dropping the subject pronoun turns the verb for 'look' into a direct, punchy command."),
    (9, None,
     "'Driver, go quickly to the hospital!' Noemie shouts their critical destination. The verb meaning 'go' pairs naturally with the noun for 'driver' in everyday conversation."),
    (10, None,
     "'Let us get into the taxi together now.' Camille gestures into the passenger seat. The verb meaning 'let us get into' pairs naturally with the noun for 'taxi' in everyday conversation."),
    (11, None,
     "'Mathias will pull through, I hope.' Noemie prays for his recovery. The clause hinges on the everyday verb meaning 'is going to'."),
    (12, None,
     "'We will be with him soon.' Camille comforts her as the journey begins. The clause hinges on the everyday verb meaning 'will be'."),
    (13, None,
     "'Courage, let us arrive quickly at the hospital!' Noemie urges haste as they race through the streets."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Terrified by the news of Mathias's heart attack, Camille and Noemie flag down a taxi in the street and race to the hospital, determined to support him in his battle to survive. When you watch the episode, listen out for the expressions meaning 'taxi' and 'stop'. You'll catch them now. See you next time."
CLOSING = ("lea", "Taxi! Arrêtez-vous ici, s'il vous plaît!")
