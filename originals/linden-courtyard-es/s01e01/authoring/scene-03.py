# Authoring module for linden-courtyard-es-s01e01-scene-03.
ID = 'linden-courtyard-es-s01e01-scene-03'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = 'Where Are My Glasses?  (¿Dónde están mis gafas?)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Antes de que llegue el primer huésped, el dueño de la posada, Arthur, entra apurado desde el patio con cara de agobio. Hannah y Graham observan cómo se registra los bolsillos nervioso. Escucha primero toda la escena.'
OPENER = 'Repasemos ahora los detalles paso a paso.'
TRANSITION = 'Escuchemos de nuevo la escena completa sin pausas.'
OUTRO = 'Arthur encontró las gafas en su propia frente justo cuando paraba el taxi afuera. Relájate y deja que el ritmo del inglés se te vaya quedando; nos vemos en la siguiente escena.'
CLOSING = ('arthur', 'Bye for now!')
STORY = [
    ('arthur', 'Good morning, everyone! Welcome, Hannah. Is everything ready?', '¡Buenos días a todos! Bienvenida, Hannah. ¿Está todo listo?'),
    ('hannah', 'Good morning! Yes, the desk is clean and the keys are ready.', '¡Buenos días! Sí, el mostrador está limpio y las llaves están listas.'),
    ('arthur', "Today's guest in room four is staying all week. Everything must be perfect!", 'La huésped de hoy en la habitación cuatro se queda toda la semana. ¡Todo tiene que salir perfecto!'),
    ('graham', 'Relax, Arthur. The room is clean and the towels are fresh.', 'Tranquilo, Arthur. La habitación está limpia y las toallas están frescas.'),
    ('arthur', 'I need to read the reservation book, but I cannot find my glasses!', '¡Necesito leer el libro de reservas, pero no encuentro mis gafas!'),
    ('hannah', 'Are they in your coat pocket?', '¿Están en el bolsillo de tu abrigo?'),
    ('arthur', 'No, only my pen and three old receipts!', '¡No, solo mi bolígrafo y tres recibos viejos!'),
    ('graham', 'Look in the mirror behind the desk, boss.', 'Mira en el espejo detrás del mostrador, jefe.'),
    ('arthur', 'Why would my glasses be in the... oh! They are on my head!', '¿Por qué estarían mis gafas en el... ah! ¡Están en mi cabeza!'),
    ('hannah', 'Right there on your forehead, safe and sound.', 'Justo ahí en tu frente, sanas y salvas.'),
    ('arthur', 'Do not tell anyone! Now, smile brightly when the bell rings.', '¡No se lo digas a nadie! Ahora sonríe con alegría cuando suene el timbre.'),
    ('graham', 'Here comes a taxi at the gate right now.', 'Aquí viene un taxi en la entrada ahora mismo.'),
]
WALK = [
    (0, None, ["'¡Buenos días a todos! Bienvenida, Hannah. ¿Está todo listo?' Los pronombres globales como", (None, 'everything'), 'funcionan en singular, por eso la pregunta arranca con', (None, 'Is everything ready'), 'en singular.']),
    (1, None, ["'¡Buenos días! Sí, el mostrador está limpio y las llaves están listas.' Nota cómo el adjetivo", (None, 'ready'), 'no cambia nunca: sirve igual para una cosa que para varias llaves.']),
    (2, None, ["'La huésped de hoy en la habitación cuatro se queda toda la semana. ¡Todo tiene que salir perfecto!' Incluso con palabras de tiempo puedes formar posesivo con apóstrofo y ese:", (None, "Today's guest"), 'la huésped de hoy.']),
    (3, None, ["'Tranquilo, Arthur. La habitación está limpia y las toallas están frescas.' Un simple", (None, 'Relax'), "al empezar basta para calmar a alguien, igual que nuestro 'tranquilo'."]),
    (4, None, ["'Necesito leer el libro de reservas, pero no encuentro mis gafas!' Cuando no logras localizar algo en ese instante, el inglés prefiere", (None, 'cannot find'), "en lugar de decir solo 'no encuentro'."]),
    (5, None, ["'¿Están en el bolsillo de tu abrigo?' Como 'gafas' también es plural en inglés, Hannah pregunta por ellas con", (None, 'Are they'), 'antes de nombrar', (None, 'coat pocket'), 'el bolsillo del abrigo.']),
    (6, None, ["'¡No, solo mi bolígrafo y tres recibos viejos!' Ojo con la ortografía engañosa de", (None, 'receipts'), "porque esa letra 'p' intermedia es totalmente muda al pronunciarla."]),
    (7, None, ["'Mira en el espejo detrás del mostrador, jefe.' En inglés te miras 'dentro' del espejo,", (None, 'in the mirror'), 'y', (None, 'behind the desk'), 'sitúa algo justo detrás.']),
    (8, None, ["'¿Por qué estarían mis gafas en el... ah! ¡Están en mi cabeza!' El auxiliar condicional en", (None, 'Why would'), "le da ese matiz de extrañeza incrédula: '¿por qué iban a estar...?'."]),
    (9, None, ["'Justo ahí en tu frente, sanas y salvas.' La pareja fija", (None, 'safe and sound'), "equivale exactamente a nuestro 'sano y salvo' para personas u objetos."]),
    (10, None, ["'¡No se lo digas a nadie! Ahora sonríe con alegría cuando suene el timbre.' Para prohibir algo sin doble negación, empiezas con", (None, 'Do not tell anyone'), 'cerrando con un pronombre indefinido.']),
    (11, None, ["'Aquí viene un taxi en la entrada ahora mismo.' Al anunciar algo que ves llegar,", (None, 'Here comes'), "invierte el orden igual que en español 'aquí viene'."]),
]
