# Authoring module for dix-pour-cent-s02e02-scene-27.
ID = 'dix-pour-cent-s02e02-scene-27'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 2
SCENE = 27
TITLE = 'La fin de la lune de miel  (The End of the Honeymoon)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'hicham': 'Hicham', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E02'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e02.fr.dual.srt'
INTRO = "At the agency, Andréa tries unsuccessfully to reach Mathias Barneville before meeting with Hicham. When she tries to apologize for the disastrous evening with Fabrice Luchini, Hicham's patience runs out. Let's listen to the scene in French first."
OPENER = "Let's examine how Hicham is coldly dismissing Andréa with no hesitation."
TRANSITION = "Now let's listen to the whole discussion again without stopping."
OUTRO = 'Hicham has ruthlessly fired Andréa, asserting his complete authority as majority owner. Andréa faces exile from the agency she helped build. See you next time!'
CLOSING = ('andrea', 'Au revoir!')
STORY = [
    ('mathias', 'Vous êtes sur la messagerie de Mathias.', 'You have reached Mathias', [(896, 'Bonjour, vous êtes sur la messagerie de Mathias Barneville.')], ''),
    ('mathias', 'Laissez un message après le bip.', 'Leave a message after the beep.', [(897, 'Laissez un message et je vous rappellerai.')], ''),
    ('andrea', 'Mathias ne répond toujours pas.', 'Mathias is still not answering.', [(898, 'tu as vu Mathias ?')], ''),
    ('andrea', 'Bonjour, Hicham. Je suis désolée.', 'Hello, Hicham. I am sorry.', [(902, 'Bonjour.'), (903, 'Désolée pour hier soir.')], ''),
    ('andrea', 'Hier soir, la situation était difficile.', 'Last night, the situation was difficult.', [(904, "Ça s'est tendu, j'avais peur."), (905, "C'était horrible.")], ''),
    ('hicham', 'La lune de miel est terminée.', 'The honeymoon is over.', [(907, 'la lune de miel est terminée, Marteau.')], ''),
    ('hicham', "Prends tes affaires et va-t'en.", 'Take your things and go away.', [(908, "Prends tes affaires et va-t'en.")], ''),
    ('andrea', 'Arrête, Hicham, sois raisonnable.', 'Stop it, Hicham, be reasonable.', [(909, 'Arrête, Hicham.')], ''),
    ('hicham', 'Il y a des limites ici.', 'There are limits here.', [(910, 'Il y a des limites.')], ''),
    ('hicham', 'Nous ne sommes pas des animaux.', 'We are not animals.', [(910, "On n'est pas des animaux.")], ''),
    ('andrea', "Qu'est-ce que tu veux de plus?", 'What more do you want?', [(914, "Qu'est-ce que tu veux de plus ?")], ''),
    ('hicham', 'Rentre chez toi maintenant.', 'Go home now.', [(915, 'Rentre chez toi.')], ''),
    ('andrea', 'Tu ne peux pas me virer!', 'You cannot fire me!', [(916, 'Tu ne peux pas me virer.')], ''),
    ('hicham', 'Et pourquoi pas?', 'And why not?', [(916, 'Pourquoi pas ?')], ''),
    ('andrea', "Je suis associée de l'agence.", 'I am a partner in the agency.', [(917, 'Je suis associé, il faut un accord.')], ''),
    ('hicham', "Je suis l'actionnaire majoritaire.", 'I am the majority shareholder.', [(918, 'Je suis actionnaire majoritaire.')], ''),
    ('hicham', 'Laisse ton ordinateur et tes dossiers.', 'Leave your computer and your files.', [(920, 'Laisse tout ce qui appartient'), (921, 'ordinateur, clients... tout.')], ''),
]
WALK = [
    (0, None, "'You have reached Mathias's voicemail.' A standard French greeting on an answering machine."),
    (1, None, "'Leave a message after the beep.' Mathias's voicemail greeting instructs callers to leave a message after the beep."),
    (2, None, "'Mathias is still not answering.' Andréa sighs in frustration that Mathias is still not picking up his phone."),
    (3, None, "'Hello, Hicham. I am sorry.' A polite opening apology addressed to her boss."),
    (4, None, "'Last night, the situation was difficult.' Andréa explains that the situation with Fabrice Luchini was difficult the night before."),
    (5, None, "'The honeymoon is over.' A metaphor announcing the end of good relations."),
    (6, None, "'Take your things and go away.' Hicham snaps and orders Andréa to pack her things and get out."),
    (7, None, "'Stop it, Hicham, be reasonable.' An imperative followed by the subjunctive form of etre."),
    (8, None, "'There are limits here.' Hicham warns the partners that there are limits to what he will tolerate here."),
    (9, None, "'We are not animals.' A formal first-person plural negative statement."),
    (10, None, "'What more do you want?' An idiomatic question with de plus meaning further."),
    (11, None, "'Go home now.' Furious at her rebellion, Hicham orders Andréa to go home at once."),
    (12, None, "'You cannot fire me!' Andréa shoots back that he cannot fire a founding partner of the agency."),
    (13, None, "'And why not?' Hicham challenges her to say why he cannot dismiss her."),
    (14, None, "'I am a partner in the agency.' The feminine noun associee referring to her partnership status."),
    (15, None, "'I am the majority shareholder.' Hicham reminds her that he owns the majority of ASK's shares."),
    (16, None, "'Leave your computer and your files.' An imperative followed by possessive determiners."),
]
