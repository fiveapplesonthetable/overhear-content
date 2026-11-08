# Authoring module for linden-courtyard-es-s01e03-scene-06.
ID = 'linden-courtyard-es-s01e03-scene-06'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 3
SCENE = 6
TITLE = 'A Five-Star Sigh of Relief  (Un suspiro de alivio de cinco estrellas)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = 'De vuelta en el mostrador de la planta baja, Arthur camina de un lado a otro nervioso hasta que Hannah baja sonriendo junto a él y Tessa. Entonces Hannah repara en algo apoyado al lado de la campanilla de latón. Escucha primero.'
OPENER = 'Ahora analicemos cada frase con calma.'
TRANSITION = 'Volvamos a oír toda la escena a velocidad natural.'
OUTRO = 'Unos dibujos limpios a lápiz y una nota de nueve sobre diez los han convencido de que Caleb es un inspector secreto de guías de viaje, justo cuando un golpe metálico resuena por la casa. Hasta la próxima.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('arthur', 'Well? Did he shout? Did he ask for his money back?', '¿Y bien? ¿Gritó? ¿Pidió que le devolviéramos su dinero?'),
    ('hannah', 'Neither! He loved the quiet roof beams and thanked us.', '¡Ni lo uno ni lo otro! Le encantaron las vigas silenciosas del techo y nos dio las gracias.'),
    ('arthur', 'Hannah, you have a gift for hospitality! My blood pressure is saved!', '¡Hannah, tienes un don para la hospitalidad! ¡Mi tensión arterial está a salvo!'),
    ('tessa', 'He even finished every drop of vegetable soup before going up.', 'Incluso se terminó hasta la última gota de sopa de verduras antes de subir.'),
    ('hannah', 'Wait, whose small brown leather notebook is this on the counter?', 'Esperen, ¿de quién es este pequeño cuaderno de cuero marrón en el mostrador?'),
    ('tessa', 'Caleb set it down when he took the dry towel from me!', '¡Caleb lo dejó apoyado cuando me tomó la toalla seca!'),
    ('arthur', 'Do not snoop, of course... wait, it fell open to the middle page!', 'No curioseen, por supuesto... ¡esperen, se abrió solo por la página central!'),
    ('hannah', 'Why are there neat pencil drawings of three guesthouses on our street?', '¿Por qué hay dibujos limpios a lápiz de tres posadas de nuestra calle?'),
    ('tessa', "Look at the words beside ours: 'Courtyard width, street noise, quiet score: nine out of ten!'", "Miren las palabras junto a la nuestra: 'Ancho del patio, ruido de la calle, puntuación de silencio: ¡nueve de diez!'"),
    ('arthur', 'Nine out of ten?! Nobody measures courtyards unless...', '¡¿Nueve de diez?! Nadie mide patios a menos que...'),
    ('tessa', 'Unless he writes for the annual Portland Travel Guide!', '¡A menos que escriba para la Guía Anual de Viajes de Portland!'),
    ('hannah', 'Quick, close it! Let us take it upstairs... wait, what is that loud clanking sound?', '¡Rápido, ciérralo! Subámoslo arriba... esperen, ¿qué es ese ruido metálico tan fuerte?'),
]
WALK = [
    (0, None, ["'¿Y bien? ¿Gritó? ¿Pidió que le devolviéramos su dinero?' Mira qué compacto resulta", (None, 'ask for his money back'), "donde 'back' al final expresa toda la idea de devolución."]),
    (1, None, ["'¡Ni lo uno ni lo otro! Le encantaron las vigas silenciosas del techo y nos dio las gracias.' Cuando quieres descartar dos preguntas seguidas de golpe,", (None, 'Neither'), "responde 'ninguna de las dos cosas'."]),
    (2, None, ["'¡Hannah, tienes un don para la hospitalidad! ¡Mi tensión arterial está a salvo!' El giro", (None, 'have a gift for'), 'elogia un talento natural para un oficio o trato.']),
    (3, None, ["'Incluso se terminó hasta la última gota de sopa de verduras antes de subir.' Fíjate en la preposición temporal seguida de '-ing':", (None, 'before going up'), 'antes de subir.']),
    (4, None, ["'Esperen, ¿de quién es este pequeño cuaderno de cuero marrón en el mostrador?' Para preguntar de quién es algo, el inglés coloca", (None, 'whose'), 'pegado delante del objeto completo.']),
    (5, None, ["'¡Caleb lo dejó apoyado cuando me tomó la toalla seca!' El verbo compuesto", (None, 'set it down'), 'describe posar un objeto con cuidado sobre una superficie.']),
    (6, None, ["'No curioseen, por supuesto... ¡esperen, se abrió solo por la página central!' La combinación", (None, 'fell open'), 'retrata muy gráficamente un libro que cae y queda abierto.']),
    (7, None, ["'¿Por qué hay dibujos limpios a lápiz de tres posadas de nuestra calle?' Para preguntar '¿por qué hay...?' en plural se invierte a", (None, 'Why are there'), 'antes del sustantivo plural.']),
    (8, None, ["'Miren las palabras junto a la nuestra: Ancho del patio, ruido de la calle, puntuación de silencio: ¡nueve de diez!' En calificaciones o escalas, la proporción se dice con", (None, 'nine out of ten'), 'nueve de diez.']),
    (9, None, ["'¡¿Nueve de diez?! Nadie mide patios a menos que...' El conector condicional", (None, 'unless'), "resume en una sola palabra nuestro 'a menos que' o 'salvo que'."]),
    (10, None, ["'¡A menos que escriba para la Guía Anual de Viajes de Portland!' En inglés, tras 'unless' se usa presente simple,", (None, 'Unless he writes'), 'donde el español exige subjuntivo.']),
    (11, None, ["'¡Rápido, ciérralo! Subámoslo arriba... esperen, ¿qué es ese ruido metálico tan fuerte?' El verbo sonoro", (None, 'clanking sound'), 'imita directamente el choque seco de piezas de metal.']),
]
