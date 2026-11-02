# Authoring module for dix-pour-cent-s02e06-scene-22.
ID = 'dix-pour-cent-s02e06-scene-22'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 6
SCENE = 22
TITLE = 'Perdus dans les couloirs  (Lost in the Corridors)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'hicham': 'Hicham', 'juliette': 'Juliette'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E06'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e06.fr.dual.srt'
INTRO = "Lost behind the scenes of the Palais des Festivals, Andrea, Juliette Binoche, and Hicham rush frantically through service hallways. Time is running out before the opening ceremony as panic escalates. Let's listen to the scene in French first."
OPENER = "Let's examine how Andrea, Juliette, and Hicham navigate the backstage maze step by step."
TRANSITION = "Now let's listen to the whole scene once more from start to finish."
OUTRO = "A frantic search for a restroom turns into a backstage labyrinth as Juliette's dress suffers unexpected damage moments before the show. See you next time!"
CLOSING = ('juliette', 'À bientôt!')
STORY = [
    ('andrea', 'Par ici, dépêchons-nous un peu!', 'This way, let us hurry up a bit!', [(604, 'Par ici.')], ''),
    ('juliette', 'Je dois monter sur scène bientôt.', 'I have to go on stage soon.', [(600, 'Tu montes')], ''),
    ('juliette', "C'est un véritable cauchemar!", 'It is a true nightmare!', [(603, 'un cauchemar')], ''),
    ('hicham', 'Où mènent tous ces longs couloirs?', 'Where do all these long corridors lead?', [(614, 'Un couloir')], ''),
    ('andrea', 'Il y a des toilettes par là.', 'There are bathrooms over there.', [(604, 'Il y a des toilettes par là.')], ''),
    ('juliette', 'Fais attention à ma robe!', 'Be careful with my dress!', [(605, 'fais attention.')], ''),
    ('hicham', 'Regardez, cette porte est fermée!', 'Look, this door is locked!', [(615, 'portes')], ''),
    ('andrea', "Ce n'est pas possible, nous tournons!", 'It is not possible, we are turning!', [(611, "C'est pas possible !")], ''),
    ('juliette', 'Je ne vois que des portes.', 'I only see doors.', [(615, 'portes marron.')], ''),
    ('hicham', 'On est complètement perdus ici!', 'We are completely lost here!', [(613, 'On est perdus !')], ''),
    ('andrea', 'Prenons ce couloir par ici.', 'Let us take this corridor this way.', [(606, 'Par ici.')], ''),
    ('juliette', 'Attention, ma belle robe se déchire!', 'Watch out, my beautiful dress is tearing!', [(617, 'Non !')], ''),
    ('andrea', 'Oh non, un accroc en bas!', 'Oh no, a tear at the bottom!', [(607, "c'est pas ça !")], ''),
    ('juliette', 'La cérémonie va bientôt commencer!', 'The ceremony will begin soon!', [(600, 'Tu montes')], ''),
]
WALK = [
    (0, None, "'This way, let us hurry up a bit!' Literally 'by here,' that quick two-word pointer leads into 'hurry-ourselves a little' in French."),
    (1, None, "'I have to go on stage soon.' Pairing 'I must' with 'mount on stage' in French drops any article before 'stage'—just like English 'on stage.'"),
    (2, None, "'It is a true nightmare!' Placing 'veritable' ahead of 'nightmare' intensifies the disaster in French, where 'nightmare' has its own vivid single word."),
    (3, None, "'Where do all these long corridors lead?' After 'where' in French, 'lead' flips ahead of the entire subject 'all these long corridors'!"),
    (4, None, "'There are bathrooms over there.' Notice the twin to line one's 'by here': swapping 'here' for 'there' after 'by' means 'that way' or 'over there.'"),
    (5, None, "'Be careful with my dress!' Literally 'make attention to my dress,' French builds 'be careful with' using 'make' and 'to'!"),
    (6, None, "'Look, this door is locked!' Depending on context, the description at the end can mean either 'closed' or 'locked' in French."),
    (7, None, "'It is not possible, we are turning!' Saying 'we turn' on its own captures the panicky feeling of going around in circles in French."),
    (8, None, "'I only see doors.' Framing 'see' inside 'not... than' expresses 'only' in French, followed by 'some doors.'"),
    (9, None, "'We are completely lost here!' Notice casual 'one is' paired with '-s' on 'lost'—because 'one' actually refers to all three of them in French!"),
    (10, None, "'Let us take this corridor this way.' Dropping 'we' before 'take' gives an instant 'let's take' suggestion in French."),
    (11, None, "'Watch out, my beautiful dress is tearing!' Turning 'tear' into 'tears itself' in French describes fabric ripping on its own without naming a culprit."),
    (12, None, "'Oh no, a tear at the bottom!' Built from 'hook,' that handy word means a 'snag' or 'rip' in fabric, followed by 'in low' for 'at the bottom.'"),
    (13, None, "'The ceremony will begin soon!' Placing 'soon' right between 'goes' and 'begin' slots the time adverb neatly inside the near-future pair in French."),
]
