# Authoring module for linden-courtyard-it-s01e03-scene-07.
ID = "linden-courtyard-it-s01e03-scene-07"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 3
SCENE = 7
TITLE = "Returning the Notebook  (Restituendo il taccuino)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"hannah": "Hannah", "caleb": "Caleb"}
INTRO = "Hannah risale fino alla porta della soffitta per restituire a Caleb il taccuino di pelle dimenticato, cercando di apparire disinvolta anche se è convinta di parlare con un ispettore in incognito. Ascoltiamo prima la scena."
OPENER = "Analizziamo con calma ogni battuta di questo dialogo."
TRANSITION = "Riascoltiamo tutta la scena dall'inizio alla fine."
OUTRO = "Caleb ha riavuto il suo taccuino senza sospettare nulla, ma quel termosifone che inizia a raffreddarsi non promette niente di buono. Manca l'ultima scena del terzo episodio: scendiamo in cantina! A tra poco."
CLOSING = ("caleb", "Have a good night!")
STORY = [
    ("hannah", "Excuse me, Caleb? Sorry to disturb you.", "Mi scusi, Caleb? Mi dispiace disturbarla."),
    ("caleb", "Oh, my leather notebook! Thank you! I was just looking for it.", "Oh, il mio taccuino di pelle! Grazie! Lo stavo giusto cercando."),
    ("hannah", "You left it by the soup cup on the front counter.", "Lo ha lasciato accanto alla tazza di zuppa sul bancone d'ingresso."),
    ("caleb", "All my street notes from this week are in here. You saved me.", "Tutti i miei appunti sulle strade di questa settimana sono qui dentro. Mi ha salvato."),
    ("hannah", "We are glad you find our courtyard peaceful for your... work.", "Siamo felici che trovi il nostro cortile tranquillo per il suo... lavoro."),
    ("caleb", "Very peaceful! Though did you hear a funny metal knock just now?", "Molto tranquillo! Però ha sentito uno strano colpo metallico proprio adesso?"),
    ("hannah", "Yes! It sounded like it came from the heating pipe in the corner.", "Sì! Sembrava provenire dal tubo del riscaldamento nell'angolo."),
    ("caleb", "Feel the radiator. The top is warm, while the bottom is turning cool.", "Senta il termosifone. La parte alta è calda, mentre il fondo sta diventando fresco."),
    ("hannah", "Oh! Sometimes old pipes have a little air bubble at night.", "Oh! A volte i vecchi tubi fanno una piccola bolla d'aria di notte."),
    ("caleb", "I have a warm blanket, so I am quite comfortable tonight.", "Ho una coperta calda, quindi sto benissimo stanotte."),
    ("hannah", "Thank you for being so patient! Graham will check the basement right away.", "Grazie per essere così paziente! Graham controllerà subito il seminterrato."),
    ("caleb", "Good night, Hannah. See you at breakfast.", "Buonanotte, Hannah. Ci vediamo a colazione."),
]
WALK = [
    (0, None, ["'Mi scusi, Caleb? Mi dispiace disturbarla.' Quando bussi a una porta per chiedere scusa del disturbo sul momento, la formula cortese usa l'infinito in", (None, "Sorry to disturb you"), "scusi il disturbo."]),
    (1, None, ["'Oh, il mio taccuino di pelle! Grazie! Lo stavo giusto cercando.' Il passato progressivo", (None, "I was just looking for it"), "rende alla perfezione il nostro lo stavo proprio cercando."]),
    (2, None, ["'Lo ha lasciato accanto alla tazza di zuppa sul bancone d'ingresso.' Qui la breve preposizione in", (None, "by the soup cup"), "indica vicinanza immediata: proprio accanto alla tazza."]),
    (3, None, ["'Tutti i miei appunti sulle strade di questa settimana sono qui dentro. Mi ha salvato.' Senza bisogno di preposizione tra tutto e il possessivo si dice", (None, "All my street notes"), "tutti i miei appunti."]),
    (4, None, ["'Siamo felici che trovi il nostro cortile tranquillo per il suo... lavoro.' Dopo siamo contenti l'inglese omette volentieri il che e prosegue col presente indicativo in", (None, "We are glad you find"), "siamo lieti che trovi."]),
    (5, None, ["'Molto tranquillo! Però ha sentito uno strano colpo metallico proprio adesso?' Attenzione al doppio valore di", (None, "funny"), "che qui non significa divertente da ridere, bensì insolito o curioso."]),
    (6, None, ["'Sì! Sembrava provenire dal tubo del riscaldamento nell'angolo.' Per descrivere a che cosa somiglia un rumore seguito da un'intera frase si usa", (None, "It sounded like"), "sembrava proprio che."]),
    (7, None, ["'Senta il termosifone. La parte alta è calda, mentre il fondo sta diventando fresco.' Per invitare a toccare una superficie e sentirne la temperatura si usa", (None, "Feel the radiator"), "mentre", (None, "turning cool"), "esprime il raffreddarsi graduale."]),
    (8, None, ["'Oh! A volte i vecchi tubi fanno una piccola bolla d'aria di notte.' Con la notte in generale l'inglese sceglie la preposizione puntuale in", (None, "at night"), "di notte."]),
    (9, None, ["'Ho una coperta calda, quindi sto benissimo stanotte.' L'aggettivo", (None, "quite comfortable"), "riferito a una persona significa sentirsi comodo e a proprio agio."]),
    (10, None, ["'Grazie per essere così paziente! Graham controllerà subito il seminterrato.' Per ringraziare di una qualità dimostrata si abbina la preposizione alla forma progressiva in", (None, "Thank you for being"), "grazie di essere."]),
    (11, None, ["'Buonanotte, Hannah. Ci vediamo a colazione.' Dandosi appuntamento al pasto del mattino si usa la preposizione puntuale senza articolo:", (None, "See you at breakfast"), "ci vediamo a colazione."]),
]
CALLOUT_TRANS = {
    "Sorry to disturb you": "mi dispiace disturbarla",
    "I was just looking for it": "lo stavo giusto cercando",
    "by the soup cup": "accanto alla tazza di zuppa",
    "All my street notes": "tutti i miei appunti sulle strade",
    "We are glad you find": "siamo felici che trovi",
    "funny": "strano, curioso",
    "It sounded like": "sembrava che",
    "Feel the radiator": "senta il termosifone",
    "turning cool": "diventando fresco",
    "at night": "di notte",
    "quite comfortable": "molto comodo",
    "Thank you for being": "grazie per essere",
    "See you at breakfast": "ci vediamo a colazione",
}
