# Authoring module for dix-pour-cent-s04e02-scene-09.
ID = 'dix-pour-cent-s04e02-scene-09'
SHOW = 'dix-pour-cent'
SEASON = 4
EPISODE = 2
SCENE = 9
TITLE = "L'attente au café  (Waiting at the Café)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'serveur': 'Le serveur'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S04E02'
SOURCE_FILE = 'sources/dix-pour-cent/s04/e02.fr.dual.srt'
INTRO = "Sitting anxiously at a bistro table, Andrea waits for her important meeting with iconic actress Nathalie Baye. When she orders another coffee, a playful waiter teases her with celebrity lookalikes until an urgent phone call reveals that Mathias has diverted Nathalie to ASK. Let's listen to their conversation in French first."
OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."
OUTRO = "Andrea races out of the cafe after realizing Mathias has intercepted Nathalie Baye. When you watch the episode, listen out for the expressions meaning 'excuse me' and 'madam'. You'll catch them now. See you next time!"
CLOSING = ('andrea', 'À bientôt!')
STORY = [
    ('andrea', 'Pardon monsieur, excusez-moi.', 'Pardon sir, excuse me.', [(449, 'Pardon, excusez-moi.')], ''),
    ('serveur', 'Oui madame, que désirez-vous?', 'Yes madam, what would you like?', [(450, 'Bien sûr.')], ''),
    ('andrea', 'Je peux commander un autre café?', 'Can I order another coffee?', [(450, 'Je peux commander un autre café ?')], ''),
    ('serveur', "Bien sûr, je vous l'apporte immédiatement.", 'Of course, I bring it to you immediately.', [(450, 'Bien sûr.')], ''),
    ('andrea', "Vous avez vu Nathalie Baye aujourd'hui?", 'Have you seen Nathalie Baye today?', [(451, 'Vous avez vu Nathalie Baye ?')], ''),
    ('serveur', 'Nathalie Baye? Non, pas du tout.', 'Nathalie Baye? No, not at all.', [(452, 'Nathalie Baye ?'), (453, 'Non, mais Catherine Deneuve est là-bas.')], ''),
    ('serveur', 'Mais Catherine Deneuve est assise là-bas!', 'But Catherine Deneuve is seated over there!', [(453, 'Catherine Deneuve est là-bas.')], ''),
    ('andrea', 'Vraiment? Où ça dans la salle?', 'Really? Where in the room?', [(453, 'Vraiment ? Où ça ?')], ''),
    ('serveur', "Je plaisante, c'était une petite blague!", 'I am joking, it was a little joke!', [(454, 'Je plaisante !')], ''),
    ('andrea', "Super, je n'ai pas le temps de rire.", 'Great, I do not have time to laugh.', [(455, 'Super.')], ''),
    ('andrea', 'Allô Gabriel? Où est passée Nathalie?', 'Hello Gabriel? Where did Nathalie go?', [(451, 'Nathalie')], ''),
    ('andrea', "Mathias l'a emmenée directement à l'agence!", 'Mathias took her directly to the agency!', [], ''),
    ('serveur', 'Madame, voici votre nouveau café chaud!', 'Madam, here is your hot fresh coffee!', [(450, 'café')], ''),
    ('andrea', 'Donnez-le plutôt à Catherine Deneuve!', 'Give it instead to Catherine Deneuve!', [(453, 'Catherine')], ''),
]
WALK = [
    (0, None, "'Pardon sir, excuse me.' Andrea calls the waiter to her table."),
    (1, None, "'Yes madam, what would you like?' The waiter responds with professional courtesy."),
    (2, None, "'Can I order another coffee?' Andrea asks for another drink while waiting."),
    (3, None, "'Of course, I bring it to you immediately.' The waiter confirms the second cup."),
    (4, None, "'Have you seen Nathalie Baye today?' Andrea checks whether her actress has arrived."),
    (5, None, "'Nathalie Baye? No, not at all.' The waiter clarifies that he has not spotted her."),
    (6, None, "'But Catherine Deneuve is seated over there!' The waiter points out a playful illusion."),
    (7, None, "'Really? Where in the room?' Andrea takes the bait for a brief moment."),
    (8, None, "'I am joking, it was a little joke!' The waiter laughs at his own jest."),
    (9, None, "'Great, I do not have time to laugh.' Andrea shows her impatience under pressure."),
    (10, None, "'Hello Gabriel? Where did Nathalie go?' Andrea checks in by phone."),
    (11, None, "'Mathias took her directly to the agency!' Andrea learns of Mathias's tactical maneuver."),
    (12, None, "'Madam, here is your hot fresh coffee!' The waiter delivers the cup as she rises."),
    (13, None, "'Give it instead to Catherine Deneuve!' Andrea snaps back with dry sarcasm."),
]
