# Authoring module for linden-courtyard-it-s01e01-scene-07.
ID = "linden-courtyard-it-s01e01-scene-07"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 1
SCENE = 7
TITLE = "Tea and a Warm Cardigan  (Tè e un cardigan caldo)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"tessa": "Tessa", "evelyn": "Evelyn", "graham": "Graham"}
INTRO = "Nell'accogliente angolo caffetteria, Tessa porta una teiera fumante e un morbido maglioncino color crema ben piegato per Evelyn, mentre Graham ripone la valigia misteriosa nello sgabuzzino dietro il bancone. Ascolta prima tutta la scena."
OPENER = "Adesso rivediamo ogni frase con attenzione."
TRANSITION = "Ascoltiamo ancora una volta tutta la scena senza pause."
OUTRO = "Un infuso caldo alla menta e un maglioncino in prestito hanno trasformato un brutto spavento in una serata serena. Manca solo l'ultima scena del primo episodio, con una sorpresa davanti al portone. A presto."
CLOSING = ("tessa", "Good night!")
STORY = [
    ("tessa", "Here you are, ma'am: hot mint tea and honey.", "Ecco a lei, signora: tè caldo alla menta e miele."),
    ("evelyn", "Oh, thank you, Tessa. My hands were cold from the shock!", "Oh, grazie, Tessa. Avevo le mani fredde per lo spavento!"),
    ("tessa", "And look, this soft wool cardigan is clean and never worn. Try it on.", "E guardi, questo morbido cardigan di lana è pulito e mai indossato. Lo provi."),
    ("evelyn", "Are you sure? It looks lovely and warm!", "È sicura? Sembra grazioso e caldo!"),
    ("graham", "It fits you very well, ma'am.", "Le sta molto bene, signora."),
    ("evelyn", "You good people are saving my whole trip.", "Voi brave persone mi state salvando l'intero viaggio."),
    ("tessa", "A traveler cannot sit upstairs sad on her first evening in Portland!", "Una viaggiatrice non può restare seduta di sopra triste nella sua prima sera a Portland!"),
    ("graham", "I locked the other blue suitcase safely in our luggage closet.", "Ho chiuso a chiave l'altra valigia blu al sicuro nel nostro ripostiglio dei bagagli."),
    ("evelyn", "Thank you, Graham. That little wooden train inside looked old and precious.", "Grazie, Graham. Quel piccolo treno di legno all'interno sembrava antico e prezioso."),
    ("tessa", "Whoever owns it will surely look for it soon.", "Chiunque ne sia il proprietario la cercherà sicuramente presto."),
    ("evelyn", "I think I will sleep well tonight after all.", "Penso che dopotutto stanotte dormirò bene."),
    ("graham", "Rest well, ma'am. Ring down if you need anything.", "Riposi bene, signora. Suoni pure quaggiù se ha bisogno di qualsiasi cosa."),
]
WALK = [
    (0, None, ["'Ecco a lei, signora: tè caldo alla menta e miele.' Quando porgi una tazza o un piatto a qualcuno, l'espressione", (None, "Here you are"), "rende con naturalezza il nostro ecco a lei."]),
    (1, None, ["'Oh, grazie, Tessa. Avevo le mani fredde per lo spavento!' Dove noi diciamo avevo le mani fredde, l'inglese preferisce il possessivo seguito dal verbo essere al passato in", (None, "My hands were cold"), "le mie mani erano fredde."]),
    (2, None, ["'E guardi, questo morbido cardigan di lana è pulito e mai indossato. Lo provi.' Coi verbi composti separabili il pronome oggetto si incastra esattamente nel mezzo, come in", (None, "Try it on"), "lo provi."]),
    (3, None, ["'È sicura? Sembra grazioso e caldo!' Per descrivere l'aspetto visivo di qualcosa,", (None, "It looks lovely"), "collega direttamente il verbo sembrare all'aggettivo senza preposizioni."]),
    (4, None, ["'Le sta molto bene, signora.' Quando parli della misura e della vestibilità di un indumento, la scelta giusta è", (None, "It fits you"), "ti cade a pennello."]),
    (5, None, ["'Voi brave persone mi state salvando l'intero viaggio.' Rivolgendosi a più persone con affetto e gratitudine, l'inglese può accostare il pronome direttamente al gruppo in", (None, "You good people"), "voi brave persone."]),
    (6, None, ["'Una viaggiatrice non può restare seduta di sopra triste nella sua prima sera a Portland!' Una sola parola compatta,", (None, "upstairs"), "racchiude tutta l'idea di su al piano superiore."]),
    (7, None, ["'Ho chiuso a chiave l'altra valigia blu al sicuro nel nostro ripostiglio dei bagagli.' Il verbo specifico", (None, "I locked"), "contiene già da solo il significato di chiudere a chiave, senza dover aggiungere altro."]),
    (8, None, ["'Grazie, Graham. Quel piccolo treno di legno all'interno sembrava antico e prezioso.' L'aggettivo", (None, "precious"), "indica spesso qualcosa di caro al cuore e ricco di valore affettivo."]),
    (9, None, ["'Chiunque ne sia il proprietario la cercherà sicuramente presto.' Il pronome", (None, "Whoever"), "significa chiunque senza bisogno di congiuntivo, mentre", (None, "look for"), "è il verbo frasale per cercare."]),
    (10, None, ["'Penso che dopotutto stanotte dormirò bene.' Posta in chiusura di frase, la locuzione", (None, "after all"), "corrisponde esattamente al nostro dopotutto o in fin dei conti."]),
    (11, None, ["'Riposi bene, signora. Suoni pure quaggiù se ha bisogno di qualsiasi cosa.' Nelle frasi ipotetiche introdotte da se, l'inglese sceglie il pronome aperto in", (None, "if you need anything"), "per dire qualsiasi cosa."]),
]
CALLOUT_TRANS = {
    "Here you are": "ecco a lei",
    "My hands were cold": "avevo le mani fredde",
    "Try it on": "lo provi",
    "It looks lovely": "sembra grazioso",
    "It fits you": "le sta bene, le va a pennello",
    "You good people": "voi brave persone",
    "upstairs": "di sopra, al piano superiore",
    "I locked": "ho chiuso a chiave",
    "precious": "prezioso, caro",
    "Whoever": "chiunque",
    "look for": "cercare",
    "after all": "dopotutto",
    "if you need anything": "se ha bisogno di qualsiasi cosa",
}
