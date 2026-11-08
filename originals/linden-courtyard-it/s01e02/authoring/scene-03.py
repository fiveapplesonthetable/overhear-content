# Authoring module for linden-courtyard-it-s01e02-scene-03.
ID = "linden-courtyard-it-s01e02-scene-03"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = "Counting the Change  (Contando il resto)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"hannah": "Hannah", "arthur": "Arthur", "tessa": "Tessa"}
INTRO = "Nove minuti più tardi, Hannah rientra di volata dal cancello del cortile reggendo due borse di tela piene zeppe di spesa per Tessa e Arthur. Ascolta prima tutta la scena."
OPENER = "Adesso osserviamo da vicino ogni frase."
TRANSITION = "Torniamo ad ascoltare la scena intera tutta d'un fiato."
OUTRO = "Un panetto sbagliato di burro salato ha rischiato di rovinare i panini alla marmellata, finché Tessa non lo ha trasformato nell'ingrediente segreto delle uova strapazzate. A presto."
CLOSING = ("tessa", "Bye for now!")
STORY = [
    ("hannah", "Nine minutes! Here are the milk, the eggs, and the apples!", "Nove minuti! Ecco il latte, le uova e le mele!"),
    ("tessa", "You are a hero, Hannah! Give me the milk first for the coffee machine.", "Sei un mito, Hannah! Dammi prima il latte per la macchina del caffè."),
    ("arthur", "Impressive speed! Did the shopkeeper give you a receipt?", "Velocità impressionante! Il negoziante ti ha dato lo scontrino?"),
    ("hannah", "Right here! Everything cost thirty-eight, so here is twelve in change.", "Eccolo qui! Tutto è costato trentotto, quindi ecco dodici di resto."),
    ("arthur", "Ten, eleven, twelve. Exact to the last coin, thank you!", "Dieci, undici, dodici. Esatto fino all'ultima moneta, grazie!"),
    ("tessa", "Wait a second, Hannah... which pack of butter did you grab?", "Aspetta un secondo, Hannah... quale panetto di burro hai preso al volo?"),
    ("hannah", "The gold wrapper on the top shelf. Why?", "Quello con l'incarto dorato sullo scaffale in alto. Perché?"),
    ("tessa", "That is extra salty sea butter! My sweet jam rolls need plain butter!", "Quello è burro marino molto salato! Ai miei panini dolci con la marmellata serve burro non salato!"),
    ("hannah", "Oh no! All the wrappers looked the same when I was running!", "Oh no! Tutti gli incarti sembravano uguali mentre correvo!"),
    ("arthur", "Can we serve salty butter with sweet strawberry jam?", "Possiamo servire burro salato con la marmellata dolce di fragole?"),
    ("tessa", "Wait, salty butter is terrible for jam, but amazing for scrambled eggs!", "Aspettate, il burro salato è terribile per la marmellata, ma straordinario per le uova strapazzate!"),
    ("hannah", "Phew! Quick thinking saves breakfast again.", "Meno male! La prontezza di spirito salva di nuovo la colazione."),
]
WALK = [
    (0, None, ["'Nove minuti! Ecco il latte, le uova e le mele!' Mentre il nostro ecco è invariabile, presentando più cose insieme l'inglese usa il plurale", (None, "Here are"), "ecco qui."]),
    (1, None, ["'Sei un mito, Hannah! Dammi prima il latte per la macchina del caffè.' Nel parlato entusiasta di tutti i giorni,", (None, "a hero"), "si rivolge tranquillamente sia a un uomo sia a una donna."]),
    (2, None, ["'Velocità impressionante! Il negoziante ti ha dato lo scontrino?' Guarda l'ordine del doppio complemento in", (None, "give you a receipt"), "dove il destinatario precede l'oggetto senza alcuna preposizione."]),
    (3, None, ["'Eccolo qui! Tutto è costato trentotto, quindi ecco dodici di resto.' Il verbo irregolare", (None, "cost"), "mantiene la stessa identica forma al presente e al passato, mentre", (None, "in change"), "significa di resto."]),
    (4, None, ["'Dieci, undici, dodici. Esatto fino all'ultima moneta, grazie!' L'espressione", (None, "to the last coin"), "sottolinea che i conti tornano al centesimo."]),
    (5, None, ["'Aspetta un secondo, Hannah... quale panetto di burro hai preso al volo?' Quando si sceglie fra poche varietà ben precise sullo scaffale, l'interrogativo giusto è", (None, "which pack"), "quale confezione."]),
    (6, None, ["'Quello con l'incarto dorato sullo scaffale in alto. Perché?' Per ripiani e mensole si usa la preposizione di superficie in", (None, "on the top shelf"), "sullo scaffale più alto."]),
    (7, None, ["'Quello è burro marino molto salato! Ai miei panini dolci con la marmellata serve burro non salato!' In cucina l'aggettivo semplice o naturale senza aggiunte si rende con", (None, "plain butter"), "burro classico non salato."]),
    (8, None, ["'Oh no! Tutti gli incarti sembravano uguali mentre correvo!' Per dire sembravano uguali l'inglese inserisce sempre l'articolo determinativo in", (None, "looked the same"), "mai senza articolo."]),
    (9, None, ["'Possiamo servire burro salato con la marmellata dolce di fragole?' Coi verbi modali come potere basta invertire verbo e soggetto in", (None, "Can we serve"), "senza altri ausiliari."]),
    (10, None, ["'Aspettate, il burro salato è terribile per la marmellata, ma straordinario per le uova strapazzate!' Il piatto forte del mattino,", (None, "scrambled eggs"), "prende nome dal verbo mescolare rapidamente in padella."]),
    (11, None, ["'Meno male! La prontezza di spirito salva di nuovo la colazione.' Il sospiro di sollievo si scrive", (None, "Phew"), "e l'abbinamento", (None, "Quick thinking"), "indica il pensare svelto nelle emergenze."]),
]
CALLOUT_TRANS = {
    "Here are": "ecco (al plurale)",
    "a hero": "un eroe, un mito",
    "give you a receipt": "darti uno scontrino",
    "cost": "è costato",
    "in change": "di resto",
    "to the last coin": "fino all'ultima moneta",
    "which pack": "quale confezione",
    "on the top shelf": "sullo scaffale in alto",
    "plain butter": "burro semplice non salato",
    "looked the same": "sembravano uguali",
    "Can we serve": "possiamo servire",
    "scrambled eggs": "uova strapazzate",
    "Phew": "meno male, fiuu",
    "Quick thinking": "prontezza di spirito",
}
