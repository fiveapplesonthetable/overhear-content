# Authoring module for hotel-du-tilleul-s02e01-scene-02.
ID = 'hotel-du-tilleul-s02e01-scene-02'
SHOW = 'hotel-du-tilleul'
SEASON = 2
EPISODE = 1
SCENE = 2
TITLE = 'On déplace les livres  (Move the Books)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'claire': 'Claire', 'nadia': 'Nadia', 'henri': 'Henri'}
INTRO = ('In the quiet back hallway behind the kitchen, Claire and Henri stand before a tall wooden bookcase '
         'packed with old travel guides. Nadia hurries out of the cafe corner wiping flour from her hands. '
         "Let's listen in first.")
OPENER = "Let's go back down the hallway and unpack the bookcase line by line."
TRANSITION = "Now let's hear the whole scene again without stopping."
OUTRO = ('The heavy bookcase is aside and the hidden lock turns cleanly on the first try. Notice how naturally '
         'those action words, lift, pull, turn, open, fit together. See you next time.')
CLOSING = ('nadia', 'Bonne journée!')
STORY = [
    ('nadia',
     "C'est vrai? Il y a vraiment une pièce secrète derrière le mur de ma cuisine?",
     'Is it true? Is there really a secret room behind my kitchen wall?'),
    ('claire',
     'Aide-moi à poser ces gros livres verts sur la chaise, Nadia.',
     'Help me put these big green books on the chair, Nadia.'),
    ('henri',
     "Prenez d'abord l'étagère du haut, comme ça le bois devient léger.",
     'Take the top shelf first, that way the wood gets light.'),
    ('nadia',
     'Ces guides de voyage sont plus vieux que nous deux, Claire!',
     'These travel guides are older than both of us, Claire!'),
    ('claire',
     "C'est la dernière étagère. Prêt à tirer à trois, Henri?",
     'That is the last shelf. Ready to pull on three, Henri?'),
    ('henri',
     'Un, deux, trois! Glissez le côté gauche vers moi!',
     'One, two, three! Slide the left side toward me!'),
    ('nadia',
     'Regardez derrière le bois! De la peinture blanche et une serrure en laiton!',
     'Look behind the wood! White paint and a brass lock!'),
    ('claire',
     'Une vraie porte, cachée ici, dans le couloir!',
     'A real door, hidden right here in the hallway!'),
    ('henri',
     'Essayons la grande clé du coffre en cèdre.',
     "Let's try the big key from the cedar chest."),
    ('nadia',
     'Elle tourne, Henri?',
     'Does it turn, Henri?'),
    ('henri',
     'Un tour ferme vers la droite... et le loquet est ouvert!',
     'One firm turn to the right... and the latch is open!'),
    ('claire',
     "Soulevez d'abord la poignée, comme pour la porte d'entrée!",
     'Lift the handle first, just like with the front door!'),
]
WALK = [
    (0, "Il y a vraiment une pièce secrète derrière le mur de ma cuisine?",
     ["'Is there really a secret room behind my kitchen wall?' For a room in a house, Nadia uses",
      (None, 'une pièce'),
      "the general word for any room in a home; a hotel bedroom has its own word."]),
    (1, None,
     ["'Help me put these big green books on the chair, Nadia.' Claire speaks to her friend with",
      (None, 'Aide-moi'),
      "the casual 'you' command; to Henri she would say the longer, polite version."]),
    (3, None,
     ["'These travel guides are older than both of us, Claire!' The chunk",
      (None, 'plus vieux que'),
      "works like 'older than': swap in any other adjective after 'plus' to compare things."]),
    (4, 'Prêt à tirer à trois, Henri?',
     "'Ready to pull on three, Henri?' French counts 'at three', so a countdown always ends with a little "
     "word for 'at' before the number."),
    (5, 'Glissez le côté gauche vers moi!',
     ["'Slide the left side toward me!' The tiny word",
      (None, 'vers moi'),
      "means 'toward me'; Henri points the whole bookcase in his own direction."]),
    (9, None,
     "'Does it turn, Henri?' Nadia says 'she turns', because a key is feminine in French, so every 'it' for "
     "the key becomes 'she'."),
    (11, None,
     ["'Lift the handle first, just like with the front door!' The front door is",
      (None, "la porte d'entrée"),
      "literally 'the door of entry', and it still sticks unless you lift the handle."]),
]
