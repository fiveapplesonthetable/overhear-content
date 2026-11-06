# Authoring module for posada-del-limonero-s01e01-scene-05.
ID = 'posada-del-limonero-s01e01-scene-05'
SHOW = 'posada-del-limonero'
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = '¡No es mi ropa!  (Not My Clothes!)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'carmen': 'Carmen', 'clara': 'Clara', 'mateo': 'Mateo'}
INTRO = "Two minutes after going upstairs, Room 4's buzzer rings at the desk—not twice, but four times in a row. Clara hurries up to find Carmen and Mateo staring at the open suitcase on the stand. Listen first."
OPENER = "Let's replay each line and look at how the Spanish works."
TRANSITION = "Now let's hear the entire scene again at natural speed."
OUTRO = "Instead of dresses and sheet music, the blue suitcase holds big brown shoes and a wooden toy train. Let's see what is written on that tag next time."
CLOSING = ('clara', '¡Nos vemos!')
STORY = [
    ('clara', 'Señora Carmen, ¿va todo bien? ¡Ha tocado el timbre!', 'Madam Carmen, is everything alright? You rang the bell!'),
    ('carmen', '¡Mire dentro de esta maleta, Clara! ¡Esta no es mi maleta!', 'Look inside this suitcase, Clara! This is not my suitcase!'),
    ('clara', 'Espere, ¡es azul oscuro, igual que la suya!', 'Wait, it is dark blue, just like yours!'),
    ('carmen', '¡Por fuera es idéntica, sí! ¡Pero mire por dentro!', 'On the outside it is identical, yes! Yet look on the inside!'),
    ('mateo', 'Dos pares de zapatos marrones de hombre y jerséis grises.', "Two pairs of men's brown shoes and grey sweaters."),
    ('clara', '¿Y qué es esto envuelto en papel blanco? ¡Un trenecito de madera!', 'And what is this wrapped in white paper? A little wooden train!'),
    ('carmen', '¡Yo desde luego no uso la talla cuarenta y cuatro!', 'I certainly do not wear size forty-four!'),
    ('mateo', 'Con razón pesaba tanto. ¡Madera y cuero!', 'No wonder it weighed so much. Wood and leather!'),
    ('carmen', '¡Alguien en la estación se llevó mi maleta azul por error!', 'Someone at the station took my blue suitcase by mistake!'),
    ('clara', 'Siéntese, por favor, señora. No se preocupe, miramos la etiqueta ahora mismo.', 'Please sit down, madam. Do not worry, we will check the tag right now.'),
    ('mateo', 'Hay una pequeña tarjeta de cartón atada al asa.', 'There is a small cardboard card tied to the handle.'),
    ('carmen', '¡Ay, vamos a bajarla a la luz!', 'Oh, let us bring it downstairs into the light!'),
]
WALK = [
    (0, None, ["'Madam Carmen, is everything alright? You rang the bell!' Asking", (None, 'va todo bien'), "literally 'goes everything well?', is a natural check when someone calls for help."]),
    (1, None, ["'Look inside this suitcase, Clara! This is not my suitcase!' Carmen keeps the polite command", (None, 'Mire'), 'even in her shock.']),
    (2, None, ["'Wait, it is dark blue, just like yours!' When two colour words team up like", (None, 'azul oscuro'), "literally 'blue dark', they stay unchanged side by side."]),
    (3, None, ["'On the outside it is identical, yes! Yet look on the inside!' Pair", (None, 'Por fuera'), 'and', (None, 'por dentro'), 'whenever you contrast the outside of something with its inside.']),
    (4, None, ["'Two pairs of men's brown shoes and grey sweaters.' In Spain, a pullover sweater is called", (None, 'jerséis'), 'in the plural, borrowed long ago from English wool knitwear.']),
    (5, None, ["'And what is this wrapped in white paper? A little wooden train!' Adding a warm diminutive ending turns a regular train into", (None, 'Un trenecito'), 'a little toy train.']),
    (6, None, ["'I certainly do not wear size forty-four!' For clothing and shoe sizes, Spanish says", (None, 'uso la talla'), "literally 'I use the size', and forty-four is 'forty and four'."]),
    (7, None, ["'No wonder it weighed so much. Wood and leather!'", (None, 'Con razón'), "literally 'with reason', is the exact everyday idiom for 'no wonder!'."]),
    (8, None, ["'Someone at the station took my blue suitcase by mistake!' At the end,", (None, 'por error'), "gives a compact two-word chunk for 'by mistake'."]),
    (9, None, ["'Please sit down, madam. Do not worry, we will check the tag right now.' Listen to Clara's gentle", (None, 'Siéntese'), 'and', (None, 'No se preocupe'), 'two polite comforts every hospitality worker in Spain knows by heart.']),
    (10, None, ["'There is a small cardboard card tied to the handle.' Notice", (None, 'al asa'), "which uses the masculine form of 'the' right before a word starting with a stressed a sound, even though handles are feminine."]),
    (11, None, ["'Oh, let us bring it downstairs into the light!' Notice how", (None, 'bajarla'), "tucks 'it'—the feminine suitcase—straight onto the end of 'bring down'."]),
]
