# Authoring module for dix-pour-cent-s02e01-scene-09.
ID = 'dix-pour-cent-s02e01-scene-09'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 1
SCENE = 9
TITLE = "L'agent de façade  (The Front Agent)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'gabriel': 'Gabriel', 'mathias': 'Mathias', 'virginie': 'Virginie'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E01'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e01.fr.dual.srt'
INTRO = "At the ASK offices, actress Virginie Efira arrives in complete distress. Scandalous magazine photos showed her kissing an old flame in Brussels, and her partner Ramzy Bedia immediately threw her out of their apartment. Now Mathias and Gabriel must manage the crisis. Let's listen to the scene in French first."
OPENER = "Let's examine how Gabriel and Mathias try to reassure a panicked actress."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "Gabriel has agreed to become Virginie's public agent while Mathias represents Ramzy. See you next time!"
CLOSING = ('virginie', 'À demain!')
STORY = [
    ('gabriel', "Virginie, bonjour! Merci d'être là.", 'Virginie, hello! Thank you for being here.', [(196, 'Virginie, bonjour !'), (197, "Merci d'être là.")], ''),
    ('virginie', "Il m'a donné trente minutes pour faire ma valise.", 'He gave me thirty minutes to pack my suitcase.', [(200, "Il m'a donné 30 minutes pour faire ma valise.")], ''),
    ('virginie', 'Aucune de mes affaires ne va ensemble.', 'None of my clothes match.', [(201, 'Aucune de mes affaires ne va ensemble.')], ''),
    ('gabriel', 'Tu aurais dû lui parler.', 'You should have spoken to him.', [(204, 'Tu aurais dû lui parler.')], ''),
    ('virginie', "C'était rien, juste un au revoir très affectueux.", 'It was nothing, just a very affectionate goodbye.', [(205, "C'était rien, juste un au revoir."), (206, 'Un au revoir très affectueux,')], ''),
    ('virginie', "Ce type ne compte pas, c'est une vieille histoire.", 'That guy does not matter, it is an old story.', [(211, 'Ce type ne compte pas'), (212, "C'est une très vieille flamme.")], ''),
    ('virginie', "J'ai tout gâché! Comment on paie le loyer maintenant?", 'How do we pay the rent now?', [(224, "J'ai tout gâché."), (225, 'Comment on paie le loyer ?')], ''),
    ('gabriel', 'Il faut être raisonnables. Mathias va trouver une solution.', 'We must be reasonable. Mathias will find a solution.', [(227, 'Il faut être raisonnables.'), (228, 'Mathias va trouver une solution.')], ''),
    ('mathias', "Virginie, calme-toi. On s'en occupe.", 'Virginie, calm down. We are handling it.', [(245, "on s'en occupe.")], ''),
    ('mathias', 'Les paparazzi sont en bas, ils vous attendent.', 'The paparazzi are downstairs, they are waiting for you.', [(246, 'Les paparazzi sont en bas !'), (247, "Ils m'ont dans leur viseur !")], ''),
    ('mathias', "Voilà ce qu'on va faire.", 'Here is what we are going to do.', [(255, "Bien, voilà ce qu'on va faire.")], ''),
    ('gabriel', 'Je serai en quelque sorte ton agent par intérim.', 'I will be your interim agent in a way.', [(257, 'Je serai en quelque sorte une agente par intérim.')], ''),
    ('mathias', 'Un arrangement temporaire, juste une façade.', 'A temporary arrangement, just a facade.', [(259, 'Un arrangement temporaire. Juste une façade.')], ''),
    ('virginie', "D'abord mon mec me quitte, maintenant mon agent!", 'First my boyfriend leaves me, now my agent!', [(260, "D'abord mon mec me plaque, maintenant mon agent.")], ''),
    ('mathias', 'Ne le prends pas comme ça. Gabriel et moi travaillons ensemble.', 'Do not take it like that. Gabriel and I work together.', [(262, 'Ne le prends pas comme ça. Gabriel et moi'), (263, 'travaillons en étroite collaboration.')], ''),
    ('gabriel', 'On va arranger ça, on te le promet.', 'We are going to fix this, we promise you.', [(268, 'on va arranger de belles façades.'), (269, 'On vous le promet.')], ''),
]
WALK = [
    (0, ('gabriel', 'bonjour'), "'Virginie, hello! Thank you for being here.' Gabriel greets his client warmly as she arrives, using the word for 'hello'."),
    (1, ('virginie', 'valise'), "'He gave me thirty minutes to pack my suitcase.' Virginie sobs that Ramzy gave her thirty minutes to pack her bags and leave, using the word for 'suitcase'."),
    (2, ('virginie', 'affaires'), "'None of my clothes match.' Looking down at her outfit, Virginie wails that none of her clothes even match, using the word for 'clothes'."),
    (3, ('gabriel', 'parler'), "'You should have spoken to him.' Gabriel gently points out that she should have talked to Ramzy the night before, using the verb for 'to speak'."),
    (4, ('virginie', 'au revoir'), "'It was nothing, just a very affectionate goodbye.' Virginie insists the kiss in the street was just an overly warm goodbye, using the phrase for 'goodbye'."),
    (5, ('virginie', 'vieille'), "'That guy does not matter, it is an old story.' Virginie swears the other man means nothing to her and is just old history, using the word for 'old'."),
    (6, ('virginie', 'loyer'), "'I ruined everything! How do we pay the rent now?' Virginie bursts into tears, wondering how they will pay the rent, using the word for 'rent'."),
    (7, ('gabriel', 'raisonnables'), "'We must be reasonable. Mathias will find a solution.' Gabriel urges patience while invoking Mathias's authority, using the word for 'reasonable'."),
    (8, ('mathias', 'calme-toi'), "'Virginie, calm down. We are handling it.' Mathias tells Virginie to calm down and promises that the agency is handling it, using the phrase for 'calm down'."),
    (9, ('mathias', 'en bas'), "'The paparazzi are downstairs, they are waiting for you.' Mathias warns them that the paparazzi are waiting downstairs, using the phrase for 'downstairs'."),
    (10, ('mathias', 'faire'), "'Here is what we are going to do.' Mathias introduces a plan of action, using the verb for 'to do'."),
    (11, ('gabriel', 'agent'), "'I will be your interim agent in a way.' Gabriel offers to serve as her interim representative, using the word for 'agent'."),
    (12, ('mathias', 'façade'), "'A temporary arrangement, just a facade.' Mathias clarifies the diplomatic nature of the split, calling it a temporary front."),
    (13, ('virginie', 'mec'), "'First my boyfriend leaves me, now my agent!' Virginie sums up her terrible morning with dark humour, using a slang word for 'boyfriend'."),
    (14, ('mathias', 'ensemble'), "'Do not take it like that. Gabriel and I work together.' Mathias calms her down and reminds her that he and Gabriel work together, using the word for 'together'."),
    (15, ('gabriel', 'promet'), "'We are going to fix this, we promise you.' Gabriel ends on a supportive note, promising they will fix it, using the verb for 'promise'."),
]
