# Authoring module for linden-courtyard-it-s01e03-scene-03.
ID = "linden-courtyard-it-s01e03-scene-03"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 3
SCENE = 3
TITLE = "Left at the Landing  (A sinistra sul pianerottolo)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"hannah": "Hannah", "tessa": "Tessa", "arthur": "Arthur"}
INTRO = "Dieci minuti prima delle otto, Hannah, Tessa e Arthur danno gli ultimi ritocchi alla camera del terzo piano. Ogni dettaglio conta prima che arrivi il viaggiatore sotto la pioggia. Ascolta prima tutta la scena."
OPENER = "Vediamo ora da vicino ogni frase di questi preparativi."
TRANSITION = "Riascoltiamo tutta la scena di seguito a ritmo naturale."
OUTRO = "La lampada d'ottone diffonde già una luce calda proprio mentre giù in cortile suona la campanella del cancello. Nella prossima scena Caleb entra cercando riparo dalla pioggia. A presto."
CLOSING = ("hannah", "Bye for now!")
STORY = [
    ("tessa", "Tuck that sheet corner tight, Hannah! Here go the two soft pillows.", "Rimbocca bene quell'angolo del lenzuolo, Hannah! Ecco qui i due cuscini morbidi."),
    ("hannah", "Done! And the blue rug fits right beside the bed.", "Fatto! E il tappeto blu ci sta a pennello proprio accanto al letto."),
    ("arthur", "Where should I hang this round mirror? Left of the window or right?", "Dove dovrei appendere questo specchio rotondo? A sinistra della finestra o a destra?"),
    ("hannah", "Right beside the desk, where the light is good.", "Proprio accanto alla scrivania, dove la luce è buona."),
    ("tessa", "Plug in Graham's brass lamp... oh, look how warm that yellow light is!", "Attacca la spina della lampada d'ottone di Graham... oh, guarda com'è calda quella luce gialla!"),
    ("arthur", "Honestly, I almost want to sleep up here myself tonight!", "Sinceramente, quasi quasi vorrei dormire quassù io stesso stanotte!"),
    ("hannah", "Wait, what discount should we offer him for changing rooms?", "Aspettate, quale sconto dovremmo offrirgli per il cambio di camera?"),
    ("arthur", "Half price for tonight, and free breakfast all week!", "Metà prezzo per stanotte e colazione gratuita tutta la settimana!"),
    ("tessa", "Generous! Did you just hear the courtyard gate bell downstairs?", "Generoso! Avete appena sentito giù la campanella del cancello del cortile?"),
    ("hannah", "Eight o'clock on the dot! Our guest is here!", "Le otto spaccate! Il nostro ospite è qui!"),
    ("arthur", "My heart is pounding! Hannah, you explain it, you sound calm and honest!", "Mi batte forte il cuore! Hannah, spiegaglielo tu, hai un tono calmo e sincero!"),
    ("hannah", "Leave it to me. Let us go down and welcome him.", "Lascia fare a me. Scendiamo a dargli il benvenuto."),
]
WALK = [
    (0, None, ["'Rimbocca bene quell'angolo del lenzuolo, Hannah! Ecco qui i due cuscini morbidi.' Rimboccare le lenzuola sotto il materasso si esprime col verbo specifico", (None, "Tuck"), "chiuso dall'aggettivo", (None, "tight"), "ben teso."]),
    (1, None, ["'Fatto! E il tappeto blu ci sta a pennello proprio accanto al letto.' Oltre che per i vestiti, il verbo entrare nelle misure giuste vale per i mobili in", (None, "fits right beside"), "ci sta proprio accanto."]),
    (2, None, ["'Dove dovrei appendere questo specchio rotondo? A sinistra della finestra o a destra?' Per chiedere un consiglio pratico sul da farsi si usa il modale condizionale in", (None, "Where should I hang"), "dove dovrei appendere."]),
    (3, None, ["'Proprio accanto alla scrivania, dove la luce è buona.' Qui la parola", (None, "Right"), "non indica la destra, ma rafforza la precisione spaziale come il nostro proprio."]),
    (4, None, ["'Attacca la spina della lampada d'ottone di Graham... oh, guarda com'è calda quella luce gialla!' Collegare un apparecchio elettrico alla presa di corrente si dice", (None, "Plug in"), "attaccare la spina."]),
    (5, None, ["'Sinceramente, quasi quasi vorrei dormire quassù io stesso stanotte!' Il pronome enfatico", (None, "myself"), "rafforza il soggetto per dire io in persona, io stesso."]),
    (6, None, ["'Aspettate, quale sconto dovremmo offrirgli per il cambio di camera?' Dopo la preposizione per, il verbo cambiare prende la forma sostantivata e il plurale in", (None, "for changing rooms"), "per cambiare stanza."]),
    (7, None, ["'Metà prezzo per stanotte e colazione gratuita tutta la settimana!' Due sostantivi affiancati bastano per lo sconto del cinquanta per cento:", (None, "Half price"), "metà prezzo, senza preposizioni."]),
    (8, None, ["'Generoso! Avete appena sentito giù la campanella del cancello del cortile?' Nell'uso americano", (None, "Did you just hear"), "abbina il passato con l'ausiliare all'avverbio appena."]),
    (9, None, ["'Le otto spaccate! Il nostro ospite è qui!' Per sottolineare la puntualità al secondo, l'espressione idiomatica", (None, "on the dot"), "equivale al nostro in punto o spaccate."]),
    (10, None, ["'Mi batte forte il cuore! Hannah, spiegaglielo tu, hai un tono calmo e sincero!' Quando il cuore martella per l'agitazione si usa l'immagine vivida", (None, "My heart is pounding"), "E nota il pronome espresso in", (None, "you explain it"), "per dire spiegaglielo proprio tu."]),
    (11, None, ["'Lascia fare a me. Scendiamo a dargli il benvenuto.' Per rassicurare un collega assumendoti l'incarico basta la formula", (None, "Leave it to me"), "lascia fare a me."]),
]
CALLOUT_TRANS = {
    "Tuck": "rimbocca",
    "tight": "ben teso, stretto",
    "fits right beside": "ci sta proprio accanto",
    "Where should I hang": "dove dovrei appendere",
    "Right": "proprio, esattamente",
    "Plug in": "attacca la spina",
    "myself": "io stesso",
    "for changing rooms": "per il cambio di camera",
    "Half price": "metà prezzo",
    "Did you just hear": "avete appena sentito",
    "on the dot": "spaccate, in punto",
    "My heart is pounding": "mi batte forte il cuore",
    "you explain it": "spiegaglielo tu",
    "Leave it to me": "lascia fare a me",
}
