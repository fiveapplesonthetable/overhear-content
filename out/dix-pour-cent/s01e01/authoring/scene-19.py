SOURCE_NOTE = 'French dialogue is an A1 abridgment. Original video confirms speakers and setting; unprompted original-audio transcription confirms the address forms. Dual subtitles provide scene locators.'
# Authoring module for dix-pour-cent-s01e01-scene-19.
ID = 'dix-pour-cent-s01e01-scene-19'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 19
TITLE = 'Le contrat et la taupe  (The Contract and the Mole)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'gabriel': 'Gabriel', 'noemie': 'Noémie'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = ("Andrea wants to know the terms of Mathias's contract for the actor Guillaume Canet, and sends Camille to "
 'find out. Camille asks Noemie for help, while Gabriel is trying to discover who told Cecile the truth. '
 'Listen to the requests, denials and interruption in French.')
OPENER = "Let's go back through it slowly. Camille arrives at the desks, looks around, and notices that the friendly assistant is missing."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ('You have heard refusals built with not, nothing and nobody. Meanwhile, Mathias asks Noemie to find Miranda '
 "Jones's number: he wants to see the producer about Cecile's part. See you next time.")
CLOSING = ('noemie', 'Au revoir!')
STORY = [('camille', "Hervé n'est pas là?", "Isn't Hervé here?", [(538, "Hervé n'est pas là")], ''),
 ('camille',
  "Noémie, j'ai un problème.",
  'Noémie, I have a problem.',
  [(539, 'Noémie'), (540, "J'ai un problème")],
  ''),
 ('camille',
  "Je pense que tu peux m'aider.",
  'I think you can help me.',
  [(541, "Je pense que vous pouvez m'aider")],
  'A1 abridgment preserves the familiar address and original speakers.'),
 ('noemie', 'Je ne crois pas.', "I don't think so.", [(541, 'Je ne crois pas')], ''),
 ('camille',
  "S'il te plaît. Il n'y a rien entre Mathias et moi, d'accord?",
  "Please. There's nothing between Mathias and me, okay?",
  [(542, "S'il vous plaît"), (543, "entre Mathias et moi, d'accord")],
  'A1 abridgment preserves the familiar address and original speakers.'),
 ('noemie',
  "Pardon? Ça ne m'inquiète pas du tout.",
  "Excuse me? That doesn't worry me at all.",
  [(544, 'Pardon'), (545, "Ça ne m'inquiète pas du tout")],
  ''),
 ('noemie',
  "Alors, c'est quoi ton problème?",
  "So, what's your problem?",
  [(552, "Alors, c'est quoi ton problème")],
  ''),
 ('camille',
  'Je ne connais rien aux contrats.',
  "I don't know anything about contracts.",
  [(553, 'Je ne connais rien aux contrats')],
  ''),
 ('camille',
  'Je peux regarder un contrat de Mathias? Celui de Canet, par exemple?',
  "Can I look at one of Mathias's contracts? Canet's, for example?",
  [(555, 'regarder un de ceux de Mathias'), (555, 'Celui de Canet, par exemple')],
  'Conditional request simplified; contract noun made explicit.'),
 ('noemie',
  "Non, non, non! C'est impossible.",
  "No, no, no! That's impossible.",
  [(556, 'Non, non, non'), (557, "c'est impossible")],
  ''),
 ('noemie',
  'Il ne laisse personne voir ses contrats.',
  "He doesn't let anyone see his contracts.",
  [(558, 'Il ne laisse personne voir ses contrats')],
  ''),
 ('gabriel',
  'Où est le traître? Où est la taupe?',
  "Where's the traitor? Where's the mole?",
  [(563, 'Où est le traître'), (564, 'Où est la taupe')],
  ''),
 ('gabriel',
  "Elle est partie! Elle m'a quitté.",
  "She's gone! She's left me.",
  [(570, 'Elle est partie'), (571, "Elle m'a quitté")],
  ''),
 ('noemie',
  'Oui, Mathias?',
  'Yes, Mathias?',
  [(579, 'Oui, Mathias')],
  'Noemie answers her boss directly; no phone call is involved.')]
WALK = [(0,
  None,
  "'Isn't Herve here?' Two small negatives surround 'is'. The last word can mean either 'here' or 'there', "
  'depending on where the speaker is looking.'),
 (1,
  None,
  "'Noémie, I have a problem.' Simple and direct: I have, then the thing. She tries to sound casual."),
 (2,
  None,
  "'I think you can help me.' A short linking word joins 'think' to the next statement. Camille uses the "
  'familiar address with Noemie, as the assistants do with each other.'),
 (3,
  None,
  "'I don't think so.' The two negative words surround 'think'. Noemie is reluctant to help, and suspicious "
  "about Camille's relationship with Mathias."),
 (4,
  "S'il te plaît.",
  "'Please.' The expression literally means 'if it pleases you'. Its middle word has the familiar form for "
  'one person.'),
 (4,
  "Il n'y a rien entre Mathias et moi, d'accord?",
  "'There's nothing between Mathias and me, okay?' Here the negative pairs with the word for 'nothing' "
  "instead of the usual 'not'. Camille thinks Noémie is jealous. Of course she can't say that Mathias is "
  'really her father.'),
 (5,
  None,
  "'Excuse me? That doesn't worry me at all.' The words at the end mean 'at all', and they make the denial "
  'stronger. She says it a little too fast to be believed.'),
 (6,
  None,
  "'So, what's your problem?' The familiar possessive before 'problem' matches the way the two assistants "
  'address each other. Noemie now asks what Camille actually needs.'),
 (7,
  None,
  "'I don't know anything about contracts.' Negative plus 'nothing' again. Camille plays the innocent "
  'beginner, which is partly true.'),
 (8,
  'Je peux regarder un contrat de Mathias?',
  "'Can I look at one of Mathias's contracts?' The owner follows a short word meaning 'of'. French says 'a "
  "contract of Mathias', where English uses the ending on his name."),
 (8,
  'Celui de Canet, par exemple?',
  "'Canet's, for example?' The first word means 'the one' and replaces the masculine noun 'contract'. "
  'Camille can name the contract she wants without repeating that noun.'),
 (9,
  None,
  "'No, no, no! That's impossible.' Repeating 'no' strengthens the refusal. The description that follows "
  "already contains the idea of 'not possible', without another pair of negatives."),
 (10,
  None,
  "'He doesn't let anyone see his contracts.' This time the small negative before 'let' pairs with 'nobody' "
  "after it. The possessive before 'contracts' is plural because there is more than one contract."),
 (11,
  None,
  "'Where's the traitor? Where's the mole?' Gabriel repeats the same question pattern with two different "
  "people to find. The noun for 'mole' also means a spy inside an organisation."),
 (12,
  None,
  "'She's gone! She's left me.' The action meaning 'depart' builds this past with 'be'. The action meaning "
  "'leave someone' uses 'have', with the little object meaning 'me' before it."),
 (13,
  None,
  "'Yes, Mathias?' Noemie answers when her boss calls her. Naming him at the end identifies the person whose "
  'attention she is acknowledging.')]
