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
INTRO = "Mathias won't tell Andréa, so he certainly won't tell Camille. Her boss's only advice is one word: improvise. So Camille goes to the assistants' desks, where Noémie, Mathias's loyal assistant, is sitting alone. Listen to the whole scene in French first, and don't worry if some of it slips past you."
OPENER = "Let's go back through it slowly. Camille arrives at the desks, looks around, and notices that the friendly assistant is missing."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = 'Well done, that was a busy office, and if you keep only one thing, keep that small two-part negative wrapped around the verb, because it runs through the whole episode. See you next time!'
CLOSING = ('noemie', 'Au revoir!')
STORY = [
    ('camille', "Hervé n'est pas là?", 'Isn', [(538, "Hervé n'est pas là")], ''),
    ('camille', "Noémie, j'ai un problème.", 'Noémie, I have a problem.', [(539, 'Noémie'), (540, "J'ai un problème")], ''),
    ('camille', "Je pense que vous pouvez m'aider.", 'I think you can help me.', [(541, "Je pense que vous pouvez m'aider")], ''),
    ('noemie', 'Je ne crois pas.', 'I don', [(541, 'Je ne crois pas')], ''),
    ('camille', "S'il vous plaît. Il n'y a rien entre Mathias et moi, d'accord?", "Please. There's nothing between Mathias and me, okay?", [(542, "S'il vous plaît"), (543, "entre Mathias et moi, d'accord")], ''),
    ('noemie', "Pardon? Ça ne m'inquiète pas du tout.", 'Excuse me? That doesn', [(544, 'Pardon'), (545, "Ça ne m'inquiète pas du tout")], ''),
    ('noemie', "Alors, c'est quoi ton problème?", 'So, what', [(552, "Alors, c'est quoi ton problème")], ''),
    ('camille', 'Je ne connais rien aux contrats.', 'I don', [(553, 'Je ne connais rien aux contrats')], ''),
    ('camille', 'Je peux regarder un contrat de Mathias? Celui de Canet, par exemple?', "Can I look at one of Mathias's contracts? Canet's, for example?", [(555, 'Celui de Canet, par exemple')], ''),
    ('noemie', "Non, non, non! C'est impossible.", 'No, no, no! That', [(556, 'Non, non, non'), (557, "c'est impossible")], ''),
    ('noemie', 'Il ne laisse personne voir ses contrats.', 'He doesn', [(558, 'Il ne laisse personne voir ses contrats')], ''),
    ('gabriel', 'Où est le traître? Où est la taupe?', 'Where', [(563, 'Où est le traître'), (564, 'Où est la taupe')], ''),
    ('camille', "Qu'est-ce qui se passe?", 'What', [(566, "Qu'est-ce qui se passe")], ''),
    ('gabriel', "Quelqu'un a dit à Cécile qu'elle était trop vieille pour le rôle.", 'Someone told Cécile she was too old for the part.', [(567, "Quelqu'un a dit à Cécile qu'elle était trop vieille pour le rôle")], ''),
    ('gabriel', "Elle est partie! Elle m'a quitté.", 'She', [(570, 'Elle est partie'), (571, "Elle m'a quitté")], ''),
    ('noemie', 'Oui, Mathias? Bien sûr.', 'Yes, Mathias? Of course.', [(579, 'Oui, Mathias'), (580, 'Bien sûr')], ''),
    ('noemie', 'Il veut le numéro de Miranda Jones, la productrice de Tarantino.', 'He wants the number of Miranda Jones, Tarantino', [(581, 'le numéro de Miranda Jones, la productrice de Tarantino')], ''),
]
WALK = [
    (0, None, "'Isn't Hervé here?' The verb sits between two small words that together make it negative. That two-part negative is the grammar of this whole scene, so keep an ear out for it. With Hervé gone, Camille turns to Noémie."),
    (1, None, "'Noémie, I have a problem.' Simple and direct: I have, then the thing. She tries to sound casual."),
    (2, None, "'I think you can help me.' Notice that Camille uses the polite, formal 'you' with Noémie. She is new, and she wants a favour, so she is careful."),
    (3, None, "'I don't think so.' Short and cold, the same two-part negative around the verb. Noémie is not in a helpful mood, because earlier she saw Camille arguing with Mathias, and she is quietly in love with him."),
    (4, "S'il vous plaît.", "'Please.' Literally 'if it pleases you', again with the formal 'you'. Then Camille tries to clear the air."),
    (4, "Il n'y a rien entre Mathias et moi, d'accord?", "'There's nothing between Mathias and me, okay?' Here the negative pairs with the word for 'nothing' instead of the usual 'not'. Camille thinks Noémie is jealous. Of course she can't say that Mathias is really her father."),
    (5, None, "'Excuse me? That doesn't worry me at all.' The words at the end mean 'at all', and they make the denial stronger. She says it a little too fast to be believed."),
    (6, None, "'So, what's your problem?' Very informal: Noémie uses the casual 'you' with the newcomer, while Camille keeps the polite one. That uneven pairing tells you who feels senior here."),
    (7, None, "'I don't know anything about contracts.' Negative plus 'nothing' again. Camille plays the innocent beginner, which is partly true."),
    (8, 'Je peux regarder un contrat de Mathias?', "'Can I look at one of Mathias's contracts?' To say one thing belongs to someone, French puts the owner after a small word meaning 'of': a contract of Mathias. Then she slips in the one she really wants."),
    (8, 'Celui de Canet, par exemple?', "'Canet's, for example?' The first word means 'the one', so it's 'the one of Canet'. That's the contract Andréa asked about, and Noémie sees straight through it."),
    (9, None, "'No, no, no! That's impossible.' The triple no says everything."),
    (10, None, "'He doesn't let anyone see his contracts.' This time the negative pairs with the word for 'nobody'. So you have now heard 'not', 'nothing' and 'nobody', all built the same way. Just then, Gabriel bursts in."),
    (11, None, "'Where's the traitor? Where's the mole?' A mole is the spy inside a company, in French just as in English."),
    (12, None, "'What's going on?' A fixed phrase you'll hear constantly, worth learning as one block."),
    (13, None, "'Someone told Cécile she was too old for the part.' The verb for 'told' is in the past, and 'she was' uses the past tense for describing. Camille says nothing. She is the someone, though Gabriel doesn't know it."),
    (14, None, "'She's gone! She's left me.' Two past forms: the first is built with the verb 'to be', because it's about leaving a place, and the second with 'to have'. Gabriel is heartbroken, and paranoid too: he grabs a colleague and accuses them of working for a rival agency."),
    (15, None, "'Yes, Mathias? Of course.' Noémie's phone rings and her voice turns soft. Her boss is calling."),
    (16, None, "'He wants the number of Miranda Jones, Tarantino's producer.' Again the owner comes after the word for 'of'. Mathias wants to meet the woman who turned Cécile down, and Noémie gets to work at once."),
]
