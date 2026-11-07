# Authoring module for hotel-du-tilleul-s02e01-scene-04.
ID = 'hotel-du-tilleul-s02e01-scene-04'
SHOW = 'hotel-du-tilleul'
SEASON = 2
EPISODE = 1
SCENE = 4
TITLE = 'Sous le drap blanc  (Under the White Sheet)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'claire': 'Claire', 'odette': 'Odette', 'henri': 'Henri'}
INTRO = ('Hearing excited voices down the hall, Room 4 guest Odette walks over with her morning teacup just as '
         'Claire and Henri reach the tall shape under the white cloth. Listen first.')
OPENER = "Let's lift that white sheet again and listen closely."
TRANSITION = "Now let's hear the whole conversation again."
OUTRO = ('Beneath the dust sheet stands a warm walnut piano with eighty-seven working keys and one silent middle '
         'note. See you in the next scene.')
CLOSING = ('odette', 'Bonne journée!')
STORY = [
    ('odette',
     'Bonjour! Pourquoi tout le monde est dans le mur du couloir?',
     'Good morning! Why is everyone standing inside the hallway wall?'),
    ('claire',
     'Venez voir, Odette! On a trouvé la chambre neuf!',
     'Come and see, Odette! We found Room Nine!'),
    ('odette',
     'Oh là là, regardez ces fenêtres en arc! Je peux entrer?',
     'Goodness, look at those arched windows! May I come in?'),
    ('henri',
     'Attention à la marche poussiéreuse, madame. Aidez-moi à plier ce drap blanc.',
     'Mind the dusty step, madam. Help me fold this white sheet.'),
    ('claire',
     'Un, deux... oh! Regardez ce bois foncé et brillant!',
     'One, two... oh! Look at this dark, shiny wood!'),
    ('odette',
     'Un piano droit! Un vrai piano droit en noyer!',
     'An upright piano! A real walnut upright piano!'),
    ('henri',
     "Attention au couvercle: il est fermé depuis des dizaines d'années.",
     'Careful with the lid: it has been closed for decades.'),
    ('odette',
     'Regardez les touches en ivoire, Claire. Elles sont propres et entières.',
     'Look at the ivory keys, Claire. They are clean and whole.'),
    ('claire',
     'Allez-y, Odette: jouez un accord pour la maison!',
     'Go ahead, Odette: play a chord for the house!'),
    ('odette',
     'Écoutez... un peu grave, très chaud, et attendez: le ré du milieu ne fait aucun son!',
     'Listen... a little low, very warm, and wait: the middle D makes no sound!'),
    ('henri',
     'Toutes les touches chantent, sauf une note têtue au milieu?',
     'Every key sings except one stubborn note in the middle?'),
    ('odette',
     'Donnez une bonne réparation à un vieux piano, Henri, et il se souvient de chaque chanson.',
     'Give an old piano one good repair, Henri, and it remembers every song.'),
]
WALK = [
    (1, None,
     ["'Come and see, Odette! We found Room Nine!'",
      (None, 'Venez voir'),
      "is literally 'come see': two commands back to back, with no 'and' in between."]),
    (2, 'Je peux entrer?',
     "'May I come in?' Just three words, literally 'I can enter?'. French makes a polite question here simply "
     "by raising the voice at the end."),
    (3, 'Attention à la marche poussiéreuse, madame.',
     ["'Mind the dusty step, madam.' Henri's",
      (None, 'Attention à'),
      "literally 'attention to', is the everyday way to say 'mind' or 'watch out for'."]),
    (5, None,
     ["'An upright piano! A real walnut upright piano!' In French an upright is",
      (None, 'Un piano droit'),
      "literally a 'straight piano', standing tall against the wall."]),
    (6, None,
     ["'Careful with the lid: it has been closed for decades.' Henri says",
      (None, "des dizaines d'années"),
      "literally 'tens of years', the usual French way to talk about decades."]),
    (9, None,
     ["'Listen... a little low, very warm, and wait: the middle D makes no sound!' Odette calls the note",
      (None, 'le ré du milieu'),
      "because French musicians sing note names, do, re, mi, instead of using letters."]),
    (11, None,
     "'Give an old piano one good repair, Henri, and it remembers every song.' Odette's advice has a handy "
     "shape: a command, then 'and', then the happy result. Swap in your own advice for the piano."),
]
