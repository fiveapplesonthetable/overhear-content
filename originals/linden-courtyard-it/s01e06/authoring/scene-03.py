# Authoring module for linden-courtyard-it-s01e06-scene-03.
ID = "linden-courtyard-it-s01e06-scene-03"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 6
SCENE = 3
TITLE = "Thirty Days on Paper  (Trenta giorni sulla carta)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"arthur": "Arthur", "hannah": "Hannah", "graham": "Graham"}
INTRO = "Di nuovo dietro il bancone della Locanda del Cortile del Tiglio, Arthur siede abbattuto accanto alla bacheca delle chiavi mentre Graham e Hannah si chinano sul registro parlando a bassa voce. Ascolta prima tutta la scena."
OPENER = "Ripassiamo ora ogni frase con tranquillità."
TRANSITION = "Ascoltiamo un'altra volta l'intera scena a ritmo normale."
OUTRO = "Hannah si è ricordata che hanno un esperto di edifici storici a cortile seduto proprio sotto il loro albero. Nella prossima scena Tessa serve la torta e Owen si accorge che dentro qualcosa non va. Alla prossima."
CLOSING = ("graham", "Bye for now!")
STORY = [
    ("arthur", "Fifteen years of polishing brass keys and straightening ties... gone in thirty days!", "Quindici anni passati a lucidare chiavi d'ottone e raddrizzare cravatte... svaniti in trenta giorni!"),
    ("graham", "Stop burying us before we read the whole document, Arthur.", "Smettila di darci per spacciati prima ancora di leggere l'intero documento, Arthur."),
    ("hannah", "Yes! Earlier I noticed a second page clipped behind the cover letter.", "Sì! Poco fa ho notato una seconda pagina fermata con la graffetta dietro la lettera di accompagnamento."),
    ("arthur", "Legal paragraphs give me a headache even with two pairs of glasses!", "I paragrafi legali mi fanno venire il mal di testa persino con due paia di occhiali!"),
    ("graham", "This house survived eighty winters and one broken boiler valve yesterday.", "Questa casa è sopravvissuta a ottanta inverni e ieri pure a una valvola rotta della caldaia."),
    ("hannah", "Wait, who is sitting ten meters away in our courtyard right now?", "Aspettate, chi è seduto a dieci metri di distanza nel nostro cortile proprio adesso?"),
    ("arthur", "Two brothers eating lemon cake?", "Due fratelli che mangiano torta al limone?"),
    ("hannah", "An architect who works with historic courtyard buildings all over Portland!", "Un architetto che lavora con edifici storici a cortile in tutta Portland!"),
    ("graham", "Smart thinking, Hannah. Caleb reads city building rules every single week.", "Ottima pensata, Hannah. Caleb legge i regolamenti edilizi comunali ogni singola settimana."),
    ("arthur", "Oh, I could never bother a paying guest with our landlord troubles!", "Oh, non potrei mai disturbare un ospite pagante con i nostri guai d'affitto!"),
    ("hannah", "After we guarded his blue suitcase all week? He will want to help!", "Dopo che abbiamo custodito la sua valigia blu per tutta la settimana? Vorrà darci una mano di sicuro!"),
    ("graham", "Wait, Tessa is taking the cake out to their table right now.", "Aspettate, Tessa sta portando fuori la torta al loro tavolo proprio adesso."),
]
WALK = [
    (0, None, ["'Quindici anni passati a lucidare chiavi d'ottone e raddrizzare cravatte... svaniti in trenta giorni!' Dopo la preposizione specificativa compare il gerundio sostantivato in", (None, "of polishing"), "mentre", (None, "gone in thirty days"), "esprime il timore di vedere tutto sparire."]),
    (1, None, ["'Smettila di darci per spacciati prima ancora di leggere l'intero documento, Arthur.' L'aggettivo di totalità si colloca tra articolo e nome in", (None, "the whole document"), "il documento intero."]),
    (2, None, ["'Sì! Poco fa ho notato una seconda pagina fermata con la graffetta dietro la lettera di accompagnamento.' Per riferirsi a qualche minuto prima nella stessa giornata basta", (None, "Earlier"), "e il foglio iniziale di una pratica si chiama", (None, "cover letter"), "lettera di presentazione."]),
    (3, None, ["'I paragrafi legali mi fanno venire il mal di testa persino con due paia di occhiali!' Far venire mal di testa usa l'articolo indeterminativo in", (None, "give me a headache"), "e per contare gli occhiali serve", (None, "two pairs of glasses"), "due paia di occhiali."]),
    (4, None, ["'Questa casa è sopravvissuta a ottanta inverni e ieri pure a una valvola rotta della caldaia.' A differenza dell'italiano, il verbo sopravvivere è transitivo diretto senza preposizione in", (None, "survived eighty winters"), "è sopravvissuta a ottanta inverni."]),
    (5, None, ["'Aspettate, chi è seduto a dieci metri di distanza nel nostro cortile proprio adesso?' La distanza precisa da dove ci troviamo si chiude con l'avverbio spaziale in", (None, "ten meters away"), "a dieci metri da qui."]),
    (6, None, ["'Due fratelli che mangiano torta al limone?' Per descrivere qualcuno colto in un'azione non serve il pronome relativo: basta il participio presente", (None, "eating lemon cake"), "che mangiano torta al limone."]),
    (7, None, ["'Un architetto che lavora con edifici storici a cortile in tutta Portland!' La distribuzione in ogni quartiere di una città è resa benissimo da", (None, "all over Portland"), "in giro per tutta Portland."]),
    (8, None, ["'Ottima pensata, Hannah. Caleb legge i regolamenti edilizi comunali ogni singola settimana.' Il complimento rapido per un'intuizione brillante è", (None, "Smart thinking"), "seguito dal composto", (None, "city building rules"), "norme edilizie comunali."]),
    (9, None, ["'Oh, non potrei mai disturbare un ospite pagante con i nostri guai d'affitto!' Lo scrupolo di Arthur unisce condizionale e negazione in", (None, "could never bother"), "davanti all'espressione alberghiera", (None, "paying guest"), "ospite pagante."]),
    (10, None, ["'Dopo che abbiamo custodito la sua valigia blu per tutta la settimana? Vorrà darci una mano di sicuro!' Il futuro esprime qui una previsione sicura sulla buona volontà altrui:", (None, "He will want to help"), "vorrà sicuramente aiutare."]),
    (11, None, ["'Aspettate, Tessa sta portando fuori la torta al loro tavolo proprio adesso.' Quando il soggetto è un nome proprio e non un pronome, l'inversione presentativa mette il verbo prima del nome in", (None, "taking the cake out"), "ecco Tessa di ritorno."]),
]
CALLOUT_TRANS = {
    "of polishing": "passati a lucidare",
    "gone in thirty days": "svaniti in trenta giorni",
    "the whole document": "l'intero documento",
    "Earlier": "poco fa, prima",
    "cover letter": "lettera di accompagnamento",
    "give me a headache": "mi fanno venire il mal di testa",
    "two pairs of glasses": "due paia di occhiali",
    "survived eighty winters": "è sopravvissuta a ottanta inverni",
    "ten meters away": "a dieci metri di distanza",
    "eating lemon cake": "che mangiano torta al limone",
    "all over Portland": "in tutta Portland",
    "Smart thinking": "ottima pensata, ben pensato",
    "city building rules": "regolamenti edilizi comunali",
    "could never bother": "non potrei mai disturbare",
    "paying guest": "ospite pagante",
    "He will want to help": "vorrà aiutare",
    "taking the cake out": "ecco che torna Tessa",
}
