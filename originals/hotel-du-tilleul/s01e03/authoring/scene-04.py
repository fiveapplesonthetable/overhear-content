# Authoring module for hotel-du-tilleul-s01e03-scene-04.
ID = 'hotel-du-tilleul-s01e03-scene-04'
SHOW = 'hotel-du-tilleul'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = 'Sous la pluie  (In from the Rain)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'claire': 'Claire', 'antoine': 'Antoine', 'nadia': 'Nadia'}
INTRO = ('Down in the lobby, quiet traveller Antoine steps inside shaking out a wet umbrella. Claire '
 'greets him at the desk while Nadia brings a warm towel. Listen first.')
OPENER = "Let's hear how Claire welcomes Antoine and explains the room mix-up honestly."
TRANSITION = "Now let's hear the whole conversation again from the beginning."
OUTRO = ('Honesty, a dry towel, and a cup of hot soup kept the conversation calm. Next time, Antoine '
 'climbs the stairs to judge the attic room for himself.')
CLOSING = ('antoine', "À tout à l'heure!")
STORY = [('claire',
  "Bonsoir! Entrez vite à l'abri de la pluie, monsieur.",
  'Good evening! Come quickly inside out of the rain, sir.'),
 ('antoine',
  "Bonsoir. Pardon pour l'eau sur votre sol propre.",
  'Good evening. Sorry for the water on your clean floor.'),
 ('claire',
  "Ce n'est rien du tout! Vous devez être Monsieur Antoine.",
  'It is nothing at all! You must be Mr Antoine.'),
 ('antoine',
  "Oui, Antoine. J'ai réservé la chambre sept par téléphone hier.",
  'Yes, Antoine. I booked room seven by phone yesterday.'),
 ('nadia',
  'Voici une serviette sèche pour votre manteau et un bol de soupe chaude, monsieur.',
  'Here is a dry towel for your coat and a bowl of hot soup, sir.'),
 ('antoine',
  "De la soupe chaude? Après le quai froid de la gare, c'est merveilleux.",
  'Hot soup? After the cold station platform, that is wonderful.'),
 ('claire',
  'Monsieur, avant de monter, je vous dois des excuses sincères.',
  'Sir, before going upstairs, I owe you an honest apology.'),
 ('antoine',
  'Ah bon? Il y a un problème avec ma réservation?',
  'Oh really? Is there a problem with my booking?'),
 ('claire',
  'Nous avons noté deux réservations pour la chambre sept par erreur ce soir.',
  'We wrote two bookings for room seven by mistake tonight.'),
 ('antoine',
  'Oh... sous cette pluie? Tous les hôtels près de la gare affichaient complet.',
  'Oh... in this rain? Every hotel near the station had a full sign.'),
 ('claire',
  'Rassurez-vous! Nous avons préparé notre chambre calme sous les toits juste pour vous.',
  'Rest assured! We prepared our quiet attic room just for you.'),
 ('antoine',
  "Une chambre sous les toits? Je peux la voir d'abord?",
  'An attic room? May I see it first?')]
WALK = [(0,
  "Entrez vite à l'abri de la pluie, monsieur.",
  ["'Come quickly inside out of the rain, sir.' The welcoming phrase",
   (None, "à l'abri"),
   "means 'into shelter', safe from wind or rain."]),
 (2,
  "Ce n'est rien du tout!",
  "'It is nothing at all!' Adding 'of all' onto 'it is nothing' makes a handy phrase to brush away "
  "a guest's apology."),
 (3,
  "J'ai réservé la chambre sept par téléphone hier.",
  "'I booked room seven by phone yesterday.' In French, methods of communication like phone or "
  "post take 'by', literally 'by telephone'."),
 (4,
  None,
  ["'Here is a dry towel for your coat and a bowl of hot soup, sir.' Hear the feminine form",
   (None, 'sèche'),
   "for 'dry' describing the feminine towel, with a soft 'sh' sound at the end."]),
 (7,
  'Ah bon? Il y a un problème avec ma réservation?',
  ["'Oh really? Is there a problem with my booking?' Two tiny words,",
   (None, 'Ah bon?'),
   "literally 'oh good?', mean 'oh really?' even when the news is not good at all!"]),
 (10,
  'Rassurez-vous!',
  "'Rest assured!' Literally 'reassure yourself', a calmer, warmer cousin of 'do not worry'."),
 (11,
  "Je peux la voir d'abord?",
  "'May I see it first?' Because 'room' is feminine, 'it' is feminine too and sits right before "
  "'see'.")]
