# Authoring module for linden-courtyard-it-s01e06-scene-06.
ID = "linden-courtyard-it-s01e06-scene-06"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 6
SCENE = 6
TITLE = "Permanent Keys  (Chiavi definitive)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"arthur": "Arthur", "tessa": "Tessa", "hannah": "Hannah"}
INTRO = "Nel luminoso angolo caffetteria della Locanda del Cortile del Tiglio, Arthur si pianta dritto davanti a Tessa e Hannah stringendo ancora il secondo foglio della lettera con un sorriso radioso. Ascoltiamo prima la scena."
OPENER = "Ora ripercorriamo il dialogo con calma, battuta per battuta."
TRANSITION = "Ascoltiamo di nuovo l'intera scena a ritmo normale."
OUTRO = "Una caffetteria aperta al quartiere per Tessa e un posto fisso come responsabile della ricezione per Hannah! Nella prossima scena scende la sera e si accendono le lanterne del cortile. A tra poco."
CLOSING = ("arthur", "See you later!")
STORY = [
    ("arthur", "Tessa, how many cinnamon rolls and lemon cakes can your oven bake each morning?", "Tessa, quante girelle alla cannella e torte al limone riesce a sfornare il tuo forno ogni mattina?"),
    ("tessa", "Double what I make now! Are we really opening the courtyard cafe to our street?", "Il doppio di quello che preparo adesso! Apriamo davvero la caffetteria del cortile alla nostra via?"),
    ("arthur", "Starting tomorrow at eight! Four tables inside, three tables under the tree!", "A partire da domani alle otto! Quattro tavoli dentro, tre tavoli sotto l'albero!"),
    ("tessa", "My dream cafe, right here in our own courtyard! Wait until I tell the baker's market!", "La caffetteria dei miei sogni, proprio qui nel nostro cortile! Aspettate che lo racconti al mercato dei fornai!"),
    ("arthur", "And now, Hannah, today is Friday, the last day of your five day trial week.", "E ora, Hannah, oggi è venerdì, l'ultimo giorno della tua settimana di prova di cinque giorni."),
    ("hannah", "Oh! With the suitcases, the boiler, and the letter, I completely forgot!", "Oh! Tra le valigie, la caldaia e la lettera, me n'ero completamente dimenticata!"),
    ("arthur", "On Monday you opened our tricky door; since then you saved rooms, pipes, breakfast, and our lease.", "Lunedì hai aperto la nostra porta capricciosa; da allora hai salvato camere, tubature, colazione e il nostro contratto d'affitto."),
    ("tessa", "If you do not hire her full time, Arthur, I am hiring her in my kitchen!", "Se non la assumi a tempo pieno, Arthur, la assumo io nella mia cucina!"),
    ("arthur", "Hands off, Tessa! Hannah, would you stay as our permanent front desk manager?", "Giù le mani, Tessa! Hannah, resteresti come nostra responsabile stabile della ricezione?"),
    ("hannah", "Stay here with all of you? Yes, a hundred times yes!", "Restare qui con tutti voi? Sì, cento volte sì!"),
    ("arthur", "Wonderful! Your name goes in Graham's big paper book in permanent ink!", "Meraviglioso! Il tuo nome entra nel grande registro di carta di Graham con inchiostro indelebile!"),
    ("hannah", "Best first week of my life!", "La migliore prima settimana della mia vita!"),
]
WALK = [
    (0, None, ["'Tessa, quante girelle alla cannella e torte al limone riesce a sfornare il tuo forno ogni mattina?' Con sostantivi plurali numerabili la quantità si chiede sempre con", (None, "how many"), "seguito dai profumatissimi", (None, "cinnamon rolls"), "dolcetti arrotolati alla cannella."]),
    (1, None, ["'Il doppio di quello che preparo adesso! Apriamo davvero la caffetteria del cortile alla nostra via?' Senza preposizioni intermedie, la risposta entusiasta lega direttamente", (None, "Double what I make now"), "il doppio di ciò che preparo ora."]),
    (2, None, ["'A partire da domani alle otto! Quattro tavoli dentro, tre tavoli sotto l'albero!' Per fissare il momento esatto in cui parte una novità si usa il participio iniziale in", (None, "Starting tomorrow at eight"), "a cominciare da domani alle otto."]),
    (3, None, ["'La caffetteria dei miei sogni, proprio qui nel nostro cortile! Aspettate che lo racconti al mercato dei fornai!' Il sostantivo per sogno fa da aggettivo in", (None, "dream cafe"), "e la gioia impaziente brilla in", (None, "Wait until I tell"), "aspettate che lo dica."]),
    (4, None, ["'E ora, Hannah, oggi è venerdì, l'ultimo giorno della tua settimana di prova di cinque giorni.' Nel mondo del lavoro il periodo iniziale di inserimento si chiama", (None, "trial week"), "settimana di prova."]),
    (5, None, ["'Oh! Tra le valigie, la caldaia e la lettera, me n'ero completamente dimenticata!' In inglese il verbo dimenticare non richiede pronomi riflessivi né particelle, come senti in", (None, "completely forgot"), "ho dimenticato del tutto."]),
    (6, None, ["'Lunedì hai aperto la nostra porta capricciosa; da allora hai salvato camere, tubature, colazione e il nostro contratto d'affitto.' Qualcosa che richiede un piccolo trucco per aprirsi è una", (None, "tricky door"), "e il tempo trascorso da quel momento è", (None, "since then"), "da allora."]),
    (7, None, ["'Se non la assumi a tempo pieno, Arthur, la assumo io nella mia cucina!' L'orario lavorativo completo si esprime con le due parole asciutte", (None, "full time"), "a tempo pieno."]),
    (8, None, ["'Giù le mani, Tessa! Hannah, resteresti come nostra responsabile stabile della ricezione?' Dopo lo scherzoso", (None, "Hands off"), "Arthur formula la proposta professionale col condizionale cortese", (None, "would you stay"), "ti fermeresti."]),
    (9, None, ["'Restare qui con tutti voi? Sì, cento volte sì!' Per moltiplicare un sì pieno di entusiasmo l'inglese premette l'articolo indeterminativo in", (None, "a hundred times yes"), "cento volte sì."]),
    (10, None, ["'Meraviglioso! Il tuo nome entra nel grande registro di carta di Graham con inchiostro indelebile!' Per indicare il mezzo con cui si scrive su un foglio si usa la preposizione interna:", (None, "in permanent ink"), "con inchiostro indelebile."]),
    (11, None, ["'La migliore prima settimana della mia vita!' Nelle esclamazioni spontanee cade spesso l'articolo iniziale lasciando svettare il superlativo in", (None, "Best first week"), "la migliore prima settimana."]),
]
CALLOUT_TRANS = {
    "how many": "quante, quanti",
    "cinnamon rolls": "girelle alla cannella",
    "Double what I make now": "il doppio di quello che preparo adesso",
    "Starting tomorrow at eight": "a partire da domani alle otto",
    "dream cafe": "caffetteria dei sogni",
    "Wait until I tell": "aspettate che lo racconti",
    "trial week": "settimana di prova",
    "completely forgot": "me n'ero completamente dimenticata",
    "tricky door": "porta capricciosa, con il trucco",
    "since then": "da allora",
    "full time": "a tempo pieno",
    "Hands off": "giù le mani",
    "would you stay": "resteresti",
    "a hundred times yes": "cento volte sì",
    "in permanent ink": "con inchiostro indelebile",
    "Best first week": "la migliore prima settimana",
}
