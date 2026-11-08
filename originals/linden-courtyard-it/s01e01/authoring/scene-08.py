# Authoring module for linden-courtyard-it-s01e01-scene-08.
ID = "linden-courtyard-it-s01e01-scene-08"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = "Left on the Step  (Lasciata sul gradino)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"hannah": "Hannah", "graham": "Graham"}
INTRO = "Sono quasi le nove di sera e le lanterne del cortile brillano piano mentre Hannah conclude il suo primo turno insieme a Graham. All'improvviso la campanella del cancello suona una volta nel silenzio della notte. Ascolta prima la scena."
OPENER = "Ripercorriamo insieme ogni battuta di questo finale di episodio."
TRANSITION = "Riascoltiamo ora tutta la scena per intero."
OUTRO = "La valigia di Evelyn è tornata, ma lo sconosciuto è svanito nel buio chiedendo di custodire la sua fino a venerdì. Così si chiude il primo episodio; ti aspettiamo nel secondo!"
CLOSING = ("graham", "Have a good night!")
STORY = [
    ("hannah", "Did you hear that, Graham? Someone just rang the gate bell!", "Hai sentito, Graham? Qualcuno ha appena suonato la campanella del cancello!"),
    ("graham", "At nine o'clock? Stay here, let us open the door together.", "Alle nove in punto? Resta qui, apriamo la porta insieme."),
    ("hannah", "Hello? Good evening! Nobody is standing in the courtyard!", "C'è nessuno? Buonasera! Non c'è nessuno in piedi nel cortile!"),
    ("graham", "Wait. Look down on the stone step.", "Aspetta. Guarda giù sul gradino di pietra."),
    ("hannah", "Another dark blue suitcase! Is this Miss Evelyn's bag?", "Un'altra valigia blu scuro! È il bagaglio della signorina Evelyn?"),
    ("graham", "Check the zipper... yes, her initials are right here!", "Controlla la cerniera... sì, le sue iniziali sono proprio qui!"),
    ("hannah", "Why did the person run away without taking his own suitcase back?", "Perché quella persona è scappata via senza riprendersi la propria valigia?"),
    ("graham", "Look, there is a folded white envelope taped to the handle.", "Guarda, c'è una busta bianca piegata fissata col nastro adesivo alla maniglia."),
    ("hannah", "Let me read it: 'Sorry for the mistake. Please keep my blue bag until Friday.'", "Fammi leggere: «Scusate per l'errore. Per favore, tenete la mia borsa blu fino a venerdì.»"),
    ("graham", "Until Friday? No name, no signature!", "Fino a venerdì? Nessun nome, nessuna firma!"),
    ("hannah", "Why leave your own shoes and wooden train with strangers until Friday?", "Perché lasciare le proprie scarpe e un treno di legno a degli sconosciuti fino a venerdì?"),
    ("graham", "Welcome to the Linden Courtyard Inn, Hannah. Your second day will not be boring.", "Benvenuta alla Locanda del Cortile del Tiglio, Hannah. Il tuo secondo giorno non sarà noioso."),
]
WALK = [
    (0, None, ["'Hai sentito, Graham? Qualcuno ha appena suonato la campanella del cancello!' Ecco una domanda nitida al passato:", (None, "Did you hear that"), "mette l'ausiliare davanti e lascia il verbo sentire invariato."]),
    (1, None, ["'Alle nove in punto? Resta qui, apriamo la porta insieme.' L'espressione tradizionale", (None, "nine o'clock"), "indica sempre un'ora spaccata, senza minuti aggiunti."]),
    (2, None, ["'C'è nessuno? Buonasera! Non c'è nessuno in piedi nel cortile!' Distingui bene i saluti serali: quando incontri o accogli qualcuno di sera dici", (None, "Good evening"), "mentre l'augurio della buonanotte si usa solo al congedo."]),
    (3, None, ["'Aspetta. Guarda giù sul gradino di pietra.' Accostando sguardo e direzione verso il basso,", (None, "Look down"), "invita subito ad abbassare gli occhi a terra."]),
    (4, None, ["'Un'altra valigia blu scuro! È il bagaglio della signorina Evelyn?' Al singolare l'inglese fonde articolo indeterminativo e aggettivo in una parola sola:", (None, "Another"), "un'altra."]),
    (5, None, ["'Controlla la cerniera... sì, le sue iniziali sono proprio qui!' In inglese il possessivo di terza persona concorda col possessore e non con la cosa posseduta, quindi per una donna si usa", (None, "her initials"), "le sue iniziali."]),
    (6, None, ["'Perché quella persona è scappata via senza riprendersi la propria valigia?' Dopo una preposizione come senza, l'inglese non usa l'infinito italiano ma la forma progressiva del verbo:", (None, "without taking"), "senza prendere."]),
    (7, None, ["'Guarda, c'è una busta bianca piegata fissata col nastro adesivo alla maniglia.' Dal sostantivo che indica il nastro adesivo si ricava direttamente il participio", (None, "taped"), "incollato col nastro."]),
    (8, None, ["'Fammi leggere: «Scusate per l'errore. Per favore, tenete la mia borsa blu fino a venerdì.»' Per scusarsi di uno sbaglio specifico si lega l'aggettivo alla preposizione in", (None, "Sorry for the mistake"), "scusate per l'errore."]),
    (9, None, ["'Fino a venerdì? Nessun nome, nessuna firma!' Ricorda che i giorni della settimana come", (None, "Friday"), "vogliono sempre l'iniziale maiuscola, preceduti da", (None, "Until"), "per indicare il limite temporale fino a."]),
    (10, None, ["'Perché lasciare le proprie scarpe e un treno di legno a degli sconosciuti fino a venerdì?' Occhio al falso amico", (None, "strangers"), "che non vuol dire stranieri dall'estero, bensì persone sconosciute."]),
    (11, None, ["'Benvenuta alla Locanda del Cortile del Tiglio, Hannah. Il tuo secondo giorno non sarà noioso.' Il futuro negativo", (None, "will not be boring"), "descrive qualcosa che non risulterà noioso."]),
]
CALLOUT_TRANS = {
    "Did you hear that": "hai sentito",
    "nine o'clock": "le nove in punto",
    "Good evening": "buonasera",
    "Look down": "guarda giù",
    "Another": "un'altra",
    "her initials": "le sue iniziali",
    "without taking": "senza prendere",
    "taped": "fissata col nastro adesivo",
    "Sorry for the mistake": "scusate per l'errore",
    "Friday": "venerdì",
    "Until": "fino a",
    "strangers": "sconosciuti",
    "will not be boring": "non sarà noioso",
}
