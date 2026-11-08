# Authoring module for hotel-du-tilleul-s01e01-scene-01.
ID = 'hotel-du-tilleul-s01e01-scene-01'
SHOW = 'hotel-du-tilleul'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Soulevez la poignée  (Lift the Handle)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'claire': 'Claire', 'henri': 'Henri'}
INTRO = ('Claire arrives early for her very first morning at the Hotel du Tilleul guesthouse in Lyon. '
 'Behind the front desk, veteran handyman Henri is already pouring strong tea. Listen to the scene '
 'first without worrying about catching every word.')
OPENER = "Let's step back through Claire's arrival at the front door."
TRANSITION = "Now let's listen to the whole conversation again from the beginning."
OUTRO = ('Claire is inside, the eight brass keys are on the board, and her first morning has begun. Do not '
 'worry if a few words went past quickly; they come back all week. See you next time.')
CLOSING = ('claire', 'À bientôt!')
STORY = [('claire',
  'Bonjour! Excusez-moi, la porte est fermée à clé?',
  'Good morning! Excuse me, is the door locked?'),
 ('henri',
  "Bonjour. Non, soulevez d'abord la poignée, puis poussez.",
  'Good morning. No, lift the handle first, then push.'),
 ('claire',
  "Oh, ça s'ouvre! Merci. Je suis Claire, la nouvelle réceptionniste.",
  'Oh, it opens! Thank you. I am Claire, the new receptionist.'),
 ('henri',
  "Moi, c'est Henri. Vous êtes en avance de dix minutes.",
  'I am Henri. You are ten minutes early.'),
 ('claire',
  "Je marche toujours vite le premier jour. Où est l'ordinateur?",
  'I always walk fast on the first day. Where is the computer?'),
 ('henri',
  'Dans le tiroir. Ici, on utilise ce grand cahier en papier et un crayon.',
  'In the drawer. Here we use this big paper notebook and a pencil.'),
 ('claire', 'Un cahier en papier? Vraiment?', 'A paper notebook? Really?'),
 ('henri',
  'Le papier marche toujours quand le courant est coupé.',
  'Paper still works when the power goes out.'),
 ('claire', "C'est vrai! Et voici les clés?", 'Fair enough! And here are the keys?'),
 ('henri',
  "Oui, huit chambres, huit clés en laiton. Le client de la chambre quatre arrive aujourd'hui.",
  "Yes, eight rooms, eight brass keys. Room four's guest arrives today."),
 ('claire',
  "Super. Dites-moi tout ce qu'il faut savoir.",
  'Great. Tell me everything I need to know.'),
 ('henri',
  "Règle numéro un: buvez d'abord du thé chaud, puis répondez à la sonnette.",
  'Rule number one: drink hot tea first, then answer the bell.')]
WALK = [(0,
  'Excusez-moi, la porte est fermée à clé?',
  ["'Excuse me, is the door locked?' Notice the three-word chunk at the end,",
   (None, 'fermée à clé?'),
   'which literally says closed with a key.']),
 (1,
  "Non, soulevez d'abord la poignée, puis poussez.",
  "'No, lift the handle first, then push.' Henri uses polite commands ending in a soft sound "
  "because Claire is new here. The little word for 'first' sits right after the action."),
 (2,
  "Oh, ça s'ouvre!",
  "'Oh, it opens!' Instead of just saying it opens, French says the door opens itself, which is "
  'very common for doors, windows, and drawers.'),
 (3,
  None,
  ["'I am Henri. You are ten minutes early.' To introduce himself casually, Henri starts with",
   (None, "Moi, c'est Henri."),
   "which literally means 'me, it is Henri', and French expresses 'early' as 'in advance'."]),
 (4,
  "Où est l'ordinateur?",
  "'Where is the computer?' Notice how 'the' drops its vowel and joins onto the word for computer "
  'because it begins with a vowel sound.'),
 (5,
  'Ici, on utilise ce grand cahier en papier et un crayon.',
  "'Here we use this big paper notebook and a pencil.' Everyday spoken French reaches for that "
  "tiny two-letter word meaning 'one' whenever English says 'we'."),
 (7,
  None,
  "'Paper never loses the room list when it rains.' French uses two small negative words around "
  "'loses' to say 'never'. At the end, the expression for 'when the power goes out' is two short words."),
 (9,
  "Le client de la chambre quatre arrive aujourd'hui.",
  "'Room four arrives today.' Hotel rooms take 'four' right after 'the room', and the French word "
  "for 'today' literally packs 'on the day of today' into one word."),
 (11,
  None,
  "'Rule number one: drink hot tea first, then answer the bell.' French puts the colour or "
  "temperature word 'hot' after 'tea', not before it as English does.")]
