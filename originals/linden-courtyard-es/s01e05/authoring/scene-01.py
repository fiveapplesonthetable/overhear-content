# Authoring module for linden-courtyard-es-s01e05-scene-01.
ID = 'linden-courtyard-es-s01e05-scene-01'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'Truth in the Courtyard  (La verdad en el patio)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'evelyn': 'Evelyn'}
INTRO = 'Todavía bajo el árbol del patio en la posada Linden Courtyard Inn, en Portland, Caleb se sienta con Hannah y la señorita Evelyn para contar desde el principio el misterio del lunes por la noche. Escucha primero toda la escena.'
OPENER = 'Ahora repasemos la conversación con calma, frase por frase.'
TRANSITION = 'Escuchemos otra vez toda la escena a velocidad natural.'
OUTRO = 'Todas las piezas del lunes y del martes encajan por fin. En la próxima escena, Caleb explica por qué lleva tres años sin hablar con su hermano Owen. Hasta la próxima.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('evelyn', 'Let me look at you properly, Caleb! You grew taller than the piano!', '¡Déjame mirarte bien, Caleb! ¡Creciste más alto que el piano!'),
    ('caleb', 'I cannot believe you are staying in the exact same guesthouse, Miss Evelyn.', 'No puedo creer que se aloje exactamente en la misma posada, señorita Evelyn.'),
    ('hannah', 'Wait, so we rode the same train on Monday, and you took her suitcase?', 'Espere, ¿así que viajamos en el mismo tren el lunes y usted se llevó la maleta de ella?'),
    ('caleb', "By complete accident! At my cousin's apartment I opened it and saw sheet music and a red ribbon.", '¡Por puro accidente! En el apartamento de mi primo la abrí y vi partituras y una cinta roja.'),
    ('evelyn', 'Why did you leave my bag on the step at night and run away?', '¿Por qué dejó mi maleta en el escalón de noche y salió corriendo?'),
    ('caleb', 'Because when I walked here on Monday evening, I saw my older brother walking down this street!', '¡Porque cuando caminé hacia aquí el lunes por la tarde, vi a mi hermano mayor bajando por esta calle!'),
    ('hannah', 'Your older brother lives here in Portland?', '¿Su hermano mayor vive aquí en Portland?'),
    ('caleb', 'Yes. I panicked, rang your bell, and slipped the Friday note onto the handle.', 'Sí. Entré en pánico, toqué su timbre y deslicé la nota del viernes en el asa.'),
    ('evelyn', 'Wait, and Wednesday night you checked in here under your real name?', 'Espere, ¿y el miércoles por la noche se registró aquí con su nombre verdadero?'),
    ('caleb', 'I needed a quiet place nearby before Friday, and honestly forgot you still had my bag!', '¡Necesitaba un lugar tranquilo cerca antes del viernes, y sinceramente olvidé que aún tenían mi maleta!'),
    ('hannah', 'Until you called us on Tuesday asking us not to open the white package!', '¡Hasta que nos llamó el martes pidiéndonos que no abriéramos el paquete blanco!'),
    ('caleb', 'Everything in that white paper belongs to my brother Owen, not me.', 'Todo lo que hay en ese papel blanco pertenece a mi hermano Owen, no a mí.'),
]
WALK = [
    (0, None, ["'¡Déjame mirarte bien, Caleb! ¡Creciste más alto que el piano!' Para comparar estatura añadimos '-er' al adjetivo seguido de 'than':", (None, 'taller than the piano'), 'más alto que el piano.']),
    (1, None, ["'No puedo creer que se aloje exactamente en la misma posada, señorita Evelyn.' Para expresar incredulidad alegre, el inglés une", (None, 'I cannot believe'), 'directamente con la frase siguiente.']),
    (2, None, ["'Espere, ¿así que viajamos en el mismo tren el lunes y usted se llevó la maleta de ella?' Con medios de transporte públicos como el tren, el verbo clásico en inglés americano es", (None, 'rode the same train'), 'viajamos en el mismo tren.']),
    (3, None, ["'¡Por puro accidente! En el apartamento de mi primo la abrí y vi partituras y una cinta roja.' El bloque", (None, 'By complete accident'), 'explica que algo ocurrió sin ninguna intención.']),
    (4, None, ["'¿Por qué dejó mi maleta en el escalón de noche y salió corriendo?' Con el auxiliar 'did' al inicio, ambos verbos quedan en forma base:", (None, 'leave'), 'y', (None, 'run away'), 'salir huyendo.']),
    (5, None, ["'¡Porque cuando caminé hacia aquí el lunes por la tarde, vi a mi hermano mayor bajando por esta calle!' Tras verbos de vista como 'saw', usar '-ing' en", (None, 'walking down this street'), 'muestra la acción en pleno movimiento.']),
    (6, None, ["'¿Su hermano mayor vive aquí en Portland?' A veces una pregunta de sorpresa mantiene el orden afirmativo,", (None, 'lives here in Portland'), 'subiendo solo la entonación final.']),
    (7, None, ["'Sí. Entré en pánico, toqué su timbre y deslicé la nota del viernes en el asa.' Tres pasados seguidos dan ritmo al relato, cerrando con", (None, 'onto the handle'), 'sobre el asa.']),
    (8, None, ["'Espere, ¿y el miércoles por la noche se registró aquí con su nombre verdadero?' En hoteles siempre te registras con el verbo compuesto", (None, 'checked in'), 'y para la identidad se dice', (None, 'under your real name'), 'bajo tu nombre real.']),
    (9, None, ["'¡Necesitaba un lugar tranquilo cerca antes del viernes, y sinceramente olvidé que aún tenían mi maleta!' El adverbio", (None, 'nearby'), "significa 'cerca de aquí' sin requerir ninguna preposición."]),
    (10, None, ["'¡Hasta que nos llamó el martes pidiéndonos que no abriéramos el paquete blanco!' Observa dónde va la negación en peticiones indirectas:", (None, 'not to open'), "siempre delante de 'to'."]),
    (11, None, ["'Todo lo que hay en ese papel blanco pertenece a mi hermano Owen, no a mí.' El verbo de pertenencia lleva preposición fija:", (None, 'belongs to my brother'), 'pertenece a mi hermano.']),
]
