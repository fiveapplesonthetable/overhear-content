# Authoring module for dix-pour-cent-s02e01-scene-03.
ID = 'dix-pour-cent-s02e01-scene-03'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 1
SCENE = 3
TITLE = "Matin agité à l'agence ASK  (Hectic Morning at the ASK Agency)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'gabriel': 'Gabriel', 'herve': 'Hervé', 'noemie': 'Noémie'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E01'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e01.fr.dual.srt'
INTRO = "The next morning at the ASK agency reception desk, Noémie is busy fielding phone calls from fans. Gabriel arrives looking for Camille while Hervé brings the morning mail. Suddenly a shocking magazine cover catches their attention. Let's listen to the scene in French first."
OPENER = "Let's examine how normal agency banter suddenly turns into an emergency."
TRANSITION = "Now let's listen to the whole morning scene at ASK again without pausing."
OUTRO = "The tabloid magazine is on newsstands everywhere, threatening Virginie and Ramzy's film release. The agents must quickly find a way to manage the fallout. See you next time!"
CLOSING = ('gabriel', 'Au revoir!')
STORY = [
    ('gabriel', 'Camille est là? Où est-elle?', 'Is Camille here? Where is she?', [(72, 'Camille est là ?'), (73, 'Mais elle est où')], ''),
    ('noemie', "Camille n'est pas encore arrivée.", 'Camille has not arrived yet.', [(72, 'Pas encore.')], ''),
    ('gabriel', 'On se retrouve au café comme la première fois.', "Let's meet at the cafe like the first time.", [(74, 'On se retrouve au Café'), (75, 'comme la première fois.')], ''),
    ('gabriel', "Attends, tu ne t'appelles pas Laurence?", "Wait, isn't your name Laurence?", [(77, "Tu ne t'appelles pas Laurence ?")], ''),
    ('noemie', "Non, Laura Smet n'habite pas ici.", 'No, Laura Smet does not live here.', [(78, "Non, Laura Smet n'habite pas ici.")], ''),
    ('noemie', 'Vous pouvez envoyer du courrier pour elle.', 'You can send mail for her.', [(79, 'Vous pouvez envoyer du courrier ici')], ''),
    ('herve', 'Bonjour Noémie, le meilleur pour la fin!', 'Hello Noémie, the best for last!', [(84, 'Le meilleur pour la fin !')], ''),
    ('herve', "Tu sens très bon aujourd'hui.", 'You smell very good today.', [(85, 'Tu sens bon !')], ''),
    ('noemie', "C'est le parfum de Léa Seydoux.", "It is Lea Seydoux's perfume.", [(86, "C'est le parfum de Léa Seydoux.")], ''),
    ('herve', 'Tu sens comme une vraie star!', 'You smell like a real star!', [(87, 'Tu sens la star !')], ''),
    ('gabriel', "Noémie, j'ai des choses pour toi.", 'Noémie, I have things for you.', [(88, "J'ai des choses pour toi.")], ''),
    ('noemie', 'Regardez la couverture de ce magazine!', 'Look at the cover of this magazine!', [(90, 'LA NOUVELLE PASSION DE VIRGINIE EFIRA')], ''),
    ('herve', 'La nouvelle passion de Virginie Efira?', "Virginie Efira's new passion?", [(90, 'LA NOUVELLE PASSION DE VIRGINIE EFIRA')], ''),
    ('gabriel', "Mince! C'est une catastrophe pour l'agence.", 'Darn! It is a disaster for the agency.', [(91, 'Merde !')], ''),
]
WALK = [
    (0, ('gabriel', 'Où'), "'Is Camille here? Where is she?' Gabriel asks two quick questions about his missing assistant, using the word for 'where'."),
    (1, ('noemie', 'encore'), "'Camille has not arrived yet.' Noémie informs Gabriel that Camille has not arrived at the office yet, using the word for 'yet'."),
    (2, ('gabriel', 'la première fois'), "'Let\'s meet at the cafe like the first time.' Gabriel proposes they meet at the cafe like the very first time, using the expression for 'the first time'."),
    (3, ('gabriel', 'Attends,'), "'Wait, isn\'t your name Laurence?' Gabriel stops a passing visitor and tells her to wait, using the word for 'wait'."),
    (4, ('noemie', 'ici'), "'No, Laura Smet does not live here.' Noémie explains to the fan at reception that the actress does not live here, using the word for 'here'."),
    (5, ('noemie', 'courrier'), "'You can send mail for her.' Noémie tells the fan politely that they can send mail for the actress instead, using the word for 'mail'."),
    (6, ('herve', 'la fin!'), "'Hello Noémie, the best for last!' Hervé greets Noémie cheerfully with a classic saying about saving the best for the end, using the word for 'the end'."),
    (7, ('herve', "aujourd'hui"), "'You smell very good today.' Hervé compliments his colleague on how good she smells today, using the word for 'today'."),
    (8, ('noemie', 'parfum'), "'It is Lea Seydoux\'s perfume.' Noémie points out that it is a celebrity\'s perfume, using the word for 'perfume'."),
    (9, ('herve', 'vraie'), "'You smell like a real star!' Hervé tells her she smells like a real movie star, using the word for 'real' or 'true'."),
    (10, ('gabriel', 'choses'), "'Noémie, I have things for you.' Gabriel hands Noémie a stack of folders to process, mentioning he has things for her, using the word for 'things'."),
    (11, ('noemie', 'couverture'), "'Look at the cover of this magazine!' Noémie gasps and tells everyone to look at the cover of the gossip magazine, using the word for 'cover'."),
    (12, ('herve', 'nouvelle'), "'Virginie Efira\'s new passion?' Hervé reads the sensational headline aloud in disbelief, using the word for 'new'."),
    (13, ('gabriel', 'Mince!'), "'Darn! It is a disaster for the agency.' Gabriel exclaims in frustration that the news is a disaster for the agency, using a polite word for 'darn'."),
]
