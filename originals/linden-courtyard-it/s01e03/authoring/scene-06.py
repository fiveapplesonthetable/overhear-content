# Authoring module for linden-courtyard-it-s01e03-scene-06.
ID = "linden-courtyard-it-s01e03-scene-06"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 3
SCENE = 6
TITLE = "A Five-Star Sigh of Relief  (Un sospiro di sollievo a cinque stelle)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"arthur": "Arthur", "hannah": "Hannah", "tessa": "Tessa"}
INTRO = "Tornati al bancone del pianterreno, Arthur cammina avanti e indietro sulle spine finché Hannah non scende sorridendo verso lui e Tessa. Poi lo sguardo di Hannah cade su un oggetto rimasto accanto al campanello d'ottone. Ascolta prima la scena."
OPENER = "Ripassiamo frase per frase questa scoperta al bancone."
TRANSITION = "Ascoltiamo di nuovo l'intera scena senza fermarci."
OUTRO = "Schizzi ordinati a matita e un voto di nove su dieci hanno convinto tutti che Caleb sia un ispettore in incognito, proprio mentre un colpo metallico rimbomba nei muri. Alla prossima scena."
CLOSING = ("tessa", "See you later!")
STORY = [
    ("arthur", "Well? Did he shout? Did he ask for his money back?", "Allora? Ha urlato? Ha chiesto indietro i suoi soldi?"),
    ("hannah", "Neither! He loved the quiet roof beams and thanked us.", "Né l'una né l'altra cosa! Ha adorato le silenziose travi del tetto e ci ha ringraziati."),
    ("arthur", "Hannah, you have a gift for hospitality! My blood pressure is saved!", "Hannah, hai un talento naturale per l'ospitalità! La mia pressione arteriosa è salva!"),
    ("tessa", "He even finished every drop of vegetable soup before going up.", "Ha persino finito fino all'ultima goccia di zuppa di verdure prima di salire."),
    ("hannah", "Wait, whose small brown leather notebook is this on the counter?", "Aspettate, di chi è questo piccolo taccuino di pelle marrone sul bancone?"),
    ("tessa", "Caleb set it down when he took the dry towel from me!", "Caleb lo ha appoggiato quando ha preso da me l'asciugamano asciutto!"),
    ("arthur", "Do not snoop, of course... wait, it fell open to the middle page!", "Non curiosate, mi raccomando... fermi, si è aperto da solo alla pagina centrale!"),
    ("hannah", "Why are there neat pencil drawings of three guesthouses on our street?", "Perché ci sono precisi disegni a matita di tre locande della nostra via?"),
    ("tessa", "Look at the words beside ours: 'Courtyard width, street noise, quiet score: nine out of ten!'", "Guardate le parole accanto alla nostra: «Larghezza del cortile, rumore della strada, punteggio di silenzio: nove su dieci!»"),
    ("arthur", "Nine out of ten?! Nobody measures courtyards unless...", "Nove su dieci?! Nessuno misura i cortili a meno che..."),
    ("tessa", "Unless he writes for the annual Portland Travel Guide!", "A meno che non scriva per la Guida Turistica Annuale di Portland!"),
    ("hannah", "Quick, close it! Let us take it upstairs... wait, what is that loud clanking sound?", "Presto, chiudetelo! Portiamolo di sopra... aspettate, che cos'è questo forte rumore di ferraglia?"),
]
WALK = [
    (0, None, ["'Allora? Ha urlato? Ha chiesto indietro i suoi soldi?' Per chiedere un rimborso in denaro si chiude la frase con l'avverbio di restituzione in", (None, "ask for his money back"), "chiedere indietro i soldi."]),
    (1, None, ["'Né l'una né l'altra cosa! Ha adorato le silenziose travi del tetto e ci ha ringraziati.' Quando scarti in un colpo solo due ipotesi appena fatte, basta una parola:", (None, "Neither"), "nessuna delle due."]),
    (2, None, ["'Hannah, hai un talento naturale per l'ospitalità! La mia pressione arteriosa è salva!' Avere una dote innata per un mestiere si esprime con", (None, "a gift for hospitality"), "un dono per l'accoglienza."]),
    (3, None, ["'Ha persino finito fino all'ultima goccia di zuppa di verdure prima di salire.' Anche dopo la preposizione temporale prima di, il verbo inglese prende la forma progressiva in", (None, "before going up"), "prima di salire."]),
    (4, None, ["'Aspettate, di chi è questo piccolo taccuino di pelle marrone sul bancone?' Per chiedere a chi appartiene un oggetto si apre con", (None, "whose"), "seguito subito dall'oggetto posseduto senza articolo."]),
    (5, None, ["'Caleb lo ha appoggiato quando ha preso da me l'asciugamano asciutto!' Posare un oggetto sopra un piano si rende col verbo frasale separabile", (None, "set it down"), "lo ha appoggiato."]),
    (6, None, ["'Non curiosate, mi raccomando... fermi, si è aperto da solo alla pagina centrale!' Ficcare il naso negli affari altrui si dice col verbo colloquiale", (None, "Do not snoop"), "mentre", (None, "fell open"), "indica un libro che cade aprendosi da solo."]),
    (7, None, ["'Perché ci sono precisi disegni a matita di tre locande della nostra via?' Invertendo ordine affermativo e verbo al plurale,", (None, "Why are there"), "chiede perché ci sono."]),
    (8, None, ["'Guardate le parole accanto alla nostra: «Larghezza del cortile, rumore della strada, punteggio di silenzio: nove su dieci!»' Nei voti e nei punteggi dove noi diciamo nove su dieci, l'inglese dice", (None, "nine out of ten"), "nove fuori da dieci."]),
    (9, None, ["'Nove su dieci?! Nessuno misura i cortili a meno che...' Una sola congiunzione compatta,", (None, "unless"), "traduce tutto il nostro a meno che non, senza aggiungere alcuna negazione."]),
    (10, None, ["'A meno che non scriva per la Guida Turistica Annuale di Portland!' Mentre l'italiano richiede il congiuntivo dopo a meno che non, l'inglese usa il semplice indicativo affermativo in", (None, "Unless he writes"), "a meno che scriva."]),
    (11, None, ["'Presto, chiudetelo! Portiamolo di sopra... aspettate, che cos'è questo forte rumore di ferraglia?' Il suono onomatopeico", (None, "clanking sound"), "imita alla perfezione lo sbattere sordo di tubi metallici."]),
]
CALLOUT_TRANS = {
    "ask for his money back": "chiedere indietro i suoi soldi",
    "Neither": "né l'uno né l'altro",
    "a gift for hospitality": "un dono per l'ospitalità",
    "before going up": "prima di salire",
    "whose": "di chi",
    "set it down": "lo ha appoggiato",
    "Do not snoop": "non curiosate",
    "fell open": "si è aperto da solo",
    "Why are there": "perché ci sono",
    "nine out of ten": "nove su dieci",
    "unless": "a meno che",
    "Unless he writes": "a meno che non scriva",
    "clanking sound": "rumore metallico",
}
