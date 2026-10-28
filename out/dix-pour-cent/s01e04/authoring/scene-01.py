# Authoring module for dix-pour-cent-s01e04-scene-01.
ID = 'dix-pour-cent-s01e04-scene-01'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = 'Vingt-trois mois de retard  (Twenty-Three Months Late)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
VOICES = {'narrator': 'sky', 'audrey': 'emilie', 'mathias': 'marcel', 'inspecteur': 'theo'}
LABELS = {'audrey': 'Audrey', 'mathias': 'Mathias', 'inspecteur': "L'inspecteur"}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E04'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e04.fr.dual.srt'
INTRO = "First, in the agency kitchen, Camille tries to blend in with Hervé and Noémie. You'll hear the whole scene in French first — don't worry about catching every word."
OPENER = "Let's go back through it step by step. Audrey is carrying her baby son down the corridor as she tries to keep up with Mathias."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = 'Outside, Audrey admits she already owes forty thousand euros in back taxes, and Mathias tells her she has no choice: she has to go back to work right away. See you next time!'
CLOSING = ('audrey', 'Au revoir!')
STORY = [
    ('audrey', 'Attends, tu marches trop vite. Je ne veux pas le réveiller.', "Wait, you're walking too fast. I don't want to wake him.", [(1, 'Attends, tu marches trop vite'), (2, 'Je ne veux pas le réveiller')], ''),
    ('audrey', "Il n'a pas dormi de la nuit. Il fait ses dents.", "He didn't sleep all night. He's teething.", [(3, "Il n'a pas dormi de la nuit"), (4, 'Il fait ses dents')], ''),
    ('mathias', 'On ne prend aucun risque. Laisse-moi parler.', 'We', [(10, 'On ne prend aucun risque'), (10, 'parler')], ''),
    ('inspecteur', "C'est votre mari?", 'Is he your husband?', [(16, "C'est votre mari ?")], ''),
    ('mathias', 'Non, son agent.', 'No, her agent.', [(16, 'Non, son agent')], ''),
    ('inspecteur', 'Madame, vous avez vingt-trois mois de retard.', 'Madam, you are twenty-three months late.', [(19, 'madame'), (20, 'vous avez'), (20, 'mois de retard')], ''),
    ('audrey', 'Oui, mais au moins je paie mes impôts en France!', 'Yes, but at least I pay my taxes in France!', [(21, 'Oui, mais au moins je paie mes impôts en France !')], ''),
    ('mathias', 'Audrey a eu deux enfants en trois ans.', 'Audrey had two children in three years.', [(24, 'Audrey a eu deux enfants en trois ans')], ''),
    ('mathias', 'Maintenant, elle veut retrouver du travail et payer ses impôts.', 'Now she wants to find work again and pay her taxes.', [(28, 'Maintenant, elle'), (28, 'retrouver du travail et payer ses impôts')], ''),
    ('inspecteur', 'Vous ne trouvez pas de travail, madame?', 'You can', [(30, 'Vous ne trouvez pas de travail, madame ?')], ''),
    ('mathias', 'Bien sûr que si!', 'Of course she can!', [(32, 'Bien sûr que si')], ''),
    ('inspecteur', "Mais vous avez refusé un rôle dans un film d'action.", 'But you turned down a role in an action film.', [(36, 'vous avez'), (36, 'refusé un rôle'), (37, "Un film d'action")], ''),
    ('audrey', 'Je ne pouvais pas courir après des zombies!', 'I couldn', [(38, 'Je ne pouvais pas courir après des zombies')], ''),
    ('mathias', "Le retour d'Audrey sur un tournage est imminent.", 'Audrey', [(42, "le retour d'Audrey sur un tournage est imminent")], ''),
    ('audrey', "Oui, c'est un projet énorme.", 'Yes, it', [(44, "Oui, c'est un projet énorme")], ''),
    ('inspecteur', "J'attends votre chèque cette semaine, avec dix pour cent de plus.", 'I expect your cheque this week, with ten percent extra.', [(47, "J'attends votre chèque cette semaine"), (48, "Et comme c'est en retard")], ''),
]
WALK = [
    (0, None, "'Wait, you're walking too fast.' A casual command from the verb 'to wait', followed by 'you walk too fast'."),
    (1, None, "'I don't want to wake him.' The negative wraps around 'want', and the little word for 'him' sits right before the verb 'to wake'."),
    (2, None, "'He didn't sleep all night.' Literally 'of the night', the idiomatic way to say 'all night long' after a negative."),
    (3, None, "'He's teething.' Literally 'he is making his teeth'."),
    (4, None, "'We're not taking any risks. Let me do the talking.' The negative word after the verb means 'no' or 'not any'. Mathias thinks the friendly inspector Mr Jarron is still in charge, but a much stricter man is sitting at the desk."),
    (5, None, "'Is he your husband?' The inspector uses the polite 'your' as they sit down."),
    (6, None, "'No, her agent.' The word for 'his' or 'her' takes the masculine form here because 'agent' is a masculine noun."),
    (7, None, "'Madam, you are twenty-three months late.' Literally 'you have twenty-three months of delay'. French uses 'to have' with a noun for being late."),
    (8, None, "'Yes, but at least I pay my taxes in France!' Unlike rich stars who move abroad. Her proud defence doesn't impress the inspector at all."),
    (9, None, "'Audrey had two children in three years.' The everyday past tense of 'to have', 'has had'."),
    (10, None, "'Now she wants to find work again and pay her taxes.' The prefix on 'to find again' works just like 're-' in English."),
    (11, None, "'You can't find work, madam?' After a negative, the word for 'some' becomes the simple short word for 'of' or 'any'."),
    (12, None, "'Of course she can!' Notice how 'well' sets up the clause and leads naturally into 'yes!'."),
    (13, None, "'But you turned down a role in an action film.' The inspector has been reading the newspapers."),
    (14, None, "'I couldn't run after zombies!' She had just given birth when that part was offered to her. The verb 'could' is in the past tense used for how things were."),
    (15, None, "'Audrey's return to a film shoot is imminent.' Mathias invents a big comeback on the spot."),
    (16, None, "'Yes, it's a huge project.' Audrey plays along with her agent's lie."),
    (17, None, "'I expect your cheque this week, with ten percent extra.' The lie backfires: if she has a big film coming, she doesn't need any more time to pay. Now let's hear the whole scene at the tax office again."),
]
