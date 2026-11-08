# Authoring module for linden-courtyard-it-s01e04-scene-07.
ID = "linden-courtyard-it-s01e04-scene-07"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 4
SCENE = 7
TITLE = "Sunlight on the Tag  (Sole sull'etichetta)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"hannah": "Hannah", "evelyn": "Evelyn", "graham": "Graham"}
INTRO = "A mezzogiorno, Graham apre il ripostiglio del corridoio per arieggiarlo dopo il temporale e posa la valigia blu non reclamata vicino al bancone, proprio mentre arriva la signorina Evelyn. Ascolta prima la scena."
OPENER = "Seguiamo da vicino questa scoperta sotto la luce del sole."
TRANSITION = "Riascoltiamo ora tutta la conversazione senza interruzioni."
OUTRO = "La luce del giorno su una vecchia targhetta da viaggio ha appena riaperto venticinque anni di ricordi: due fratelli in via Linden e il trenino di legno del nonno. Resta un'ultima scena nell'episodio quattro."
CLOSING = ("evelyn", "Bye for now!")
STORY = [
    ("graham", "Let me set this blue suitcase here for five minutes while I sweep the closet.", "Lasciami appoggiare qui questa valigia blu per cinque minuti mentre spazzo il ripostiglio."),
    ("hannah", "Careful with it, Graham. Friday at noon is tomorrow!", "Con cautela, Graham. Venerdì a mezzogiorno è domani!"),
    ("evelyn", "Oh, is that the twin suitcase from Monday's train?", "Oh, quella è la valigia gemella del treno di lunedì?"),
    ("hannah", "Yes, ma'am, still waiting for its owner.", "Sì, signora, sta ancora aspettando il suo proprietario."),
    ("evelyn", "May I look at the paper tag again here in the bright sunlight?", "Posso guardare di nuovo l'etichetta di carta qui alla luce viva del sole?"),
    ("graham", "Go right ahead, ma'am. Monday afternoon the lobby was dark.", "Faccia pure con comodo, signora. Lunedì pomeriggio l'atrio era buio."),
    ("evelyn", "Wait a moment... Number twelve, Linden Street, and two childhood initials written in the corner!", "Aspetti un momento... Numero dodici di via Linden, e due iniziali d'infanzia scritte nell'angolo!"),
    ("hannah", "Miss Evelyn, you look amazed! Do you know Number twelve, Linden Street?", "Signorina Evelyn, sembra stupita! Conosce il numero dodici di via Linden?"),
    ("evelyn", "Know it? Every Friday for six years I climbed those wooden stairs to teach piano!", "Se lo conosco? Ogni venerdì per sei anni ho salito quelle scale di legno per insegnare pianoforte!"),
    ("graham", "Twenty-five years ago? In that same house?", "Venticinque anni fa? In quella stessa casa?"),
    ("evelyn", "A carpenter lived there with his two grandsons. The older boy played piano, and the little one loved trains!", "Lì viveva un falegname con i suoi due nipoti maschi. Il ragazzo più grande suonava il pianoforte, e il piccolino adorava i treni!"),
    ("hannah", "A carpenter... and a little wooden toy train inside the bag!", "Un falegname... e un piccolo trenino giocattolo di legno dentro la borsa!"),
]
WALK = [
    (0, None, ["'Lasciami appoggiare qui questa valigia blu per cinque minuti mentre spazzo il ripostiglio.' Appoggiare delicatamente un oggetto si rende con", (None, "set this blue suitcase here"), "mentre", (None, "sweep"), "significa spazzare con la scopa."]),
    (1, None, ["'Con cautela, Graham. Venerdì a mezzogiorno è domani!' Per raccomandare attenzione nel maneggiare qualcosa basta", (None, "Careful with it"), "e mezzogiorno esatto si dice", (None, "at noon"), "a mezzogiorno."]),
    (2, None, ["'Oh, quella è la valigia gemella del treno di lunedì?' Due oggetti identici si definiscono con", (None, "twin suitcase"), "e anche i giorni della settimana prendono il genitivo sassone in", (None, "Monday's train"), "il treno di lunedì."]),
    (3, None, ["'Sì, signora, sta ancora aspettando il suo proprietario.' Poiché la valigia è un oggetto inanimato, il possessivo neutro senza apostrofo compare in", (None, "its owner"), "il suo proprietario."]),
    (4, None, ["'Posso guardare di nuovo l'etichetta di carta qui alla luce viva del sole?' Per chiedere un permesso con molta eleganza si apre con", (None, "May I look at"), "e sotto il sole si costruisce con", (None, "in the bright sunlight"), "nella luce intensa del sole."]),
    (5, None, ["'Faccia pure con comodo, signora. Lunedì pomeriggio l'atrio era buio.' Per dare il via libera con calore e cortesia la risposta ideale è", (None, "Go right ahead"), "faccia pure."]),
    (6, None, ["'Aspetti un momento... Numero dodici di via Linden, e due iniziali d'infanzia scritte nell'angolo!' Nota il composto", (None, "childhood initials"), "iniziali d'infanzia, seguite dal participio", (None, "written"), "incise nel legno o nel cuoio."]),
    (7, None, ["'Signorina Evelyn, sembra stupita! Conosce il numero dodici di via Linden?' Con i verbi d'aspetto visivo l'aggettivo segue direttamente il verbo in", (None, "you look amazed"), "lei ha l'aria meravigliata."]),
    (8, None, ["'Se lo conosco? Ogni venerdì per sei anni ho salito quelle scale di legno per insegnare pianoforte!' Nota la durata continuativa espressa da", (None, "for six years"), "e", (None, "teach piano"), "senza articolo davanti allo strumento."]),
    (9, None, ["'Venticinque anni fa? In quella stessa casa?' L'avverbio che corrisponde al nostro fa si colloca sempre in fondo all'espressione temporale come in", (None, "Twenty-five years ago"), "venticinque anni fa."]),
    (10, None, ["'Lì viveva un falegname con i suoi due nipoti maschi. Il ragazzo più grande suonava il pianoforte, e il piccolino adorava i treni!' Attenzione a", (None, "carpenter"), "che è il falegname, e a", (None, "grandsons"), "che distingue i nipoti di nonno dai figli di fratelli."]),
    (11, None, ["'Un falegname... e un piccolo trenino giocattolo di legno dentro la borsa!' Guarda l'ordine impeccabile in", (None, "little wooden toy train"), "dimensione, materiale e funzione prima del nome principale."]),
]
CALLOUT_TRANS = {
    "set this blue suitcase here": "appoggiare qui questa valigia blu",
    "sweep": "spazzare",
    "Careful with it": "attento con quella",
    "at noon": "a mezzogiorno",
    "twin suitcase": "valigia gemella",
    "Monday's train": "il treno di lunedì",
    "its owner": "il suo proprietario",
    "May I look at": "posso guardare",
    "in the bright sunlight": "alla luce viva del sole",
    "Go right ahead": "faccia pure",
    "childhood initials": "iniziali d'infanzia",
    "written": "incise, intagliate",
    "you look amazed": "sembra stupita",
    "for six years": "per sei anni",
    "teach piano": "insegnare pianoforte",
    "Twenty-five years ago": "venticinque anni fa",
    "carpenter": "falegname",
    "grandsons": "nipoti di nonno",
    "little wooden toy train": "piccolo trenino giocattolo di legno",
}
