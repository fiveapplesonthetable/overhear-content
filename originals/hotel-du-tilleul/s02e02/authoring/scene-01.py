# Authoring module for hotel-du-tilleul-s02e02-scene-01.
ID = 'hotel-du-tilleul-s02e02-scene-01'
SHOW = 'hotel-du-tilleul'
SEASON = 2
EPISODE = 2
SCENE = 1
TITLE = 'Deux paniers et une liste  (Two Baskets and a List)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'claire': 'Claire', 'nadia': 'Nadia', 'henri': 'Henri'}
INTRO = ('Twenty minutes after the fuse pop at the Hotel du Tilleul, kitchen power is back on and Henri is measuring '
         'copper wire in the courtyard. Claire and Nadia step out into the bright Saturday air with two market '
         'baskets. Listen first.')
OPENER = "Let's check that shopping list again with Henri."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = ('With baskets in hand and black tape added in pencil, Claire and Nadia head for the Saturday market, while '
         'Etienne makes a phone order with nobody watching. See you next time.')
CLOSING = ('nadia', 'À tout à l\'heure!')
STORY = [
    ('nadia',
     'Le four est de nouveau chaud! Tu as sauvé mon pain du samedi, Henri.',
     'The oven is hot again! You saved my Saturday bread, Henri.'),
    ('henri',
     "Gardez juste les doigts d'Étienne loin des interrupteurs jusqu'à ce soir.",
     "Just keep Etienne's fingers away from the switches until this evening."),
    ('claire',
     'Pendant que vous réparez la chambre neuf, Nadia et moi, on va au marché du samedi.',
     'While you fix Room Nine, Nadia and I are going to the Saturday market.'),
    ('henri',
     'Vous avez une liste écrite, ou vous achetez la moitié de la place?',
     'Do you have a written list, or are you buying half the square?'),
    ('claire',
     'Elle est ici, sur papier, Henri: douze tasses blanches, des citrons frais et du miel de la région.',
     'Right here on paper, Henri: twelve white cups, fresh lemons and local honey.'),
    ('nadia',
     'Et aussi quatre pots de confiture et des herbes fraîches pour la cour!',
     'And also four jars of jam and fresh herbs for the courtyard!'),
    ('henri',
     'Bien. Prenez aussi un rouleau de ruban isolant noir au stand de bricolage.',
     'Good. Also pick up a roll of black electrical tape at the hardware stall.'),
    ('claire',
     "Un rouleau de ruban isolant noir: c'est écrit au crayon!",
     "One roll of black electrical tape: it's written down in pencil!"),
    ('henri',
     'Vous apprenez vite, Claire. Prenez la petite caisse sur le comptoir.',
     'You learn fast, Claire. Take the petty cash box from the desk.'),
    ('nadia',
     'Viens, Claire, avant que les plus beaux citrons jaunes disparaissent!',
     'Come on, Claire, before the best yellow lemons disappear!'),
    ('claire',
     'On a besoin de chaises en plus au marché, Henri?',
     'Do we need extra chairs from the market, Henri?'),
    ('henri',
     "Étienne dit qu'il commande six chaises pliantes par téléphone... souhaitez-nous bonne chance.",
     'Etienne says he is ordering six folding chairs by phone... wish us luck.'),
]
WALK = [
    (0, 'Le four est de nouveau chaud!',
     ["'The oven is hot again!' Nadia's",
      (None, 'de nouveau'),
      "literally 'of new', is a handy way to say 'again'."]),
    (2, None,
     ["'While you fix Room Nine, Nadia and I are going to the Saturday market.' Claire says",
      (None, 'Nadia et moi, on va'),
      "literally 'Nadia and me, one goes': spoken French loves this relaxed way of saying 'we'."]),
    (3, None,
     ["'Do you have a written list, or are you buying half the square?' Henri teases with",
      (None, 'la moitié de la place'),
      "'half of the square'; a town square shares its name with a seat or a free spot."]),
    (4, None,
     ["'Right here on paper, Henri: twelve white cups, fresh lemons and local honey.' Claire's",
      (None, 'du miel de la région'),
      "is 'honey from the region', the usual way to say local food in France."]),
    (7, None,
     ["'One roll of black electrical tape: it's written down in pencil!' For pencil, Claire says",
      (None, 'au crayon'),
      "'at the pencil': French writes 'at the pen' or 'at the pencil' rather than 'in'."]),
    (8, 'Prenez la petite caisse sur le comptoir.',
     ["'Take the petty cash box from the desk.' A shop's",
      (None, 'la petite caisse'),
      "literally 'the little till', is the box of coins for small purchases."]),
    (11, None,
     ["'Etienne says he is ordering six folding chairs by phone... wish us luck.' Henri's",
      (None, 'souhaitez-nous bonne chance'),
      "is a ready-made chunk: wish someone 'good chance' and you have wished them luck."]),
]
