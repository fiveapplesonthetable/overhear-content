# Authoring module for linden-courtyard-it-s01e01-scene-06.
ID = "linden-courtyard-it-s01e01-scene-06"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = "The Luggage Tag  (L'etichetta del bagaglio)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"hannah": "Hannah", "evelyn": "Evelyn", "arthur": "Arthur"}
INTRO = "Tornati al bancone d'ingresso, Hannah, Evelyn e il proprietario Arthur si chinano sulla valigia blu sotto la lampada da tavolo. Finalmente Arthur mette a frutto i suoi occhiali. Ascolta prima tutta la scena."
OPENER = "Esaminiamo adesso ogni battuta con calma."
TRANSITION = "Riascoltiamo di nuovo l'intero scambio a passo normale."
OUTRO = "Dalla stazione non ci sono ancora notizie, e il misterioso proprietario abita a soli cinque minuti da lì. Nella prossima scena Tessa interviene per salvare la serata di Evelyn."
CLOSING = ("arthur", "See you soon!")
STORY = [
    ("arthur", "Dear me, what a mix-up! Let me look at the tag with my glasses.", "Mamma mia, che pasticcio! Mi faccia guardare l'etichetta con i miei occhiali."),
    ("evelyn", "Is there a name or a phone number on it?", "C'è un nome o un numero di telefono sopra?"),
    ("arthur", "No phone number, unfortunately. Only two initials and an old street name.", "Nessun numero di telefono, purtroppo. Solo due iniziali e il nome di una vecchia via."),
    ("hannah", "Wait, that street is right here in our neighborhood, five minutes away!", "Aspettate, quella via è proprio qui nel nostro quartiere, a cinque minuti da qui!"),
    ("evelyn", "How strange! We rode the same morning train to the same district.", "Che strano! Abbiamo preso lo stesso treno del mattino verso lo stesso quartiere."),
    ("arthur", "Hannah, call the station lost and found office right away.", "Hannah, chiama subito l'ufficio oggetti smarriti della stazione."),
    ("hannah", "I am dialing now... Hello? Did anyone report a swapped blue suitcase?", "Sto componendo il numero... Pronto? Qualcuno ha segnalato una valigia blu scambiata?"),
    ("evelyn", "Tell them mine has a red ribbon inside the top pocket!", "Riferisci pure che la mia ha un nastro rosso dentro la tasca superiore!"),
    ("hannah", "Not yet? Please take our guesthouse number and address. Thank you!", "Non ancora? La prego, prenda il numero e l'indirizzo della nostra locanda. Grazie!"),
    ("arthur", "They have nothing yet, ma'am, I am terribly sorry.", "Non hanno ancora nulla, signora, sono terribilmente dispiaciuto."),
    ("evelyn", "It is not your fault. Still, I only have the coat on my back!", "Non è colpa sua. Eppure ho solo il cappotto che porto addosso!"),
    ("hannah", "Wait one moment, Tessa in the cafe just waved to me with an idea!", "Un attimo, Tessa dalla caffetteria mi ha appena fatto cenno con la mano: ha un'idea!"),
]
WALK = [
    (0, None, ["'Mamma mia, che pasticcio! Mi faccia guardare l'etichetta con i miei occhiali.' Nelle esclamazioni con un nome numerabile singolare l'inglese inserisce sempre l'articolo indeterminativo in", (None, "what a mix-up"), "e usa", (None, "look at"), "per puntare lo sguardo."]),
    (1, None, ["'C'è un nome o un numero di telefono sopra?' Per trasformare c'è in una domanda basta scambiare l'ordine delle prime due parole in", (None, "Is there"), "proprio come nelle altre frasi interrogative."]),
    (2, None, ["'Nessun numero di telefono, purtroppo. Solo due iniziali e il nome di una vecchia via.' Mettere la negazione direttamente davanti al sostantivo in", (None, "No phone number"), "equivale al nostro nessun numero di telefono."]),
    (3, None, ["'Aspettate, quella via è proprio qui nel nostro quartiere, a cinque minuti da qui!' Chiudere l'indicazione di tempo o spazio con l'avverbio finale in", (None, "five minutes away"), "esprime subito la distanza da dove ti trovi."]),
    (4, None, ["'Che strano! Abbiamo preso lo stesso treno del mattino verso lo stesso quartiere.' Davanti a un aggettivo isolato l'esclamazione si costruisce con", (None, "How strange"), "mentre", (None, "rode"), "è il passato irregolare per viaggiare su un mezzo."]),
    (5, None, ["'Hannah, chiama subito l'ufficio oggetti smarriti della stazione.' Il reparto degli oggetti smarriti si chiama ovunque con la coppia fissa", (None, "lost and found"), "letteralmente perduto e ritrovato."]),
    (6, None, ["'Sto componendo il numero... Pronto? Qualcuno ha segnalato una valigia blu scambiata?' Nelle domande al passato,", (None, "Did anyone report"), "affida il tempo passato all'ausiliare iniziale e lascia il verbo principale alla forma base."]),
    (7, None, ["'Riferisci pure che la mia ha un nastro rosso dentro la tasca superiore!' Il pronome indipendente", (None, "mine"), "sostituisce la mia valigia senza mai volere l'articolo determinativo davanti."]),
    (8, None, ["'Non ancora? La prego, prenda il numero e l'indirizzo della nostra locanda. Grazie!' Due parole rapidissime al telefono,", (None, "Not yet"), "bastano sia per chiedere sia per rispondere non ancora."]),
    (9, None, ["'Non hanno ancora nulla, signora, sono terribilmente dispiaciuto.' Per scusarsi con estrema cortesia,", (None, "terribly sorry"), "rafforza le scuse con calore ed eleganza."]),
    (10, None, ["'Non è colpa sua. Eppure ho solo il cappotto che porto addosso!' Tieni pronta questa frase gentile per togliere dall'imbarazzo chi ti aiuta:", (None, "It is not your fault"), "non è colpa sua."]),
    (11, None, ["'Un attimo, Tessa dalla caffetteria mi ha appena fatto cenno con la mano: ha un'idea!' Nell'inglese americano l'avverbio col passato semplice in", (None, "just waved"), "esprime benissimo un'azione appena accaduta."]),
]
CALLOUT_TRANS = {
    "what a mix-up": "che pasticcio, che confusione",
    "look at": "guardare",
    "Is there": "c'è",
    "No phone number": "nessun numero di telefono",
    "five minutes away": "a cinque minuti di distanza",
    "How strange": "che strano",
    "rode": "abbiamo viaggiato su, abbiamo preso",
    "lost and found": "oggetti smarriti",
    "Did anyone report": "qualcuno ha segnalato",
    "mine": "la mia",
    "Not yet": "non ancora",
    "terribly sorry": "terribilmente dispiaciuto",
    "It is not your fault": "non è colpa sua",
    "just waved": "ha appena salutato con la mano",
}
