# Authoring module for linden-courtyard-it-s01e03-scene-08.
ID = "linden-courtyard-it-s01e03-scene-08"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 3
SCENE = 8
TITLE = "Ice-Cold Pipes  (Tubi gelati)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"graham": "Graham", "hannah": "Hannah", "arthur": "Arthur"}
INTRO = "Giù all'ingresso, Hannah e Arthur aspettano con il fiato sospeso davanti alla porta della cantina finché Graham non risale pulendosi le mani con uno straccio e scuotendo la testa. Ascolta prima tutta la scena."
OPENER = "Ripercorriamo riga per riga questo verdetto dalla cantina."
TRANSITION = "Ascoltiamo un'altra volta tutta la scena a ritmo naturale."
OUTRO = "Un presunto ispettore turistico al terzo piano, una valvola ceduta in cantina e una corsa alle sette del mattino oltre il ponte. Si chiude così il terzo episodio; ci ritroviamo nel quarto!"
CLOSING = ("graham", "See you tomorrow!")
STORY = [
    ("arthur", "Tell me it was just a tiny air bubble, Graham! Please!", "Dimmi che era solo una minuscola bolla d'aria, Graham! Ti prego!"),
    ("graham", "Bad news. The brass pressure valve on the old boiler just gave up.", "Brutte notizie. La valvola a pressione d'ottone sulla vecchia caldaia ha appena ceduto."),
    ("hannah", "Does that mean no radiators tonight, or no hot water too?", "Questo significa niente termosifoni stanotte, o anche niente acqua calda?"),
    ("graham", "The rooms will stay warm until morning, Hannah, because the brick walls hold heat.", "Le camere resteranno calde fino al mattino, Hannah, perché i muri di mattoni trattengono il calore."),
    ("arthur", "Thank heavens! And the morning showers?", "Sia lodato il cielo! E le docce del mattino?"),
    ("graham", "By tomorrow morning, the shower water will be ice cold.", "Entro domani mattina, l'acqua della doccia sarà gelata."),
    ("arthur", "Ice cold showers?! With the Portland Travel Guide inspector on the third floor?!", "Docce gelate?! Con l'ispettore della Guida Turistica di Portland al terzo piano?!"),
    ("hannah", "Do you have a spare brass valve in your toolbox?", "Hai una valvola d'ottone di ricambio nella cassetta degli attrezzi?"),
    ("graham", "Used my last one in winter. Only the old hardware shop past the bridge sells this size.", "Ho usato l'ultima quest'inverno. Solo la vecchia ferramenta oltre il ponte vende questa misura."),
    ("hannah", "What time does that hardware shop open?", "A che ora apre quella ferramenta?"),
    ("graham", "Seven sharp, half an hour before breakfast.", "Alle sette in punto, mezz'ora prima della colazione."),
    ("hannah", "Set your alarm, Graham. Tomorrow morning we beat the cold showers!", "Punta la sveglia, Graham. Domani mattina battiamo sul tempo le docce fredde!"),
]
WALK = [
    (0, None, ["'Dimmi che era solo una minuscola bolla d'aria, Graham! Ti prego!' L'aggettivo", (None, "tiny"), "indica qualcosa di piccolissimo, ancora più minuto di piccolo."]),
    (1, None, ["'Brutte notizie. La valvola a pressione d'ottone sulla vecchia caldaia ha appena ceduto.' Attenzione a", (None, "Bad news"), "che resta non numerabile singolare, mentre il verbo frasale", (None, "gave up"), "dice con umorismo che il pezzo si è arreso."]),
    (2, None, ["'Questo significa niente termosifoni stanotte, o anche niente acqua calda?' Per verificare la conseguenza pratica di ciò che hai appena sentito chiedi", (None, "Does that mean"), "significa forse che."]),
    (3, None, ["'Le camere resteranno calde fino al mattino, Hannah, perché i muri di mattoni trattengono il calore.' L'abbinamento", (None, "stay warm"), "esprime il mantenersi caldo nel tempo, grazie a", (None, "hold heat"), "trattenere il calore."]),
    (4, None, ["'Sia lodato il cielo! E le docce del mattino?' Un'esclamazione vivace di grande sollievo è", (None, "Thank heavens"), "grazie al cielo."]),
    (5, None, ["'Entro domani mattina, l'acqua della doccia sarà gelata.' Mettere il sostantivo ghiaccio davanti all'aggettivo freddo crea l'intensificatore", (None, "ice cold"), "fredda come il ghiaccio."]),
    (6, None, ["'Docce gelate?! Con l'ispettore della Guida Turistica di Portland al terzo piano?!' Nota come l'intero titolo della guida preceda la professione finale in", (None, "Portland Travel Guide inspector"), "senza alcuna preposizione."]),
    (7, None, ["'Hai una valvola d'ottone di ricambio nella cassetta degli attrezzi?' Qualsiasi pezzo di scorta o di riserva si indica premettendo l'aggettivo in", (None, "spare brass valve"), "valvola di ricambio."]),
    (8, None, ["'Ho usato l'ultima quest'inverno. Solo la vecchia ferramenta oltre il ponte vende questa misura.' Il negozio di ferramenta si chiama", (None, "hardware shop"), "e la preposizione", (None, "past the bridge"), "significa subito oltre il ponte."]),
    (9, None, ["'A che ora apre quella ferramenta?' Per chiedere a che ora inizia o apre qualcosa, l'inglese non usa preposizioni iniziali ma apre direttamente con", (None, "What time"), "a che ora."]),
    (10, None, ["'Alle sette in punto, mezz'ora prima della colazione.' Aggiungere", (None, "sharp"), "dopo il numero dell'ora equivale a in punto, e osserva l'articolo vocalico in", (None, "half an hour"), "perché l'acca di ora è muta."]),
    (11, None, ["'Punta la sveglia, Graham. Domani mattina battiamo sul tempo le docce fredde!' Puntare o impostare la sveglia per il mattino seguente si dice sempre", (None, "Set your alarm"), "con il verbo regolare impostare."]),
]
CALLOUT_TRANS = {
    "tiny": "minuscola, piccolissima",
    "Bad news": "brutte notizie",
    "gave up": "ha ceduto, si è arresa",
    "Does that mean": "questo significa",
    "stay warm": "restare calde",
    "hold heat": "trattengono il calore",
    "Thank heavens": "grazie al cielo",
    "ice cold": "gelata, fredda come il ghiaccio",
    "Portland Travel Guide inspector": "ispettore della Guida Turistica di Portland",
    "spare brass valve": "valvola d'ottone di ricambio",
    "hardware shop": "negozio di ferramenta",
    "past the bridge": "oltre il ponte",
    "What time": "a che ora",
    "sharp": "in punto, spaccate",
    "half an hour": "mezz'ora",
    "Set your alarm": "punta la sveglia",
}
