ID = 'paquita-salas-s01e04-scene-04'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 4
SCENE = 4
TITLE = 'Rellenar una fichita  (Filling In a Profile Form)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'mariona': 'Mariona', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E04: Divacel'
SOURCE_FILE = 'sources/paquita-salas/s01/e04.es.srt'
SOURCE_NOTE = 'Native Spanish captions from episode stream. Scene window 00:03:20,920–00:04:11,040.'
INTRO = "Back at the PS Management office, Paquita wraps up a quick call to actor David about his Hyundai commercial and turns to Mariona's agency profile form. With Magüi taking notes, they go through Mariona's age, driving licence, languages, eye colour, and height. Listen to the Spanish first."
OPENER = "Now let's go through it line by line with the English translation."
TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'You heard practical interview questions for filling out a personal profile, from driving licences and languages to eye colour and height. See you next time.'
CLOSING = ('magui', '¡Hasta luego!')

STORY = [
    ('paquita', 'A ver, David, lo de Hyundai se ha caído.', "Let's see, David, the Hyundai job fell through.", [(56, 'A ver, David, lo de Hyundai se ha caído')], ''),
    ('paquita', 'A ver, cariño, tenemos que rellenar una fichita.', 'Right, darling, we need to fill in a little profile form.', [(58, 'A ver cariño, tenemos que rellenar una fichita')], ''),
    ('mariona', 'Vale. Nombre, Mariona Terés.', 'Okay. Name, Mariona Terés.', [(59, 'Vale. Nombre')], 'Used correct character name.'),
    ('paquita', '¿Edad?', 'Age?', [(61, 'Edad')], ''),
    ('mariona', 'Veintiséis.', 'Twenty-six.', [(61, '26')], 'Written out in words.'),
    ('paquita', '¿Carné de conducir?', 'Driving licence?', [(63, 'Carné de conducir')], ''),
    ('mariona', 'No.', 'No.', [(64, 'No')], ''),
    ('paquita', '¿Nada? ¿Moto?', 'Nothing at all? A motorbike?', [(64, 'Nada'), (65, 'Moto')], ''),
    ('paquita', '¿Idiomas?', 'Languages?', [(66, 'Idiomas')], ''),
    ('mariona', 'Catalán, castellano, inglés también. Un poquito.', 'Catalan, Spanish, and English too. A little bit.', [(67, 'Catalán'), (68, 'Castellano, inglés también. Un poquito')], ''),
    ('magui', 'Inglés medio. ¿Instrumentos musicales, por ejemplo?', 'Intermediate English. Musical instruments, for example?', [(69, 'Inglés medio'), (76, 'Instrumentos musicales, por ejemplo')], ''),
    ('mariona', 'No.', 'No.', [(77, 'No')], ''),
    ('magui', '¿Color de ojos?', 'Eye colour?', [(78, 'Color de ojos')], ''),
    ('mariona', 'Marrón. Y altura, uno sesenta.', 'Brown. And height, one metre sixty.', [(78, 'Marrón'), (79, 'Altura'), (80, '1,60')], 'Spoken number written out.'),
]

WALK = [
    (0, None, "'Let's see, David, the Hyundai job fell through.'"),
    (1, None, "'Right, darling, we need to fill in a little profile form.'"),
    (2, None, "'Okay. Name, Mariona Terés.'"),
    (3, None, "'Age?'"),
    (4, None, "'Twenty-six.'"),
    (5, None, "'Driving licence?'"),
    (6, None, "'No.'"),
    (7, None, "'Nothing at all? A motorbike?'"),
    (8, None, "'Languages?'"),
    (9, None, "'Catalan, Spanish, and English too. A little bit.'"),
    (10, None, "'Intermediate English. Musical instruments, for example?'"),
    (11, None, "'No.'"),
    (12, None, "'Eye colour?'"),
    (13, None, "'Brown. And height, one metre sixty.'"),
]
