# Authoring module for linden-courtyard-it-s01e02-scene-02.
ID = "linden-courtyard-it-s01e02-scene-02"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 2
SCENE = 2
TITLE = "No Milk in the Fridge  (Niente latte in frigo)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"tessa": "Tessa", "hannah": "Hannah", "arthur": "Arthur"}
INTRO = "In cucina, Tessa apre il frigorifero e trattiene il fiato proprio mentre entrano Hannah e il proprietario Arthur. Otto ospiti si stanno svegliando di sopra e la colazione comincia tra venti minuti. Ascolta prima tutta la scena."
OPENER = "Analizziamo adesso la scena frase dopo frase."
TRANSITION = "Riascoltiamo tutta la scena a velocità naturale."
OUTRO = "Con la lista della spesa in mente e il contante della cassa, Hannah scatta verso il negozio all'angolo. Nella prossima scena vedremo con che cosa tornerà."
CLOSING = ("hannah", "See you later!")
STORY = [
    ("tessa", "Oh no! Arthur, Hannah, we have a kitchen emergency!", "Oh no! Arthur, Hannah, abbiamo un'emergenza in cucina!"),
    ("arthur", "Please do not say the word emergency before my morning coffee!", "Per favore non pronunciare la parola emergenza prima del mio caffè del mattino!"),
    ("tessa", "The dairy van has a flat tire outside town. Look in the fridge!", "Il furgone dei latticini ha una gomma a terra fuori città. Guardate in frigo!"),
    ("hannah", "One tiny splash of milk, two eggs, and no butter at all!", "Un goccio minuscolo di latte, due uova e niente burro del tutto!"),
    ("arthur", "Eight hungry guests will come down the stairs at seven thirty!", "Otto ospiti affamati scenderanno le scale alle sette e trenta!"),
    ("tessa", "My bread is already in the oven, at least.", "Il mio pane è già nel forno, se non altro."),
    ("hannah", "Give me a bag and some cash! The corner market opens at seven.", "Datemi una borsa e dei contanti! Il mercato all'angolo apre alle sette."),
    ("arthur", "Can you run there and back in ten minutes?", "Riesci a correre fin là e tornare indietro in dieci minuti?"),
    ("hannah", "Watch me! Tell me exactly what to buy.", "Stammi a guardare! Ditemi esattamente che cosa comprare."),
    ("tessa", "Three bottles of milk, twenty eggs, butter, cheese, and red apples!", "Tre bottiglie di latte, venti uova, burro, formaggio e mele rosse!"),
    ("arthur", "Here is fifty from the cash box. Bring back the receipt!", "Ecco cinquanta dalla cassa. Riporta indietro lo scontrino!"),
    ("hannah", "Hold the fort, I am already out the door!", "Tenete duro qui, io sono già fuori dalla porta!"),
]
WALK = [
    (0, None, ["'Oh no! Arthur, Hannah, abbiamo un'emergenza in cucina!' Mettendo il luogo direttamente davanti al nome principale in", (None, "kitchen emergency"), "si ottiene subito emergenza in cucina senza preposizione."]),
    (1, None, ["'Per favore non pronunciare la parola emergenza prima del mio caffè del mattino!' Una preghiera cortese al negativo si apre in modo limpido con", (None, "Please do not say"), "seguita dal verbo invariato."]),
    (2, None, ["'Il furgone dei latticini ha una gomma a terra fuori città. Guardate in frigo!' Nell'inglese americano uno pneumatico bucato o sgonfio si chiama", (None, "a flat tire"), "letteralmente una gomma piatta."]),
    (3, None, ["'Un goccio minuscolo di latte, due uova e niente burro del tutto!' Aggiungere", (None, "at all"), "subito dopo", (None, "no butter"), "rende la negazione assoluta: neanche un grammo di burro."]),
    (4, None, ["'Otto ospiti affamati scenderanno le scale alle sette e trenta!' Ricorda che l'inglese non usa avere fame ma l'aggettivo affamato, come senti in", (None, "hungry guests"), "ospiti affamati."]),
    (5, None, ["'Il mio pane è già nel forno, se non altro.' Messa in fondo alla frase, la locuzione", (None, "at least"), "attenua il problema proprio come il nostro almeno o se non altro."]),
    (6, None, ["'Datemi una borsa e dei contanti! Il mercato all'angolo apre alle sette.' Il denaro contante si indica con il nome non numerabile in", (None, "some cash"), "che non prende mai il plurale."]),
    (7, None, ["'Riesci a correre fin là e tornare indietro in dieci minuti?' Tre sole parole brevi,", (None, "there and back"), "sintetizzano con grande efficacia andata e ritorno."]),
    (8, None, ["'Stammi a guardare! Ditemi esattamente che cosa comprare.' Quando accetti una sfida con entusiasmo dici", (None, "Watch me"), "mentre", (None, "what to buy"), "unisce pronome interrogativo e infinito come che cosa comprare."]),
    (9, None, ["'Tre bottiglie di latte, venti uova, burro, formaggio e mele rosse!' Essendo il latte non numerabile, se ne contano i contenitori in", (None, "Three bottles of milk"), "mentre uova e mele vanno al plurale."]),
    (10, None, ["'Ecco cinquanta dalla cassa. Riporta indietro lo scontrino!' Il verbo accompagnato dalla particella in", (None, "Bring back"), "esprime chiaramente il movimento di riportare indietro qualcosa."]),
    (11, None, ["'Tenete duro qui, io sono già fuori dalla porta!' L'espressione idiomatica", (None, "Hold the fort"), "significa letteralmente difendere il fortino, cioè badare a tutto mentre qualcuno si assenta."]),
]
CALLOUT_TRANS = {
    "kitchen emergency": "emergenza in cucina",
    "Please do not say": "per favore non dire",
    "a flat tire": "una gomma a terra",
    "at all": "affatto, del tutto",
    "no butter": "niente burro",
    "hungry guests": "ospiti affamati",
    "at least": "almeno, se non altro",
    "some cash": "dei contanti",
    "there and back": "andata e ritorno",
    "Watch me": "stammi a guardare",
    "what to buy": "che cosa comprare",
    "Three bottles of milk": "tre bottiglie di latte",
    "Bring back": "riporta indietro",
    "Hold the fort": "tenete duro, badate a tutto",
}
