# Authoring module for linden-courtyard-it-s01e01-scene-04.
ID = "linden-courtyard-it-s01e01-scene-04"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = "Room Four on the Second Floor  (La camera quattro al secondo piano)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"hannah": "Hannah", "evelyn": "Evelyn", "graham": "Graham"}
INTRO = "All'ingresso della locanda, Evelyn, un'insegnante di pianoforte in pensione, scende dalla vettura trascinando una grande valigia blu scuro. Hannah accoglie la sua prima vera ospite mentre Graham si avvicina per dare una mano coi bagagli. Ascoltiamo la scena."
OPENER = "Riascoltiamo adesso ogni intervento un passo alla volta."
TRANSITION = "Ora sentiamo di nuovo l'intera conversazione di fila."
OUTRO = "Hannah ha gestito la sua prima registrazione con garbo, ma Graham ha notato subito quanto pesi quella valigia blu. Alla prossima scena per scoprire il perché."
CLOSING = ("evelyn", "Take care!")
STORY = [
    ("hannah", "Welcome! Good morning, ma'am.", "Benvenuta! Buongiorno, signora."),
    ("evelyn", "Good morning, my dear. I have a room for Evelyn.", "Buongiorno, cara. Ho una camera prenotata a nome Evelyn."),
    ("hannah", "Yes, room four on the second floor! How was your train trip?", "Sì, la camera quattro al secondo piano! Com'è andato il suo viaggio in treno?"),
    ("evelyn", "Quiet and pleasant, thank you, though this suitcase feels very heavy today.", "Tranquillo e piacevole, grazie, anche se questa valigia sembra molto pesante oggi."),
    ("graham", "Allow me. Goodness, did you pack stones in here?", "Mi permetta. Perbacco, ha messo delle pietre qui dentro?"),
    ("evelyn", "Only dresses, sheet music, and my favorite teacup!", "Solo vestiti, spartiti musicali e la mia tazza da tè preferita!"),
    ("hannah", "Here is your key, number four. Breakfast is from seven thirty to ten.", "Ecco la sua chiave, numero quattro. La colazione è dalle sette e trenta alle dieci."),
    ("evelyn", "Wonderful. Is the window facing the street or the courtyard?", "Magnifico. La finestra dà sulla strada o sul cortile?"),
    ("hannah", "The courtyard, right above the old tree. It is very quiet.", "Sul cortile, proprio sopra il vecchio albero. È molto silenziosa."),
    ("evelyn", "Just what I need. Where are the stairs?", "Proprio quello che mi ci vuole. Dove sono le scale?"),
    ("graham", "Right through this archway. I will carry the blue bag up for you.", "Proprio oltre quest'arco. Le porto su io la valigia blu."),
    ("evelyn", "Thank you both very much.", "Grazie mille a tutti e due."),
]
WALK = [
    (0, None, ["'Benvenuta! Buongiorno, signora.' Negli Stati Uniti l'appellativo cortese più naturale per rivolgersi a una signora è", (None, "ma'am"), "breve, caldo e molto rispettoso."]),
    (1, None, ["'Buongiorno, cara. Ho una camera prenotata a nome Evelyn.' Quando arrivi in albergo ti basta dire", (None, "I have a room for"), "seguito dal tuo nome per annunciare la prenotazione."]),
    (2, None, ["'Sì, la camera quattro al secondo piano! Com'è andato il suo viaggio in treno?' Ricorda che negli Stati Uniti il pianterreno conta come primo livello, e per chiedere del viaggio passato usi", (None, "How was your train trip"), "al passato semplice."]),
    (3, None, ["'Tranquillo e piacevole, grazie, anche se questa valigia sembra molto pesante oggi.' La combinazione", (None, "feels very heavy"), "descrive la sensazione fisica di peso che provi sollevando o tirando il bagaglio."]),
    (4, None, ["'Mi permetta. Perbacco, ha messo delle pietre qui dentro?' Per offrirti con galanteria di portare un peso dici", (None, "Allow me"), "mentre", (None, "Goodness"), "è un'esclamazione garbata di stupore."]),
    (5, None, ["'Solo vestiti, spartiti musicali e la mia tazza da tè preferita!' La musica stampata su fogli si chiama", (None, "sheet music"), "un nome non numerabile che resta sempre al singolare."]),
    (6, None, ["'Ecco la sua chiave, numero quattro. La colazione è dalle sette e trenta alle dieci.' Dire l'ora nel parlato quotidiano è immediato: accosti semplicemente ora e minuti in", (None, "seven thirty"), "senza congiunzioni."]),
    (7, None, ["'Magnifico. La finestra dà sulla strada o sul cortile?' Dove l'italiano dice dare su, l'inglese usa l'immagine del volto rivolto verso l'esterno con", (None, "facing the street"), "senza alcuna preposizione."]),
    (8, None, ["'Sul cortile, proprio sopra il vecchio albero. È molto silenziosa.' Mettere l'avverbio davanti alla preposizione in", (None, "right above"), "precisa il punto esatto: proprio sopra il tiglio."]),
    (9, None, ["'Proprio quello che mi ci vuole. Dove sono le scale?' Memorizza la frase", (None, "Just what I need"), "perfetta ogni volta che una soluzione risponde esattamente ai tuoi desideri."]),
    (10, None, ["'Proprio oltre quest'arco. Le porto su io la valigia blu.' Per offrirti spontaneamente di fare qualcosa sul momento usi il futuro con", (None, "I will carry"), "completato da", (None, "up"), "per indicare la salita al piano superiore."]),
    (11, None, ["'Grazie mille a tutti e due.' Inserire la parola", (None, "both"), "dentro", (None, "Thank you both"), "permette di ringraziare due interlocutori insieme in modo snello e cordiale."]),
]
CALLOUT_TRANS = {
    "ma'am": "signora",
    "I have a room for": "ho una camera a nome di",
    "How was your train trip": "com'è andato il suo viaggio in treno",
    "feels very heavy": "sembra molto pesante",
    "Allow me": "mi permetta",
    "Goodness": "perbacco",
    "sheet music": "spartiti musicali",
    "seven thirty": "sette e trenta",
    "facing the street": "che dà sulla strada",
    "right above": "proprio sopra",
    "Just what I need": "proprio quello che mi serve",
    "I will carry": "porterò",
    "up": "su, al piano di sopra",
    "both": "entrambi, tutti e due",
    "Thank you both": "grazie a tutti e due",
}
