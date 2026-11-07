# Authoring module for hotel-du-tilleul-s02e01-scene-06.
ID = 'hotel-du-tilleul-s02e01-scene-06'
SHOW = 'hotel-du-tilleul'
SEASON = 2
EPISODE = 1
SCENE = 6
TITLE = 'Cartes postales de mai  (Postcards from May)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'nadia': 'Nadia', 'odette': 'Odette', 'henri': 'Henri'}
INTRO = ('Back at the four-table cafe corner while Claire answers the front-desk phone, Nadia pours fresh tea for '
         'Odette and Henri as they spread the old postcards from the cedar chest across the table. '
         "Let's listen in first.")
OPENER = "Let's read those old postcards again, card by card."
TRANSITION = "Now let's hear the whole scene again from the beginning."
OUTRO = ('Thirty years ago Room 9 welcomed the street every Friday at six, and now Nadia, Odette and Henri are '
         'ready to bring the tradition back. See you next time.')
CLOSING = ('nadia', 'À plus!')
STORY = [
    ('nadia',
     'Regardez cette photo en noir et blanc de notre tilleul: il arrivait seulement au premier étage!',
     'Look at this black-and-white photo of our linden tree: it only reached the first floor!'),
    ('henri',
     'Lisez le dos de cette carte postale bleue, madame.',
     'Read the back of that blue postcard, madam.'),
    ('odette',
     'Le dix mai, il y a trente ans. Thé et piano dans la chambre neuf, chaque vendredi à six heures.',
     'May tenth, thirty years ago. Tea and piano in Room Nine, every Friday at six.'),
    ('nadia',
     'Chaque vendredi à six heures! Toute la rue venait ici pour le thé et la musique!',
     'Every Friday at six! The whole street came here for tea and music!'),
    ('henri',
     'Regardez la carte suivante: gardez deux chaises du coin pour la boulangère et le professeur.',
     'Look at the next card: save two corner chairs for the baker and the teacher.'),
    ('odette',
     "Comme c'est joli: cette maison rassemblait déjà les voisins il y a trente ans.",
     'How lovely: this house was already bringing neighbours together thirty years ago.'),
    ('nadia',
     "Et vendredi prochain, c'est le premier vendredi du mois!",
     'And next Friday is the first Friday of the month!'),
    ('henri',
     'Attends: tu veux rouvrir la chambre neuf vendredi prochain à six heures?',
     'Wait: you want to reopen Room Nine next Friday at six?'),
    ('nadia',
     'Six jours pour laver les vitres, peindre les volets et faire des tartes au citron!',
     'Six days to wash the windows, paint the shutters and bake lemon tarts!'),
    ('odette',
     'Si vous réveillez cette touche muette, Henri, je joue volontiers à six heures.',
     'If you wake up that silent key, Henri, I will gladly play at six.'),
    ('henri',
     'Marché conclu! Allons dire notre plan du vendredi à Claire et Étienne!',
     "Deal! Let's go tell Claire and Etienne our Friday plan!"),
    ('nadia',
     'Prends la carte postale: Étienne va voir cette photo et il va dire oui!',
     'Bring the postcard: Etienne is going to see this photo and say yes!'),
]
WALK = [
    (0, None,
     "'Look at this black-and-white photo of our linden tree: it only reached the first floor!' Careful: in "
     "France the first floor is one floor up, because street level has its own name, the ground floor."),
    (1, None,
     ["'Read the back of that blue postcard, madam.' The back of a card is",
      (None, 'le dos'),
      "the same word as the back of your body."]),
    (2, 'Thé et piano dans la chambre neuf, chaque vendredi à six heures.',
     "'Tea and piano in Room Nine, every Friday at six.' To say 'every Friday', French simply says 'each "
     "Friday', and it needs no 'on' in front."),
    (7, None,
     ["'Wait: you want to reopen Room Nine next Friday at six?' Henri builds",
      (None, 'rouvrir'),
      "from the word for 'open' with a little re- in front, just like English 'reopen'."]),
    (8, None,
     "'Six days to wash the windows, paint the shutters and bake lemon tarts!' Nadia's tarts are literally "
     "'tarts at the lemon': French names a flavour with a small 'at the'."),
    (9, None,
     ["'If you wake up that silent key, Henri, I will gladly play at six.'",
      (None, 'volontiers'),
      "is a lovely one-word 'gladly', a little more elegant than 'with pleasure'."]),
    (10, 'Marché conclu!',
     "'Deal!' Literally 'market concluded': a deal is sealed the way you'd shake hands at a market stall."),
]
