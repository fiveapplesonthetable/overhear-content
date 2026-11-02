# Authoring module for dix-pour-cent-s02e05-scene-09.
ID = 'dix-pour-cent-s02e05-scene-09'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 5
SCENE = 9
TITLE = 'La nouvelle junior  (The New Junior)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'camille': 'Camille', 'hicham': 'Hicham'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E05'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e05.fr.dual.srt'
INTRO = "In the ASK conference room, Hicham interrupts the partners meeting to deliver a major announcement. Without consulting the other agents, he reveals his choice for the new junior agent position. Let's listen to the scene in French first."
OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the whole dialogue again."
OUTRO = "Hicham stuns the agency partners by appointing Camille as the new junior agent. Despite Andrea's surprise, Hicham praises Camille's tenacity, discretion, and quiet courage. See you next time!"
CLOSING = ('hicham', 'Au revoir!')
STORY = [
    ('hicham', "Et maintenant, que diriez-vous d'accueillir officiellement notre nouveau junior?", 'And now, what would you say to officially welcoming our new junior?', [(259, "que diriez-vous d'accueillir officiellement notre nouveau junior ?")], ''),
    ('andrea', 'Vous auriez dû nous consulter avant.', 'You should have consulted us beforehand.', [(260, 'Vous auriez dû nous consulter.')], ''),
    ('hicham', "Je me suis consulté moi-même. Et j'ai décidé.", 'I consulted myself. And I decided.', [(261, 'Je me suis consulté moi-même.'), (262, "Et j'ai décidé.")], ''),
    ('hicham', 'Notre nouveau junior est une femme.', 'Our new junior is a woman.', [(263, 'Notre nouveau junior est une femme.')], ''),
    ('hicham', "Et elle s'appelle Camille Valentini.", 'And her name is Camille Valentini.', [(264, "Et elle s'appelle Camille..."), (265, 'Valentini.')], ''),
    ('andrea', 'Quoi? Camille?', 'What? Camille?', [(265, 'Quoi ?')], ''),
    ('hicham', 'Il y avait des candidats qui savaient très bien se vendre.', 'There were candidates who knew very well how to sell themselves.', [(266, 'Il y avait des candidats qui savaient très bien se vendre.')], ''),
    ('hicham', "Elle, elle n'a pas parlé, elle a agi.", 'She did not talk, she acted.', [(267, "Elle, elle n'a pas parlé, elle a agi.")], ''),
    ('andrea', 'Camille, vous étiez candidate?', 'Camille, were you a candidate?', [(268, 'Vous étiez candidate ?')], ''),
    ('camille', 'Non, pas du tout.', 'No, not at all.', [(268, 'Non, pas du tout.')], ''),
    ('hicham', "Non, elle ne l'était pas, mais elle est venue seule à Paris.", 'No, she was not, but she came to Paris alone.', [(269, "Non, elle ne l'était pas, mais elle est venue seule à Paris,")], ''),
    ('hicham', "Elle s'y est fait une place sans révéler qui était son père.", 'She made a place for herself there without revealing who her father was.', [(270, "elle s'y est fait une place,"), (271, 'sans révéler qui était son père...')], ''),
    ('hicham', 'Serrer les dents, ne se confier à personne.', 'Gritting your teeth, confiding in no one.', [(272, 'Serrer les dents, ne se confier à personne,')], ''),
    ('hicham', "Ce sont les qualités qu'il faut dans ce métier.", 'Those are the qualities you need in this business.', [(274, "Ce sont les qualités qu'il faut dans ce métier.")], ''),
    ('hicham', 'Alors bienvenue, Camille, notre nouvelle agente.', 'So welcome, Camille, our new agent.', [(275, 'Alors bienvenue, Camille, notre nouvelle agente.')], ''),
    ('camille', 'Merci, je ferai de mon mieux.', 'Thank you, I will do my best.', [(276, 'Je vois.')], ''),
]
WALK = [
    (0, None, "'And now, what would you say to officially welcoming our new junior?' Opening with 'what would you say of' is a polished expression meaning 'how about...', followed by 'to welcome'."),
    (1, None, "'You should have consulted us beforehand.' French builds 'you should have' out of 'you would have owed', and bare 'before' at the end works like 'beforehand'."),
    (2, None, "'I consulted myself. And I decided.' Hicham doubles down in French: the opening already means 'I consulted myself', and tacking 'me-same' onto it stresses 'my very own self'."),
    (3, None, "'Our new junior happens to be female.' In French, Hicham keeps 'our new junior' in the default form up front so the reveal lands only on the final word."),
    (4, None, "'And her name is Camille Valentini.' Rather than saying 'her name is', French says 'she calls herself' before giving her first name and surname."),
    (5, None, "'What? Camille?' Saying that blunt single-word 'what?' in French shows pure shock — in calmer moments you'd say 'pardon?' instead."),
    (6, None, "'There were candidates who knew very well how to sell themselves.' Opening with 'it there had' gives 'there were', and 'knew to sell themselves' needs no 'how' in French."),
    (7, None, "'She did not talk, she acted.' Repeating 'she, she' at the start puts sharp contrast on Camille, and the closing action means 'took action' rather than stage acting in French."),
    (8, None, "'Camille, were you a candidate?' In front of the partners, Andrea addresses Camille with the formal 'you', and French drops 'a' before roles like 'candidate'."),
    (9, None, "'No, not at all.' Literally 'not of the all', this handy chunk is the quickest way in French to make a 'no' sound completely emphatic."),
    (10, None, "'No, she was not, but she came to Paris alone.' Where English stops at 'she wasn't', French tucks a placeholder 'it' before 'was' — literally 'she was not it'."),
    (11, None, "'She made a place for herself there without revealing who her father was.' A single-letter word meaning 'there' points back to Paris, and after 'without', French uses 'to reveal' rather than '-ing'."),
    (12, None, "'Gritting your teeth, confiding in no one.' Before body parts, French prefers 'the' over 'your' — so this idiom is literally 'clenching the teeth'."),
    (13, None, "'Those are the qualities you need in this business.' Rather than saying 'you need', French uses impersonal 'it takes', paired with a word meaning 'craft' or 'trade'."),
    (14, None, "'So welcome, Camille, our new agent.' Just like English 'welcome', the French greeting is built from 'well' plus 'come'."),
    (15, None, "'Thank you, I will do my best.' Notice the extra 'of' inside this handy expression: word-for-word, Camille promises 'I will do of my best'."),
]
