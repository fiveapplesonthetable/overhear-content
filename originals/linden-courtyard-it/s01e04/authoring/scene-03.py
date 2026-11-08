# Authoring module for linden-courtyard-it-s01e04-scene-03.
ID = "linden-courtyard-it-s01e04-scene-03"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 4
SCENE = 3
TITLE = "Hot Cinnamon Rolls  (Girelle calde alla cannella)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"tessa": "Tessa", "evelyn": "Evelyn", "arthur": "Arthur"}
INTRO = "Di ritorno alla locanda, la signorina Evelyn scende alle sette e dieci cercando una tazza di tè prima di prepararsi. Tessa e Arthur si scambiano uno sguardo d'intesa e avviano il loro piano di distrazione. Ascolta prima la scena."
OPENER = "Esaminiamo ora le espressioni di questa colazione improvvisata."
TRANSITION = "Riascoltiamo la conversazione completa con naturalezza."
OUTRO = "Le girelle calde alla cannella hanno regalato esattamente i dieci minuti necessari mentre Hannah entrava di corsa dal cancello del cortile. Nella prossima scena scendiamo nel locale caldaia."
CLOSING = ("tessa", "See you later!")
STORY = [
    ("evelyn", "Good morning! Something smells like warm cinnamon all the way upstairs!", "Buongiorno! Qualcosa profuma di cannella calda fin lassù di sopra!"),
    ("tessa", "Good morning, Miss Evelyn! My cinnamon rolls just came out of the oven.", "Buongiorno, signorina Evelyn! Le mie girelle alla cannella sono appena uscite dal forno."),
    ("arthur", "Sit right down by the sunny window, ma'am! No rush to go upstairs yet!", "Si accomodi pure qui vicino alla finestra soleggiata, signora! Nessuna fretta di salire ancora!"),
    ("evelyn", "Actually, I only came down to ask why the bathroom tap felt so chilly.", "In realtà sono scesa solo per chiedere perché il rubinetto del bagno sembrava così freddo."),
    ("arthur", "Chilly? Ah, yes! Our neighborhood water pipes take a gentle morning stretch!", "Freddino? Ah, sì! Le tubature dell'acqua del nostro quartiere fanno un dolce risveglio mattutino!"),
    ("tessa", "Have a hot cup of tea and a cinnamon roll for ten minutes first!", "Prenda prima una tazza di tè caldo e una girella alla cannella per dieci minuti!"),
    ("evelyn", "Well, nobody wise says no to warm cinnamon bread at seven in the morning.", "Beh, nessuna persona saggia dice di no al pane tiepido alla cannella alle sette del mattino."),
    ("arthur", "Wonderful choice! Would you like honey or apple jam beside it?", "Ottima scelta! Gradisce del miele o della confettura di mele accanto?"),
    ("evelyn", "Just a little butter, thank you. Why are you looking at your watch, sir?", "Solo un poco di burro, grazie. Perché sta guardando l'orologio da polso, signore?"),
    ("arthur", "Me? Oh, I simply love being on time! Seven fourteen is a beautiful minute!", "Io? Oh, adoro semplicemente essere puntuale! Le sette e quattordici sono un minuto splendido!"),
    ("tessa", "Look through the courtyard window, Arthur. Someone just ran through the gate!", "Guarda dalla finestra sul cortile, Arthur. Qualcuno è appena entrato di corsa dal cancello!"),
    ("arthur", "Saved! Excuse me one moment, ma'am, enjoy your hot tea!", "Salvi! Mi scusi un istante, signora, si goda il suo tè caldo!"),
]
WALK = [
    (0, None, ["'Buongiorno! Qualcosa profuma di cannella calda fin lassù di sopra!' Per dire che una cosa ha il profumo di un'altra si usa", (None, "smells like"), "mentre", (None, "all the way upstairs"), "enfatizza la distanza fin su ai piani alti."]),
    (1, None, ["'Buongiorno, signorina Evelyn! Le mie girelle alla cannella sono appena uscite dal forno.' I dolci arrotolati tipici della colazione si chiamano", (None, "cinnamon rolls"), "e", (None, "came out of"), "rende il movimento di uscita dal forno."]),
    (2, None, ["'Si accomodi pure qui vicino alla finestra soleggiata, signora! Nessuna fretta di salire ancora!' L'avverbio nel mezzo di", (None, "Sit right down"), "rende l'invito più caloroso e immediato, mentre", (None, "No rush"), "significa senza alcuna fretta."]),
    (3, None, ["'In realtà sono scesa solo per chiedere perché il rubinetto del bagno sembrava così freddo.' Attenzione al falso amico", (None, "Actually"), "che significa in realtà e non attualmente, mentre", (None, "chilly"), "indica un freddo pungente al tatto."]),
    (4, None, ["'Freddino? Ah, sì! Le tubature dell'acqua del nostro quartiere fanno un dolce risveglio mattutino!' Tre sostantivi compongono", (None, "neighborhood water pipes"), "le condutture idriche del rione."]),
    (5, None, ["'Prenda prima una tazza di tè caldo e una girella alla cannella per dieci minuti!' Quando offri cibi o bevande al tavolo, l'inglese preferisce", (None, "Have a hot cup"), "al posto del verbo prendere letterale."]),
    (6, None, ["'Beh, nessuna persona saggia dice di no al pane tiepido alla cannella alle sette del mattino.' Coi pronomi indefiniti composti come", (None, "nobody wise"), "l'aggettivo si colloca eccezionalmente dopo il pronome, proprio come in italiano."]),
    (7, None, ["'Ottima scelta! Gradisce del miele o della confettura di mele accanto?' Per fare un'offerta cortese a tavola la formula d'oro è", (None, "Would you like"), "seguita qui da", (None, "apple jam"), "marmellata di mele."]),
    (8, None, ["'Solo un poco di burro, grazie. Perché sta guardando l'orologio da polso, signore?' L'orologio che si porta al polso si chiama", (None, "watch"), "ben distinto da quello appeso alla parete, e", (None, "a little butter"), "indica una piccola quantità."]),
    (9, None, ["'Io? Oh, adoro semplicemente essere puntuale! Le sette e quattordici sono un minuto splendido!' Essere in perfetto orario si esprime con", (None, "being on time"), "e notare che un orario intero è trattato al singolare con", (None, "is"), "è."]),
    (10, None, ["'Guarda dalla finestra sul cortile, Arthur. Qualcuno è appena entrato di corsa dal cancello!' Guardare attraverso un vetro o varcare un ingresso usa due volte", (None, "through"), "che esprime il passaggio da parte a parte."]),
    (11, None, ["'Salvi! Mi scusi un istante, signora, si goda il suo tè caldo!' Per congedarsi un attimo con garbo dici", (None, "Excuse me one moment"), "e auguri buon proseguimento con", (None, "enjoy"), "si goda."]),
]
CALLOUT_TRANS = {
    "smells like": "profuma di, sa di",
    "all the way upstairs": "fin lassù di sopra",
    "cinnamon rolls": "girelle alla cannella",
    "came out of": "sono uscite da",
    "Sit right down": "si sieda pure qui",
    "No rush": "nessuna fretta",
    "Actually": "in realtà",
    "chilly": "freddino, gelido",
    "neighborhood water pipes": "tubature dell'acqua del quartiere",
    "Have a hot cup": "prenda una tazza calda",
    "nobody wise": "nessuna persona saggia",
    "Would you like": "gradirebbe, vorrebbe",
    "apple jam": "confettura di mele",
    "watch": "orologio da polso",
    "a little butter": "un poco di burro",
    "being on time": "essere puntuale",
    "is": "è",
    "through": "attraverso, da",
    "Excuse me one moment": "mi scusi un momento",
    "enjoy": "si goda",
}
