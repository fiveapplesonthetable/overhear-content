# Authoring module for linden-courtyard-it-s01e05-scene-05.
ID = "linden-courtyard-it-s01e05-scene-05"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 5
SCENE = 5
TITLE = "Simple Words First  (Prima parole semplici)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"caleb": "Caleb", "hannah": "Hannah"}
INTRO = "Venti minuti prima di mezzogiorno, Caleb cammina avanti e indietro sulle pietre del cortile della Locanda del Cortile del Tiglio stringendo un foglio stropicciato, mentre Hannah gli si avvicina con un bicchiere d'acqua. Ascolta prima tutta la scena."
OPENER = "Ripassiamo adesso la conversazione con calma, battuta per battuta."
TRANSITION = "Riascoltiamo ora tutta la scena di fila."
OUTRO = "Niente discorsi in diciannove punti: solo grazie per essere venuto, mi sei mancato, e siediti per il tè e la torta al limone. Mancano dieci minuti alle dodici. Alla prossima."
CLOSING = ("caleb", "Take care!")
STORY = [
    ("hannah", "Here, drink a sip of cool water, Caleb. What is on that paper?", "Tieni, bevi un sorso d'acqua fresca, Caleb. Che cosa c'è su quel foglio?"),
    ("caleb", "A five minute speech explaining nineteen reasons why we were both wrong in April.", "Un discorso di cinque minuti che spiega diciannove motivi per cui avevamo torto entrambi ad aprile."),
    ("hannah", "Nineteen reasons?! Are you welcoming your brother or reading a train schedule?", "Diciannove motivi?! Stai accogliendo tuo fratello o stai leggendo un orario ferroviario?"),
    ("caleb", "When I get nervous, my sentences grow very long and formal!", "Quando mi agito, le mie frasi diventano lunghissime e formali!"),
    ("hannah", "Fold that paper and put it in your pocket right now.", "Piega quel foglio e mettilo subito in tasca."),
    ("caleb", "Without my notes, what do I say when he walks through that gate?", "Senza i miei appunti, che cosa dico quando varca quel cancello?"),
    ("hannah", "Start with three short sentences. First: 'Hello, Owen, thank you for coming.'", "Comincia con tre frasi brevi. Prima: «Ciao, Owen, grazie per essere venuto.»"),
    ("caleb", "'Hello, Owen, thank you for coming.' Okay, I can remember that.", "«Ciao, Owen, grazie per essere venuto.» Va bene, questo posso ricordarmelo."),
    ("hannah", "Second: 'I missed you these three years.'", "Seconda: «Mi sei mancato in questi tre anni.»"),
    ("caleb", "'I missed you these three years.' Honest and clear. And third?", "«Mi sei mancato in questi tre anni.» Sincero e chiaro. E la terza?"),
    ("hannah", "'Sit down, there is hot tea and Friday lemon cake.'", "«Siediti, c'è tè caldo e la torta al limone del venerdì.»"),
    ("caleb", "Tea and lemon cake! Hannah, you should open a school for nervous brothers.", "Tè e torta al limone! Hannah, dovresti aprire una scuola per fratelli nervosi."),
]
WALK = [
    (0, None, ["'Tieni, bevi un sorso d'acqua fresca, Caleb. Che cosa c'è su quel foglio?' Per invitare a bere un piccolo goccio con calma si usa la misura", (None, "a sip of"), "un sorso di."]),
    (1, None, ["'Un discorso di cinque minuti che spiega diciannove motivi per cui avevamo torto entrambi ad aprile.' Davanti a un altro nome l'unità di durata resta singolare in", (None, "five minute speech"), "mentre", (None, "both wrong"), "unisce entrambi nella colpa."]),
    (2, None, ["'Diciannove motivi?! Stai accogliendo tuo fratello o stai leggendo un orario ferroviario?' I due sostantivi affiancati in", (None, "train schedule"), "indicano la tabella degli orari dei treni."]),
    (3, None, ["'Quando mi agito, le mie frasi diventano lunghissime e formali!' Due verbi diversi rendono l'idea di diventare:", (None, "get nervous"), "per uno stato emotivo rapido e", (None, "grow very long"), "per qualcosa che si allunga gradualmente."]),
    (4, None, ["'Piega quel foglio e mettilo subito in tasca.' L'imperativo concreto parte con", (None, "Fold that paper"), "e precisa il possessivo davanti alla tasca in", (None, "in your pocket"), "nella tua tasca."]),
    (5, None, ["'Senza i miei appunti, che cosa dico quando varca quel cancello?' Oltrepassare un ingresso dall'esterno verso l'interno si esprime con", (None, "walks through"), "cammina attraverso."]),
    (6, None, ["'Comincia con tre frasi brevi. Prima: «Ciao, Owen, grazie per essere venuto.»' Una delle formule d'accoglienza più calde e naturali della lingua è", (None, "thank you for coming"), "grazie di essere venuto."]),
    (7, None, ["'«Ciao, Owen, grazie per essere venuto.» Va bene, questo posso ricordarmelo.' Col modale della capacità seguito dal verbo base,", (None, "I can remember that"), "rassicura subito chi ascolta."]),
    (8, None, ["'Seconda: «Mi sei mancato in questi tre anni.»' Attenzione al soggetto capovolto rispetto all'italiano: in", (None, "I missed you"), "il soggetto è chi sente la mancanza, non la persona lontana."]),
    (9, None, ["'«Mi sei mancato in questi tre anni.» Sincero e chiaro. E la terza?' La coppia di aggettivi", (None, "Honest and clear"), "promuove una frase limpida senza giri di parole."]),
    (10, None, ["'«Siediti, c'è tè caldo e la torta al limone del venerdì.»' Per far accomodare un ospite al tavolo, il verbo si completa quasi sempre con la particella in", (None, "Sit down"), "siediti."]),
    (11, None, ["'Tè e torta al limone! Hannah, dovresti aprire una scuola per fratelli nervosi.' Un consiglio affettuoso o scherzoso ricorre al modale morbido in", (None, "you should open"), "dovresti aprire."]),
]
CALLOUT_TRANS = {
    "a sip of": "un sorso di",
    "five minute speech": "discorso di cinque minuti",
    "both wrong": "entrambi in torto",
    "train schedule": "orario ferroviario",
    "get nervous": "mi agito, divento nervoso",
    "grow very long": "diventano molto lunghe",
    "Fold that paper": "piega quel foglio",
    "in your pocket": "in tasca, nella tua tasca",
    "walks through": "varca, passa attraverso",
    "thank you for coming": "grazie per essere venuto",
    "I can remember that": "posso ricordarmelo",
    "I missed you": "mi sei mancato",
    "Honest and clear": "sincero e chiaro",
    "Sit down": "siediti",
    "you should open": "dovresti aprire",
}
