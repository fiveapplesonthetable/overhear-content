# Authoring module for linden-courtyard-it-s01e01-scene-01.
ID = "linden-courtyard-it-s01e01-scene-01"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = "Lift the Handle  (Solleva la maniglia)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"hannah": "Hannah", "graham": "Graham"}
INTRO = "Hannah arriva in anticipo nella sua prima mattina alla Locanda del Cortile del Tiglio, a Portland. Dietro il bancone dell'ingresso, Graham, lo storico tuttofare della casa, si versa già una tazza di tè bollente. Ascolta prima tutta la scena in inglese senza preoccuparti di capire ogni singola parola."
OPENER = "Ora riascoltiamo il dialogo con calma, frase per frase."
TRANSITION = "Ascoltiamo di nuovo tutta la scena a velocità naturale."
OUTRO = "Hannah è entrata, le otto chiavi d'ottone pendono dalla bacheca e la sua prima giornata è appena cominciata. Non importa se qualche parola ti è sfuggita: tornerà spesso lungo tutta la settimana. Alla prossima."
CLOSING = ("hannah", "See you soon!")
STORY = [
    ("hannah", "Good morning! Excuse me, is the door locked?", "Buongiorno! Mi scusi, la porta è chiusa a chiave?"),
    ("graham", "Good morning. No, lift the handle first, then push.", "Buongiorno. No, solleva prima la maniglia, poi spingi."),
    ("hannah", "Oh, it opens! Thank you. I am Hannah, the new receptionist.", "Oh, si apre! Grazie. Sono Hannah, la nuova addetta alla ricezione."),
    ("graham", "I am Graham. You are ten minutes early.", "Sono Graham. Sei in anticipo di dieci minuti."),
    ("hannah", "I always walk fast on my first day. Where is the computer?", "Cammino sempre veloce nel mio primo giorno. Dov'è il computer?"),
    ("graham", "In the drawer. Here we use this big paper book and a pencil.", "Nel cassetto. Qui usiamo questo grande registro di carta e una matita."),
    ("hannah", "A paper book? Really?", "Un registro di carta? Davvero?"),
    ("graham", "Paper never loses the room list when it rains.", "La carta non perde mai la lista delle camere quando piove."),
    ("hannah", "Fair enough! And these are the keys?", "Giusto! E queste sono le chiavi?"),
    ("graham", "Yes, eight rooms, eight brass keys. Room four is arriving today.", "Sì, otto camere, otto chiavi d'ottone. La camera quattro arriva oggi."),
    ("hannah", "Great. Tell me everything I need to know.", "Ottimo. Dimmi tutto quello che devo sapere."),
    ("graham", "Rule one: drink hot tea first, then answer the bell.", "Regola numero uno: prima bevi tè caldo, poi rispondi al campanello."),
]
WALK = [
    (0, None, ["'Buongiorno! Mi scusi, la porta è chiusa a chiave?' Per salutare al mattino usi", (None, "Good morning"), "e per fare una domanda sposti il verbo", (None, "is"), "prima del soggetto."]),
    (1, None, ["'Buongiorno. No, solleva prima la maniglia, poi spingi.' Dare istruzioni pratiche in inglese è semplicissimo: basta il verbo nudo come", (None, "lift"), "oppure", (None, "push"), "senza alcun pronome davanti."]),
    (2, None, ["'Oh, si apre! Grazie. Sono Hannah, la nuova addetta alla ricezione.' Nota il piccolo soggetto neutro in", (None, "it opens"), "perché l'inglese, a differenza dell'italiano, non lascia mai il verbo senza soggetto esplicito."]),
    (3, None, ["'Sono Graham. Sei in anticipo di dieci minuti.' Mentre noi diciamo essere in anticipo di, l'inglese unisce direttamente la misura di tempo all'aggettivo finale in", (None, "You are ten minutes early"), "con struttura linearissima."]),
    (4, None, ["'Cammino sempre veloce nel mio primo giorno. Dov'è il computer?' Davanti a un giorno specifico del calendario compare la preposizione di contatto in", (None, "on my first day"), "molto comune negli orari di lavoro."]),
    (5, None, ["'Nel cassetto. Qui usiamo questo grande registro di carta e una matita.' Osserva la sequenza compatta di", (None, "big paper book"), "dove dimensione e materiale precedono il nome senza alcuna preposizione."]),
    (6, None, ["'Un registro di carta? Davvero?' Una sola parola con intonazione ascendente,", (None, "Really"), "basta per esprimere sorpresa proprio come il nostro davvero."]),
    (7, None, ["'La carta non perde mai la lista delle camere quando piove.' Anche coi verbi atmosferici serve obbligatoriamente il pronome neutro, come senti in", (None, "when it rains"), "alla fine della frase."]),
    (8, None, ["'Giusto! E queste sono le chiavi?' Quando accetti una spiegazione sensata, la formula colloquiale", (None, "Fair enough"), "rende alla perfezione il nostro ci sta o mi sembra giusto."]),
    (9, None, ["'Sì, otto camere, otto chiavi d'ottone. La camera quattro arriva oggi.' La forma progressiva", (None, "is arriving today"), "indica un arrivo già fissato per la giornata odierna."]),
    (10, None, ["'Ottimo. Dimmi tutto quello che devo sapere.' Dopo il pronome", (None, "everything"), "l'inglese salta il pronome relativo e attacca subito", (None, "I need to know"), "con grande fluidità."]),
    (11, None, ["'Regola numero uno: prima bevi tè caldo, poi rispondi al campanello.' Proprio come in italiano, il verbo rispondere vale sia per il telefono sia in", (None, "answer the bell"), "quando suona il campanello del bancone."]),
]
CALLOUT_TRANS = {
    "Good morning": "buongiorno",
    "is": "è",
    "lift": "solleva",
    "push": "spingi",
    "it opens": "si apre",
    "You are ten minutes early": "sei in anticipo di dieci minuti",
    "on my first day": "nel mio primo giorno",
    "big paper book": "grande registro di carta",
    "Really": "davvero",
    "when it rains": "quando piove",
    "Fair enough": "giusto, ci sta",
    "is arriving today": "arriva oggi",
    "everything": "tutto",
    "I need to know": "che devo sapere",
    "answer the bell": "rispondi al campanello",
}
