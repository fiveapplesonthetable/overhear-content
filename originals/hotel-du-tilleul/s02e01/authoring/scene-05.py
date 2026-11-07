# Authoring module for hotel-du-tilleul-s02e01-scene-05.
ID = 'hotel-du-tilleul-s02e01-scene-05'
SHOW = 'hotel-du-tilleul'
SEASON = 2
EPISODE = 1
SCENE = 5
TITLE = 'On mesure le jardin d\'hiver  (Measuring the Sunroom)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'antoine': 'Antoine', 'thibault': 'Thibault', 'claire': 'Claire'}
INTRO = ('Ten minutes later, Antoine hurries downstairs with his leather notebook alongside his older brother '
         'Thibault, who walked over early from his flat in Lyon after their Friday reunion. Claire meets them at '
         'the sunroom door. Listen first.')
OPENER = "Let's take the measurements again with Antoine and Thibault."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = ('Antoine approves the acoustics, and Thibault volunteers a pair of strong hands for the weekend. '
         'See you next time.')
CLOSING = ('antoine', 'À plus tard!')
STORY = [
    ('antoine',
     'Claire, Nadia nous a dit que vous avez ouvert une neuvième pièce cachée!',
     'Claire, Nadia told us you unlocked a hidden ninth room!'),
    ('thibault',
     'Mon petit frère a pris son mètre avant de finir sa tartine.',
     'My little brother grabbed his tape measure before finishing his toast.'),
    ('claire',
     'Entrez, tous les deux! Dites-nous si on peut ouvrir cette pièce sans danger.',
     'Come in, both of you! Tell us if we can open this room safely.'),
    ('antoine',
     'Quatre mètres de large, six de long, mur en brique à gauche, plafond en bois.',
     'Four metres wide, six long, brick wall on the left, wooden ceiling.'),
    ('thibault',
     'Écoute comme la rue est calme quand on tape une fois dans les mains.',
     'Listen how quiet the street is when you clap your hands once.'),
    ('antoine',
     'Zéro écho! Le bois au-dessus du verre garde la musique douce et les voix calmes.',
     'Zero echo! Wood above the glass keeps music soft and voices calm.'),
    ('claire',
     "Alors le café de Nadia et le piano d'Odette ne vont pas réveiller les clients d'en haut?",
     "So Nadia's café and Odette's piano won't wake the guests upstairs?"),
    ('antoine',
     "Pas du tout: ce mur de brique épais bloque tous les bruits de l'escalier.",
     'Not at all: this thick brick wall blocks every sound from the stairs.'),
    ('thibault',
     "J'ai tout le week-end libre, loin de la mairie, Claire. Donnez-nous du travail!",
     'I have the whole weekend free, far from City Hall, Claire. Put us to work!'),
    ('claire',
     'Vous pouvez porter les tables de la cave après le déjeuner?',
     'Can you carry the tables up from the cellar after lunch?'),
    ('thibault',
     "Avec plaisir! Travailler avec Antoine, c'est mieux qu'un bureau.",
     'With pleasure! Working with Antoine beats an office.'),
    ('antoine',
     "D'abord, je dessine les loquets des fenêtres, pour faire entrer l'air frais de la cour.",
     'First, I am sketching the window latches, to let fresh air in from the courtyard.'),
]
WALK = [
    (1, None,
     ["'My little brother grabbed his tape measure before finishing his toast.' Thibault's",
      (None, 'son mètre'),
      "is the same word as 'metre', and it also names the tape measure itself."]),
    (2, 'Entrez, tous les deux!',
     ["'Come in, both of you!' The chunk",
      (None, 'tous les deux'),
      "literally 'all the two', is how French says 'both'."]),
    (3, None,
     "'Four metres wide, six long, brick wall on the left, wooden ceiling.' French measures 'four metres of "
     "wide': first the number, then a little 'of', then the width."),
    (4, None,
     ["'Listen how quiet the street is when you clap your hands once.' To his brother, Thibault says",
      (None, 'Écoute'),
      "the casual command; with Claire he switches to the polite form."]),
    (6, None,
     ["'So Nadia's cafe and Odette's piano won't wake the guests upstairs?' The upstairs guests are",
      (None, "les clients d'en haut"),
      "literally 'the guests from up high'."]),
    (7, None,
     ["'Not at all: this thick brick wall blocks every sound from the stairs.' Antoine's",
      (None, 'Pas du tout'),
      "is a firm but friendly 'not at all', literally 'not of the whole'."]),
    (10, None,
     ["'With pleasure! Working with Antoine beats an office.'",
      (None, 'Avec plaisir'),
      "word for word 'with pleasure', is the warmest way to say yes to a favour."]),
]
