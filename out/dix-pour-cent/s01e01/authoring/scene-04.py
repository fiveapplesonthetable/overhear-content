# Authoring module for dix-pour-cent-s01e01-scene-04.
ID = 'dix-pour-cent-s01e01-scene-04'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'Un nouveau caprice?  (Another Whim?)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = ('Mathias greets Camille at the agency, then continues their conversation at a restaurant. He orders coffee, '
 'she asks for tea, and they begin to talk about her plans in Paris. Listen to the polite order and the much '
 'more familiar conversation that follows.')
OPENER = ("Let's go through the meeting. Mathias first greets Camille at the agency; at the restaurant, a waiter "
 'takes their drinks order.')
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ('You have heard a polite order to a waiter and a familiar conversation between people who know each other '
 'well. The word for you changes with the person being addressed. See you next time.')
CLOSING = ('camille', 'Salut, Mathias!')
STORY = [('mathias',
  'Bonjour, Camille. Entrez.',
  'Hello, Camille. Come in.',
  [(123, 'Bonjour, Camille'), (124, 'Entrez')],
  ''),
 ('mathias', "Un café, s'il vous plaît.", 'A coffee, please.', [(125, "Un café, s'il vous plaît")], ''),
 ('camille', 'Un thé.', 'Tea.', [(126, 'Un thé ?')], 'Order punctuated as a short statement.'),
 ('mathias',
  "Pourquoi tu n'as pas appelé?",
  "Why didn't you call?",
  [(128, "Pourquoi tu n'as pas appelé ?")],
  ''),
 ('camille',
  'Je ne sais pas. Je voulais te faire la surprise.',
  "I don't know. I wanted to surprise you.",
  [(129, 'Je sais pas'), (129, 'Je voulais te faire la surprise')],
  ''),
 ('camille',
  "C'est sympa ici. Des sucettes gratuites!",
  "It's nice here. Free lollipops!",
  [(133, "C'est sympa ici"), (134, 'Des sucettes gratuites')],
  ''),
 ('mathias',
  "C'est du sucre pour le café.",
  "It's sugar for the coffee.",
  [(135, "C'est du sucre pour le café")],
  ''),
 ('mathias',
  "Qu'est-ce que tu fais à Paris? Tu es en vacances?",
  'What are you doing in Paris? Are you on holiday?',
  [(137, "Qu'est-ce que tu fais à Paris ? Tu es en vacances ?")],
  ''),
 ('camille',
  'En quelque sorte. Ça fait trois semaines que je suis là.',
  "Sort of. I've been here for three weeks.",
  [(138, 'En quelque sorte'), (139, 'Ça fait trois semaines que je suis là')],
  ''),
 ('mathias',
  "Tu n'aimais pas Mandelieu? C'est un bel endroit.",
  "Didn't you like Mandelieu? It's a lovely place.",
  [(141, "Tu n'aimais pas"), (141, 'Mandelieu'), (142, "C'est un bel endroit")],
  ''),
 ('camille',
  "J'ai un petit loft. Et je cherche du boulot.",
  "I've got a little loft. And I'm looking for work.",
  [(150, 'un petit loft'), (151, 'Et je cherche du boulot')],
  ''),
 ('camille',
  "Tu connais beaucoup de monde dans le cinéma. Tu pourrais m'aider.",
  'You know a lot of people in the film industry. You could help me.',
  [(152, 'tu connais beaucoup de monde dans le cinéma'), (153, "tu pourrais m'aider")],
  ''),
 ('mathias', 'Un nouveau caprice?', 'Another whim?', [(154, 'Un nouveau caprice ?')], ''),
 ('camille',
  "Je suis sérieuse. J'ai toujours adoré le cinéma.",
  "I'm serious. I've always loved films.",
  [(155, 'je suis sérieuse'), (156, "J'ai toujours adoré le cinéma")],
  ''),
 ('mathias',
  "Écoute, c'est une industrie, et elle est pleine de requins.",
  "Listen, it's an industry, and it's full of sharks.",
  [(161, 'Écoute'), (163, "C'est une industrie"), (164, 'et elle est pleine de requins')],
  ''),
 ('mathias',
  "Désolé, c'est tout ce que je peux faire.",
  "Sorry, that's all I can do.",
  [(170, "Désolé, c'est tout ce que je peux faire")],
  '')]
WALK = [(0,
  'Bonjour, Camille.',
  "'Hello, Camille.' A greeting followed directly by someone's name is enough to welcome them. Mathias keeps "
  'his tone reserved.'),
 (0,
  'Entrez.',
  "'Come in.' This command is in the formal form, as if she were a stranger. Remember that, because it won't "
  'last.'),
 (1,
  None,
  "'A coffee, please.' The last part literally means 'if it pleases you', with the formal 'you'; it's the "
  "standard way to say please to anyone you don't know."),
 (2,
  None,
  "'Tea.' Camille names her drink in one short group. The little word before it means 'a', as in Mathias's "
  'coffee order. A complete sentence is unnecessary when the waiter is taking an order.'),
 (3,
  None,
  "'Why didn't you call?' The question begins with 'why'. Mathias has switched to the familiar 'you', and "
  "the two little negatives surround the helping verb meaning 'have'."),
 (4,
  'Je voulais te faire la surprise.',
  "'I wanted to surprise you.' Camille answers with the casual 'you' too; the small word for 'you' sits "
  'right before the verb.'),
 (5,
  None,
  "'It's nice here. Free lollipops!' At the restaurant table, Camille mistakes the wrapped sugar sticks for "
  "sweets. The informal description 'nice' fits her cheerful first impression."),
 (6,
  None,
  "'It's sugar for the coffee.' The little word before 'sugar' names an unspecified amount. Mathias points "
  'out what the sticks really are.'),
 (7,
  None,
  "'What are you doing in Paris? Are you on holiday?' The opening question expression asks 'what'. The "
  'holiday noun in this expression normally has a plural form, although English uses the singular.'),
 (8,
  'Ça fait trois semaines que je suis là.',
  "'I've been here for three weeks.' French uses the present tense for this: literally 'it makes three weeks "
  "that I am here'. She has moved to Paris without telling him."),
 (9,
  None,
  "'Didn't you like Mandelieu? It's a lovely place.' Listen to the ending of the description 'lovely'. "
  'Before a masculine word beginning with a vowel, it has a special short form.'),
 (10,
  None,
  "'I've got a little loft. And I'm looking for work.' The word for work here is a casual one, like 'a "
  "job'."),
 (11,
  "Tu pourrais m'aider.",
  "'You could help me.' This is the gentle, polite 'could'. She hopes he'll use his contacts in the film "
  'business.'),
 (12,
  None,
  "'Another whim?' The adjective means 'new', but 'another' captures his impatient tone. Its ending matches "
  'a masculine noun.'),
 (13,
  'Je suis sérieuse.',
  "'I'm serious.' The word for 'serious' takes a feminine ending, because Camille is a woman. The man's "
  'version ends differently.'),
 (13,
  "J'ai toujours adoré le cinéma.",
  "'I've always loved films.' The word for 'always' fits between 'have' and the past action. Here the French "
  'word for cinema includes films and the world of film-making.'),
 (14,
  None,
  "'Listen, it's an industry, and it's full of sharks.' The word for 'full' has a feminine ending to match "
  "'industry'. The sharks are a warning about the people in that business."),
 (15,
  None,
  "'Sorry, that's all I can do.' The last action is left in its plain form after 'can'. The apology makes "
  'his refusal sound gentler, but he still offers no help.')]
