# Authoring module for linden-courtyard-it-s01e03-scene-02.
ID = "linden-courtyard-it-s01e03-scene-02"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 3
SCENE = 2
TITLE = "The Sunny Attic  (La soffitta luminosa)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"graham": "Graham", "hannah": "Hannah", "tessa": "Tessa"}
INTRO = "Lassù, sotto il tetto in legno del terzo piano, Graham apre lo studio in soffitta per Hannah mentre Tessa sale con una pila di asciugamani freschi. Ascoltiamo prima tutta la scena."
OPENER = "Ripassiamo adesso ogni battuta un passo alla volta."
TRANSITION = "Torniamo ad ascoltare l'intera conversazione senza pause."
OUTRO = "Tra grandi travi di legno e il ticchettio della pioggia sul tetto, alla soffitta mancano soltanto una lampada, due cuscini e un tappeto. Ci ritroviamo nella prossima scena mentre corrono contro il tempo."
CLOSING = ("tessa", "See you later!")
STORY = [
    ("hannah", "Oh, look at this room! Big wooden beams and a window over the courtyard!", "Oh, guarda questa stanza! Grandi travi di legno e una finestra sul cortile!"),
    ("tessa", "Listen to the rain on the roof. It feels so cozy up here!", "Ascolta la pioggia sul tetto. È così accogliente quassù!"),
    ("graham", "Dry, warm, and quiet. Now tell me what is missing.", "Asciutta, calda e silenziosa. Ora ditemi che cosa manca."),
    ("hannah", "Okay: there is a bed, a table, and a chair, but no bedside lamp.", "Allora: c'è un letto, un tavolo e una sedia, ma nessuna lampada sul comodino."),
    ("tessa", "And no mirror on the wall, and the floor feels bare without a rug.", "E nessuno specchio alla parete, e il pavimento sembra spoglio senza un tappeto."),
    ("graham", "There is a brass reading lamp in my workshop downstairs.", "C'è una lampada da lettura in ottone nel mio laboratorio di sotto."),
    ("tessa", "And I have two soft pillows and a woven blue rug in the closet!", "E io ho due cuscini morbidi e un tappeto blu intrecciato nel ripostiglio!"),
    ("hannah", "What about the small bathroom next door? Does the light work?", "E il bagnetto qui accanto? Funziona la luce?"),
    ("graham", "New bulb last week, clean soap, plenty of hot water.", "Lampadina nuova la settimana scorsa, sapone pulito, acqua calda in abbondanza."),
    ("tessa", "Give us fifteen minutes and this attic will beat room seven!", "Dateci quindici minuti e questa soffitta batterà la camera sette!"),
    ("hannah", "Grab those cardboard boxes, Graham. Down the stairs we go!", "Afferra quegli scatoloni di cartone, Graham. Giù per le scale, si va!"),
    ("graham", "Careful on the turn, do not bump the wall!", "Attenta alla curva, non urtare il muro!"),
]
WALK = [
    (0, None, ["'Oh, guarda questa stanza! Grandi travi di legno e una finestra sul cortile!' A differenza dell'italiano guardare qualcosa, il verbo inglese richiede sempre la preposizione di direzione in", (None, "look at this room"), "guarda questa stanza."]),
    (1, None, ["'Ascolta la pioggia sul tetto. È così accogliente quassù!' Lo stesso vale per ascoltare: non è mai transitivo diretto, ma vuole la preposizione in", (None, "Listen to the rain"), "ascolta la pioggia."]),
    (2, None, ["'Asciutta, calda e silenziosa. Ora ditemi che cosa manca.' Nelle interrogative indirette come", (None, "what is missing"), "l'ordine delle parole resta affermativo, con il participio presente per dire che cosa manca."]),
    (3, None, ["'Allora: c'è un letto, un tavolo e una sedia, ma nessuna lampada sul comodino.' Quando apri un elenco di arredi, il verbo si accorda col primo nome singolare in", (None, "there is a bed"), "c'è un letto."]),
    (4, None, ["'E nessuno specchio alla parete, e il pavimento sembra spoglio senza un tappeto.' Per quadri e specchi appesi a una parete verticale l'inglese sceglie la preposizione di contatto:", (None, "on the wall"), "sulla parete."]),
    (5, None, ["'C'è una lampada da lettura in ottone nel mio laboratorio di sotto.' L'avverbio compatto", (None, "downstairs"), "basta da solo per dire giù al piano inferiore senza aggiungere preposizioni."]),
    (6, None, ["'E io ho due cuscini morbidi e un tappeto blu intrecciato nel ripostiglio!' Il participio", (None, "woven"), "precede il colore per descrivere un tessuto lavorato a intreccio."]),
    (7, None, ["'E il bagnetto qui accanto? Funziona la luce?' Per introdurre un nuovo punto pratico nella conversazione,", (None, "What about"), "equivale al nostro e per quanto riguarda."]),
    (8, None, ["'Lampadina nuova la settimana scorsa, sapone pulito, acqua calda in abbondanza.' Davanti a nomi non numerabili come l'acqua, la formula", (None, "plenty of hot water"), "indica abbondanza più che sufficiente."]),
    (9, None, ["'Dateci quindici minuti e questa soffitta batterà la camera sette!' Il futuro", (None, "will beat"), "non si usa solo nello sport, ma anche per dire che qualcosa supererà un'alternativa."]),
    (10, None, ["'Afferra quegli scatoloni di cartone, Graham. Giù per le scale, si va!' Spostare la direzione in apertura di frase in", (None, "Down the stairs we go"), "dà slancio e ritmo di squadra."]),
    (11, None, ["'Attenta alla curva, non urtare il muro!' Per raccomandare di non sbattere contro qualcosa basta", (None, "do not bump"), "seguito direttamente dall'oggetto."]),
]
CALLOUT_TRANS = {
    "look at this room": "guarda questa stanza",
    "Listen to the rain": "ascolta la pioggia",
    "what is missing": "che cosa manca",
    "there is a bed": "c'è un letto",
    "on the wall": "alla parete, sul muro",
    "downstairs": "di sotto, al piano inferiore",
    "woven": "intrecciato, tessuto",
    "What about": "e per quanto riguarda",
    "plenty of hot water": "acqua calda in abbondanza",
    "will beat": "batterà, supererà",
    "Down the stairs we go": "giù per le scale si va",
    "do not bump": "non urtare",
}
