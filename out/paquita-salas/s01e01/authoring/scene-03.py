ID = 'paquita-salas-s01e01-scene-03'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = 'Gente que quiere trabajar  (People Who Want to Work)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'lidia': 'Lidia', 'paquita': 'Paquita'}
SOURCE_NAME = 'Paquita Salas S01E01: Casada con esto'
SOURCE_FILE = 'sources/paquita-salas/s01/e01.es.srt'
SOURCE_NOTE = 'Window 00:02:44,280–00:03:51,200.'
INTRO = ("Lidia lists her recent acting credits, from shooting a film in China to thirty guest spots on the television quiz show Pasapalabra. "
         "Paquita then explains why she only wants clients who jump at every role, recalling an actress who turned down the hit daily drama Puente Viejo. "
         "Listen to the Spanish first.")
OPENER = "Let's walk through what Lidia and Paquita say."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how Spanish expresses eagerness as 'having lots of desires', and how Paquita talks about roles, storylines, and seizing an opportunity. See you next time.")
CLOSING = ('lidia', '¡Nos vemos!')

STORY = [
    ('paquita', '¿Y qué más?',
     'And what else?',
     [(64, '¿Y qué más?')], ''),
    ('lidia', 'Rodé una película en China.',
     'I shot a film in China.',
     [(66, 'Rodé una película en China')], ''),
    ('lidia', 'Sí, teatro y microteatro. He hecho más.',
     "Yes, theatre and micro-theatre. I've done more.",
     [(69, 'Sí, teatro y microteatro'), (70, 'He hecho más')], ''),
    ('paquita', 'Los diez Pasapalabra.',
     'The ten Pasapalabra episodes.',
     [(71, 'Los diez'), (71, 'Pasapalabra')], ''),
    ('lidia', 'Treinta.',
     'Thirty.',
     [(71, '30')],
     'Spelled out numeral 30.'),
    ('paquita', '¿Treinta? Madre mía, Lidi.',
     'Thirty? Goodness me, Lidi.',
     [(72, 'Madre mía, Lidi')],
     'Spelled out numeral 30.'),
    ('paquita', 'Representamos a gente con mucho talento y muchas ganas.',
     'We represent people with a lot of talent and enthusiasm.',
     [(73, 'Representamos a gente'), (74, 'con mucho talento'), (74, 'muchas ganas')],
     'Combined the two parallel phrases about clients.'),
    ('paquita', 'Gente que quiere trabajar. Eso es muy importante.',
     "People who want to work. That's very important.",
     [(75, 'Gente que quiere trabajar. Eso es muy importante')], ''),
    ('paquita', 'Hay mucha gente que no quiere trabajar en realidad.',
     "There are lots of people who don't actually want to work.",
     [(76, 'hay mucha gente que no quiere trabajar en realidad')],
     'Removed leading conjunction porque so the sentence stands cleanly.'),
    ('paquita', 'Le ofrecieron un papel precioso en Puente Viejo.',
     'They offered her a lovely part in Puente Viejo.',
     [(79, 'Le ofrecieron un papel precioso en'), (79, 'Puente Viejo')], ''),
    ('paquita', 'Un papel de enfermera. Tenía una trama increíble.',
     'A nurse role. She had an incredible storyline.',
     [(80, 'Un papel de enfermera'), (80, 'Tenía una trama increíble')], ''),
    ('paquita', 'No lo quería hacer porque para ella Puente Viejo era poco.',
     "She didn't want to do it because Puente Viejo wasn't big enough for her.",
     [(81, 'no lo quería hacer'), (82, 'porque para ella'), (82, 'Puente Viejo'), (82, 'era poco')], ''),
    ('paquita', '¿Para ti Puente Viejo es poco? Esto es un trabajo.',
     "Puente Viejo isn't enough for you? This is a job.",
     [(83, 'Para ti'), (83, 'Puente Viejo'), (83, 'poco? Esto es un trabajo')],
     'Added es for natural beginner clarity.'),
    ('paquita', 'Te llamaron de Puente Viejo. Aprovecha esa oportunidad.',
     'Puente Viejo called you. Take that opportunity.',
     [(85, 'Te llamaron de'), (85, 'Puente Viejo'), (85, 'Aprovecha esa oportunidad')], '')
]

WALK = [
    (0, None, "'And what else?' Literally, and what more, using the everyday word for more where English reaches for else. You can ask this three-word question in shops, interviews, or chats."),
    (1, None, "'I shot a film in China.' The first word comes from the action word for rolling camera reels, so in cinema it means shoot or film. Notice the feminine word for a before film."),
    (2, None, "'Yes, theatre and micro-theatre. I've done more.' Adding the prefix for micro onto the word for theatre names short fifteen-minute plays performed for tiny audiences in Madrid. Then I have plus the irregular form for done means I've done."),
    (3, None, "'The ten Pasapalabra episodes.' Using the masculine plural word for the right before ten turns the show's title into ten appearances on Pasapalabra without needing a word for episodes."),
    (4, None, "'Thirty.' Lidia corrects ten to thirty in a single word. Unlike twenty-five, which joins into one word, numbers in the thirties add the little word for and if you keep counting past thirty."),
    (5, None, "'Thirty? Goodness me, Lidi.' Literally, mother of mine, a warm, harmless exclamation you'll hear constantly in Spain for surprise or disbelief. Lidi is Paquita's affectionate short name for Lidia."),
    (6, None, "'We represent people with a lot of talent and enthusiasm.' Notice how the word for a lot changes its ending: masculine singular before talent, then feminine plural before the word for desires or keenness, which is how Spanish says enthusiasm."),
    (7, None, "'People who want to work. That's very important.' Because the word for people is grammatically singular, wants stays singular too. In the second sentence, that uses the neuter form because it points to the whole idea."),
    (8, None, "'There are lots of people who don't actually want to work.' One short three-letter word at the front covers both there is and there are, never changing for singular or plural. At the end, in reality means actually."),
    (9, None, "'They offered her a lovely part in Puente Viejo.' The word for paper also means an acting part or role, since actors used to receive their lines on a roll of paper. Lovely comes after the word it describes."),
    (10, None, "'A nurse role. She had an incredible storyline.' Literally, a role of nurse, with no word for a before nurse. The word for plot or storyline originally meant the weave of threads in cloth."),
    (11, None, "'She didn't want to do it because Puente Viejo wasn't big enough for her.' Notice how the little word for it sits in front of wanted rather than after to do, though tacking it onto do would also work in Spanish."),
    (12, None, "'Puente Viejo isn't enough for you? This is a job.' After the word for, casual you uses its special form rather than the subject form. Calling something little here means beneath you or not prestigious enough."),
    (13, None, "'Puente Viejo called you. Take that opportunity.' Literally, they called you from Puente Viejo. Then Paquita uses a direct casual command meaning make the most of or seize that opportunity.")
]
