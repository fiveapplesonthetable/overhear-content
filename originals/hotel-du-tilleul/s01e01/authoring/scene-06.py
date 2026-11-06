# Authoring module for hotel-du-tilleul-s01e01-scene-06.
ID = 'hotel-du-tilleul-s01e01-scene-06'
SHOW = 'hotel-du-tilleul'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = "L'étiquette du bagage  (The Luggage Tag)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'claire': 'Claire', 'odette': 'Odette', 'etienne': 'Étienne'}
INTRO = ('Back at the front desk, Claire, Odette, and owner Etienne lean over the blue suitcase under the '
 'desk lamp. Etienne finally puts his glasses to good use. Listen to the scene first.')
OPENER = "Let's hear how they inspect the luggage tag and phone the station."
TRANSITION = "Now let's hear the whole scene again from start to finish."
OUTRO = ('No luck at the train station yet, and the mysterious owner lives just five minutes away. Next '
 "time, Nadia steps in to rescue Odette's evening.")
CLOSING = ('etienne', 'Bonne soirée!')
STORY = [('etienne',
  "Mon Dieu, quelle confusion! Laissez-moi regarder l'étiquette avec mes lunettes.",
  'Dear me, what a mix-up! Let me look at the tag with my glasses.'),
 ('odette',
  'Il y a un nom ou un numéro de téléphone dessus?',
  'Is there a name or a phone number on it?'),
 ('etienne',
  'Pas de numéro de téléphone, malheureusement. Seulement deux initiales et un vieux nom de rue.',
  'No phone number, unfortunately. Only two initials and an old street name.'),
 ('claire',
  'Attendez, cette rue est juste ici dans notre quartier, à cinq minutes!',
  'Wait, that street is right here in our neighbourhood, five minutes away!'),
 ('odette',
  "Comme c'est étrange! Nous avons pris le même train ce matin pour le même quartier.",
  'How strange! We rode the same train this morning to the same district.'),
 ('etienne',
  'Claire, appelez tout de suite le bureau des objets trouvés de la gare.',
  'Claire, call the station lost-and-found office right away.'),
 ('claire',
  "Je compose le numéro... Allô? Quelqu'un a signalé une valise bleue échangée?",
  'I am dialling the number... Hello? Did anyone report a swapped blue suitcase?'),
 ('odette',
  'Dites-leur que la mienne a un ruban rouge dans la poche du haut!',
  'Tell them mine has a red ribbon in the top pocket!'),
 ('claire',
  "Pas encore? Prenez le numéro et l'adresse de notre hôtel, s'il vous plaît. Merci!",
  'Not yet? Please take our guesthouse number and address. Thank you!'),
 ('etienne',
  "Ils n'ont rien pour l'instant, madame, je suis vraiment désolé.",
  'They have nothing for now, madam, I am truly sorry.'),
 ('odette',
  "Ce n'est pas votre faute. Mais je n'ai que le manteau sur mon dos!",
  'It is not your fault. Still, I only have the coat on my back!'),
 ('claire',
  'Un instant, Nadia vient de me faire signe depuis le café avec une idée!',
  'One moment, Nadia just waved to me from the cafe with an idea!')]
WALK = [(1,
  None,
  ["'Is there a name or a phone number on it?' At the end of the question,",
   (None, 'dessus?'),
   "packs 'on it' into one compact word so Odette does not have to repeat 'the tag'."]),
 (2,
  'Pas de numéro de téléphone, malheureusement.',
  "'No phone number, unfortunately.' In short answers without an action word, 'not of' is the "
  "crisp French way to say 'no' before a thing."),
 (3,
  None,
  "'Wait, that street is right here in our neighbourhood, five minutes away!' In French you say "
  "'at five minutes' for distance, without needing an extra word for 'away'."),
 (5,
  None,
  "'Claire, call the station lost-and-found office right away.' Notice how optimistic French is: "
  "where English says 'lost and found', French simply calls it 'the office of found objects'."),
 (6,
  'Je compose le numéro... Allô?',
  "'I am dialling the number... Hello?' In French, that telephone greeting is used strictly on the "
  'phone, never face to face in a room.'),
 (8,
  'Pas encore?',
  ["'Not yet?' Two tiny words,",
   (None, 'Pas encore?'),
   "literally 'not again' or 'not still', give you 'not yet' in any situation."]),
 (10,
  None,
  "'It is not your fault. Still, I only have the coat on my back!' Wrapping 'not... that' around "
  "'have' is how French says 'only', literally 'I do not have except the coat'."),
 (11,
  None,
  "'One moment, Nadia just waved to me from the cafe with an idea!' Using 'comes from' before an "
  "action means someone 'just' did it seconds ago.")]
