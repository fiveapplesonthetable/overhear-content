# Authoring module for linden-courtyard-fr-s01e01-scene-04.
ID = 'linden-courtyard-fr-s01e01-scene-04'
SHOW = 'linden-courtyard-fr'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'Room Four on the Second Floor  (La chambre quatre au premier étage)'
LEVEL = 'A1 — débutant'
PAIR = 'en-fr'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = 'À la réception, Evelyn, professeure de piano à la retraite, descend du taxi en tirant une grande valise bleu marine. Hannah accueille sa toute première vraie cliente tandis que Graham se tient prêt à porter son bagage. Écoutons comment se passe cet accueil.'
OPENER = "Parcourons maintenant ce dialogue d'arrivée ligne par ligne."
TRANSITION = 'Écoutons une nouvelle fois la scène entière au fil naturel des voix.'
OUTRO = 'Hannah a réussi son premier enregistrement avec aisance, mais Graham a bien senti que cette valise bleue pesait un poids inhabituel. À très bientôt pour découvrir pourquoi!'
CLOSING = ('evelyn', 'Take care!')
STORY = [('hannah', "Welcome! Good morning, ma'am.", 'Bienvenue! Bonjour, madame.'),
 ('evelyn', 'Good morning, my dear. I have a booking for Evelyn.', "Bonjour, ma chère. J'ai une réservation pour Evelyn."),
 ('hannah',
  'Yes, room four on the second floor! How was your train trip?',
  "Oui, la chambre quatre au premier étage! Comment s'est passé votre voyage en train?"),
 ('evelyn',
  'Quiet and pleasant, thank you, though this suitcase feels very heavy today.',
  "Calme et agréable, merci, même si cette valise me semble très lourde aujourd'hui."),
 ('graham', 'Allow me. Goodness, did you pack stones in here?', 'Permettez-moi. Bonté divine, avez-vous mis des pierres là-dedans?'),
 ('evelyn', 'Only dresses, sheet music, and my favorite teacup!', 'Seulement des robes, des partitions et ma tasse à thé préférée!'),
 ('hannah',
  'Here is your key, number four. Breakfast is from seven thirty to ten.',
  'Voici votre clé, la numéro quatre. Le petit-déjeuner est servi de sept heures trente à dix heures.'),
 ('evelyn',
  'Wonderful. Is the window facing the street or the courtyard?',
  'Merveilleux. La fenêtre donne-t-elle sur la rue ou sur la cour?'),
 ('hannah', 'The courtyard, right above the old tree. It is very quiet.', "Sur la cour, juste au-dessus du vieil arbre. C'est très calme."),
 ('evelyn', 'Just what I need. Where are the stairs?', "Exactement ce qu'il me faut. Où est l'escalier?"),
 ('graham',
  'Right through this archway. I will carry the blue bag up for you.',
  'Juste sous cette arche. Je vais vous monter le sac bleu.'),
 ('evelyn', 'Thank you both very much.', 'Merci beaucoup à vous deux.')]
WALK = [(0,
  None,
  ["'Bienvenue! Bonjour, madame.' Aux États-Unis, le mot poli",
   (None, "ma'am"),
   'contracte l\'ancien emprunt français "madame" pour saluer une cliente avec déférence.']),
 (1,
  None,
  ["'Bonjour, ma chère. J'ai une chambre au nom d'Evelyn.' En arrivant à l'hôtel, la formule simple",
   (None, 'I have a booking for'),
   'suivie du prénom suffit à annoncer sa réservation.']),
 (2,
  None,
  ['\'Oui, la chambre quatre au premier étage! Comment s\'est passé votre voyage en train?\' Attention au décalage américain: le "deuxième '
   'niveau" correspond à notre premier étage! Puis',
   (None, 'How was your train trip'),
   "s'enquiert poliment du trajet."]),
 (3,
  None,
  ["'Calme et agréable, merci, même si cette valise me semble très lourde aujourd'hui.' Le verbe de sensation dans",
   (None, 'feels very heavy'),
   'décrit le poids ressenti au bout du bras.']),
 (4,
  None,
  ["'Permettez-moi. Bonté divine, avez-vous mis des pierres là-dedans?' Graham offre son aide d'un courtois",
   (None, 'Allow me'),
   'avant de lâcher un',
   (None, 'Goodness'),
   'plein de surprise polie en soulevant le bagage.']),
 (5,
  None,
  ["'Seulement des robes, des partitions et ma tasse à thé préférée!' Pour désigner des partitions imprimées, l'anglais réunit feuille et "
   'musique dans le composé indénombrable',
   (None, 'sheet music'),
   'sans marque de pluriel.']),
 (6,
  None,
  ["'Voici votre clé, la numéro quatre. Le petit-déjeuner est servi de sept heures trente à dix heures.' Les horaires parlés juxtaposent "
   "simplement l'heure et les minutes:",
   (None, 'seven thirty'),
   'sans ajouter le mot "heures".']),
 (7,
  None,
  ["'Merveilleux. La fenêtre donne-t-elle sur la rue ou sur la cour?' Pour demander sur quoi donne une chambre, l'anglais utilise l'image "
   "du visage tourné vers l'extérieur:",
   (None, 'facing the street'),
   'donnant sur la rue.']),
 (8,
  None,
  ["'Sur la cour, juste au-dessus du vieil arbre. C'est très calme.' L'ajout du premier mot dans",
   (None, 'right above'),
   'précise que la fenêtre se situe exactement à la verticale du tilleul.']),
 (9,
  None,
  ["'Exactement ce qu'il me faut. Où est l'escalier?' La réponse concise",
   (None, 'Just what I need'),
   'exprime une satisfaction immédiate en quatre petits mots très courants.']),
 (10,
  None,
  ["'Juste sous cette arche. Je vais vous monter le sac bleu.' Pour une décision serviable prise sur l'instant, Graham emploie",
   (None, 'I will carry'),
   'et ajoute la particule',
   (None, 'up'),
   "qui traduit à elle seule l'idée de monter."]),
 (11,
  None,
  ["'Merci beaucoup à vous deux.' Placé juste après le pronom, le mot",
   (None, 'both'),
   'permet dans',
   (None, 'Thank you both'),
   'de remercier chaleureusement deux personnes à la fois.'])]
