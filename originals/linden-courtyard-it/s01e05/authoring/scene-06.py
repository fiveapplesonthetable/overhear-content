# Authoring module for linden-courtyard-it-s01e05-scene-06.
ID = "linden-courtyard-it-s01e05-scene-06"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 5
SCENE = 6
TITLE = "Ten Minutes to Twelve  (Dieci minuti alle dodici)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"arthur": "Arthur", "hannah": "Hannah", "tessa": "Tessa"}
INTRO = "Dentro, al bancone della Locanda del Cortile del Tiglio, alle undici e cinquanta Arthur si raddrizza la cravatta blu pulita mentre Hannah e Tessa tengono d'occhio l'orologio, proprio quando il postino appoggia una busta bianca spessa. Ascoltiamo prima."
OPENER = "Rivediamo ora ogni battuta con calma, una per volta."
TRANSITION = "Ascoltiamo di nuovo l'intera scena a velocità naturale."
OUTRO = "Quella busta spessa col timbro rosso resta chiusa sul bancone mentre le campane della chiesa cominciano a suonare mezzogiorno. Usciamo verso il cancello nella prossima scena."
CLOSING = ("tessa", "See you later!")
STORY = [
    ("arthur", "How does my tie look today, Hannah? Zero orange juice in sight!", "Come sta la mia cravatta oggi, Hannah? Zero succo d'arancia in vista!"),
    ("hannah", "Sharp and spotless, Arthur! Even your glasses are on your nose instead of your forehead.", "Elegante e immacolata, Arthur! Perfino i tuoi occhiali sono sul naso invece che sulla fronte."),
    ("arthur", "Progress! Today our courtyard hosts a family reunion. Quiet dignity from everyone!", "Grandi passi avanti! Oggi il nostro cortile ospita un ricongiungimento familiare. Sobria dignità da parte di tutti!"),
    ("tessa", "Says the man peeking through the lace curtain every thirty seconds!", "Lo dice l'uomo che sbircia dalla tenda di pizzo ogni trenta secondi!"),
    ("arthur", "I am checking the weather, Tessa! Who left this thick envelope by the bell?", "Sto controllando il tempo, Tessa! Chi ha lasciato questa busta spessa accanto al campanello?"),
    ("hannah", "The mailman just asked me to sign for it. It has a red property office stamp.", "Il postino mi ha appena chiesto di firmare per ritirarla. Porta un timbro rosso dell'ufficio immobiliare."),
    ("arthur", "From the building landlord's lawyer? Strange, our rent is paid until next summer.", "Dall'avvocato del proprietario dell'edificio? Strano, il nostro affitto è pagato fino alla prossima estate."),
    ("tessa", "Open it after twelve, boss! Look at the clock: five minutes to noon!", "Aprila dopo le dodici, capo! Guarda l'orologio: mancano cinque minuti a mezzogiorno!"),
    ("arthur", "Right you are. Paperwork can wait. Put it beside the book for now.", "Hai proprio ragione. Le scartoffie possono aspettare. Mettila accanto al registro per ora."),
    ("hannah", "I placed the blue suitcase right beside Caleb's table under the tree.", "Ho sistemato la valigia blu proprio accanto al tavolo di Caleb sotto l'albero."),
    ("tessa", "And the teapot is hot! Everybody step back from the window!", "E la teiera è bollente! Tutti indietro di un passo dalla finestra!"),
    ("arthur", "Listen... the church clock down the street is starting to chime twelve!", "Ascoltate... l'orologio della chiesa in fondo alla via sta cominciando a battere le dodici!"),
]
WALK = [
    (0, None, ["'Come sta la mia cravatta oggi, Hannah? Zero succo d'arancia in vista!' Per chiedere un parere sull'aspetto di un vestito si apre con", (None, "How does my tie look"), "mentre", (None, "in sight"), "vale in vista."]),
    (1, None, ["'Elegante e immacolata, Arthur! Perfino i tuoi occhiali sono sul naso invece che sulla fronte.' Il binomio brillante", (None, "Sharp and spotless"), "elogia un abbigliamento curato e senza nemmeno una macchia."]),
    (2, None, ["'Grandi passi avanti! Oggi il nostro cortile ospita un ricongiungimento familiare. Sobria dignità da parte di tutti!' Quando parenti lontani si ritrovano insieme, la formula fissa è", (None, "family reunion"), "riunione di famiglia."]),
    (3, None, ["'Lo dice l'uomo che sbircia dalla tenda di pizzo ogni trenta secondi!' Per punzecchiare con simpatia chi predica bene si attacca con l'inversione", (None, "Says the man"), "seguita dal gesto furtivo", (None, "peeking through"), "che sbircia attraverso."]),
    (4, None, ["'Sto controllando il tempo, Tessa! Chi ha lasciato questa busta spessa accanto al campanello?' In senso spaziale la piccola preposizione", (None, "by the bell"), "indica vicinanza immediata: proprio lì accanto al campanello."]),
    (5, None, ["'Il postino mi ha appena chiesto di firmare per ritirarla. Porta un timbro rosso dell'ufficio immobiliare.' Con pacchi e raccomandate, l'espressione postale esatta è", (None, "sign for it"), "mettere una firma per la consegna."]),
    (6, None, ["'Dall'avvocato del proprietario dell'edificio? Strano, il nostro affitto è pagato fino alla prossima estate.' La scadenza nel tempo viene fissata in modo trasparente da", (None, "until next summer"), "senza articolo davanti alla stagione."]),
    (7, None, ["'Aprila dopo le dodici, capo! Guarda l'orologio: mancano cinque minuti a mezzogiorno!' Nella seconda metà dell'ora i minuti mancanti si legano all'ora successiva in", (None, "five minutes to noon"), "cinque minuti a mezzogiorno."]),
    (8, None, ["'Hai proprio ragione. Le scartoffie possono aspettare. Mettila accanto al registro per ora.' La replica cordiale", (None, "Right you are"), "conferma subito, e il nome non numerabile", (None, "Paperwork"), "raccoglie moduli e pratiche d'ufficio."]),
    (9, None, ["'Ho sistemato la valigia blu proprio accanto al tavolo di Caleb sotto l'albero.' Premettendo l'avverbio di precisione in", (None, "right beside"), "si rafforza la vicinanza: esattamente a fianco."]),
    (10, None, ["'E la teiera è bollente! Tutti indietro di un passo dalla finestra!' Con un soggetto indefinito collettivo, l'imperativo di gruppo usa", (None, "step back"), "fate un passo indietro."]),
    (11, None, ["'Ascoltate... l'orologio della chiesa in fondo alla via sta cominciando a battere le dodici!' La posizione lungo la strada è resa da", (None, "down the street"), "mentre", (None, "chime twelve"), "indica il rintoccare melodioso delle dodici."]),
]
CALLOUT_TRANS = {
    "How does my tie look": "come sta la mia cravatta",
    "in sight": "in vista",
    "Sharp and spotless": "elegante e immacolata",
    "family reunion": "ricongiungimento familiare",
    "Says the man": "lo dice l'uomo",
    "peeking through": "che sbircia attraverso",
    "by the bell": "accanto al campanello",
    "sign for it": "firmare per ritirarla",
    "until next summer": "fino alla prossima estate",
    "five minutes to noon": "cinque minuti a mezzogiorno",
    "Right you are": "hai proprio ragione",
    "Paperwork": "scartoffie, pratiche burocratiche",
    "right beside": "proprio accanto a",
    "step back": "fate un passo indietro",
    "down the street": "in fondo alla via",
    "chime twelve": "battere le dodici",
}
