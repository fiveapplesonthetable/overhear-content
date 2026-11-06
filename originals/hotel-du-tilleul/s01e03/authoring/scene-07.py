# Authoring module for hotel-du-tilleul-s01e03-scene-07.
ID = 'hotel-du-tilleul-s01e03-scene-07'
SHOW = 'hotel-du-tilleul'
SEASON = 1
EPISODE = 3
SCENE = 7
TITLE = 'Le carnet rendu  (Returning the Notebook)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'claire': 'Claire', 'antoine': 'Antoine'}
INTRO = ("Claire climbs up to the attic door to return Antoine's forgotten leather notebook, trying hard "
 'to act normal despite thinking he is a secret hotel inspector. Listen first.')
OPENER = "Let's listen to their polite exchange at the attic door and that suspicious pipe sound."
TRANSITION = "Now let's listen to the whole conversation again from top to bottom."
OUTRO = ('Antoine got his notebook back without suspecting a thing, yet that cooling radiator is a warning '
 'sign. One final scene in Episode 3, down to the cellar! See you next time.')
CLOSING = ('antoine', 'Bonne nuit!')
STORY = [('claire',
  'Excusez-moi, Monsieur Antoine? Pardon de vous déranger.',
  'Excuse me, Mr Antoine? Sorry to disturb you.'),
 ('antoine',
  'Oh, mon carnet en cuir! Merci! Je le cherchais justement.',
  'Oh, my leather notebook! Thank you! I was just looking for it.'),
 ('claire',
  "Vous l'avez laissé près du bol de soupe sur le comptoir.",
  'You left it near the soup bowl on the counter.'),
 ('antoine',
  'Toutes mes notes de la semaine sont dedans. Vous me sauvez.',
  'All my notes from this week are inside. You saved me.'),
 ('claire',
  'Nous sommes ravis que notre cour soit paisible pour votre... travail.',
  'We are delighted that our courtyard is peaceful for your... work.'),
 ('antoine',
  "Très paisible! Mais vous avez entendu un drôle de choc métallique à l'instant?",
  'Very peaceful! Though did you hear a funny metallic knock just now?'),
 ('claire',
  'Oui! On dirait que ça vient du tuyau de chauffage dans le coin.',
  'Yes! It sounds like it comes from the heating pipe in the corner.'),
 ('antoine',
  'Touchez le radiateur: le haut est tiède, et le bas devient froid.',
  'Touch the radiator: the top is lukewarm, and the bottom is turning cold.'),
 ('claire',
  "Oh! Parfois les vieux tuyaux ont une petite bulle d'air la nuit.",
  'Oh! Sometimes old pipes have a little air bubble at night.'),
 ('antoine',
  "J'ai une bonne couverture chaude, alors je suis très bien ce soir.",
  'I have a good warm blanket, so I am very comfortable tonight.'),
 ('claire',
  'Merci pour votre patience! Henri va vérifier la cave tout de suite.',
  'Thank you for your patience! Henri is going to check the cellar right away.'),
 ('antoine',
  'Bonne nuit, Claire. À demain au petit-déjeuner.',
  'Good night, Claire. See you tomorrow at breakfast.')]
WALK = [(0,
  'Pardon de vous déranger.',
  ["'Sorry to disturb you.' Knocking on an office or guest-room door,",
   (None, 'Pardon de vous déranger.'),
   'is polite, natural, and effortless.']),
 (1,
  'Je le cherchais justement.',
  "'I was just looking for it.' French builds 'for' right inside 'search', so you 'search it' "
  "directly without an extra word for 'for'."),
 (5,
  None,
  "'Very peaceful! Though did you hear a funny metallic knock just now?' Placed before a thing "
  "with 'of', the word for 'funny' shifts meaning to 'strange' or 'odd'."),
 (6,
  'On dirait que ça vient du tuyau de chauffage dans le coin.',
  ["'It sounds like it comes from the heating pipe in the corner.' Starting an observation with",
   (None, 'On dirait que'),
   "literally 'one would say that', works for 'it looks like' and 'it sounds like' alike."]),
 (7,
  None,
  "'Touch the radiator: the top is lukewarm, and the bottom is turning cold.' Notice 'the high' "
  "and 'the low' act as 'the top' and 'the bottom'."),
 (9,
  None,
  "'I have a good warm blanket, so I am very comfortable tonight.' Saying simply 'I am well' means "
  "'I am comfortable' without needing a long word."),
 (11,
  'À demain au petit-déjeuner.',
  "'See you tomorrow at breakfast.' Literally 'until tomorrow', ready for every evening goodbye.")]
