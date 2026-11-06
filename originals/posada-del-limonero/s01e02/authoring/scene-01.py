# Authoring module for posada-del-limonero-s01e02-scene-01.
ID = 'posada-del-limonero-s01e02-scene-01'
SHOW = 'posada-del-limonero'
SEASON = 1
EPISODE = 2
SCENE = 1
TITLE = 'La cinta roja  (The Red Ribbon)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'clara': 'Clara', 'carmen': 'Carmen', 'mateo': 'Mateo'}
INTRO = 'Tuesday morning arrives bright and clear at the Lemon Tree Inn. Carmen hurries downstairs to the front desk, where Clara and Mateo have her returned suitcase waiting. Listen to the whole scene first.'
OPENER = "Let's go back through the conversation slowly, one line at a time."
TRANSITION = "Now let's hear the entire scene again at natural speed."
OUTRO = 'Carmen has her teacup and clothes back, and a twenty-five-year-old memory is starting to stir. Next, trouble brews in the breakfast kitchen. See you next time.'
CLOSING = ('carmen', '¡Hasta luego!')
STORY = [
    ('clara', '¡Buenos días, señora Carmen! Mire qué llegó anoche a nuestra puerta.', 'Good morning, Madam Carmen! Look what arrived at our gate last night.'),
    ('carmen', '¡Mi maleta! Voy a abrir el bolsillo de arriba... ¡sí, mi cinta roja!', 'My suitcase! I am going to open the top pocket... yes, my red ribbon!'),
    ('mateo', '¿Y su taza dentro? ¿Sigue entera?', 'And your cup inside? Is it still in one piece?'),
    ('carmen', '¡Ni una sola grieta! ¿Quién la trajo de vuelta?', 'Not a single crack! Who brought it back?'),
    ('clara', 'No lo sabemos. Alguien la dejó en el escalón y tocó el timbre.', 'We do not know. Someone left it on the step and rang the bell.'),
    ('carmen', '¿Y no pidió su propia maleta con el tren de madera?', 'And he did not ask for his own suitcase with the wooden train?'),
    ('mateo', 'Dejó una nota corta pidiendo guardarla hasta el viernes.', 'He left a short note asking us to keep it until Friday.'),
    ('carmen', '¡Qué curioso! La letra de esa etiqueta me resultaba muy familiar.', 'How curious! The handwriting on that tag felt very familiar to me.'),
    ('clara', '¿De verdad? ¿Conoce a alguien en Valencia?', 'Really? Do you know someone in Valencia?'),
    ('carmen', 'Hace veinticinco años di clases de piano cerca de aquí, pero los recuerdos se borran.', 'Twenty-five years ago I taught piano near here, though memories fade.'),
    ('mateo', 'De momento, su maleta sigue guardada bajo llave.', 'For now, his suitcase stays safe under lock and key.'),
    ('carmen', '¡Maravilloso! Ahora estoy lista para un gran desayuno.', 'Wonderful! Now I am ready for a big breakfast.'),
]
WALK = [
    (0, None, ["'Good morning, Madam Carmen! Look what arrived at our gate last night.' One compact word,", (None, 'anoche'), "covers all of 'last night'."]),
    (1, None, "'My suitcase! I am going to open the top pocket... yes, my red ribbon!' Notice 'pocket of above' where English says 'top pocket'."),
    (2, None, ["'And your cup inside? Is it still in one piece?' Pairing", (None, 'Sigue entera'), "literally asks 'does it continue whole?', a natural way to check if fragile china survived."]),
    (3, None, ["'Not a single crack! Who brought it back?' At the end,", (None, 'de vuelta'), "means 'back' or 'in return' after bringing or coming."]),
    (4, None, ["'We do not know. Someone left it on the step and rang the bell.' In Spanish you rarely just say 'we do not know'; you slip in 'it' and say", (None, 'No lo sabemos'), "literally 'we do not know it'."]),
    (5, None, "'And he did not ask for his own suitcase with the wooden train?' Placing 'own' right before 'suitcase' emphasises that it belonged to him."),
    (6, None, ["'He left a short note asking us to keep it until Friday.' Look at", (None, 'guardarla'), "where 'keep' and 'it' join into one smooth word."]),
    (7, None, ["'How curious! The handwriting on that tag felt very familiar to me.' One everyday word,", (None, 'La letra'), "means a letter of the alphabet, song lyrics, and a person's handwriting."]),
    (8, None, ["'Really? Do you know someone in Valencia?' Whenever 'know' or 'see' points to a person, Spanish inserts a tiny 'a' in", (None, 'Conoce a alguien'), 'marking the human being.']),
    (9, None, ["'Twenty-five years ago I taught piano near here, though memories fade.' Spanish puts 'ago' at the front:", (None, 'Hace veinticinco años'), "literally says 'it makes twenty-five years'."]),
    (10, None, ["'For now, his suitcase stays safe under lock and key.' Both", (None, 'De momento'), "for 'for now' and", (None, 'bajo llave'), "literally 'under key', are crisp everyday chunks."]),
    (11, None, ["'Wonderful! Now I am ready for a big breakfast.' Placed before 'breakfast', the shortened", (None, 'gran'), 'means grand or hearty.']),
]
