# Authoring module for hotel-du-tilleul-s02e02-scene-08.
ID = 'hotel-du-tilleul-s02e02-scene-08'
SHOW = 'hotel-du-tilleul'
SEASON = 2
EPISODE = 2
SCENE = 8
TITLE = "L'écriture de ma tante  (Ask My Aunt's Ledger)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'etienne': 'Étienne', 'claire': 'Claire', 'odette': 'Odette'}
INTRO = ('At the front desk as Saturday evening settles in, Claire and Odette lay the handwritten sheet of music '
         'under the desk lamp in front of Etienne. Listen first.')
OPENER = "Let's look at that handwriting again with Etienne."
TRANSITION = "Now let's hear the whole conversation again from the start."
OUTRO = ("The unfinished waltz belonged to Etienne's aunt, and the City Hall heritage visit just jumped forward "
         'from Friday to Wednesday at three! Episode 2 is complete, see you in Episode 3.')
CLOSING = ('etienne', 'Bonne nuit!')
STORY = [
    ('claire',
     'Étienne, regardez ce qui était caché dans le piano droit de la chambre neuf!',
     'Etienne, look what was hidden inside the upright piano in Room Nine!'),
    ('etienne',
     'De la musique écrite à la main? Je baisse mes lunettes... attendez une seconde!',
     'Handwritten music? Let me pull my glasses down... wait a second!'),
    ('odette',
     'Vous savez qui a écrit la Valse de la cour il y a trente ans, Étienne?',
     'Do you know who wrote the Courtyard Waltz thirty years ago, Etienne?'),
    ('etienne',
     "Regardez ces grandes lettres rondes: c'est l'écriture de ma tante!",
     "Look at those big round letters: that is my aunt's handwriting!"),
    ('claire',
     'Votre tante jouait du piano et tenait le salon de thé du vendredi?',
     'Your aunt played the piano and ran the Friday tea room?'),
    ('etienne',
     'Elle faisait des gâteaux le matin et elle écrivait des petites chansons le soir!',
     'She baked cakes in the morning and wrote little songs in the evening!'),
    ('odette',
     "Pourquoi elle s'est arrêtée au milieu de la page deux, en mai, il y a trente ans?",
     'Why did she stop in the middle of page two, in May, thirty years ago?'),
    ('etienne',
     "Son vieux livre d'or vert de ce printemps-là est encore dans le coffre du grenier!",
     'Her old green guest book from that spring is still in the attic chest!'),
    ('claire',
     'Attendez, le téléphone de la réception clignote: il y a un message vocal.',
     'Wait, the front desk phone is blinking: there is a voice message.'),
    ('etienne',
     'Écoutez-le, Claire! Qui appelle un samedi soir?',
     'Play it, Claire! Who calls on a Saturday evening?'),
    ('claire',
     "C'est la mairie, le service du patrimoine. Leur visite du café est maintenant mercredi à trois heures!",
     'It is City Hall, the heritage office. Their café visit is now Wednesday at three!'),
    ('etienne',
     'Mercredi à trois heures? Ça nous donne trois jours au lieu de six!',
     'Wednesday at three? That gives us three days instead of six!'),
]
WALK = [
    (1, None,
     ["'Handwritten music? Let me pull my glasses down... wait a second!' Etienne's",
      (None, 'Je baisse mes lunettes'),
      "uses the word for 'lower', the same one you use for turning a radio down."]),
    (3, None,
     ["'Look at those big round letters: that is my aunt's handwriting!' Etienne's",
      (None, "l'écriture de ma tante"),
      "is 'the writing of my aunt': French has no 's to show who owns something."]),
    (4, None,
     ["'Your aunt played the piano and ran the Friday tea room?' French plays 'of the piano':",
      (None, 'jouait du piano'),
      "takes a little 'of the' for instruments, while sports and games take 'at the'."]),
    (5, None,
     "'She baked cakes in the morning and wrote little songs in the evening!' For things someone used to do "
     "again and again, French reaches for one special past form, and you hear it twice in this line."),
    (7, None,
     ["'Her old green guest book from that spring is still in the attic chest!' A hotel guest book is a",
      (None, "livre d'or"),
      "literally a 'book of gold'."]),
    (8, None,
     ["'Wait, the front desk phone is blinking: there is a voice message.'",
      (None, 'clignote'),
      "is the word for blinking lights, and for a car's indicator too."]),
    (11, None,
     ["'Wednesday at three? That gives us three days instead of six!' Etienne's",
      (None, 'au lieu de six'),
      "uses 'in the place of' to mean 'instead of', a handy chunk for any change of plan."]),
]
