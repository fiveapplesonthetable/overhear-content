# Authoring module for linden-courtyard-fr-s01e03-scene-04.
ID = 'linden-courtyard-fr-s01e03-scene-04'
SHOW = 'linden-courtyard-fr'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = "In from the Rain  (À l'abri de la pluie)"
LEVEL = 'A1 — débutant'
PAIR = 'en-fr'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb', 'tessa': 'Tessa'}
INTRO = "En bas dans le hall d'entrée, Caleb, un voyageur posé d'une trentaine d'années, franchit la porte en secouant son parapluie ruisselant. Hannah l'accueille au comptoir pendant que Tessa lui tend une serviette sèche. Écoutez d'abord l'échange complet."
OPENER = 'Étudions maintenant pas à pas cet accueil plein de tact.'
TRANSITION = "Réécoutons l'ensemble du dialogue au fil naturel de la conversation."
OUTRO = "Une franchise immédiate, une serviette bien sèche et une soupe fumante ont préservé toute la sérénité de la soirée. Dans la prochaine scène, Caleb monte l'escalier pour juger la mansarde par lui-même. À bientôt!"
CLOSING = ('caleb', 'See you soon!')
STORY = [('hannah', 'Good evening! Come inside out of the rain, sir.', "Bonsoir! Entrez vous mettre à l'abri de la pluie, monsieur."),
 ('caleb', 'Good evening. Sorry for dripping water on your clean floor.', "Bonsoir. Désolé d'égoutter de l'eau sur votre sol propre."),
 ('hannah', 'Do not worry at all! You must be Caleb.', 'Ne vous inquiétez pas du tout! Vous devez être Caleb.'),
 ('caleb', 'Yes, Caleb. I booked room seven by phone yesterday.', "Oui, Caleb. J'ai réservé la chambre sept par téléphone hier."),
 ('tessa',
  'Here is a dry towel for your coat and a cup of hot soup, sir.',
  'Voici une serviette sèche pour votre manteau et un bol de soupe chaude, monsieur.'),
 ('caleb',
  'Hot soup? After that cold train platform, that sounds wonderful.',
  'De la soupe chaude? Après ce quai de gare glacial, cela me semble merveilleux.'),
 ('hannah', 'Sir, before we go upstairs, I owe you an honest apology.', 'Monsieur, avant de monter, je vous dois des excuses sincères.'),
 ('caleb', 'Oh? Is there a problem with my booking?', 'Ah? Y a-t-il un problème avec ma réservation?'),
 ('hannah',
  'We accidentally wrote two bookings on room seven tonight.',
  'Nous avons inscrit par mégarde deux réservations sur la chambre sept ce soir.'),
 ('caleb',
  'Ah... in this rain? Every hotel near the station looked full.',
  "Ah... sous cette pluie? Tous les hôtels près de la gare avaient l'air complets."),
 ('hannah',
  'Please do not worry! We prepared our quiet third floor attic study just for you.',
  "S'il vous plaît, ne vous inquiétez pas! Nous avons préparé notre paisible bureau sous les combles au deuxième étage rien que pour "
  'vous.'),
 ('caleb', 'An attic study? May I see it first?', "Un bureau sous les combles? Puis-je le voir d'abord?")]
WALK = [(0,
  None,
  ["'Bonsoir! Entrez vous mettre à l'abri de la pluie, monsieur.' Observez le double mouvement spatial dans",
   (None, 'inside out of the rain'),
   "qui invite à entrer dedans tout en sortant de l'averse."]),
 (1,
  None,
  ["'Bonsoir. Désolé d'égoutter de l'eau sur votre sol propre.' Après la préposition d'excuse, le verbe goutter prend la forme nominale "
   'dans',
   (None, 'Sorry for dripping'),
   "désolé de faire goutter de l'eau."]),
 (2,
  None,
  ["'Ne vous inquiétez pas du tout! Vous devez être Caleb.' Placé en bout de défense,",
   (None, 'at all'),
   'efface toute gêne, puis',
   (None, 'You must be'),
   "exprime une déduction chaleureuse sur l'identité du voyageur."]),
 (3,
  None,
  ["'Oui, Caleb. J'ai réservé la chambre sept par téléphone hier.' Sans aucun article défini, le moyen de communication se construit "
   'sobrement en',
   (None, 'by phone'),
   'exactement comme notre "par téléphone".']),
 (4,
  None,
  ["'Voici une serviette sèche pour votre manteau et un bol de soupe chaude, monsieur.' Pour tendre un objet singulier avec courtoisie, "
   'Tessa commence tout simplement par',
   (None, 'Here is a dry towel'),
   'voici une serviette sèche.']),
 (5,
  None,
  ["'De la soupe chaude? Après ce quai de gare glacial, cela me semble merveilleux.' Un quai ferroviaire se dit",
   (None, 'train platform'),
   'et la réaction enthousiaste',
   (None, 'that sounds wonderful'),
   "juge une proposition séduisante à ce qu'on vient d'entendre."]),
 (6,
  None,
  ["'Monsieur, avant de monter, je vous dois des excuses sincères.' Le verbe devoir une dette morale s'entend dans",
   (None, 'I owe you'),
   'suivi du singulier',
   (None, 'an honest apology'),
   'là où le français préfère le pluriel "des excuses".']),
 (7,
  None,
  ["'Ah? Y a-t-il un problème avec ma réservation?' Calme et posée, l'inversion",
   (None, 'Is there a problem'),
   "permet de s'informer d'un contretemps sans hausser le ton."]),
 (8,
  None,
  ["'Nous avons inscrit par mégarde deux réservations sur la chambre sept ce soir.' L'adverbe",
   (None, 'accidentally'),
   "souligne l'erreur involontaire juste devant le prétérit irrégulier",
   (None, 'wrote'),
   'du verbe écrire.']),
 (9,
  None,
  ["'Ah... sous cette pluie? Tous les hôtels près de la gare avaient l'air complets.' Attention au singulier distributif",
   (None, 'Every hotel'),
   'qui traduit "tous les hôtels" pris un par un, avant',
   (None, 'looked full'),
   'semblait complet.']),
 (10,
  None,
  ["'S'il vous plaît, ne vous inquiétez pas! Nous avons préparé notre paisible bureau sous les combles au deuxième étage rien que pour "
   "vous.' Trois petits mots chaleureux,",
   (None, 'just for you'),
   'rendent aussitôt ce changement de chambre exclusif et attentionné.']),
 (11,
  None,
  ["'Un bureau sous les combles? Puis-je le voir d'abord?' Plus distingué et courtois que l'auxiliaire courant de capacité,",
   (None, 'May I see it'),
   'demande la permission avec une parfaite élégance.'])]
