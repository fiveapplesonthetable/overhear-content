# Authoring module for linden-courtyard-it-s01e02-scene-07.
ID = "linden-courtyard-it-s01e02-scene-07"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 2
SCENE = 7
TITLE = "How Regulars Order  (Come ordinano gli abituali)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"tessa": "Tessa", "hannah": "Hannah", "graham": "Graham"}
INTRO = "Sotto il sole tranquillo del primo pomeriggio, Hannah si concede dieci minuti di pausa nell'angolo caffetteria mentre Tessa pulisce il bancone e Graham stringe la gamba traballante di una sedia di legno. Ascolta prima tutta la scena."
OPENER = "Ripercorriamo con calma ogni battuta di questa pausa pomeridiana."
TRANSITION = "Ascoltiamo di nuovo l'intera scena dall'inizio alla fine."
OUTRO = "Una tazza di caffè in compagnia, una sedia riparata e tre colleghi che ormai formano una vera squadra. Resta un'ultima scena nel secondo episodio, e per Arthur sta per arrivare un bel grattacapo. A tra poco."
CLOSING = ("tessa", "See you later!")
STORY = [
    ("tessa", "Sit down, Hannah! You ran half the city this morning, drink some coffee.", "Siediti, Hannah! Stamattina hai attraversato di corsa mezza città, bevi un caffè."),
    ("hannah", "Gladly! With milk and a little sugar, please.", "Volentieri! Con latte e un poco di zucchero, per favore."),
    ("graham", "Watch that corner chair, wait ten seconds while I tighten this screw.", "Occhio a quella sedia d'angolo, aspetta dieci secondi mentre stringo questa vite."),
    ("hannah", "Done already? You carry a screwdriver everywhere, Graham!", "Già fatto? Porti un cacciavite dappertutto, Graham!"),
    ("graham", "Old houses loosen one screw every Tuesday. Now sit.", "Le case vecchie allentano una vite ogni martedì. Adesso siediti."),
    ("tessa", "Look, you survived the breakfast rush and the mystery phone call!", "Guarda, sei sopravvissuta alla corsa della colazione e alla telefonata misteriosa!"),
    ("hannah", "Honestly, I like it here much better than my old gray office.", "Sinceramente, mi trovo molto meglio qui che nel mio vecchio ufficio grigio."),
    ("tessa", "Wait until Friday at noon, I want a front row seat when the suitcase man walks in!", "Aspetta venerdì a mezzogiorno, voglio un posto in prima fila quando entrerà l'uomo della valigia!"),
    ("graham", "Nobody stares at guests. We hand over the bag and mind our business.", "Nessuno fissa gli ospiti. Consegnamo la valigia e pensiamo ai fatti nostri."),
    ("tessa", "Listen to him! Graham is twice as curious as we are!", "Sentilo! Graham è curioso il doppio di noi!"),
    ("graham", "I am simply checking security. That is my job.", "Controllo semplicemente la sicurezza. È il mio lavoro."),
    ("hannah", "Sure, Graham, your secret is safe with us!", "Certo, Graham, il tuo segreto è al sicuro con noi!"),
]
WALK = [
    (0, None, ["'Siediti, Hannah! Stamattina hai attraversato di corsa mezza città, bevi un caffè.' Nota ancora la posizione della parola metà davanti all'articolo determinativo in", (None, "half the city"), "mezza città, senza preposizione."]),
    (1, None, ["'Volentieri! Con latte e un poco di zucchero, per favore.' Davanti a sostanze non numerabili come lo zucchero, una piccola quantità si esprime con", (None, "a little sugar"), "senza inserire alcuna preposizione nel mezzo."]),
    (2, None, ["'Occhio a quella sedia d'angolo, aspetta dieci secondi mentre stringo questa vite.' Dall'aggettivo stretto deriva con un suffisso il verbo pratico", (None, "tighten"), "stringere o serrare."]),
    (3, None, ["'Già fatto? Porti un cacciavite dappertutto, Graham!' Il nome dell'attrezzo", (None, "screwdriver"), "descrive alla lettera ciò che fa: spinge e gira la vite."]),
    (4, None, ["'Le case vecchie allentano una vite ogni martedì. Adesso siediti.' Ecco subito il verbo opposto a stringere:", (None, "loosen"), "allentare, abbinato alla cadenza regolare di", (None, "every Tuesday"), "ogni martedì."]),
    (5, None, ["'Guarda, sei sopravvissuta alla corsa della colazione e alla telefonata misteriosa!' Mentre in italiano diciamo sopravvivere a qualcosa, il verbo inglese regge l'oggetto diretto senza preposizione in", (None, "survived the breakfast rush"), "il gran daffare della colazione."]),
    (6, None, ["'Sinceramente, mi trovo molto meglio qui che nel mio vecchio ufficio grigio.' Per rafforzare il comparativo di bontà o preferenza si uniscono le tre parole", (None, "much better than"), "molto meglio di."]),
    (7, None, ["'Aspetta venerdì a mezzogiorno, voglio un posto in prima fila quando entrerà l'uomo della valigia!' Anche parlando di venerdì prossimo, nelle frasi temporali introdotte da quando l'inglese rifiuta il futuro e usa il presente in", (None, "when the suitcase man walks in"), "quando entra."]),
    (8, None, ["'Nessuno fissa gli ospiti. Consegnamo la valigia e pensiamo ai fatti nostri.' Guardare qualcuno con insistenza si dice", (None, "stares at"), "mentre l'espressione", (None, "mind our business"), "significa badare ai fatti propri."]),
    (9, None, ["'Sentilo! Graham è curioso il doppio di noi!' I paragoni moltiplicativi si costruiscono incorniciando l'aggettivo in", (None, "twice as curious as"), "due volte più curioso di."]),
    (10, None, ["'Controllo semplicemente la sicurezza. È il mio lavoro.' Quando indichi la tua mansione o il tuo incarico specifico scegli il nome numerabile in", (None, "my job"), "il mio mestiere."]),
    (11, None, ["'Certo, Graham, il tuo segreto è al sicuro con noi!' La frase idiomatica", (None, "your secret is safe with us"), "promette massima discrezione con un sorriso complice."]),
]
CALLOUT_TRANS = {
    "half the city": "mezza città",
    "a little sugar": "un poco di zucchero",
    "tighten": "stringo, stringere",
    "screwdriver": "cacciavite",
    "loosen": "allentano, allentare",
    "every Tuesday": "ogni martedì",
    "survived the breakfast rush": "sei sopravvissuta alla corsa della colazione",
    "much better than": "molto meglio di",
    "when the suitcase man walks in": "quando entrerà l'uomo della valigia",
    "stares at": "fissa con lo sguardo",
    "mind our business": "pensiamo ai fatti nostri",
    "twice as curious as": "curioso il doppio di",
    "my job": "il mio lavoro",
    "your secret is safe with us": "il tuo segreto è al sicuro con noi",
}
