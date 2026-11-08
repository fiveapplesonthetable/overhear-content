# Authoring module for linden-courtyard-es-s01e03-scene-03.
ID = 'linden-courtyard-es-s01e03-scene-03'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 3
SCENE = 3
TITLE = 'Left at the Landing  (A la izquierda en el rellano)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'hannah': 'Hannah', 'tessa': 'Tessa', 'arthur': 'Arthur'}
INTRO = 'Diez minutos antes de las ocho, Hannah, Tessa y Arthur dan los últimos retoques a la habitación del tercer piso. Cada detalle cuenta antes de que llegue el viajero empapado. Escucha primero.'
OPENER = 'Ahora recorramos las frases una por una.'
TRANSITION = 'Escuchemos de nuevo toda la escena seguida.'
OUTRO = 'La lámpara de latón ya brilla con luz cálida justo cuando suena abajo la campana de la verja. En la siguiente escena, Caleb entra huyendo de la lluvia. Hasta pronto.'
CLOSING = ('hannah', 'Bye for now!')
STORY = [
    ('tessa', 'Tuck that sheet corner tight, Hannah! Here go the two soft pillows.', '¡Mete bien prieta esa esquina de la sábana, Hannah! Aquí van las dos almohadas suaves.'),
    ('hannah', 'Done! And the blue rug fits right beside the bed.', '¡Listo! Y la alfombra azul encaja justo al lado de la cama.'),
    ('arthur', 'Where should I hang this round mirror? Left of the window or right?', '¿Dónde debería colgar este espejo redondo? ¿A la izquierda de la ventana o a la derecha?'),
    ('hannah', 'Right beside the desk, where the light is good.', 'Justo al lado del escritorio, donde la luz es buena.'),
    ('tessa', "Plug in Graham's brass lamp... oh, look how warm that yellow light is!", 'Enchufa la lámpara de latón de Graham... ¡oh, mira qué cálida es esa luz amarilla!'),
    ('arthur', 'Honestly, I almost want to sleep up here myself tonight!', '¡Sinceramente, casi quiero dormir aquí arriba yo mismo esta noche!'),
    ('hannah', 'Wait, what discount should we offer him for changing rooms?', 'Espera, ¿qué descuento deberíamos ofrecerle por cambiar de habitación?'),
    ('arthur', 'Half price for tonight, and free breakfast all week!', '¡Mitad de precio por esta noche y desayuno gratis toda la semana!'),
    ('tessa', 'Generous! Did you just hear the courtyard gate bell downstairs?', '¡Qué generoso! ¿Acabas de oír abajo la campana de la verja del patio?'),
    ('hannah', "Eight o'clock on the dot! Our guest is here!", '¡Las ocho en punto! ¡Nuestro huésped ya está aquí!'),
    ('arthur', 'My heart is pounding! Hannah, you explain it, you sound calm and honest!', '¡Me late el corazón con fuerza! ¡Hannah, explícalo tú, suenas tranquila y sincera!'),
    ('hannah', 'Leave it to me. Let us go down and welcome him.', 'Déjamelo a mí. Bajemos a darle la bienvenida.'),
]
WALK = [
    (0, None, ["'¡Mete bien prieta esa esquina de la sábana, Hannah! Aquí van las dos almohadas suaves.' Al final de", (None, 'Tuck that sheet corner tight'), 'el adjetivo indica cómo debe quedar la sábana tras remetarla.']),
    (1, None, ["'¡Listo! Y la alfombra azul encaja justo al lado de la cama.' Añadir", (None, 'right beside'), "refuerza la cercanía exacta, igual que nuestro 'justo al lado de'."]),
    (2, None, ["'¿Dónde debería colgar este espejo redondo? ¿A la izquierda de la ventana o a la derecha?' Para pedir consejo práctico al momento,", (None, 'Where should I hang'), 'suena cortés y directo.']),
    (3, None, ["'Justo al lado del escritorio, donde la luz es buena.' La cláusula", (None, 'where the light is good'), 'explica el motivo práctico de forma sencilla y natural.']),
    (4, None, ["'Enchufa la lámpara de latón de Graham... ¡oh, mira qué cálida es esa luz amarilla!' Con aparatos eléctricos usamos el verbo con partícula", (None, 'Plug in'), 'para conectar a la corriente.']),
    (5, None, ["'¡Sinceramente, casi quiero dormir aquí arriba yo mismo esta noche!' El pronombre enfático", (None, 'myself'), "al final subraya 'yo mismo en persona' sin cambiar el significado del verbo."]),
    (6, None, ["'Espera, ¿qué descuento deberíamos ofrecerle por cambiar de habitación?' Tras una preposición como 'por', el verbo inglés toma siempre terminación en '-ing':", (None, 'for changing rooms'), 'nunca infinitivo.']),
    (7, None, ["'¡Mitad de precio por esta noche y desayuno gratis toda la semana!' Dos bloques comerciales esenciales:", (None, 'Half price'), 'sin artículo ni preposición, y', (None, 'free breakfast'), 'para desayuno incluido sin coste.']),
    (8, None, ["'¡Qué generoso! ¿Acabas de oír abajo la campana de la verja del patio?' Combinar pasado con", (None, 'Did you just hear'), "equivale en inglés americano a nuestro '¿acabas de oír?'."]),
    (9, None, ["'¡Las ocho en punto! ¡Nuestro huésped ya está aquí!' Además de 'o'clock', el giro coloquial", (None, 'on the dot'), 'destaca la puntualidad al segundo exacto.']),
    (10, None, ["'¡Me late el corazón con fuerza! ¡Hannah, explícalo tú, suenas tranquila y sincera!' En órdenes donde importa quién actúa, el inglés conserva el pronombre delante:", (None, 'you explain it'), "para marcar 'explícalo tú'."]),
    (11, None, ["'Déjamelo a mí. Bajemos a darle la bienvenida.' La promesa breve", (None, 'Leave it to me'), 'tranquiliza enseguida a cualquiera cuando te haces cargo de un asunto.']),
]
