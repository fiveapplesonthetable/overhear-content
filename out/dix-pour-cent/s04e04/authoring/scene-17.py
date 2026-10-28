# Authoring module for dix-pour-cent-s04e04-scene-17.
ID = 'dix-pour-cent-s04e04-scene-17'
SHOW = 'dix-pour-cent'
SEASON = 4
EPISODE = 4
SCENE = 17
TITLE = 'La trahison découverte  (The Betrayal Discovered)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S04E04'
SOURCE_FILE = 'sources/dix-pour-cent/s04/e04.fr.dual.srt'
INTRO = "Left alone at Mathias's desk, Camille looks for the paternity document on his computer. Instead, she spots an open draft email detailing Mathias's ruthless plot to deceive author Ulrika. Let's listen to this chilling discovery in French first."
OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."
OUTRO = "Horrified by the evidence of her father's treachery, Camille quickly hides her discovery as Mathias returns. When you watch the episode, listen out for the expressions meaning 'let us see' and 'form'. You'll catch them now. See you next time!"
CLOSING = ('mathias', 'À bientôt!')
STORY = [
    ('camille', 'Voyons ce formulaire sur son ordinateur.', 'Let us look for this form on his computer.', [], ''),
    ('camille', "Attends, qu'est-ce que c'est que ça?", 'Wait, what is this?', [], ''),
    ('camille', "C'est un brouillon d'e-mail ouvert.", 'It is an open draft email.', [], ''),
    ('camille', "J'ai fait des promesses à Ulrika...", 'I made promises to Ulrika...', [(1029, "J'AI FAIT DES PROMESSES")], ''),
    ('camille', "Pour qu'elle signe le contrat...", 'So that she signs the contract...', [(1029, "POUR QU'ELLE SIGNE")], ''),
    ('camille', 'Mais je compte la décourager progressivement...', 'But I plan to discourage her gradually...', [(1030, 'DÉCOURAGER PROGRESSIVEMENT')], ''),
    ('camille', 'On peut la remplacer plus tard...', 'We can replace her later on...', [(1031, 'ON PEUT LA REMPLACER')], ''),
    ('camille', 'Utiliser la note de frais...', 'Use the expense account...', [(1032, 'LA NOTE DE FRAIS')], ''),
    ('camille', 'Pour une fondation animale...', 'For an animal foundation...', [(1032, 'POUR UNE FONDATION ANIMALE')], ''),
    ('camille', "Mon Dieu, c'est une trahison totale!", 'My God, this is total betrayal!', [], ''),
    ('camille', 'Il a menti à tout le monde.', 'He lied to everyone.', [], ''),
    ('mathias', 'Camille? Tu as trouvé ce formulaire?', 'Camille? Did you find that form?', [], ''),
    ('mathias', 'Voici deux verres pour fêter ça!', 'Here are two glasses to celebrate this!', [(1029, 'pour')], ''),
    ('camille', 'Oui, tout va très bien, papa.', 'Yes, everything is fine, dad.', [], ''),
]
WALK = [
    (0, None, "'Let us look for this form on his computer.' Camille prepares to search for the legal paperwork."),
    (1, None, "'Wait, what is this?' Camille is distracted by an unexpected open window on the screen."),
    (2, None, "'It is an open draft email.' Camille notices an unsent message written by Mathias."),
    (3, None, "'I made promises to Ulrika...' Camille reads the beginning of her father's private strategy notes."),
    (4, None, "'So that she signs the contract...' Camille discovers how Mathias persuaded the Swedish author."),
    (5, None, "'But I plan to discourage her gradually...' Camille discovers his plan to push the author aside."),
    (6, None, "'We can replace her later on...' Camille reads that Mathias intends to bring in a new writer."),
    (7, None, "'Use the expense account...' Camille uncovers his plan to charge the company for personal schemes."),
    (8, None, "'For an animal foundation...' Camille reads how Mathias planned to feign charitable support."),
    (9, None, "'My God, this is total betrayal!' Camille realizes that her father betrayed both her and ASK."),
    (10, None, "'He lied to everyone.' Camille sees clearly that Mathias manipulated everyone around him."),
    (11, None, "'Camille? Did you find that form?' Mathias returns from the kitchen holding two glasses."),
    (12, None, "'Here are two glasses to celebrate this!' Mathias approaches warmly to toast their reunion."),
    (13, None, "'Yes, everything is fine, dad.' Camille conceals her devastation behind a composed expression."),
]
