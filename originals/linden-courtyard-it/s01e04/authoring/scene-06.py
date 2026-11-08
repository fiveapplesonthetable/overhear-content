# Authoring module for linden-courtyard-it-s01e04-scene-06.
ID = "linden-courtyard-it-s01e04-scene-06"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 4
SCENE = 6
TITLE = "The Acoustic Architect  (L'architetto acustico)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"caleb": "Caleb", "hannah": "Hannah", "tessa": "Tessa"}
INTRO = "Fuori, all'ombra del grande tiglio del cortile, Caleb apre il suo taccuino di pelle marrone davanti a Hannah e Tessa mentre cantano gli uccellini del mattino. Ascoltiamo prima il dialogo."
OPENER = "Scopriamo frase per frase il vero mestiere di Caleb e il suo legame con il quartiere."
TRANSITION = "Riascoltiamo ora tutta la scena nel cortile."
OUTRO = "Caleb è un architetto acustico, e quell'accenno tranquillo a due vie di distanza e al venerdì ha appena fatto spalancare gli occhi a Hannah e Tessa. A tra poco."
CLOSING = ("tessa", "See you later!")
STORY = [
    ("caleb", "Look closely at this page. It measures decibels and quietness, not hotel stars!", "Guardate da vicino questa pagina. Misura i decibel e la quiete, non le stelle degli alberghi!"),
    ("hannah", "Decibels? So 'nine out of ten' was not a review of my front desk?", "Decibel? Quindi «nove su dieci» non era una recensione del mio bancone d'accoglienza?"),
    ("caleb", "Well, your front desk deserves ten! Honestly, though, I am an acoustic architect.", "Beh, il tuo bancone merita dieci! A dire il vero, però, sono un architetto acustico."),
    ("tessa", "An acoustic architect! Do you design concert halls?", "Un architetto acustico! Progetta sale da concerto?"),
    ("caleb", "Small libraries and courtyards, mostly. I measure how old stone walls block street noise.", "Piccole biblioteche e cortili, per lo più. Misuro come i vecchi muri di pietra bloccano il rumore della strada."),
    ("hannah", "That is why you listened for cars up in the attic last night!", "Ecco perché ieri sera tendeva l'orecchio alle auto lassù in soffitta!"),
    ("caleb", "Exactly. Outside on the avenue it is loud, yet inside this courtyard you hear leaves and birds.", "Esatto. Fuori sul viale c'è frastuono, eppure dentro questo cortile si sentono le foglie e gli uccelli."),
    ("tessa", "Wait until Arthur hears he panicked all night over decibels!", "Aspetta che Arthur scopra di essersi agitato tutta la notte per delle misure sonore!"),
    ("caleb", "Truthfully, I also chose this neighborhood for an old family reason.", "In tutta sincerità, ho scelto questo quartiere anche per un vecchio motivo di famiglia."),
    ("hannah", "Oh? Did your family live near here once?", "Oh? La sua famiglia viveva qui vicino un tempo?"),
    ("caleb", "Two streets away, when I was small. Friday is... an important day for me.", "A due vie di distanza, quando ero piccolo. Venerdì è... un giorno importante per me."),
    ("tessa", "Wait, did he just say Friday?!", "Aspetta, ha appena detto venerdì?!"),
]
WALK = [
    (0, None, ["'Guardate da vicino questa pagina. Misura i decibel e la quiete, non le stelle degli alberghi!' Osservare qualcosa con attenzione si dice", (None, "Look closely at"), "dove la preposizione resta indispensabile davanti all'oggetto."]),
    (1, None, ["'Decibel? Quindi «nove su dieci» non era una recensione del mio bancone d'accoglienza?' Un giudizio scritto da un cliente si chiama", (None, "review"), "recensione."]),
    (2, None, ["'Beh, il tuo bancone merita dieci! A dire il vero, però, sono un architetto acustico.' Nota", (None, "though"), "inserito tra virgole con il senso di però, e l'articolo", (None, "an"), "davanti al suono vocalico."]),
    (3, None, ["'Un architetto acustico! Progetta sale da concerto?' Attenzione a", (None, "design"), "con consonante muta prima della nasale, e al composto", (None, "concert halls"), "sale da concerto."]),
    (4, None, ["'Piccole biblioteche e cortili, per lo più. Misuro come i vecchi muri di pietra bloccano il rumore della strada.' Altro falso amico celebre:", (None, "libraries"), "sono le biblioteche, mentre i rumori del traffico sono", (None, "street noise"), "rumore stradale."]),
    (5, None, ["'Ecco perché ieri sera tendeva l'orecchio alle auto lassù in soffitta!' Per introdurre la spiegazione di un fatto appena chiarito si usa", (None, "That is why"), "mentre", (None, "listened for"), "indica tendere l'orecchio per cogliere un suono."]),
    (6, None, ["'Esatto. Fuori sul viale c'è frastuono, eppure dentro questo cortile si sentono le foglie e gli uccelli.' La congiunzione elegante", (None, "yet"), "tra due frasi significa eppure, tuttavia."]),
    (7, None, ["'Aspetta che Arthur scopra di essersi agitato tutta la notte per delle misure sonore!' L'espressione vivace", (None, "Wait until Arthur hears"), "equivale al nostro aspetta che Arthur lo venga a sapere, seguita da", (None, "over"), "per via di."]),
    (8, None, ["'In tutta sincerità, ho scelto questo quartiere anche per un vecchio motivo di famiglia.' Il passato irregolare di scegliere è", (None, "chose"), "accompagnato da", (None, "family reason"), "motivo di famiglia."]),
    (9, None, ["'Oh? La sua famiglia viveva qui vicino un tempo?' Per chiedere se qualcosa accadeva nel passato lontano si chiude la frase con", (None, "once"), "un tempo, una volta."]),
    (10, None, ["'A due vie di distanza, quando ero piccolo. Venerdì è... un giorno importante per me.' La distanza si misura aggiungendo l'avverbio dopo il nome in", (None, "Two streets away"), "a due strade da qui."]),
    (11, None, ["'Aspetta, ha appena detto venerdì?!' Per verificare a caldo una parola appena sentita si uniscono ausiliare passato e avverbio in", (None, "did he just say"), "ha appena detto."]),
]
CALLOUT_TRANS = {
    "Look closely at": "guardate da vicino",
    "review": "recensione",
    "though": "però, tuttavia",
    "an": "un",
    "design": "progettare",
    "concert halls": "sale da concerto",
    "libraries": "biblioteche",
    "street noise": "rumore della strada",
    "That is why": "ecco perché",
    "listened for": "tendeva l'orecchio a",
    "yet": "eppure, tuttavia",
    "Wait until Arthur hears": "aspetta che Arthur lo sappia",
    "over": "per, riguardo a",
    "chose": "ho scelto",
    "family reason": "motivo di famiglia",
    "once": "un tempo, una volta",
    "Two streets away": "a due vie di distanza",
    "did he just say": "ha appena detto",
}
