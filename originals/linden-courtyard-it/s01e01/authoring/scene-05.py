# Authoring module for linden-courtyard-it-s01e01-scene-05.
ID = "linden-courtyard-it-s01e01-scene-05"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = "Not My Clothes!  (Non sono i miei vestiti!)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"evelyn": "Evelyn", "hannah": "Hannah", "graham": "Graham"}
INTRO = "Due minuti dopo essere saliti, il cicalino della camera quattro suona al bancone: non due volte, ma quattro di seguito. Hannah corre al piano di sopra e trova Evelyn e Graham davanti alla valigia aperta. Ascolta prima tutta la scena."
OPENER = "Vediamo con calma che cosa è appena successo, frase per frase."
TRANSITION = "Torniamo ad ascoltare l'intera scena a ritmo naturale."
OUTRO = "Al posto di abiti e spartiti, la valigia blu nasconde grandi scarpe marroni da uomo e un trenino di legno. Nella prossima scena scopriremo che cosa c'è scritto su quel cartellino."
CLOSING = ("hannah", "Goodbye!")
STORY = [
    ("hannah", "Miss Evelyn, is everything all right? You rang the bell!", "Signorina Evelyn, va tutto bene? Ha suonato il campanello!"),
    ("evelyn", "Look inside this suitcase, Hannah! This is not my bag!", "Guarda dentro questa valigia, Hannah! Questa non è la mia valigia!"),
    ("hannah", "Wait, it is dark blue, just like yours!", "Aspetti, è blu scuro, proprio come la sua!"),
    ("evelyn", "The outside is identical, yes! But look inside!", "L'esterno è identico, sì! Ma guarda dentro!"),
    ("graham", "Two pairs of big brown men's shoes and gray sweaters.", "Due paia di grandi scarpe marroni da uomo e maglioni grigi."),
    ("hannah", "And what is this wrapped in white paper? A little wooden train!", "E che cos'è questo avvolto nella carta bianca? Un piccolo treno di legno!"),
    ("evelyn", "I certainly do not wear size eleven shoes!", "Di sicuro io non porto scarpe taglia undici!"),
    ("graham", "No wonder it was so heavy. Wood and leather!", "Non c'è da stupirsi che fosse così pesante. Legno e cuoio!"),
    ("evelyn", "Someone at the train station took my blue suitcase by mistake!", "Qualcuno alla stazione ferroviaria ha preso la mia valigia blu per sbaglio!"),
    ("hannah", "Please sit down, ma'am. Do not worry, we will check the tag right now.", "La prego, si sieda, signora. Non si preoccupi, controlliamo subito l'etichetta."),
    ("graham", "There is a small paper card tied to the side handle.", "C'è un piccolo cartoncino legato alla maniglia laterale."),
    ("evelyn", "Oh, let us bring it downstairs to the light!", "Oh, portiamola giù alla luce!"),
]
WALK = [
    (0, None, ["'Signorina Evelyn, va tutto bene? Ha suonato il campanello!' Usare il titolo davanti al nome di battesimo in", (None, "Miss Evelyn"), "suona affettuoso e deferente, mentre", (None, "rang"), "è il passato irregolare del verbo suonare."]),
    (1, None, ["'Guarda dentro questa valigia, Hannah! Questa non è la mia valigia!' Negare col verbo essere richiede soltanto di mettere la negazione subito dopo il verbo in", (None, "This is not"), "senza alcun articolo davanti al possessivo."]),
    (2, None, ["'Aspetti, è blu scuro, proprio come la sua!' Il pronome possessivo autonomo", (None, "yours"), "vale la tua o la sua senza bisogno di ripetere la parola valigia né di usare l'articolo."]),
    (3, None, ["'L'esterno è identico, sì! Ma guarda dentro!' Cogli il netto contrasto spaziale fra", (None, "The outside"), "che indica la parte esterna e", (None, "inside"), "per guardare all'interno."]),
    (4, None, ["'Due paia di grandi scarpe marroni da uomo e maglioni grigi.' Perfino un plurale irregolare che cambia vocale interna prende apostrofo ed esse in", (None, "men's shoes"), "per dire scarpe da uomo."]),
    (5, None, ["'E che cos'è questo avvolto nella carta bianca? Un piccolo treno di legno!' Dal nome del legno nasce l'aggettivo di materiale che precede il sostantivo in", (None, "wooden train"), "trenino di legno."]),
    (6, None, ["'Di sicuro io non porto scarpe taglia undici!' Per abiti, scarpe, cappelli o occhiali che si indossano, il verbo inglese da scegliere è sempre", (None, "wear"), "portare addosso."]),
    (7, None, ["'Non c'è da stupirsi che fosse così pesante. Legno e cuoio!' Due sole parole in apertura,", (None, "No wonder"), "rendono con naturalezza il nostro ci credo bene o non c'è da meravigliarsi."]),
    (8, None, ["'Qualcuno alla stazione ferroviaria ha preso la mia valigia blu per sbaglio!' Alla fine della frase il blocco fisso", (None, "by mistake"), "corrisponde esattamente all'italiano per errore o per sbaglio."]),
    (9, None, ["'La prego, si sieda, signora. Non si preoccupi, controlliamo subito l'etichetta.' Rassicurare qualcuno sul momento è facilissimo con", (None, "Do not worry"), "valido sia dando del tu sia dando del lei."]),
    (10, None, ["'C'è un piccolo cartoncino legato alla maniglia laterale.' Per dire c'è davanti a un solo elemento si parte con", (None, "There is"), "mentre al plurale il verbo cambierebbe numero."]),
    (11, None, ["'Oh, portiamola giù alla luce!' Le proposte che includono chi parla e chi ascolta si aprono con", (None, "let us bring it downstairs"), "dove l'ultima parola contiene già l'idea di scendere al piano inferiore."]),
]
CALLOUT_TRANS = {
    "Miss Evelyn": "signorina Evelyn",
    "rang": "ha suonato",
    "This is not": "questa non è",
    "yours": "la sua, la tua",
    "The outside": "l'esterno",
    "inside": "dentro",
    "men's shoes": "scarpe da uomo",
    "wooden train": "treno di legno",
    "wear": "indossare, portare",
    "No wonder": "non c'è da stupirsi",
    "by mistake": "per sbaglio",
    "Do not worry": "non si preoccupi, non preoccuparti",
    "There is": "c'è",
    "let us bring it downstairs": "portiamola giù",
}
