# Authoring module for dix-pour-cent-s04e04-scene-23.
ID = 'dix-pour-cent-s04e04-scene-23'
SHOW = 'dix-pour-cent'
SEASON = 4
EPISODE = 4
SCENE = 23
TITLE = 'Vos méthodes sont révoltantes  (Your methods are revolting)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'mathias': 'Mathias', 'ulrika': 'Ulrika'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S04E04'
SOURCE_FILE = 'sources/dix-pour-cent/s04/e04.fr.dual.srt'
INTRO = "Mathias is furious about what happened to Camille. He decides to call the author, Ulrika, to cancel their secret deal. We'll hear it in French first, don't worry about catching every word."
OPENER = "Let's go back through it. Mathias makes his call."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around your methods are revolting, and for the words meaning 'to have' and 'to say'. You'll catch them now. See you next time!"
CLOSING = ('mathias', 'Au revoir.')
STORY = [
    ('ulrika', 'Allô?', 'Hello?', [(1207, 'Allô ?')], ''),
    ('mathias', 'Ulrika?', 'Is this Ulrika?', [(1207, 'Ulrika ?')], ''),
    ('mathias', 'Ici Mathias Barneville.', 'This is Mathias Barneville speaking.', [(1208, 'Ici Mathias Barneville.')], ''),
    ('ulrika', 'Oui, bonjour Mathias.', 'Yes, hello Mathias.', [], ''),
    ('mathias', "Camille m'a tout dit.", 'Camille told me everything.', [(1209, "Camille m'a tout dit.")], ''),
    ('mathias', 'Je sais la vérité.', 'I know the truth.', [], ''),
    ('ulrika', 'Mais Mathias, attendez.', 'But Mathias, wait.', [], ''),
    ('mathias', "Non, c'est terminé.", 'No, it', [], ''),
    ('mathias', 'Vos méthodes sont révoltantes.', 'Your methods are revolting.', [(1209, 'Vos méthodes sont révoltantes,')], ''),
    ('mathias', 'Je refuse de travailler avec vous.', 'I refuse to work with you.', [], ''),
    ('ulrika', 'Vous faites une erreur.', 'You are making a mistake.', [], ''),
    ('mathias', 'Ne me rappelez plus jamais.', 'Don', [(1210, 'ne me rappelez plus jamais.')], ''),
    ('mathias', 'Au revoir, Ulrika.', 'Goodbye, Ulrika.', [], ''),
]
WALK = [
    (0, None, "'Hello?' The author answers the phone."),
    (1, None, "'Is this Ulrika?' He confirms it is her on the line."),
    (2, None, "'This is Mathias Barneville speaking.' He introduces himself formally with his full name."),
    (3, None, "'Yes, hello Mathias.' She replies calmly."),
    (4, None, "'Camille told me everything.' He says Camille confessed about the scheme."),
    (5, None, "'I know the truth.' He knows all the details now."),
    (6, None, "'But Mathias, wait.' She tries to stop him from speaking."),
    (7, None, "'No, it's over.' He refuses to listen to her excuses."),
    (8, None, "'Your methods are revolting.' He condemns her terrible actions."),
    (9, None, "'I refuse to work with you.' He cancels their secret deal completely."),
    (10, None, "'You are making a mistake.' She tries to warn him."),
    (11, None, "'Don't ever call me again.' He gives a strict instruction to stay away."),
    (12, None, "'Goodbye, Ulrika.' He says farewell and cuts the line. Let's listen to the whole scene again."),
]
