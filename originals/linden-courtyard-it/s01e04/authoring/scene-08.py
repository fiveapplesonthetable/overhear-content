# Authoring module for linden-courtyard-it-s01e04-scene-08.
ID = "linden-courtyard-it-s01e04-scene-08"
SHOW = "linden-courtyard-it"
SEASON = 1
EPISODE = 4
SCENE = 8
TITLE = "The Boy on the Stairs  (Il bambino sulle scale)"
LEVEL = "A1 — principiante"
PAIR = "en-it"
LABELS = {"evelyn": "Evelyn", "hannah": "Hannah", "caleb": "Caleb"}
INTRO = "Uscendo nel cortile soleggiato della locanda, la signorina Evelyn racconta altro a Hannah sui due fratelli del numero dodici, senza sapere che Caleb è appena sceso dalla scala esterna dietro di loro. Ascolta prima la scena."
OPENER = "Ripercorriamo con cura ogni frase di questo riconoscimento emozionante nel cortile."
TRANSITION = "Riascoltiamo adesso l'intera scena finale dall'inizio alla fine."
OUTRO = "Che momento emozionante nel cortile! Il piccolo Caleb del terzo gradino si trova proprio davanti alla sua insegnante di pianoforte d'infanzia, ed è lui il proprietario della valigia misteriosa. Episodio quattro completato; ci ritroviamo nel quinto."
CLOSING = ("caleb", "Goodbye!")
STORY = [
    ("hannah", "Tell me more about the two boys on Linden Street, Miss Evelyn!", "Mi racconti qualcosa di più sui due bambini di via Linden, signorina Evelyn!"),
    ("evelyn", "The older brother was bold and loud, always rushing through his music scales.", "Il fratello maggiore era spavaldo e rumoroso, correva sempre veloce lungo le scale musicali."),
    ("hannah", "And the younger brother with the wooden train?", "E il fratello minore con il trenino di legno?"),
    ("evelyn", "Quiet as a mouse! He sat on the third stair listening to every single note.", "Silenzioso come un topolino! Sedeva sul terzo gradino ascoltando ogni singola nota."),
    ("hannah", "Listening to the sound of the room... wait a second!", "Ad ascoltare il suono della stanza... aspetti un secondo!"),
    ("evelyn", "Whenever I finished playing, he asked why the piano sounded warmer when it rained.", "Ogni volta che finivo di suonare, chiedeva perché il pianoforte suonava più caldo quando pioveva."),
    ("caleb", "Because wet wooden shutters soften the echo from the stone street...", "Perché le persiane di legno bagnate attutiscono l'eco della strada di pietra..."),
    ("hannah", "Caleb! Were you standing right there?!", "Caleb! Era fermo proprio lì?!"),
    ("evelyn", "Good heavens... look at your eyes! Little Caleb from the third stair?!", "Santo cielo... guardi i suoi occhi! Il piccolo Caleb del terzo gradino?!"),
    ("caleb", "Miss Evelyn?! My brother's Friday piano teacher?!", "Signorina Evelyn?! L'insegnante di pianoforte del venerdì di mio fratello?!"),
    ("hannah", "Wait, then Monday night on our step... the second blue suitcase...", "Aspetti, allora lunedì sera sul nostro gradino... la seconda valigia blu..."),
    ("caleb", "Yes, Hannah. That blue suitcase is mine, and I owe you both the whole truth.", "Sì, Hannah. Quella valigia blu è mia, e devo a tutt'e due l'intera verità."),
]
WALK = [
    (0, None, ["'Mi racconti qualcosa di più sui due bambini di via Linden, signorina Evelyn!' Per chiedere altri dettagli su una storia si usa", (None, "Tell me more about"), "mi racconti di più su."]),
    (1, None, ["'Il fratello maggiore era spavaldo e rumoroso, correva sempre veloce lungo le scale musicali.' Sbrigare un esercizio in tutta fretta si esprime con", (None, "rushing through"), "mentre", (None, "bold"), "significa audace, spavaldo."]),
    (2, None, ["'E il fratello minore con il trenino di legno?' Il comparativo", (None, "younger brother"), "indica il fratello più giovane tra i due."]),
    (3, None, ["'Silenzioso come un topolino! Sedeva sul terzo gradino ascoltando ogni singola nota.' Il paragone idiomatico per chi non fa il minimo rumore è", (None, "Quiet as a mouse"), "e un singolo scalino si chiama", (None, "third stair"), "terzo gradino."]),
    (4, None, ["'Ad ascoltare il suono della stanza... aspetti un secondo!' Quando colleghi all'improvviso due indizi nella mente esclami", (None, "wait a second"), "aspetta un secondo."]),
    (5, None, ["'Ogni volta che finivo di suonare, chiedeva perché il pianoforte suonava più caldo quando pioveva.' Nota", (None, "Whenever"), "che racchiude ogni volta che in una parola, e", (None, "finished playing"), "che regge il gerundio."]),
    (6, None, ["'Perché le persiane di legno bagnate attutiscono l'eco della strada di pietra...' Rendere più morbido o ovattato un rimbombo si dice", (None, "soften the echo"), "attutiscono l'eco, grazie alle", (None, "wet wooden shutters"), "persiane di legno bagnate."]),
    (7, None, ["'Caleb! Era fermo proprio lì?!' Il passato progressivo interrogativo", (None, "Were you standing"), "coglie la persona già lì in piedi mentre gli altri parlavano."]),
    (8, None, ["'Santo cielo... guardi i suoi occhi! Il piccolo Caleb del terzo gradino?!' Un'esclamazione gentile e un poco d'altri tempi per lo stupore improvviso è", (None, "Good heavens"), "santo cielo."]),
    (9, None, ["'Signorina Evelyn?! L'insegnante di pianoforte del venerdì di mio fratello?!' Guarda la catena compatta in", (None, "My brother's Friday piano teacher"), "dove possessivo, giorno e materia precedono tutti la parola insegnante."]),
    (10, None, ["'Aspetti, allora lunedì sera sul nostro gradino... la seconda valigia blu...' Qui", (None, "then"), "non ha valore temporale ma deduttivo, proprio come il nostro allora, quindi."]),
    (11, None, ["'Sì, Hannah. Quella valigia blu è mia, e devo a tutt'e due l'intera verità.' Dopo il verbo essere il possessivo resta autonomo in", (None, "is mine"), "mentre dovere qualcosa a qualcuno si costruisce con", (None, "I owe you both"), "devo a entrambe."]),
]
CALLOUT_TRANS = {
    "Tell me more about": "mi racconti di più su",
    "rushing through": "correndo veloce lungo",
    "bold": "spavaldo, audace",
    "younger brother": "fratello minore",
    "Quiet as a mouse": "silenzioso come un topolino",
    "third stair": "terzo gradino",
    "wait a second": "aspetti un secondo",
    "Whenever": "ogni volta che",
    "finished playing": "finivo di suonare",
    "soften the echo": "attutiscono l'eco",
    "wet wooden shutters": "persiane di legno bagnate",
    "Were you standing": "era fermo in piedi",
    "Good heavens": "santo cielo",
    "My brother's Friday piano teacher": "l'insegnante di pianoforte del venerdì di mio fratello",
    "then": "allora, quindi",
    "is mine": "è mia",
    "I owe you both": "devo a tutt'e due",
}
