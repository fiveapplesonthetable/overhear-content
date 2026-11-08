# Authoring module for linden-courtyard-it-s01e05-scene-02.
ID = "linden-courtyard-it-s01e05-scene-02"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 5
SCENE = 2
TITLE = "Three Years of Silence  (Tre anni di silenzio)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"caleb": "Caleb", "hannah": "Hannah", "graham": "Graham"}
INTRO = "Dentro, al bancone dell'ingresso, Graham tira fuori dal ripostiglio la valigia blu scuro per Caleb e Hannah. È ormai venerdì mattina, tre ore prima di mezzogiorno. Ascoltiamo prima il dialogo."
OPENER = "Ripercorriamo ora ogni battuta con tranquillità."
TRANSITION = "Riascoltiamo adesso l'intera scena di seguito."
OUTRO = "Invece di nascondersi dall'altro lato della strada, Caleb ha tre ore per farsi coraggio e restare proprio qui nel cortile. Ci vediamo nella prossima scena."
CLOSING = ("graham", "See you later!")
STORY = [
    ("graham", "So our mystery Friday caller was sleeping upstairs under my attic roof all along.", "Quindi il nostro misterioso interlocutore del venerdì dormiva di sopra sotto il tetto della mia mansarda fin dall'inizio."),
    ("caleb", "Sorry for the trouble, Graham. Thank you for guarding this bag all week.", "Scusa per il disturbo, Graham. Grazie per aver custodito questa borsa tutta la settimana."),
    ("hannah", "Why could you not simply hand Owen the wooden train at his front door?", "Perché non potevi semplicemente consegnare a Owen il treno di legno davanti alla porta di casa sua?"),
    ("caleb", "Three years ago, after our grandfather died, Owen and I argued bitterly over selling the old house.", "Tre anni fa, dopo la morte di nostro nonno, Owen e io abbiamo litigato aspramente per la vendita della vecchia casa."),
    ("graham", "Family houses and old memories, those arguments cut deep.", "Case di famiglia e vecchi ricordi: quelle discussioni lasciano ferite profonde."),
    ("caleb", "We have not spoken since that day. Last week I sent him one short postcard.", "Non ci parliamo da quel giorno. La settimana scorsa gli ho spedito una breve cartolina."),
    ("hannah", "Asking him to meet you here on Friday at noon?", "Chiedendogli di incontrarti qui venerdì a mezzogiorno?"),
    ("caleb", "Actually, I only wrote: 'Something from Grandfather is waiting at the Linden Courtyard Inn Friday at noon.'", "In realtà ho scritto solo: «Qualcosa del nonno ti aspetta alla Locanda del Cortile del Tiglio venerdì a mezzogiorno.»"),
    ("graham", "Aha! You feared that if you signed your name, stubborn big brother would stay home!", "Ecco! Temevi che, firmando col tuo nome, il fratello maggiore testardo sarebbe rimasto a casa!"),
    ("caleb", "You know older brothers well, Graham.", "Conosci bene i fratelli maggiori, Graham."),
    ("hannah", "Wait, were you planning to hand the clerk the bag and watch from across the street?!", "Aspetta, avevi intenzione di far dare la borsa all'addetto e guardare dall'altro lato della strada?!"),
    ("caleb", "That was my cowardly Monday plan... before I met all of you.", "Quello era il mio piano codardo del lunedì... prima di conoscere tutti voi."),
]
WALK = [
    (0, None, ["'Quindi il nostro misterioso interlocutore del venerdì dormiva di sopra sotto il tetto della mia mansarda fin dall'inizio.' Posta in fondo alla frase, la locuzione", (None, "all along"), "rivela che qualcosa era vero fin dal primo momento."]),
    (1, None, ["'Scusa per il disturbo, Graham. Grazie per aver custodito questa borsa tutta la settimana.' Quando ringrazi per un'azione già compiuta, dopo la preposizione basta la forma progressiva in", (None, "for guarding"), "per aver custodito."]),
    (2, None, ["'Perché non potevi semplicemente consegnare a Owen il treno di legno davanti alla porta di casa sua?' Il sostantivo per mano diventa un verbo comodissimo in", (None, "hand Owen"), "porgere direttamente a Owen senza preposizioni."]),
    (3, None, ["'Tre anni fa, dopo la morte di nostro nonno, Owen e io abbiamo litigato aspramente per la vendita della vecchia casa.' Per introdurre il motivo di una lite si abbina il verbo alla preposizione sopra in", (None, "argued bitterly over"), "abbiamo discusso amaramente riguardo a."]),
    (4, None, ["'Case di famiglia e vecchi ricordi: quelle discussioni lasciano ferite profonde.' Due parole incisive,", (None, "cut deep"), "dipingono l'idea di ferire nel profondo senza bisogno di avverbi lunghi."]),
    (5, None, ["'Non ci parliamo da quel giorno. La settimana scorsa gli ho spedito una breve cartolina.' Per un silenzio iniziato nel passato e ancora aperto, l'inglese sceglie il passato composto", (None, "have not spoken"), "legato al punto d'origine", (None, "since that day"), "da quella domenica."]),
    (6, None, ["'Chiedendogli di incontrarti qui venerdì a mezzogiorno?' Guarda il cambio di preposizione nella stessa espressione:", (None, "on Friday at noon"), "usa una preposizione per il giorno e un'altra per l'ora esatta."]),
    (7, None, ["'In realtà ho scritto solo: «Qualcosa del nonno ti aspetta alla Locanda del Cortile del Tiglio venerdì a mezzogiorno.»' L'avverbio", (None, "Actually"), "corregge con garbo e vuol dire in realtà, non attualmente, seguito da", (None, "is waiting"), "sta aspettando."]),
    (8, None, ["'Ecco! Temevi che, firmando col tuo nome, il fratello maggiore testardo sarebbe rimasto a casa!' Raccontando al passato un'ipotesi futura, compare il condizionale semplice in", (None, "would stay home"), "sarebbe rimasto a casa."]),
    (9, None, ["'Conosci bene i fratelli maggiori, Graham.' Senza articolo determinativo, il plurale generale", (None, "older brothers"), "abbraccia tutta la categoria dei fratelli più grandi."]),
    (10, None, ["'Aspetta, avevi intenzione di far dare la borsa all'addetto e guardare dall'altro lato della strada?!' La preposizione di attraversamento in", (None, "across the street"), "indica il marciapiede opposto della via."]),
    (11, None, ["'Quello era il mio piano codardo del lunedì... prima di conoscere tutti voi.' Per abbracciare l'intero gruppo con calore si unisce la totalità al pronome plurale in", (None, "all of you"), "tutti voi."]),
]
CALLOUT_TRANS = {
    "all along": "fin dall'inizio, per tutto il tempo",
    "for guarding": "per aver custodito",
    "hand Owen": "consegnare a Owen",
    "argued bitterly over": "abbiamo litigato aspramente per",
    "cut deep": "feriscono nel profondo",
    "have not spoken": "non ci siamo parlati, non ci parliamo",
    "since that day": "da quella domenica",
    "on Friday at noon": "venerdì a mezzogiorno",
    "Actually": "in realtà",
    "is waiting": "sta aspettando, ti aspetta",
    "would stay home": "sarebbe rimasto a casa",
    "older brothers": "i fratelli maggiori",
    "across the street": "dall'altro lato della strada",
    "all of you": "tutti voi",
}
