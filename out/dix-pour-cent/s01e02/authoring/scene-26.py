# Authoring module for dix-pour-cent-s01e02-scene-26.
ID = 'dix-pour-cent-s01e02-scene-26'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 2
SCENE = 26
TITLE = 'Adieu, Samuel  (Goodbye, Samuel)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'gabriel': 'Gabriel', 'francoise': 'Françoise', 'line': 'Line'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E02'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e02.fr.dual.srt'
INTRO = ("After Samuel's burial at Père-Lachaise, the agency holds a tribute. Gabriel welcomes the guests and "
 'introduces Françoise Fabian. Line Renaud then joins in with her own memories. Both actresses loved Samuel, '
 'but their rivalry colours the way they remember him. Listen first to their words of affection and loss.')
OPENER = "Let's go back through the tribute. Gabriel greets everyone and thanks them for coming."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ("That's the end of this scene. When you watch it, listen for the back-to-front way of saying 'we miss you'; "
 'both Françoise and Line use it. See you next time!')
CLOSING = ('francoise', 'Bonne journée!')
STORY = [('gabriel',
  "Bonsoir. Au nom d'ASK, je vous remercie d'être venus.",
  'Good evening. On behalf of ASK, thank you for coming.',
  [(713, 'Bonsoir'), (714, "Au nom d'ASK, je vous remercie d'être venus")],
  'Source video confirms Gabriel is the presenter, not Mathias.'),
 ('gabriel',
  'Je laisse la parole à une grande amie de Samuel, Françoise Fabian.',
  "I give the floor to a great friend of Samuel's, Françoise Fabian.",
  [(715, 'Je laisse la parole à une grande amie de Samuel'), (716, 'Françoise Fabian')],
  'Source video confirms Gabriel is the presenter, not Mathias.'),
 ('francoise',
  'Bonsoir. Il y a quelques semaines, je dînais avec Samuel.',
  'Good evening. A few weeks ago, I was having dinner with Samuel.',
  [(717, 'Bonsoir'), (718, 'Il y a quelques semaines, je dînais avec Samuel')],
  ''),
 ('francoise',
  'Il a dit quelque chose de merveilleux.',
  'He said something wonderful.',
  [(719, 'Il a dit quelque chose de merveilleux')],
  ''),
 ('francoise',
  'Vous, les acteurs, vous jouez pour ne pas grandir.',
  "You actors, you play so you don't grow up.",
  [(720, 'vous les acteurs'), (723, 'Vous jouez pour ne pas grandir')],
  ''),
 ('francoise',
  'Vous jouez pour ne pas mourir.',
  "You play so you don't die.",
  [(723, 'vous jouez pour ne pas mourir')],
  ''),
 ('francoise',
  'Samuel, tu nous manques terriblement.',
  'Samuel, we miss you terribly.',
  [(726, 'Tu nous manques terriblement')],
  ''),
 ('line',
  'Samou était plein de joie, libre!',
  'Samou was full of joy, free!',
  [(730, 'Samou était plein de joie, libre')],
  ''),
 ('line',
  'Comme on faisait la fête, dans le temps!',
  'How we used to party, back in the day!',
  [(732, 'Comme on faisait la fête, dans le temps')],
  ''),
 ('line', 'Tu nous manques, Samou.', 'We miss you, Samou.', [(735, 'Tu nous manques, Samou')], ''),
 ('line',
  'Mais je te promets une chose. Nous continuerons à rire.',
  "But I promise you one thing. We'll keep on laughing.",
  [(736, 'Mais je te promets une chose'), (737, 'Nous continuerons à rire')],
  ''),
 ('francoise',
  'Oui, il faut se battre contre le chagrin.',
  'Yes, we must fight against sorrow.',
  [(740, 'Oui, il faut se battre contre le chagrin')],
  ''),
 ('francoise',
  'Samuel aimait vraiment rire.',
  'Samuel really loved to laugh.',
  [(741, 'Samuel aimait vraiment rire')],
  ''),
 ('line',
  'Tu aimais une belle chanson. Celle-là surtout.',
  'You loved a beautiful song. This one most of all.',
  [(746, 'Tu aimais une belle chanson'), (747, 'celle-là surtout')],
  ''),
 ('line',
  "Tu disais que c'était notre chanson.",
  'You used to say it was our song.',
  [(748, "Tu disais que c'était")],
  '')]
WALK = [(0, 'Bonsoir.', "'Good evening.' Remember, this is the greeting for the evening."),
 (0,
  "Au nom d'ASK, je vous remercie d'être venus.",
  "'On behalf of ASK, thank you for coming.' Literally 'in the name of ASK, I thank you for having come'. A "
  'formal phrase for speeches.'),
 (1,
  None,
  "'I give the floor to a great friend of Samuel's, Françoise Fabian.' Literally 'I leave the word to'. The "
  "word for 'friend' has its feminine ending here, and so does 'great'."),
 (2, 'Bonsoir.', "'Good evening.' Françoise greets the room in the same way, simply and with dignity."),
 (2,
  'Il y a quelques semaines, je dînais avec Samuel.',
  "'A few weeks ago, I was having dinner with Samuel.' The same opening can mean there is or ago. Before a "
  'number of weeks, it places the dinner in the past; was having dinner sets the scene for what Samuel '
  'said.'),
 (3,
  None,
  "'He said something wonderful.' Has plus said presents one completed remark. Something is built from some "
  'and thing, with a short linking word before wonderful. The description tells us what kind of thing he '
  'said.'),
 (4,
  None,
  "'You actors, you play so you don't grow up.' Françoise quotes Samuel addressing actors as a group. Play "
  "links their profession with children's games. The purpose phrase explains what they hope to avoid: "
  'growing up.'),
 (5,
  None,
  "'You play so you don't die.' The same purpose pattern returns. The two words for not sit together before "
  'die, because they are denying that action rather than the earlier play.'),
 (6,
  None,
  "'Samuel, we miss you terribly.' Watch out, this one works back to front. In French you say 'you are "
  "missing to us'. The person who is missed is the subject."),
 (7,
  None,
  "'Samou was full of joy, free!' Line's pet name makes the memory intimate. Full of links the quality to "
  'joy; free adds another description of Samuel, rather than referring to a price.'),
 (8,
  None,
  "'How we used to party, back in the day!' The background past again, for something that happened again and "
  "again. Literally 'how we used to make the party'."),
 (9,
  None,
  "'We miss you, Samou.' The same back-to-front verb as in Françoise's speech: the two rivals are saying the "
  'same thing.'),
 (10,
  'Mais je te promets une chose.',
  "'But I promise you one thing.' She speaks to Samuel with the casual 'you', as to an old friend."),
 (10,
  'Nous continuerons à rire.',
  "'We'll keep on laughing.' This is the simple future: the verb 'continue' with a future ending. Line wants "
  'laughter, not tears.'),
 (11,
  None,
  "'Yes, we must fight against sorrow.' Françoise takes the floor back, with the expression for 'we must'. "
  'The word at the end is a strong one for grief.'),
 (12,
  None,
  "'Samuel really loved to laugh.' Loved followed directly by laugh describes something Samuel enjoyed. "
  "Really strengthens the memory. Françoise agrees with Line's image of him, while trying to add her own "
  'view of their friend.'),
 (13,
  None,
  "'You loved a beautiful song. This one most of all.' Line has the last word. The word for 'beautiful' is "
  'feminine, like the song.'),
 (14,
  None,
  "'You used to say it was our song.' Line uses two action words in the background past. Then the music "
  "starts, and the whole room sings Samuel's song together. Let's hear the whole farewell once more.")]
