# Authoring module for linden-courtyard-it-s01e02-scene-08.
ID = "linden-courtyard-it-s01e02-scene-08"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 2
SCENE = 8
TITLE = "Two Names, One Room  (Due nomi, una camera)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"arthur": "Arthur", "hannah": "Hannah", "graham": "Graham"}
INTRO = "Il mercoledì sera, mentre scende il crepuscolo su Portland, Arthur esce pallido dal suo ufficio tenendo in mano sia la tavoletta elettronica sia il registro di carta di Graham. Hannah e Graham alzano subito lo sguardo. Ascolta prima la scena."
OPENER = "Controlliamo riga per riga che cosa ha appena scoperto Arthur."
TRANSITION = "Riascoltiamo ancora una volta tutta la scena a velocità naturale."
OUTRO = "Due ospiti prenotati nella camera sette, la pioggia fuori e appena quaranta minuti prima del treno delle otto. Così termina il secondo episodio; ti aspettiamo nel terzo per vedere se la soffitta salverà la serata!"
CLOSING = ("arthur", "See you tomorrow!")
STORY = [
    ("arthur", "Graham... Hannah... please tell me room six is free tonight.", "Graham... Hannah... vi prego, ditemi che la camera sei è libera stasera."),
    ("hannah", "No, Arthur, the couple from the south checked into room six an hour ago.", "No, Arthur, la coppia venuta dal sud ha preso possesso della camera sei un'ora fa."),
    ("graham", "Every key from one to seven is taken, and room eight has wet paint.", "Ogni chiave dalla uno alla sette è occupata, e la camera otto ha la vernice fresca."),
    ("arthur", "Oh, disaster! Yesterday I took a phone booking on the tablet without my glasses!", "Che disastro! Ieri ho segnato una prenotazione telefonica sulla tavoletta senza i miei occhiali!"),
    ("hannah", "Wait, let me look at the tablet screen and the paper book together.", "Aspetta, fammi controllare insieme lo schermo e il registro di carta."),
    ("graham", "Let me guess. You promised somebody a room we do not have?", "Fammi indovinare. Hai promesso a qualcuno una camera che non abbiamo?"),
    ("hannah", "Arthur! Room seven is already occupied, and you booked a second guest into room seven!", "Arthur! La camera sette è già occupata, e hai prenotato un secondo ospite nella camera sette!"),
    ("arthur", "And he arrives here at eight o'clock this evening, in forty minutes!", "E arriva col treno serale delle otto, tra quaranta minuti!"),
    ("graham", "Told you that tablet is a trap.", "Te l'avevo detto che quell'aggeggio elettronico è una trappola."),
    ("arthur", "It is raining outside and every hotel on our street is full! What do we do?", "Fuori piove e ogni albergo nella nostra via è al completo! Che cosa facciamo?"),
    ("hannah", "Wait, what is on the third floor above the stairs?", "Aspettate, che cosa c'è al terzo piano in cima alle scale?"),
    ("graham", "The old sunny attic study... follow me, quickly!", "Il vecchio studio luminoso in soffitta... seguitemi, presto!"),
]
WALK = [
    (0, None, ["'Graham... Hannah... vi prego, ditemi che la camera sei è libera stasera.' Una stanza non prenotata e disponibile per la notte si descrive semplicemente con", (None, "is free tonight"), "è libera stasera."]),
    (1, None, ["'No, Arthur, la coppia venuta dal sud ha preso possesso della camera sei un'ora fa.' Quando un ospite entra ufficialmente in una stanza specifica si usa il verbo frasale", (None, "checked into room six"), "seguito dal numero."]),
    (2, None, ["'Ogni chiave dalla uno alla sette è occupata, e la camera otto ha la vernice fresca.' Sui cartelli di avviso dove noi scriviamo vernice fresca, l'inglese dice letteralmente vernice bagnata:", (None, "wet paint"), "appena stesa."]),
    (3, None, ["'Che disastro! Ieri ho segnato una prenotazione telefonica sulla tavoletta senza i miei occhiali!' Con schermi, telefoni e dispositivi digitali l'inglese usa sempre la preposizione di superficie in", (None, "on the tablet"), "sullo schermo."]),
    (4, None, ["'Aspetta, fammi controllare insieme lo schermo e il registro di carta.' Posizionato in chiusura di frase,", (None, "together"), "indica il confronto fianco a fianco tra due fonti diverse."]),
    (5, None, ["'Fammi indovinare. Hai promesso a qualcuno una camera che non abbiamo?' Prima di anticipare con ironia la conclusione altrui si apre con", (None, "Let me guess"), "identico al nostro fammi indovinare."]),
    (6, None, ["'Arthur! La camera sette è già occupata, e hai prenotato un secondo ospite nella camera sette!' La stessa parola che indica un libro funziona anche come verbo per registrare una prenotazione in", (None, "you booked"), "hai prenotato."]),
    (7, None, ["'E arriva col treno serale delle otto, tra quaranta minuti!' Per gli orari ferroviari e dei trasporti pubblici, il presente semplice", (None, "he arrives"), "è la scelta più naturale anche parlando di stasera."]),
    (8, None, ["'Te l'avevo detto che quell'aggeggio elettronico è una trappola.' Nel parlato confidenziale cade spesso il pronome soggetto iniziale nella celebre battuta", (None, "Told you"), "te l'avevo detto."]),
    (9, None, ["'Fuori piove e ogni albergo nella nostra via è al completo! Che cosa facciamo?' Quando cerchi subito una soluzione pratica insieme agli altri chiedi al presente", (None, "What do we do"), "che cosa facciamo."]),
    (10, None, ["'Aspettate, che cosa c'è al terzo piano in cima alle scale?' Ricordando il conteggio americano dei piani a partire da terra,", (None, "on the third floor"), "indica il livello della mansarda sopra le camere."]),
    (11, None, ["'Il vecchio studio luminoso in soffitta... seguitemi, presto!' Due parole cariche di energia per chiudere la puntata:", (None, "follow me"), "seguitemi."]),
]
CALLOUT_TRANS = {
    "is free tonight": "è libera stasera",
    "checked into room six": "ha preso la camera sei",
    "wet paint": "vernice fresca",
    "on the tablet": "sul tablet, sullo schermo",
    "together": "insieme",
    "Let me guess": "fammi indovinare",
    "you booked": "hai prenotato",
    "he arrives": "arriva",
    "Told you": "te l'avevo detto",
    "What do we do": "che cosa facciamo",
    "on the third floor": "al terzo piano",
    "follow me": "seguimi, seguitemi",
}
