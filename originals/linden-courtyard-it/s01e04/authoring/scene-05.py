# Authoring module for linden-courtyard-it-s01e04-scene-05.
ID = "linden-courtyard-it-s01e04-scene-05"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 4
SCENE = 5
TITLE = "Five-Star Showers  (Docce a cinque stelle)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"arthur": "Arthur", "caleb": "Caleb", "hannah": "Hannah"}
INTRO = "Venti minuti più tardi, nell'angolo luminoso della colazione, Caleb scende riposato mentre Hannah versa il caffè e Arthur gli gira intorno con evidente agitazione. Ascolta prima tutta la scena."
OPENER = "Rivediamo insieme le battute di questo malinteso a colazione."
TRANSITION = "Riascoltiamo ora la scena per intero senza pause."
OUTRO = "Arthur si è lasciato sfuggire il segreto in tempo da primato e, invece di arrabbiarsi, Caleb li invita nel cortile per mostrare di che cosa si occupa davvero. A presto."
CLOSING = ("caleb", "Take care!")
STORY = [
    ("caleb", "Good morning, Hannah! Good morning, sir! What a bright morning after the rain.", "Buongiorno, Hannah! Buongiorno, signore! Che mattinata luminosa dopo la pioggia."),
    ("hannah", "Good morning, Caleb! Did you sleep well under the roof beams?", "Buongiorno, Caleb! Ha dormito bene sotto le travi del tetto?"),
    ("caleb", "Best sleep I have had all month, and the shower water was wonderfully hot!", "La migliore dormita di tutto il mese, e l'acqua della doccia era meravigliosamente calda!"),
    ("arthur", "Hot! Hear that, Hannah? Reliable, modern, five-star hot water!", "Calda! Senti, Hannah? Acqua calda affidabile, moderna e a cinque stelle!"),
    ("caleb", "Old brick buildings usually take ages to warm up on the top floor.", "I vecchi edifici di mattoni di solito impiegano un'eternità a scaldarsi all'ultimo piano."),
    ("arthur", "Please write that down! 'Hot water on the third floor: ten out of ten!'", "Per favore, prenda nota! «Acqua calda al terzo piano: dieci su dieci!»"),
    ("caleb", "Excuse me? Ten out of ten?", "Come scusi? Dieci su dieci?"),
    ("hannah", "What Arthur means is... we hope every guest feels ten out of ten here!", "Quello che Arthur intende dire è... speriamo che ogni ospite si senta dieci su dieci qui!"),
    ("arthur", "No, Hannah, let us be honest professionals! Sir, we respect the Portland Travel Guide!", "No, Hannah, siamo professionisti sinceri! Signore, rispettiamo la Guida Turistica di Portland!"),
    ("caleb", "The Portland Travel Guide? Wait, do you think I am a hotel inspector?", "La Guida Turistica di Portland? Aspettate, pensate che io sia un ispettore d'albergo?"),
    ("hannah", "When your notebook fell open on the counter last night, we saw 'nine out of ten'...", "Quando il suo taccuino è caduto aperto sul bancone ieri sera, abbiamo visto «nove su dieci»..."),
    ("caleb", "Oh! Come outside to the courtyard for a minute. Let me show you what I really do!", "Oh! Venite fuori nel cortile un minuto. Lasciate che vi mostri che cosa faccio davvero!"),
]
WALK = [
    (0, None, ["'Buongiorno, Hannah! Buongiorno, signore! Che mattinata luminosa dopo la pioggia.' L'esclamazione su un nome singolare richiede l'articolo in", (None, "What a bright morning"), "che mattinata luminosa."]),
    (1, None, ["'Buongiorno, Caleb! Ha dormito bene sotto le travi del tetto?' La domanda al passato semplice si appoggia all'ausiliare in", (None, "Did you sleep well"), "e le travi portanti si chiamano", (None, "roof beams"), "travi del tetto."]),
    (2, None, ["'La migliore dormita di tutto il mese, e l'acqua della doccia era meravigliosamente calda!' Per collegare un'esperienza a un periodo ancora in corso si usa", (None, "I have had all month"), "che ho fatto in tutto il mese."]),
    (3, None, ["'Calda! Senti, Hannah? Acqua calda affidabile, moderna e a cinque stelle!' Quando un numero e un nome fungono insieme da aggettivo perdono il plurale e prendono il trattino in", (None, "five-star"), "a cinque stelle."]),
    (4, None, ["'I vecchi edifici di mattoni di solito impiegano un'eternità a scaldarsi all'ultimo piano.' Per dire metterci tantissimo tempo nel parlato quotidiano è vivacissima l'espressione", (None, "take ages"), "impiegare un'eternità."]),
    (5, None, ["'Per favore, prenda nota! «Acqua calda al terzo piano: dieci su dieci!»' Annotare qualcosa su carta si dice", (None, "write that down"), "mentre i punteggi si esprimono con", (None, "ten out of ten"), "dieci su dieci."]),
    (6, None, ["'Come scusi? Dieci su dieci?' Con tono interrogativo,", (None, "Excuse me?"), "non chiede permesso ma esprime sorpresa chiedendo all'altro di ripetere o spiegarsi."]),
    (7, None, ["'Quello che Arthur intende dire è... speriamo che ogni ospite si senta dieci su dieci qui!' Per chiarire o correggere con tatto le parole altrui si apre con", (None, "What Arthur means is"), "ciò che Arthur intende dire è."]),
    (8, None, ["'No, Hannah, siamo professionisti sinceri! Signore, rispettiamo la Guida Turistica di Portland!' Nella sua forma distesa più solenne, l'esortazione plurale appare come", (None, "let us be"), "siamo."]),
    (9, None, ["'La Guida Turistica di Portland? Aspettate, pensate che io sia un ispettore d'albergo?' Dove l'italiano richiede il congiuntivo sia, l'inglese mantiene il semplice indicativo in", (None, "do you think I am"), "pensate che io sia."]),
    (10, None, ["'Quando il suo taccuino è caduto aperto sul bancone ieri sera, abbiamo visto «nove su dieci»...' Nota il risultato unito direttamente al verbo di caduta in", (None, "fell open"), "è caduto restando aperto."]),
    (11, None, ["'Oh! Venite fuori nel cortile un minuto. Lasciate che vi mostri che cosa faccio davvero!' Per proporre di far vedere qualcosa di persona si usa", (None, "Let me show you"), "seguito da", (None, "what I really do"), "con ordine affermativo."]),
]
CALLOUT_TRANS = {
    "What a bright morning": "che mattinata luminosa",
    "Did you sleep well": "ha dormito bene",
    "roof beams": "travi del tetto",
    "I have had all month": "che ho fatto in tutto il mese",
    "five-star": "a cinque stelle",
    "take ages": "impiegano un'eternità",
    "write that down": "prenda nota, lo scriva",
    "ten out of ten": "dieci su dieci",
    "Excuse me?": "come scusi?",
    "What Arthur means is": "quello che Arthur intende dire è",
    "let us be": "siamo",
    "do you think I am": "pensate che io sia",
    "fell open": "è caduto aperto",
    "Let me show you": "lasciate che vi mostri",
    "what I really do": "che cosa faccio davvero",
}
