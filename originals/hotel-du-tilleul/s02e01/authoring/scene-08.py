# Authoring module for hotel-du-tilleul-s02e01-scene-08.
ID = 'hotel-du-tilleul-s02e01-scene-08'
SHOW = 'hotel-du-tilleul'
SEASON = 2
EPISODE = 1
SCENE = 8
TITLE = "Ne touchez pas l'interrupteur  (Don't Touch That Switch)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'henri': 'Henri', 'etienne': 'Étienne', 'claire': 'Claire'}
INTRO = ('Back at the threshold of Room 9, Henri opens his leather tool bag to inspect the old brass wall switch, '
         'but an excited Etienne reaches past him beside Claire. Listen first.')
OPENER = "Let's slow down that one impatient click."
TRANSITION = "Now let's hear the whole scene again from start to finish."
OUTRO = ('One impatient click from Etienne pops the ground-floor fuse and proves Room 9 needs fresh wiring before '
         'Friday! Episode 1 of Season 2 is complete, see you in Episode 2.')
CLOSING = ('henri', 'Bon courage!')
STORY = [
    ('henri',
     'Attendez une minute avant de toucher cet interrupteur en laiton, patron.',
     'Wait one minute before touching that brass switch, boss.'),
    ('etienne',
     'Pourquoi attendre? Je me souviens de cette lampe en verre: regardez comme elle brille!',
     'Why wait? I remember this glass lamp: watch how it glows!'),
    ('claire',
     'Étienne, attendez! Henri a sorti son tournevis!',
     'Etienne, wait! Henri has his screwdriver out!'),
    ('etienne',
     'Juste un petit clic... pop! Oh non.',
     'Just one little click... pop! Oh no.'),
    ('claire',
     "C'était quoi, ce gros bruit dans le couloir?",
     'What was that loud bang in the hallway?'),
    ('henri',
     "C'est le vieux fil: il a fait sauter le fusible du rez-de-chaussée.",
     'It is the old wire: it blew the ground-floor fuse.'),
    ('etienne',
     "La lampe de l'entrée est éteinte! J'ai aussi cassé le four de la cuisine?",
     'The lobby lamp went out! Did I break the kitchen oven too?'),
    ('claire',
     "Aïe, j'entends Nadia qui appelle depuis la cuisine dans le noir!",
     'Uh-oh, I can hear Nadia calling from the dark kitchen!'),
    ('henri',
     'Du fil en tissu de trente ans, patron. Ne touchez jamais un interrupteur avant moi.',
     'Thirty-year-old cloth wire, boss. Never touch a switch before I do.'),
    ('etienne',
     'Vous pouvez réparer avant le déjeuner, Henri? Dites-moi que vous avez des fusibles de rechange!',
     'Can you fix it before lunch, Henri? Tell me you have spare fuses!'),
    ('henri',
     "La cuisine, deux minutes. Mais la chambre neuf a besoin d'un nouveau fil en cuivre.",
     'The kitchen, two minutes. But Room Nine needs new copper wire.'),
    ('claire',
     'Tenez bien la lampe de poche, Étienne: notre compte à rebours commence vraiment!',
     'Hold the flashlight steady, Etienne: our countdown is really starting!'),
]
WALK = [
    (0, None,
     ["'Wait one minute before touching that brass switch, boss.' The long word",
      (None, 'cet interrupteur'),
      "names a light switch; it comes from 'interrupt', because it cuts the current."]),
    (1, 'Pourquoi attendre?',
     "'Why wait?' Etienne asks 'why' with the plain 'to wait' shape, just two quick words when he's in "
     "a hurry."),
    (3, 'Juste un petit clic... pop!',
     "'Just one little click... pop!' French has sound words too, and these two are spelled almost the "
     "same as in English."),
    (5, None,
     ["'It is the old wire: it blew the ground-floor fuse.' A fuse 'jumps' in French:",
      (None, 'il a fait sauter le fusible'),
      "literally 'it made the fuse jump'."]),
    (7, None,
     ["'Uh-oh, I can hear Nadia calling from the dark kitchen!' Claire's",
      (None, 'Aïe'),
      "is the little cry French speakers use for 'ouch' or 'uh-oh'."]),
    (9, 'Dites-moi que vous avez des fusibles de rechange!',
     ["'Tell me you have spare fuses!' Remember",
      (None, 'de rechange'),
      "from the broken boiler valve? Add it after any part to make it a spare."]),
    (11, None,
     ["'Hold the flashlight steady, Etienne: our countdown is really starting!' A flashlight is",
      (None, 'la lampe de poche'),
      "literally a 'pocket lamp'."]),
]
