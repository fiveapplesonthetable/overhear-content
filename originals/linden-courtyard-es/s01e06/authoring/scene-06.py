# Authoring module for linden-courtyard-es-s01e06-scene-06.
ID = 'linden-courtyard-es-s01e06-scene-06'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 6
SCENE = 6
TITLE = 'Permanent Keys  (Llaves permanentes)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'arthur': 'Arthur', 'tessa': 'Tessa', 'hannah': 'Hannah'}
INTRO = 'En el soleado rincón de la cafetería, Arthur se planta erguido frente a Tessa y Hannah con la segunda página de la carta aún en la mano y una sonrisa enorme. Escuchemos primero.'
OPENER = 'Repasemos línea por línea estas grandes noticias.'
TRANSITION = 'Volvamos a oír la escena completa de corrido.'
OUTRO = '¡Una cafetería abierta al barrio para Tessa y un puesto fijo de encargada de recepción para Hannah! En la próxima escena cae la tarde y se encienden los farolillos del patio.'
CLOSING = ('arthur', 'See you later!')
STORY = [
    ('arthur', 'Tessa, how many cinnamon rolls and lemon cakes can your oven bake each morning?', 'Tessa, ¿cuántos rollos de canela y pasteles de limón puede hornear tu horno cada mañana?'),
    ('tessa', 'Double what I make now! Are we really opening the courtyard cafe to our street?', '¡El doble de lo que hago ahora! ¿De verdad vamos a abrir la cafetería del patio a nuestra calle?'),
    ('arthur', 'Starting tomorrow at eight! Four tables inside, three tables under the tree!', '¡Empezando mañana a las ocho! ¡Cuatro mesas dentro, tres mesas bajo el árbol!'),
    ('tessa', 'My dream cafe, right here in our own courtyard! Wait until I tell the whole street!', '¡La cafetería de mis sueños, justo aquí en nuestro propio patio! ¡Esperen a que se lo cuente a toda la calle!'),
    ('arthur', 'And now, Hannah, today is Friday, the last day of your five day trial week.', 'Y ahora, Hannah, hoy es viernes, el último día de tu semana de prueba de cinco días.'),
    ('hannah', 'Oh! With the suitcases, the boiler, and the letter, I completely forgot!', '¡Oh! ¡Con las maletas, la caldera y la carta, se me olvidó por completo!'),
    ('arthur', 'On Monday you opened our tricky door; since then you saved rooms, pipes, breakfast, and our lease.', 'El lunes abriste nuestra puerta con truco; desde entonces salvaste habitaciones, tuberías, el desayuno y nuestro contrato.'),
    ('tessa', 'If you do not hire her full time, Arthur, I am hiring her in my kitchen!', '¡Si no la contratas a jornada completa, Arthur, la contrato yo en mi cocina!'),
    ('arthur', 'Hands off, Tessa! Hannah, would you stay as our permanent front desk manager?', '¡Quieta ahí, Tessa! Hannah, ¿te quedarías como nuestra encargada fija de recepción?'),
    ('hannah', 'Stay here with all of you? Yes, a hundred times yes!', '¿Quedarme aquí con todos ustedes? ¡Sí, cien veces sí!'),
    ('arthur', "Wonderful! Your name goes in Graham's big paper book in permanent ink!", '¡Maravilloso! ¡Tu nombre entra en el gran libro de papel de Graham con tinta permanente!'),
    ('hannah', 'Best first week of my life!', '¡La mejor primera semana de mi vida!'),
]
WALK = [
    (0, None, ["'Tessa, ¿cuántos rollos de canela y pasteles de limón puede hornear tu horno cada mañana?' Con sustantivos contables en plural preguntamos la cantidad con", (None, 'how many'), '¿cuántos?']),
    (1, None, ["'¡El doble de lo que hago ahora! ¿De verdad vamos a abrir la cafetería del patio a nuestra calle?' Muy ágil y directo,", (None, 'Double what I make now'), 'significa el doble de lo que preparo ahora.']),
    (2, None, ["'¡Empezando mañana a las ocho! ¡Cuatro mesas dentro, tres mesas bajo el árbol!' Para anunciar desde cuándo entra en vigor algo nuevo, abre con", (None, 'Starting tomorrow'), 'a partir de mañana.']),
    (3, None, ["'¡La cafetería de mis sueños, justo aquí en nuestro propio patio! ¡Esperen a que se lo cuente a toda la calle!' En inglés 'dream' delante de un nombre significa soñado:", (None, 'My dream cafe'), "la cafetería de mis sueños."]),
    (4, None, ["'Y ahora, Hannah, hoy es viernes, el último día de tu semana de prueba de cinco días.' De nuevo la medida en singular cuando funciona como adjetivo:", (None, 'five day trial week'), 'semana de prueba de cinco días.']),
    (5, None, ["'¡Oh! ¡Con las maletas, la caldera y la carta, se me olvidó por completo!' Donde decimos 'se me olvidó', el inglés pone a la persona como sujeto activo:", (None, 'I completely forgot'), 'olvidé por completo.']),
    (6, None, ["'El lunes abriste nuestra puerta con truco; desde entonces salvaste habitaciones, tuberías, el desayuno y nuestro contrato.' El conector temporal", (None, 'since then'), 'une aquel lunes con todo el resto de la semana.']),
    (7, None, ["'¡Si no la contratas a jornada completa, Arthur, la contrato yo en mi cocina!' En vocabulario laboral, trabajar a tiempo completo es", (None, 'hire her full time'), 'contratarla a jornada completa.']),
    (8, None, ["'¡Quieta ahí, Tessa! Hannah, ¿te quedarías como nuestra encargada fija de recepción?' Dos expresiones geniales:", (None, 'Hands off'), '¡manos fuera, ni tocarla!, y la oferta cortés', (None, 'would you stay'), '¿te quedarías?']),
    (9, None, ["'¿Quedarme aquí con todos ustedes? ¡Sí, cien veces sí!' Con 'hundred' en singular se añade siempre 'a':", (None, 'a hundred times yes'), '¡cien veces sí!']),
    (10, None, ["'¡Maravilloso! ¡Tu nombre entra en el gran libro de papel de Graham con tinta permanente!' Para materiales de escritura como tinta o lápiz usamos 'in':", (None, 'in permanent ink'), 'con tinta indeleble.']),
    (11, None, ["'¡La mejor primera semana de mi vida!' Cerrando con entusiasmo puro,", (None, 'Best first week of my life'), 'omite el artículo inicial como es habitual en exclamaciones habladas.']),
]
