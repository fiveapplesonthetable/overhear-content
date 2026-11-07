# Authoring module for hotel-du-tilleul-s02e02-scene-05.
ID = 'hotel-du-tilleul-s02e02-scene-05'
SHOW = 'hotel-du-tilleul'
SEASON = 2
EPISODE = 2
SCENE = 5
TITLE = 'Une montagne de chaises  (A Mountain of Chairs)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'claire': 'Claire', 'nadia': 'Nadia', 'etienne': 'Étienne'}
INTRO = ('Carrying wrapped cups and market baskets, Claire and Nadia push open the courtyard gate, and stop dead in '
         "front of Etienne, who is surrounded by tall stacks of wooden chairs. Let's listen in first.")
OPENER = "Let's climb back over that mountain of chairs, line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = ("Folding the chairs flat clears the courtyard path in minutes and turns Etienne's mistake into neat stacks "
         'under the arch. See you next time.')
CLOSING = ('claire', 'Bonne soirée!')
STORY = [
    ('claire',
     "Étienne? D'où viennent toutes ces chaises en bois?",
     'Etienne? Where did all these wooden chairs come from?'),
    ('nadia',
     "Il y a un mur de chaises du citronnier en pot jusqu'à l'escalier!",
     'There is a wall of chairs from the potted lemon tree all the way to the stairs!'),
    ('etienne',
     "D'abord, la bonne nouvelle: chaque chaise était à moitié prix!",
     'Good news first: every chair was half price!'),
    ('claire',
     'Et quelle est la mauvaise nouvelle, Étienne?',
     'And what is the bad news, Etienne?'),
    ('etienne',
     "J'ai demandé six, j'ai accepté vingt-quatre, et j'ai dit aujourd'hui par erreur!",
     'I asked for six, agreed to twenty-four, and said today by mistake!'),
    ('nadia',
     "Comment nos clients d'en haut vont sortir dans la rue sans grimper sur le bois?",
     'How are our upstairs guests going to get out to the street without climbing over wood?'),
    ('claire',
     'Attendez, regardez comme chaque chaise devient plate quand on appuie sur le loquet!',
     'Wait, look how flat each chair gets when you press the latch!'),
    ('nadia',
     "Oh! Quatre chaises pliées prennent la place d'une seule valise!",
     'Oh! Four folded chairs take up the space of just one suitcase!'),
    ('etienne',
     "C'est vrai? Montrez-moi ce loquet, Claire!",
     'Really? Show me that latch, Claire!'),
    ('claire',
     "On soulève un peu le siège, on plie, et on en range douze sous l'arche, au sec.",
     'We lift the seat a little, we fold, and we put twelve away under the arch, out of the rain.'),
    ('nadia',
     'Et on met douze chaises dans la chambre neuf quand Henri finit la lampe!',
     'And we put twelve chairs in Room Nine when Henri finishes the lamp!'),
    ('etienne',
     'Claire, ma réceptionniste pour de bon, vous me sauvez la vie deux fois en deux jours!',
     'Claire, my receptionist for good, you have saved my life twice in two days!'),
]
WALK = [
    (0, None,
     ["'Etienne? Where did all these wooden chairs come from?'",
      (None, "D'où viennent"),
      "literally 'from where come', puts the 'from' at the front of the question, never at the end like English."]),
    (1, None,
     ["'There is a wall of chairs from the potted lemon tree all the way to the stairs!' A lemon tree is",
      (None, 'du citronnier'),
      "the word for lemon plus -ier, the ending French gives to many fruit trees."]),
    (2, None,
     ["'Good news first: every chair was half price!' Etienne's",
      (None, 'la bonne nouvelle'),
      "is 'the good news', and in French news can be counted: one piece of news, two pieces of news."]),
    (4, None,
     ["'I asked for six, agreed to twenty-four, and said today by mistake!' His",
      (None, 'par erreur'),
      "literally 'by error', is how French says 'by mistake'."]),
    (7, None,
     ["'Oh! Four folded chairs take up the space of just one suitcase!' Nadia's",
      (None, "d'une seule valise"),
      "uses the word for 'single' or 'alone' to mean 'just one'."]),
    (9, None,
     "'We lift the seat a little, we fold, and we put twelve away under the arch, out of the rain.' Claire "
     "repeats the word for 'we' at every step, a friendly way to show how something is done rather than "
     "giving orders."),
    (11, None,
     ["'Claire, my receptionist for good, you have saved my life twice in two days!' The chunk",
      (None, 'pour de bon'),
      "means 'for good', for real and for keeps: Claire's job is permanent now."]),
]
