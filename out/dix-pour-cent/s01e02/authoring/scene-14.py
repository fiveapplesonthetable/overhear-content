# Authoring module for dix-pour-cent-s01e02-scene-14.
ID = 'dix-pour-cent-s01e02-scene-14'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 2
SCENE = 14
TITLE = 'Hélène veut vendre  (Hélène Wants to Sell)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'helene': 'Hélène', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E02'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e02.fr.dual.srt'
INTRO = ("An emergency meeting brings the four partners to a hotel to see Samuel's widow, Hélène. Andréa arrives "
 "still talking to Gabor, the director, who is being dramatic about a bad cold. Gabriel offers the group's "
 'support. Hélène then explains her decision about the inherited shares. First, listen in French.')
OPENER = ("Let's go back through it slowly. Andréa is still on the phone with Gabor, the director, who has a bad cold "
 'and is very dramatic about it.')
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ("That was a tough business meeting, and you got through it in French. Listen for 'I want to sell' when you "
 'watch: it changes everything for the agency. See you next time!')
CLOSING = ('andrea', 'Bonne soirée!')
STORY = [('andrea',
  "Non, Gabor, tu ne vas pas mourir. Je t'appelle demain.",
  "No, Gabor, you're not going to die. I'll call you tomorrow.",
  [(396, 'Non, Gabor, tu ne vas pas mourir'), (400, "Je t'appelle demain")],
  ''),
 ('andrea', 'Désolée. Je suis là.', "Sorry. I'm here.", [(402, 'Désolée. Je suis là')], ''),
 ('helene',
  "Merci. Samuel n'a pas laissé de testament.",
  "Thank you. Samuel didn't leave a will.",
  [(405, 'Merci'), (408, "Samuel n'a pas laissé de testament")],
  ''),
 ('helene',
  "J'hérite donc de toutes ses parts.",
  'So I inherit all his shares.',
  [(409, "J'hérite donc de toutes ses parts")],
  ''),
 ('helene',
  "Je ne veux pas travailler à l'agence. Je veux vendre.",
  "I don't want to work at the agency. I want to sell.",
  [(412, 'je veux vendre')],
  'Summarises her refusal to become involved in agency work before the explicit wish to sell.'),
 ('andrea', 'À qui?', 'To whom?', [(418, 'À qui ?')], ''),
 ('helene',
  'Je ne sais pas. Au plus rapide.',
  "I don't know. To the quickest.",
  [(419, 'Je ne sais pas'), (420, 'Au plus rapide')],
  ''),
 ('andrea',
  'On peut racheter les parts de Samuel.',
  "We can buy Samuel's shares.",
  [(426, 'On peut racheter les parts de Samuel')],
  ''),
 ('helene',
  'Que voulez-vous dire, on?',
  'What do you mean, we?',
  [(427, 'Que voulez-vous dire')],
  "Makes the quoted on explicit to clarify Hélène's question."),
 ('mathias', 'Nous. Nous quatre.', 'Us. The four of us.', [(428, 'Nous. Nous quatre')], ''),
 ('andrea',
  "Moi, je n'ai rien. Je suis locataire.",
  'Me, I have nothing. I rent my flat.',
  [(430, "Moi j'ai rien"), (431, 'je suis locataire')],
  'Restores ne in the spoken negative; locataire is translated as renting her home.'),
 ('mathias', "L'argent, ça se trouve.", 'Money can be found.', [(436, "L'argent, ça se trouve")], ''),
 ('andrea',
  "C'est facile à dire quand on en a!",
  "That's easy to say when you have some!",
  [(437, "c'est facile à dire quand on en a")],
  ''),
 ('mathias', 'Tu pourrais gagner plus.', 'You could earn more.', [(438, 'Tu pourrais gagner plus')], ''),
 ('andrea',
  'Avec des films nuls? Non, merci.',
  'With rubbish films? No, thank you.',
  [(440, 'des films nuls')],
  'Shortens the angry argument to a clean refusal of bad films.'),
 ('mathias',
  "Tu préférerais qu'ASK disparaisse?",
  'Would you rather ASK disappeared?',
  [(444, "Tu préférerais qu'ASK disparaisse ?")],
  '')]
WALK = [(0,
  'Non, Gabor, tu ne vas pas mourir.',
  "'No, Gabor, you're not going to die.' The action word 'to go' plus another action word is the near "
  "future; here it's negative, so the two little words for 'not' wrap around the action word 'to go'."),
 (0,
  "Je t'appelle demain.",
  "'I'll call you tomorrow.' French often uses the present for a near plan like this."),
 (1,
  None,
  "'Sorry. I'm here.' The word for 'sorry' ends with an extra letter because Andréa is a woman. She hangs up "
  'and joins the others.'),
 (2,
  None,
  "'Thank you. Samuel didn't leave a will.' The negative changes a will into no will: the short article "
  'before will is the one French normally uses after a negated have or leave. Here will means the '
  'inheritance document, not a future action.'),
 (3,
  None,
  "'So I inherit all his shares.' The word in the middle means 'so' or 'therefore'. Samuel's part of the "
  'agency now belongs to her.'),
 (4,
  None,
  "'I don't want to work at the agency. I want to sell.' Hélène builds two sentences the same way: the word "
  "for 'want', then another action word in its basic form. First negative, then positive."),
 (5,
  None,
  "'To whom?' The first word is to, not at: it introduces the person who would buy the shares. The question "
  "asks for the buyer's identity, not the price."),
 (6,
  None,
  "'I don't know. To the quickest.' The middle word makes quick into the quickest. The final description "
  'stands for the quickest buyer, so Hélène need not repeat buyer itself.'),
 (7,
  None,
  "'We can buy Samuel's shares.' Buy here means acquire the shares from their new owner, Hélène. The French "
  'action word can also mean buy back, but it does not require the buyer to have owned the thing before.'),
 (8,
  None,
  "'What do you mean, we?' Literally 'what do you want to say'. That's how French asks what someone means."),
 (9,
  None,
  "'Us. The four of us.' French uses the same word for we before an action and us standing alone here. "
  'Mathias means the four partners: himself, Andréa, Gabriel and Arlette.'),
 (10,
  None,
  "'Me, I have nothing. I rent my flat.' Starting with the strong word for 'me' puts the focus on herself. "
  "Andréa doesn't own a home, so she has nothing to put in."),
 (11,
  None,
  "'Money can be found.' Literally, money finds itself. That self pattern can express that something is "
  'possible or obtainable, without saying who does it. Mathias treats raising the money as a solvable '
  'problem.'),
 (12,
  None,
  "'That's easy to say when you have some!' The small word just before the last verb means 'some of it', the "
  'money.'),
 (13,
  None,
  "'You could earn more.' The ending on the verb makes it 'could'. Mathias thinks Andréa chooses her actors "
  'badly.'),
 (14,
  None,
  "'With rubbish films? No, thank you.' The word for 'rubbish' is a very common way to say something is bad. "
  'Andréa would rather work with artists she believes in.'),
 (15,
  None,
  "'Would you rather ASK disappeared?' A long sentence, but you can hear the key words: 'you would prefer' "
  "and the name of the agency. In the end it's Arlette who breaks the tension, joking that being sold would "
  "be a bit like having Mathias as their boss. Let's hear the whole meeting again, all in French.")]
