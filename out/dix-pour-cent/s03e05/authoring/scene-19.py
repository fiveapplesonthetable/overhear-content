# Authoring module for dix-pour-cent-s03e05-scene-19.
ID = 'dix-pour-cent-s03e05-scene-19'
SHOW = 'dix-pour-cent'
SEASON = 3
EPISODE = 5
SCENE = 19
TITLE = 'Fausse déception  (Feigned Disappointment)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'hicham': 'Hicham', 'mathias': 'Mathias', 'noemie': 'Noémie'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S03E05'
SOURCE_FILE = 'sources/dix-pour-cent/s03/e05.fr.dual.srt'
INTRO = 'In his office at ASK, Mathias receives a phone call from Hicham. Hicham announces that Solaris has signed the rival co-production deal. Mathias feigns total devastation while Noemie listens in secrecy. Listen to the scene in French first.'
OPENER = "Let's walk through the conversation step by step."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "Mathias's cunning act keeps Hicham completely in the dark about his secret maneuvers. When you watch the episode, listen out for the expressions meaning 'are you doing' and 'signed'. You'll catch them now. See you next time!"
CLOSING = ('mathias', 'À demain!')
STORY = [
    ('mathias', 'Allô, Hicham? Comment vas-tu?', 'Hello, Hicham? How are you doing?', [(783, 'Allo')], ''),
    ('hicham', 'Ils ont signé hier soir le contrat.', 'They signed the contract yesterday evening.', [(784, 'signé hier soir le deal')], ''),
    ('mathias', "Ce n'est pas vrai, c'est signé?", 'It is not true, it is signed?', [(784, "Non c'est pas vrai")], ''),
    ('hicham', 'Oui, le deal de coproduction est fait.', 'Yes, the co-production deal is done.', [(784, 'deal de copro avec Solaris')], ''),
    ('mathias', 'Je ne savais pas du tout cela.', 'I did not know that at all.', [(785, 'je savais pas du tout')], ''),
    ('mathias', 'Franchement, je suis totalement consterné.', 'Frankly, I am totally dismayed.', [(786, 'Je suis consterné')], ''),
    ('mathias', "C'est vraiment une terrible malchance.", 'It is really terrible bad luck.', [(787, "C'est vraiment pas de chance")], ''),
    ('hicham', 'Nous avons perdu ce projet ensemble.', 'We lost this project together.', [(788, "ce qu'on peut faire de plus")], ''),
    ('mathias', "Je ne vois rien d'autre à faire.", 'I see nothing else to do.', [(788, "vois vraiment pas ce qu'on peut faire")], ''),
    ('mathias', 'Je suis vraiment navré, Hicham.', 'I am truly sorry, Hicham.', [(790, 'Vraiment navré Hicham')], ''),
    ('hicham', 'Merci, on se voit demain au bureau.', 'Thank you, see you tomorrow at the office.', [(791, 'à demain')], ''),
    ('mathias', 'Oui, à demain. Salut, Hicham.', 'Yes, see you tomorrow. Bye, Hicham.', [(791, 'Ouais toi aussi à demain'), (792, 'Salut')], ''),
    ('noemie', 'Il a tout cru sans hésiter?', 'He believed everything without hesitating?', [(790, 'navré Hicham')], ''),
    ('mathias', 'Absolument, notre secret est bien gardé.', 'Absolutely, our secret is well kept.', [(792, 'Salut')], ''),
]
WALK = [
    (0, None, "'Hello, Hicham? How are you doing?' Mathias answers the phone with polite calm."),
    (1, None, "'They signed the contract yesterday evening.' Hicham delivers the bad news about the rival deal."),
    (2, None, "'It is not true, it is signed?' Mathias feigns complete disbelief."),
    (3, None, "'Yes, the co-production deal is done.' Hicham confirms the deal with Solaris."),
    (4, None, "'I did not know that at all.' Mathias denies any prior knowledge."),
    (5, None, "'Frankly, I am totally dismayed.' He exaggerates his emotional distress."),
    (6, None, "'It is really terrible bad luck.' Mathias laments the supposed stroke of misfortune."),
    (7, None, "'We lost this project together.' Hicham mourns their mutual loss."),
    (8, None, "'I see nothing else to do.' Mathias claims total helplessness."),
    (9, None, "'I am truly sorry, Hicham.' He offers condolences to his rival boss."),
    (10, None, "'Thank you, see you tomorrow at the office.' Hicham thanks him and ends the call."),
    (11, None, "'Yes, see you tomorrow. Bye, Hicham.' Mathias says goodbye and hangs up."),
    (12, None, "'He believed everything without hesitating?' Noemie asks if the boss fell for the trick."),
    (13, None, "'Absolutely, our secret is well kept.' Mathias smiles with triumph. Now listen to the whole scene again at normal speed, and see how much more you catch."),
]
