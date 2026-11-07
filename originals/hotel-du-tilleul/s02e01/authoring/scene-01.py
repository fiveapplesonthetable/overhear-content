# Authoring module for hotel-du-tilleul-s02e01-scene-01.
ID = 'hotel-du-tilleul-s02e01-scene-01'
SHOW = 'hotel-du-tilleul'
SEASON = 2
EPISODE = 1
SCENE = 1
TITLE = 'La neuvième clé  (The Ninth Key)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'claire': 'Claire', 'henri': 'Henri', 'etienne': 'Étienne'}
INTRO = ("It is early Saturday morning at the Hotel du Tilleul in Lyon, just hours after Henri carried a dusty "
         "cedar box stamped 'Room 9' up from the cellar. Claire and Etienne lean over the front desk as Henri "
         'turns the tiny brass key. Listen to the scene first.')
OPENER = "Let's open the cedar box again, one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = ('Inside the cedar box sits a heavy door key and a floor plan pointing straight behind the hallway '
         "bookcase. Don't worry if a word or two went past quickly; they return right away. See you next time.")
CLOSING = ('claire', 'À bientôt!')
STORY = [
    ('etienne',
     'Tournez la petite clé doucement, Henri: mon cœur bat très vite!',
     'Turn the little key slowly, Henri: my heart is beating really fast!'),
    ('henri',
     'Du calme, patron. Une serrure en laiton de la cave ne casse jamais.',
     'Relax, boss. A brass lock from the cellar never breaks.'),
    ('claire',
     'Ça a fait clic! Soulevez le couvercle en bois, Henri!',
     'It clicked! Lift the wooden lid, Henri!'),
    ('henri',
     'Dedans, il y a une grande clé de porte, un plan bleu et des cartes postales.',
     'Inside there is a big door key, a blue plan and some postcards.'),
    ('etienne',
     'Lisez le haut de ce papier bleu plié! Où sont mes lunettes?',
     'Read the top of that folded blue paper! Where are my glasses?'),
    ('claire',
     'Toujours sur votre front, Étienne, là où vous les avez laissées hier soir.',
     'Still on your forehead, Etienne, right where you left them last night.'),
    ('etienne',
     'Ah! Regardez ici: rez-de-chaussée, chambre neuf, jardin d\'hiver!',
     'Aha! Look here: ground floor, Room Nine, garden sunroom!'),
    ('claire',
     'Attendez, on a un jardin d\'hiver au rez-de-chaussée?',
     'Wait, we have a garden sunroom on the ground floor?'),
    ('henri',
     'Regardez la flèche derrière la bibliothèque du couloir du fond.',
     'Look at the arrow behind the bookcase in the back hallway.'),
    ('etienne',
     'Cette lourde bibliothèque en bois est contre ce mur depuis vingt ans!',
     'That heavy wooden bookcase has stood against that wall for twenty years!'),
    ('claire',
     'Alors derrière ces vieux livres, il y a une neuvième porte!',
     'So behind those old books, there is a ninth door!'),
    ('henri',
     "D'abord une gorgée de café, ensuite on déplace les livres.",
     'First a sip of coffee, then we move the books.'),
]
WALK = [
    (0, 'Tournez la petite clé doucement, Henri: mon cœur bat très vite!',
     ["'Turn the little key slowly, Henri: my heart is beating really fast!' Etienne says",
      (None, 'mon cœur bat'),
      "which is simply 'my heart beats'. French has no separate 'is beating' form, so one short present does the job."]),
    (1, 'Du calme, patron.',
     ["'Relax, boss.' Henri's",
      (None, 'Du calme'),
      "is literally 'some calm', a two-word way to settle down a nervous person."]),
    (2, 'Ça a fait clic!',
     "'It clicked!' French doesn't turn the sound into a verb the way English does; the lock literally "
     "'made click'."),
    (3, None,
     ["'Inside there is a big door key, a blue plan and some postcards.' Listen for",
      (None, 'il y a'),
      "the everyday chunk for 'there is' and 'there are', used for one key or for a whole pile of cards."]),
    (5, None,
     "'Still on your forehead, Etienne, right where you left them last night.' In French, glasses are always "
     "plural and feminine, so 'left them' takes an extra -es at the end of the written word."),
    (7, None,
     ["'Wait, we have a garden sunroom on the ground floor?' A glass sunroom is a",
      (None, "jardin d'hiver"),
      "literally a 'winter garden', a warm place for plants when it's cold outside."]),
    (9, None,
     ["'That heavy wooden bookcase has stood against that wall for twenty years!' Watch out:",
      (None, 'bibliothèque'),
      "means both a bookcase and a library. A shop that sells books has a different name altogether."]),
]
