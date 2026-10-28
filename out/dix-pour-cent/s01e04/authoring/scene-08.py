# Authoring module for dix-pour-cent-s01e04-scene-08.
ID = 'dix-pour-cent-s01e04-scene-08'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 4
SCENE = 8
TITLE = "Un acheteur allemand  (A German Buyer)"
LEVEL = "A1 — débutant"
PAIR = 'fr-en'
VOICES = {"narrator": "sky", "helene": "emilie", "mathias": "marcel", "lea": "lucie"}
LABELS = {"helene": "Hélène", "mathias": "Mathias", "lea": "Andréa"}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E04'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e04.fr.dual.srt'
INTRO = 'She has news about the sale of the agency, and none of the agents are going to like it. Meanwhile, the boss of rival agency StarMédia is still pressing Mathias to jump ship. Listen to the French first without worrying about catching every word.'
OPENER = "Let's walk through it step by step. Mathias arrives late and apologises to Hélène."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = 'A German buyer at the door, and Mathias tempted to leave for StarMédia. Next, we follow Mathias home for dinner with his wife Catherine. See you next time!'
CLOSING = ("lea", "Bonne soirée!")
STORY = [
    ('mathias', "Désolé. Vous savez ce que c'est, les actrices.", 'Sorry. You know what actresses are like.', [(211, "Désolé. Vous savez ce que c'est, les actrices")], ''),
    ('helene', "Samuel était l'expert. Une de ses anciennes amies veut voir son testament.", 'Samuel was the expert. One of his old friends wants to see his will.', [(212, "Samuel était l'expert"), (213, 'Une de ses anciennes'), (214, 'son testament')], ''),
    ('helene', "J'ai trouvé un acheteur pour l'agence. C'est une offre sérieuse.", "I've found a buyer for the agency. It's a serious offer.", [(215, "J'ai trouvé un acheteur pour l'agence. C'est une offre sérieuse")], ''),
    ('helene', 'Très généreuse, aussi.', 'Very generous, too.', [(216, 'Très généreuse, aussi')], ''),
    ('mathias', 'Vous pouvez nous en dire plus?', 'Can you tell us more about it?', [(217, 'Vous pouvez'), (217, 'en dire plus')], ''),
    ('helene', "Jonas Hirsch, de l'agence Sterne à Berlin. Vous le connaissez?", 'Jonas Hirsch, from the Sterne agency in Berlin. Do you know him?', [(218, "Jonas Hirsch, de l'agence Sterne à Berlin"), (219, 'Vous le connaissez')], ''),
    ('mathias', "Oui. Il veut créer un groupe d'agences européennes.", 'Yes. He wants to create a group of European agencies.', [(220, 'Oui'), (221, 'Il veut créer un'), (221, "d'agences européennes")], ''),
    ('helene', 'Je lui ai demandé de vous garder tous les quatre.', 'I asked him to keep all four of you.', [(222, 'Je lui ai demandé de vous garder tous les quatre')], ''),
    ('helene', "Mais je ne sais pas si c'est dans ses projets.", 'But I don', [(223, "mais je ne sais pas si c'est dans ses projets")], ''),
    ('lea', 'Il doit bien y avoir une solution!', 'There must be a solution!', [(224, 'Il doit bien y avoir une solution')], ''),
    ('mathias', 'On peut inventer une nouvelle taxe sur les acteurs français?', 'Can we invent a new tax on French actors?', [(225, 'Laquelle'), (226, "qu'il y a une nouvelle taxe sur les acteurs français")], ''),
    ('lea', 'Pas question, Gabriel! On doit trouver une autre solution.', 'Out of the question, Gabriel! We must find another solution.', [(227, "On n'est pas dans"), (230, 'Pas question'), (230, 'une solution')], ''),
    ('lea', "Tout le monde est au courant que l'agence est en vente.", 'Everyone knows that the agency is for sale.', [(231, 'Tout le monde est au courant'), (234, 'en vente')], ''),
    ('mathias', "C'est mauvais pour l'agence d'être en position de faiblesse.", 'It', [(236, "C'est mauvais pour l'agence"), (236, 'en position de faiblesse')], ''),
    ('lea', "Avec les Allemands qui achètent l'agence, qu'est-ce qu'on va faire?", 'With the Germans buying the agency, what are we going to do?', [(240, 'les Allemands qui')], ''),
    ('mathias', "Si je vais chez StarMédia maintenant, je vais avoir beaucoup d'ennemis.", 'If I go to StarMédia now, I', [(242, 'StarMédia maintenant'), (243, "beaucoup d'ennemis")], ''),
]
WALK = [
    (0, None, "'Sorry. You know what actresses are like.' Literally 'you know what it is, actresses'."),
    (1, None, "'Samuel was the expert. One of his old friends wants to see his will.' The adjective for 'old' or 'former' comes before the noun."),
    (2, None, "'I've found a buyer for the agency.' Past tense with 'have', and the noun for 'buyer' comes from the verb 'to buy'."),
    (3, None, "'It's a serious offer.' Feminine ending on the adjective to match 'offer'."),
    (4, None, "'Very generous, too.' Another feminine adjective ending, still describing the offer."),
    (5, None, "'Can you tell us more about it?' Two small object words sit before 'tell': 'to us' and 'about it'."),
    (6, None, "'Jonas Hirsch, from the Sterne agency in Berlin. Do you know him?' The little word for 'him' sits right before 'know'."),
    (7, None, "'Yes. He wants to create a group of European agencies.' Notice the feminine plural ending on 'European'."),
    (8, None, "'I asked him to keep all four of you.' Literally 'you all the four'."),
    (9, None, "'But I don't know if that's in his plans.' Hélène makes no promises about their jobs."),
    (10, None, "'Can we invent a new tax on French actors?' The verb 'must' followed by the expression for 'there to be'."),
    (11, None, "'Out of the question, Gabriel! We must find another solution.'s a new tax on French actors?' A weak joke at a tense moment."),
    (12, None, "'We're not in trade, Gabriel!' Andréa cuts the joke short."),
    (13, None, "'No way, we have to find a solution.' That two-word opener means 'out of the question'."),
    (14, None, "'Everyone knows that the agency is for sale.' Literally 'everyone is in the current', the everyday idiom for 'everyone knows'."),
    (15, None, "'It's bad for the agency to be in a position of weakness.' Meanwhile, over lunch at a restaurant, François of StarMédia tells Mathias that with the Germans buying ASK, nothing is keeping him there."),
    (16, None, "'With the Germans buying the agency, what are we going to do?' Capital letter on the nationality noun when it means the people."),
    (17, None, "'If I go to StarMédia now, I'll have a lot of enemies.' Talking to François, Mathias hesitates to betray Gabriel, Andréa, and Arlette, though François scoffs that they aren't real friends. Now let's hear the whole scene again from start to finish."),
]
