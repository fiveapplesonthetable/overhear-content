# Authoring module for linden-courtyard-it-s01e02-scene-01.
ID = "linden-courtyard-it-s01e02-scene-01"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 2
SCENE = 1
TITLE = "The Red Ribbon  (Il nastro rosso)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"hannah": "Hannah", "evelyn": "Evelyn", "graham": "Graham"}
INTRO = "Il martedì mattina sorge limpido e luminoso alla Locanda del Cortile del Tiglio. Evelyn scende svelta al bancone d'ingresso, dove Hannah e Graham la aspettano con la sua valigia ritrovata. Ascolta prima tutta la scena in inglese."
OPENER = "Ora ripassiamo il dialogo con calma, battuta per battuta."
TRANSITION = "Torniamo ad ascoltare l'intera scena di seguito."
OUTRO = "Evelyn ha ritrovato la sua tazza e i suoi abiti, mentre affiora un ricordo di venticinque anni prima. Tra poco in cucina scoppierà un piccolo imprevisto prima della colazione. Alla prossima."
CLOSING = ("evelyn", "See you soon!")
STORY = [
    ("hannah", "Good morning, Miss Evelyn! Look what arrived at our gate last night.", "Buongiorno, signorina Evelyn! Guardi che cosa è arrivato al nostro cancello ieri sera."),
    ("evelyn", "My suitcase! Let me open the top pocket... yes, my red ribbon!", "La mia valigia! Mi faccia aprire la tasca superiore... sì, il mio nastro rosso!"),
    ("graham", "And your teacup inside? Is it still in one piece?", "E la sua tazza da tè all'interno? È ancora tutta intera?"),
    ("evelyn", "Not a single crack! Who brought it back?", "Nemmeno una singola crepa! Chi l'ha riportata indietro?"),
    ("hannah", "We do not know. Someone left it on the step and rang the bell.", "Non lo sappiamo. Qualcuno l'ha lasciata sul gradino e ha suonato il campanello."),
    ("evelyn", "And he did not ask for his own suitcase with the wooden train?", "E non ha chiesto della sua valigia con il treno di legno?"),
    ("graham", "He left a short note asking us to keep it until Friday.", "Ha lasciato un breve biglietto chiedendoci di tenerla fino a venerdì."),
    ("evelyn", "How curious! The handwriting on that tag felt oddly familiar to me.", "Che cosa curiosa! La calligrafia su quell'etichetta mi è sembrata stranamente familiare."),
    ("hannah", "Really? Do you know someone in Portland?", "Davvero? Conosce qualcuno a Portland?"),
    ("evelyn", "Twenty-five years ago I taught piano near here, though memories fade.", "Venticinque anni fa insegnavo pianoforte qui vicino, anche se i ricordi sbiadiscono."),
    ("graham", "For now, his bag stays safe under lock and key.", "Per ora la sua borsa resta al sicuro sotto chiave."),
    ("evelyn", "Wonderful! Now I am ready for a big breakfast.", "Meraviglioso! Ora sono pronta per una bella colazione abbondante."),
]
WALK = [
    (0, None, ["'Buongiorno, signorina Evelyn! Guardi che cosa è arrivato al nostro cancello ieri sera.' Dove noi diciamo ieri sera o stanotte, l'inglese unisce aggettivo e sostantivo in", (None, "last night"), "letteralmente la notte scorsa."]),
    (1, None, ["'La mia valigia! Mi faccia aprire la tasca superiore... sì, il mio nastro rosso!' La formula", (None, "Let me open"), "annuncia ciò che stai per fare tu stesso, seguita dal verbo base senza preposizione."]),
    (2, None, ["'E la sua tazza da tè all'interno? È ancora tutta intera?' L'espressione figurata", (None, "in one piece"), "significa in un pezzo solo, perfetta per chiedere se un oggetto fragile è intatto."]),
    (3, None, ["'Nemmeno una singola crepa! Chi l'ha riportata indietro?' Quando il pronome interrogativo chi fa da soggetto della frase, come in", (None, "Who brought it back"), "non si usa alcun ausiliare."]),
    (4, None, ["'Non lo sappiamo. Qualcuno l'ha lasciata sul gradino e ha suonato il campanello.' Nella risposta negativa", (None, "We do not know"), "non serve aggiungere alcun pronome oggetto equivalente al nostro lo."]),
    (5, None, ["'E non ha chiesto della sua valigia con il treno di legno?' Per chiedere o reclamare un oggetto si abbina sempre il verbo alla preposizione in", (None, "ask for"), "chiedere di avere."]),
    (6, None, ["'Ha lasciato un breve biglietto chiedendoci di tenerla fino a venerdì.' La struttura compatta", (None, "asking us to keep"), "collega direttamente la persona all'infinito con preposizione."]),
    (7, None, ["'Che cosa curiosa! La calligrafia su quell'etichetta mi è sembrata stranamente familiare.' La grafia scritta a mano ha un nome composto trasparente:", (None, "handwriting"), "formato da mano e scrittura."]),
    (8, None, ["'Davvero? Conosce qualcuno a Portland?' Il verbo conoscere regge direttamente la persona senza preposizioni in", (None, "know someone"), "conoscere qualcuno."]),
    (9, None, ["'Venticinque anni fa insegnavo pianoforte qui vicino, anche se i ricordi sbiadiscono.' L'equivalente di fa si mette sempre dopo la misura di tempo in", (None, "Twenty-five years ago"), "seguito dal passato irregolare", (None, "taught"), "insegnavo."]),
    (10, None, ["'Per ora la sua borsa resta al sicuro sotto chiave.' Il modo di dire", (None, "under lock and key"), "rafforza il nostro sotto chiave nominando sia la serratura sia la chiave."]),
    (11, None, ["'Meraviglioso! Ora sono pronta per una bella colazione abbondante.' Dopo l'aggettivo pronto, l'inglese introduce il sostantivo con la preposizione in", (None, "ready for"), "pronta per."]),
]
CALLOUT_TRANS = {
    "last night": "ieri sera, stanotte",
    "Let me open": "mi faccia aprire",
    "in one piece": "tutta intera, intatta",
    "Who brought it back": "chi l'ha riportata indietro",
    "We do not know": "non lo sappiamo",
    "ask for": "chiedere, reclamare",
    "asking us to keep": "chiedendoci di tenere",
    "handwriting": "calligrafia, scrittura a mano",
    "know someone": "conoscere qualcuno",
    "Twenty-five years ago": "venticinque anni fa",
    "taught": "insegnavo, ho insegnato",
    "under lock and key": "sotto chiave",
    "ready for": "pronta per",
}
