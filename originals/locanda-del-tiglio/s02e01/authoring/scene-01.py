# Authoring module for locanda-del-tiglio-s02e01-scene-01.
ID = 'locanda-del-tiglio-s02e01-scene-01'
SHOW = 'locanda-del-tiglio'
SEASON = 2
EPISODE = 1
SCENE = 1
TITLE = 'La nona chiave  (The Ninth Key)'
LEVEL = 'A1 — beginner'
PAIR = 'it-en'
LABELS = {'chiara': 'Chiara', 'bruno': 'Bruno', 'cesare': 'Cesare'}
INTRO = "It is early Saturday morning at the Locanda del Tiglio in Bologna, just hours after Bruno carried a dusty cedar box marked 'Room 9' up from the cellar. Chiara and Cesare lean over the front desk as Bruno turns the tiny brass key. Listen to the scene first."
OPENER = "Let's open the cedar box again, one line at a time."
TRANSITION = "Now let's hear the whole front-desk scene again from start to finish."
OUTRO = "Inside the cedar box sit a heavy door key and a floor plan pointing straight behind the hallway bookcase. Don't worry if a word or two went past quickly; they return right away. See you next time."
CLOSING = ('chiara', 'Ciao, alla prossima!')
STORY = [
    ('cesare', 'Gira la piccola chiave piano, Bruno. Mi batte forte il cuore!', 'Turn the little key slowly, Bruno. My heart is pounding!'),
    ('bruno', 'Calma, capo. Una serratura di ottone non si rompe mai.', 'Relax, boss. A brass lock never breaks.'),
    ('chiara', 'Ha fatto clic! Alza il coperchio, Bruno!', 'It clicked! Lift the lid, Bruno!'),
    ('bruno', "Dentro c'è... una grande chiave, una pianta blu e delle cartoline.", "Inside there's... a big key, a blue floor plan and some postcards."),
    ('cesare', 'Leggi il foglio blu! Dove sono i miei occhiali?', 'Read the blue sheet! Where are my glasses?'),
    ('chiara', 'Sono sulla fronte, signor Cesare, come ieri sera.', "They're on your forehead, Cesare, just like last night."),
    ('cesare', "Ecco! Guardate: 'Piano terra, camera nove, giardino d'inverno'!", "Aha! Look: 'Ground floor, room nine, winter garden'!"),
    ('chiara', "Aspetti, abbiamo un giardino d'inverno al piano terra?", 'Wait, we have a sunroom on the ground floor?'),
    ('bruno', 'Guardate la freccia: è dietro la libreria del corridoio.', "Look at the arrow: it's behind the hallway bookcase."),
    ('cesare', "Quella libreria pesante è contro il muro da vent'anni!", 'That heavy bookcase has stood against the wall for twenty years!'),
    ('chiara', "Allora dietro i vecchi libri c'è una nona porta!", 'Then behind the old books there is a ninth door!'),
    ('bruno', 'Prima un sorso di caffè, poi spostiamo i libri.', 'A sip of coffee first, then we move the books.'),
]
WALK = [
    (0, None, ["'Turn the little key slowly, Bruno. My heart is pounding!' Listen for the word for slowly at the end of his first sentence.", (None, 'Piano'), 'Remember it: the very same word comes back today meaning floor, and later meaning the instrument.']),
    (1, None, ["'Relax, boss. A brass lock never breaks.' Bruno's teasing word for the owner is short and blunt.", (None, 'Capo.'), 'It means boss or head, from the same Latin root as English captain.']),
    (2, None, ["'It clicked! Lift the lid, Bruno!' Italian says the lock made a click, using the everyday verb for do and make.", (None, 'Ha fatto clic!'), 'Swap in any sound you like: it made a bang, it made a pop.']),
    (3, None, ["'Inside there's a big key, a blue floor plan and some postcards.' Careful: this word usually means a house plant, but on paper it is a floor plan.", (None, 'Una pianta blu'), 'So Bruno is not holding a blue plant.']),
    (4, None, ["'Read the blue sheet! Where are my glasses?' As in English, glasses are always plural, so my becomes plural too.", (None, 'I miei occhiali'), 'Cesare asks this question in every episode.']),
    (5, None, ["'They're on your forehead, Cesare, just like last night.' Chiara keeps a polite title in front of his first name.", (None, 'Signor Cesare'), 'The word for sir drops its final vowel when a name follows.']),
    (6, None, ["'Ground floor, room nine, winter garden!' The Italian sunroom is literally a garden of winter.", (None, "Giardino d'inverno"), 'A glass room where plants and people stay warm in the cold months.']),
    (7, None, ["'Wait, we have a sunroom on the ground floor?' The ground floor is literally the earth floor.", (None, 'Al piano terra'), 'There is that word for slowly again, now meaning a floor of a building.']),
    (8, None, ["'Look at the arrow: it's behind the hallway bookcase.' Here is a false friend: it looks like library, but it means a bookcase or a bookshop.", (None, 'La libreria'), 'Bologna has a famous old library, and that takes a completely different word.']),
    (9, None, ["'That heavy bookcase has stood against the wall for twenty years!' Where English says has stood for, Italian keeps the present tense: it is there since twenty years.", (None, "Da vent'anni!"), 'Twenty loses its last vowel before years.']),
    (10, None, ["'Then behind the old books there is a ninth door!' The word for ninth grows straight out of the word for nine.", (None, 'Una nona porta!'), 'Door is feminine, so ninth ends in a.']),
    (11, None, ["'A sip of coffee first, then we move the books.' Bruno's plan comes in two steps, first and then.", (None, 'Prima'), 'and', (None, 'poi.'), 'A handy pair for giving any set of instructions.']),
]
