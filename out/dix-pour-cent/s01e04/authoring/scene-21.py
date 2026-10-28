# Authoring module for dix-pour-cent-s01e04-scene-21.
ID = 'dix-pour-cent-s01e04-scene-21'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 4
SCENE = 21
TITLE = 'Le cours de pole dance  (The Pole-Dancing Class)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'audrey': 'Audrey', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E04'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e04.fr.dual.srt'
INTRO = "She has brought her two small children along to the dance studio, and Mathias arrives with the contracts. Let's hear the scene in French first; don't worry about catching every word."
OPENER = "Let's go through the scene step by step. The dance coach asks if Audrey is ready, and Audrey apologises for her ordinary sports clothes."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "Audrey is trying her best to prepare for the role and find a nanny, even if her heart isn't really in leaving her children. Back at her flat, she is about to interview her first nanny applicant—or so she thinks. See you next time!"
CLOSING = ('audrey', "À tout à l'heure!")
STORY = [
    ('audrey', "Je n'ai pas eu le temps d'acheter une tenue.", 'I didn', [(540, "Je n'ai pas eu le temps d'acheter")], ''),
    ('audrey', "J'ai un mois. J'ai déjà fait ça, mais il y a longtemps.", "I have one month. I've done it before, but a long time ago.", [(543, "J'ai un mois"), (544, 'Il y a longtemps')], ''),
    ('audrey', "On commence par le carrousel? Oh, c'est rapide!", 'Do we start with the carousel? Oh, that', [(546, 'Le carrousel'), (551, "Oh, c'est rapide")], ''),
    ('audrey', "Attention, c'est glissant!", 'Careful, it', [(553, "C'est glissant")], ''),
    ('audrey', "Mon cœur! Maman ne l'a pas fait exprès!", 'Sweetheart! Mummy didn', [(554, "Mon cœur ! Maman ne l'a pas fait exprès")], ''),
    ('audrey', "Fais voir, mon chéri. Je t'ai fait mal?", 'Let me see, darling. Did I hurt you?', [(555, "Fais voir, mon chéri. Je t'ai fait mal")], ''),
    ('audrey', "Bonjour, Mathias. Merci d'être venu.", 'Hello, Mathias. Thank you for coming.', [(557, 'Bonjour, Mathias'), (558, "Merci d'être venu")], ''),
    ('audrey', "Traverser Paris avec les enfants, c'est difficile.", 'Crossing Paris with the children is hard.', [(559, 'Traverser Paris avec')], ''),
    ('mathias', 'Pas de problème, Audrey.', 'No problem, Audrey.', [(560, 'Pas de problème'), (557, 'Audrey')], ''),
    ('audrey', "Dis bonjour à Mathias. Mais c'est quoi ces bêtises?", 'Say hello to Mathias. Hey, what is this nonsense?', [(561, 'Dis bonjour à Mathias'), (563, "C'est quoi ces bêtises")], ''),
    ('audrey', 'Elle sent que je pars. Les enfants sont comme des éponges.', 'She senses that I', [(564, 'Elle sent que je pars. Les enfants sont comme des éponges')], ''),
    ('mathias', "J'ai apporté cinq exemplaires des contrats.", 'I', [(565, "J'ai apporté cinq exemplaires des contrats")], ''),
    ('audrey', "Attends une seconde. C'est un questionnaire pour la nounou.", 'Wait a second. This is a questionnaire for the nanny.', [(566, 'Attends une seconde'), (567, "C'est pour la nounou")], ''),
    ('mathias', "Avez-vous un problème avec l'alcool, le Coca-Cola, les bonbons?", 'Do you have a problem with alcohol, Coca-Cola, sweets?', [(568, 'un problème avec'), (568, "l'alcool, le Coca-Cola, les bonbons")], ''),
    ('mathias', 'Quoi? Les bonbons?', 'What? Sweets?', [(568, 'les bonbons'), (568, 'Quoi')], ''),
    ('audrey', "Le sucre est très mauvais! J'ai vu un documentaire.", 'Sugar is very bad! I saw a documentary.', [(569, 'Le sucre est'), (570, "J'ai vu un documentaire")], ''),
    ('audrey', 'Dis-moi ce que tu en penses.', 'Tell me what you think of it.', [(571, 'Dis-moi ce que tu en penses')], ''),
]
WALK = [
    (0, None, "'I didn't have time to buy an outfit.' Literally 'I have not had the time to buy'. With two small children, she barely has a minute to herself."),
    (1, "J'ai un mois.", "'I have one month.' Before filming begins."),
    (1, "J'ai déjà fait ça, mais il y a longtemps.", "'I've done it before, but a long time ago.' Notice how 'ago' is expressed with the little phrase that usually means 'there is'."),
    (2, None, "'Do we start with the carousel? Oh, that's fast!' The coach shows her a spinning move on the pole."),
    (3, None, "'Careful, it's slippery!' Audrey spins round the pole, slips off, and accidentally bumps her little boy, who starts crying."),
    (4, None, "'Sweetheart! Mummy didn't do it on purpose!' Literally 'my heart!'. The last two words mean 'on purpose'."),
    (5, None, "'Let me see, darling. Did I hurt you?' Literally 'did I do bad to you?'. Just then, Mathias walks into the studio."),
    (6, None, "'Hello, Mathias. Thank you for coming.' Literally 'thank you for having come'."),
    (7, None, "'Crossing Paris with the children is hard.' That is why she asked Mathias to bring the contracts to the studio."),
    (8, None, "'No problem, Audrey.' Mathias is in a good mood now that she is taking the role."),
    (9, 'Dis bonjour à Mathias.', "'Say hello to Mathias.' Audrey speaks to her little girl, who answers with a cheeky toddler word instead."),
    (9, "Mais c'est quoi ces bêtises?", "'Hey, what is this nonsense?' The last word means 'silly things' or 'nonsense'."),
    (10, None, "'She senses that I'm leaving. Children are like sponges.' Audrey is already feeling guilty about leaving them to shoot the film."),
    (11, None, "'I've brought five copies of the contracts.' Mathias gets down to business."),
    (12, None, "'Wait a second. This is a questionnaire for the nanny.' Before signing anything, Audrey wants Mathias's opinion on her list of questions for nanny candidates."),
    (13, None, "'Do you have a problem with alcohol, Coca-Cola, sweets?' Mathias reads the question aloud in disbelief."),
    (14, None, "'What? Sweets?' He cannot believe she puts sweets on the same list as alcohol."),
    (15, None, "'Sugar is very bad! I saw a documentary.' Audrey is dead serious."),
    (16, None, "'Tell me what you think of it.' Literally 'tell me that which you think of it'. Let's listen to the whole scene again without stopping."),
]
