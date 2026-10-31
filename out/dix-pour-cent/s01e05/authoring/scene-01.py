# Authoring module for dix-pour-cent-s01e05-scene-01.
ID = 'dix-pour-cent-s01e05-scene-01'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'Vous êtes en verre?  (Are You Made of Glass?)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'joey': 'JoeyStarr', 'julie': 'Julie', 'samir': 'Samir'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E05'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e05.fr.dual.srt'
INTRO = ('In episode five of Call My Agent, Julie Gayet and JoeyStarr are acting together in an eighteenth-century '
 'costume film. Julie plays an aristocrat, JoeyStarr a servant, and their argument is stopping the shoot. '
 'Their agents, Andrea and Gabriel, will have to help. Listen to the French first; you do not need to catch '
 'every word.')
OPENER = "Let's return to the first take. A grand declaration of love ends with a much less grand argument."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ('The director needs the agents because the two stars cannot work together. You have heard requests, '
 'complaints and a few very short instructions. See you next time.')
CLOSING = ('joey', 'À demain!')
STORY = [('joey', 'Madame.', 'Madam.', [(1, 'Madame')], ''),
 ('julie', "Non! Je n'y crois pas!", "No! I don't believe it!", [(2, "Non ! Je n'y crois pas")], ''),
 ('samir',
  "Coupez! Qu'est-ce qui se passe?",
  'Cut! What is going on?',
  [(4, 'Coupez'), (4, "Qu'est-ce qui se passe ?")],
  ''),
 ('julie',
  'Il la pousse dans les buissons.',
  'He pushes her into the bushes.',
  [(5, 'Il la pousse dans les buissons')],
  ''),
 ('joey', 'Vous êtes en verre?', 'Are you made of glass?', [(6, 'Vous êtes en verre ?')], ''),
 ('julie',
  'Non, je suis une aristocrate, il est serviteur.',
  'No, I am an aristocrat, he is a servant.',
  [(7, 'Non. Je suis une aristocrate, il est serviteur')],
  ''),
 ('julie',
  'Il doit faire preuve de respect.',
  'He has to show respect.',
  [(8, 'il doit'), (8, 'faire preuve de respect')],
  ''),
 ('joey', "Je travaille, d'accord?", "I'm working, okay?", [(10, 'je travaille'), (11, "D'accord")], ''),
 ('julie',
  "On pourrait avoir un peu de délicatesse et d'élégance dans cette scène?",
  'Could we have a little delicacy and elegance in this scene?',
  [(12, "On pourrait avoir un peu de délicatesse et d'élégance"), (13, 'dans cette scène ?')],
  ''),
 ('joey',
  "C'est pour moi? J'en ai marre.",
  "Is that aimed at me? I'm fed up.",
  [(14, "C'est pour moi ?"), (15, "J'en ai marre")],
  ''),
 ('julie', 'Moi aussi!', 'Me too!', [(16, 'Moi aussi')], ''),
 ('joey',
  'Allez à vos dîners mondains!',
  'Go to your high-society dinners!',
  [(17, 'Allez à vos dîners mondains !')],
  ''),
 ('julie',
  "Articulez, s'il vous plaît. Je ne comprends pas un mot.",
  "Articulate, please. I don't understand a word.",
  [(18, "Articulez, s'il vous plaît. Je ne comprends pas un mot")],
  ''),
 ('samir',
  'On a combien de retard?',
  'How far behind schedule are we?',
  [(20, 'On a combien de retard ?')],
  ''),
 ('samir',
  "Cinq jours. Je n'y crois pas!",
  "Five days. I don't believe it!",
  [(21, "Cinq jours. Je n'y crois pas !")],
  ''),
 ('samir',
  'Appelez leurs agents maintenant!',
  'Call their agents right now!',
  [(22, 'Appelez leurs agents maintenant !')],
  '')]
WALK = [(0,
  None,
  "'Madam.' This form of address fits a servant speaking to an aristocrat. It is also the ordinary "
  'respectful way to address a woman today.'),
 (1,
  None,
  "'No! I don't believe it!' The expression for not believing something also conveys astonishment. The small "
  'extra word points back to the situation she cannot believe.'),
 (2,
  None,
  "'Cut! What is going on?' The first word is an instruction. The question then uses an everyday expression "
  'for something happening, rather than for a person passing by.'),
 (3,
  None,
  "'He pushes her into the bushes.' The little word for her stands before the action. It tells us who gets "
  'pushed, rather than who does the pushing.'),
 (4,
  None,
  "'Are you made of glass?' French uses its word for in before a material here. The question is sarcastic: "
  'he thinks she is being too delicate.'),
 (5,
  None,
  "'No, I am an aristocrat, he is a servant.' Her character has higher social rank. Listen to how French can "
  'name a role without always using a word for a before it.'),
 (6,
  None,
  "'He has to show respect.' The expression literally says to make proof of respect. It is a way of saying "
  "that a quality should be visible in someone's behaviour."),
 (7,
  None,
  "'I'm working, okay?' The French action word needs no separate helper for an activity happening now. He "
  'presents the rough acting as part of his job.'),
 (8,
  None,
  "'Could we have a little delicacy and elegance in this scene?' Asking whether they could have something "
  'makes a demand sound more indirect. The complaint is still very pointed.'),
 (9,
  None,
  "'Is that aimed at me? I'm fed up.' The last expression means having had enough. Its small connecting word "
  'refers back to the thing causing the irritation.'),
 (10,
  None,
  "'Me too!' French uses a strong form of me for this short reply. No separate action word is needed to "
  'agree with the complaint.'),
 (11,
  None,
  "'Go to your high-society dinners!' Now JoeyStarr mocks Julie's social world. The instruction uses the "
  'same polite form that the stars have been using to address one another.'),
 (12,
  None,
  "'Speak clearly, please. I don't understand a word.' The word for a single word makes the denial emphatic. "
  'She claims to understand nothing at all.'),
 (13,
  None,
  "'How far behind schedule are we?' The question asks how much delay they have. French builds the thought "
  'with have, although English naturally asks how far behind they are.'),
 (14,
  None,
  "'Five days. I don't believe it!' The number comes before the thing being counted. This time the director "
  'is the one who cannot believe what he hears.'),
 (15,
  None,
  "'Call their agents right now!' The possessive means their, referring to the two stars. The final word "
  'makes the timing urgent.')]
