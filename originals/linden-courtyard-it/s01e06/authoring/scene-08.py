# Authoring module for linden-courtyard-it-s01e06-scene-08.
ID = "linden-courtyard-it-s01e06-scene-08"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 6
SCENE = 8
TITLE = "Room Nine  (La camera nove)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"graham": "Graham", "hannah": "Hannah", "arthur": "Arthur"}
INTRO = "A tarda sera di venerdì, quando il cortile della Locanda del Cortile del Tiglio si fa silenzioso, Hannah e Arthur chiudono il bancone mentre Graham risale dalla cantina sul retro portando sedie in più e una cassetta di legno impolverata. Ascoltiamo prima."
OPENER = "Seguiamo ora con calma ogni battuta di quest'ultima scena."
TRANSITION = "Riascoltiamo adesso tutta la scena per intero."
OUTRO = "Una nona chiave d'ottone, un bauletto di cedro inciso col numero nove e una planimetria che svela una porta nascosta su questo piano! Hai completato la prima stagione della Locanda del Cortile del Tiglio. Ci rivediamo nella seconda stagione!"
CLOSING = ("graham", "Until tomorrow!")
STORY = [
    ("hannah", "Did you find the three folding chairs behind the boiler room, Graham?", "Hai trovato le tre sedie pieghevoli dietro il locale caldaia, Graham?"),
    ("graham", "Found the chairs, and behind an old brick wall, I found this.", "Ho trovato le sedie e, dietro un vecchio muro di mattoni, ho trovato questo."),
    ("arthur", "A small cedar chest? I have never seen that box in fifteen years!", "Un piccolo bauletto di cedro? Non ho mai visto quella scatola in quindici anni!"),
    ("hannah", "Brush the dust off the brass plate on top... wait, read that number!", "Spazzola via la polvere dalla targhetta d'ottone sopra... aspetta, leggi quel numero!"),
    ("arthur", "Let me pull my glasses down from my forehead... 'Room Nine'?!", "Fatemi abbassare gli occhiali dalla fronte... «Camera Nove»?!"),
    ("hannah", "Graham, look at the wooden key board behind us: one, two, three, four, five, six, seven, eight!", "Graham, guarda la bacheca di legno delle chiavi dietro di noi: uno, due, tre, quattro, cinque, sei, sette, otto!"),
    ("arthur", "This guesthouse has only ever had eight rooms! Where on earth is Room Nine?!", "Questa locanda ha sempre avuto soltanto otto camere! Dove mai può essere la Camera Nove?!"),
    ("graham", "Listen when I tilt the box. Something metal just slid inside.", "Ascoltate quando inclino la scatola. Qualcosa di metallo è appena scivolato dentro."),
    ("hannah", "There is a tiny keyhole on the front latch, and look taped underneath: an old brass key!", "C'è un minuscolo buco della serratura sul gancio davanti, e guardate incollata sotto col nastro: una vecchia chiave d'ottone!"),
    ("arthur", "A ninth brass key?! Do we open it tonight or wait until morning?!", "Una nona chiave d'ottone?! La apriamo stasera o aspettiamo fino a domattina?!"),
    ("graham", "Look at the folded blueprint sticking out of the hinge. There is a hidden door drawn on this floor!", "Guardate la planimetria piegata che spunta dalla cerniera. C'è una porta segreta disegnata su questo piano!"),
    ("hannah", "Grab the flashlight, both of you. My second week starts right now!", "Prendete la torcia elettrica, tutti e due. La mia seconda settimana comincia proprio adesso!"),
]
WALK = [
    (0, None, ["'Hai trovato le tre sedie pieghevoli dietro il locale caldaia, Graham?' Le sedie richiudibili di scorta si chiamano", (None, "folding chairs"), "col participio presente in funzione di aggettivo."]),
    (1, None, ["'Ho trovato le sedie e, dietro un vecchio muro di mattoni, ho trovato questo.' Il nome del materiale resta invariato al singolare davanti al sostantivo principale in", (None, "brick wall"), "muro di mattoni."]),
    (2, None, ["'Un piccolo bauletto di cedro? Non ho mai visto quella scatola in quindici anni!' Il legno profumato precede il contenitore in", (None, "cedar chest"), "mentre l'esperienza lungo quindici anni vuole", (None, "have never seen"), "non ho mai visto."]),
    (3, None, ["'Spazzola via la polvere dalla targhetta d'ottone sopra... aspetta, leggi quel numero!' Togliere uno strato superficiale passando la mano si esprime con", (None, "Brush the dust off"), "spazzola via la polvere da."]),
    (4, None, ["'Fatemi abbassare gli occhiali dalla fronte... «Camera Nove»?!' Il verbo tirare unito alla direzione verso il basso dipinge il gesto tipico di Arthur in", (None, "pull my glasses down"), "abbassarmi gli occhiali."]),
    (5, None, ["'Graham, guarda la bacheca di legno delle chiavi dietro di noi: uno, due, tre, quattro, cinque, sei, sette, otto!' La posizione alle spalle di chi parla usa il pronome oggetto diretto dopo la preposizione in", (None, "behind us"), "dietro di noi."]),
    (6, None, ["'Questa locanda ha sempre avuto soltanto otto camere! Dove mai può essere la Camera Nove?!' Per rafforzare l'unicità in tutta la storia della casa compare", (None, "has only ever had"), "e lo sbalordimento esplode in", (None, "Where on earth"), "dove mai al mondo."]),
    (7, None, ["'Ascoltate quando inclino la scatola. Qualcosa di metallo è appena scivolato dentro.' Inclinare leggermente un oggetto è", (None, "tilt the box"), "e dopo i pronomi indefiniti il materiale si accosta senza preposizione in", (None, "Something metal"), "qualcosa di metallico."]),
    (8, None, ["'C'è un minuscolo buco della serratura sul gancio davanti, e guardate incollata sotto col nastro: una vecchia chiave d'ottone!' Chiave e foro si fondono in un'unica parola composta in", (None, "tiny keyhole"), "minuscolo buco della serratura."]),
    (9, None, ["'Una nona chiave d'ottone?! La apriamo stasera o aspettiamo fino a domattina?!' L'ordinale trasforma nove in", (None, "ninth brass key"), "perdendo la vocale muta intermedia, seguito dal dilemma", (None, "wait until morning"), "aspettiamo fino a domattina."]),
    (10, None, ["'Guardate la planimetria piegata che spunta dalla cerniera. C'è una porta segreta disegnata su questo piano!' Qualcosa che sporge da una fessura sta", (None, "sticking out of"), "rivelando una misteriosa", (None, "hidden door"), "porta nascosta."]),
    (11, None, ["'Prendete la torcia elettrica, tutti e due. La mia seconda settimana comincia proprio adesso!' Per afferrare al volo uno strumento utile si usa il vivace", (None, "Grab the flashlight"), "chiuso dal presente imminente", (None, "starts right now"), "inizia in questo istante."]),
]
CALLOUT_TRANS = {
    "folding chairs": "sedie pieghevoli",
    "brick wall": "muro di mattoni",
    "cedar chest": "bauletto di cedro",
    "have never seen": "non ho mai visto",
    "Brush the dust off": "spazzola via la polvere da",
    "pull my glasses down": "abbassare i miei occhiali",
    "behind us": "dietro di noi",
    "has only ever had": "ha sempre avuto soltanto",
    "Where on earth": "dove mai",
    "tilt the box": "inclino la scatola",
    "Something metal": "qualcosa di metallo",
    "tiny keyhole": "minuscolo buco della serratura",
    "ninth brass key": "nona chiave d'ottone",
    "wait until morning": "aspettiamo fino a domattina",
    "sticking out of": "che spunta da",
    "hidden door": "porta nascosta, segreta",
    "Grab the flashlight": "prendete la torcia elettrica",
    "starts right now": "comincia proprio adesso",
}
