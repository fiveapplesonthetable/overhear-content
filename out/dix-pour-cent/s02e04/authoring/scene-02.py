# Authoring module for dix-pour-cent-s02e04-scene-02.
ID = 'dix-pour-cent-s02e04-scene-02'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 4
SCENE = 2
TITLE = "L'arrivée d'Isabelle Adjani  (Adjani Arrives)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'isabelle': 'Isabelle', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E04'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e04.fr.dual.srt'
INTRO = "At the ASK offices, acclaimed French screen star Isabelle Adjani arrives to meet her agents. When Andréa mentions that young visionary director Sacha Hartman has a magnificent part for her, Isabelle expresses interest while insisting on proper artistic protocol. Let's listen to the scene in French first."
OPENER = "Let's examine how Andréa pitches the exciting new role to Isabelle Adjani."
TRANSITION = "Now let's listen to Andréa and Isabelle's elegant exchange again at full speed."
OUTRO = 'Isabelle agrees to meet Sacha Hartman, on the condition that Andréa acts with utmost discretion. Andréa immediately hurries to her office to arrange the high-profile meeting. See you next time!'
CLOSING = ('isabelle', 'Bonne soirée!')
STORY = [
    ('andrea', "Bonjour Isabelle, tu vas bien aujourd'hui?", 'Hello Isabelle, are you doing well today?', [(22, '-Bonjour, Isabelle. -Bonjour.'), (23, '-Tu vas bien ? -Très bien.')], ''),
    ('isabelle', 'Très bien, Andréa, merci beaucoup.', 'Very well, Andréa, thank you very much.', [(23, '-Très bien.')], ''),
    ('isabelle', "Tu t'occupes du réalisateur Sacha Hartman?", 'Do you handle the director Sacha Hartman?', [(25, 'Le prochain film de Sacha Hartman.'), (26, "-C'est l'un des tiens ? -Je m'occupe de lui.")], ''),
    ('andrea', "Oui, je m'occupe de lui.", 'Yes, I take care of him.', [(26, "-Je m'occupe de lui.")], ''),
    ('isabelle', "J'adore son travail, il est très talentueux.", 'I love his work, he is very talented.', [(27, "Je l'adore."), (31, "C'est ça. Très talentueux.")], ''),
    ('isabelle', "Décrocher une Palme d'Or, c'est formidable.", "Winning a Palme d'Or, that is wonderful.", [(28, "Décrocher une Palme d'Or avec un premier film..."), (29, "C'est beau.")], ''),
    ('andrea', 'Il a un très beau rôle pour toi.', 'He has a very fine role for you.', [(35, 'Il a un très beau rôle pour toi.')], ''),
    ('isabelle', 'Vraiment? Mais je ne sollicite jamais les rôles.', 'Really? But I never solicit roles.', [(36, '-Vraiment ? -Oui.'), (38, "Ce n'est pas vraiment mon style"), (39, 'de solliciter des rôles.')], ''),
    ('mathias', "Isabelle préfère qu'un réalisateur lui demande.", 'Isabelle prefers that a director asks her.', [(41, "Isabelle aime qu'un réalisateur demande. C'est juste, c'est comme ça que ça marche.")], ''),
    ('andrea', 'Les réalisateurs aiment aussi se sentir désirés.', 'Directors also like to feel wanted.', [(43, 'Les réalisateurs aiment se sentir désirés.')], ''),
    ('isabelle', 'On ferait mieux de lire le scénario.', 'We had better read the script.', [(45, "On ferait mieux de lire le scénario d'abord, ne nous précipitons pas.")], ''),
    ('andrea', 'Sacha est à Paris en ce moment.', 'Sacha is in Paris right now.', [(47, 'Sacha est à Paris en ce moment.')], ''),
    ('isabelle', "D'accord, mais s'il te plaît, sois discrète.", 'All right, but please, be discreet.', [(49, "D'accord, alors."), (51, '-Attends... -Sois discret !')], ''),
    ('andrea', "Oui, bien sûr, je l'appelle maintenant.", 'Yes, of course, I call him now.', [(50, "Je l'appelle maintenant."), (52, 'Oui, bien sûr.')], ''),
]
WALK = [
    (0, None, "'Hello Isabelle, are you doing well today?' Andréa inquires about well-being."),
    (1, None, "'Very well, Andréa, thank you very much.' Isabelle replies graciously and thanks Andréa warmly."),
    (2, None, "'Do you handle the director Sacha Hartman?' Isabelle inquires about client representation."),
    (3, None, "'Yes, I take care of him.' Andréa confirms that she represents the young director."),
    (4, None, "'I love his work, he is very talented.' High praise from an esteemed cinema star."),
    (5, None, "'Winning a Palme d'Or, that is wonderful.' Isabelle expresses admiration for his prestigious festival win."),
    (6, None, "'He has a very fine role for you.' Andréa links client to new project."),
    (7, None, "'Really? But I never solicit roles.' Isabelle asserts her artistic dignity as a star who never chases roles."),
    (8, None, "'Isabelle prefers that a director asks her.' Mathias defends his star client's traditional protocol."),
    (9, None, "'Directors also like to feel wanted.' Andrea counters with modern auteur psychology."),
    (10, None, "'We had better read the script.' Isabelle cautiously suggests that they read the script first."),
    (11, None, "'Sacha is in Paris right now.' Andréa creates opportune urgency."),
    (12, None, "'All right, but please, be discreet.' Isabelle demands absolute discretion."),
    (13, None, "'Yes, of course, I call him now.' Andréa promises to call the director right away."),
]
