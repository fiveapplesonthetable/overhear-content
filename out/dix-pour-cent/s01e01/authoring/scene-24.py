# Authoring module for dix-pour-cent-s01e01-scene-24.
ID = 'dix-pour-cent-s01e01-scene-24'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 24
TITLE = 'Mathias au jardin  (Mathias in the Garden)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'cecile': 'Cécile', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = ('After his meeting with Miranda, Mathias visits Cecile at home. She has left Gabriel and distrusts agents, '
 'but she lets Mathias join her in the garden. Hear the French first and follow the change in her mood.')
OPENER = "Let's go through the visit. Cecile welcomes Mathias, but she is not yet ready to trust another agent."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ('You have heard an apology and several requests for help; listen again for the polite forms and the small '
 'words naming who is helped. See you next time.')
CLOSING = ('cecile', 'À bientôt, Mathias!')
STORY = [('cecile',
  'Bonjour, Mathias. Entrez.',
  'Hello, Mathias. Come in.',
  [(651, 'Bonjour, Mathias'), (652, 'Entrez')],
  ''),
 ('mathias', 'Cécile.', 'Cecile.', [(651, 'Cécile')], ''),
 ('cecile',
  'Je jardine. Vous venez?',
  "I'm gardening. Are you coming?",
  [(656, 'Je jardine. Vous venez')],
  ''),
 ('mathias',
  "Au nom de l'agence, je vous présente mes excuses.",
  'On behalf of the agency, I apologise.',
  [(657, "Au nom de l'agence, je vous présente mes excuses")],
  ''),
 ('cecile',
  "Vous voulez me récupérer, mais il n'y a aucune chance.",
  'You want to win me back, but there is no chance.',
  [(659, 'Je sais que vous êtes là pour me récupérer'), (660, "il n'y a aucune chance")],
  'Shortened or rephrased from the cited source dialogue.'),
 ('mathias',
  'Vous allez signer avec StarMédia?',
  'Are you going to sign with StarMédia?',
  [(661, 'Tu vas signer avec StarMédia')],
  'Formal address follows the checked original French audio; the paired SRT is a reconstruction.'),
 ('cecile',
  'Je ne sais pas. Tout le monde ment dans ce milieu.',
  "I don't know. Everyone lies in this business.",
  [(661, 'sais pas'), (663, 'Tout le monde ment dans ce milieu')],
  'Shortened or rephrased from the cited source dialogue.'),
 ('cecile',
  'Vous pouvez me donner un coup de main?',
  'Can you give me a hand?',
  [(665, 'Tu peux me donner un coup de main')],
  'Formal address follows the checked original French audio; the paired SRT is a reconstruction.'),
 ('mathias',
  'Oui, bien sûr.',
  'Yes, of course.',
  [(665, 'Oui')],
  'Shortened or rephrased from the cited source dialogue.'),
 ('cecile',
  'Passez-moi le seau.',
  'Hand me the bucket.',
  [(667, 'Passe-moi le seau')],
  'Formal address follows the checked original French audio; the paired SRT is a reconstruction.'),
 ('mathias', 'Le seau? Ah, oui.', 'The bucket? Oh, yes.', [(667, 'Le seau'), (668, 'Ah, oui')], ''),
 ('cecile',
  "C'est du compost. Ça nourrit la terre.",
  "It's compost. It feeds the earth.",
  [(669, "c'est du compost"), (670, 'Ça nourrit la terre')],
  ''),
 ('cecile',
  'La terre, elle est vraie. Elle ne sait pas mentir.',
  "The earth is genuine. It doesn't know how to lie.",
  [(671, 'La terre, elle est vraie'), (671, 'sait pas mentir')],
  'Shortened or rephrased from the cited source dialogue.'),
 ('mathias',
  'Écoutez, Cécile. Je comprends votre déception.',
  'Listen, Cécile. I understand your disappointment.',
  [(672, 'Écoute, Cécile'), (673, 'Je comprends ta déception')],
  'Formal address follows the checked original French audio; the paired SRT is a reconstruction.'),
 ('mathias', "J'ai parlé à Miranda.", 'I talked to Miranda.', [(675, "j'ai parlé à Miranda")], ''),
 ('mathias',
  'Ils sont prêts à en discuter.',
  "They're ready to talk about it.",
  [(676, 'Ils sont prêts à en discuter')],
  ''),
 ('cecile',
  "Ah bon? Qu'est-ce qu'elle a dit?",
  'Really? What did she say?',
  [(678, 'Ah bon'), (679, "Qu'est-ce qu'elle a dit")],
  '')]
WALK = [(0,
  None,
  "'Hello, Mathias. Come in.' The polite instruction begins straight with the action, without a separate "
  "word for 'you'. It welcomes Mathias inside."),
 (1,
  None,
  "'Cecile.' Mathias answers her greeting with her first name. They know each other through the agency."),
 (2,
  'Je jardine. Vous venez?',
  "'I'm gardening. Are you coming?' French has no separate 'I am doing' form: 'I garden' also means 'I'm "
  "gardening'. Out in the garden, Mathias starts with an apology."),
 (3,
  None,
  "'On behalf of the agency, I apologise.' Literally, he presents his apologies 'in the name of' the agency. "
  'The French apology noun is plural in this formal expression.'),
 (4,
  None,
  "'You want to win me back, but there is no chance.' The action meaning 'get back' can refer to recovering "
  'a client. Cecile recognises exactly why he has come.'),
 (4,
  None,
  "'You want to win me back, but there is no chance.' In the second half, the expression for 'there is' "
  "becomes negative. The word before 'chance' means 'not a single'."),
 (5,
  None,
  "'Are you going to sign with StarMedia?' The polite form of 'go' comes before the action 'sign', showing a "
  "plan. The small word linking it to the agency means 'with'."),
 (6,
  'Je ne sais pas.',
  "'I don't know.' The negative wraps around the action word in two parts. In everyday speech the French "
  'often drop the first part, and Cécile does in the show, but the full form is the one to learn.'),
 (6,
  'Tout le monde ment dans ce milieu.',
  "'Everyone lies in this business.' Literally 'all the world lies in this circle'. That's a dig at Gabriel, "
  'and at agents in general.'),
 (7,
  None,
  "'Can you give me a hand?' The expression asks for help, rather than a body part. Cecile keeps the polite "
  "'you' when she asks Mathias to help with the garden."),
 (8,
  None,
  "'Yes, of course.' The final two words make a useful reply on their own. Mathias agrees readily to her "
  'request for help.'),
 (9,
  None,
  "'Hand me the bucket.' In this polite instruction, 'me' attaches after the action with a hyphen. In an "
  'ordinary statement it would come before the action.'),
 (10,
  None,
  "'The bucket? Oh, yes.' The little definite article is masculine, matching 'bucket'. Mathias repeats her "
  'request while working out what she wants.'),
 (11,
  None,
  "'It's compost. It feeds the earth.' The first little word before compost means 'some', because you can't "
  'count compost. The man in the elegant suit is carrying a bucket of it.'),
 (12,
  'La terre, elle est vraie.',
  "'The earth is honest.' Literally 'the earth, it is true'. French often names the thing first and then "
  'repeats it with a short stand-in word.'),
 (12,
  'Elle ne sait pas mentir.',
  "'It doesn't know how to lie.' After the verb for 'to know how' comes an infinitive: 'to lie'. Unlike "
  'people, she means. Mathias puts on his gentle voice.'),
 (13,
  None,
  "'Listen, Cecile. I understand your disappointment.' The first word is a polite instruction. The word "
  "meaning 'your' also keeps their conversation polite."),
 (14,
  None,
  "'I talked to Miranda.' This is the past tense with 'have' plus the past form of 'talk'. Miranda is the "
  'producer who said Cécile was too old.'),
 (15,
  None,
  "'They're ready to talk about it.' The tiny word in front of the verb means 'about it'. And that changes "
  'everything for Cécile.'),
 (16,
  None,
  "'Really? What did she say?' The first two words show surprise, a bit like 'oh really?'. Suddenly she is "
  "listening very closely. Let's listen to the whole scene again, in one go.")]
