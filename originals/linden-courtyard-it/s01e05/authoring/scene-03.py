# Authoring module for linden-courtyard-it-s01e05-scene-03.
ID = "linden-courtyard-it-s01e05-scene-03"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 5
SCENE = 3
TITLE = "Friday Lemon Cake  (La torta al limone del venerdì)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"evelyn": "Evelyn", "caleb": "Caleb", "tessa": "Tessa"}
INTRO = "Alle nove e mezza, nell'angolo caffetteria della Locanda del Cortile del Tiglio, Tessa versa caffè appena fatto per la signorina Evelyn e Caleb mentre rievocano i venerdì pomeriggio di venticinque anni prima. Ascolta prima tutta la scena."
OPENER = "Adesso ripassiamo il dialogo frase per frase."
TRANSITION = "Torniamo ad ascoltare la scena intera a ritmo naturale."
OUTRO = "Sei limoni freschi nel cestino della cucina e due ore e mezza prima di mezzogiorno: Tessa si allaccia già il grembiule. Usciamo in cortile nella prossima scena."
CLOSING = ("tessa", "Bye for now!")
STORY = [
    ("tessa", "So, Caleb, you are really staying in the courtyard to greet Owen at noon?", "Allora, Caleb, resti davvero nel cortile ad accogliere Owen a mezzogiorno?"),
    ("caleb", "Yes, Tessa. Even if he turns around and walks straight back out the gate.", "Sì, Tessa. Anche se si gira e se ne torna dritto fuori dal cancello."),
    ("evelyn", "Owen will not walk out. He always acted tough for five seconds, then softened.", "Owen non se ne andrà. Faceva sempre il duro per cinque secondi, e poi si scioglieva."),
    ("caleb", "You still remember that after all these years?", "Si ricorda ancora questo dettaglio dopo tutti questi anni?"),
    ("evelyn", "Of course! Every Friday when he missed a piano note, he frowned at the wall.", "Certo che sì! Ogni venerdì, quando sbagliava una nota al pianoforte, fissava il muro accigliato."),
    ("tessa", "How did you get him smiling again, Miss Evelyn?", "Come faceva a farlo tornare a sorridere, signorina Evelyn?"),
    ("evelyn", "His grandfather sliced warm lemon cake with powdered sugar on top!", "Suo nonno tagliava a fette una torta tiepida al limone con lo zucchero a velo sopra!"),
    ("caleb", "Oh! Yellow lemon glaze! We fought over the corner piece every single Friday!", "Oh! La glassa gialla al limone! Litigavamo per il pezzo d'angolo ogni singolo venerdì!"),
    ("tessa", "Hold everything! What time is it right now? Nine thirty-five!", "Fermi tutti! Che ore sono adesso? Le nove e trentacinque!"),
    ("caleb", "Tessa, please do not do extra work because of us.", "Tessa, ti prego, non fare lavoro in più per causa nostra."),
    ("tessa", "Six yellow lemons are sitting in my basket right now. This kitchen was waiting for today!", "Ci sono sei limoni gialli nel mio cestino proprio adesso. Questa cucina non aspettava altro che oggi!"),
    ("evelyn", "Bake plenty of corner pieces, my dear!", "Inforna tanti pezzi d'angolo, cara mia!"),
]
WALK = [
    (0, None, ["'Allora, Caleb, resti davvero nel cortile ad accogliere Owen a mezzogiorno?' Infilare l'avverbio nel mezzo della forma progressiva", (None, "are really staying"), "conferma una decisione ferma presa per oggi."]),
    (1, None, ["'Sì, Tessa. Anche se si gira e se ne torna dritto fuori dal cancello.' L'ipotesi estrema si apre con", (None, "Even if"), "mentre", (None, "turns around"), "disegna il gesto di voltarsi sui propri passi."]),
    (2, None, ["'Owen non se ne andrà. Faceva sempre il duro per cinque secondi, e poi si scioglieva.' Accostare il verbo recitare o comportarsi all'aggettivo in", (None, "acted tough"), "rende benissimo il nostro fare il duro."]),
    (3, None, ["'Si ricorda ancora questo dettaglio dopo tutti questi anni?' Il complemento di tempo", (None, "after all these years"), "scorre con lo stesso ordine naturale dell'italiano."]),
    (4, None, ["'Certo che sì! Ogni venerdì, quando sbagliava una nota al pianoforte, fissava il muro accigliato.' Per dire mancare un bersaglio o sbagliare un tasto musicale si usa", (None, "missed a piano note"), "mancava una nota al pianoforte."]),
    (5, None, ["'Come faceva a farlo tornare a sorridere, signorina Evelyn?' Nella lingua viva la struttura", (None, "get him smiling"), "esprime il riuscire a sbloccare qualcuno facendolo sorridere."]),
    (6, None, ["'Suo nonno tagliava a fette una torta tiepida al limone con lo zucchero a velo sopra!' In pasticceria lo zucchero ridotto in polvere finissima si chiama", (None, "powdered sugar"), "spolverato", (None, "on top"), "in superficie."]),
    (7, None, ["'Oh! La glassa gialla al limone! Litigavamo per il pezzo d'angolo ogni singolo venerdì!' Quando due bambini si contendono la stessa fetta, il passato irregolare si unisce alla preposizione in", (None, "fought over"), "litigavamo per."]),
    (8, None, ["'Fermi tutti! Che ore sono adesso? Le nove e trentacinque!' L'esclamazione vivace", (None, "Hold everything"), "ferma la conversazione quando spunta un'idea improvvisa."]),
    (9, None, ["'Tessa, ti prego, non fare lavoro in più per causa nostra.' Prima di un pronome o di un nome, la locuzione", (None, "because of us"), "traduce per colpa nostra o per via di noi."]),
    (10, None, ["'Ci sono sei limoni gialli nel mio cestino proprio adesso. Questa cucina non aspettava altro che oggi!' In inglese gli oggetti appoggiati in un recipiente spesso stanno seduti, come senti in", (None, "are sitting"), "si trovano lì pronti."]),
    (11, None, ["'Inforna tanti pezzi d'angolo, cara mia!' Per indicare abbondanza generosa nei cibi e nelle quantità, il blocco", (None, "plenty of"), "suona caldo e colloquiale."]),
]
CALLOUT_TRANS = {
    "are really staying": "resti davvero",
    "Even if": "anche se",
    "turns around": "si gira, fa dietrofront",
    "acted tough": "faceva il duro",
    "after all these years": "dopo tutti questi anni",
    "missed a piano note": "sbagliava una nota al pianoforte",
    "get him smiling": "farlo sorridere",
    "powdered sugar": "zucchero a velo",
    "on top": "sopra, in cima",
    "fought over": "litigavamo per, ci contendevamo",
    "Hold everything": "fermi tutti",
    "because of us": "per causa nostra",
    "are sitting": "stanno, si trovano",
    "plenty of": "in abbondanza, tanti",
}
