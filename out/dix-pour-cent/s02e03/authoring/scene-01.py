# Authoring module for dix-pour-cent-s02e03-scene-01.
ID = 'dix-pour-cent-s02e03-scene-01'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 3
SCENE = 1
TITLE = "Norman s'entraîne à conduire  (Norman's Driving Practice)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'gabriel': 'Gabriel', 'norman': 'Norman'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E03'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e03.fr.dual.srt'
INTRO = "In Episode 3 of Season 2 of Dix pour cent, internet comedy star Norman Thavaud wants to pass his driving test for a film role even though he is terrified of cars, while Hicham tries to poach Fabrice Luchini behind the other agents' backs. We open in the ASK corridor as Gabriel catches up with Andréa. You'll hear the whole conversation in French first; don't worry about catching every word."
OPENER = "Let's examine how Gabriel coaches Norman during the driving lesson."
TRANSITION = "Now let's listen to Norman's frantic driving practice again at full speed."
OUTRO = "Norman tries his best behind the wheel, but his lack of driving experience makes Gabriel anxious. The upcoming film role requires a valid driver's license, raising the pressure on ASK. See you next time!"
CLOSING = ('gabriel', 'Au revoir!')
STORY = [
    ('gabriel', "On est dans les temps pour l'examen?", 'Are we on time for the exam?', [(2, 'On est dans les temps ?')], ''),
    ('norman', "Il faut se dépêcher, c'est loin.", 'We must hurry, it is far.', [(3, "Faut se dépêcher. -C'est loin.")], ''),
    ('gabriel', "Ne t'inquiète pas, respire bien.", 'Do not worry, breathe deeply.', [(16, 'Ça va aller. Respire bien.')], ''),
    ('norman', "Ça ne sert à rien d'être tendu.", 'It is useless to be tense.', [(18, "Comme je disais, ça sert à rien d'être tendu.")], ''),
    ('gabriel', 'Tu as oublié de parapher cette feuille.', 'You forgot to initial this sheet.', [(6, 'Désolé, vous avez oublié de parapher...')], ''),
    ('norman', "Attends, voilà, c'est bon maintenant.", 'Wait, here, it is good now.', [(7, '-celle-là. -Attends.'), (8, "C'est bon.")], ''),
    ('gabriel', 'Très bien, on y va quand même.', 'Very good, we go anyway.', [(11, "On y va quand même. D'accord.")], ''),
    ('gabriel', 'Bonne chance pour ton permis de conduire.', 'Good luck for your driving license.', [(13, '-Bonne chance, Norman.')], ''),
    ('norman', 'Merci Gabriel, je suis un peu stressé.', 'Thank you Gabriel, I am a bit stressed.', [(13, '-Merci.'), (20, 'Je suis pas tendu du tout.')], ''),
    ('norman', 'Est-ce que je continue tout droit?', 'Do I continue straight ahead?', [(24, '-Je continue ?')], ''),
    ('gabriel', 'Norman, il faut passer en deuxième.', 'Norman, you must shift into second gear.', [(25, 'Norman, il faut passer en deuxième...')], ''),
    ('gabriel', "Attention, c'est la cinquième vitesse!", 'Watch out, that is fifth gear!', [(27, "C'est la cinquième... Lâchez pas !")], ''),
    ('gabriel', "N'appuie pas sur le frein et l'accélérateur.", 'Do not press on the brake and the accelerator.', [(29, "N'appuyez pas"), (30, "sur le frein et l'accélérateur en même temps !")], ''),
    ('norman', "D'accord, je respire calmement.", 'All right, I am breathing calmly.', [(28, 'Respirez bien maintenant. Voilà.')], ''),
]
WALK = [
    (0, None, "'Are we on time for the exam?' The key word here means 'is', paired with 'test' to make the point clear."),
    (1, None, "'We must hurry, it is far.' The verb meaning 'is necessary' anchors the whole remark."),
    (2, None, "'Do not worry, breathe deeply.' A reassuring negative command form paired with a regular verb."),
    (3, None, "'It is useless to be tense.' The verb meaning 'serves' anchors the whole remark."),
    (4, None, "'You forgot to initial this sheet.' A compound past verb governing an infinitive."),
    (5, None, "'Wait, here, it is good now.' A series of short conversational particles confirming completion."),
    (6, None, "'Very good, we go anyway.' An encouraging adverbial opener with an idiomatic motion verb."),
    (7, None, "'Good luck for your driving license.' A classic wish of success specifying the driver's test."),
    (8, None, "'Thank you Gabriel, I am a bit stressed.' A courteous thanks followed by an adjective of emotional state."),
    (9, None, "'Do I continue straight ahead?' A standard question form formula asking for directional guidance."),
    (10, None, "'Norman, you must shift into second gear.' An impersonal modal verb followed by an ordinal gear number."),
    (11, None, "'Watch out, that is fifth gear!' Gabriel pairs the verb meaning 'is' with the noun for 'car gear'."),
    (12, None, "'Do not press on the brake and the accelerator.' The key word here means 'press', paired with 'gas pedal' to make the point clear."),
    (13, None, "'All right, I am breathing calmly.' An agreement token followed by an adverbial description of composure."),
]
