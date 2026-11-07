# Authoring module for posada-del-limonero-s02e01-scene-01.
ID = 'posada-del-limonero-s02e01-scene-01'
SHOW = 'posada-del-limonero'
SEASON = 2
EPISODE = 1
SCENE = 1
TITLE = 'La novena llave  (The Ninth Key)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'clara': 'Clara', 'mateo': 'Mateo', 'ernesto': 'Ernesto'}
INTRO = "It is early Saturday morning at the Lemon Tree Inn in Valencia, just hours after Mateo carried a dusty cedar box stamped 'Room 9' up from the cellar. Clara and Ernesto lean over the front desk as Mateo turns the tiny brass key. Listen to the scene first."
OPENER = "Let's go back through the conversation slowly, one line at a time."
TRANSITION = "Now let's hear the entire scene again at natural speed."
OUTRO = "Inside the cedar box sits a heavy door key and a floor plan pointing straight behind the hallway bookcase. Don't worry if a word or two went past quickly; they return right away. See you next time."
CLOSING = ('clara', '¡Hasta luego!')
STORY = [
    ('ernesto', 'Gira la llave pequeña despacio, Mateo. ¡Mi corazón va muy rápido!', 'Turn the small key slowly, Mateo. My heart is beating fast!'),
    ('mateo', 'Tranquilo, jefe. Una cerradura de latón del sótano nunca se rompe.', 'Relax, boss. A brass lock from the cellar never breaks.'),
    ('clara', '¡Ha hecho clic! ¡Levanta la tapa de madera, Mateo!', 'It clicked! Lift the wooden lid, Mateo!'),
    ('mateo', 'Dentro hay una llave grande, un plano azul y unas postales.', 'Inside there is one big key, a blue plan and some postcards.'),
    ('ernesto', '¡Lee lo que pone arriba en el papel azul! ¿Dónde están mis gafas?', 'Read what it says at the top of the blue paper! Where are my glasses?'),
    ('clara', 'Siguen en su frente, Ernesto, donde las dejó anoche.', 'Still on your forehead, Ernesto, right where you left them last night.'),
    ('ernesto', '¡Ajá! Mirad: planta baja, habitación nueve, galería del jardín.', 'Aha! Look: ground floor, Room Nine, garden sunroom.'),
    ('clara', 'Un momento, ¿tenemos una galería en la planta baja?', 'Wait a moment, we have a sunroom on the ground floor?'),
    ('mateo', 'Mirad la flecha: está detrás de la librería del pasillo.', 'Look at the arrow: it is behind the hallway bookcase.'),
    ('ernesto', '¡Esa librería de madera está contra la pared desde hace veinte años!', 'That wooden bookcase has stood against the wall for twenty years!'),
    ('clara', 'Entonces, detrás de esos libros viejos, ¡hay una novena puerta!', 'Then behind those old books, there is a ninth door!'),
    ('mateo', 'Primero, un sorbo de café. Después, movemos los libros.', 'First, a sip of coffee. Then we move the books.'),
]
WALK = [
    (0, None, ["'Turn the small key slowly, Mateo. My heart is beating fast!' The word for 'slowly' is", (None, 'despacio'), 'and anxious owners like to say it twice for extra care.']),
    (1, None, ["'Relax, boss. A brass lock from the cellar never breaks.' Staff in Spain often call the owner", (None, 'jefe'), "which means 'boss' and sounds friendly rather than stiff."]),
    (2, None, ["'It clicked! Lift the wooden lid, Mateo!' Spanish borrows the sound itself here:", (None, 'Ha hecho clic'), "is literally 'it has made click'."]),
    (3, None, ["'Inside there is one big key, a blue plan and some postcards.' One tiny word,", (None, 'hay'), "covers both 'there is' and 'there are', so the whole list fits after it."]),
    (4, None, ["'Read what it says at the top of the blue paper! Where are my glasses?' To ask what a paper says, people in Spain use the word for 'puts':", (None, 'lo que pone'), "is literally 'what it puts'."]),
    (5, None, ["'Still on your forehead, Ernesto, right where you left them last night.' Clara keeps the respectful 'your' for her boss, so", (None, 'su frente'), "is the polite way to say 'your forehead'."]),
    (6, None, ["'Aha! Look: ground floor, Room Nine, garden sunroom.' He talks to the whole team at once, so he picks", (None, 'Mirad'), "the friendly plural 'look' that you hear all over Spain."]),
    (7, None, ["'Wait a moment, we have a sunroom on the ground floor?' The ground floor is", (None, 'la planta baja'), "literally 'the low floor', the level where guests walk in."]),
    (8, None, ["'Look at the arrow: it is behind the hallway bookcase.' In Spain", (None, 'la librería'), 'can be a bookcase at home as well as a bookshop on the street.']),
    (9, None, ["'That wooden bookcase has stood against the wall for twenty years!' Spanish counts time up to now with", (None, 'desde hace veinte años'), 'and keeps the verb in the present: it still stands there.']),
    (10, None, ["'Then behind those old books, there is a ninth door!' Ninth is", (None, 'novena'), 'and it ends in a to match the word for door.']),
    (11, None, ["'First, a sip of coffee. Then we move the books.' A small mouthful of a drink is", (None, 'un sorbo'), 'and Mateo never skips one before heavy lifting.']),
]
