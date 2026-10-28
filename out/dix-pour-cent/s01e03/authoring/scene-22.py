# Authoring module for dix-pour-cent-s01e03-scene-22.
ID = 'dix-pour-cent-s01e03-scene-22'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 3
SCENE = 22
TITLE = "Un Bardot pour rien  (A Bardot for Nothing)"
LEVEL = "A1 — débutant"
PAIR = 'fr-en'
VOICES = {"narrator": "sky", "gabriel": "theo", "camille": "emilie", "lea": "lucie"}
LABELS = {"gabriel": "Gabriel", "camille": "Camille", "lea": "Andréa"}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E03'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e03.fr.dual.srt'
INTRO = "Meanwhile, the partners have surprising news about the director Solveig Akerfelt. Both Laura Smet and her mother Nathalie Baye tried to sabotage their auditions so they wouldn't have to spend three months on a boat together, and Gabriel hasn't dared to tell anyone that Laura was rejected. First, let's listen to the whole scene in French; don't worry about catching every word."
OPENER = "Let's go through the scene step by step. In the meeting room, Gabriel is feeling guilty about the auditions."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "Right after this, in the agency kitchen, the actor Zinedine Soualem proudly demonstrates the new Portuguese coffee machine to prove he can play a Portuguese role. Meanwhile, Gabriel has to find a way to get Laura's part back from Solveig Akerfelt. See you next time!"
CLOSING = ("lea", "Au revoir!")
STORY = [
    ('gabriel', 'Je me sens mal pour Nathalie.', 'I feel bad for Nathalie.', [(556, 'Je me sens mal pour Nathalie')], ''),
    ('lea', "Comment ça s'est passé avec Laura Smet?", 'How did it go with Laura Smet?', [(557, "comment ça s'est passé"), (557, 'avec Laura Smet')], ''),
    ('gabriel', "Bien. Pas mal. Je n'ai pas encore de réponse.", 'Fine. Not bad. I don', [(558, 'Bien'), (559, 'Pas mal'), (560, 'de réponse')], ''),
    ('lea', 'Elle ne veut pas de Nathalie Baye.', 'She doesn', [(562, 'Elle ne veut pas de Nathalie Baye')], ''),
    ('gabriel', "Ce n'est pas possible!", 'That', [(562, 'pas possible')], ''),
    ('lea', "Akerfelt n'a pas aimé son essai. Ils sont complètement fous?", "Akerfelt didn't like her audition. Are they completely crazy?", [(565, "Akerfelt n'a pas aimé"), (566, 'Ils sont complètement fous')], ''),
    ('gabriel', "C'est dur. Ce n'est pas bon pour l'agence.", 'That', [(568, "C'est dur"), (569, "pour l'agence")], ''),
    ('camille', "Bonjour. Vous avez beaucoup d'appels.", 'Hello. You have lots of calls.', [(571, 'Bonjour'), (572, "beaucoup d'appels")], ''),
    ('camille', 'Isabelle Adjani a un problème de cheveux très urgent.', 'Isabelle Adjani has a very urgent hair problem.', [(575, 'Isabelle Adjani a un problème de cheveux très urgent')], ''),
    ('camille', 'On commence par qui?', 'Who do we start with?', [(576, 'On commence par qui')], ''),
    ('gabriel', 'Solveig Akerfelt.', 'Solveig Akerfelt.', [(576, 'Solveig Akerfelt')], ''),
    ('camille', "Elle n'est pas sur ma liste.", 'She isn', [(577, "Elle n'est pas sur ma liste")], ''),
    ('lea', "C'est méchant! Tu as fait faire un Bardot à Laura pour rien!", "That's mean! You made Laura do a Bardot for nothing!", [(578, "C'est méchant"), (579, 'Tu as fait faire un Bardot à Laura pour rien')], ''),
    ('lea', 'Sans Nathalie, Laura peut jouer la fille maintenant.', 'Without Nathalie, Laura can play the daughter now.', [(580, 'Sans Nathalie, Laura peut jouer la fille maintenant')], ''),
    ('camille', 'Je suis virée?', 'Am I fired?', [(581, 'Je suis virée')], ''),
    ('gabriel', 'Oui. Je suis désolé.', 'Yes. I', [(581, 'Oui. Je suis désolé')], ''),
    ('camille', 'Je suis vraiment virée?', 'Am I really fired?', [(582, 'Je suis vraiment virée')], ''),
    ('gabriel', 'Non, je fais un Bardot!', 'No, I', [(583, 'Non, je fais un Bardot')], ''),
]
WALK = [
    (0, None, "'I feel bad for Nathalie.' Literally 'I feel myself badly for Nathalie'. Gabriel thinks only Laura was rejected."),
    (1, None, "'How did it go with Laura Smet?' Literally 'how did it pass itself'. A very common everyday way to ask how something went."),
    (2, None, "'Fine. Not bad. I don't have an answer yet.' Gabriel lies to cover up Laura's disaster. Notice the negative with the word for 'yet' right after the verb."),
    (3, None, "'She doesn't want Nathalie Baye.' Here comes the shock: Nathalie's tragic audition worked all too well, and the director rejected her."),
    (4, None, "'That's not possible!' Standard negative around the verb 'is'. Now Gabriel realizes both actresses have lost their parts."),
    (5, None, "'Akerfelt didn't like her audition.' The past tense made negative, with the two negative words wrapping around the helper verb 'has'."),
    (6, None, "'Are they completely crazy?' The adjective at the end is in the masculine plural form."),
    (7, None, "'That's tough. It's not good for the agency.' Two short sentences with 'it is' and 'it is not'."),
    (8, None, "'Hello. You have lots of calls.' Back at Andréa's desk, Camille reads out the morning messages using the polite 'you'."),
    (9, None, "'Isabelle Adjani has a very urgent hair problem.' Notice how French links 'problem of hair' with the little word for 'of', and puts 'very urgent' at the end."),
    (10, None, "'Who do we start with?' Literally 'we start by whom?', using the everyday word for 'we'."),
    (11, None, "'Solveig Akerfelt.' Gabriel rushes in, still thinking about the Scandinavian director."),
    (12, None, "'She isn't on my list.' Camille checks her notepad, puzzled."),
    (13, None, "'That's mean!' Andréa is shocked that the director rejected a star like Nathalie Baye."),
    (14, None, "'You made Laura do a Bardot for nothing!' Earlier, Gabriel told Laura to act like an impossible diva, like Brigitte Bardot, so she wouldn't have to act with her mother."),
    (15, None, "'Without Nathalie, Laura can play the daughter now.' Now that her mother is out of the film, Laura would gladly take the part—if Gabriel hadn't ruined her audition!"),
    (16, None, "'Am I fired?' Gabriel plays a grim joke on Camille, telling her she is fired, and poor Camille believes him."),
    (17, None, "'Yes. I'm sorry.' He keeps a completely straight face."),
    (18, None, "'Am I really fired?' Notice the word for 'really' placed right between 'am' and 'fired'."),
    (19, None, "'No, I'm doing a Bardot!' He was just pretending, to let off steam, though Camille says her blood froze in her veins. Now let's hear the whole scene again from beginning to end."),
]
