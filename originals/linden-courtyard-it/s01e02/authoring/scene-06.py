# Authoring module for linden-courtyard-it-s01e02-scene-06.
ID = "linden-courtyard-it-s01e02-scene-06"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = "The Friday Caller  (La telefonata del venerdì)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"hannah": "Hannah", "graham": "Graham"}
INTRO = "Finita la colazione, l'ingresso ritrova la quiete mentre Hannah aggiorna il registro di carta e Graham lubrifica il cardine della porta. A un tratto squilla il telefono sul bancone. Ascoltiamo la scena."
OPENER = "Seguiamo da vicino ogni passaggio di questa telefonata misteriosa."
TRANSITION = "Riascoltiamo ora tutta la conversazione di fila."
OUTRO = "Adesso c'è un appuntamento preciso — venerdì a mezzogiorno — e una voce agitata al telefono che rifiuta di dire il proprio nome. Ci vediamo nella prossima scena."
CLOSING = ("hannah", "Bye for now!")
STORY = [
    ("hannah", "Linden Courtyard Inn, good morning! Hannah speaking.", "Locanda del Cortile del Tiglio, buongiorno! Parla Hannah."),
    ("graham", "Who is it? Another booking for the weekend?", "Chi è? Un'altra prenotazione per il fine settimana?"),
    ("hannah", "Wait, hello, sir! You are calling about the dark blue suitcase?", "Aspetti, pronto, signore! Chiama per la valigia blu scuro?"),
    ("graham", "Ask him his name! Write it down!", "Chiedigli come si chiama! Prendi nota!"),
    ("hannah", "Yes, sir, we locked your bag safely in our closet. What is your name, please?", "Sì, signore, abbiamo chiuso la sua valigia al sicuro nel nostro ripostiglio. Come si chiama, per favore?"),
    ("graham", "What is he saying? Why are you frowning?", "Che cosa sta dicendo? Perché aggrotti la fronte?"),
    ("hannah", "Sir? He says, 'Please do not open the white paper package. I will come Friday at noon.'", "Signore? Dice: «Per favore non aprite il pacchetto di carta bianca. Verrò venerdì a mezzogiorno.»"),
    ("graham", "Give me the phone, let me ask him properly!", "Passami il telefono, lascia che glielo chieda io come si deve!"),
    ("hannah", "Too late! He said 'Thank you' and hung up!", "Troppo tardi! Ha detto «Grazie» e ha riattaccato!"),
    ("graham", "Polite voice? Young or old?", "Voce educata? Giovane o anziana?"),
    ("hannah", "Quiet, polite, maybe thirty-five. He sounded nervous, not angry.", "Pacata, gentile, forse sui trentacinque anni. Sembrava nervoso, non arrabbiato."),
    ("graham", "Nervous about a wooden toy train? This story gets stranger every hour.", "Nervoso per un trenino giocattolo di legno? Questa storia diventa più strana di ora in ora."),
]
WALK = [
    (0, None, ["'Locanda del Cortile del Tiglio, buongiorno! Parla Hannah.' Rispondendo al telefono di lavoro ci si presenta col proprio nome seguito dal participio presente in", (None, "Hannah speaking"), "parla Hannah."]),
    (1, None, ["'Chi è? Un'altra prenotazione per il fine settimana?' Al telefono o dietro una porta chiusa l'inglese usa il soggetto neutro singolare:", (None, "Who is it"), "finché non si conosce l'identità della persona."]),
    (2, None, ["'Aspetti, pronto, signore! Chiama per la valigia blu scuro?' Qui Hannah conserva l'ordine affermativo in", (None, "You are calling about"), "affidando tutta la sorpresa della domanda all'intonazione della voce."]),
    (3, None, ["'Chiedigli come si chiama! Prendi nota!' Per dire annotalo o scrivilo su carta il verbo si accompagna sempre alla particella verso il basso:", (None, "Write it down"), "col pronome al centro."]),
    (4, None, ["'Sì, signore, abbiamo chiuso la sua valigia al sicuro nel nostro ripostiglio. Come si chiama, per favore?' Dove noi diciamo come si chiama, l'inglese chiede qual è il suo nome con", (None, "What is your name"), "in modo diretto e universale."]),
    (5, None, ["'Che cosa sta dicendo? Perché aggrotti la fronte?' Un unico verbo espressivo,", (None, "frowning"), "descrive il gesto di aggrottare le sopracciglia in questo preciso istante."]),
    (6, None, ["'Signore? Dice: «Per favore non aprite il pacchetto di carta bianca. Verrò venerdì a mezzogiorno.»' Per indicare le dodici esatte di giorno l'inglese ricorre alla preposizione puntuale in", (None, "at noon"), "a mezzogiorno."]),
    (7, None, ["'Passami il telefono, lascia che glielo chieda io come si deve!' L'avverbio", (None, "properly"), "significa come si deve, nel modo corretto e completo."]),
    (8, None, ["'Troppo tardi! Ha detto «Grazie» e ha riattaccato!' Chiudere una telefonata conserva l'immagine delle vecchie cornette appese al muro nel passato irregolare", (None, "hung up"), "ha riagganciato."]),
    (9, None, ["'Voce educata? Giovane o anziana?' Nel parlato rapido Graham riduce la domanda all'osso coi due aggettivi opposti:", (None, "Young or old"), "giovane o anziano."]),
    (10, None, ["'Pacata, gentile, forse sui trentacinque anni. Sembrava nervoso, non arrabbiato.' Per descrivere l'impressione lasciata da una voce al telefono si usa", (None, "sounded nervous"), "seguito subito dall'aggettivo."]),
    (11, None, ["'Nervoso per un trenino giocattolo di legno? Questa storia diventa più strana di ora in ora.' Per esprimere un cambiamento graduale il verbo diventare si unisce al comparativo in", (None, "gets stranger"), "diventa più strana."]),
]
CALLOUT_TRANS = {
    "Hannah speaking": "parla Hannah",
    "Who is it": "chi è",
    "You are calling about": "chiama per, sta chiamando riguardo a",
    "Write it down": "prendi nota, scrivilo",
    "What is your name": "come si chiama",
    "frowning": "aggrottando la fronte",
    "at noon": "a mezzogiorno",
    "properly": "come si deve",
    "hung up": "ha riattaccato",
    "Young or old": "giovane o anziano",
    "sounded nervous": "sembrava nervoso (dalla voce)",
    "gets stranger": "diventa più strana",
}
