# Authoring module for dix-pour-cent-s01e02-scene-17.
ID = 'dix-pour-cent-s01e02-scene-17'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 2
SCENE = 17
TITLE = 'Line et Françoise, une vieille histoire  (Line and Françoise, an Old Story)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'arlette': 'Arlette', 'andrea': 'Andréa'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E02'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e02.fr.dual.srt'
INTRO = ("Arlette and Andréa are still at the café after discussing the agency's future. Arlette finds Gabriel's "
 "suggestion of replacing Françoise with Line amusing, given the actresses' shared history. She explains "
 'their long rivalry, and Andréa learns details she had not heard before. Listen to their conversation in '
 'French first.')
OPENER = "Let's go through it together. Hervé starts with a word that means bold, a little too bold."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ('Arlette has explained both an old falling-out and two careers that each actress envies. Listen again for '
 'how French talks about understanding a person, introducing someone, and no longer speaking. See you next '
 'time!')
CLOSING = ('arlette', 'À bientôt!')
STORY = [('arlette',
  "C'est cocasse, quand même!",
  "It's funny, all the same!",
  [(491, "C'est culotté de la part de Gabriel")],
  'Original French audio uses cocasse, oddly funny, not the dual subtitles’ culotté, cheeky. Omits the '
  'following clause naming Gabriel’s casting suggestion.'),
 ('andrea',
  'Tu trouves ça cocasse?',
  "You think it's funny?",
  [(492, 'Tu trouves ça culotté')],
  'Restores the original cocasse in Andréa’s sceptical question.'),
 ('arlette',
  'Oui! Il y a une vieille histoire entre Line et Françoise.',
  "Yes! There's an old story between Line and Françoise.",
  [(495, 'histoire entre Line et Françoise')],
  'Turns the source condition about knowing the history into an explicit statement that there is an old '
  'history.'),
 ('andrea', 'Quelle histoire?', 'What story?', [(496, 'Quelle histoire')], ''),
 ('arlette',
  'Elles ne peuvent pas se sentir.',
  "They can't stand each other.",
  [(497, 'Elles ne peuvent pas se sentir')],
  'Neutral equivalent of the original informal Elles ne peuvent pas se piffer, they cannot stand each '
  'other.'),
 ('andrea',
  "Ah bon? Je n'ai jamais entendu ça.",
  "Really? I've never heard that.",
  [(498, "Ah bon ? Je n'ai jamais entendu ça")],
  ''),
 ('arlette',
  'Line était une chanteuse connue. Françoise était une jeune actrice.',
  'Line was a well-known singer. Françoise was a young actress.',
  [(502, 'Line était une chanteuse connue')],
  'Simplifies the conservatoire background to being a young actress.'),
 ('arlette',
  'Françoise avait un amoureux. Devine qui!',
  'Françoise had a boyfriend. Guess who!',
  [(504, 'Françoise'), (505, 'Devinez qui')],
  'Summarises the romantic connection confirmed in the next exchange; original French audio restores '
  'familiar Devine qui, rather than the dual subtitle’s formal Devinez.'),
 ('andrea', 'Je ne sais pas.', "I don't know.", [(506, 'Je ne sais pas')], ''),
 ('arlette', 'Samuel!', 'Samuel!', [(507, 'Samuel')], ''),
 ('andrea',
  'Françoise était avec Samuel?',
  'Françoise was with Samuel?',
  [(508, 'Françoise était avec Samuel')],
  ''),
 ('arlette',
  'Oui! Et un jour, elle le présente à Line.',
  'Yes! And one day, she introduces him to Line.',
  [(508, 'Oui'), (509, 'elle le présente à Line')],
  'Uses an affirmative sentence in place of until she introduced him.'),
 ('arlette',
  'Depuis, les deux femmes ne se parlent plus.',
  "Since then, the two women don't speak to each other any more.",
  [(512, 'Les deux femmes')],
  'Summarises their falling-out and never reconciling as no longer speaking.'),
 ('arlette',
  "Line est devenue une star, et Françoise a fait du cinéma d'auteur.",
  'Line became a star, and Françoise worked in art-house cinema.',
  [(514, 'Line est devenue une star'), (515, "cinéma d'auteur")],
  ''),
 ('arlette',
  'Au fond, Françoise aurait aimé être chanteuse.',
  'Deep down, Françoise would have liked to be a singer.',
  [(517, 'Au fond'), (518, 'Françoise aurait aimé être chanteuse')],
  ''),
 ('arlette',
  'Et Line, une actrice de cinéma.',
  'And Line, a film actress.',
  [(519, 'Et Line, une actrice')],
  'Simplifies an actress of the French New Wave to a film actress.'),
 ('andrea', "Chacune déteste l'autre?", 'Each one hates the other?', [(520, "Chacune déteste l'autre")], ''),
 ('arlette', 'Exactement.', 'Exactly.', [(521, 'Exactement')], '')]
WALK = [(0,
  None,
  "'It's funny, all the same!' Funny here means oddly amusing, rather than a deliberately told joke. All the "
  "same adds emphasis to Arlette's reaction. She sees an irony in choosing Line to replace Françoise, "
  'because she knows their history.'),
 (1,
  None,
  "'You think it's funny?' Find can express an opinion, as in do you find it funny? That points to Gabriel's "
  "casting suggestion. Andréa's question challenges Arlette's reaction and invites her to explain it."),
 (2,
  None,
  "'Yes! There's an old story between Line and Françoise.' Three little words at the start mean 'there is'. "
  "You'll hear them constantly."),
 (3,
  None,
  "'What story?' This question word agrees with the word; story is feminine, so it takes the feminine "
  'spelling, though it sounds the same.'),
 (4,
  None,
  "'They can't stand each other.' Literally 'they can't smell each other'. The little self-directed word "
  "makes it mutual: each other. That's the first language point of the scene."),
 (5,
  None,
  "'Really? I've never heard that.' The word for 'never' takes the place of the usual 'not' in the two-part "
  'negative. Arlette settles in to tell the story.'),
 (6,
  None,
  "'Line was a well-known singer. Françoise was a young actress.' The past descriptions give the background "
  'before the particular events. Both singer and actress are feminine here, and the words describing them '
  'take feminine endings too.'),
 (7,
  None,
  "'Françoise had a boyfriend. Guess who!' Had describes a relationship that existed then. Arlette follows "
  "it with a playful invitation to guess the man's identity, rather than naming him immediately."),
 (8, None, "'I don't know.' The classic two-part negative around the verb 'to know'."),
 (9,
  None,
  "'Samuel!' The surprise is a name, so it needs no sentence around it. It answers who: Samuel, the agency "
  "founder who has just died, was Françoise's partner."),
 (10,
  None,
  "'Françoise was with Samuel?' To be 'with' someone means to be their partner, in French as in English. "
  'Andréa is amazed.'),
 (11,
  None,
  "'Yes! And one day, she introduces him to Line.' The little word for him comes before introduces; to then "
  'introduces the person meeting him. The present makes that turning point vivid in a story about the past.'),
 (12,
  None,
  "'Since then, the two women don't speak to each other any more.' The reflexive word again, for 'each "
  "other', and the negative with 'any more' at the end."),
 (13,
  None,
  "'Line became a star, and Françoise worked in art-house cinema.' Became describes a change in what Line "
  'was. The phrase for art-house cinema identifies the kind of career Françoise made, rather than saying she '
  'personally directed the films.'),
 (14,
  None,
  "'Deep down, Françoise would have liked to be a singer.' Would have liked looks back on an unrealised "
  'wish. Deep down introduces an underlying feeling, even if the person does not openly admit it.'),
 (15,
  None,
  "'And Line, a film actress.' Arlette doesn't repeat the verb; we understand it: Line would have liked to "
  'be an actress.'),
 (16,
  None,
  "'Each one hates the other?' Each one has a feminine ending for the two women and still takes a singular "
  'action word. The full source question links their hostility to envy: each had the career the other did '
  'not.'),
 (17,
  None,
  "'Exactly.' Arlette confirms Andréa's explanation of the rivalry. This single word can endorse a whole "
  "account without repeating it. Now let's hear the story once more.")]
