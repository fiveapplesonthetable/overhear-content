# Authoring module for dix-pour-cent-s01e01-scene-24.
ID = 'dix-pour-cent-s01e01-scene-24'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 24
TITLE = 'Mathias au jardin  (Mathias in the Garden)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
VOICES = {'narrator': 'sky', 'cecile': 'emilie', 'mathias': 'marcel'}
LABELS = {'cecile': 'Cécile', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = "Now he drives out to see Cécile herself, with a bunch of flowers. She has left Gabriel and is thinking about a rival agency, StarMédia. She opens the door in her gardening clothes, and she is not in a trusting mood. As usual, the French comes first; you don't need to catch every word."
OPENER = "Let's walk back through the garden. Cécile greets Mathias at the door with a short, polite command."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "That's this scene done. When you watch it, notice how the polite 'you' turns casual as they work side by side in the garden. See you next time!"
CLOSING = ('cecile', 'À bientôt, Mathias!')
STORY = [
    ('cecile', 'Bonjour, Mathias. Entrez.', 'Hello, Mathias. Come in.', [(651, 'Bonjour, Mathias'), (652, 'Entrez')], ''),
    ('mathias', 'Bonjour, Cécile. Ces fleurs sont pour vous.', 'Hello, Cécile. These flowers are for you.', [], ''),
    ('cecile', 'Merci. Posez-les ici. Je jardine. Vous venez?', "Thanks. Put them here. I'm gardening. Are you coming?", [(653, 'Posez-les ici'), (656, 'Je jardine. Vous venez')], ''),
    ('mathias', "Au nom de l'agence, je vous présente mes excuses.", 'On behalf of the agency, I apologise.', [(657, "Au nom de l'agence, je vous présente mes excuses")], ''),
    ('cecile', "Vous voulez me récupérer, mais il n'y a aucune chance.", 'You want to win me back, but there is no chance.', [(659, 'Je sais que vous êtes là pour me récupérer'), (660, "il n'y a aucune chance")], ''),
    ('mathias', 'Tu vas signer avec StarMédia?', 'Are you going to sign with StarMédia?', [(661, 'Tu vas signer avec StarMédia')], ''),
    ('cecile', 'Je ne sais pas. Tout le monde ment dans ce milieu.', "I don't know. Everyone lies in this business.", [(661, 'sais pas'), (663, 'Tout le monde ment dans ce milieu')], ''),
    ('cecile', 'Tu peux me donner un coup de main?', 'Can you give me a hand?', [(665, 'Tu peux me donner un coup de main')], ''),
    ('mathias', 'Oui, bien sûr.', 'Yes, of course.', [(665, 'Oui')], ''),
    ('cecile', 'Passe-moi le seau.', 'Hand me the bucket.', [(667, 'Passe-moi le seau')], ''),
    ('mathias', 'Le seau? Ah, oui.', 'The bucket? Oh, yes.', [(667, 'Le seau'), (668, 'Ah, oui')], ''),
    ('cecile', "C'est du compost. Ça nourrit la terre.", 'It', [(669, "c'est du compost"), (670, 'Ça nourrit la terre')], ''),
    ('cecile', 'La terre, elle est vraie. Elle ne sait pas mentir.', "The earth is honest. It doesn't know how to lie.", [(671, 'La terre, elle est vraie'), (671, 'sait pas mentir')], ''),
    ('mathias', 'Écoute, Cécile. Je comprends ta déception.', 'Listen, Cécile. I understand your disappointment.', [(672, 'Écoute, Cécile'), (673, 'Je comprends ta déception')], ''),
    ('mathias', "J'ai parlé à Miranda.", 'I talked to Miranda.', [(675, "j'ai parlé à Miranda")], ''),
    ('mathias', 'Ils sont prêts à en discuter.', 'They', [(676, 'Ils sont prêts à en discuter')], ''),
    ('cecile', "Ah bon? Qu'est-ce qu'elle a dit?", 'Really? What did she say?', [(678, 'Ah bon'), (679, "Qu'est-ce qu'elle a dit")], ''),
]
WALK = [
    (0, None, "'Hello, Mathias. Come in.' That command uses the polite form of 'you'. Keep an eye on that: by the end of the scene they will both slip into the casual one. Mathias holds out his flowers."),
    (1, None, "'Hello, Cécile. These flowers are for you.' The word for 'flowers' is feminine and plural. He is still using the polite 'you', the careful voice of an agent."),
    (2, None, "'Thanks. Put them here.' Another polite command. The little word stuck on with a hyphen means 'them', the flowers. She doesn't make a fuss over the bouquet."),
    (3, None, "'I'm gardening. Are you coming?' French has no separate 'I am doing' form: 'I garden' also means 'I'm gardening'. Out in the garden, Mathias starts with an apology."),
    (4, None, "'You want to win me back, but there is no chance.' Literally 'in the name of the agency, I present you my excuses'. It's a very formal, very official way to say sorry."),
    (5, None, "'I know you're here to get me back.' The verb at the end means 'to get back' or 'to recover', like getting back something you've lost."),
    (6, None, "'But there's no chance.' The expression for 'there is' becomes negative, and the word for 'no' here means 'not a single'. So Mathias changes the subject."),
    (7, None, "'Are you going to sign with StarMédia?' Here he switches to the casual 'you' for the first time. And it's the near future again: 'you go' plus 'to sign'."),
    (8, None, "'I don't know.' The negative wraps around the verb in two parts. In everyday speech the French often drop the first part, and Cécile does in the show, but the full form is the one to learn."),
    (9, None, "'Everyone lies in this business.' Literally 'all the world lies in this circle'. That's a dig at Gabriel, and at agents in general."),
    (10, None, "'Can you give me a hand?' Now Cécile uses the casual 'you' as well. Asking for help with the garden is her way of letting him in a little."),
    (11, None, "'Yes, of course.' A smooth agent always says yes."),
    (12, None, "'Hand me the bucket.' A casual command this time: for verbs like this one, the casual command simply drops the final 's' of the casual 'you' form. Compare it with the polite command at the start of the scene."),
    (13, None, "'The bucket? Oh, yes.' Mathias isn't sure he heard right; he is not a man who usually carries buckets."),
    (14, None, "'It's compost. It feeds the earth.' The first little word before compost means 'some', because you can't count compost. The man in the elegant suit is carrying a bucket of it."),
    (15, None, "'The earth is honest.' Literally 'the earth, it is true'. French often names the thing first and then repeats it with a pronoun."),
    (16, None, "'It doesn't know how to lie.' After the verb for 'to know how' comes an infinitive: 'to lie'. Unlike people, she means. Mathias puts on his gentle voice."),
    (17, None, "'Listen, Cécile. I understand your disappointment.' The first word is a casual command, 'listen'. Then he reveals why he came."),
    (18, None, "'I talked to Miranda.' This is the past tense with 'have' plus the past form of 'talk'. Miranda is the producer who said Cécile was too old."),
    (19, None, "'They're ready to talk about it.' The tiny word in front of the verb means 'about it'. And that changes everything for Cécile."),
    (20, None, "'Really? What did she say?' The first two words show surprise, a bit like 'oh really?'. Suddenly she is listening very closely. Let's listen to the whole scene again, in one go."),
]
