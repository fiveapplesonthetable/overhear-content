# Authoring module for linden-courtyard-es-s01e04-scene-02.
ID = 'linden-courtyard-es-s01e04-scene-02'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = 'The Blue Door  (La puerta azul)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Diez minutos después, Hannah ya ha cruzado el puente sobre el río en Portland, pero detrás de la farmacia se abren dos callejuelas distintas. Llama a Graham desde una fuente de piedra. Escuchemos primero.'
OPENER = 'Repasemos cada frase del diálogo telefónico con calma.'
TRANSITION = 'Volvamos a escuchar la escena entera a ritmo natural.'
OUTRO = 'Dos válvulas nuevas en el bolsillo y pasos tempraneros sonando ya en la escalera. En la próxima escena, Tessa y Arthur intentan entretener a todo el mundo en el desayuno. Hasta pronto.'
CLOSING = ('graham', 'Bye for now!')
STORY = [
    ('hannah', 'Graham, can you hear me? I just passed the green pharmacy!', 'Graham, ¿me oyes? ¡Acabo de pasar la farmacia verde!'),
    ('graham', 'Loud and clear. Are you standing by the little stone fountain?', 'Alto y claro. ¿Estás parada junto a la pequeña fuente de piedra?'),
    ('hannah', 'Yes! There are two small streets on the left. Which one do I take?', '¡Sí! Hay dos calles pequeñas a la izquierda. ¿Cuál tomo?'),
    ('graham', 'Take the second street, beside the flower stand, not the narrow alley.', 'Toma la segunda calle, al lado del puesto de flores, no el callejón estrecho.'),
    ('hannah', 'Walking now... oh, I see the golden key sign and the blue door!', 'Caminando ahora... ¡oh, ya veo el letrero de la llave dorada y la puerta azul!'),
    ('graham', 'Good! Is the shutter open?', '¡Bien! ¿Está abierta la persiana metálica?'),
    ('hannah', 'He is unlocking it right now! Stay on the phone one second.', '¡La está abriendo con llave ahora mismo! Quédate al teléfono un segundo.'),
    ('graham', 'Make sure the brass ring inside is twenty millimeters wide.', 'Asegúrate de que el anillo de latón de dentro tenga veinte milímetros de ancho.'),
    ('hannah', 'He matched it against the old one. He has two left on the shelf!', 'La comparó con la vieja. ¡Le quedan dos en el estante!'),
    ('graham', 'Buy both! A spare valve saves next winter too.', '¡Compra las dos! Una válvula de repuesto salva también el próximo invierno.'),
    ('hannah', 'Paid in cash! Keep your toolbox open, I am running back across the bridge!', '¡Pagado en efectivo! ¡Deja abierta tu caja de herramientas, vuelvo corriendo por el puente!'),
    ('graham', 'Hurry, I just heard footsteps on the second floor stairs!', '¡Date prisa, acabo de oír pasos en la escalera del segundo piso!'),
]
WALK = [
    (0, None, ["'Graham, ¿me oyes? ¡Acabo de pasar la farmacia verde!' Al hablar por teléfono el inglés pregunta con capacidad:", (None, 'can you hear me'), "literalmente '¿puedes oírme?'."]),
    (1, None, ["'Alto y claro. ¿Estás parada junto a la pequeña fuente de piedra?' La respuesta clásica para buena señal telefónica es", (None, 'Loud and clear'), 'fuerte y claro.']),
    (2, None, ["'¡Sí! Hay dos calles pequeñas a la izquierda. ¿Cuál tomo?' Cuando eliges entre pocas opciones visibles, usas", (None, 'Which one'), "evitando repetir la palabra 'calle'."]),
    (3, None, ["'Toma la segunda calle, al lado del puesto de flores, no el callejón estrecho.' En", (None, 'flower stand'), 'vemos el nombre habitual en Estados Unidos para un puesto callejero de flores.']),
    (4, None, ["'Caminando ahora... ¡oh, ya veo el letrero de la llave dorada y la puerta azul!' Con verbos de percepción inmediata basta el presente simple:", (None, 'I see'), 'ya veo.']),
    (5, None, ["'¡Bien! ¿Está abierta la persiana metálica?' La palabra", (None, 'shutter'), 'sirve tanto para los postigos de madera de las ventanas como para el cierre enrollable de una tienda.']),
    (6, None, ["'¡La está abriendo con llave ahora mismo! Quédate al teléfono un segundo.' Para pedir que no cuelguen se dice siempre", (None, 'Stay on the phone'), "con la preposición 'on'."]),
    (7, None, ["'Asegúrate de que el anillo de latón de dentro tenga veinte milímetros de ancho.' Con medidas ponemos el adjetivo al final:", (None, 'twenty millimeters wide'), 'veinte milímetros de ancho.']),
    (8, None, ["'La comparó con la vieja. ¡Le quedan dos en el estante!' Observa qué útil es", (None, 'two left'), "donde 'left' después de una cantidad significa 'que quedan disponibles'."]),
    (9, None, ["'¡Compra las dos! Una válvula de repuesto salva también el próximo invierno.' Para referirte a dos cosas juntas basta decir", (None, 'Buy both'), 'sin añadir artículo.']),
    (10, None, ["'¡Pagado en efectivo! ¡Deja abierta tu caja de herramientas, vuelvo corriendo por el puente!' En compras diarias recuerda", (None, 'in cash'), 'para pagar en efectivo, con billetes o monedas.']),
    (11, None, ["'¡Date prisa, acabo de oír pasos en la escalera del segundo piso!' Un solo verbo,", (None, 'Hurry'), "equivale por sí mismo a '¡date prisa!' o '¡apúrate!'."]),
]
