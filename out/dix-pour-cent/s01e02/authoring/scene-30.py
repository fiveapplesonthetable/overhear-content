# Authoring module for dix-pour-cent-s01e02-scene-30.
ID = 'dix-pour-cent-s01e02-scene-30'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 2
SCENE = 30
TITLE = 'Désolée pour hier  (Sorry About Yesterday)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'gabriel': 'Gabriel'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E02'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e02.fr.dual.srt'
INTRO = ("The two actresses' casting problem has been solved, but Andréa and Gabriel still need to repair their "
 "friendship after yesterday's argument. At the tribute, they sit together away from the other guests. "
 'Andréa apologises, and Gabriel returns to their earlier conversation about her wish for a child. Listen '
 'first to their reconciliation.')
OPENER = "Let's go back through it. Andréa opens with an apology about yesterday."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ("And just like that, the two friends are back together. When you watch, listen for 'me too' and the future "
 "tense of 'to take': you'll hear them clearly now. See you next time!")
CLOSING = ('andrea', 'Bonne soirée!')
STORY = [('andrea',
  'Gabriel? Désolée pour hier.',
  'Gabriel? Sorry about yesterday.',
  [(818, 'Désolée pour hier')],
  ''),
 ('andrea',
  "Line Renaud, c'était une idée de génie.",
  'Line Renaud was a stroke of genius.',
  [(819, "Line Renaud, c'était une idée de génie")],
  ''),
 ('gabriel',
  'Merci, Andréa.',
  'Thank you, Andréa.',
  [],
  'Added brief acknowledgement in this condensed reconciliation.'),
 ('gabriel',
  'Moi aussi.',
  'Me too.',
  [(820, 'Moi aussi, je suis')],
  'Splits the original me too and apology at a natural phrase boundary.'),
 ('gabriel',
  'Je suis désolé.',
  "I'm sorry.",
  [(820, 'Moi aussi, je suis')],
  'The remainder of Gabriel’s apology.'),
 ('gabriel', "Je ne t'abandonnerai pas.", "I won't abandon you.", [(821, "Je ne t'abandonnerai pas")], ''),
 ('gabriel',
  'Quand tu voudras un enfant…',
  'When you want a child…',
  [(821, 'un enfant'), (822, "Je t'emmènerai en Hollande")],
  'Opening time clause of Gabriel’s promise; the next line completes it.'),
 ('gabriel',
  "Je t'emmènerai en Hollande.",
  "I'll take you to Holland.",
  [(821, 'un enfant'), (822, "Je t'emmènerai en Hollande")],
  'The main promise following the time clause.'),
 ('andrea',
  'Oh, Gabriel! Tu es bête!',
  "Oh, Gabriel! You're silly!",
  [],
  'Neutral affectionate response replacing the original stronger expression.'),
 ('andrea',
  'Sans toi…',
  'Without you…',
  [(824, "Sans toi, je crois que j'arrêterais ce métier")],
  'Separates the condition from the main statement at a natural pause.'),
 ('andrea',
  "Je crois que j'arrêterais ce métier.",
  "I think I'd quit this job.",
  [(824, "Sans toi, je crois que j'arrêterais ce métier")],
  'Main statement completing without you.'),
 ('gabriel', 'Oui, Sue Ellen!', 'Yes, Sue Ellen!', [(825, 'Oui, Sue Ellen')], '')]
WALK = [(0,
  None,
  "'Gabriel? Sorry about yesterday.' Sorry has a silent feminine ending because Andréa is speaking. About "
  'yesterday names the reason for the apology, without repeating what happened in their argument.'),
 (1,
  None,
  "'Line Renaud was a stroke of genius.' Literally, Line Renaud, it was an idea of genius. Andréa names the "
  'topic first and then describes the idea. She gives Gabriel credit for the choice she had dismissed.'),
 (2,
  None,
  "'Thank you, Andréa.' Thanks followed by a name makes a simple personal acknowledgement. Here it accepts "
  'her praise and helps move the conversation away from their argument.'),
 (3,
  None,
  "'Me too.' These two words let Gabriel say he feels the same. The opening me is the strong form used on "
  'its own; it is not the short me that attaches to an action.'),
 (4,
  None,
  "'I'm sorry.' Gabriel completes the thought from me too. His written sorry has no feminine ending, but it "
  "sounds exactly like Andréa's earlier apology."),
 (5,
  None,
  "'I won't abandon you.' The ending puts abandon in the future. The short you comes before it and "
  'identifies the person he promises to support. He takes back his angry remark about finding someone else.'),
 (6,
  None,
  "'When you want a child…' French uses will want after when here, even though ordinary English says when "
  'you want. The sentence points to a possible later time and leads into his promise.'),
 (7,
  None,
  "'I'll take you to Holland.' Take means take a person along, rather than carry an object. You comes before "
  'take. The destination recalls their earlier conversation about a donor; Gabriel turns that memory into a '
  'joke about supporting her.'),
 (8,
  None,
  "'Oh, Gabriel! You're silly!' Silly can sound affectionate when said with a smile. It has the same spoken "
  'and written ending when describing a man or a woman.'),
 (9,
  None,
  "'Without you…' Without introduces the person whose absence would change things. French uses the strong "
  'you after this word, the same form heard in and you or for you.'),
 (10,
  None,
  "'I think I'd quit this job.' The ending on quit makes this a hypothetical result of being without "
  'Gabriel. This job means the profession of being an agent, rather than one particular task.'),
 (11,
  None,
  "'Yes, Sue Ellen!' Gabriel answers the confession by using a familiar television character's name as a "
  "teasing nickname. He keeps the moment light rather than making another grand declaration. Let's hear the "
  'conversation again.')]
