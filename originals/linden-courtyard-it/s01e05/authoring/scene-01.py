# Authoring module for linden-courtyard-it-s01e05-scene-01.
ID = "linden-courtyard-it-s01e05-scene-01"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = "Truth in the Courtyard  (La verità nel cortile)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"caleb": "Caleb", "hannah": "Hannah", "evelyn": "Evelyn"}
INTRO = "Sempre all'ombra dell'albero nel cortile della Locanda del Cortile del Tiglio, a Portland, Caleb si siede con Hannah e la signorina Evelyn per raccontare dall'inizio il mistero di lunedì sera. Ascolta prima tutta la scena."
OPENER = "Ora riascoltiamo la conversazione con calma, frase per frase."
TRANSITION = "Ascoltiamo di nuovo tutta la scena a velocità naturale."
OUTRO = "Tutti i tasselli di lunedì e martedì vanno finalmente al loro posto. Nella prossima scena Caleb racconta perché non parla da tre anni con suo fratello Owen. Alla prossima."
CLOSING = ("hannah", "See you soon!")
STORY = [
    ("evelyn", "Let me look at you properly, Caleb! You grew taller than the piano!", "Fatti guardare come si deve, Caleb! Sei cresciuto più del pianoforte!"),
    ("caleb", "I cannot believe you are staying in the exact same guesthouse, Miss Evelyn.", "Non riesco a credere che alloggi proprio nella stessa identica locanda, signorina Evelyn."),
    ("hannah", "Wait, so we rode the same train on Monday, and you took her suitcase?", "Aspetta, quindi lunedì abbiamo viaggiato sullo stesso treno e tu hai preso la sua valigia?"),
    ("caleb", "By complete accident! At my cousin's apartment I opened it and saw sheet music and a red ribbon.", "Per puro caso! Nell'appartamento di mio cugino l'ho aperta e ho visto degli spartiti e un nastro rosso."),
    ("evelyn", "Why did you leave my bag on the step at night and run away?", "Perché hai lasciato la mia borsa sul gradino di notte e sei scappato via?"),
    ("caleb", "Because when I walked here on Monday evening, I saw my older brother walking down this street!", "Perché lunedì sera, mentre venivo qui a piedi, ho visto mio fratello maggiore camminare lungo questa strada!"),
    ("hannah", "Your older brother lives here in Portland?", "Tuo fratello maggiore abita qui a Portland?"),
    ("caleb", "Yes. I panicked, rang your bell, and slipped the Friday note onto the handle.", "Sì. Sono andato nel panico, ho suonato il vostro campanello e ho infilato il biglietto del venerdì sulla maniglia."),
    ("evelyn", "Wait, and Wednesday night you checked in here under your real name?", "Aspetta, e mercoledì sera ti sei registrato qui col tuo vero nome?"),
    ("caleb", "I needed a quiet place nearby before Friday, and honestly forgot you still had my bag!", "Mi serviva un posto tranquillo qui vicino prima di venerdì, e sinceramente mi ero dimenticato che avevate ancora la mia borsa!"),
    ("hannah", "Until you called us on Tuesday asking us not to open the white package!", "Finché martedì non ci hai telefonato chiedendoci di non aprire il pacchetto bianco!"),
    ("caleb", "Everything in that white paper belongs to my brother Owen, not me.", "Tutto quello che c'è in quella carta bianca appartiene a mio fratello Owen, non a me."),
]
WALK = [
    (0, None, ["'Fatti guardare come si deve, Caleb! Sei cresciuto più del pianoforte!' Per confrontare l'altezza l'aggettivo prende la desinenza comparativa in", (None, "taller than the piano"), "più alto del pianoforte."]),
    (1, None, ["'Non riesco a credere che alloggi proprio nella stessa identica locanda, signorina Evelyn.' Lo stupore gioioso parte con", (None, "I cannot believe"), "e raddoppia l'enfasi grazie alla coppia", (None, "exact same"), "stessa identica."]),
    (2, None, ["'Aspetta, quindi lunedì abbiamo viaggiato sullo stesso treno e tu hai preso la sua valigia?' Nell'inglese americano i viaggi su rotaia o in autobus usano spesso il passato irregolare in", (None, "rode the same train"), "abbiamo viaggiato sullo stesso treno."]),
    (3, None, ["'Per puro caso! Nell'appartamento di mio cugino l'ho aperta e ho visto degli spartiti e un nastro rosso.' L'espressione idiomatica", (None, "By complete accident"), "chiarisce che è successo senza volerlo, mentre", (None, "sheet music"), "indica la musica stampata su fogli."]),
    (4, None, ["'Perché hai lasciato la mia borsa sul gradino di notte e sei scappato via?' Un solo ausiliare iniziale al passato regge entrambi i verbi nella forma base:", (None, "leave"), "e poi", (None, "run away"), "scappare via."]),
    (5, None, ["'Perché lunedì sera, mentre venivo qui a piedi, ho visto mio fratello maggiore camminare lungo questa strada!' Dopo un verbo di percezione visiva, la forma progressiva in", (None, "walking down this street"), "coglie il fratello nel pieno del movimento."]),
    (6, None, ["'Tuo fratello maggiore abita qui a Portland?' Per verificare un fatto inatteso Hannah lascia l'ordine affermativo in", (None, "lives here in Portland"), "affidando tutta la domanda alla voce che sale."]),
    (7, None, ["'Sì. Sono andato nel panico, ho suonato il vostro campanello e ho infilato il biglietto del venerdì sulla maniglia.' Tre passati in fila raccontano la fuga, dal suono in", (None, "rang your bell"), "fino al movimento preciso di", (None, "onto the handle"), "sopra la maniglia."]),
    (8, None, ["'Aspetta, e mercoledì sera ti sei registrato qui col tuo vero nome?' All'arrivo in albergo ci si registra con", (None, "checked in"), "mentre per il nome dichiarato sul registro si dice", (None, "under your real name"), "sotto il tuo vero nome."]),
    (9, None, ["'Mi serviva un posto tranquillo qui vicino prima di venerdì, e sinceramente mi ero dimenticato che avevate ancora la mia borsa!' Una sola parola compatta,", (None, "nearby"), "basta per dire nelle vicinanze senza aggiungere preposizioni."]),
    (10, None, ["'Finché martedì non ci hai telefonato chiedendoci di non aprire il pacchetto bianco!' Nelle richieste indirette la negazione precede sempre l'infinito completo, come senti in", (None, "not to open"), "di non aprire."]),
    (11, None, ["'Tutto quello che c'è in quella carta bianca appartiene a mio fratello Owen, non a me.' Il verbo dell'appartenenza si costruisce immancabilmente con la preposizione di direzione in", (None, "belongs to my brother"), "appartiene a mio fratello."]),
]
CALLOUT_TRANS = {
    "taller than the piano": "più alto del pianoforte",
    "I cannot believe": "non riesco a credere",
    "exact same": "stessa identica",
    "rode the same train": "abbiamo viaggiato sullo stesso treno",
    "By complete accident": "per puro caso",
    "sheet music": "spartiti musicali",
    "leave": "lasciare",
    "run away": "scappare via",
    "walking down this street": "camminare lungo questa strada",
    "lives here in Portland": "abita qui a Portland",
    "rang your bell": "ho suonato il vostro campanello",
    "onto the handle": "sulla maniglia",
    "checked in": "ti sei registrato",
    "under your real name": "col tuo vero nome",
    "nearby": "qui vicino, nelle vicinanze",
    "not to open": "di non aprire",
    "belongs to my brother": "appartiene a mio fratello",
}
