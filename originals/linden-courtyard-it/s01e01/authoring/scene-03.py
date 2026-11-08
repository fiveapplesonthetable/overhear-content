# Authoring module for linden-courtyard-it-s01e01-scene-03.
ID = "linden-courtyard-it-s01e01-scene-03"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = "Where Are My Glasses?  (Dove sono i miei occhiali?)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"arthur": "Arthur", "hannah": "Hannah", "graham": "Graham"}
INTRO = "Prima che arrivi il primo ospite della giornata, Arthur, il proprietario della locanda, entra di corsa dal cortile con aria agitata. Hannah e Graham lo osservano mentre si fruga nervosamente nelle tasche. Ascolta prima tutta la scena."
OPENER = "Rivediamo ora ogni battuta con tranquillità."
TRANSITION = "Ascoltiamo un'altra volta il dialogo completo a ritmo normale."
OUTRO = "Arthur ha ritrovato gli occhiali proprio sulla sua fronte mentre fuori si fermava l'auto davanti al cancello. Rilassati e lascia che il suono delle frasi ti diventi familiare; ci ritroviamo nella prossima scena."
CLOSING = ("arthur", "Bye for now!")
STORY = [
    ("arthur", "Good morning, everyone! Welcome, Hannah. Is everything ready?", "Buongiorno a tutti! Benvenuta, Hannah. È tutto pronto?"),
    ("hannah", "Good morning! Yes, the desk is clean and the keys are ready.", "Buongiorno! Sì, il bancone è pulito e le chiavi sono pronte."),
    ("arthur", "Today's guest in room four is staying all week. Everything must be perfect!", "L'ospite di oggi nella camera quattro si ferma tutta la settimana. Tutto dev'essere perfetto!"),
    ("graham", "Relax, Arthur. The room is clean and the towels are fresh.", "Rilassati, Arthur. La camera è pulita e gli asciugamani sono freschi di bucato."),
    ("arthur", "I need to read the reservation book, but I cannot find my glasses!", "Devo leggere il registro delle prenotazioni, ma non riesco a trovare i miei occhiali!"),
    ("hannah", "Are they in your coat pocket?", "Sono nella tasca del tuo cappotto?"),
    ("arthur", "No, only my pen and three old receipts!", "No, solo la mia penna e tre vecchie ricevute!"),
    ("graham", "Look in the mirror behind the desk, boss.", "Guarda nello specchio dietro il bancone, capo."),
    ("arthur", "Why would my glasses be in the... oh! They are on my head!", "Perché mai i miei occhiali dovrebbero essere nello... oh! Sono sulla mia testa!"),
    ("hannah", "Right there on your forehead, safe and sound.", "Proprio lì sulla tua fronte, sani e salvi."),
    ("arthur", "Do not tell anyone! Now, smile brightly when the bell rings.", "Non dirlo a nessuno! Adesso sorridi con entusiasmo quando suona il campanello."),
    ("graham", "Here comes a taxi at the gate right now.", "Ecco che arriva un taxi al cancello proprio adesso."),
]
WALK = [
    (0, None, ["'Buongiorno a tutti! Benvenuta, Hannah. È tutto pronto?' I pronomi indefiniti come", (None, "everything"), "vogliono sempre il verbo al singolare, ecco perché la domanda si apre con", (None, "Is everything ready"), "al singolare."]),
    (1, None, ["'Buongiorno! Sì, il bancone è pulito e le chiavi sono pronte.' Nota quanto è comodo l'aggettivo", (None, "ready"), "che resta identico sia per un oggetto solo sia per molte chiavi."]),
    (2, None, ["'L'ospite di oggi nella camera quattro si ferma tutta la settimana. Tutto dev'essere perfetto!' Anche le parole di tempo possono prendere il genitivo sassone con apostrofo ed esse, come in", (None, "Today's guest"), "l'ospite di oggi."]),
    (3, None, ["'Rilassati, Arthur. La camera è pulita e gli asciugamani sono freschi di bucato.' Un semplice", (None, "Relax"), "all'inizio della frase invita subito alla calma, come il nostro stai tranquillo."]),
    (4, None, ["'Devo leggere il registro delle prenotazioni, ma non riesco a trovare i miei occhiali!' Quando cerchi qualcosa senza riuscirci sul momento, l'inglese preferisce", (None, "cannot find"), "anziché il semplice non trovo."]),
    (5, None, ["'Sono nella tasca del tuo cappotto?' Dato che gli occhiali sono plurali anche in inglese, Hannah esprime il soggetto con", (None, "Are they"), "e unisce i due nomi in", (None, "coat pocket"), "senza preposizione."]),
    (6, None, ["'No, solo la mia penna e tre vecchie ricevute!' Attenzione alla grafia ingannevole di", (None, "receipts"), "dove la lettera pi centrale non si pronuncia affatto."]),
    (7, None, ["'Guarda nello specchio dietro il bancone, capo.' Come in italiano, ci si guarda dentro lo specchio con", (None, "in the mirror"), "mentre", (None, "behind the desk"), "indica la posizione dietro il bancone."]),
    (8, None, ["'Perché mai i miei occhiali dovrebbero essere nello... oh! Sono sulla mia testa!' L'ausiliare condizionale in", (None, "Why would"), "aggiunge una sfumatura di incredulità, come dire perché mai dovrebbero."]),
    (9, None, ["'Proprio lì sulla tua fronte, sani e salvi.' Il binomio fisso", (None, "safe and sound"), "corrisponde esattamente al nostro sani e salvi, usato con affetto anche per gli oggetti."]),
    (10, None, ["'Non dirlo a nessuno! Adesso sorridi con entusiasmo quando suona il campanello.' Per vietare o raccomandare di non fare qualcosa evitando doppie negazioni si usa", (None, "Do not tell anyone"), "con il pronome finale positivo."]),
    (11, None, ["'Ecco che arriva un taxi al cancello proprio adesso.' Per annunciare qualcuno o qualcosa che spunta sotto i tuoi occhi, l'inversione", (None, "Here comes"), "rende benissimo il nostro ecco che arriva."]),
]
CALLOUT_TRANS = {
    "everything": "tutto",
    "Is everything ready": "è tutto pronto",
    "ready": "pronto, pronte",
    "Today's guest": "l'ospite di oggi",
    "Relax": "rilassati, stai tranquillo",
    "cannot find": "non riesco a trovare",
    "Are they": "sono (essi)",
    "coat pocket": "tasca del cappotto",
    "receipts": "ricevute, scontrini",
    "in the mirror": "nello specchio",
    "behind the desk": "dietro il bancone",
    "Why would": "perché mai dovrebbero",
    "safe and sound": "sani e salvi",
    "Do not tell anyone": "non dirlo a nessuno",
    "Here comes": "ecco che arriva",
}
