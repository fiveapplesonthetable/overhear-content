# Authoring module for linden-courtyard-it-s01e06-scene-01.
ID = "linden-courtyard-it-s01e06-scene-01"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 6
SCENE = 1
TITLE = "At the Iron Gate  (Al cancello di ferro)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"caleb": "Caleb", "owen": "Owen", "hannah": "Hannah"}
INTRO = "Fuori, sotto i rami dell'albero alla Locanda del Cortile del Tiglio, a Portland, il fratello maggiore Owen resta dritto nel suo cappotto grigio davanti a Caleb, mentre Hannah posa una teiera calda e fa un passo indietro. Ascolta prima tutta la scena."
OPENER = "Ora rivediamo la conversazione con calma, frase per frase."
TRANSITION = "Ascoltiamo di nuovo tutta la scena a velocità naturale."
OUTRO = "Owen ha riconosciuto la grafia di Caleb in due secondi ed è venuto lo stesso. Nella prossima scena aprono il pacchetto di carta bianca sotto l'albero del cortile. Alla prossima."
CLOSING = ("hannah", "See you soon!")
STORY = [
    ("owen", "So 'someone with something from Grandfather' was you all along, Caleb.", "Quindi «qualcuno con qualcosa del nonno» eri tu fin dall'inizio, Caleb."),
    ("caleb", "Hello, Owen. Thank you for coming today.", "Ciao, Owen. Grazie per essere venuto oggi."),
    ("owen", "I recognized your neat block handwriting on that postcard in two seconds.", "Ho riconosciuto la tua calligrafia ordinata in stampatello su quella cartolina in due secondi."),
    ("caleb", "Wait, you knew it was from me and came anyway?", "Aspetta, sapevi che veniva da parte mia e sei venuto lo stesso?"),
    ("owen", "Of course I came. Why did you hide behind a mystery note?", "Certo che sono venuto. Perché ti sei nascosto dietro un biglietto misterioso?"),
    ("caleb", "Because I was afraid you were still angry. I missed you these three years.", "Perché avevo paura che fossi ancora arrabbiato. Mi sei mancato in questi tre anni."),
    ("owen", "Three stubborn years... honestly, little brother, I missed you too.", "Tre anni testardi... sinceramente, fratellino, sei mancato anche tu a me."),
    ("hannah", "Excuse me, gentlemen. Here is hot tea, and warm lemon cake is on the way.", "Scusatemi, signori. Ecco il tè caldo, e la torta tiepida al limone è in arrivo."),
    ("owen", "Lemon cake? Wait, how did she know about Friday lemon cake?", "Torta al limone? Aspetta, come faceva a sapere della torta al limone del venerdì?"),
    ("caleb", "Sit down, Owen, take off your heavy coat, and look at this blue suitcase.", "Siediti, Owen, togliti il cappotto pesante e guarda questa valigia blu."),
    ("owen", "Is that the old dark blue bag from Grandfather's workshop?", "È la vecchia borsa blu scuro del laboratorio del nonno?"),
    ("hannah", "Take all the time you need. The courtyard is yours.", "Prendetevi tutto il tempo che vi serve. Il cortile è vostro."),
]
WALK = [
    (0, None, ["'Quindi «qualcuno con qualcosa del nonno» eri tu fin dall'inizio, Caleb.' In", (None, "was you all along"), "il verbo resta alla terza persona singolare perché concorda col soggetto grammaticale qualcuno."]),
    (1, None, ["'Ciao, Owen. Grazie per essere venuto oggi.' La prima frase semplice suggerita da Hannah rompe subito il ghiaccio:", (None, "Thank you for coming today"), "limpida e calorosa."]),
    (2, None, ["'Ho riconosciuto la tua calligrafia ordinata in stampatello su quella cartolina in due secondi.' Per indicare i caratteri staccati non corsivi, la combinazione esatta è", (None, "block handwriting"), "scrittura in stampatello."]),
    (3, None, ["'Aspetta, sapevi che veniva da parte mia e sei venuto lo stesso?' La provenienza del messaggio sta in", (None, "from me"), "mentre", (None, "came anyway"), "aggiunge la sfumatura di essere venuto nonostante tutto."]),
    (4, None, ["'Certo che sono venuto. Perché ti sei nascosto dietro un biglietto misterioso?' Per confermare senza esitazioni si lega direttamente", (None, "Of course I came"), "e il rifugio dietro l'anonimato è", (None, "hide behind"), "nascondersi dietro."]),
    (5, None, ["'Perché avevo paura che fossi ancora arrabbiato. Mi sei mancato in questi tre anni.' Dove noi diciamo avere paura, l'inglese usa il verbo essere più aggettivo in", (None, "I was afraid"), "seguito da", (None, "still angry"), "ancora arrabbiato."]),
    (6, None, ["'Tre anni testardi... sinceramente, fratellino, sei mancato anche tu a me.' L'appellativo affettuoso", (None, "little brother"), "prepara la risposta simmetrica", (None, "I missed you too"), "con l'avverbio finale anche."]),
    (7, None, ["'Scusatemi, signori. Ecco il tè caldo, e la torta tiepida al limone è in arrivo.' Utilissima al ristorante o nelle consegne, la locuzione", (None, "is on the way"), "annuncia qualcosa che sta già arrivando."]),
    (8, None, ["'Torta al limone? Aspetta, come faceva a sapere della torta al limone del venerdì?' Quando si è al corrente di un dettaglio o di un ricordo preciso si abbina", (None, "know about"), "sapere riguardo a."]),
    (9, None, ["'Siediti, Owen, togliti il cappotto pesante e guarda questa valigia blu.' Per sfilarsi scarpe, giacche o cappelli si ricorre sempre al verbo con particella", (None, "take off"), "togliersi."]),
    (10, None, ["'È la vecchia borsa blu scuro del laboratorio del nonno?' Il genitivo sassone lega direttamente persona e luogo di lavoro in", (None, "Grandfather's workshop"), "il laboratorio del nonno."]),
    (11, None, ["'Prendetevi tutto il tempo che vi serve. Il cortile è vostro.' Grande cortesia ospitale nella formula", (None, "Take all the time you need"), "chiusa dal pronome possessivo autonomo", (None, "is yours"), "è vostro."]),
]
CALLOUT_TRANS = {
    "was you all along": "eri tu fin dall'inizio",
    "Thank you for coming today": "grazie per essere venuto oggi",
    "block handwriting": "scrittura in stampatello",
    "from me": "da parte mia",
    "came anyway": "sei venuto lo stesso",
    "Of course I came": "certo che sono venuto",
    "hide behind": "nasconderti dietro",
    "I was afraid": "avevo paura",
    "still angry": "ancora arrabbiato",
    "little brother": "fratellino",
    "I missed you too": "sei mancato anche tu a me",
    "is on the way": "è in arrivo",
    "know about": "sapere di",
    "take off": "togliti, togliersi",
    "Grandfather's workshop": "il laboratorio del nonno",
    "Take all the time you need": "prendetevi tutto il tempo che vi serve",
    "is yours": "è vostro",
}
