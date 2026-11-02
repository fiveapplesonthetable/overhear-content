ID = 'paquita-salas-s01e02-scene-10'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 10
TITLE = 'El antiguo tú  (The Former You)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'fernando': 'Fernando', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Window 00:09:02,920–00:09:56,560.'
INTRO = ("In the theatre audience, Paquita spots her former assistant Fernando Canelón and introduces him to Magüi as 'the former you'. "
         "She teases him for never calling and explains how he left PS Management to open his thriving agency, Red Carpet. "
         "Listen to the conversation first.")
OPENER = "Let's go through the reunion in the theatre line by line."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how changing an adjective's position shifts its meaning from 'old' to 'former', Spain's colourful words for being 'swamped' at work, and how 'to have cravings' expresses eagerness. See you next time.")
CLOSING = ('fernando', '¡Hasta luego!')

STORY = [
    ('paquita', 'Uy, mira, Fernando Canelón.',
     'Oh, look, Fernando Canelón.',
     [(191, 'Uy, mira'), (192, 'Fernando Canelón')],
     'Combined exclamation with full name across two cues.'),
    ('paquita', '¡Hombre! ¿Qué tal? ¿Cómo estás?',
     "Well, hello! How's it going? How are you?",
     [(196, '¡Hombre! ¿Qué tal?'), (197, '¿Cómo estás?')],
     'Joined warm double greeting across two cues.'),
    ('fernando', 'Muy bien, aquí, de caza.',
     'Very well, just here talent-scouting.',
     [(197, 'Muy bien, aquí'), (198, 'De caza')],
     'Joined reply and purpose across two cues.'),
    ('paquita', 'Mira, acércate. Magüi, este es Fernando.',
     'Look, come closer. Magüi, this is Fernando.',
     [(200, 'Mira, acércate. Magüi'), (200, 'Fernando'), (201, 'Este es')],
     'Added este es for clear A1 introduction.'),
    ('paquita', 'Este es el antiguo tú.',
     'This is the former you.',
     [(201, 'Este es el antiguo tú')],
     'Trimmed trailing greeting.'),
    ('magui', '¿Qué tal?',
     "How's it going?",
     [(201, '¿Qué tal?')], ''),
    ('fernando', 'Encantado.',
     'Pleased to meet you.',
     [(202, 'Encantado')],
     'Trimmed echoed phrase.'),
    ('paquita', 'No me llamas nunca.',
     'You never call me.',
     [(204, 'no me llamas nunca')],
     'Trimmed playful opening threat.'),
    ('fernando', 'Estamos muy liados, mucho jaleo en la oficina.',
     "We're really swamped, lots of chaos at the office.",
     [(206, 'Muy liados, mucho jaleo en la oficina')],
     'Added estamos and trimmed trailing tag.'),
    ('paquita', '¿Qué jaleo ni nada? Si te va genial.',
     'What chaos? Things are going great for you.',
     [(207, '¿Qué jaleo ni nada'), (208, 'Si te va genial')],
     'Trimmed por favor and joined across two cues.'),
    ('paquita', 'Cuando Fernando se fue, abrió su propia agencia, Red Carpet.',
     'When Fernando left, he opened his own agency, Red Carpet.',
     [(208, 'Fernando'), (208, 'cuando se fue'), (209, 'abrió su propia agencia, Red Carpet')],
     'Placed subject after cuando and omitted de la ofi.'),
    ('paquita', 'Lleva hasta a Amaia Salamanca.',
     'He even represents Amaia Salamanca.',
     [(211, 'Lleva hasta a Amaia Salamanca')], ''),
    ('fernando', 'Es muy trabajadora, con muchas ganas de hacer cosas.',
     "She's very hard-working, and really eager to do things.",
     [(213, 'Muy trabajadora'), (214, 'con muchas ganas de hacer cosas')],
     'Added es and trimmed confirmation tags.')
]

WALK = [
    (0, None, """'Oh, look, Fernando Canelón.' That quick opening exclamation catches a sudden surprise, followed by the casual command for "look". Funny enough, his surname literally means "cannelloni" in Spanish."""),
    (1, None, """'Well, hello! How's it going? How are you?' Shouting the term "man!" here works as a delighted "well, look who it is!". Stacking "what such?" right next to "how are you?" is how Spaniards greet an old friend warmly."""),
    (2, None, """'Very well, just here talent-scouting.' Literally "of hunt", that two-word chunk means out hunting — here, scouting fresh faces at a student showcase. Dropping "I am" keeps the answer breezy and natural."""),
    (3, None, """'Look, come closer. Magüi, this is Fernando.' The command for "come closer" tacks "yourself" onto the end as one brisk word. To introduce a man in Spanish, you use the masculine form of "this" rather than a neutral "this"."""),
    (4, None, """'This is the former you.' Placed after a word, the Spanish word "old" means antique, whereas placed before it means "former". Treating "you" like a role — "the former you" — is pure Paquita comedy."""),
    (5, None, """'How's it going?' Two short words serve as both "hi" and "how are things?" when meeting someone new. You'll hear it at every casual introduction in Spain."""),
    (6, None, """'Pleased to meet you.' Literally "enchanted" or "charmed", this single word is the standard polite reply on meeting someone. Because Fernando is a man, it ends in "-o"; a woman would say the "-a" form instead."""),
    (7, None, """'You never call me.' Spanish happily doubles the negative here: "no" before "you call me" and "never" at the end reinforce each other rather than cancelling out."""),
    (8, None, """'We're really swamped, lots of chaos at the office.' Literally "tied up" or "tangled", that first describing word is Spain's favourite everyday way to say "super busy". After it comes a lively colloquial word commotion or hustle."""),
    (9, None, """'What chaos? Things are going great for you.' Repeating someone's word with "what ... nor nothing?" brushes their excuse right aside. Starting the next sentence with "if" doesn't ask a question — it protests "why, things go great for you!"."""),
    (10, None, """'When Fernando left, he opened his own agency, Red Carpet.' Adding "himself" to "went" shifts the meaning from simply "went" to "left" or "walked away". Notice how "own" takes its feminine "-a" ending to match "agency"."""),
    (11, None, """'He even represents Amaia Salamanca.' Once again, the agency term meaning "carries" means "represents". Here "until" shifts its meaning to "even", sitting right beside the personal marker "a" before Amaia's name."""),
    (12, None, """'She's very hard-working, and really eager to do things.' Built on the root for "work", the feminine ending "-a" describes Amaia as hard-working. Literally "with many desires of to do things" is the natural Spanish chunk for being keen and motivated.""")
]
