# Authoring module for linden-courtyard-it-s01e06-scene-07.
ID = "linden-courtyard-it-s01e06-scene-07"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 6
SCENE = 7
TITLE = "Under the Golden Lanterns  (Sotto le lanterne dorate)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"hannah": "Hannah", "evelyn": "Evelyn", "owen": "Owen"}
INTRO = "Un tramonto mite scende su Portland e i fili di lanterne dorate di carta brillano sopra l'albero della Locanda del Cortile del Tiglio. Hannah, la signorina Evelyn e Owen condividono tè caldo e ricordi musicali. Ascolta prima tutta la scena."
OPENER = "Rivediamo adesso la conversazione con calma, frase per frase."
TRANSITION = "Torniamo ad ascoltare tutta la scena a velocità naturale."
OUTRO = "Lanterne dorate lassù in alto, vecchi amici riuniti e la caffetteria del cortile pronta ad aprire domattina alle otto. Resta una sola scena nella prima stagione, e Graham ha appena scovato qualcosa di curioso in cantina. Alla prossima."
CLOSING = ("evelyn", "Good night!")
STORY = [
    ("evelyn", "Look up at those golden lanterns against the evening sky. How peaceful!", "Alzate lo sguardo verso quelle lanterne dorate contro il cielo della sera. Che pace!"),
    ("owen", "To think on Monday morning Caleb picked up the wrong blue bag on Platform Two.", "E pensare che lunedì mattina Caleb ha preso la valigia blu sbagliata sul binario due."),
    ("hannah", "If he had picked up the right bag, none of us would be standing here tonight!", "Se avesse preso la valigia giusta, nessuno di noi sarebbe qui in piedi stasera!"),
    ("evelyn", "My teacup survived, two brothers made peace, and Hannah found a new home.", "La mia tazza da tè è sopravvissuta, due fratelli hanno fatto pace e Hannah ha trovato una nuova casa."),
    ("owen", "Miss Evelyn, Caleb and I booked a quiet dinner nearby. Will you join us tomorrow?", "Signorina Evelyn, Caleb e io abbiamo prenotato una cenetta tranquilla qui vicino. Si unirà a noi domani?"),
    ("evelyn", "Gladly, Owen, as long as nobody talks about selling old pianos!", "Volentieri, Owen, a patto che nessuno parli di vendere vecchi pianoforti!"),
    ("hannah", "And tomorrow morning at eight, your first courtyard coffees are on the house!", "E domani mattina alle otto, i vostri primi caffè nel cortile li offre la casa!"),
    ("owen", "We will bring half of City Hall to Tessa's tables next week, I promise.", "La settimana prossima porteremo mezzo Municipio ai tavoli di Tessa, lo prometto."),
    ("evelyn", "Listen, even the buzzer from room four has been quiet all evening!", "Ascoltate, perfino il cicalino della camera quattro è rimasto silenzioso per tutta la sera!"),
    ("hannah", "Do not tempt it, Miss Evelyn! I am almost fond of those two rings now.", "Non sfidi la sorte, signorina Evelyn! Ormai mi sono quasi affezionata a quei due squilli."),
    ("owen", "Here is to the Linden Courtyard Inn, the loudest quiet place in Portland!", "Un brindisi alla Locanda del Cortile del Tiglio, il posto tranquillo più rumoroso di Portland!"),
    ("hannah", "To good neighbors, warm bread, and open gates!", "Ai buoni vicini, al pane caldo e ai cancelli aperti!"),
]
WALK = [
    (0, None, ["'Alzate lo sguardo verso quelle lanterne dorate contro il cielo della sera. Che pace!' Il contrasto luminoso sullo sfondo scuro si disegna con", (None, "against the evening sky"), "e l'esclamazione ammirata con", (None, "How peaceful"), "quanta pace."]),
    (1, None, ["'E pensare che lunedì mattina Caleb ha preso la valigia blu sbagliata sul binario due.' Proprio come in italiano, un pensiero retrospettivo pieno di meraviglia parte con l'infinito", (None, "To think"), "mentre", (None, "picked up"), "indica sollevare da terra."]),
    (2, None, ["'Se avesse preso la valigia giusta, nessuno di noi sarebbe qui in piedi stasera!' Quando il gruppo conta tre o più persone, per escludere tutti quanti si usa", (None, "none of us"), "nessuno di noi."]),
    (3, None, ["'La mia tazza da tè è sopravvissuta, due fratelli hanno fatto pace e Hannah ha trovato una nuova casa.' Fare pace dopo un lungo disaccordo corrisponde esattamente a", (None, "made peace"), "hanno fatto pace."]),
    (4, None, ["'Signorina Evelyn, Caleb e io abbiamo prenotato una cenetta tranquilla qui vicino. Si unirà a noi domani?' L'invito conviviale più elegante e frequente è", (None, "Will you join us"), "vorrà unirsi a noi."]),
    (5, None, ["'Volentieri, Owen, a patto che nessuno parli di vendere vecchi pianoforti!' Si accetta un invito con il caloroso", (None, "Gladly"), "aggiungendo una condizione scherzosa tramite", (None, "as long as"), "purché, a patto che."]),
    (6, None, ["'E domani mattina alle otto, i vostri primi caffè nel cortile li offre la casa!' Nei bar e nei ristoranti, ciò che viene offerto gratuitamente dal locale è", (None, "on the house"), "offerto dalla casa."]),
    (7, None, ["'La settimana prossima porteremo mezzo Municipio ai tavoli di Tessa, lo prometto.' Per indicare la metà di un ente o di un gruppo si usa", (None, "half of"), "metà di."]),
    (8, None, ["'Ascoltate, perfino il cicalino della camera quattro è rimasto silenzioso per tutta la sera!' Dato che la serata è ancora in corso, Evelyn sceglie il passato composto", (None, "has been quiet"), "è rimasto tranquillo finora."]),
    (9, None, ["'Non sfidi la sorte, signorina Evelyn! Ormai mi sono quasi affezionata a quei due squilli.' Per dire per carità non dirlo a voce alta si usa", (None, "Do not tempt it"), "mentre affezionarsi a qualcosa è essere", (None, "fond of"), "affezionata a."]),
    (10, None, ["'Un brindisi alla Locanda del Cortile del Tiglio, il posto tranquillo più rumoroso di Portland!' Sollevando tazze o bicchieri si apre sempre il brindisi con", (None, "Here is to"), "seguito dal simpatico paradosso", (None, "loudest quiet place"), "il posto tranquillo più chiassoso."]),
    (11, None, ["'Ai buoni vicini, al pane caldo e ai cancelli aperti!' Nel proseguire un brindisi basta la preposizione iniziale, chiudendo sull'immagine accogliente di", (None, "open gates"), "cancelli aperti."]),
]
CALLOUT_TRANS = {
    "against the evening sky": "contro il cielo della sera",
    "How peaceful": "che pace",
    "To think": "e pensare che",
    "picked up": "ha preso, ha raccolto",
    "none of us": "nessuno di noi",
    "made peace": "hanno fatto pace",
    "Will you join us": "si unirà a noi",
    "Gladly": "volentieri",
    "as long as": "a patto che, purché",
    "on the house": "offerto dalla casa",
    "half of": "mezzo, metà di",
    "has been quiet": "è rimasto silenzioso",
    "Do not tempt it": "non sfidi la sorte",
    "fond of": "affezionata a",
    "Here is to": "un brindisi a",
    "loudest quiet place": "il posto tranquillo più rumoroso",
    "open gates": "cancelli aperti",
}
