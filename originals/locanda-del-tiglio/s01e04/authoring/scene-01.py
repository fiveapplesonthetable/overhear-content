# Authoring module for locanda-del-tiglio-s01e04-scene-01.
ID = 'locanda-del-tiglio-s01e04-scene-01'
SHOW = 'locanda-del-tiglio'
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = 'Le sei e quarantacinque  (Six Forty-Five)'
LEVEL = 'A1 — beginner'
PAIR = 'it-en'
LABELS = {'bruno': 'Bruno', 'chiara': 'Chiara'}
INTRO = 'It is six forty-five in the morning at the Locanda del Tiglio in Bologna. While the guests still sleep upstairs, Bruno sketches a quick street map on paper for Chiara. Listen to the whole scene first.'
OPENER = "Let's trace Bruno's street directions step by step."
TRANSITION = "Now let's listen to the whole dawn scene again from start to finish."
OUTRO = 'Left at the gate, across the bridge, past the green pharmacy, and left into the square—Chiara is off on her dawn mission. See you next time.'
CLOSING = ('chiara', 'A presto!')
STORY = [
    ('chiara', 'Buongiorno, Bruno! Le docce di sopra sono già davvero fredde?', 'Good morning, Bruno! Are the showers upstairs really cold already?'),
    ('bruno', "Fredde come l'acqua del fiume. Metti questa valvola rotta nella tasca del cappotto.", 'Cold as river water. Take this broken brass valve in your coat pocket.'),
    ('chiara', 'Presa. Ora dimmi come trovare la ferramenta.', 'Got it. Now tell me how to find the hardware shop.'),
    ('bruno', 'Gira a sinistra fuori dal cancello e vai dritto fino al ponte di pietra.', 'Turn left outside our gate and walk straight to the stone bridge.'),
    ('chiara', 'A sinistra al cancello, dritto fino al ponte. Attraverso il fiume?', 'Left at the gate, straight to the bridge. Do I cross the river?'),
    ('bruno', 'Sì, attraversa il ponte, poi supera la farmacia verde a destra.', 'Yes, cross the bridge, then pass the green pharmacy on your right.'),
    ('chiara', 'Ponte, poi farmacia verde a destra. E dopo?', 'Bridge, then green pharmacy on the right. And after that?'),
    ('bruno', 'Gira a sinistra nella piazzetta. Cerca una porta di legno blu.', 'Turn left into the small square. Look for a blue wooden door.'),
    ('chiara', 'Il negozio ha una grande insegna fuori?', 'Does the shop have a big sign outside?'),
    ('bruno', 'Solo una chiave dorata dipinta sopra la porta. Mostra questa valvola al commesso.', 'Only a painted golden key above the door. Show the clerk this valve.'),
    ('chiara', 'Venti millimetri, ottone, valvola per caldaia: lo ripeto per tutta la strada!', 'Twenty millimetres, brass, boiler valve—I will repeat it all the way!'),
    ('bruno', 'Corri veloce, Chiara. La camera quattro si sveglia alle sette e un quarto!', 'Run fast, Chiara. Room four wakes up at seven fifteen!'),
]
WALK = [
    (0, None, "'Good morning, Bruno! Are the showers upstairs really cold already?' In Italian, upstairs—literally of above—sits right after showers to specify which ones."),
    (1, None, ["'Cold as river water. Take this broken brass valve in your coat pocket.' Broken sits right after valve.", (None, 'Questa valvola rotta'), 'Ending in a to match the feminine valve.']),
    (2, None, ["'Got it. Now tell me how to find the hardware shop.' One crisp word says got it when someone hands you a feminine object.", (None, 'Presa.'), 'Literally taken—ending in a because valve is feminine!']),
    (3, None, ["'Turn left outside our gate and walk straight to the stone bridge.' Every walker in Bologna uses this handy phrase for directions.", (None, 'Gira a sinistra'), 'Literally turn to left first, and then go straight all the way to the bridge.']),
    (4, None, ["'Left at the gate, straight to the bridge. Do I cross the river?' Chiara checks the route using the plain present.", (None, 'Attraverso il fiume?'), 'In Italian, asking do I cross needs no helper word—just I cross with a rising voice.']),
    (5, None, ["'Yes, cross the bridge, then pass the green pharmacy on your right.' Hear how the command form shifts its final vowel.", (None, 'Attraversa il ponte'), "Changing final o to a in Italian turns Chiara's question into Bruno's instruction."]),
    (6, None, ["'Bridge, then green pharmacy on the right. And after that?' Two crisp words keep directions flowing.", (None, 'E dopo?'), 'Literally and after—your easiest prompt whenever someone gives you street directions.']),
    (7, None, ["'Turn left into the small square. Look for a blue wooden door.' Square takes an affectionate diminutive ending.", (None, 'Nella piazzetta.'), 'Turning a grand city square into an intimate neighbourhood little square.']),
    (8, None, ["'Does the shop have a big sign outside?' Italian uses a dedicated word for a shop sign hanging over a doorway.", (None, 'Una grande insegna'), 'Unlike English, that word is distinct from a paper notice or a street sign.']),
    (9, None, ["'Only a painted golden key above the door. Show the clerk this valve.' Meet the everyday word for a shop assistant.", (None, 'Al commesso.'), 'Ending in o for a man behind the counter and a for a woman.']),
    (10, None, "'Twenty millimetres, brass, boiler valve—I will repeat it all the way!' Repeating her three-item checklist out loud keeps every detail sharp while she runs."),
    (11, None, ["'Run fast, Chiara. Room four wakes up at seven fifteen!' Look at how quarter past seven is built.", (None, 'Alle sette e un quarto!'), 'Literally at the seven and a quarter.']),
]
