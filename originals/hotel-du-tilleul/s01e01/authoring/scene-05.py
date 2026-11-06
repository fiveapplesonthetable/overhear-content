# Authoring module for hotel-du-tilleul-s01e01-scene-05.
ID = 'hotel-du-tilleul-s01e01-scene-05'
SHOW = 'hotel-du-tilleul'
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = 'Ce ne sont pas mes affaires!  (Not My Clothes!)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'odette': 'Odette', 'claire': 'Claire', 'henri': 'Henri'}
INTRO = ("Two minutes after going upstairs, Room 4's buzzer rings at the desk, not twice, but four times "
 'in a row. Claire hurries up to find Odette and Henri staring at the open suitcase on the stand. '
 'Listen first.')
OPENER = "Let's go back upstairs to Room 4 and unpack what they found inside."
TRANSITION = "Now let's listen to the whole scene again without interruption."
OUTRO = ('Instead of dresses and sheet music, the blue suitcase holds big brown shoes and a wooden toy '
 "train. Let's see what is written on that tag next time.")
CLOSING = ('claire', "À tout à l'heure!")
STORY = [('claire',
  'Madame Odette, tout va bien? Vous avez sonné!',
  'Madam Odette, is everything alright? You rang the bell!'),
 ('odette',
  "Regardez dans cette valise, Claire! Ce n'est pas mon sac!",
  'Look inside this suitcase, Claire! This is not my bag!'),
 ('claire',
  'Attendez, elle est bleu foncé, exactement comme la vôtre!',
  'Wait, it is dark blue, just like yours!'),
 ('odette',
  "L'extérieur est identique, oui! Mais regardez à l'intérieur!",
  'The outside is identical, yes! But look inside!'),
 ('henri',
  'Deux paires de grandes chaussures marron pour homme et des pulls gris.',
  "Two pairs of big brown men's shoes and grey sweaters."),
 ('claire',
  "Et qu'est-ce que c'est, dans ce papier blanc? Un petit train en bois!",
  'And what is this, in this white paper? A little wooden train!'),
 ('odette',
  'Je ne chausse certainement pas du quarante-quatre!',
  'I certainly do not wear size forty-four shoes!'),
 ('henri',
  "Pas étonnant qu'elle soit si lourde. Du bois et du cuir!",
  'No wonder it is so heavy. Wood and leather!'),
 ('odette',
  "Quelqu'un à la gare a pris ma valise bleue par erreur!",
  'Someone at the train station took my blue suitcase by mistake!'),
 ('claire',
  "Asseyez-vous, madame. Ne vous inquiétez pas, on va regarder l'étiquette tout de suite.",
  'Please sit down, madam. Do not worry, we will check the tag right now.'),
 ('henri',
  'Il y a une petite carte en papier attachée à la poignée.',
  'There is a small paper card tied to the handle.'),
 ('odette', 'Oh, descendons-la à la lumière!', 'Oh, let us bring it downstairs to the light!')]
WALK = [(0,
  'Madame Odette, tout va bien?',
  ["'Madam Odette, is everything alright?' Asking",
   (None, 'tout va bien?'),
   "literally asks 'everything goes well?', a natural check-in whenever someone sounds worried."]),
 (1,
  "Ce n'est pas mon sac!",
  "'This is not my bag!' Swap in any item at the end of this handy sentence whenever a coat, "
  'umbrella, or suitcase gets mixed up.'),
 (2,
  None,
  "'Wait, it is dark blue, just like yours!' Compound colours like 'dark blue' stay unchanged in "
  'French, even when describing a feminine suitcase.'),
 (4,
  None,
  "'Two pairs of big brown men's shoes and grey sweaters.' Notice that the colour 'brown' comes "
  'from the word for chestnut and never adds a plural ending.'),
 (5,
  'Un petit train en bois!',
  "'A little wooden train!' Unlike English, French says 'in wood', 'in paper', or 'in leather' to "
  'name what an object is made of.'),
 (6,
  None,
  ["'I certainly do not wear size forty-four shoes!' French has a special everyday word,",
   (None, 'chausse'),
   'built from the word for shoe, used specifically for what shoe size you take.']),
 (8,
  None,
  "'Someone at the train station took my blue suitcase by mistake!' Notice the neat two-word chunk "
  "at the end meaning 'by mistake', reusable for any mix-up."),
 (9,
  'Asseyez-vous, madame.',
  "'Please sit down, madam.' Literally 'sit yourself', this polite command form is how you offer a "
  'guest a chair.')]
