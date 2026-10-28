# Authoring module for dix-pour-cent-s02e05-scene-04.
ID = 'dix-pour-cent-s02e05-scene-04'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 5
SCENE = 4
TITLE = 'Le contrat de Camille  (Extending the Contract)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E05'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e05.fr.dual.srt'
INTRO = "In the hallway at ASK, Camille approaches Mathias to sign her contract extension. With Andréa angry over recent agency drama and refusing to sign, Camille fears for her job, while Mathias urges her to keep a low profile. Let's listen to the scene in French first."
OPENER = "Let's examine how Camille negotiates her contract extension with Mathias."
TRANSITION = "Now let's listen to Camille and Mathias's tense conversation again at full speed."
OUTRO = "Camille refuses Mathias's offer of cash, insisting on the formal recognition of her contract. Her determination shows her professional pride as she fights for her rightful place at ASK. See you next time!"
CLOSING = ('camille', 'Au revoir!')
STORY = [
    ('camille', 'Mathias, peux-tu signer mon contrat de travail?', 'Mathias, can you sign my employment contract?', [(119, "Vous pouvez signer mon contrat, s'il vous plaît ?")], ''),
    ('mathias', "Désolé Camille, je n'ai vraiment pas le temps.", 'Sorry Camille, I really do not have time.', [(115, "Désolé, je n'ai pas le temps.")], ''),
    ('camille', "C'est pour prolonger mon contrat à l'agence.", 'It is to extend my contract at the agency.', [(113, "C'est pour prolonger mon contrat à durée déterminée.")], ''),
    ('mathias', "Ce n'est pas à Andréa de signer?", 'Is it not for Andréa to sign?', [(120, 'Ça ne devrait pas être Andréa ?')], ''),
    ('camille', 'Andréa est furieuse et refuse de me parler.', 'Andréa is furious and refuses to speak to me.', [(122, 'Elle se comporte comme une idiote.')], ''),
    ('mathias', "Ne t'inquiète pas, ça va se calmer.", 'Do not worry, it is going to calm down.', [(123, 'Ça va se tasser.')], ''),
    ('camille', "Mais je n'ai aucun contrat officiel maintenant.", 'But I have no official contract now.', [(133, "Je n'ai pas de contrat !")], ''),
    ('mathias', "Personne à l'agence ne veut ton départ.", 'Nobody at the agency wants your departure.', [(126, "Personne ne veut que tu partes. C'est moi qui suis dans le chemin.")], ''),
    ('camille', 'Alors je vais demander directement à Hicham.', 'Then I am going to ask Hicham directly.', [(129, '-Je vais demander à Hicham.')], ''),
    ('mathias', 'Non, surtout pas, Hicham est très impulsif.', 'No, especially not, Hicham is very impulsive.', [(130, 'Vaut mieux pas.'), (131, 'Il est impulsif.')], ''),
    ('mathias', "L'histoire avec Isabelle Adjani l'a énervé.", 'The affair with Isabelle Adjani annoyed him.', [(131, "Cette histoire avec Adjani l'a énervé.")], ''),
    ('camille', 'Comment puis-je vivre sans salaire ici?', 'How can I live without a salary here?', [(135, "T'as besoin de combien ?")], ''),
    ('mathias', "Regarde, de combien d'argent as-tu besoin?", 'Look, how much money do you need?', [(134, 'Regarde.'), (135, "T'as besoin de combien ?")], ''),
    ('camille', 'Je veux juste mon contrat de travail!', 'I just want my employment contract!', [(133, "Je n'ai pas de contrat !")], ''),
]
WALK = [
    (0, None, "'Mathias, can you sign my employment contract?' Notice how the verb for 'can you' leads straight into 'employment'."),
    (1, None, "'Sorry Camille, I really do not have time.' A hurried brush-off avoiding immediate workplace commitment."),
    (2, None, "'It is to extend my contract at the agency.' Camille clarifies the administrative purpose."),
    (3, None, "'Is it not for Andréa to sign?' Mathias deflects responsibility back to her direct supervisor."),
    (4, None, "'Andréa is furious and refuses to speak to me.' Camille explains the office tension paralyzing her status."),
    (5, None, "'Do not worry, it is going to calm down.' A reassuring prediction urging patience."),
    (6, None, "'But I have no official contract now.' Anxious insistence highlighting legal vulnerability."),
    (7, None, "'Nobody at the agency wants your departure.' Reassurance that her employment is valued."),
    (8, None, "'Then I am going to ask Hicham directly.' A bold threat to escalate the matter to the majority owner."),
    (9, None, "'No, especially not, Hicham is very impulsive.' The key word here means 'especially', paired with 'hasty' to make the point clear."),
    (10, None, "'The affair with Isabelle Adjani annoyed him.' Mathias cites current executive irritation."),
    (11, None, "'How can I live without a salary here?' A blunt practical question about daily livelihood."),
    (12, None, "'Look, how much money do you need?' Mathias instinctively offers financial assistance."),
    (13, None, "'I just want my employment contract!' Camille rejects a handout, demanding professional legitimacy."),
]
