# Authoring module for linden-courtyard-it-s01e06-scene-02.
ID = "linden-courtyard-it-s01e06-scene-02"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 6
SCENE = 2
TITLE = "The Wooden Train  (Il treno di legno)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"caleb": "Caleb", "owen": "Owen", "evelyn": "Evelyn"}
INTRO = "Seduti al tavolo rotondo nel cortile della Locanda del Cortile del Tiglio, Caleb apre la valigia blu scuro e porge a Owen il pacchetto avvolto nella carta bianca, mentre la signorina Evelyn si avvicina piano lungo il vialetto. Ascoltiamo prima."
OPENER = "Adesso ripercorriamo il dialogo con calma, battuta per battuta."
TRANSITION = "Riascoltiamo ora tutta la scena di seguito."
OUTRO = "Il trenino di legno del nonno è tornato a casa e lo stupore di Owen davanti alla signorina Evelyn ha riempito il cortile di sorrisi. Dentro, però, Arthur fissa ancora quella lettera. A tra poco."
CLOSING = ("evelyn", "See you later!")
STORY = [
    ("caleb", "Before the movers cleared the house, I saved this box from the attic shelf.", "Prima che i traslocatori sgomberassero la casa, ho salvato questa scatola dallo scaffale della soffitta."),
    ("owen", "Open the white paper... no! Grandfather's carved wooden train engine!", "Apri la carta bianca... non ci credo! La locomotiva di legno intagliato del nonno!"),
    ("caleb", "Look underneath the wheels. Your name and mine are still penciled there.", "Guarda sotto le ruote. Il tuo nome e il mio sono ancora scritti a matita lì sotto."),
    ("owen", "I thought this was lost when we sold the house! Why keep it for me?", "Pensavo che fosse andato perduto quando abbiamo venduto la casa! Perché conservarlo per me?"),
    ("caleb", "Because a house is brick and timber, Owen, while family is what we keep.", "Perché una casa è fatta di mattoni e travi di legno, Owen, mentre la famiglia è ciò che custodiamo."),
    ("evelyn", "And you two boys kept the best part of Number twelve right here.", "E voi due ragazzi avete custodito la parte migliore del civico dodici proprio qui."),
    ("owen", "Excuse me, ma'am... wait. That voice! Miss Evelyn, my piano teacher?!", "Mi scusi, signora... aspetti. Questa voce! Signorina Evelyn, la mia insegnante di pianoforte?!"),
    ("evelyn", "Still waiting for you to play your F major scale slowly, Owen!", "Sto ancora aspettando che tu suoni lentamente la scala di fa maggiore, Owen!"),
    ("owen", "Am I dreaming?! Did you plan this whole reunion, Caleb?", "Sto sognando?! Hai organizzato tu tutta questa rimpatriata, Caleb?"),
    ("caleb", "Pure luck, and one swapped blue suitcase on Monday morning's train!", "Pura fortuna, e una valigia blu scambiata sul treno di lunedì mattina!"),
    ("evelyn", "Life arranges better duets than we do, my dear boys.", "La vita organizza duetti migliori di quanto sappiamo fare noi, miei cari ragazzi."),
    ("owen", "Please sit with us, Miss Evelyn! Tell me I am not twenty-five years late for my lesson!", "Per favore, si sieda con noi, signorina Evelyn! Mi dica che non sono in ritardo di venticinque anni per la lezione!"),
]
WALK = [
    (0, None, ["'Prima che i traslocatori sgomberassero la casa, ho salvato questa scatola dallo scaffale della soffitta.' Gli addetti ai traslochi si chiamano", (None, "the movers"), "mentre", (None, "attic shelf"), "compatta soffitta e scaffale senza preposizioni."]),
    (1, None, ["'Apri la carta bianca... non ci credo! La locomotiva di legno intagliato del nonno!' Osserva la catena ordinata di descrittori in", (None, "carved wooden train engine"), "lavorazione a intaglio, materiale e tipo di treno."]),
    (2, None, ["'Guarda sotto le ruote. Il tuo nome e il mio sono ancora scritti a matita lì sotto.' La posizione proprio sul fondo è resa da", (None, "underneath the wheels"), "e dal nome per matita nasce il participio", (None, "penciled"), "scritto a lapis."]),
    (3, None, ["'Pensavo che fosse andato perduto quando abbiamo venduto la casa! Perché conservarlo per me?' Per chiedere il motivo di una scelta basta accostare l'interrogativo al verbo nudo in", (None, "Why keep it"), "perché tenerlo."]),
    (4, None, ["'Perché una casa è fatta di mattoni e travi di legno, Owen, mentre la famiglia è ciò che custodiamo.' La materia edilizia grezza è", (None, "brick and timber"), "messa a confronto con", (None, "what we keep"), "ciò che conserviamo."]),
    (5, None, ["'E voi due ragazzi avete custodito la parte migliore del civico dodici proprio qui.' Il superlativo irregolare di buono risplende al centro di", (None, "the best part"), "la parte migliore."]),
    (6, None, ["'Mi scusi, signora... aspetti. Questa voce! Signorina Evelyn, la mia insegnante di pianoforte?!' Rivolgendosi con rispetto a una signora non ancora riconosciuta si usa il cortese", (None, "ma'am"), "prima di esclamare", (None, "piano teacher"), "insegnante di pianoforte."]),
    (7, None, ["'Sto ancora aspettando che tu suoni lentamente la scala di fa maggiore, Owen!' Dove noi usiamo una subordinata col congiuntivo, l'inglese preferisce la costruzione snella", (None, "waiting for you to play"), "aspettando che tu suoni."]),
    (8, None, ["'Sto sognando?! Hai organizzato tu tutta questa rimpatriata, Caleb?' Davanti a una coincidenza incredibile scatta spontanea la domanda progressiva", (None, "Am I dreaming"), "sto forse sognando."]),
    (9, None, ["'Pura fortuna, e una valigia blu scambiata sul treno di lunedì mattina!' Dopo l'esclamazione", (None, "Pure luck"), "il participio", (None, "swapped"), "riassume l'intero scambio involontario di bagagli."]),
    (10, None, ["'La vita organizza duetti migliori di quanto sappiamo fare noi, miei cari ragazzi.' Per evitare di ripetere il verbo principale nel secondo termine di paragone, si chiude con l'ausiliare vicario in", (None, "better duets than we do"), "duetti migliori dei nostri."]),
    (11, None, ["'Per favore, si sieda con noi, signorina Evelyn! Mi dica che non sono in ritardo di venticinque anni per la lezione!' Come per l'anticipo, anche la misura del ritardo precede subito l'aggettivo in", (None, "twenty-five years late"), "in ritardo di venticinque anni."]),
]
CALLOUT_TRANS = {
    "the movers": "i traslocatori",
    "attic shelf": "scaffale della soffitta",
    "carved wooden train engine": "locomotiva di legno intagliato",
    "underneath the wheels": "sotto le ruote",
    "penciled": "scritti a matita",
    "Why keep it": "perché conservarlo",
    "brick and timber": "mattoni e travi di legno",
    "what we keep": "ciò che custodiamo",
    "the best part": "la parte migliore",
    "ma'am": "signora",
    "piano teacher": "insegnante di pianoforte",
    "waiting for you to play": "aspettando che tu suoni",
    "Am I dreaming": "sto sognando",
    "Pure luck": "pura fortuna",
    "swapped": "scambiata",
    "better duets than we do": "duetti migliori di quanto facciamo noi",
    "twenty-five years late": "in ritardo di venticinque anni",
}
