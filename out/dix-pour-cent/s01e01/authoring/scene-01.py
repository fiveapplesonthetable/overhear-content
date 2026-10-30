# Authoring module for dix-pour-cent-s01e01-scene-01.
ID = 'dix-pour-cent-s01e01-scene-01'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Cécile est en retard  (Cécile Is Late)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'cecile': 'Cécile', 'gabriel': 'Gabriel', 'journaliste_photo': 'La journaliste'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = ('This is Call My Agent, a story about a Paris talent agency. Gabriel, an agent, is waiting at a hotel photo '
 'shoot for his client, the actress Cecile. She answers his call from a riding lesson, and a promising film '
 'offer will soon bring some bad news. Listen to the French story first; you do not need to catch every '
 'word.')
OPENER = "Let's go back through the scene. First, the agent needs to find his missing client."
TRANSITION = 'Listen once more for the questions, the apologies and the promise to call back.'
OUTRO = ('You have heard how to ask where someone is and say that you are late. Those short patterns are useful well '
 'beyond this photo shoot. See you next time.')
CLOSING = ('cecile', 'Bonne soirée!')
STORY = [('gabriel',
  'Cécile? Vous êtes où?',
  'Cecile? Where are you?',
  [(12, 'Cécile ?'), (13, 'Vous êtes où ?')],
  ''),
 ('cecile',
  "Gabriel! Je suis à mon cours d'équitation.",
  "Gabriel! I'm at my horse-riding lesson.",
  [(12, 'Gabriel !'), (17, "Je suis à mon cours d'équitation")],
  ''),
 ('gabriel',
  'On est au Westin. Tout le monde est là.',
  "We're at the Westin. Everyone is here.",
  [(14, 'On est au Westin'), (15, 'Tout le monde est là')],
  ''),
 ('cecile', 'Oh non! Je suis en retard.', "Oh no! I'm late.", [], ''),
 ('gabriel', 'Vous savez monter, non?', "You can ride, can't you?", [(19, 'vous saviez monter')], ''),
 ('cecile',
  "Oui, oui. J'ai juste besoin d'un petit cours.",
  'Yes, yes. I just need a little lesson.',
  [(22, "J'ai juste besoin d'un petit cours")],
  ''),
 ('gabriel',
  'Je peux vous faire confiance?',
  'Can I trust you?',
  [(26, 'Je peux vous faire confiance ?')],
  ''),
 ('cecile',
  'Oui. Je suis presque au point. Je vous rappelle.',
  "Yes. I've almost got it. I'll call you back.",
  [(27, 'Je suis presque au point'), (29, 'je vous rappelle')],
  ''),
 ('gabriel', 'Vous serez là quand?', 'When will you be here?', [(30, 'Vous serez là quand ?')], ''),
 ('cecile', 'Dans une heure.', 'In an hour.', [(30, 'Dans une heure')], ''),
 ('cecile',
  'Je suis désolée. Vraiment désolée.',
  "I'm sorry. Really sorry.",
  [(41, 'Je suis désolée'), (44, 'Vraiment désolée')],
  ''),
 ('journaliste_photo',
  'Vous tournez un film aux États-Unis?',
  'Are you making a film in the United States?',
  [(51, 'un film aux États-Unis')],
  ''),
 ('cecile',
  "Rien n'est signé. On attend l'appel.",
  "Nothing is signed. We're waiting for the call.",
  [(55, "Rien n'est signé"), (55, "On attend l'appel")],
  ''),
 ('cecile',
  "C'est le prochain film de Tarantino.",
  "It's Tarantino's next film.",
  [(57, "C'est le prochain film de Tarantino")],
  ''),
 ('journaliste_photo', 'Fantastique!', 'Fantastic!', [(58, 'Fantastique !')], ''),
 ('gabriel',
  "Tarantino ne prendra pas Cécile. Problème d'âge.",
  "Tarantino won't cast Cecile. A problem with her age.",
  [(63, 'Tarantino ne prendra pas Cécile'), (64, "Problème d'âge")],
  ''),
 ('cecile',
  "C'est comme un rêve pour moi.",
  "It's like a dream for me.",
  [(68, "C'est comme un rêve pour moi")],
  'Shortened from the interrupted source sentence.')]
WALK = [(0,
  'Vous êtes où?',
  "'Where are you?' The question word comes last in this everyday spoken question. The polite word for 'you' "
  'also fits the relationship between an agent and his client.'),
 (1,
  "Je suis à mon cours d'équitation.",
  "'I'm at my horse-riding lesson.' The possessive 'my' goes with a masculine noun meaning 'lesson'. It "
  "tells us about the lesson, rather than the speaker's gender."),
 (2,
  'On est au Westin.',
  "'We're at the hotel.' Here the French speaker includes the group in one short word. Although several "
  'people are waiting, the action word has a singular form. Listen to the short sound after it.'),
 (2,
  'Tout le monde est là.',
  "'Everyone is here.' The three-word expression for 'everyone' literally says 'all the world'. French "
  'treats that expression as singular.'),
 (3,
  None,
  "'Oh no! I'm late.' French uses a little expression meaning 'in lateness' where English says 'late'. Keep "
  'those last two words together when listening.'),
 (4,
  None,
  "'You can ride, can't you?' The word for 'know' followed by an action can mean knowing how to do it. The "
  "little 'no' at the end asks for reassurance."),
 (5,
  None,
  "'Yes, yes. I just need a little lesson.' French says 'have need of' where English simply says 'need'. The "
  "short word meaning 'just' makes the request sound smaller."),
 (6,
  None,
  "'Can I trust you?' The French expression literally says 'make trust'. The little word meaning 'you' comes "
  "before that expression, although English puts 'you' last."),
 (7,
  'Je suis presque au point.',
  "'I've almost got it.' The expression at the end means being ready or having something worked out. Saying "
  "'almost' leaves a little room for doubt."),
 (7,
  'Je vous rappelle.',
  "'I'll call you back.' French uses the present here for an immediate promise. The person being called is "
  'named before the action.'),
 (8,
  None,
  "'When will you be here?' This time the form of 'be' points to the future. Again the question word waits "
  'until the end.'),
 (9,
  None,
  "'In an hour.' The short word at the start locates a moment in the future. It does not say how long the "
  'journey lasts.'),
 (10,
  None,
  "'I'm sorry. Really sorry.' The written apology has an extra e for a woman. That extra letter makes no "
  'difference to the pronunciation here.'),
 (11,
  None,
  "'Are you making a film in the United States?' In this setting the French word for 'turn' means shooting a "
  'film. It is a useful second meaning to recognise.'),
 (12,
  None,
  "'Nothing is signed. We're waiting for the call.' The French equivalent of 'nothing' works with the small "
  "negative before 'is'. There is no extra word for 'not' after it."),
 (13,
  None,
  "'It's Tarantino's next film.' French puts 'next' before the thing described. The director's name then "
  "follows a word meaning 'of'."),
 (14,
  None,
  "'Fantastic!' This familiar word expresses the journalist's delight. Meanwhile, the agent receives some "
  'bad news.'),
 (15,
  'Tarantino ne prendra pas Cécile.',
  "'Tarantino won't cast Cecile.' The two short negative words surround the future action. In this film "
  "conversation, 'take' means choosing someone for a part."),
 (15,
  "Problème d'âge.",
  "'A problem with her age.' The preposition meaning 'of' loses its vowel before 'age'. Written together, "
  'they still contain two pieces.'),
 (16,
  None,
  "'It's like a dream for me.' The final word is the form of 'me' used after a word such as 'for'. She still "
  'has no idea about the bad news.')]
