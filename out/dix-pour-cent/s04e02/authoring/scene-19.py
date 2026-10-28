# Authoring module for dix-pour-cent-s04e02-scene-19.
ID = 'dix-pour-cent-s04e02-scene-19'
SHOW = 'dix-pour-cent'
SEASON = 4
EPISODE = 2
SCENE = 19
TITLE = 'Le prix du métier  (The Price of the Trade)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'elise': 'Élise', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S04E02'
SOURCE_FILE = 'sources/dix-pour-cent/s04/e02.fr.dual.srt'
INTRO = "Late at night, Elise Formet calls Mathias Barneville to deliver major industry news. While confirming that superstar Dany Boon has agreed to sign, Elise confronts Mathias on the cynical maneuvering required to win, forcing him to reflect on the nature of their business. Let's listen to their conversation in French first."
OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."
OUTRO = "Though victorious in securing Dany Boon, Mathias is left alone with the bitter truth of Elise's words. When you watch the episode, listen out for the expressions meaning 'done' and 'is going'. You'll catch them now. See you next time!"
CLOSING = ('mathias', 'À bientôt!')
STORY = [
    ('elise', "Allô Mathias? Oui, c'est enfin fait.", 'Hello Mathias? Yes, it is finally done.', [(1024, 'Allô'), (1024, "c'est fait")], ''),
    ('mathias', 'Dany Boon va signer chez nous?', 'Is Dany Boon signing with us?', [(1025, 'signer avec vous')], ''),
    ('elise', 'Oui, il a accepté notre offre.', 'Yes, he accepted our offer.', [(1025, 'signer avec vous')], ''),
    ('mathias', "C'est une très bonne nouvelle, merci.", 'That is very good news, thank you.', [(1026, "pas l'air ravi")], ''),
    ('elise', "Tu n'as pas l'air très ravi.", 'You do not seem very thrilled.', [(1026, "pas l'air ravi")], ''),
    ('mathias', 'Je suis fatigué par ces négociations.', 'I am tired from these negotiations.', [(1026, 'ce que vous vouliez')], ''),
    ('elise', "Tu n'as jamais honte de manipuler?", 'Are you never ashamed of manipulating?', [(1027, 'jamais honte'), (1029, 'manipuler les gens')], ''),
    ('mathias', "Honte de quoi? D'obtenir des contrats?", 'Ashamed of what? Of getting contracts?', [(1028, 'Honte de quoi')], ''),
    ('elise', 'De manipuler tous nos amis artistes?', 'Of manipulating all our artist friends?', [(1029, 'manipuler les gens')], ''),
    ('mathias', "C'est notre métier, nous l'avons choisi.", 'It is our job, we chose it.', [(1032, "C'est notre métier"), (1032, "on l'a choisi")], ''),
    ('elise', 'Ce métier détruit nos belles amitiés.', 'This profession destroys our good friendships.', [(1031, 'vraie question')], ''),
    ('mathias', 'Les affaires demandent de la dureté.', 'Business demands toughness.', [(1032, 'notre métier')], ''),
    ('elise', "Je t'envoie les contrats signés demain.", 'I will send you signed contracts tomorrow.', [(1033, 'envoyez les contrats demain')], ''),
    ('mathias', "D'accord, bonne soirée à toi, Élise.", 'All right, good evening to you, Elise.', [(1034, "D'accord")], ''),
]
WALK = [
    (0, None, "'Hello Mathias? Yes, it is finally done.' Elise delivers the long-awaited news."),
    (1, None, "'Is Dany Boon signing with us?' Mathias asks about the star client's signature."),
    (2, None, "'Yes, he accepted our offer.' Elise confirms the client's consent."),
    (3, None, "'That is very good news, thank you.' Mathias expresses measured appreciation."),
    (4, None, "'You do not seem very thrilled.' Elise detects a lack of genuine joy."),
    (5, None, "'I am tired from these negotiations.' Mathias admits the weariness of endless wrangling."),
    (6, None, "'Are you never ashamed of manipulating?' Elise confronts him with an uncomfortable moral truth."),
    (7, None, "'Ashamed of what? Of getting contracts?' Mathias defends his business results."),
    (8, None, "'Of manipulating all our artist friends?' Elise highlights the betrayal of personal relationships."),
    (9, None, "'It is our job, we chose it.' Mathias reminds her of the rules of the agency trade."),
    (10, None, "'This profession destroys our good friendships.' Elise mourns the erosion of authentic bonds."),
    (11, None, "'Business demands toughness.' Mathias explains the uncompromising demands of corporate survival."),
    (12, None, "'I will send you signed contracts tomorrow.' Elise returns to immediate paperwork tasks."),
    (13, None, "'All right, good evening to you, Elise.' Mathias concludes the conversation pensively."),
]
