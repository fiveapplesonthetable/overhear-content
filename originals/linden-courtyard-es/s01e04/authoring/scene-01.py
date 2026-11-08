# Authoring module for linden-courtyard-es-s01e04-scene-01.
ID = 'linden-courtyard-es-s01e04-scene-01'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = 'Six Forty-Five  (Las seis y cuarenta y cinco)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah'}
INTRO = 'Son las seis y cuarenta y cinco de la mañana en la posada Linden Courtyard Inn, en Portland. Mientras los huéspedes siguen durmiendo arriba, Graham dibuja en papel un mapa rápido de las calles para Hannah. Escucha primero toda la escena en inglés.'
OPENER = 'Ahora repasemos la conversación con calma, frase por frase.'
TRANSITION = 'Escuchemos otra vez toda la escena a velocidad natural.'
OUTRO = 'A la izquierda al salir de la verja, cruzar el puente, pasar la farmacia verde y girar hacia la plaza: Hannah ya está en marcha. Hasta la próxima.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Good morning, Graham! Are the showers upstairs really cold already?', '¡Buenos días, Graham! ¿Las duchas de arriba de verdad están frías ya?'),
    ('graham', 'Cold as river water. Take this broken brass valve in your coat pocket.', 'Frías como agua de río. Lleva esta válvula rota de latón en el bolsillo del abrigo.'),
    ('hannah', 'Got it. Now tell me how to find the hardware shop.', 'Entendido. Ahora dime cómo encontrar la ferretería.'),
    ('graham', 'Turn left outside our gate and walk straight to the stone bridge.', 'Gira a la izquierda fuera de nuestra verja y camina todo recto hasta el puente de piedra.'),
    ('hannah', 'Left at the gate, straight to the bridge. Do I cross the river?', 'A la izquierda en la verja, recto hasta el puente. ¿Cruzo el río?'),
    ('graham', 'Yes, cross the bridge, then pass the green pharmacy on your right.', 'Sí, cruza el puente y luego pasa la farmacia verde a tu derecha.'),
    ('hannah', 'Bridge, then green pharmacy on the right. And after that?', 'El puente, luego la farmacia verde a la derecha. ¿Y después de eso?'),
    ('graham', 'Turn left into the small square. Look for a blue wooden door.', 'Gira a la izquierda entrando en la plazuela. Busca una puerta de madera azul.'),
    ('hannah', 'Does the shop have a big sign outside?', '¿La tienda tiene un letrero grande afuera?'),
    ('graham', 'Only a painted golden key above the door. Show the clerk this valve.', 'Solo una llave dorada pintada encima de la puerta. Enséñale al dependiente esta válvula.'),
    ('hannah', 'Twenty millimeters, brass, boiler valve. I will repeat it all the way!', 'Veinte milímetros, latón, válvula de caldera. ¡Lo repetiré todo el camino!'),
    ('graham', 'Run fast, Hannah. Room four wakes up at seven fifteen!', 'Corre rápido, Hannah. ¡La habitación cuatro se despierta a las siete y cuarto!'),
]
WALK = [
    (0, None, ["'¡Buenos días, Graham! ¿Las duchas de arriba de verdad están frías ya?' Observa cómo", (None, 'Are the showers upstairs'), "coloca el adverbio de lugar justo detrás del sustantivo sin usar 'de'."]),
    (1, None, ["'Frías como agua de río. Lleva esta válvula rota de latón en el bolsillo del abrigo.' La comparación", (None, 'Cold as river water'), "suena fresca y directa, omitiendo el primer 'tan' en el habla cotidiana."]),
    (2, None, ["'Entendido. Ahora dime cómo encontrar la ferretería.' Dos sílabas rapidísimas,", (None, 'Got it'), "confirman 'lo tengo' o 'entendido' en cualquier encargo diario."]),
    (3, None, ["'Gira a la izquierda fuera de nuestra verja y camina todo recto hasta el puente de piedra.' Para dar indicaciones en la calle, guarda el bloque esencial", (None, 'walk straight to'), 'camina recto hasta.']),
    (4, None, ["'A la izquierda en la verja, recto hasta el puente. ¿Cruzo el río?' Cuando pides instrucciones paso a paso, el presente con", (None, 'Do I cross'), "equivale a nuestro '¿cruzo ahora?'."]),
    (5, None, ["'Sí, cruza el puente y luego pasa la farmacia verde a tu derecha.' Para ubicar comercios según avanzas, el inglés dice", (None, 'on your right'), "con la preposición 'on'."]),
    (6, None, ["'El puente, luego la farmacia verde a la derecha. ¿Y después de eso?' La pregunta breve", (None, 'And after that'), 'invita a la otra persona a dar el siguiente paso de la ruta.']),
    (7, None, ["'Gira a la izquierda entrando en la plazuela. Busca una puerta de madera azul.' Al girar entrando en un espacio nuevo se usa", (None, 'Turn left into'), 'marcando el movimiento hacia dentro.']),
    (8, None, ["'¿La tienda tiene un letrero grande afuera?' Al final de la frase,", (None, 'outside'), "funciona solo como adverbio para decir 'afuera, en la fachada'."]),
    (9, None, ["'Solo una llave dorada pintada encima de la puerta. Enséñale al dependiente esta válvula.' Mira el doble objeto sin preposición en", (None, 'Show the clerk this valve'), 'primero la persona y luego la cosa.']),
    (10, None, ["'Veinte milímetros, latón, válvula de caldera. ¡Lo repetiré todo el camino!' La expresión", (None, 'all the way'), 'abarca el trayecto entero de principio a fin.']),
    (11, None, ["'Corre rápido, Hannah. ¡La habitación cuatro se despierta a las siete y cuarto!' El verbo con partícula", (None, 'wakes up'), 'expresa despertarse, mientras la hora se lee número a número:', (None, 'seven fifteen'), 'siete quince.']),
]
