# Authoring module for linden-courtyard-it-s01e04-scene-01.
ID = "linden-courtyard-it-s01e04-scene-01"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = "Six Forty-Five  (Le sei e quarantacinque)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"graham": "Graham", "hannah": "Hannah"}
INTRO = "Sono le sei e quarantacinque del mattino alla Locanda del Cortile del Tiglio, a Portland. Mentre gli ospiti dormono ancora di sopra, Graham disegna su un foglio una mappa veloce delle strade per Hannah. Ascolta prima tutta la scena."
OPENER = "Vediamo passo dopo passo le indicazioni stradali di questa corsa all'alba."
TRANSITION = "Ora riascolta l'intera scena tutta d'un fiato."
OUTRO = "A sinistra fuori dal cancello, dritto fino al ponte di pietra, oltre la farmacia verde e poi nella piazzetta: Hannah è già partita di corsa. A presto."
CLOSING = ("hannah", "See you soon!")
STORY = [
    ("hannah", "Good morning, Graham! Are the showers upstairs really cold already?", "Buongiorno, Graham! Le docce di sopra sono davvero già fredde?"),
    ("graham", "Cold as river water. Take this broken brass valve in your coat pocket.", "Fredde come acqua di fiume. Prendi questa valvola d'ottone rotta nella tasca del cappotto."),
    ("hannah", "Got it. Now tell me how to find the hardware shop.", "Presa. Ora dimmi come trovare la ferramenta."),
    ("graham", "Turn left outside our gate and walk straight to the stone bridge.", "Gira a sinistra fuori dal nostro cancello e cammina dritto fino al ponte di pietra."),
    ("hannah", "Left at the gate, straight to the bridge. Do I cross the river?", "A sinistra al cancello, dritto fino al ponte. Attraverso il fiume?"),
    ("graham", "Yes, cross the bridge, then pass the green pharmacy on your right.", "Sì, attraversa il ponte, poi supera la farmacia verde sulla destra."),
    ("hannah", "Bridge, then green pharmacy on the right. And after that?", "Ponte, poi farmacia verde a destra. E dopo di quello?"),
    ("graham", "Turn left into the small square. Look for a blue wooden door.", "Gira a sinistra entrando nella piazzetta. Cerca una porta di legno blu."),
    ("hannah", "Does the shop have a big sign outside?", "Il negozio ha una grande insegna fuori?"),
    ("graham", "Only a painted golden key above the door. Show the clerk this valve.", "Solo una chiave dorata dipinta sopra la porta. Mostra al commesso questa valvola."),
    ("hannah", "Twenty millimeters, brass, boiler valve. I will repeat it all the way!", "Venti millimetri, ottone, valvola della caldaia. Lo ripeterò per tutta la strada!"),
    ("graham", "Run fast, Hannah. Room four wakes up at seven fifteen!", "Corri veloce, Hannah. La camera quattro si sveglia alle sette e quindici!"),
]
WALK = [
    (0, None, ["'Buongiorno, Graham! Le docce di sopra sono davvero già fredde?' Nella domanda con il verbo essere,", (None, "Are the showers"), "inverte verbo e soggetto, mentre", (None, "upstairs"), "dice di sopra in una sola parola."]),
    (1, None, ["'Fredde come acqua di fiume. Prendi questa valvola d'ottone rotta nella tasca del cappotto.' Guarda la catena di nomi in", (None, "broken brass valve"), "e in", (None, "coat pocket"), "dove il materiale e il contenitore precedono sempre il nome principale."]),
    (2, None, ["'Presa. Ora dimmi come trovare la ferramenta.' Per dire ho capito o ce l'ho nel parlato rapido basta", (None, "Got it"), "mentre il negozio di utensili e ricambi si chiama", (None, "hardware shop"), "ferramenta."]),
    (3, None, ["'Gira a sinistra fuori dal nostro cancello e cammina dritto fino al ponte di pietra.' Le due espressioni cardine per dare indicazioni a piedi sono", (None, "Turn left"), "gira a sinistra e", (None, "walk straight"), "cammina dritto."]),
    (4, None, ["'A sinistra al cancello, dritto fino al ponte. Attraverso il fiume?' Quando chiedi conferma su una mossa da fare subito usi il presente con l'ausiliare in", (None, "Do I cross"), "attraverso io."]),
    (5, None, ["'Sì, attraversa il ponte, poi supera la farmacia verde sulla destra.' Per indicare il lato lungo cui trovi un edificio l'inglese usa la preposizione di contatto in", (None, "on your right"), "sulla tua destra."]),
    (6, None, ["'Ponte, poi farmacia verde a destra. E dopo di quello?' Per chiedere il passaggio successivo di un percorso è utilissima la domanda breve", (None, "And after that?"), "e dopo di ciò."]),
    (7, None, ["'Gira a sinistra entrando nella piazzetta. Cerca una porta di legno blu.' Nota", (None, "into"), "che esprime il movimento verso l'interno della piazza, e il verbo fisso", (None, "Look for"), "cercare con gli occhi."]),
    (8, None, ["'Il negozio ha una grande insegna fuori?' Alla terza persona singolare la domanda con avere richiede l'ausiliare in", (None, "Does the shop have"), "lasciando il verbo principale alla forma base."]),
    (9, None, ["'Solo una chiave dorata dipinta sopra la porta. Mostra al commesso questa valvola.' Con", (None, "above the door"), "indichi qualcosa appeso più in alto senza contatto diretto, e in", (None, "Show the clerk"), "il destinatario precede l'oggetto senza preposizione."]),
    (10, None, ["'Venti millimetri, ottone, valvola della caldaia. Lo ripeterò per tutta la strada!' Una promessa decisa sul momento si forma con", (None, "I will repeat"), "seguito da", (None, "all the way"), "per tutto il tragitto."]),
    (11, None, ["'Corri veloce, Hannah. La camera quattro si sveglia alle sette e quindici!' Il verbo", (None, "wakes up"), "unisce l'azione di svegliarsi alla particella che esprime il passaggio al pieno risveglio."]),
]
CALLOUT_TRANS = {
    "Are the showers": "sono le docce",
    "upstairs": "di sopra",
    "broken brass valve": "valvola d'ottone rotta",
    "coat pocket": "tasca del cappotto",
    "Got it": "capito, presa",
    "hardware shop": "ferramenta",
    "Turn left": "gira a sinistra",
    "walk straight": "cammina dritto",
    "Do I cross": "attraverso",
    "on your right": "sulla tua destra",
    "And after that?": "e dopo di quello?",
    "into": "entrando in, dentro",
    "Look for": "cerca",
    "Does the shop have": "il negozio ha",
    "above the door": "sopra la porta",
    "Show the clerk": "mostra al commesso",
    "I will repeat": "ripeterò",
    "all the way": "per tutta la strada",
    "wakes up": "si sveglia",
}
