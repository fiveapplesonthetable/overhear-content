# Authoring module for linden-courtyard-it-s01e05-scene-04.
ID = "linden-courtyard-it-s01e05-scene-04"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 5
SCENE = 4
TITLE = "Two Chairs Under the Tree  (Due sedie sotto l'albero)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"tessa": "Tessa", "hannah": "Hannah", "graham": "Graham"}
INTRO = "Alle undici in punto il profumo dolce della torta al limone arriva fino al cortile della Locanda del Cortile del Tiglio, mentre Hannah, Tessa e Graham sistemano un tavolino rotondo sotto i rami dell'albero. Ascoltiamo prima."
OPENER = "Ora rivediamo il dialogo con calma, battuta per battuta."
TRANSITION = "Ascoltiamo un'altra volta tutta la scena per intero."
OUTRO = "Due sedie sotto l'albero, la torta tiepida che riposa sulla griglia e quaranta minuti sul quadrante. Nella prossima scena Hannah aiuta Caleb a scegliere le sue prime parole. A tra poco."
CLOSING = ("hannah", "See you soon!")
STORY = [
    ("hannah", "Let us put the small wooden table right here under the tree, away from the door.", "Mettiamo il tavolino di legno proprio qui sotto l'albero, lontano dalla porta."),
    ("graham", "Good spot. Two solid chairs, facing the garden herbs instead of the lobby window.", "Buon punto. Due sedie robuste, rivolte verso le erbe del giardino invece che verso la vetrata dell'ingresso."),
    ("tessa", "Here is a clean white cloth and two blue teacups.", "Ecco una tovaglia bianca pulita e due tazze da tè blu."),
    ("hannah", "Graham, are you hanging those paper lanterns for noon?", "Graham, stai appendendo quelle lanterne di carta per mezzogiorno?"),
    ("graham", "The wire needed straightening anyway. Nothing sentimental about good maintenance.", "Il filo andava raddrizzato comunque. Non c'è niente di sentimentale in una buona manutenzione."),
    ("tessa", "Oh, listen to Mister Maintenance! Yesterday you fixed the boiler, today you fix two brothers!", "Oh, sentite il Signor Manutenzione! Ieri hai aggiustato la caldaia, oggi aggiusti due fratelli!"),
    ("graham", "I fix pipes and chairs. People have to fix their own words.", "Io riparo tubi e sedie. Le persone devono sistemare da sole le proprie parole."),
    ("hannah", "What time does your watch say now, Graham?", "Che ora segna adesso il tuo orologio, Graham?"),
    ("graham", "Eleven twenty. Cake ready, Tessa?", "Undici e venti. Torta pronta, Tessa?"),
    ("tessa", "Cooling on the rack right now, golden crust and sweet lemon sugar!", "Si sta raffreddando sulla griglia proprio ora: crosta dorata e zucchero dolce al limone!"),
    ("hannah", "Look upstairs at the attic window: Caleb has changed his shirt three times!", "Guardate lassù alla finestra della mansarda: Caleb si è cambiato la camicia tre volte!"),
    ("tessa", "Go talk to him, Hannah, before he wears out the wooden floor!", "Vai a parlargli, Hannah, prima che consumi il pavimento di legno!"),
]
WALK = [
    (0, None, ["'Mettiamo il tavolino di legno proprio qui sotto l'albero, lontano dalla porta.' Una proposta operativa condivisa si apre con", (None, "Let us put"), "mentre la distanza da un punto si indica con", (None, "away from the door"), "lontano dalla porta."]),
    (1, None, ["'Buon punto. Due sedie robuste, rivolte verso le erbe del giardino invece che verso la vetrata dell'ingresso.' Dal nome per viso nasce il participio", (None, "facing"), "orientate verso, contrapposto tramite", (None, "instead of"), "anziché."]),
    (2, None, ["'Ecco una tovaglia bianca pulita e due tazze da tè blu.' Porgendo più oggetti sul tavolo, l'espressione", (None, "Here is"), "si accorda spesso al singolare col primo elemento nominato."]),
    (3, None, ["'Graham, stai appendendo quelle lanterne di carta per mezzogiorno?' Nota l'ordine ordinatissimo di", (None, "paper lanterns"), "dove posizione e materiale vengono entrambi prima del sostantivo."]),
    (4, None, ["'Il filo andava raddrizzato comunque. Non c'è niente di sentimentale in una buona manutenzione.' Con oggetti pratici da riparare, la costruzione", (None, "needed straightening"), "assume valore passivo: aveva bisogno di essere raddrizzato."]),
    (5, None, ["'Oh, sentite il Signor Manutenzione! Ieri hai aggiustato la caldaia, oggi aggiusti due fratelli!' Il verbo ascoltare richiede sempre la preposizione di direzione davanti a chi parla, come in", (None, "listen to"), "ascoltate."]),
    (6, None, ["'Io riparo tubi e sedie. Le persone devono sistemare da sole le proprie parole.' La necessità pratica si esprime con", (None, "have to fix"), "mentre", (None, "their own words"), "sottolinea che spettano a loro in prima persona."]),
    (7, None, ["'Che ora segna adesso il tuo orologio, Graham?' In inglese un orologio da polso dice letteralmente l'ora, come senti nella domanda", (None, "does your watch say"), "che ora segna il tuo orologio."]),
    (8, None, ["'Undici e venti. Torta pronta, Tessa?' Nel parlato quotidiano gli orari si leggono spesso affiancando semplicemente ora e minuti:", (None, "Eleven twenty"), "undici e venti."]),
    (9, None, ["'Si sta raffreddando sulla griglia proprio ora: crosta dorata e zucchero dolce al limone!' Tessa sottintende soggetto e ausiliare partendo direttamente col verbo in", (None, "Cooling on the rack"), "in fase di raffreddamento sulla gratella."]),
    (10, None, ["'Guardate lassù alla finestra della mansarda: Caleb si è cambiato la camicia tre volte!' La direzione verso il piano alto sta tutta in", (None, "Look upstairs"), "e il conteggio delle ripetizioni si chiude con", (None, "three times"), "tre volte."]),
    (11, None, ["'Vai a parlargli, Hannah, prima che consumi il pavimento di legno!' Nell'inglese parlato due verbi di moto e azione si legano senza congiunzione in", (None, "Go talk to him"), "mentre", (None, "wears out"), "significa logorare per il troppo uso."]),
]
CALLOUT_TRANS = {
    "Let us put": "mettiamo",
    "away from the door": "lontano dalla porta",
    "facing": "rivolte verso",
    "instead of": "invece di",
    "Here is": "ecco qui",
    "paper lanterns": "lanterne di carta appese",
    "needed straightening": "andava raddrizzato",
    "listen to": "ascoltate, sentite",
    "have to fix": "devono sistemare",
    "their own words": "le proprie parole",
    "does your watch say": "segna il tuo orologio",
    "Eleven twenty": "undici e venti",
    "Cooling on the rack": "si sta raffreddando sulla griglia",
    "Look upstairs": "guardate lassù, al piano di sopra",
    "three times": "tre volte",
    "Go talk to him": "vai a parlargli",
    "wears out": "consuma, logora",
}
