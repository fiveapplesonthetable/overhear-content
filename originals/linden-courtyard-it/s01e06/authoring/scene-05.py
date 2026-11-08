# Authoring module for linden-courtyard-it-s01e06-scene-05.
ID = "linden-courtyard-it-s01e06-scene-05"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 6
SCENE = 5
TITLE = "Page Two, Clause Fourteen  (Pagina due, clausola quattordici)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"arthur": "Arthur", "caleb": "Caleb", "hannah": "Hannah"}
INTRO = "Alla reception della Locanda del Cortile del Tiglio, Arthur porge l'avviso di due pagine a Caleb mentre Hannah trattiene il fiato accanto al registro delle prenotazioni. Caleb sfoglia subito il secondo foglio. Ascolta prima tutta la scena."
OPENER = "Adesso analizziamo ogni battuta con calma, una per volta."
TRANSITION = "Riascoltiamo ora tutta la scena di fila."
OUTRO = "La seconda pagina ha ribaltato tutto: aprire i quattro tavoli della colazione agli abitanti del quartiere protegge la locanda per altri dieci anni. Nella prossima scena Arthur ha due grandi annunci nell'angolo caffetteria. Alla prossima."
CLOSING = ("hannah", "Take care!")
STORY = [
    ("arthur", "Look at page one, Caleb: 'commercial office conversion next month.' We are finished!", "Guarda la pagina uno, Caleb: «conversione in uffici commerciali il mese prossimo.» Siamo finiti!"),
    ("caleb", "Wait a moment, sir. Did you read page two clipped underneath?", "Aspetti un momento, signore. Ha letto la pagina due fermata sotto con la graffetta?"),
    ("arthur", "Only small gray numbers! My heart stopped at page one!", "Solo numeretti grigi! Il cuore mi si è fermato alla pagina uno!"),
    ("hannah", "Look where Caleb is pointing with his pencil, Arthur!", "Guarda dove sta indicando Caleb con la sua matita, Arthur!"),
    ("caleb", "Clause fourteen of the Portland Old Quarter Act, and my brother here just nodded!", "La clausola quattordici della Legge sul Quartiere Storico di Portland, e mio fratello qui ha appena annuito!"),
    ("arthur", "In plain words, please! What does Clause fourteen say?", "In parole povere, ti prego! Che cosa dice la clausola quattordici?"),
    ("caleb", "No courtyard building over eighty years old may become private offices if the first floor serves neighbors daily.", "Nessun edificio con cortile di oltre ottant'anni può diventare uffici privati se il piano terra serve quotidianamente gli abitanti del quartiere."),
    ("hannah", "'Serves neighbors daily'... like a public morning cafe?!", "«Serve quotidianamente gli abitanti del quartiere»... come una caffetteria mattutina aperta al pubblico?!"),
    ("caleb", "Exactly! Right now your four tables only serve overnight hotel guests.", "Esatto! In questo momento i vostri quattro tavoli servono soltanto gli ospiti che pernottano in albergo."),
    ("arthur", "Wait, if we open our courtyard gate every morning for neighborhood coffee and bread...", "Aspetta, se apriamo il cancello del nostro cortile ogni mattina per caffè e pane di quartiere..."),
    ("caleb", "Then your guesthouse lease is protected for another ten years by city law!", "Allora il contratto d'affitto della vostra locanda è protetto per altri dieci anni dalla legge comunale!"),
    ("hannah", "Arthur! Your glasses just fell off your nose for a happy reason!", "Arthur! I tuoi occhiali ti sono appena caduti dal naso per un motivo felice!"),
]
WALK = [
    (0, None, ["'Guarda la pagina uno, Caleb: «conversione in uffici commerciali il mese prossimo.» Siamo finiti!' Nei riferimenti numerati scompare l'articolo davanti a", (None, "page one"), "e lo sconforto esplode in", (None, "We are finished"), "siamo spacciati."]),
    (1, None, ["'Aspetti un momento, signore. Ha letto la pagina due fermata sotto con la graffetta?' Il foglio spillato sotto il primo è descritto con precisione da", (None, "clipped underneath"), "fissato sotto con una graffetta."]),
    (2, None, ["'Solo numeretti grigi! Il cuore mi si è fermato alla pagina uno!' Anche in inglese lo spavento improvviso usa l'immagine vivida", (None, "My heart stopped"), "il cuore si è fermato."]),
    (3, None, ["'Guarda dove sta indicando Caleb con la sua matita, Arthur!' L'imperativo guida subito lo sguardo sul punto esatto della carta tramite", (None, "Look where"), "guarda dove."]),
    (4, None, ["'La clausola quattordici della Legge sul Quartiere Storico di Portland, e mio fratello qui ha appena annuito!' Per dire fare cenno di sì col capo basta un solo verbo:", (None, "just nodded"), "ha appena annuito."]),
    (5, None, ["'In parole povere, ti prego! Che cosa dice la clausola quattordici?' Quando il linguaggio tecnico confonde, si chiede una spiegazione semplice con", (None, "In plain words"), "in parole chiare."]),
    (6, None, ["'Nessun edificio con cortile di oltre ottant'anni può diventare uffici privati se il piano terra serve quotidianamente gli abitanti del quartiere.' L'età dell'immobile sta in", (None, "over eighty years old"), "e ricorda che negli Stati Uniti", (None, "first floor"), "indica il piano terra."]),
    (7, None, ["'«Serve quotidianamente gli abitanti del quartiere»... come una caffetteria mattutina aperta al pubblico?!' Tre parole snelle dipingono l'idea vincente in", (None, "public morning cafe"), "caffetteria mattutina aperta a tutti."]),
    (8, None, ["'Esatto! In questo momento i vostri quattro tavoli servono soltanto gli ospiti che pernottano in albergo.' Un singolo aggettivo preposto,", (None, "overnight hotel guests"), "distingue chi dorme in camera da chi passa solo a colazione."]),
    (9, None, ["'Aspetta, se apriamo il cancello del nostro cortile ogni mattina per caffè e pane di quartiere...' L'abitudine quotidiana scandita sul calendario mattutino è", (None, "every morning"), "ogni mattina."]),
    (10, None, ["'Allora il contratto d'affitto della vostra locanda è protetto per altri dieci anni dalla legge comunale!' Davanti a un periodo considerato come blocco unico si usa il singolare in", (None, "another ten years"), "garantito", (None, "by city law"), "dalla legge cittadina."]),
    (11, None, ["'Arthur! I tuoi occhiali ti sono appena caduti dal naso per un motivo felice!' Quando un oggetto si stacca o scivola giù da un appoggio, il passato irregolare prende la particella di distacco in", (None, "fell off"), "sono caduti giù da."]),
]
CALLOUT_TRANS = {
    "page one": "pagina uno",
    "We are finished": "siamo finiti, siamo rovinati",
    "clipped underneath": "fermata sotto con la graffetta",
    "My heart stopped": "il cuore mi si è fermato",
    "Look where": "guarda dove",
    "just nodded": "ha appena annuito",
    "In plain words": "in parole povere",
    "over eighty years old": "di oltre ottant'anni",
    "first floor": "piano terra",
    "public morning cafe": "caffetteria mattutina aperta al pubblico",
    "overnight hotel guests": "ospiti che pernottano in albergo",
    "every morning": "ogni mattina",
    "another ten years": "altri dieci anni",
    "by city law": "dalla legge comunale",
    "fell off": "sono caduti da",
}
