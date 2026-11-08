# Authoring module for linden-courtyard-it-s01e03-scene-01.
ID = "linden-courtyard-it-s01e03-scene-01"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = "Thirty-Five Minutes  (Trentacinque minuti)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"arthur": "Arthur", "hannah": "Hannah", "graham": "Graham"}
INTRO = "La pioggia batte sui vetri dell'ingresso alla Locanda del Cortile del Tiglio, a Portland. Con un secondo ospite per la camera sette in arrivo tra trentacinque minuti, Arthur, Hannah e Graham si precipitano verso le scale. Ascolta prima tutta la scena in inglese."
OPENER = "Ora ripercorriamo il dialogo con calma, frase per frase."
TRANSITION = "Ascoltiamo di nuovo tutta la scena a velocità naturale."
OUTRO = "Restano trentacinque minuti sull'orologio e quattro scatoloni da spostare. Non preoccuparti se qualche espressione è passata svelta; la risentirai su al terzo piano. Alla prossima."
CLOSING = ("hannah", "See you soon!")
STORY = [
    ("arthur", "Thirty-five minutes! He will write a terrible one star review!", "Trentacinque minuti! Scriverà una terribile recensione da una stella!"),
    ("hannah", "Take a deep breath, Arthur. Nobody has written anything yet.", "Fai un bel respiro profondo, Arthur. Nessuno ha ancora scritto niente."),
    ("graham", "Here is the small silver key for the third floor attic door.", "Ecco la piccola chiave d'argento per la porta della soffitta al terzo piano."),
    ("arthur", "Does the attic even have a proper bed?", "Ma la soffitta ha almeno un letto vero e proprio?"),
    ("graham", "Yes, a good wooden bed, a clean desk, and the best view in the house.", "Sì, un buon letto di legno, una scrivania pulita e la vista migliore della casa."),
    ("hannah", "Then why do we never rent it to guests?", "Allora perché non la affittiamo mai agli ospiti?"),
    ("graham", "Because the stairs are narrow and Arthur keeps old lamp boxes there.", "Perché le scale sono strette e Arthur ci tiene vecchie scatole di lampade."),
    ("arthur", "Only three small boxes! Maybe four!", "Solo tre scatole piccole! Forse quattro!"),
    ("hannah", "We can move four boxes in five minutes. Let us go look right now!", "Possiamo spostare quattro scatole in cinque minuti. Andiamo a vedere subito!"),
    ("graham", "Up the stairs, turn left at the landing, last door at the top.", "Su per le scale, gira a sinistra sul pianerottolo, l'ultima porta in cima."),
    ("arthur", "I will bring clean white sheets from the linen closet!", "Io porterò lenzuola bianche pulite dall'armadio della biancheria!"),
    ("hannah", "Come on, race you to the third floor!", "Dai, facciamo a gara fino al terzo piano!"),
]
WALK = [
    (0, None, ["'Trentacinque minuti! Scriverà una terribile recensione da una stella!' Per esprimere una previsione futura carica di timore basta anteporre l'ausiliare al verbo base in", (None, "will write"), "scriverà."]),
    (1, None, ["'Fai un bel respiro profondo, Arthur. Nessuno ha ancora scritto niente.' Tieni a mente il blocco fisso", (None, "Take a deep breath"), "che letteralmente invita a prendere un respiro profondo."]),
    (2, None, ["'Ecco la piccola chiave d'argento per la porta della soffitta al terzo piano.' Guarda come tre elementi descrittivi si dispongono in fila davanti al nome finale in", (None, "third floor attic door"), "senza alcuna preposizione."]),
    (3, None, ["'Ma la soffitta ha almeno un letto vero e proprio?' Inserito prima del verbo,", (None, "even"), "aggiunge quella sfumatura di dubbio scettico che in italiano rendiamo con almeno o perfino."]),
    (4, None, ["'Sì, un buon letto di legno, una scrivania pulita e la vista migliore della casa.' Dopo un superlativo riferito a un edificio o a un luogo chiuso l'inglese preferisce la preposizione interna in", (None, "best view in the house"), "anziché l'equivalente di."]),
    (5, None, ["'Allora perché non la affittiamo mai agli ospiti?' Nelle domande con l'avverbio mai l'inglese evita il non e colloca", (None, "why do we never rent"), "subito prima del verbo principale."]),
    (6, None, ["'Perché le scale sono strette e Arthur ci tiene vecchie scatole di lampade.' Proprio come il nostro le scale, anche", (None, "the stairs are narrow"), "si costruisce sempre al plurale."]),
    (7, None, ["'Solo tre scatole piccole! Forse quattro!' Una parolina sola e comodissima,", (None, "Maybe"), "permette di correggere una stima al volo proprio come forse."]),
    (8, None, ["'Possiamo spostare quattro scatole in cinque minuti. Andiamo a vedere subito!' Nella lingua parlata americana due verbi brevi come andare e guardare si legano senza congiunzione in", (None, "go look"), "andare a vedere."]),
    (9, None, ["'Su per le scale, gira a sinistra sul pianerottolo, l'ultima porta in cima.' Per dare indicazioni chiare dentro un edificio si usa", (None, "turn left at the landing"), "indicando la svolta sul pianerottolo."]),
    (10, None, ["'Io porterò lenzuola bianche pulite dall'armadio della biancheria!' Quando ti offri sul momento di occuparti di qualcosa scegli il futuro immediato con", (None, "I will bring"), "porterò io."]),
    (11, None, ["'Dai, facciamo a gara fino al terzo piano!' L'espressione vivace", (None, "race you"), "sottintende il soggetto e lancia una sfida scherzosa a chi arriva prima."]),
]
CALLOUT_TRANS = {
    "will write": "scriverà",
    "Take a deep breath": "fai un respiro profondo",
    "third floor attic door": "porta della soffitta al terzo piano",
    "even": "almeno, persino",
    "best view in the house": "la vista migliore della casa",
    "why do we never rent": "perché non affittiamo mai",
    "the stairs are narrow": "le scale sono strette",
    "Maybe": "forse",
    "go look": "andare a vedere",
    "turn left at the landing": "gira a sinistra sul pianerottolo",
    "I will bring": "porterò",
    "race you": "facciamo a gara",
}
