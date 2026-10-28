# Authoring module for dix-pour-cent-s01e03-scene-19.
ID = 'dix-pour-cent-s01e03-scene-19'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 3
SCENE = 19
TITLE = 'Une robe pour les Césars  (Dressing for the Césars)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'maman': 'Maman'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E03'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e03.fr.dual.srt'
INTRO = "After Laura's outrageous audition, evening falls over Paris. It is the night of the César awards, the biggest night in French cinema, and Mathias has given Camille an invitation. In Camille's cosy attic loft, her mother has come up from the south to help her get dressed. She is proud, fussy, and still worried about Mathias. Let's listen in French first; don't worry about catching every word."
OPENER = "Let's go through it together. Camille's mother is adjusting her dress and asking about Mathias."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "You've got all of it: commands, negatives, and plenty of motherly advice. See you next time!"
CLOSING = ('camille', 'Bonne soirée!')
STORY = [
    ('maman', "Il t'invite à des soirées?", 'He invites you to parties?', [(490, "Il t'invite à des soirées")], ''),
    ('camille', 'Les Césars, Maman. Une exception.', 'The Césars, Mum. An exception.', [(490, 'Les Césars, Maman. Une exception')], ''),
    ('maman', 'Donc tout le bureau est au courant?', 'So the whole office knows?', [(491, 'Donc tout le bureau est au courant')], ''),
    ('camille', "Non, personne ne sait. C'est purement professionnel.", 'No, nobody knows. It', [(491, 'Non, personne ne sait'), (492, "C'est purement professionnel")], ''),
    ('maman', 'Tourne-toi. Il vient te chercher?', 'Turn around. Is he picking you up?', [(493, 'Tourne-toi'), (494, 'Il vient te chercher')], ''),
    ('camille', 'Non, je prends le métro.', 'No, I', [(494, 'Non, je prends le métro')], ''),
    ('maman', 'Classe! Serre un peu ta ceinture.', 'Classy! Tighten your belt a bit.', [(495, 'Classe'), (497, 'Serre un peu ta ceinture')], ''),
    ('camille', "Je n'arrive pas à respirer.", 'I can', [(498, "Je n'arrive pas à respirer")], ''),
    ('maman', 'Non, laisse, ça te fait une belle silhouette.', 'No, leave it, it gives you a lovely figure.', [(499, 'Non, laisse, ça te fait une belle silhouette')], ''),
    ('maman', 'Laisse-moi te regarder.', 'Let me look at you.', [(500, 'Laisse-moi te regarder')], ''),
    ('camille', 'Trop vulgaire?', 'Too flashy?', [(501, 'Trop vulgaire')], ''),
    ('maman', "Vulgaire? Une femme Valentini n'est jamais vulgaire!", 'Flashy? A Valentini woman is never flashy!', [(502, "Vulgaire ? Une femme Valentini n'est jamais vulgaire")], ''),
    ('camille', 'Les filles à Paris sont plus sobres.', 'Girls in Paris are more understated.', [(504, 'les filles à Paris sont plus sobres')], ''),
    ('maman', "Elles mangent des graines et font la tête, c'est tout!", 'They eat seeds and sulk, that', [(505, "Elles mangent des graines et font la tête, c'est tout")], ''),
    ('camille', "D'accord. Bisous, Maman!", 'Okay. Kisses, Mum!', [(506, "d'accord"), (507, 'Bisous, Maman')], ''),
    ('maman', "Prends des photos des stars. Et Camille, n'attends rien de lui.", "Take photos of the stars. And Camille, don't expect anything from him.", [(508, 'Prends des photos des stars'), (509, 'Et Camille'), (510, "n'attends rien de lui")], ''),
    ('maman', 'Et ne bois pas trop!', 'And don', [(512, 'Et ne bois pas trop')], ''),
    ('maman', 'Si tu vois Sophie Marceau, prends une photo!', 'If you see Sophie Marceau, take a photo!', [(514, 'Si tu vois Sophie Marceau, prends une photo')], ''),
]
WALK = [
    (0, None, "'He invites you to parties?' The small word for 'you' shrinks before a vowel and sits right before the verb."),
    (1, None, "'The Césars, Mum. An exception.' Camille plays it down: this is the big awards night, not a family outing."),
    (2, None, "'So the whole office knows?' Literally 'all the office is in the current', a common idiom for knowing the news."),
    (3, None, "'No, nobody knows. It's purely professional.' In French, 'nobody' pairs with the first part of the negative before the verb, without the second part after it."),
    (4, 'Tourne-toi.', "'Turn around.' A reflexive command: the word for 'yourself' is attached to the end of the verb with a hyphen."),
    (4, 'Il vient te chercher?', "'Is he picking you up?' Literally 'he comes to fetch you'. A very useful everyday phrase."),
    (5, None, "'No, I'm taking the metro.' In French you 'take' the metro or the bus, just as in English."),
    (6, None, "'Classy! Tighten your belt a bit.' Her mother is being ironic about going to a red-carpet party by underground train, and then gives another motherly command."),
    (7, None, "'I can't breathe.' Literally 'I don't manage to breathe'."),
    (8, None, "'No, leave it, it gives you a lovely figure.' Literally 'it makes to you a beautiful silhouette'."),
    (9, None, "'Let me look at you.' Another command with 'me' joined by a hyphen, followed by 'look at you'."),
    (10, None, "'Too flashy?' The French adjective is stronger, closer to 'vulgar' or 'trashy', and Camille is a bit worried."),
    (11, None, "'Flashy? A Valentini woman is never flashy!' The negative here is 'never', placed after the verb 'is'."),
    (12, None, "'Girls in Paris are more understated.' It's the same adjective Solveig used for Nathalie's acting: simple, sober, not too much."),
    (13, None, "'They eat seeds and sulk, that's all!' Literally 'they make the head', a lively idiom for pulling a long, grumpy face."),
    (14, None, "'Okay. Kisses, Mum!' The plural word for 'kisses' is how family and close friends say bye."),
    (15, 'Prends des photos des stars.', "'Take photos of the stars.' A casual command from the verb 'to take'."),
    (15, "Et Camille, n'attends rien de lui.", "'And Camille, don't expect anything from him.' A negative command: 'expect nothing from him'. Her mother knows Mathias all too well."),
    (16, None, "'And don't drink too much!' Another negative command, wrapping the two negative words around the verb 'drink'."),
    (17, None, "'If you see Sophie Marceau, take a photo!' Even while worrying, she still wants a picture of her favourite actress. Now let's hear the whole scene in Camille's loft again."),
]
