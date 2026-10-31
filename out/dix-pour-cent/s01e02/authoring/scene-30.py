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
OUTRO = ('Andréa and Gabriel have found their way back to friendship. The promise to go with her makes his support '
 'concrete, and her hypothetical confession shows what he means to her. Listen again for the words that '
 'soften this conversation after their argument. See you next time!')
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
 ('gabriel',
  'Promis, je ne te laisserai pas toute seule.',
  "I promise I won't leave you all alone.",
  [(821, "Je ne t'abandonnerai pas")],
  'Restores actual future laisserai rather than the backtranslated abandonnerai. The purpose follows in the '
  'next line.'),
 ('gabriel',
  'Pour avoir un enfant.',
  'To have a child.',
  [(821, 'un enfant'), (822, "Je t'emmènerai en Hollande")],
  'Short neutral purpose clause for the source pour faire ton petit bébé à quarante ans. Removes an invented '
  'when-plus-future clause.'),
 ('gabriel',
  "Je t'accompagnerai en Hollande.",
  "I'll go with you to Holland.",
  [(821, 'un enfant'), (822, "Je t'emmènerai en Hollande")],
  'Actual French audio says accompagnerai, accompany or go with, not the backtranslated emmènerai, take '
  'along.'),
 ('andrea',
  'Oh, Gabriel! Tu es bête!',
  "Oh, Gabriel! You're silly!",
  [],
  'Neutral affectionate response replacing the original stronger expression.'),
 ('andrea',
  "Si tu n'étais pas là…",
  "If you weren't here…",
  [(824, "Sans toi, je crois que j'arrêterais ce métier")],
  'Restores original si tu n’étais pas là instead of backtranslated sans toi.'),
 ('andrea',
  "Je crois que j'aurais envie d'arrêter ce métier.",
  "I think I'd feel like quitting this job.",
  [(824, "Sans toi, je crois que j'arrêterais ce métier")],
  'Restores actual conditional avoir envie; omits des fois and un petit peu. The dual subtitles had invented '
  'conditional arrêterais.'),
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
  "'I promise I won't leave you all alone.' The opening promised works as a short commitment: I promise. "
  'Will leave puts the support in the future. All alone describes Andréa, so both words carry their feminine '
  'form.'),
 (6,
  None,
  "'To have a child.' To introduces the purpose of the promise before it. French uses the same short linking "
  'word as for when it introduces a purpose, followed by the action. He is promising she will not face it '
  'alone.'),
 (7,
  None,
  "'I'll go with you to Holland.' Go with means accompany someone, offering company and support. You "
  'attaches to the future action. The destination recalls their earlier conversation about a donor, and '
  'Gabriel turns it into a joke between friends.'),
 (8,
  None,
  "'Oh, Gabriel! You're silly!' Silly can sound affectionate when said with a smile. It has the same spoken "
  'and written ending when describing a man or a woman.'),
 (9,
  None,
  "'If you weren't here…' If opens an imagined situation. Weren't describes his absence as hypothetical. "
  'Here refers to his presence in her life and work, rather than only his seat beside her.'),
 (10,
  None,
  "'I think I'd feel like quitting this job.' Feel like is built from have, desire and the action. The would "
  'ending is on have, while quit stays in its basic form after the linking word. She imagines how she would '
  'feel without Gabriel.'),
 (11,
  None,
  "'Yes, Sue Ellen!' Gabriel answers the confession by using a familiar television character's name as a "
  "teasing nickname. He keeps the moment light rather than making another grand declaration. Let's hear the "
  'conversation again.')]
