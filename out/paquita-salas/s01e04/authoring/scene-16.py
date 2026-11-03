ID = 'paquita-salas-s01e04-scene-16'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 4
SCENE = 16
TITLE = 'Una tiene sus secretos  (A Woman Has Her Secrets)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paco': 'Paco', 'paquita': 'Paquita'}
SOURCE_NAME = 'Paquita Salas S01E04: Divacel'
SOURCE_FILE = 'sources/paquita-salas/s01/e04.es.srt'
SOURCE_NOTE = 'Native Spanish captions from episode stream. Scene window 00:15:18,440–00:15:47,440.'
INTRO = 'Out of options, Paquita pays a surprise visit to her ex-husband Paco Cerdeña at his production office. When her handbag spills open and reveals a popular romance novel, the two former spouses share a warm, teasing laugh about books before Paco invites her in. Listen to the Spanish first.'
OPENER = "Now let's go through it line by line with the English translation."
TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = "You heard Paco's surprised welcome, Paquita's playful line that a woman has her secrets, and her polite request to step into his office. See you next time."
CLOSING = ('paco', '¡Hasta pronto!')

STORY = [
    ('paco', 'Paquita, ¿qué haces tú aquí?', 'Paquita, what are you doing here?', [(349, 'Paquita, ¿qué haces tú aquí')], ''),
    ('paquita', 'Hola, Paco. De visita.', 'Hi, Paco. Just visiting.', [(350, 'Hola, Paco. De visita')], ''),
    ('paquita', 'Mira, mira.', 'Look, look.', [(352, 'mira, mira')], ''),
    ('paco', '¿Qué lees?', 'What are you reading?', [(353, 'Qué lees')], ''),
    ('paquita', 'Mira, las Cincuenta sombras.', 'Look, Fifty Shades.', [(353, 'Mira, las'), (353, 'Cincuenta sombras')], 'Removed subtitle quotes.'),
    ('paco', '¿De Grey?', 'Of Grey?', [(354, 'De Grey')], ''),
    ('paquita', 'Sí, de Grey. Que una tiene sus secretos.', 'Yes, of Grey. A woman has her secrets.', [(354, 'Sí, de Grey'), (355, 'Que una tiene sus secretos')], ''),
    ('paco', 'Ya. Esto está pasado de moda.', 'I see. This is out of fashion.', [(355, 'Ya'), (356, 'Esto está')], 'Replaced rare Gallicism demodé with pasado de moda.'),
    ('paco', 'Ahora hay que leer algo más intelectual, por ejemplo.', 'Nowadays one should read something more intellectual, for example.', [(357, 'Ahora hay que leer'), (358, 'por ejemplo'), (359, 'más intelectual')], ''),
    ('paquita', 'Excitante diría yo.', 'Exciting, I would say.', [(360, 'Excitante diría yo')], ''),
    ('paquita', '¿Puedo pasar?', 'May I come in?', [(361, 'Puedo pasar')], ''),
    ('paco', 'Pasa.', 'Come in.', [(362, 'Pasa')], ''),
]

WALK = [
    (0, None, "'Paquita, what are you doing here?'"),
    (1, None, "'Hi, Paco. Just visiting.'"),
    (2, None, "'Look, look.'"),
    (3, None, "'What are you reading?'"),
    (4, None, "'Look, Fifty Shades.'"),
    (5, None, "'Of Grey?'"),
    (6, None, "'Yes, of Grey. A woman has her secrets.'"),
    (7, None, "'I see. This is out of fashion.'"),
    (8, None, "'Nowadays one should read something more intellectual, for example.'"),
    (9, None, "'Exciting, I would say.'"),
    (10, None, "'May I come in?'"),
    (11, None, "'Come in.'"),
]
