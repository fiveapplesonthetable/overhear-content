# Authoring module for linden-courtyard-fr-s01e02-scene-08.
ID = 'linden-courtyard-fr-s01e02-scene-08'
SHOW = 'linden-courtyard-fr'
SEASON = 1
EPISODE = 2
SCENE = 8
TITLE = 'Two Names, One Room  (Deux noms, une seule chambre)'
LEVEL = 'A1 — débutant'
PAIR = 'en-fr'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = "Le mercredi en fin d'après-midi, alors que le crépuscule gagne Portland, Arthur sort blême de son bureau en tenant à la fois la tablette tactile et le grand registre papier de Graham. Hannah et Graham lèvent aussitôt les yeux. Écoutez d'abord."
OPENER = "Reprenons phrase par phrase ce rebondissement de fin d'épisode."
TRANSITION = 'Réécoutons une dernière fois toute la scène à son rythme normal.'
OUTRO = "Deux clients réservés pour la même chambre sept, une averse battante dehors et quarante minutes à peine avant le train de huit heures! Ainsi s'achève le deuxième épisode; retrouvez-nous au troisième épisode pour voir si le grenier sauvera la soirée! À demain!"
CLOSING = ('arthur', 'See you tomorrow!')
STORY = [('arthur',
  'Graham... Hannah... please tell me room six is free tonight.',
  'Graham... Hannah... dites-moi je vous en supplie que la chambre six est libre ce soir.'),
 ('hannah',
  'No, Arthur, the couple from the south checked into room six an hour ago.',
  "Non, Arthur, le couple venu du Sud s'est installé dans la chambre six il y a une heure."),
 ('graham',
  'Every key from one to seven is taken, and room eight has wet paint.',
  'Toutes les clés de un à sept sont prises, et la peinture est fraîche dans la chambre huit.'),
 ('arthur',
  'Oh, disaster! Yesterday I took a phone booking on the tablet without my glasses!',
  "Oh, catastrophe! Hier, j'ai pris une réservation téléphonique sur la tablette sans mes lunettes!"),
 ('hannah',
  'Wait, let me look at the tablet screen and the paper book together.',
  "Attends, laisse-moi regarder l'écran de la tablette et le registre en papier côte à côte."),
 ('graham',
  'Let me guess. You promised somebody a room we do not have?',
  "Laisse-moi deviner. Tu as promis à quelqu'un une chambre que nous n'avons pas?"),
 ('hannah',
  'Arthur! Room seven is already occupied, and you booked a second guest into room seven!',
  'Arthur! La chambre sept est déjà occupée, et tu as réservé la chambre sept pour un deuxième client!'),
 ('arthur',
  "And he arrives here at eight o'clock this evening, in forty minutes!",
  'Et il arrive ici à huit heures ce soir, dans quarante minutes!'),
 ('graham', 'Told you that tablet is a trap.', "Je te l'avais bien dit que cette tablette était un piège."),
 ('arthur',
  'It is raining outside and every hotel on our street is full! What do we do?',
  "Il pleut dehors et tous les hôtels de notre rue sont complets! Qu'est-ce qu'on fait?"),
 ('hannah', 'Wait, what is on the third floor above the stairs?', "Attendez, qu'y a-t-il au deuxième étage en haut de l'escalier?"),
 ('graham', 'The old sunny attic study... follow me, quickly!', 'Le vieux bureau ensoleillé du grenier... suivez-moi, vite!')]
WALK = [(0,
  None,
  ["'Graham... Hannah... dites-moi je vous en supplie que la chambre six est libre ce soir.' Ici l'adjectif dans",
   (None, 'is free tonight'),
   'ne signifie pas gratuit, mais disponible pour la nuit.']),
 (1,
  None,
  ["'Non, Arthur, le couple venu du Sud s'est installé dans la chambre six il y a une heure.' En hôtellerie, la tournure",
   (None, 'checked into room six'),
   'indique que les voyageurs ont pris possession de leur chambre.']),
 (2,
  None,
  ['\'Toutes les clés de un à sept sont prises, et la peinture est fraîche dans la chambre huit.\' Là où nous disons "peinture fraîche", '
   "l'anglais dit concrètement",
   (None, 'wet paint'),
   'peinture encore humide.']),
 (3,
  None,
  ["'Oh, catastrophe! Hier, j'ai pris une réservation téléphonique sur la tablette sans mes lunettes!' Avec les appareils numériques et "
   "écrans, l'anglais choisit la préposition de surface dans",
   (None, 'on the tablet'),
   'sur la tablette.']),
 (4,
  None,
  ["'Attends, laisse-moi regarder l'écran de la tablette et le registre en papier côte à côte.' Placé tout à la fin,",
   (None, 'together'),
   "exprime l'idée de comparer les deux supports ensemble."]),
 (5,
  None,
  ["'Laisse-moi deviner. Tu as promis à quelqu'un une chambre que nous n'avons pas?' Plein d'ironie tranquille,",
   (None, 'Let me guess'),
   "annonce qu'on a déjà compris la gaffe."]),
 (6,
  None,
  ["'Arthur! La chambre sept est déjà occupée, et tu as réservé la chambre sept pour un deuxième client!' Vous retrouvez ici le mot livre "
   'devenu verbe régulier au passé dans',
   (None, 'you booked'),
   'tu as réservé.']),
 (7,
  None,
  ["'Et il arrive par le train du soir de huit heures, dans quarante minutes!' Pour un horaire officiel de train, le présent simple",
   (None, 'he arrives'),
   'suffit à annoncer une arrivée imminente.']),
 (8,
  None,
  ["'Je te l'avais bien dit que cette tablette était un piège.' À l'oral familier, Graham élide le sujet au début de",
   (None, 'Told you'),
   'qui claque exactement comme notre "Je te l\'avais bien dit!".']),
 (9,
  None,
  ["'Il pleut dehors et tous les hôtels de notre rue sont complets! Qu'est-ce qu'on fait?' Au cœur de l'urgence, la question au présent",
   (None, 'What do we do'),
   'traduit directement notre "Qu\'est-ce qu\'on fait?".']),
 (10,
  None,
  ["'Attendez, qu'y a-t-il au deuxième étage en haut de l'escalier?' Aux États-Unis, le niveau sous les combles au-dessus du premier étage "
   "s'appelle",
   (None, 'on the third floor'),
   'puisque le rez-de-chaussée compte déjà pour un.']),
 (11,
  None,
  ["'Le vieux bureau ensoleillé du grenier... suivez-moi, vite!' Graham prend aussitôt les commandes avec l'impératif",
   (None, 'follow me'),
   "pour entraîner l'équipe vers le grenier."])]
