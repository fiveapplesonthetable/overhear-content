# Authoring module for hotel-du-tilleul-s01e01-scene-04.
ID = 'hotel-du-tilleul-s01e01-scene-04'
SHOW = 'hotel-du-tilleul'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'La chambre quatre au deuxième étage  (Room Four on the Second Floor)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'claire': 'Claire', 'odette': 'Odette', 'henri': 'Henri'}
INTRO = ('At the front desk, retired music teacher Odette steps inside from her taxi pulling a large '
 'dark-blue suitcase. Claire greets her first real guest while Henri stands ready to help with the '
 "bag. Let's hear how it goes.")
OPENER = "Let's listen closely to Claire's first guest check-in."
TRANSITION = "Now let's hear the whole conversation again from top to bottom."
OUTRO = ('Claire handled her first check-in smoothly, though Henri noticed that blue suitcase felt '
 'strangely heavy. See you next time to find out why.')
CLOSING = ('odette', 'À bientôt!')
STORY = [('claire', 'Bienvenue! Bonjour, madame.', 'Welcome! Good morning, madam.'),
 ('odette',
  "Bonjour, ma chère. J'ai une réservation au nom d'Odette.",
  'Good morning, my dear. I have a reservation under the name Odette.'),
 ('claire',
  'Oui, la chambre quatre au deuxième étage! Comment était votre voyage en train?',
  'Yes, room four on the second floor! How was your train trip?'),
 ('odette',
  "Calme et agréable, merci, mais cette valise semble très lourde aujourd'hui.",
  'Quiet and pleasant, thank you, though this suitcase feels very heavy today.'),
 ('henri',
  'Permettez-moi. Mon Dieu, vous avez mis des pierres dedans?',
  'Allow me. Goodness, did you pack stones inside?'),
 ('odette',
  'Seulement des robes, des partitions et ma tasse préférée!',
  'Only dresses, sheet music, and my favourite cup!'),
 ('claire',
  'Voici votre clé, numéro quatre. Le petit-déjeuner est de sept heures trente à dix heures.',
  'Here is your key, number four. Breakfast is from seven thirty to ten.'),
 ('odette',
  'Parfait. La fenêtre donne sur la rue ou sur la cour?',
  'Wonderful. Does the window face the street or the courtyard?'),
 ('claire',
  "Sur la cour, juste au-dessus du vieux tilleul. C'est très calme.",
  'The courtyard, right above the old linden tree. It is very quiet.'),
 ('odette',
  "Exactement ce qu'il me faut. Où est l'escalier?",
  'Just what I need. Where are the stairs?'),
 ('henri',
  'Juste sous cette arche. Je vais monter la valise bleue pour vous.',
  'Right under this archway. I will carry the blue suitcase up for you.'),
 ('odette', 'Merci beaucoup à vous deux.', 'Thank you both very much.')]
WALK = [(1,
  "J'ai une réservation au nom d'Odette.",
  "'I have a reservation under the name Odette.' At French hotels and restaurants, you give a "
  "booking 'at the name of' rather than 'under the name'."),
 (2,
  'Comment était votre voyage en train?',
  "'How was your train trip?' Notice 'in train' for 'by train': French uses 'in' for enclosed "
  'vehicles like trains, cars, and buses.'),
 (4,
  'Permettez-moi.',
  ["'Allow me.' When offering to carry something heavy for a guest,",
   (None, 'Permettez-moi.'),
   'is a warm, courteous one-phrase offer.']),
 (5,
  None,
  "'Only dresses, sheet music, and my favourite cup!' Unlike English, French cannot leave plural "
  "things bare; that short word before 'dresses' and 'sheet music' means 'some'."),
 (6,
  'Le petit-déjeuner est de sept heures trente à dix heures.',
  "'Breakfast is from seven thirty to ten.' French literally calls breakfast 'the little lunch', "
  "and always includes the word 'hours' when telling clock time."),
 (7,
  None,
  ["'Wonderful. Does the window face the street or the courtyard?' To ask which way a room faces, "
   'French says the window',
   (None, 'donne sur'),
   "which literally means 'gives onto'."]),
 (9,
  "Exactement ce qu'il me faut. Où est l'escalier?",
  "'Just what I need. Where are the stairs?' Where English uses plural 'stairs', French treats "
  "'the staircase' as a single masculine thing."),
 (10,
  'Je vais monter la valise bleue pour vous.',
  "'I will carry the blue suitcase up for you.' Combining 'I go' with 'go up' makes a simple "
  "near-future plan, and the same word means both 'climb up' and 'carry upstairs'.")]
