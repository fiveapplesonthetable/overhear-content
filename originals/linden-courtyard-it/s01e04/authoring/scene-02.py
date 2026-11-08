# Authoring module for linden-courtyard-it-s01e04-scene-02.
ID = "linden-courtyard-it-s01e04-scene-02"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = "The Blue Door  (La porta blu)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"hannah": "Hannah", "graham": "Graham"}
INTRO = "Dieci minuti dopo, Hannah ha già attraversato il ponte sul fiume a Portland, ma dietro la farmacia si aprono due stradine diverse. Chiama Graham da vicino a una fontanella di pietra. Ascoltiamo prima la telefonata."
OPENER = "Ripercorriamo battuta per battuta la chiamata di Hannah dalla piazzetta."
TRANSITION = "Riascoltiamo adesso l'intera scena senza interruzioni."
OUTRO = "Due valvole nuove in tasca e i primi passi già udibili sulle scale del secondo piano. Nella prossima scena Tessa e Arthur provano a trattenere tutti a colazione. A tra poco."
CLOSING = ("graham", "Bye for now!")
STORY = [
    ("hannah", "Graham, can you hear me? I just passed the green pharmacy!", "Graham, mi senti? Ho appena superato la farmacia verde!"),
    ("graham", "Loud and clear. Are you standing by the little stone fountain?", "Forte e chiaro. Sei ferma vicino alla piccola fontana di pietra?"),
    ("hannah", "Yes! There are two small streets on the left. Which one do I take?", "Sì! Ci sono due stradine sulla sinistra. Quale prendo?"),
    ("graham", "Take the second street, beside the flower stand, not the narrow alley.", "Prendi la seconda strada, accanto al chiosco dei fiori, non il vicolo stretto."),
    ("hannah", "Walking now... oh, I see the golden key sign and the blue door!", "Sto camminando ora... oh, vedo l'insegna della chiave dorata e la porta blu!"),
    ("graham", "Good! Is the shutter open?", "Bene! La serranda è aperta?"),
    ("hannah", "He is unlocking it right now! Stay on the phone one second.", "La sta aprendo con la chiave proprio adesso! Resta al telefono un secondo."),
    ("graham", "Make sure the brass ring inside is twenty millimeters wide.", "Assicurati che l'anello d'ottone all'interno sia largo venti millimetri."),
    ("hannah", "He matched it against the old one. He has two left on the shelf!", "L'ha confrontata con quella vecchia. Gliene restano due sullo scaffale!"),
    ("graham", "Buy both! A spare valve saves next winter too.", "Comprale tutt'e due! Una valvola di scorta salva anche il prossimo inverno."),
    ("hannah", "Paid in cash! Keep your toolbox open, I am running back across the bridge!", "Pagato in contanti! Tieni aperta la cassetta degli attrezzi, sto tornando di corsa sul ponte!"),
    ("graham", "Hurry, I just heard footsteps on the second floor stairs!", "Fai presto, ho appena sentito dei passi sulle scale del secondo piano!"),
]
WALK = [
    (0, None, ["'Graham, mi senti? Ho appena superato la farmacia verde!' Al telefono l'inglese appoggia i verbi di percezione a potere in", (None, "can you hear me"), "mentre", (None, "just passed"), "indica un'azione appena compiuta."]),
    (1, None, ["'Forte e chiaro. Sei ferma vicino alla piccola fontana di pietra?' La risposta classica quando la linea telefonica è perfetta è", (None, "Loud and clear"), "forte e chiaro, e", (None, "by"), "vale accanto a."]),
    (2, None, ["'Sì! Ci sono due stradine sulla sinistra. Quale prendo?' Davanti a una scelta fra due opzioni precise si usa", (None, "Which one"), "dove il pronome evita di ripetere la parola strada."]),
    (3, None, ["'Prendi la seconda strada, accanto al chiosco dei fiori, non il vicolo stretto.' La preposizione", (None, "beside"), "significa proprio a fianco di, e", (None, "flower stand"), "è la bancarella dei fiori."]),
    (4, None, ["'Sto camminando ora... oh, vedo l'insegna della chiave dorata e la porta blu!' Tre sostantivi in fila formano", (None, "golden key sign"), "dove chiave dorata specifica il tipo di insegna."]),
    (5, None, ["'Bene! La serranda è aperta?' La serranda avvolgibile di una bottega si chiama", (None, "shutter"), "e la domanda inverte il verbo essere in", (None, "Is the shutter open?"), "è aperta la serranda."]),
    (6, None, ["'La sta aprendo con la chiave proprio adesso! Resta al telefono un secondo.' Togliere la chiusura a chiave si dice con un verbo preciso,", (None, "is unlocking"), "mentre per non far riagganciare usi", (None, "Stay on the phone"), "resta in linea."]),
    (7, None, ["'Assicurati che l'anello d'ottone all'interno sia largo venti millimetri.' Per raccomandare un controllo attento si apre con", (None, "Make sure"), "e la misura si chiude con l'aggettivo in", (None, "twenty millimeters wide"), "largo venti millimetri."]),
    (8, None, ["'L'ha confrontata con quella vecchia. Gliene restano due sullo scaffale!' Nota come la quantità residua si costruisca mettendo il participio dopo il numero in", (None, "two left"), "due rimaste."]),
    (9, None, ["'Comprale tutt'e due! Una valvola di scorta salva anche il prossimo inverno.' Per dire entrambi senza articolo basta", (None, "Buy both"), "e un pezzo di ricambio si definisce", (None, "spare valve"), "valvola di scorta."]),
    (10, None, ["'Pagato in contanti! Tieni aperta la cassetta degli attrezzi, sto tornando di corsa sul ponte!' Pagare con banconote e monete si dice", (None, "Paid in cash"), "con la preposizione", (None, "in"), "davanti al contante."]),
    (11, None, ["'Fai presto, ho appena sentito dei passi sulle scale del secondo piano!' L'esortazione rapida per mettere fretta è il semplice verbo", (None, "Hurry"), "sbrigati, e i rumori di passi si chiamano", (None, "footsteps"), "passi."]),
]
CALLOUT_TRANS = {
    "can you hear me": "mi senti",
    "just passed": "ho appena superato",
    "Loud and clear": "forte e chiaro",
    "by": "vicino a, accanto a",
    "Which one": "quale",
    "beside": "accanto a",
    "flower stand": "chiosco dei fiori",
    "golden key sign": "insegna della chiave dorata",
    "shutter": "serranda",
    "Is the shutter open?": "la serranda è aperta?",
    "is unlocking": "sta aprendo con la chiave",
    "Stay on the phone": "resta al telefono",
    "Make sure": "assicurati",
    "twenty millimeters wide": "largo venti millimetri",
    "two left": "due rimaste",
    "Buy both": "comprale entrambe",
    "spare valve": "valvola di scorta",
    "Paid in cash": "pagato in contanti",
    "in": "in",
    "Hurry": "fai presto, sbrigati",
    "footsteps": "passi",
}
