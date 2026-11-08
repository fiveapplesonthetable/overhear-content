# Authoring module for linden-courtyard-it-s01e02-scene-05.
ID = "linden-courtyard-it-s01e02-scene-05"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 2
SCENE = 5
TITLE = "Juice on the Tie  (Succo sulla cravatta)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"arthur": "Arthur", "evelyn": "Evelyn", "hannah": "Hannah"}
INTRO = "La colazione è nel vivo nel luminoso angolo caffetteria. Evelyn siede vicino alla finestra mentre Arthur insiste per aiutare Hannah a servire le bevande come il direttore di un grande albergo. Ascolta prima tutta la scena."
OPENER = "Ripassiamo ogni battuta di questa scena a tavola."
TRANSITION = "Ascoltiamo di nuovo l'intera scena senza interruzioni."
OUTRO = "Evelyn ha gradito moltissimo la colazione, anche se la cravatta di Arthur si è bevuta quasi tutta la spremuta d'arancia. Tra poco il telefono del bancone porterà novità sulla valigia misteriosa. Alla prossima."
CLOSING = ("evelyn", "Take care!")
STORY = [
    ("hannah", "Good morning again, Miss Evelyn! Would you like coffee or black tea?", "Buongiorno di nuovo, signorina Evelyn! Gradisce caffè o tè nero?"),
    ("evelyn", "Black tea without sugar, please, and one slice of warm bread.", "Tè nero senza zucchero, per favore, e una fetta di pane tiepido."),
    ("arthur", "Allow me to pour the fresh orange juice, ma'am!", "Mi permetta di versarle la spremuta fresca d'arancia, signora!"),
    ("evelyn", "Oh, how kind of you, sir. Just half a glass.", "Oh, che gentile da parte sua, signore. Solo mezzo bicchiere."),
    ("arthur", "At our guesthouse, five-star service comes naturally... whoops!", "Nella nostra locanda, il servizio a cinque stelle viene naturale... ops!"),
    ("hannah", "Careful, Arthur, the pitcher spout is wide!", "Attento, Arthur, il beccuccio della brocca è largo!"),
    ("arthur", "Oh dear! Not a drop on the table, thank goodness... all of it is on my tie!", "Povero me! Neanche una goccia sul tavolo, meno male... è finito tutto sulla mia cravatta!"),
    ("evelyn", "Do not worry! Cold sparkling water takes orange juice right out.", "Non si preoccupi! L'acqua fredda frizzante toglie subito il succo d'arancia."),
    ("hannah", "Here is a clean cloth and cold water, Arthur.", "Ecco un panno pulito e dell'acqua fredda, Arthur."),
    ("arthur", "Excuse me, ma'am, I shall retreat to my office with dignity!", "Mi scusi, signora, mi ritirerò nel mio ufficio con dignità!"),
    ("evelyn", "The scrambled eggs are delicious, Hannah. Tell Tessa my compliments!", "Le vostre uova strapazzate sono squisite, Hannah. Faccia i miei complimenti a Tessa!"),
    ("hannah", "I will! Enjoy your morning.", "Sarà fatto! Buona mattinata."),
]
WALK = [
    (0, None, ["'Buongiorno di nuovo, signorina Evelyn! Gradisce caffè o tè nero?' Per offrire da bere o da mangiare con garbo, la formula regina è", (None, "Would you like"), "molto più cortese di una domanda diretta col verbo volere."]),
    (1, None, ["'Tè nero senza zucchero, per favore, e una fetta di pane tiepido.' Poiché il pane in inglese non si conta mai a unità intere col semplice articolo, si chiede una porzione precisa con", (None, "one slice of warm bread"), "una fetta di pane tiepido."]),
    (2, None, ["'Mi permetta di versarle la spremuta fresca d'arancia, signora!' Nel registro più premuroso e formale,", (None, "Allow me to pour"), "unisce il permesso cortese al gesto di versare."]),
    (3, None, ["'Oh, che gentile da parte sua, signore. Solo mezzo bicchiere.' Ringraziare con", (None, "how kind of you"), "è pura eleganza, e osserva la posizione dell'articolo dopo la metà in", (None, "half a glass"), "mezzo bicchiere."]),
    (4, None, ["'Nella nostra locanda, il servizio a cinque stelle viene naturale... ops!' Quando un numero e un nome fanno da aggettivo davanti a un altro nome in", (None, "five-star service"), "la parola stella resta al singolare, e", (None, "whoops"), "è l'esclamazione per un piccolo pasticcio."]),
    (5, None, ["'Attento, Arthur, il beccuccio della brocca è largo!' Per avvisare al volo di fare attenzione basta l'aggettivo isolato", (None, "Careful"), "senza bisogno di alcun verbo."]),
    (6, None, ["'Povero me! Neanche una goccia sul tavolo, meno male... è finito tutto sulla mia cravatta!' L'esclamazione di sollievo", (None, "thank goodness"), "corrisponde al nostro meno male o per fortuna."]),
    (7, None, ["'Non si preoccupi! L'acqua fredda frizzante toglie subito il succo d'arancia.' L'acqua gassata al ristorante o a tavola si chiama", (None, "sparkling water"), "acqua scintillante, mentre", (None, "takes orange juice right out"), "indica smacchiare subito."]),
    (8, None, ["'Ecco un panno pulito e dell'acqua fredda, Arthur.' Il sostantivo", (None, "cloth"), "indica uno strofinaccio o un panno di tessuto pulito per asciugare."]),
    (9, None, ["'Mi scusi, signora, mi ritirerò nel mio ufficio con dignità!' Arthur accentua con autoironia la propria solennità scegliendo", (None, "I shall retreat"), "un futuro ricercato e volutamente teatrale."]),
    (10, None, ["'Le vostre uova strapazzate sono squisite, Hannah. Faccia i miei complimenti a Tessa!' Proprio come in italiano, per congratularsi con chi cucina si usa sempre il plurale in", (None, "my compliments"), "i miei complimenti."]),
    (11, None, ["'Sarà fatto! Buona mattinata.' Per promettere che riferirai un messaggio bastano soggetto e ausiliare futuro:", (None, "I will"), "lo farò senz'altro."]),
]
CALLOUT_TRANS = {
    "Would you like": "gradisce, vorrebbe",
    "one slice of warm bread": "una fetta di pane tiepido",
    "Allow me to pour": "mi permetta di versare",
    "how kind of you": "che gentile da parte sua",
    "half a glass": "mezzo bicchiere",
    "five-star service": "servizio a cinque stelle",
    "whoops": "ops",
    "Careful": "attento, attenzione",
    "thank goodness": "meno male",
    "sparkling water": "acqua frizzante",
    "takes orange juice right out": "toglie subito il succo d'arancia",
    "cloth": "panno, strofinaccio",
    "I shall retreat": "mi ritirerò",
    "my compliments": "i miei complimenti",
    "I will": "lo farò, sarà fatto",
}
