# Authoring module for hotel-du-tilleul-s01e01-scene-03.
ID = 'hotel-du-tilleul-s01e01-scene-03'
SHOW = 'hotel-du-tilleul'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = 'Où sont mes lunettes?  (Where Are My Glasses?)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'etienne': 'Étienne', 'claire': 'Claire', 'henri': 'Henri'}
INTRO = ('Before the first guest arrives, guesthouse owner Etienne hurries in from the courtyard looking '
 'flustered. Claire and Henri watch as Etienne searches his pockets in a panic. Listen to the '
 'whole scene first.')
OPENER = "Let's walk through Etienne's morning panic and his missing glasses."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = ('Etienne found his glasses on his own forehead just as the taxi pulled up outside. Relax and let '
 'the rhythm of the words sink in; see you next time.')
CLOSING = ('etienne', "À tout à l'heure!")
STORY = [('etienne',
  'Bonjour à tous! Bienvenue, Claire. Tout est prêt?',
  'Good morning, everyone! Welcome, Claire. Is everything ready?'),
 ('claire',
  'Bonjour, monsieur! Oui, le bureau est propre et les clés sont prêtes.',
  'Good morning, sir! Yes, the desk is clean and the keys are ready.'),
 ('etienne',
  'La cliente de la chambre quatre reste toute la semaine. Tout doit être parfait!',
  'The guest in room four is staying all week. Everything must be perfect!'),
 ('henri',
  'Calmez-vous, Étienne. La chambre est propre et les serviettes sont fraîches.',
  'Relax, Etienne. The room is clean and the towels are fresh.'),
 ('etienne',
  'Je dois lire le cahier de réservations, mais je ne trouve pas mes lunettes!',
  'I need to read the reservation book, but I cannot find my glasses!'),
 ('claire', 'Elles sont dans la poche de votre manteau?', 'Are they in your coat pocket?'),
 ('etienne',
  'Non, seulement mon stylo et trois vieux tickets!',
  'No, only my pen and three old receipts!'),
 ('henri',
  'Regardez dans le miroir derrière le comptoir, patron.',
  'Look in the mirror behind the counter, boss.'),
 ('etienne',
  'Pourquoi mes lunettes seraient... oh! Elles sont sur ma tête!',
  'Why would my glasses be... oh! They are on my head!'),
 ('claire',
  'Juste là sur votre front, bien au chaud.',
  'Right there on your forehead, safe and sound.'),
 ('etienne',
  'Ne dites rien à personne! Maintenant, un grand sourire quand la cloche sonne.',
  'Do not tell anyone! Now, a big smile when the bell rings.'),
 ('henri',
  "Voilà un taxi devant le portail à l'instant.",
  'Here comes a taxi in front of the gate right now.')]
WALK = [(0,
  'Bonjour à tous! Bienvenue, Claire.',
  "'Good morning, everyone! Welcome, Claire.' Adding 'to all' after 'good morning' is a natural "
  'way to greet a whole room at once.'),
 (1,
  None,
  "'Good morning, sir! Yes, the desk is clean and the keys are ready.' Hear how 'ready' gains a "
  "spoken 't' sound at the end because 'keys' is feminine plural."),
 (2,
  'La cliente de la chambre quatre reste toute la semaine.',
  ["'The guest in room four is staying all week.' That feminine ending on",
   (None, 'La cliente'),
   'tells us right away the expected guest is a woman.']),
 (4,
  None,
  "'I need to read the reservation book, but I cannot find my glasses!' Where English says 'I "
  "cannot find', French simply uses the present of 'find' in the negative: 'I do not find'."),
 (5,
  None,
  "'Are they in your coat pocket?' Because 'glasses' is feminine plural in French, Claire refers "
  "to them as 'she-plural' rather than 'they' neutral, and reverses 'coat pocket' into 'the pocket "
  "of your coat'."),
 (7,
  None,
  ["'Look in the mirror behind the counter, boss.' Even while teasing Etienne, Henri uses the "
   'polite command',
   (None, 'Regardez'),
   "paired with the affectionate word for 'boss'."]),
 (8,
  'Elles sont sur ma tête!',
  "'They are on my head!' Notice that 'my' matches the feminine word 'head', not Etienne himself."),
 (10,
  'Ne dites rien à personne!',
  "'Do not tell anyone!' French piles up 'nothing' and 'to nobody' in the same sentence, literally "
  "'say nothing to nobody', and that is completely standard."),
 (11,
  None,
  "'Here comes a taxi in front of the gate right now.' Starting with the pointing word for 'here "
  "is' lets Henri spot the arriving car without needing an action word at all.")]
