# Authoring module for hotel-du-tilleul-s01e02-scene-08.
ID = 'hotel-du-tilleul-s01e02-scene-08'
SHOW = 'hotel-du-tilleul'
SEASON = 1
EPISODE = 2
SCENE = 8
TITLE = 'Deux noms, une chambre  (Two Names, One Room)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'etienne': 'Étienne', 'claire': 'Claire', 'henri': 'Henri'}
INTRO = ('On Wednesday evening, as dusk settles over Lyon, Etienne comes out of his office holding both '
 "the tablet computer and Henri's paper ledger, looking pale. Claire and Henri look up at once. "
 'Listen first.')
OPENER = "Let's hear how Etienne discovers the Wednesday evening double-booking."
TRANSITION = "Now let's hear the whole conversation again from the beginning."
OUTRO = ('Two guests booked into Room 7, pouring rain outside, and only forty minutes before the eight '
 "o'clock arrival! Episode 2 is done; join us in Episode 3 to see if the attic can save the night.")
CLOSING = ('etienne', 'Bonne soirée!')
STORY = [('etienne',
  "Henri... Claire... dites-moi que la chambre six est libre ce soir, s'il vous plaît.",
  'Henri... Claire... please tell me room six is free tonight.'),
 ('claire',
  'Non, Étienne, le couple du sud est arrivé dans la chambre six il y a une heure.',
  'No, Etienne, the couple from the south checked into room six an hour ago.'),
 ('henri',
  'Toutes les clés de un à sept sont prises, et la peinture de la huit est fraîche.',
  'Every key from one to seven is taken, and room eight has wet paint.'),
 ('etienne',
  "Quelle catastrophe! Hier, j'ai noté une réservation sur la tablette sans mes lunettes!",
  'What a disaster! Yesterday I wrote a booking on the tablet without my glasses!'),
 ('claire',
  "Attendez, regardons l'écran de la tablette et le cahier en papier ensemble.",
  'Wait, let us look at the tablet screen and the paper book together.'),
 ('henri',
  "Laissez-moi deviner. Vous avez promis une chambre qu'on n'a pas?",
  'Let me guess. You promised a room we do not have?'),
 ('claire',
  'Étienne! La chambre sept est déjà occupée, et vous avez mis un deuxième client dans la sept!',
  'Etienne! Room seven is already occupied, and you put a second guest in seven!'),
 ('etienne',
  'Et il arrive ici à huit heures ce soir — dans quarante minutes!',
  "And he arrives here at eight o'clock this evening—in forty minutes!"),
 ('henri',
  'Je vous avais dit que cette tablette est un piège.',
  'I told you that tablet is a trap.'),
 ('etienne',
  "Il pleut dehors et tous les hôtels de la rue sont complets! Qu'est-ce qu'on fait?",
  'It is raining outside and every hotel on the street is full! What do we do?'),
 ('claire',
  "Attendez, qu'est-ce qu'il y a au troisième étage, en haut de l'escalier?",
  'Wait, what is on the third floor, at the top of the stairs?'),
 ('henri',
  'Le vieux bureau clair sous les toits... suivez-moi, vite!',
  'The old bright attic study... follow me, quickly!')]
WALK = [(0,
  None,
  "'Henri... Claire... please tell me room six is free tonight.' The same word means both 'free' "
  "as in unoccupied and 'free' to choose."),
 (2,
  None,
  "'Every key from one to seven is taken, and room eight has wet paint.' Where English says 'wet "
  "paint', French says 'fresh paint', just like fresh bread!"),
 (5,
  'Laissez-moi deviner.',
  ["'Let me guess.' Before making a wry prediction,",
   (None, 'Laissez-moi deviner.'),
   "is a handy phrase that means 'let me guess'."]),
 (7,
  None,
  "'And he arrives on the eight o'clock evening train, in forty minutes!' In French, train "
  "timetables always use twenty-four-hour time, literally 'twenty hours' for eight in the "
  'evening.'),
 (9,
  "Il pleut dehors et tous les hôtels de la rue sont complets! Qu'est-ce qu'on fait?",
  "'It is raining outside and every hotel on the street is full! What do we do?' On a French hotel "
  "door, the word for 'complete' means 'full, no vacancies'."),
 (10,
  None,
  "'Wait, what is on the third floor, at the top of the stairs?' Combining 'what is it that' with "
  "'there is' builds the everyday French question for 'what is there?'."),
 (11,
  None,
  ["'The old bright attic study... follow me, quickly!' French often describes an attic room "
   'poetically as',
   (None, 'sous les toits...'),
   "literally 'under the roofs'."])]
