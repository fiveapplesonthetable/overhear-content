# Authoring module for dix-pour-cent-s02e01-scene-07.
ID = 'dix-pour-cent-s02e01-scene-07'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 1
SCENE = 7
TITLE = 'Réunion de crise financière  (Financial Crisis Meeting)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'gabriel': 'Gabriel', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E01'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e01.fr.dual.srt'
INTRO = "In the ASK conference room, Mathias calls an urgent meeting of the agency partners to discuss their dire finances. Between sluggish film productions and a massive five hundred thousand euro tax bill, drastic measures are needed immediately. Let's listen to the scene in French first."
OPENER = "Let's examine how the partners react to the emergency financial proposal step by step."
TRANSITION = "Now let's listen to the tense partners meeting once more."
OUTRO = "The partners are in open revolt against Mathias's austerity plan, refusing to accept any salary reductions. See you next time!"
CLOSING = ('andrea', 'À bientôt!')
STORY = [
    ('mathias', 'Tout le monde est là? On peut commencer.', 'Is everyone here? We can get started.', [(150, 'Tout le monde est là ?')], ''),
    ('andrea', "Tu vois bien que oui. Qu'est-ce qui se passe?", 'You can see we are. What is going on?', [(151, 'Tu vois bien que oui.')], ''),
    ('mathias', 'Voilà, on a eu six mois difficiles.', 'Well, we have had six difficult months.', [(152, 'Voilà, on a eu six mois difficiles.')], ''),
    ('mathias', 'Monter des films est compliqué, et on a des contrats en suspens.', 'Setting up films is complicated, and we have contracts on hold.', [(153, 'on a des contrats en suspens...')], ''),
    ('mathias', 'Cette année, nos bénéfices sont vraiment en baisse.', 'This year, our profits are really down.', [(154, 'Sans compter le nouveau cadre sur les salaires des comédiens...'), (155, 'Nos bénéfices sont en baisse sur le premier semestre.')], ''),
    ('mathias', 'Nous devons payer une amende de cinq cent mille euros.', 'We must pay a fine of five hundred thousand euros.', [(156, "On pourrait s'en sortir"), (157, 'si Mme Brancillon ne nous avait pas frappés'), (158, 'avec un redressement fiscal de 500 000 €.')], ''),
    ('gabriel', "Cinq cent mille euros? C'est absurde!", 'Five hundred thousand euros? That is absurd!', [(168, "C'est absurde.")], ''),
    ('andrea', "Dommage que la femme de Mathias n'ait pas pris de parts.", "Too bad Mathias\\'s wife did not take shares.", [(160, "Dommage que la femme de Mathias n'ait pas pris de parts.")], ''),
    ('mathias', "Mais elle n'en a pas pris. En conclusion...", 'But she did not take any. In conclusion...', [(161, "Mais elle n'en a pas pris."), (162, 'En conclusion...')], ''),
    ('mathias', 'Notre seule option est de réduire les salaires pendant deux mois.', 'Our only option is to reduce salaries for two months.', [(164, 'Notre seule option est de réduire les salaires pendant deux mois.')], ''),
    ('gabriel', 'Pardon? Les salaires de qui?', 'Excuse me? Whose salaries?', [(165, 'Pardon ?'), (166, '-Les salaires de qui ? -De tout le monde.')], ''),
    ('mathias', "Les salaires de tout le monde. Il n'y a pas d'autre solution.", "Everyone\\'s salaries. There is no other solution.", [(166, '-Les salaires de qui ? -De tout le monde.')], ''),
    ('andrea', 'Hors de question! Ne baissez pas mon salaire!', 'Out of the question! Do not lower my salary!', [(167, 'Hors de question, si vous réduisez le mien, je vais crever de faim.')], ''),
    ('gabriel', "C'est absurde, je suis d'accord!", 'It is absurd, I agree!', [(168, "C'est absurde."), (170, "Je suis d'accord !")], ''),
]
WALK = [
    (0, ('mathias', 'Tout le monde'), 'Mathias checks the attendance around the conference table, asking if everyone is there, using the phrase for everyone.'),
    (1, ('andrea', 'se passe?'), 'Andrea impatiently presses for the reason behind the sudden gathering, asking what is going on.'),
    (2, ('mathias', 'difficiles.'), 'Mathias begins his gloomy financial summary of the past semester, noting they have had six difficult months. Notice the word for difficult.'),
    (3, ('mathias', 'compliqué,'), 'Mathias reminds them that setting up films is complicated. Notice how the word for complicated is very similar in French.'),
    (4, ('mathias', 'bénéfices'), 'Decreasing revenues have tightened cash flow. Mathias points out that their profits are down. Pay attention to the word for profits.'),
    (5, ('mathias', 'amende'), 'The audit by the tax inspector has created an immediate crisis. They must pay a fine, which translates to this word.'),
    (6, ('gabriel', 'absurde!'), 'Gabriel expresses genuine disbelief at the astronomical tax penalty. He calls it absurd.'),
    (7, ('andrea', 'Dommage'), 'Andrea laments that Catherine refused to invest her personal fortune into the agency. She says it is too bad.'),
    (8, ('mathias', 'conclusion...'), 'Mathias cuts off the discussion about his private life, moving to his conclusion. The word for conclusion is identical.'),
    (9, ('mathias', 'option'), 'He proposes a temporary wage reduction across the board. He says their only option is to reduce salaries. Note the word for option.'),
    (10, ('gabriel', 'salaires'), 'Gabriel is stunned by the idea that employees and partners should take pay cuts. He asks whose salaries they are talking about.'),
    (11, ('mathias', 'solution.'), 'Mathias insists that survival requires equal sacrifice and there is no other solution. Notice how the word for solution is also similar.'),
    (12, ('andrea', 'question!'), 'Andrea protests dramatically that any cut to her salary will leave her starving. She says it is out of the question.'),
    (13, ('gabriel', "d'accord!"), "Gabriel backs Andrea and rejects the proposed payroll reductions, saying he agrees. Now let's listen to the tense partners meeting once more."),
]
