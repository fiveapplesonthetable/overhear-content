# Authoring module for linden-courtyard-es-s01e02-scene-06.
ID = 'linden-courtyard-es-s01e02-scene-06'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = 'The Friday Caller  (La llamada del viernes)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Después del desayuno, el vestíbulo vuelve a quedar en calma mientras Hannah pone al día el libro de papel y Graham engrasa la bisagra de la puerta. De pronto suena el teléfono del mostrador. Escuchemos.'
OPENER = 'Analicemos despacio esta llamada misteriosa.'
TRANSITION = 'Oigamos de nuevo toda la escena seguida.'
OUTRO = 'Ahora ya tienen una cita exacta —el viernes al mediodía— y una voz nerviosa al teléfono que se niega a dar su nombre. Hasta la próxima escena.'
CLOSING = ('hannah', 'Bye for now!')
STORY = [
    ('hannah', 'Linden Courtyard Inn, good morning! Hannah speaking.', 'Linden Courtyard Inn, ¡buenos días! Les habla Hannah.'),
    ('graham', 'Who is it? Another booking for the weekend?', '¿Quién es? ¿Otra reserva para el fin de semana?'),
    ('hannah', 'Wait, hello, sir! You are calling about the dark blue suitcase?', '¡Espere, hola, señor! ¿Llama por la maleta azul oscuro?'),
    ('graham', 'Ask him his name! Write it down!', '¡Pregúntale su nombre! ¡Apúntalo!'),
    ('hannah', 'Yes, sir, we locked your bag safely in our closet. What is your name, please?', 'Sí, señor, guardamos su maleta bajo llave en nuestro armario. ¿Cuál es su nombre, por favor?'),
    ('graham', 'What is he saying? Why are you frowning?', '¿Qué está diciendo? ¿Por qué frunces el ceño?'),
    ('hannah', "Sir? He says, 'Please do not open the white paper package. I will come Friday at noon.'", '¿Señor? Dice: "Por favor, no abran el paquete de papel blanco. Iré el viernes al mediodía."'),
    ('graham', 'Give me the phone, let me ask him properly!', '¡Dame el teléfono, déjame preguntarle como es debido!'),
    ('hannah', "Too late! He said 'Thank you' and hung up!", '¡Demasiado tarde! ¡Dijo "Gracias" y colgó!'),
    ('graham', 'Polite voice? Young or old?', '¿Voz educada? ¿Joven o mayor?'),
    ('hannah', 'Quiet, polite, maybe thirty-five. He sounded nervous, not angry.', 'Tranquila, educada, quizá de unos treinta y cinco. Sonaba nervioso, no enfadado.'),
    ('graham', 'Nervous about a wooden toy train? This story gets stranger every hour.', '¿Nervioso por un tren de juguete de madera? Esta historia se pone más rara cada hora.'),
]
WALK = [
    (0, None, ["'Linden Courtyard Inn, ¡buenos días! Les habla Hannah.' Al contestar el teléfono en inglés te identificas con tu nombre seguido de", (None, 'Hannah speaking'), "literalmente 'Hannah hablando'."]),
    (1, None, ["'¿Quién es? ¿Otra reserva para el fin de semana?' Al teléfono o en la puerta, el inglés pregunta con sujeto neutro:", (None, 'Who is it'), 'hasta saber de quién se trata.']),
    (2, None, ["'¡Espere, hola, señor! ¿Llama por la maleta azul oscuro?' Nota que Hannah mantiene el orden de afirmación en", (None, 'You are calling about'), 'y convierte la frase en pregunta solo con la entonación de sorpresa.']),
    (3, None, ["'¡Pregúntale su nombre! ¡Apúntalo!' Apuntar algo en papel se dice siempre", (None, 'Write it down'), 'indicando que queda fijado por escrito.']),
    (4, None, ["'Sí, señor, guardamos su maleta bajo llave en nuestro armario. ¿Cuál es su nombre, por favor?' Donde nosotros decimos '¿cuál es su nombre?', el inglés pregunta", (None, 'What is your name'), "usando 'qué' en lugar de 'cuál'."]),
    (5, None, ["'¿Qué está diciendo? ¿Por qué frunces el ceño?' Un solo verbo inglés,", (None, 'frowning'), "expresa todo nuestro 'fruncir el ceño' en este mismo instante."]),
    (6, None, ['\'¿Señor? Dice: "Por favor, no abran el paquete de papel blanco. Iré el viernes al mediodía."\' Para las doce exactas del día el inglés dice', (None, 'at noon'), 'al mediodía.']),
    (7, None, ["'¡Dame el teléfono, déjame preguntarle como es debido!' El adverbio", (None, 'properly'), "significa 'como corresponde' o 'en condiciones', no 'propiamente'."]),
    (8, None, ['\'¡Demasiado tarde! ¡Dijo "Gracias" y colgó!\' Colgar el teléfono conserva la imagen de los antiguos auriculares de pared en', (None, 'hung up'), 'pasado irregular de colgar.']),
    (9, None, ["'¿Voz educada? ¿Joven o mayor?' Graham recorta al máximo sus preguntas rápidas:", (None, 'Young or old'), 'joven o mayor.']),
    (10, None, ["'Tranquila, educada, quizá de unos treinta y cinco. Sonaba nervioso, no enfadado.' Con verbos de percepción auditiva,", (None, 'sounded nervous'), 'va seguido directamente del adjetivo.']),
    (11, None, ["'¿Nervioso por un tren de juguete de madera? Esta historia se pone más rara cada hora.' Para decir 'volverse más raro', el adjetivo suma terminación comparativa en", (None, 'gets stranger'), 'más extraña.']),
]
