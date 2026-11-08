# Authoring module for linden-courtyard-es-s01e03-scene-07.
ID = 'linden-courtyard-es-s01e03-scene-07'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 3
SCENE = 7
TITLE = 'Returning the Notebook  (Devolviendo el cuaderno)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb'}
INTRO = 'Hannah sube hasta la puerta del ático para devolver el cuaderno de cuero olvidado de Caleb, esforzándose por actuar con naturalidad aunque cree que él es un inspector secreto. Escuchemos primero.'
OPENER = 'Vamos a recorrer la conversación frase por frase.'
TRANSITION = 'Escuchemos de nuevo la escena completa a ritmo normal.'
OUTRO = 'Caleb recuperó su cuaderno sin sospechar nada, pero ese radiador que empieza a enfriarse anuncia problemas. Queda una última escena en el episodio tres: ¡bajemos al sótano! Hasta pronto.'
CLOSING = ('caleb', 'Have a good night!')
STORY = [
    ('hannah', 'Excuse me, Caleb? Sorry to disturb you.', '¿Disculpe, Caleb? Siento molestarlo.'),
    ('caleb', 'Oh, my leather notebook! Thank you! I was just looking for it.', '¡Oh, mi cuaderno de cuero! ¡Gracias! Justo lo estaba buscando.'),
    ('hannah', 'You left it by the soup cup on the front counter.', 'Lo dejó junto a la taza de sopa en el mostrador de entrada.'),
    ('caleb', 'All my street notes from this week are in here. You saved me.', 'Todas mis notas de calles de esta semana están aquí dentro. Me ha salvado.'),
    ('hannah', 'We are glad you find our courtyard peaceful for your... work.', 'Nos alegra que encuentre nuestro patio tranquilo para su... trabajo.'),
    ('caleb', 'Very peaceful! Though did you hear a funny metal knock just now?', '¡Muy tranquilo! ¿Aunque acaba de oír un golpe de metal curioso ahora mismo?'),
    ('hannah', 'Yes! It sounded like it came from the heating pipe in the corner.', '¡Sí! Sonó como si viniera de la tubería de la calefacción en la esquina.'),
    ('caleb', 'Feel the radiator. The top is warm, while the bottom is turning cool.', 'Toque el radiador. La parte de arriba está caliente, mientras que la de abajo se está enfriando.'),
    ('hannah', 'Oh! Sometimes old pipes have a little air bubble at night.', '¡Oh! A veces las tuberías viejas tienen una pequeña burbuja de aire por la noche.'),
    ('caleb', 'I have a warm blanket, so I am quite comfortable tonight.', 'Tengo una manta abrigada, así que estoy bastante cómodo esta noche.'),
    ('hannah', 'Thank you for being so patient! Graham will check the basement right away.', '¡Gracias por ser tan paciente! Graham revisará el sótano ahora mismo.'),
    ('caleb', 'Good night, Hannah. See you at breakfast.', 'Buenas noches, Hannah. Nos vemos en el desayuno.'),
]
WALK = [
    (0, None, ["'¿Disculpe, Caleb? Siento molestarlo.' Al llamar a una puerta o interrumpir a alguien,", (None, 'Sorry to disturb you'), 'es la fórmula de cortesía más natural.']),
    (1, None, ["'¡Oh, mi cuaderno de cuero! ¡Gracias! Justo lo estaba buscando.' Recuerda que 'buscar' en inglés lleva preposición fija:", (None, 'looking for it'), 'mirando en busca de ello.']),
    (2, None, ["'Lo dejó junto a la taza de sopa en el mostrador de entrada.' Aquí la preposición corta", (None, 'by the soup cup'), "significa 'al lado de' o 'junto a'."]),
    (3, None, ["'Todas mis notas de calles de esta semana están aquí dentro. Me ha salvado.' El giro", (None, 'in here'), "refuerza la idea de 'aquí adentro, entre estas páginas'."]),
    (4, None, ["'Nos alegra que encuentre nuestro patio tranquilo para su... trabajo.' Con", (None, 'you find our courtyard peaceful'), "el verbo 'encontrar' expresa opinión personal sobre cómo resulta un lugar."]),
    (5, None, ["'¡Muy tranquilo! ¿Aunque acaba de oír un golpe de metal curioso ahora mismo?' Fíjate en que", (None, 'funny'), "además de gracioso suele significar 'extraño' o 'raro' con ruidos."]),
    (6, None, ["'¡Sí! Sonó como si viniera de la tubería de la calefacción en la esquina.' Cuando describes a qué se pareció un ruido con una frase completa, usas", (None, 'It sounded like'), 'sonó como si.']),
    (7, None, ["'Toque el radiador. La parte de arriba está caliente, mientras que la de abajo se está enfriando.' Para cambios graduales de temperatura o estado funciona muy bien", (None, 'turning cool'), 'volviéndose frío.']),
    (8, None, ["'¡Oh! A veces las tuberías viejas tienen una pequeña burbuja de aire por la noche.' Mientras decimos 'por la mañana' con 'in', con la noche se cambia a", (None, 'at night'), 'sin artículo.']),
    (9, None, ["'Tengo una manta abrigada, así que estoy bastante cómodo esta noche.' En inglés americano,", (None, 'quite comfortable'), "significa 'bastante o muy cómodo', con tono tranquilizador."]),
    (10, None, ["'¡Gracias por ser tan paciente! Graham revisará el sótano ahora mismo.' De nuevo tras 'for' aparece el verbo en '-ing' en", (None, 'for being so patient'), 'por ser tan paciente.']),
    (11, None, ["'Buenas noches, Hannah. Nos vemos en el desayuno.' Para quedar en una comida del día se usa la preposición puntual:", (None, 'at breakfast'), 'en el desayuno.']),
]
