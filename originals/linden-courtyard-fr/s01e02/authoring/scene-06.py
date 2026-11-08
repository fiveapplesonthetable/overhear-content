# Authoring module for linden-courtyard-fr-s01e02-scene-06.
ID = 'linden-courtyard-fr-s01e02-scene-06'
SHOW = 'linden-courtyard-fr'
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = "The Friday Caller  (L'appel pour vendredi)"
LEVEL = 'A1 — débutant'
PAIR = 'en-fr'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Après le coup de feu du petit-déjeuner, le hall retrouve son calme pendant que Hannah met à jour le registre papier et que Graham huile la charnière de la porte. Soudain, le téléphone du comptoir retentit. Écoutons.'
OPENER = 'Décortiquons ensemble chaque phrase de cet appel mystérieux.'
TRANSITION = "Réécoutons maintenant toute la conversation téléphonique d'un seul bloc."
OUTRO = "L'équipe a désormais un rendez-vous précis — vendredi à midi — et le souvenir d'une voix nerveuse qui a refusé de donner son nom. À très vite pour la suite!"
CLOSING = ('hannah', 'Bye for now!')
STORY = [('hannah', 'Linden Courtyard Inn, good morning! Hannah speaking.', "Auberge de la Cour du Tilleul, bonjour! Hannah à l'appareil."),
 ('graham', 'Who is it? Another booking for the weekend?', 'Qui est-ce? Encore une réservation pour la fin de semaine?'),
 ('hannah',
  'Wait, hello, sir! You are calling about the dark blue suitcase?',
  'Attendez, bonjour, monsieur! Vous appelez au sujet de la valise bleu marine?'),
 ('graham', 'Ask him his name! Write it down!', 'Demande-lui son nom! Note-le!'),
 ('hannah',
  'Yes, sir, we locked your bag safely in our closet. What is your name, please?',
  "Oui, monsieur, nous avons enfermé votre sac en sécurité dans notre placard. Quel est votre nom, s'il vous plaît?"),
 ('graham', 'What is he saying? Why are you frowning?', "Qu'est-ce qu'il dit? Pourquoi fronces-tu les sourcils?"),
 ('hannah',
  "Sir? He says, 'Please do not open the white paper package. I will come Friday at noon.'",
  'Monsieur? Il dit: "S\'il vous plaît, n\'ouvrez pas le paquet en papier blanc. Je viendrai vendredi à midi."'),
 ('graham', 'Give me the phone, let me ask him properly!', 'Passe-moi le téléphone, laisse-moi lui demander comme il faut!'),
 ('hannah', "Too late! He said 'Thank you' and hung up!", 'Trop tard! Il a dit "Merci" et il a raccroché!'),
 ('graham', 'Polite voice? Young or old?', 'Une voix polie? Jeune ou âgée?'),
 ('hannah',
  'Quiet, polite, maybe thirty-five. He sounded nervous, not angry.',
  "Posée, polie, trente-cinq ans peut-être. Il avait l'air nerveux, pas en colère."),
 ('graham',
  'Nervous about a wooden toy train? This story gets stranger every hour.',
  "Nerveux à cause d'un petit train en bois? Cette histoire devient plus étrange d'heure en heure.")]
WALK = [(0,
  None,
  ["'Auberge de la Cour du Tilleul, bonjour! Hannah à l'appareil.' En décrochant le téléphone professionnel, la formule",
   (None, 'Hannah speaking'),
   'correspond exactement à notre "Hannah à l\'appareil".']),
 (1,
  None,
  ["'Qui est-ce? Encore une réservation pour la fin de semaine?' Pour savoir qui est en ligne, l'anglais demande",
   (None, 'Who is it'),
   "en utilisant le pronom neutre tant que la personne n'est pas identifiée."]),
 (2,
  None,
  ["'Attendez, bonjour, monsieur! Vous appelez au sujet de la valise bleu marine?' Le présent continu dans",
   (None, 'You are calling about'),
   "exprime le motif précis de l'appel en cours."]),
 (3,
  None,
  ["'Demande-lui son nom! Note-le!' Avec un pronom court, celui-ci se glisse obligatoirement au milieu du verbe à particule dans",
   (None, 'Write it down'),
   'pour dire "note-le par écrit".']),
 (4,
  None,
  ["'Oui, monsieur, nous avons enfermé votre sac en sécurité dans notre placard. Quel est votre nom, s'il vous plaît?' Plutôt que "
   '"comment vous appelez-vous?", l\'anglais demande littéralement',
   (None, 'What is your name'),
   'quel est votre nom.']),
 (5,
  None,
  ["'Qu'est-ce qu'il dit? Pourquoi fronces-tu les sourcils?' Un seul mot anglais,",
   (None, 'frowning'),
   'suffit à traduire tout le geste de froncer les sourcils.']),
 (6,
  None,
  ['\'Monsieur? Il dit: "S\'il vous plaît, n\'ouvrez pas le paquet en papier blanc. Je viendrai vendredi à midi."\' Comme pour toute heure '
   "précise, midi s'introduit avec la préposition ponctuelle dans",
   (None, 'at noon'),
   'à midi pile.']),
 (7,
  None,
  ["'Passe-moi le téléphone, laisse-moi lui demander comme il faut!' Attention au faux-ami partiel:",
   (None, 'properly'),
   'veut dire "convenablement, dans les règles", et non "proprement".']),
 (8,
  None,
  ['\'Trop tard! Il a dit "Merci" et il a raccroché!\' Pour le téléphone, le prétérit irrégulier',
   (None, 'hung up'),
   "rappelle l'époque où l'on raccrochait le combiné à son support."]),
 (9,
  None,
  ["'Une voix polie? Jeune ou âgée?' Deux adjectifs opposés reliés sans article,",
   (None, 'Young or old'),
   "permettent à Graham d'aller droit au but."]),
 (10,
  None,
  ["'Posée, polie, trente-cinq ans peut-être. Il avait l'air nerveux, pas en colère.' Lorsqu'on juge l'état de quelqu'un au son de sa "
   'voix, on emploie',
   (None, 'sounded nervous'),
   "où l'adjectif signifie inquiet ou tendu, et non irrité."]),
 (11,
  None,
  ["'Nerveux à cause d'un petit train en bois? Cette histoire devient plus étrange d'heure en heure.' Ici le même mot écrit qu'à l'épisode "
   'un n\'est plus le nom "inconnu", mais le comparatif dans',
   (None, 'gets stranger'),
   'devient plus bizarre.'])]
