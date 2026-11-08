# Authoring module for linden-courtyard-it-s01e03-scene-05.
ID = "linden-courtyard-it-s01e03-scene-05"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 3
SCENE = 5
TITLE = "Half Price and Quiet Beams  (Metà prezzo e travi silenziose)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"hannah": "Hannah", "caleb": "Caleb", "graham": "Graham"}
INTRO = "Graham porta la borsa da viaggio di Caleb fino al terzo piano mentre Hannah apre la porta della soffitta appena sistemata. Tutti trattengono il fiato aspettando il giudizio di Caleb. Ascolta prima tutta la scena."
OPENER = "Rivediamo con calma ogni battuta di questa visita in soffitta."
TRANSITION = "Riascoltiamo ora tutta la scena a velocità naturale."
OUTRO = "Altro che recensione arrabbiata: Caleb è rimasto incantato dalle travi di quercia vecchie di ottant'anni. Nella prossima scena torniamo giù al bancone d'ingresso. A presto."
CLOSING = ("hannah", "Good night!")
STORY = [
    ("hannah", "Here we are, sir. Watch your head on this low wooden beam.", "Eccoci arrivati, signore. Attento alla testa sotto questa trave bassa di legno."),
    ("caleb", "Oh... look at the proportions of this timber roof!", "Oh... guardate le proporzioni di questo tetto a travi di legno!"),
    ("graham", "Solid oak, eighty years old. Not a single leak.", "Quercia massiccia, ottant'anni d'età. Nemmeno una singola infiltrazione."),
    ("hannah", "Because of our mistake, tonight is half price, with breakfast included.", "A causa del nostro errore, stanotte è a metà prezzo, con colazione inclusa."),
    ("caleb", "Listen for a second... you cannot hear a single car from the street.", "Ascoltate un secondo... non si sente nemmeno un'auto dalla strada."),
    ("hannah", "Only the courtyard tree and the rain.", "Solo l'albero del cortile e la pioggia."),
    ("caleb", "To tell you the truth, I hate noisy first floor rooms. I love this space!", "A dirvi la verità, detesto le camere rumorose al pianterreno. Adoro questo spazio!"),
    ("graham", "Really? You do not mind the extra stairs?", "Davvero? Non le pesano le scale in più?"),
    ("caleb", "Not at all! And this wide desk under the window is ideal for my work.", "Per niente! E questa scrivania ampia sotto la finestra è ideale per il mio lavoro."),
    ("hannah", "What a relief! Here is your silver key, Caleb.", "Che sollievo! Ecco la sua chiave d'argento, Caleb."),
    ("caleb", "Thank you both for being honest instead of sending me back into the rain.", "Grazie a entrambi per essere stati sinceri invece di rimandarmi fuori sotto la pioggia."),
    ("graham", "Sleep well, sir. Breakfast starts at seven thirty downstairs.", "Dorma bene, signore. La colazione inizia alle sette e trenta di sotto."),
]
WALK = [
    (0, None, ["'Eccoci arrivati, signore. Attento alla testa sotto questa trave bassa di legno.' Quando arrivi a destinazione usi", (None, "Here we are"), "mentre", (None, "Watch your head"), "è l'avviso fisso per non battere la testa."]),
    (1, None, ["'Oh... guardate le proporzioni di questo tetto a travi di legno!' Nelle costruzioni e nell'architettura, il legname strutturale da carpenteria si chiama", (None, "timber roof"), "tetto in travatura di legno."]),
    (2, None, ["'Quercia massiccia, ottant'anni d'età. Nemmeno una singola infiltrazione.' Per indicare l'età di persone o edifici l'inglese chiude con l'aggettivo vecchio in", (None, "eighty years old"), "anziché usare il verbo avere."]),
    (3, None, ["'A causa del nostro errore, stanotte è a metà prezzo, con colazione inclusa.' Quando introduci un motivo con un sostantivo anziché un verbo usi la coppia", (None, "Because of"), "a causa di."]),
    (4, None, ["'Ascoltate un secondo... non si sente nemmeno un'auto dalla strada.' Per rendere la forma impersonale italiana non si sente, l'inglese usa il pronome generico in", (None, "you cannot hear"), "non si riesce a sentire."]),
    (5, None, ["'Solo l'albero del cortile e la pioggia.' Nel nome composto", (None, "courtyard tree"), "il cortile precede l'albero senza bisogno della preposizione del."]),
    (6, None, ["'A dirvi la verità, detesto le camere rumorose al pianterreno. Adoro questo spazio!' Per fare una confidenza sincera l'espressione idiomatica d'apertura è", (None, "To tell you the truth"), "a dirla tutta."]),
    (7, None, ["'Davvero? Non le pesano le scale in più?' Chiedere se qualcosa dà fastidio o dispiace si costruisce con", (None, "You do not mind"), "non le dispiace."]),
    (8, None, ["'Per niente! E questa scrivania ampia sotto la finestra è ideale per il mio lavoro.' Una risposta entusiasta e rassicurante a chi teme di disturbare è", (None, "Not at all"), "nient'affatto, figuriamoci."]),
    (9, None, ["'Che sollievo! Ecco la sua chiave d'argento, Caleb.' Anche con la parola sollievo l'esclamazione vuole l'articolo indeterminativo in", (None, "What a relief"), "che sollievo."]),
    (10, None, ["'Grazie a entrambi per essere stati sinceri invece di rimandarmi fuori sotto la pioggia.' Nota come la locuzione", (None, "instead of sending"), "regga subito il gerundio inglese invece dell'infinito italiano."]),
    (11, None, ["'Dorma bene, signore. La colazione inizia alle sette e trenta di sotto.' L'augurio affettuoso e cortese prima di andare a letto è semplicemente", (None, "Sleep well"), "dorma bene."]),
]
CALLOUT_TRANS = {
    "Here we are": "eccoci arrivati",
    "Watch your head": "attento alla testa",
    "timber roof": "tetto in travi di legno",
    "eighty years old": "di ottant'anni",
    "Because of": "a causa di",
    "you cannot hear": "non si sente",
    "courtyard tree": "albero del cortile",
    "To tell you the truth": "a dirvi la verità",
    "You do not mind": "non le dispiace, non le pesa",
    "Not at all": "per niente, figuriamoci",
    "What a relief": "che sollievo",
    "instead of sending": "invece di rimandare",
    "Sleep well": "dorma bene",
}
