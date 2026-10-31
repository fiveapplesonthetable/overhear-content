# Authoring module for dix-pour-cent-s01e02-scene-29.
ID = 'dix-pour-cent-s01e02-scene-29'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 2
SCENE = 29
TITLE = 'Hier soir  (Last Night)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'hippolyte': 'Hippolyte'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E02'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e02.fr.dual.srt'
INTRO = ('Camille has just discovered that Hippolyte is her half-brother. He does not know they share a father and '
 'still wants to kiss her. Away from the other guests, she urgently asks what happened at his flat the night '
 'before. Listen first to her questions and his account of the evening.')
OPENER = "Let's walk through it. Camille pulls back and worries that someone might come into the room."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ('The account moves from where they were to the kiss, the bed and falling asleep. Listen for the different '
 "ways French sets a scene and then tells what happened. Camille's relief makes sense to us, while Hippolyte "
 'still does not know their family connection. See you next time!')
CLOSING = ('camille', 'Ouf! À plus tard!')
STORY = [('camille',
  "Non, si quelqu'un entre…",
  'No, what if someone comes in…',
  [(794, "quelqu'un")],
  'Condenses original warning si quelqu’un rentre; omits il ne faut pas and retains the unfinished '
  'condition.'),
 ('hippolyte', 'Personne ne va entrer.', "Nobody's going to come in.", [(795, 'Personne ne va entrer')], ''),
 ('camille', 'Attends.', 'Wait.', [(796, 'Attends')], ''),
 ('camille',
  'Je ne me souviens plus très bien.',
  "I don't remember very well anymore.",
  [(797, 'souviens pas vraiment')],
  'Restores actual plus très bien from French audio, with the written first negative added.'),
 ('camille',
  "Qu'est-ce qu'on a fait hier soir?",
  'What did we do last night?',
  [(797, 'On a fait quoi hier soir')],
  'Restores actual opening Qu’est-ce qu’on; dual subtitles had moved quoi after the action.'),
 ('hippolyte',
  'Tu ne te souviens de rien?',
  "You don't remember anything?",
  [(800, 'Tu ne te souviens de rien')],
  ''),
 ('camille',
  'Dis-moi!',
  'Tell me!',
  [(805, 'Dis-moi')],
  'Short neutral equivalent of the original Réponds-moi!, answer me. Removes the invented de rien response.'),
 ('hippolyte',
  'On était chez moi.',
  'We were at my place.',
  [(806, 'On est rentrés chez moi')],
  'Restores actual on était chez moi, not the backtranslated movement construction on est rentrés.'),
 ('hippolyte', "On s'est embrassés.", 'We kissed.', [(806, "on s'est embrassés")], ''),
 ('hippolyte',
  "Je t'ai portée jusqu'à mon lit.",
  'I carried you to my bed.',
  [(807, "je t'ai portée jusqu'à mon lit")],
  ''),
 ('hippolyte', 'Et après, rien.', 'And then, nothing.', [(808, 'rien')], ''),
 ('hippolyte',
  "Tu t'es endormie en deux secondes.",
  'You fell asleep in two seconds.',
  [(809, "Tu t'es endormie en deux secondes")],
  ''),
 ('camille', 'Vraiment?', 'Really?', [(809, 'Vraiment')], ''),
 ('hippolyte', 'Oui, vraiment.', 'Yes, really.', [(810, 'Oui, vraiment')], ''),
 ('camille', 'Merci!', 'Thank you!', [(811, 'Merci')], '')]
WALK = [(0,
  None,
  "'No, what if someone comes in…' If introduces the possible interruption she fears. Camille leaves the "
  'warning unfinished because the situation makes the consequence clear. Someone is not a specific person: '
  'it could be any guest.'),
 (1,
  None,
  "'Nobody's going to come in.' Here the word for 'nobody' comes first, and the little negative word follows "
  'it. Camille stops him.'),
 (2, None, "'Wait.' Camille gives a casual command, said to one person. Then she confesses something."),
 (3,
  None,
  "'I don't remember very well anymore.' Anymore replaces the ordinary second negative word after remember. "
  'Very well describes the clarity of her memory. She is asking him to fill in what she can no longer recall '
  'clearly.'),
 (4,
  None,
  "'What did we do last night?' The French question begins with what and keeps we before the past helper. "
  'Done carries the action, and yesterday evening is the usual way to say last night.'),
 (5,
  None,
  "'You don't remember anything?' This time the negative is not 'not' but 'nothing'. The second little word "
  'changes, the pattern stays the same.'),
 (6,
  None,
  "'Tell me!' The short me attaches to the familiar command with a hyphen. Camille asks for an answer to the "
  'question about last night, rather than continuing the flirtation.'),
 (7,
  None,
  "'We were at my place.' Were sets the scene before Hippolyte describes the kiss and the bed. At my place "
  "is built from the word for at someone's home and the strong form of me."),
 (8,
  None,
  "'We kissed.' The verb has a little word meaning 'each other', and it also takes 'to be' in the past."),
 (9,
  None,
  "'I carried you to my bed.' The past form gets an extra letter at the end in writing, because the person "
  'carried is a woman.'),
 (10,
  None,
  "'And then, nothing.' Then places this after the kiss and being carried to bed. Nothing stands alone "
  'because the previous question makes clear what further intimacy she is asking about.'),
 (11,
  None,
  "'You fell asleep in two seconds.' Again 'to be' in the past, and again a feminine ending, because it's "
  'Camille who fell asleep.'),
 (12,
  None,
  "'Really?' One word can question whether a whole account is true. Camille repeats the word he used earlier "
  'to describe how much he liked her, but now she uses it to ask for reassurance.'),
 (13,
  None,
  "'Yes, really.' Yes confirms the account, and really strengthens the confirmation. He repeats her question "
  'word as an answer, leaving her no reason to think he is teasing about what happened.'),
 (14,
  None,
  "'Thank you!' This ordinary expression of gratitude sounds unexpected after his story. Camille thanks him "
  'because the evening stopped when she fell asleep. He still does not know why that is such a relief. '
  "Here's the whole scene once more.")]
