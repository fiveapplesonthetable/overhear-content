# Authoring module for dix-pour-cent s03e06 scene 08 (cues 442-461).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e06/authoring/scene-08.py --out out/dix-pour-cent/s03e06/scene-08.json

ID = "dix-pour-cent-s03e06-scene-08"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 8
TITLE = "La geisha et le cadavre  (The Geisha and the Corpse)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "isabelle": "emilie", "realisateur": "theo"}
LABELS = {"lea": "Andréa", "isabelle": "Isabelle", "realisateur": "Le Réalisateur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 442-461. On set, the director complains that the stand-in looks like a geisha, "
               "while nurse Isabelle corrects him on accurate post-mortem skin lividity. Adapted for A1 French.")

INTRO = ("On the film set, nurse Isabelle Huppert is prepped to stand in as a dead body. "
         "When the director arrives and finds her covered in white talcum powder, an argument breaks out over medical accuracy. "
         "Let's listen to their exchange in French first.")

STORY = [
    ("realisateur", "Mais qu'est-ce que c'est que ça?",
     "What on earth is that?",
     [(442, "Mais qu'est-ce que c'est que ça ?")], "The director is shocked by the makeup"),
    ("realisateur", "J'ai dit fantôme, pas geisha!",
     "I said ghost, not geisha!",
     [(443, "J'ai dit fantôme, j'ai pas dit geisha.")], "The director mocks the white face paint"),
    ("lea", "Nous faisons ce que nous pouvons!",
     "We are doing what we can!",
     [(444, "Je fais ce que je peux.")], "Andrea defends the rushed preparations"),
    ("isabelle", "La lividité cadavérique n'est pas blanche.",
     "Post-mortem lividity is not white.",
     [(445, "la lividité cadavérique, c'est pas blanc.")], "Isabelle provides a medical correction"),
    ("isabelle", "La peau devient plutôt rose bleutée.",
     "The skin turns rather bluish pink.",
     [(446, "c'est plutôt rose bleutée.")], "Isabelle describes real corpse coloration"),
    ("realisateur", "Vous donnez des conseils médicaux maintenant?",
     "Are you giving medical advice now?",
     [(447, "je dis rien.")], "The director reacts with irritation"),
    ("isabelle", "Je dis ça par expérience professionnelle!",
     "I say that from professional experience!",
     [(447, "Non, je dis ça")], "Isabelle stands by her hospital expertise"),
    ("isabelle", "Vous vous en moquez au cinéma?",
     "Do you not care about accuracy in cinema?",
     [(448, "Vous vous en foutez, au cinéma ?")], "Isabelle questions movie realism"),
    ("realisateur", "Je dois la dé-talquer complètement?",
     "Should I completely de-talc her?",
     [(449, "Je fais quoi ? Je la dé-talque ?")], "The director seeks a quick fix"),
    ("lea", "Oui s'il te plaît, nettoie son visage.",
     "Yes please, clean her face.",
     [(450, "Oui, s'il te plaît, oui.")], "Andrea urges prompt action"),
    ("realisateur", "Le tournage prend beaucoup de retard!",
     "The shoot is falling very behind!",
     [(449, "Je fais quoi ?")], "The director worries about timing"),
    ("lea", "Tout va très bien se passer.",
     "Everything is going to go very well.",
     [(461, "C'est plutôt simple.")], "Andrea reassures the panicked crew"),
    ("isabelle", "Faites confiance à une infirmière diplômée!",
     "Trust a certified nurse!",
     [(448, "au cinéma ?")], "Isabelle asserts her credentials proudly"),
]

OPENER = "Let's explore how nurse Isabelle challenges the movie director line by line."

WALK = [
    (0, None,
     "'What on earth is that?' The director is horrified by the strange makeup look."),
    (1, None,
     "'I said ghost, not geisha!' The director angrily points out the thick white powder covering her face."),
    (2, None,
     "'We are doing what we can!' Andrea defends their improvised on-set preparations."),
    (3, None,
     "'Post-mortem lividity is not white.' Isabelle points out the scientific inaccuracy of the makeup."),
    (4, None,
     "'The skin turns rather bluish pink.' The nurse describes authentic physiological coloration after death."),
    (5, None,
     "'Are you giving medical advice now?' The director is annoyed by the unexpected critique."),
    (6, None,
     "'I say that from professional experience!' Isabelle proudly defends her hospital training."),
    (7, None,
     "'Do you not care about accuracy in cinema?' Isabelle questions the casual indifference of filmmakers."),
    (8, None,
     "'Should I completely de-talc her?' The director asks whether to wipe off the white powder."),
    (9, None,
     "'Yes please, clean her face.' Andrea urges him to fix the makeup quickly."),
    (10, None,
     "'The shoot is falling very behind!' The director stresses over the tight production schedule."),
    (11, None,
     "'Everything is going to go very well.' Andrea reassures the crew that the shot will work."),
    (12, None,
     "'Trust a certified nurse!' Isabelle brings comedic confidence to her acting debut."),
]

TRANSITION = "Now let's listen to the on-set banter once more from start to finish."

OUTRO = ("Nurse Isabelle brings real-world clinical knowledge to a chaotic film set, clashing comically with the director. "
         "Let's review the key makeup and filmmaking vocabulary from this scene.")

CLOSING = ("isabelle", "Faites confiance à une infirmière diplômée!")
