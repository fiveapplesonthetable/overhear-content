# Authoring module for dix-pour-cent-s01e04-scene-04.
ID = 'dix-pour-cent-s01e04-scene-04'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 4
SCENE = 4
TITLE = "Le film d'Augustin  (Augustin's Film)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'augustin': 'Augustin', 'mathias': 'Mathias', 'noemie': 'Noémie'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E04'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e04.fr.dual.srt'
INTRO = ('Mathias is meeting Augustin, a young internet comedy star preparing his first cinema film. Augustin wants an '
 'unknown actress for the lead, but Mathias hopes to get Audrey the role. First, listen to their conversation in '
 'French.')
OPENER = "Let's break it down. Noémie sets down the coffee on Mathias's desk as he compliments Augustin's script."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "Mathias hasn't even told Audrey about Augustin's film yet, and he certainly hasn't told her what kind of part it is. You'll catch every step of his trick when you watch. See you next time!"
CLOSING = ('augustin', 'Bonne journée!')
STORY = [('noemie', 'Voilà le café, Mathias.', 'Here is the coffee, Mathias.', [], ''),
 ('mathias',
  "Merci, Noémie. J'adore cette version finale.",
  'Thank you, Noémie. I love this final version.',
  [(93, "J'adore cette version finale")],
  'The thanks to Noémie bridges the newly written coffee line; the original thanks in cue 95 is Augustin’s reply '
  'to praise.'),
 ('mathias',
  "Je crois qu'on tient vraiment quelque chose.",
  'I think we really have something here.',
  [(94, "Je crois qu'on tient vraiment quelque chose")],
  ''),
 ('mathias',
  'Vous êtes toujours sûr pour le rôle principal féminin?',
  'Are you still sure about the female lead?',
  [(96, 'Vous êtes toujours sûr pour le rôle principal féminin ?')],
  ''),
 ('augustin',
  "Oui! Elle s'appelle Armelle Borzek. Elle est géniale!",
  "Yes! Her name is Armelle Borzek. She's brilliant!",
  [(97, 'Oui'), (98, 'Armelle Borzek'), (97, 'Elle est géniale !')],
  ''),
 ('augustin',
  'Retenez ce nom, elle est fantastique!',
  "Remember that name, she's fantastic!",
  [(100, 'Retenez ce nom, elle est fantastique !')],
  ''),
 ('mathias',
  'Mais le public ne la connaît pas.',
  "But the public doesn't know her.",
  [(102, 'Mais le public')],
  ''),
 ('augustin',
  "Dans mes vidéos en ligne, il n'y a pas de stars.",
  'In my online videos, there are no stars.',
  [(103, 'mes vidéos en ligne'), (104, 'Pas de stars')],
  ''),
 ('mathias',
  "C'est vrai. Mais le cinéma, ce n'est pas Internet.",
  "That's true. But cinema isn't the Internet.",
  [(105, "C'est vrai"), (106, 'Mais le cinéma'), (106, 'pas Internet')],
  ''),
 ('mathias',
  "Quand j'ai lu cette dernière version, j'ai pensé à Audrey Fleurot.",
  'When I read this latest version, I thought of Audrey Fleurot.',
  [(108, "Quand j'ai lu cette dernière version, j'ai pensé"), (109, 'Audrey Fleurot')],
  ''),
 ('augustin',
  'Audrey Fleurot? Pourquoi pas? Elle est sublime!',
  "Audrey Fleurot? Why not? She's sublime!",
  [(112, 'Audrey Fleurot'), (113, 'Pourquoi pas ?'), (114, 'Elle est sublime')],
  ''),
 ('mathias',
  'Elle attire le public, et elle aime vos vidéos.',
  'She draws the public, and she likes your videos.',
  [(119, 'elle attire le public'), (120, 'Et elle aime vos vidéos')],
  ''),
 ('augustin',
  'Attends! Audrey Fleurot a regardé mes vidéos?',
  'Wait! Audrey Fleurot watched my videos?',
  [(121, 'Attends !'), (122, 'Audrey Fleurot a regardé mes vidéos')],
  ''),
 ('augustin',
  "Elle t'a dit qu'elle les aimait? Vraiment?",
  'She told you she liked them? Really?',
  [(123, "Elle t'a dit qu'elle les aimait ?"), (124, 'Vraiment ?')],
  ''),
 ('noemie', 'Ne faites pas attention à moi.', "Don't mind me.", [(125, 'Ne faites pas attention à moi')], '')]
WALK = [(0, None, "'Here is the coffee, Mathias.' The first word is the handy pointer word for 'here is' or 'there is'."),
 (1,
  None,
  "'Thank you, Noémie. I love this final version.' The action word means 'to love' or 'to adore', very common in "
  'everyday French for things you really like.'),
 (2, None, "'I think we really have something here.' Literally 'we hold really something'."),
 (3,
  None,
  "'Are you still sure about the female lead?' Literally 'the main feminine role'. Now Mathias plants a doubt."),
 (4,
  None,
  "'Yes! Her name is Armelle Borzek. She's brilliant!' French gives a name with 'she calls herself'. You hear the "
  "same short word for 'she' again before the compliment."),
 (5,
  None,
  "'Remember that name, she's fantastic!' Augustin gives a polite command from the action word 'to retain' or 'to "
  "remember'."),
 (6, None, "'But the public doesn't know her.' The little word for 'her' sits right before the verb 'knows'."),
 (7, None, "'In my online videos, there are no stars.' Literally 'videos in line', the French phrase for online."),
 (8,
  None,
  "'That's true. But cinema isn't the Internet.' The first short phrase agrees with Augustin. The word for 'but' "
  "then signals Mathias's objection, followed by a negative around 'is'."),
 (9,
  None,
  "'When I read this latest version, I thought of Audrey Fleurot.' Both verbs are in the everyday past tense. To "
  "think of someone uses the preposition 'to'."),
 (10,
  None,
  "'Audrey Fleurot? Why not? She's sublime!' The short question is an encouraging suggestion. You can use the "
  'same two-word pattern when someone offers you an idea or an invitation.'),
 (11,
  None,
  "'She draws the public, and she likes your videos.' Notice the two different possessives: earlier Augustin said "
  "'my videos'; Mathias answers with the polite form of 'your'. His flattery seals the deal."),
 (12,
  None,
  "'Wait! Audrey Fleurot watched my videos?' In his excitement, Augustin drops the polite form and uses a casual "
  'command.'),
 (13,
  None,
  "'She told you she liked them? Really?' The short word before 'liked' means 'them', referring to the videos. "
  'French puts this object before the action, where English puts it afterwards.'),
 (14,
  None,
  "'Don't mind me.' Literally 'do not pay attention to me'. It is a polite command, with the negative around "
  "'do'. Augustin is dancing around the room when Noémie comes back.")]
