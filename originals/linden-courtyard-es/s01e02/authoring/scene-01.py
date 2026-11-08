# Authoring module for linden-courtyard-es-s01e02-scene-01.
ID = 'linden-courtyard-es-s01e02-scene-01'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 2
SCENE = 1
TITLE = 'The Red Ribbon  (La cinta roja)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = 'La mañana del martes amanece clara y luminosa en Linden Courtyard Inn. Evelyn baja deprisa a la recepción, donde Hannah y Graham la esperan con su maleta recuperada. Escucha primero toda la escena en inglés.'
OPENER = 'Ahora repasemos la conversación paso a paso.'
TRANSITION = 'Volvamos a escuchar toda la escena seguida.'
OUTRO = 'Evelyn ya recuperó su taza y su ropa, y un recuerdo de hace veinticinco años empieza a despertarse. Muy pronto habrá revuelo en la cocina del desayuno. Hasta la próxima.'
CLOSING = ('evelyn', 'See you soon!')
STORY = [
    ('hannah', 'Good morning, Miss Evelyn! Look what arrived at our gate last night.', '¡Buenos días, señorita Evelyn! Mire lo que llegó anoche a nuestra entrada.'),
    ('evelyn', 'My suitcase! Let me open the top pocket... yes, my red ribbon!', '¡Mi maleta! Déjeme abrir el bolsillo superior... ¡sí, mi cinta roja!'),
    ('graham', 'And your teacup inside? Is it still in one piece?', '¿Y su taza de té adentro? ¿Sigue entera?'),
    ('evelyn', 'Not a single crack! Who brought it back?', '¡Ni una sola grieta! ¿Quién la trajo de vuelta?'),
    ('hannah', 'We do not know. Someone left it on the step and rang the bell.', 'No lo sabemos. Alguien la dejó en el escalón y tocó el timbre.'),
    ('evelyn', 'And he did not ask for his own suitcase with the wooden train?', '¿Y no preguntó por su propia maleta con el tren de madera?'),
    ('graham', 'He left a short note asking us to keep it until Friday.', 'Dejó una nota corta pidiéndonos que la guardemos hasta el viernes.'),
    ('evelyn', 'How curious! The handwriting on that tag felt oddly familiar to me.', '¡Qué curioso! La letra de esa etiqueta me resultó extrañamente familiar.'),
    ('hannah', 'Really? Do you know someone in Portland?', '¿De verdad? ¿Conoce a alguien en Portland?'),
    ('evelyn', 'Twenty-five years ago I taught piano near here, though memories fade.', 'Hace veinticinco años di clases de piano cerca de aquí, aunque los recuerdos se desvanecen.'),
    ('graham', 'For now, his bag stays safe under lock and key.', 'Por ahora, su maleta se queda segura bajo llave.'),
    ('evelyn', 'Wonderful! Now I am ready for a big breakfast.', '¡Estupendo! Ahora estoy lista para un buen desayuno.'),
]
WALK = [
    (0, None, ["'¡Buenos días, señorita Evelyn! Mire lo que llegó anoche a nuestra entrada.' Mientras decimos 'buenas noches' en plural, 'anoche' en inglés se dice", (None, 'last night'), "literalmente 'la noche pasada'."]),
    (1, None, ["'¡Mi maleta! Déjeme abrir el bolsillo superior... ¡sí, mi cinta roja!' Con", (None, 'Let me open'), 'pides permiso o anuncias lo que vas a hacer, llevando el verbo siguiente directo sin preposición.']),
    (2, None, ["'¿Y su taza de té adentro? ¿Sigue entera?' La expresión", (None, 'in one piece'), "significa literalmente 'en una sola pieza', ideal para algo frágil que no se rompió."]),
    (3, None, ["'¡Ni una sola grieta! ¿Quién la trajo de vuelta?' Cuando 'quién' es el sujeto que realiza la acción,", (None, 'Who brought it back'), 'no necesita verbo auxiliar en la pregunta.']),
    (4, None, ["'No lo sabemos. Alguien la dejó en el escalón y tocó el timbre.' En presente negativo,", (None, 'We do not know'), "basta por sí solo sin añadir un 'lo' equivalente al español."]),
    (5, None, ["'¿Y no preguntó por su propia maleta con el tren de madera?' Para pedir o reclamar un objeto en inglés se enlaza verbo y preposición en", (None, 'ask for'), 'seguido de lo que buscas.']),
    (6, None, ["'Dejó una nota corta pidiéndonos que la guardemos hasta el viernes.' El giro", (None, 'asking us to keep'), "une a la persona con un infinitivo directo, sin usar cláusula con 'que'."]),
    (7, None, ["'¡Qué curioso! La letra de esa etiqueta me resultó extrañamente familiar.' La escritura a mano tiene su propia palabra compuesta:", (None, 'handwriting'), "formada por 'mano' y 'escritura'."]),
    (8, None, ["'¿De verdad? ¿Conoce a alguien en Portland?' En inglés no existe la 'a' personal delante de personas: dices directo", (None, 'know someone'), 'sin preposición intermedia.']),
    (9, None, ["'Hace veinticinco años di clases de piano cerca de aquí, aunque los recuerdos se desvanecen.' Para situar tiempo atrás, la palabra", (None, 'ago'), 'se coloca al final en', (None, 'Twenty-five years ago'), 'seguida del pasado irregular', (None, 'taught'), 'enseñé.']),
    (10, None, ["'Por ahora, su maleta se queda segura bajo llave.' El modismo clásico", (None, 'under lock and key'), "une candado y llave para decir 'a buen recaudo'."]),
    (11, None, ["'¡Estupendo! Ahora estoy lista para un buen desayuno.' La estructura", (None, 'ready for'), "conecta 'listo' con cualquier sustantivo que venga detrás."]),
]
