# Authoring module for dix-pour-cent-s01e03-scene-01.
ID = 'dix-pour-cent-s01e03-scene-01'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = 'La lettre oubliée  (The Forgotten Letter)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'camille': 'Camille', 'gabriel': 'Gabriel'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E03'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e03.fr.dual.srt'
INTRO = "We start with Andréa, the toughest agent at ASK, just off the phone. The agency had one friend at the tax office, a Mr Jarron, and a letter was supposed to go to him. Her assistant Camille was in charge of posting it. Here's the story in French first; don't worry if a lot of it goes past you."
OPENER = "Let's go back through it. Andréa finishes a call with one of her stars, Cécile de France, in her usual casual way."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "A forgotten letter and a crisis meeting: not a good start to the week. If it felt fast, that's normal; the key lines will stand out when you watch. See you next time!"
CLOSING = ('andrea', 'À bientôt!')
STORY = [
    ('andrea', 'Cécile! Oui, super. Rappelle-moi. Salut.', 'Cécile! Yes, great. Call me back. Bye.', [(1, 'Cécile ! Oui, super'), (3, 'rappelle-moi. Salut')], ''),
    ('andrea', 'Le contrôle fiscal. Cette lettre pour monsieur Jarron?', 'That letter for Mr Jarron?', [(5, 'Le contrôle fiscal'), (6, 'Cette lettre pour M. Jarron')], ''),
    ('camille', "Oui, je l'ai envoyée.", 'Yes, I sent it.', [(7, "Oui, je l'ai envoyée")], ''),
    ('camille', "J'ai pris la lettre. Je l'ai mise dans une enveloppe.", 'I put it in an envelope.', [(8, "J'ai pris la lettre"), (8, "je l'ai mise dans une enveloppe")], ''),
    ('camille', 'Oh non!', 'Oh no!', [], ''),
    ('camille', 'Je suis désolée.', "I'm sorry.", [], ''),
    ('andrea', 'À quoi ça sert de payer une assistante?', "What's the point of paying an assistant?", [(10, 'À quoi ça sert de payer une assistante ?')], ''),
    ('andrea', 'Non, Gabriel, on ne peut pas toujours tout arranger!', "No, Gabriel, you can't always fix everything!", [(15, 'Non, Gabriel, on ne peut pas toujours tout arranger')], ''),
    ('andrea', 'On a eu un appel ce matin.', 'We had a call this morning.', [(16, 'un appel ce matin')], ''),
    ('andrea', 'Le dossier est dans un autre service.', 'The file is in another department.', [(17, 'dans un autre service')], ''),
    ('andrea', 'Jarron était notre seul allié.', 'Jarron was our only ally.', [(18, 'Jarron était notre seul allié')], ''),
    ('gabriel', 'Il faut peut-être mettre nos comptes en ordre.', 'Maybe we need to put our books in order.', [(19, 'peut-être'), (19, 'mettre nos comptes en ordre')], ''),
    ('andrea', "La vie, c'est une grande blague pour toi?", 'Is life a big joke to you?', [(21, 'une grande blague pour toi')], ''),
    ('andrea', 'Tu es aussi stupide que ça?', 'Are you really that stupid?', [(22, 'Tu es aussi stupide que ça ?')], ''),
    ('gabriel', 'Fais-lui un café.', 'Make her a coffee.', [(24, 'Fais-lui un café')], ''),
]
WALK = [
    (0, None, "'Cécile! Yes, great. Call me back. Bye.' This command 'call me back' is in the casual form, and the little word for 'me' comes after it, joined with a hyphen. The last word is the casual goodbye."),
    (1, 'Le contrôle fiscal.', "'The tax audit.' Literally 'the fiscal control'. This is what everyone at the agency is afraid of."),
    (1, 'Cette lettre pour monsieur Jarron?', "'That letter for Mr Jarron?' The first word means 'this' or 'that', in its feminine form, because the word for letter is feminine."),
    (2, None, "'Yes, I sent it.' The little word for 'it' comes before the action word and loses its vowel. And because 'it', the letter, is feminine and comes first, the past form of the action word gets an extra e on paper."),
    (3, "J'ai pris la lettre.", "'I took the letter.' The everyday past tense: 'I have' plus the past form of 'to take'. Camille walks through what she did, step by step."),
    (3, "Je l'ai mise dans une enveloppe.", "'I put it in an envelope.' And then she stops, because she remembers what she didn't do."),
    (4, None, "'Oh no!' In the show she swears. The letter is still sitting somewhere in the office."),
    (5, None, "'I'm sorry.' The word for sorry ends with an extra e on paper, because Camille is a woman."),
    (6, None, "'What's the point of paying an assistant?' Literally 'to what does it serve to pay an assistant'. Andréa is furious. Then the partners gather for a crisis meeting, and Gabriel tries to calm everyone down."),
    (7, None, "'No, Gabriel, you can't always fix everything!' The word for 'we' or 'one' is used here for people in general."),
    (8, None, "'We had a call this morning.' The same everyday past tense, with the past form of 'to have'."),
    (9, None, "'The file is in another department.' Their audit has been moved, away from their friend."),
    (10, None, "'Jarron was our only ally.' This is another past tense, used to describe how things were. Now they have no one."),
    (11, None, "'Maybe we need to put our books in order.' The first two words mean 'it is necessary', a very common way to say what has to be done. Gabriel's honest idea goes down very badly."),
    (12, None, "'Is life a big joke to you?' The partners turn on him. Notice the casual 'you' at the end: they are old colleagues."),
    (13, None, "'Are you really that stupid?' Literally 'are you as stupid as that?'. Just then Hervé announces that Laura Smet has arrived."),
    (14, None, "'Make her a coffee.' Another casual command, with the little word for 'to her' joined on with a hyphen. Gabriel jumps at the chance to escape. Hervé replies that the coffee has already been drunk."),
]
