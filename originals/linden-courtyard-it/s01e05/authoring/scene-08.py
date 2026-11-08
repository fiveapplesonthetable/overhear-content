# Authoring module for linden-courtyard-it-s01e05-scene-08.
ID = "linden-courtyard-it-s01e05-scene-08"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 5
SCENE = 8
TITLE = "The Red-Stamped Letter  (La lettera col timbro rosso)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"arthur": "Arthur", "hannah": "Hannah", "tessa": "Tessa"}
INTRO = "Dopo aver fatto entrare Owen nel cortile della Locanda del Cortile del Tiglio per lasciare riservatezza ai due fratelli, Hannah rientra piano nell'ingresso, dove Tessa osserva commossa e Arthur apre la busta raccomandata. Ascoltiamo prima."
OPENER = "Esaminiamo adesso ogni battuta di questo finale di episodio."
TRANSITION = "Riascoltiamo ora tutta la scena dall'inizio alla fine."
OUTRO = "Fuori sotto l'albero due fratelli lontani si siedono finalmente insieme, mentre dentro un avviso di vendita commerciale minaccia l'intera locanda entro trenta giorni. Il quinto episodio finisce qui; ti aspettiamo nel gran finale di stagione."
CLOSING = ("arthur", "Bye for now!")
STORY = [
    ("tessa", "Hannah, look through the glass. They are standing face to face under the tree!", "Hannah, guarda attraverso il vetro. Sono in piedi faccia a faccia sotto l'albero!"),
    ("hannah", "Neither of them walked away! Caleb is pointing at the two chairs right now!", "Nessuno dei due se n'è andato! Caleb sta indicando le due sedie proprio adesso!"),
    ("arthur", "Wonderful... let me just glance at this landlord letter while we wait.", "Meraviglioso... fatemi solo dare un'occhiata veloce a questa lettera del proprietario mentre aspettiamo."),
    ("tessa", "Probably a boring notice about painting the street shutters.", "Sarà di sicuro un noioso avviso sulla verniciatura delle persiane verso strada."),
    ("arthur", "Oh... oh no. Where is my chair? My knees feel weak.", "Oh... oh no. Dov'è la mia sedia? Mi sento piegare le ginocchia."),
    ("hannah", "Arthur! Your face went completely white! Sit down, what does the letter say?", "Arthur! Sei diventato bianco in volto! Siediti, che cosa dice la lettera?"),
    ("arthur", "Read the top line for me, Hannah. Tell me my glasses are playing tricks again!", "Leggimi la prima riga in alto, Hannah. Dimmi che i miei occhiali mi stanno giocando un altro scherzo!"),
    ("hannah", "'Notice of Property Transfer: Number Eight Courtyard Building offered for commercial office sale.'", "«Avviso di trasferimento immobiliare: Edificio del Cortile Numero Otto messo in vendita per uffici commerciali.»"),
    ("tessa", "Commercial office sale?! Turn our guesthouse and kitchen into gray offices?!", "Vendita per uffici commerciali?! Trasformare la nostra locanda e la cucina in uffici grigi?!"),
    ("arthur", "They give us thirty days before new buyers inspect the building!", "Ci danno trenta giorni prima che i nuovi acquirenti vengano a ispezionare l'edificio!"),
    ("hannah", "Wait, there is a second folded page clipped to the back of this notice...", "Aspettate, c'è una seconda pagina piegata fermata con una graffetta sul retro di questo avviso..."),
    ("arthur", "Not a word to anyone outside yet! Let the two brothers have their Friday afternoon first!", "Ancora neanche una parola a nessuno là fuori! Lasciamo prima ai due fratelli il loro venerdì pomeriggio!"),
]
WALK = [
    (0, None, ["'Hannah, guarda attraverso il vetro. Sono in piedi faccia a faccia sotto l'albero!' L'espressione simmetrica", (None, "face to face"), "coincide parola per parola col nostro faccia a faccia."]),
    (1, None, ["'Nessuno dei due se n'è andato! Caleb sta indicando le due sedie proprio adesso!' Quando parli esattamente di due persone ed escludi entrambe, la forma precisa è", (None, "Neither of them"), "nessuno dei due."]),
    (2, None, ["'Meraviglioso... fatemi solo dare un'occhiata veloce a questa lettera del proprietario mentre aspettiamo.' Per uno sguardo rapido e di sfuggita a un foglio basta il verbo", (None, "glance at"), "dare una rapida occhiata a."]),
    (3, None, ["'Sarà di sicuro un noioso avviso sulla verniciatura delle persiane verso strada.' Dopo la preposizione d'argomento il verbo prende sempre la forma progressiva sostantivata, come in", (None, "about painting"), "riguardo al ridipingere."]),
    (4, None, ["'Oh... oh no. Dov'è la mia sedia? Mi sento piegare le ginocchia.' Davanti alle sensazioni fisiche improvvise il verbo sentire si unisce direttamente all'aggettivo in", (None, "feel weak"), "si sentono deboli."]),
    (5, None, ["'Arthur! Sei diventato bianco in volto! Siediti, che cosa dice la lettera?' Nei cambi improvvisi di colore o stato, il passato irregolare di andare vale diventare in", (None, "went completely white"), "è diventato tutto bianco."]),
    (6, None, ["'Leggimi la prima riga in alto, Hannah. Dimmi che i miei occhiali mi stanno giocando un altro scherzo!' Quando la vista sembra ingannarci, il modo di dire idiomatico è", (None, "playing tricks"), "fare brutti scherzi."]),
    (7, None, ["'«Avviso di trasferimento immobiliare: Edificio del Cortile Numero Otto messo in vendita per uffici commerciali.»' Nel linguaggio degli annunci legali l'articolo scompare e il participio resta asciutto in", (None, "offered for"), "proposto per."]),
    (8, None, ["'Vendita per uffici commerciali?! Trasformare la nostra locanda e la cucina in uffici grigi?!' Per trasformare radicalmente qualcosa si apre con", (None, "Turn"), "e si introduce il risultato finale con", (None, "into gray offices"), "in uffici grigi."]),
    (9, None, ["'Ci danno trenta giorni prima che i nuovi acquirenti vengano a ispezionare l'edificio!' Il termine secco di preavviso risuona chiarissimo in", (None, "thirty days"), "trenta giorni."]),
    (10, None, ["'Aspettate, c'è una seconda pagina piegata fermata con una graffetta sul retro di questo avviso...' Dal nome della graffetta metallica nasce il participio descrittivo in", (None, "clipped to the back"), "agganciata sul retro."]),
    (11, None, ["'Ancora neanche una parola a nessuno là fuori! Lasciamo prima ai due fratelli il loro venerdì pomeriggio!' Per chiedere il massimo riservo senza usare nemmeno un verbo basta l'esclamazione", (None, "Not a word"), "neppure una parola."]),
]
CALLOUT_TRANS = {
    "face to face": "faccia a faccia",
    "Neither of them": "nessuno dei due",
    "glance at": "dare un'occhiata veloce a",
    "about painting": "sulla verniciatura",
    "feel weak": "sembrano deboli, cedono",
    "went completely white": "è diventato completamente bianco",
    "playing tricks": "giocando scherzi",
    "offered for": "messo in, offerto per",
    "Turn": "trasformare",
    "into gray offices": "in uffici grigi",
    "thirty days": "trenta giorni",
    "clipped to the back": "fermata con una graffetta sul retro",
    "Not a word": "neanche una parola",
}
