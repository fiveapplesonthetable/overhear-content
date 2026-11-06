# Authoring module for locanda-del-tiglio-s01e03-scene-02.
ID = 'locanda-del-tiglio-s01e03-scene-02'
SHOW = 'locanda-del-tiglio'
SEASON = 1
EPISODE = 3
SCENE = 2
TITLE = 'La mansarda luminosa  (The Sunny Attic)'
LEVEL = 'A1 — beginner'
PAIR = 'it-en'
LABELS = {'bruno': 'Bruno', 'chiara': 'Chiara', 'giulia': 'Giulia'}
INTRO = "Up under the wooden eaves on the third floor, Bruno unlocks the attic study for Chiara while Giulia comes up carrying fresh towels. Let's listen to the whole scene first."
OPENER = "Let's inspect the third-floor attic room line by line."
TRANSITION = "Now let's hear the whole attic scene again from start to finish."
OUTRO = 'With wooden beams and rain on the roof, the attic only needs a lamp, two pillows, and a rug. See you next time as they race the clock.'
CLOSING = ('giulia', 'A presto!')
STORY = [
    ('chiara', 'Oh, guarda questa stanza! Grandi travi di legno e una finestra sul cortile!', 'Oh, look at this room! Big wooden beams and a window over the courtyard!'),
    ('giulia', 'Senti la pioggia sul tetto: è così accogliente quassù!', 'Listen to the rain on the roof—it feels so cosy up here!'),
    ('bruno', 'Asciutta, calda e silenziosa. Ora ditemi cosa manca.', 'Dry, warm, and quiet. Now tell me what is missing.'),
    ('chiara', "Allora: c'è un letto, un tavolo e una sedia, ma niente lampada vicino al letto.", 'Okay: there is a bed, a table, and a chair, but no bedside lamp.'),
    ('giulia', 'E niente specchio al muro, e il pavimento sembra vuoto senza tappeto.', 'And no mirror on the wall, and the floor feels bare without a rug.'),
    ('bruno', "C'è una lampada da lettura di ottone nel mio laboratorio giù.", 'There is a brass reading lamp in my workshop downstairs.'),
    ('giulia', 'E io ho due cuscini morbidi e un tappeto blu nel ripostiglio!', 'And I have two soft pillows and a woven blue rug in the store room!'),
    ('chiara', 'E il piccolo bagno qui accanto? La luce funziona?', 'What about the small bathroom next door? Does the light work?'),
    ('bruno', 'Lampadina nuova la settimana scorsa, sapone pulito e tanta acqua calda.', 'New bulb last week, clean soap, plenty of hot water.'),
    ('giulia', 'Dateci quindici minuti e questa mansarda batte la camera sette!', 'Give us fifteen minutes and this attic will beat room seven!'),
    ('chiara', 'Prendi quelle scatole di cartone, Bruno: scendiamo subito!', 'Grab those cardboard boxes, Bruno—down the stairs we go!'),
    ('bruno', 'Attente alla curva, non toccate il muro!', 'Careful on the turn, do not bump the wall!'),
]
WALK = [
    (0, None, ["'Oh, look at this room! Big wooden beams and a window over the courtyard!' Look at stops needing at in Italian.", (None, 'Guarda questa stanza!'), 'You look the room directly, without any small linking word in between.']),
    (1, None, ["'Listen to the rain on the roof—it feels so cosy up here!' Two neat words blend at the end to say up here.", (None, 'È così accogliente quassù!'), 'Built from here plus up, it pairs naturally with its twin word for down here.']),
    (2, None, ["'Dry, warm, and quiet. Now tell me what is missing.' One compact word handles is missing.", (None, 'Cosa manca.'), 'Whenever salt is missing from soup or a lamp is missing from a room, Italian speakers reach for that word.']),
    (3, None, ["'Okay: there is a bed, a table, and a chair, but no bedside lamp.' Taking stock of a list starts with a classic filler word.", (None, 'Allora'), "Literally then, Italian speakers use it at the start of a turn just like okay, well then, or let's see."]),
    (4, None, ["'And no mirror on the wall, and the floor feels bare without a rug.' Watch out for a false friend on the floor.", (None, 'Il pavimento'), 'In Italian that means an indoor floor—never the outdoor sidewalk!']),
    (5, None, ["'There is a brass reading lamp in my workshop downstairs.' Notice how reading lamp shows its purpose.", (None, 'Una lampada da lettura'), "Literally a lamp for reading, using the same purpose link we saw earlier in men's shoes."]),
    (6, None, "'And I have two soft pillows and a woven blue rug in the store room!' Soft changes its ending to i here to match the two pillows."),
    (7, None, ["'What about the small bathroom next door? Does the light work?' Two short words say right next door.", (None, 'Qui accanto?'), 'Literally here beside, and at the end works uses the word for functions rather than works at a job.']),
    (8, None, ["'New bulb last week, clean soap, plenty of hot water.' Lamp shrinks playfully to make light bulb.", (None, 'Lampadina nuova'), 'Literally little lamp, because the glass bulb sits inside the bigger fixture.']),
    (9, None, ["'Give us fifteen minutes and this attic will beat room seven!' Us hooks onto the end of plural give.", (None, 'Dateci quindici minuti'), 'Giving to us fifteen minutes—brisk, confident, and ready to move.']),
    (10, None, "'Grab those cardboard boxes, Bruno—down the stairs we go!' Big paper grows an augmenting ending to become cardboard—literally heavy thick paper!"),
    (11, None, ["'Careful on the turn, do not bump the wall!' Speaking to Chiara and Giulia together, Bruno ends careful in e.", (None, 'Attente alla curva'), 'Feminine plural because both people carrying boxes beside him are women.']),
]
