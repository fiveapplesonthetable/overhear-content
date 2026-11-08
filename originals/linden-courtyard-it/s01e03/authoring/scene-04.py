# Authoring module for linden-courtyard-it-s01e03-scene-04.
ID = "linden-courtyard-it-s01e03-scene-04"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = "In from the Rain  (Al riparo dalla pioggia)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"hannah": "Hannah", "caleb": "Caleb", "tessa": "Tessa"}
INTRO = "Giù all'ingresso, Caleb, un viaggiatore dai modi pacati sui trent'anni, entra scuotendo l'ombrello bagnato. Hannah lo accoglie al bancone mentre Tessa gli porge subito un asciugamano asciutto. Ascoltiamo prima la scena."
OPENER = "Esaminiamo con calma ogni battuta di questo incontro."
TRANSITION = "Ascoltiamo ancora una volta tutta la scena di fila."
OUTRO = "La sincerità, un asciugamano asciutto e una tazza di zuppa fumante hanno mantenuto serena l'accoglienza. Nella prossima scena Caleb sale le scale per giudicare la soffitta con i propri occhi. Alla prossima."
CLOSING = ("caleb", "See you soon!")
STORY = [
    ("hannah", "Good evening! Come inside out of the rain, sir.", "Buonasera! Entri pure al riparo dalla pioggia, signore."),
    ("caleb", "Good evening. Sorry for dripping water on your clean floor.", "Buonasera. Mi scusi se sgocciolo acqua sul vostro pavimento pulito."),
    ("hannah", "Do not worry at all! You must be Caleb.", "Non si preoccupi affatto! Lei dev'essere Caleb."),
    ("caleb", "Yes, Caleb. I booked room seven by phone yesterday.", "Sì, Caleb. Ho prenotato ieri per telefono la camera sette."),
    ("tessa", "Here is a dry towel for your coat and a cup of hot soup, sir.", "Ecco un asciugamano asciutto per il cappotto e una tazza di zuppa calda, signore."),
    ("caleb", "Hot soup? After that cold walk in the rain, that sounds wonderful.", "Zuppa calda? Dopo quella fredda camminata sotto la pioggia, suona meraviglioso."),
    ("hannah", "Sir, before we go upstairs, I owe you an honest apology.", "Signore, prima di salire, le devo delle scuse sincere."),
    ("caleb", "Oh? Is there a problem with my booking?", "Oh? C'è un problema con la mia prenotazione?"),
    ("hannah", "We accidentally booked two guests into room seven tonight.", "Per sbaglio abbiamo registrato due ospiti nella camera sette per stanotte."),
    ("caleb", "Ah... in this rain? Every hotel near the station looked full.", "Ah... con questa pioggia? Ogni albergo vicino alla stazione sembrava al completo."),
    ("hannah", "Please do not worry! We prepared our quiet third floor attic study just for you.", "La prego, non si preoccupi! Abbiamo preparato il nostro silenzioso studio in soffitta al terzo piano apposta per lei."),
    ("caleb", "An attic study? May I see it first?", "Uno studio in soffitta? Posso vederlo prima?"),
]
WALK = [
    (0, None, ["'Buonasera! Entri pure al riparo dalla pioggia, signore.' Accostare l'entrata all'uscita dalle intemperie in", (None, "Come inside out of the rain"), "rende con vivacità l'invito a mettersi all'asciutto."]),
    (1, None, ["'Buonasera. Mi scusi se sgocciolo acqua sul vostro pavimento pulito.' Dopo la formula di scusa seguita da preposizione, il verbo prende la forma progressiva in", (None, "Sorry for dripping"), "scusi se sgocciolo."]),
    (2, None, ["'Non si preoccupi affatto! Lei dev'essere Caleb.' Chiudere l'invito a non preoccuparsi con", (None, "Do not worry at all"), "cancella ogni imbarazzo fin dal primo secondo."]),
    (3, None, ["'Sì, Caleb. Ho prenotato ieri per telefono la camera sette.' Per indicare il mezzo di comunicazione non si mette articolo:", (None, "by phone"), "per telefono."]),
    (4, None, ["'Ecco un asciugamano asciutto per il cappotto e una tazza di zuppa calda, signore.' In inglese la zuppa calda servita in tazza da bere si offre semplicemente come", (None, "a cup of hot soup"), "una tazza di zuppa."]),
    (5, None, ["'Zuppa calda? Dopo quella fredda camminata sotto la pioggia, suona meraviglioso.' Quando reagisci con entusiasmo a una proposta appena ascoltata dici", (None, "that sounds wonderful"), "sembra un'ottima idea."]),
    (6, None, ["'Signore, prima di salire, le devo delle scuse sincere.' Mentre noi chiediamo scusa al plurale, l'inglese usa il singolare preceduto dal verbo dovere in", (None, "I owe you an honest apology"), "le devo delle scuse sincere."]),
    (7, None, ["'Oh? C'è un problema con la mia prenotazione?' La struttura", (None, "a problem with"), "lega sempre la parola problema alla preposizione con."]),
    (8, None, ["'Per sbaglio abbiamo registrato due ospiti nella camera sette per stanotte.' L'avverbio", (None, "accidentally"), "prima del verbo chiarisce subito che si è trattato di una svista involontaria."]),
    (9, None, ["'Ah... con questa pioggia? Ogni albergo vicino alla stazione sembrava al completo.' Dove in italiano diciamo con questa pioggia, l'inglese ci vede immersi dentro gli elementi atmosferici con", (None, "in this rain"), "sotto questa pioggia."]),
    (10, None, ["'La prego, non si preoccupi! Abbiamo preparato il nostro silenzioso studio in soffitta al terzo piano apposta per lei.' La chiusa", (None, "just for you"), "significa appositamente per lei, con riguardo speciale."]),
    (11, None, ["'Uno studio in soffitta? Posso vederlo prima?' Per chiedere il permesso con grande educazione il modale più raffinato è", (None, "May I see it"), "posso vederlo."]),
]
CALLOUT_TRANS = {
    "Come inside out of the rain": "entri al riparo dalla pioggia",
    "Sorry for dripping": "mi scusi se sgocciolo",
    "Do not worry at all": "non si preoccupi affatto",
    "by phone": "per telefono",
    "a cup of hot soup": "una tazza di zuppa calda",
    "that sounds wonderful": "suona meraviglioso",
    "I owe you an honest apology": "le devo delle scuse sincere",
    "a problem with": "un problema con",
    "accidentally": "per sbaglio, accidentalmente",
    "in this rain": "con questa pioggia",
    "just for you": "apposta per lei",
    "May I see it": "posso vederlo",
}
