# Authoring module for linden-courtyard-it-s01e04-scene-04.
ID = "linden-courtyard-it-s01e04-scene-04"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 4
SCENE = 4
TITLE = "Down in the Cellar  (Giù in cantina)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"graham": "Graham", "hannah": "Hannah"}
INTRO = "Giù nella cantina di mattoni sotto il cortile, Hannah porge a Graham la valvola nuova mentre illumina con una torcia elettrica la caldaia spenta. Ascoltiamo prima la scena."
OPENER = "Analizziamo insieme i verbi pratici di questa riparazione in cantina."
TRANSITION = "Riascoltiamo ora il dialogo completo a ritmo naturale."
OUTRO = "Una fiamma blu costante, i tubi di rame che si scaldano e Graham che chiama Hannah socia invece di principiante. Nella prossima scena torniamo di sopra per la colazione. A presto."
CLOSING = ("hannah", "See you soon!")
STORY = [
    ("hannah", "Here are both brass valves, Graham! Catch my breath? Never!", "Ecco tutt'e due le valvole d'ottone, Graham! Riprendere fiato? Mai!"),
    ("graham", "Hold this flashlight steady on the pipe joint right here.", "Tieni ferma questa torcia sul giunto del tubo proprio qui."),
    ("hannah", "Got it! Did you turn off the main water tap already?", "Fatto! Hai già chiuso il rubinetto principale dell'acqua?"),
    ("graham", "Off and drained. Pass me the heavy wrench on your left.", "Chiuso e svuotato. Passami la chiave inglese pesante alla tua sinistra."),
    ("hannah", "This big iron one? Here you go.", "Questa grande di ferro? Ecco a te."),
    ("graham", "One turn, two turns... look how clean that new brass thread fits.", "Un giro, due giri... guarda come combacia pulita quella filettatura nuova d'ottone."),
    ("hannah", "No drips at all! Can we light the boiler now?", "Neanche una goccia! Possiamo accendere la caldaia adesso?"),
    ("graham", "Open the blue wheel slowly to the left, not too fast.", "Apri piano la manopola blu verso sinistra, non troppo in fretta."),
    ("hannah", "Turning slowly... listen! Water is rushing in!", "Giro piano... ascolta! L'acqua sta entrando a fiotti!"),
    ("graham", "And there goes the burner flame, steady blue, just how it should be.", "E ecco che parte la fiamma del bruciatore, blu fissa, proprio come dovrebbe essere."),
    ("hannah", "Touch the copper pipe! It is warming up already!", "Tocca il tubo di rame! Si sta già scaldando!"),
    ("graham", "Three minutes to reach the third floor. Good run today, partner.", "Tre minuti per arrivare al terzo piano. Ottima corsa oggi, socia."),
]
WALK = [
    (0, None, ["'Ecco tutt'e due le valvole d'ottone, Graham! Riprendere fiato? Mai!' Dopo una corsa, riprendere fiato si dice letteralmente afferrare il proprio respiro con", (None, "Catch my breath"), "riprendere fiato."]),
    (1, None, ["'Tieni ferma questa torcia sul giunto del tubo proprio qui.' Nota l'aggettivo finale in", (None, "Hold this flashlight steady"), "tieni ferma questa torcia, e il composto", (None, "pipe joint"), "raccordo del tubo."]),
    (2, None, ["'Fatto! Hai già chiuso il rubinetto principale dell'acqua?' Per chiudere un flusso d'acqua o spegnere un impianto si usa il verbo frasale", (None, "turn off"), "qui interrogato al passato con", (None, "Did you turn off"), "hai chiuso."]),
    (3, None, ["'Chiuso e svuotato. Passami la chiave inglese pesante alla tua sinistra.' L'attrezzo metallico per stringere dadi e bulloni si chiama", (None, "heavy wrench"), "con la consonante iniziale muta nella pronuncia."]),
    (4, None, ["'Questa grande di ferro? Ecco a te.' Per non ripetere il nome chiave inglese basta", (None, "This big iron one"), "mentre porgendo un oggetto in mano dici", (None, "Here you go"), "ecco qui."]),
    (5, None, ["'Un giro, due giri... guarda come combacia pulita quella filettatura nuova d'ottone.' Il verbo", (None, "fits"), "indica che un pezzo entra della misura esatta nella sua sede, la", (None, "brass thread"), "filettatura d'ottone."]),
    (6, None, ["'Neanche una goccia! Possiamo accendere la caldaia adesso?' Per rafforzare una negazione totale si chiude con", (None, "No drips at all"), "nemmeno una perdita, e", (None, "light the boiler"), "vale accendere la fiamma della caldaia."]),
    (7, None, ["'Apri piano la manopola blu verso sinistra, non troppo in fretta.' Gli avverbi di modo seguono l'oggetto come in", (None, "slowly"), "lentamente, e", (None, "not too fast"), "raccomanda di non esagerare con la velocità."]),
    (8, None, ["'Giro piano... ascolta! L'acqua sta entrando a fiotti!' Quando un liquido scorre dentro con impeto e rumore si usa il verbo", (None, "is rushing in"), "sta scorrendo dentro con forza."]),
    (9, None, ["'E ecco che parte la fiamma del bruciatore, blu fissa, proprio come dovrebbe essere.' L'esclamazione dinamica", (None, "there goes"), "segnala qualcosa che si avvia sotto i tuoi occhi, e", (None, "how it should be"), "significa come dovrebbe essere."]),
    (10, None, ["'Tocca il tubo di rame! Si sta già scaldando!' Il cambiamento graduale di temperatura si esprime col verbo frasale progressivo", (None, "is warming up"), "si sta riscaldando."]),
    (11, None, ["'Tre minuti per arrivare al terzo piano. Ottima corsa oggi, socia.' Nota come", (None, "reach the third floor"), "non chieda nessuna preposizione davanti alla destinazione, a differenza dell'italiano arrivare al."]),
]
CALLOUT_TRANS = {
    "Catch my breath": "riprendere fiato",
    "Hold this flashlight steady": "tieni ferma questa torcia",
    "pipe joint": "giunto del tubo",
    "turn off": "chiudere, spegnere",
    "Did you turn off": "hai chiuso",
    "heavy wrench": "chiave inglese pesante",
    "This big iron one": "questa grande di ferro",
    "Here you go": "ecco a te",
    "fits": "combacia, entra su misura",
    "brass thread": "filettatura d'ottone",
    "No drips at all": "neanche una goccia",
    "light the boiler": "accendere la caldaia",
    "slowly": "lentamente, piano",
    "not too fast": "non troppo in fretta",
    "is rushing in": "sta entrando con forza",
    "there goes": "ecco che parte",
    "how it should be": "come dovrebbe essere",
    "is warming up": "si sta scaldando",
    "reach the third floor": "arrivare al terzo piano",
}
