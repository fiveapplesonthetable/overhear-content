# Authoring module for hotel-du-tilleul-s01e02-scene-03.
ID = 'hotel-du-tilleul-s01e02-scene-03'
SHOW = 'hotel-du-tilleul'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = 'Le compte de la monnaie  (Counting the Change)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'claire': 'Claire', 'etienne': 'Étienne', 'nadia': 'Nadia'}
INTRO = ('Nine minutes later, Claire bursts back through the courtyard gate carrying two heavy cloth bags '
 'of groceries for Nadia and Etienne. Listen to the scene first.')
OPENER = "Let's check Claire's shopping bags and the butter surprise."
TRANSITION = "Now let's listen to the whole conversation again from the top."
OUTRO = ('An accidental packet of salted butter nearly caused a jam crisis, until Nadia turned it into the '
 'secret ingredient for the eggs. See you next time.')
CLOSING = ('nadia', 'À bientôt!')
STORY = [('claire',
  'Neuf minutes! Voici le lait, les œufs et les pommes!',
  'Nine minutes! Here are the milk, the eggs, and the apples!'),
 ('nadia',
  "Tu es une héroïne, Claire! Donne-moi le lait d'abord pour la machine à café.",
  'You are a hero, Claire! Give me the milk first for the coffee machine.'),
 ('etienne',
  "Quelle vitesse! L'épicier vous a donné un ticket?",
  'What speed! Did the grocer give you a receipt?'),
 ('claire',
  'Juste ici! Tout a coûté trente-huit euros, alors voici douze euros de monnaie.',
  'Right here! Everything cost thirty-eight euros, so here is twelve euros in change.'),
 ('etienne',
  'Dix, onze, douze. Le compte est bon au centime près, merci!',
  'Ten, eleven, twelve. Exact to the last cent, thank you!'),
 ('nadia',
  'Attends une seconde, Claire... tu as pris quelle plaquette de beurre?',
  'Wait a second, Claire... which packet of butter did you grab?'),
 ('claire',
  "Le papier doré sur l'étagère du haut. Pourquoi?",
  'The gold wrapper on the top shelf. Why?'),
 ('nadia',
  "C'est du beurre demi-sel! Mes petits pains sucrés ont besoin de beurre doux!",
  'That is salted butter! My sweet rolls need unsalted butter!'),
 ('claire',
  'Oh non! Tous les paquets se ressemblaient quand je courais!',
  'Oh no! All the packets looked alike when I was running!'),
 ('etienne',
  'On peut servir du beurre salé avec de la confiture de fraises?',
  'Can we serve salted butter with strawberry jam?'),
 ('nadia',
  'Attendez: le beurre salé est mauvais pour la confiture, mais génial pour les œufs brouillés!',
  'Wait: salted butter is bad for jam, but amazing for scrambled eggs!'),
 ('claire',
  'Ouf! Une bonne idée sauve encore le petit-déjeuner.',
  'Phew! A good idea saves breakfast again.')]
WALK = [(0,
  None,
  "'Nine minutes! Here are the milk, the eggs, and the apples!' One unchanging pointing word "
  "introduces both singular 'milk' and plural 'eggs'."),
 (1,
  "Donne-moi le lait d'abord pour la machine à café.",
  "'Give me the milk first for the coffee machine.' In French, machines use 'to' to show what they "
  "make, literally 'machine to coffee'."),
 (3,
  'Tout a coûté trente-huit euros, alors voici douze euros de monnaie.',
  ["'Everything cost thirty-eight euros, so here is twelve euros in change.' In a shop,",
   (None, 'monnaie.'),
   'means loose coins and change handed back to you.']),
 (4,
  None,
  "'Ten, eleven, twelve. Exact to the last cent, thank you!' Literally 'the count is good to the "
  "cent near', a classic French shopkeeper phrase."),
 (5,
  None,
  "'Wait a second, Claire... which packet of butter did you grab?' Putting 'which packet' at the "
  'end rather than the front keeps the question relaxed and conversational.'),
 (7,
  None,
  ["'That is salted butter! My sweet rolls need unsalted butter!' French supermarkets label plain "
   "unsalted butter as 'sweet butter', and salted butter as",
   (None, 'beurre demi-sel!'),
   "literally 'half-salt butter'."]),
 (10,
  None,
  "'Wait: salted butter is bad for jam, but amazing for scrambled eggs!' Notice Nadia says 'wait' "
  'politely in the plural here because she is answering both Etienne and Claire together.'),
 (11,
  'Ouf! Une bonne idée sauve encore le petit-déjeuner.',
  "'Phew! A good idea saves breakfast again.' That three-letter sigh at the start sounds like and "
  "means English 'phew'.")]
