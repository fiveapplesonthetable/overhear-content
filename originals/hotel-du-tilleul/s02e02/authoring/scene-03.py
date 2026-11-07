# Authoring module for hotel-du-tilleul-s02e02-scene-03.
ID = 'hotel-du-tilleul-s02e02-scene-03'
SHOW = 'hotel-du-tilleul'
SEASON = 2
EPISODE = 2
SCENE = 3
TITLE = 'Douze tasses blanches  (Twelve White Cups)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'claire': 'Claire', 'nadia': 'Nadia', 'antoine': 'Antoine'}
INTRO = ('At the sunny corner of the market square, Antoine is sketching an arched stone doorway when Claire and '
         'Nadia arrive at the ceramic table. Listen to the whole scene first.')
OPENER = "Let's pick up those cups again and listen closely."
TRANSITION = "Now let's listen to the whole scene again from the start."
OUTRO = ("Twelve thick stoneware cups, quiet saucers and a matching milk jug are wrapped in paper, with Henri's "
         'black tape remembered too. See you next time.')
CLOSING = ('nadia', 'Bonne journée!')
STORY = [
    ('claire',
     'Regarde toutes ces tasses, Nadia: des mugs bleus, des tasses en verre, des bols blancs!',
     'Look at all these cups, Nadia: blue mugs, glass cups, white bowls!'),
    ('nadia',
     'Les tasses fines sont jolies, Claire, mais le thé refroidit en trois minutes.',
     'Thin cups look pretty, Claire, but tea goes cold in three minutes.'),
    ('antoine',
     "Essayez le grès blanc crème, bien épais, sur l'étagère de gauche.",
     'Try the thick cream-white stoneware on the left shelf.'),
    ('claire',
     'Oh, bonjour, Antoine! Votre frère est juste derrière nous, avec le miel.',
     'Oh, hello, Antoine! Your brother is right behind us, with the honey.'),
    ('antoine',
     "Touchez l'anse de cette tasse: l'argile épaisse garde la chaleur et ne s'abîme pas facilement.",
     "Feel the handle of this cup: thick clay holds the heat and doesn't chip easily."),
    ('nadia',
     'Et écoutez ce petit bruit doux quand on la pose sur la soucoupe!',
     'And listen to that soft little clink when you set it on the saucer!'),
    ('antoine',
     "Des soucoupes calmes, et les clients entendent le piano d'Odette dans toute la pièce.",
     "Quiet saucers, and the guests hear Odette's piano across the whole room."),
    ('claire',
     'Même pour des tasses, Antoine pense comme un architecte acoustique!',
     'Even for cups, Antoine thinks like an acoustic architect!'),
    ('nadia',
     'Si on achète douze tasses et douze soucoupes ensemble, il y a une réduction?',
     'If we buy twelve cups and twelve saucers together, is there a discount?'),
    ('claire',
     'Regarde le panneau à la craie: la douzaine est moins chère!',
     'Look at the chalk sign: a dozen is cheaper!'),
    ('antoine',
     'Et un pot à lait blanc assorti en plus. Emballez-les dans du papier journal.',
     'And a matching white milk jug on top. Wrap them in newspaper.'),
    ('nadia',
     "Emballé et payé! N'oublie pas le ruban noir d'Henri sur le chemin du retour!",
     "Wrapped and paid! Don't forget Henri's black tape on the way home!"),
]
WALK = [
    (1, None,
     ["'Thin cups look pretty, Claire, but tea goes cold in three minutes.' Nadia's",
      (None, 'le thé refroidit'),
      "packs 'goes cold' into one word, built from the word for 'cold' with re- in front."]),
    (2, None,
     ["'Try the thick cream-white stoneware on the left shelf.' Antoine says",
      (None, "l'étagère de gauche"),
      "'the shelf of left': left and right follow the noun with a little 'of'."]),
    (4, None,
     ["'Feel the handle of this cup: thick clay holds the heat and doesn't chip easily.' A cup handle has its "
      "own name,",
      (None, "l'anse"),
      "different from the door handle you heard in the hallway."]),
    (5, None,
     "'And listen to that soft little clink when you set it on the saucer!' Nadia says 'when one sets it': "
     "French often uses 'one' where English says 'you' for everybody."),
    (7, None,
     ["'Even for cups, Antoine thinks like an acoustic architect!' The chunk",
      (None, 'pense comme'),
      "means 'thinks like'; the small word for 'like' slots in before the comparison, just as in English."]),
    (8, None,
     ["'If we buy twelve cups and twelve saucers together, is there a discount?' A shop discount is",
      (None, 'une réduction'),
      "easy to remember, since it reduces the price."]),
    (10, None,
     ["'And a matching white milk jug on top. Wrap them in newspaper.' Wrapping paper from old news is",
      (None, 'du papier journal'),
      "literally 'newspaper paper'."]),
]
