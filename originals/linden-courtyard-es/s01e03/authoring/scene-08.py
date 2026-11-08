# Authoring module for linden-courtyard-es-s01e03-scene-08.
ID = 'linden-courtyard-es-s01e03-scene-08'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 3
SCENE = 8
TITLE = 'Ice-Cold Pipes  (Tuberías heladas)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = 'Abajo en la recepción, Hannah y Arthur esperan inquietos junto a la puerta del sótano hasta que Graham sube limpiándose las manos con un trapo y negando con la cabeza. Escucha primero.'
OPENER = 'Repasemos ahora cada línea de la escena con calma.'
TRANSITION = 'Escuchemos de nuevo toda la conversación de corrido.'
OUTRO = 'Un supuesto inspector de viajes en el tercer piso, una válvula rota en el sótano y una carrera a las siete de la mañana al otro lado del puente. Terminamos el episodio tres; nos vemos en el episodio cuatro.'
CLOSING = ('graham', 'See you tomorrow!')
STORY = [
    ('arthur', 'Tell me it was just a tiny air bubble, Graham! Please!', '¡Dime que solo era una diminuta burbuja de aire, Graham! ¡Por favor!'),
    ('graham', 'Bad news. The brass pressure valve on the old boiler just gave up.', 'Malas noticias. La válvula de presión de latón de la caldera vieja acaba de rendirse.'),
    ('hannah', 'Does that mean no radiators tonight, or no hot water too?', '¿Eso significa sin radiadores esta noche, o también sin agua caliente?'),
    ('graham', 'The rooms will stay warm until morning, Hannah, because the brick walls hold heat.', 'Las habitaciones se mantendrán calientes hasta la mañana, Hannah, porque los muros de ladrillo guardan el calor.'),
    ('arthur', 'Thank heavens! And the morning showers?', '¡Menos mal! ¿Y las duchas de la mañana?'),
    ('graham', 'By tomorrow morning, the shower water will be ice cold.', 'Para mañana por la mañana, el agua de la ducha estará helada.'),
    ('arthur', 'Ice cold showers?! With the Portland Travel Guide inspector on the third floor?!', '¡¿Duchas heladas?! ¡¿Con el inspector de la Guía de Viajes de Portland en el tercer piso?!'),
    ('hannah', 'Do you have a spare brass valve in your toolbox?', '¿Tienes una válvula de latón de repuesto en tu caja de herramientas?'),
    ('graham', 'Used my last one in winter. Only the old hardware shop past the bridge sells this size.', 'Usé la última en invierno. Solo la vieja ferretería pasando el puente vende este tamaño.'),
    ('hannah', 'What time does that hardware shop open?', '¿A qué hora abre esa ferretería?'),
    ('graham', 'Seven sharp, half an hour before breakfast.', 'A las siete en punto, media hora antes del desayuno.'),
    ('hannah', 'Set your alarm, Graham. Tomorrow morning we beat the cold showers!', 'Pon tu despertador, Graham. ¡Mañana por la mañana les ganamos a las duchas frías!'),
]
WALK = [
    (0, None, ["'¡Dime que solo era una diminuta burbuja de aire, Graham! ¡Por favor!' Después de", (None, 'Tell me'), "el inglés omite con naturalidad el equivalente a 'que' y entra directo en la frase."]),
    (1, None, ["'Malas noticias. La válvula de presión de latón de la caldera vieja acaba de rendirse.' Atención a", (None, 'Bad news'), 'que pese a terminar en ese es incontable en inglés, y al verbo con partícula', (None, 'gave up'), 'rendirse o dejar de funcionar.']),
    (2, None, ["'¿Eso significa sin radiadores esta noche, o también sin agua caliente?' Al final de una pregunta o afirmación,", (None, 'too'), "añade la idea de 'también' con una sola sílaba."]),
    (3, None, ["'Las habitaciones se mantendrán calientes hasta la mañana, Hannah, porque los muros de ladrillo guardan el calor.' La combinación", (None, 'stay warm'), "une 'permanecer' con un adjetivo para indicar que el calor dura."]),
    (4, None, ["'¡Menos mal! ¿Y las duchas de la mañana?' La exclamación de alivio", (None, 'Thank heavens'), 'suena muy cotidiana y amable cuando te libras de un susto.']),
    (5, None, ["'Para mañana por la mañana, el agua de la ducha estará helada.' Decir", (None, 'ice cold'), "pinta la temperatura con una imagen directa: fría como el hielo."]),
    (6, None, ["'¡¿Duchas heladas?! ¡¿Con el inspector de la Guía de Viajes de Portland en el tercer piso?!' En pisos de edificios el inglés elige siempre", (None, 'on the third floor'), 'como sobre esa planta.']),
    (7, None, ["'¿Tienes una válvula de latón de repuesto en tu caja de herramientas?' Delante de cualquier pieza u objeto,", (None, 'spare'), "significa 'de repuesto' o 'extra'."]),
    (8, None, ["'Usé la última en invierno. Solo la vieja ferretería pasando el puente vende este tamaño.' En inglés la ferretería se llama", (None, 'hardware shop'), 'tienda de herrajes, y', (None, 'past the bridge'), "indica 'pasando el puente'."]),
    (9, None, ["'¿A qué hora abre esa ferretería?' Para preguntar horarios no hace falta preposición al principio:", (None, 'What time does'), "equivale directo a nuestro '¿a qué hora?'."]),
    (10, None, ["'A las siete en punto, media hora antes del desayuno.' Tras una hora exacta,", (None, 'Seven sharp'), "significa 'a las siete clavadas' sin un minuto de retraso."]),
    (11, None, ["'Pon tu despertador, Graham. ¡Mañana por la mañana les ganamos a las duchas frías!' Para programar el despertador del móvil o reloj se dice siempre", (None, 'Set your alarm'), 'ajustar la alarma.']),
]
