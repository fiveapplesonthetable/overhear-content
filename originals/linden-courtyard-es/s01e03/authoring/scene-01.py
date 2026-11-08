# Authoring module for linden-courtyard-es-s01e03-scene-01.
ID = 'linden-courtyard-es-s01e03-scene-01'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = 'Thirty-Five Minutes  (Treinta y cinco minutos)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'La lluvia golpea las ventanas del vestíbulo en la posada Linden Courtyard Inn, en Portland. Con un segundo huésped para la habitación siete a punto de llegar en treinta y cinco minutos, Arthur, Hannah y Graham se apresuran hacia la escalera. Escucha primero toda la escena en inglés.'
OPENER = 'Ahora repasemos la conversación con calma, frase por frase.'
TRANSITION = 'Escuchemos otra vez toda la escena a velocidad natural.'
OUTRO = 'Quedan treinta y cinco minutos en el reloj y cuatro cajas en el camino. No te preocupes si alguna expresión pasó rápido; volverán a salir arriba en el tercer piso. Hasta la próxima.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('arthur', 'Thirty-five minutes! He will write a terrible one star review!', '¡Treinta y cinco minutos! ¡Escribirá una reseña terrible de una estrella!'),
    ('hannah', 'Take a deep breath, Arthur. Nobody has written anything yet.', 'Respira hondo, Arthur. Todavía nadie ha escrito nada.'),
    ('graham', 'Here is the small silver key for the third floor attic door.', 'Aquí está la llavecita plateada para la puerta del ático del tercer piso.'),
    ('arthur', 'Does the attic even have a proper bed?', '¿El ático siquiera tiene una cama en condiciones?'),
    ('graham', 'Yes, a good wooden bed, a clean desk, and the best view in the house.', 'Sí, una buena cama de madera, un escritorio limpio y la mejor vista de la casa.'),
    ('hannah', 'Then why do we never rent it to guests?', '¿Entonces por qué nunca se lo alquilamos a los huéspedes?'),
    ('graham', 'Because the stairs are narrow and Arthur keeps old lamp boxes there.', 'Porque la escalera es estrecha y Arthur guarda allí cajas viejas de lámparas.'),
    ('arthur', 'Only three small boxes! Maybe four!', '¡Solo tres cajas pequeñas! ¡Quizás cuatro!'),
    ('hannah', 'We can move four boxes in five minutes. Let us go look right now!', 'Podemos mover cuatro cajas en cinco minutos. ¡Vamos a mirar ahora mismo!'),
    ('graham', 'Up the stairs, turn left at the landing, last door at the top.', 'Subiendo la escalera, gira a la izquierda en el rellano, la última puerta arriba del todo.'),
    ('arthur', 'I will bring clean white sheets from the linen closet!', '¡Traeré sábanas blancas limpias del armario de la ropa blanca!'),
    ('hannah', 'Come on, race you to the third floor!', '¡Vamos, te echo una carrera hasta el tercer piso!'),
]
WALK = [
    (0, None, ["'¡Treinta y cinco minutos! ¡Escribirá una reseña terrible de una estrella!' Para hablar del futuro inmediato o temido, el auxiliar", (None, 'will write'), 'marca la acción sin cambiar la terminación del verbo.']),
    (1, None, ["'Respira hondo, Arthur. Todavía nadie ha escrito nada.' Guarda el bloque fijo", (None, 'Take a deep breath'), 'que en inglés literalmente invita a tomar un aliento profundo.']),
    (2, None, ["'Aquí está la llavecita plateada para la puerta del ático del tercer piso.' Mira cómo se apilan los detalles antes del sustantivo final en", (None, 'third floor attic door'), 'sin preposiciones intermedias.']),
    (3, None, ["'¿El ático siquiera tiene una cama en condiciones?' El adverbio", (None, 'even'), "añade ese matiz de duda o sorpresa equivalente a nuestro 'siquiera'."]),
    (4, None, ["'Sí, una buena cama de madera, un escritorio limpio y la mejor vista de la casa.' Con superlativos de lugares, el inglés prefiere", (None, 'best view in the house'), "usando 'en' en lugar de 'de'."]),
    (5, None, ["'¿Entonces por qué nunca se lo alquilamos a los huéspedes?' Observa el orden de pregunta con adverbio de frecuencia:", (None, 'why do we never rent'), "colocando 'nunca' justo delante del verbo."]),
    (6, None, ["'Porque la escalera es estrecha y Arthur guarda allí cajas viejas de lámparas.' En inglés 'escalera' suele ir en plural,", (None, 'the stairs are narrow'), 'por los escalones que la forman.']),
    (7, None, ["'¡Solo tres cajas pequeñas! ¡Quizás cuatro!' Una palabra sola y muy útil,", (None, 'Maybe'), 'sirve para suavizar o corregir un cálculo sobre la marcha.']),
    (8, None, ["'Podemos mover cuatro cajas en cinco minutos. ¡Vamos a mirar ahora mismo!' En el habla cotidiana se enlazan dos verbos de movimiento seguidos en", (None, 'go look'), 'sin necesidad de conjunción.']),
    (9, None, ["'Subiendo la escalera, gira a la izquierda en el rellano, la última puerta arriba del todo.' Para indicar direcciones breves,", (None, 'turn left at the landing'), 'marca el giro y el punto exacto con total claridad.']),
    (10, None, ["'¡Traeré sábanas blancas limpias del armario de la ropa blanca!' Cuando alguien se ofrece en el acto a hacer algo, usa", (None, 'I will bring'), 'para expresar decisión espontánea.']),
    (11, None, ["'¡Vamos, te echo una carrera hasta el tercer piso!' El giro coloquial", (None, 'race you'), 'omite el sujeto y lanza un reto amistoso al instante.']),
]
