# Authoring module for linden-courtyard-es-s01e02-scene-03.
ID = 'linden-courtyard-es-s01e02-scene-03'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = 'Counting the Change  (Contando el cambio)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'hannah': 'Hannah', 'arthur': 'Arthur', 'tessa': 'Tessa'}
INTRO = 'Nueve minutos más tarde, Hannah irrumpe de nuevo por la reja del patio cargando dos pesadas bolsas de tela llenas de compras para Tessa y Arthur. Escucha primero la escena.'
OPENER = 'Ahora analicemos cada frase despacio.'
TRANSITION = 'Volvamos a escuchar la escena entera del tirón.'
OUTRO = 'Un paquete equivocado de mantequilla con sal casi provoca una crisis con la mermelada, hasta que Tessa lo convirtió en el ingrediente estrella de los huevos revueltos. Hasta pronto.'
CLOSING = ('tessa', 'Bye for now!')
STORY = [
    ('hannah', 'Nine minutes! Here are the milk, the eggs, and the apples!', '¡Nueve minutos! ¡Aquí están la leche, los huevos y las manzanas!'),
    ('tessa', 'You are a hero, Hannah! Give me the milk first for the coffee machine.', '¡Eres una heroína, Hannah! Dame primero la leche para la cafetera.'),
    ('arthur', 'Impressive speed! Did the shopkeeper give you a receipt?', '¡Qué velocidad tan impresionante! ¿El tendero te dio recibo?'),
    ('hannah', 'Right here! Everything cost thirty-eight, so here is twelve in change.', '¡Aquí mismo! Todo costó treinta y ocho, así que aquí hay doce de cambio.'),
    ('arthur', 'Ten, eleven, twelve. Exact to the last coin, thank you!', 'Diez, once, doce. Exacto hasta la última moneda, ¡gracias!'),
    ('tessa', 'Wait a second, Hannah... which pack of butter did you grab?', 'Espera un segundo, Hannah... ¿qué paquete de mantequilla agarraste?'),
    ('hannah', 'The gold wrapper on the top shelf. Why?', 'El del envoltorio dorado en el estante de arriba. ¿Por qué?'),
    ('tessa', 'That is extra salty sea butter! My sweet jam rolls need plain butter!', '¡Esa es mantequilla marina extrasalada! ¡Mis panecillos dulces con mermelada necesitan mantequilla sin sal!'),
    ('hannah', 'Oh no! All the wrappers looked the same when I was running!', '¡Oh, no! ¡Todos los envoltorios se veían iguales mientras iba corriendo!'),
    ('arthur', 'Can we serve salty butter with sweet strawberry jam?', '¿Podemos servir mantequilla salada con mermelada dulce de fresa?'),
    ('tessa', 'Wait, salty butter is terrible for jam, but amazing for scrambled eggs!', '¡Espera, la mantequilla salada es terrible para la mermelada, pero increíble para los huevos revueltos!'),
    ('hannah', 'Phew! Quick thinking saves breakfast again.', '¡Uf! Pensar rápido salva el desayuno otra vez.'),
]
WALK = [
    (0, None, ["'¡Nueve minutos! ¡Aquí están la leche, los huevos y las manzanas!' Como enumera varios productos juntos, Hannah presenta la compra en plural con", (None, 'Here are'), 'aquí están.']),
    (1, None, ["'¡Eres una heroína, Hannah! Dame primero la leche para la cafetera.' En el inglés actual,", (None, 'a hero'), 'se usa muchísimo tanto para hombres como para mujeres en tono entusiasta.']),
    (2, None, ["'¡Qué velocidad tan impresionante! ¿El tendero te dio recibo?' Fíjate en el orden de doble objeto en", (None, 'give you a receipt'), 'donde la persona va antes que la cosa entregada, sin preposición.']),
    (3, None, ["'¡Aquí mismo! Todo costó treinta y ocho, así que aquí hay doce de cambio.' Ojo al verbo irregular", (None, 'cost'), 'que suena idéntico en presente y en pasado, mientras que', (None, 'in change'), "significa 'de vuelta'."]),
    (4, None, ["'Diez, once, doce. Exacto hasta la última moneda, ¡gracias!' La frase", (None, 'to the last coin'), 'celebra que las cuentas cuadran al céntimo.']),
    (5, None, ["'Espera un segundo, Hannah... ¿qué paquete de mantequilla agarraste?' Cuando eliges entre opciones concretas de un mismo producto en el estante, el interrogativo preciso es", (None, 'which pack'), '¿cuál paquete?']),
    (6, None, ["'El del envoltorio dorado en el estante de arriba. ¿Por qué?' Con superficies y repisas el inglés usa siempre", (None, 'on the top shelf'), 'sobre el estante superior.']),
    (7, None, ["'¡Esa es mantequilla marina extrasalada! ¡Mis panecillos dulces con mermelada necesitan mantequilla sin sal!' Para comida sencilla, natural o sin condimento añadido, la expresión clave es", (None, 'plain butter'), 'mantequilla normal sin sal.']),
    (8, None, ["'¡Oh, no! ¡Todos los envoltorios se veían iguales mientras iba corriendo!' La expresión fija", (None, 'looked the same'), "lleva siempre artículo definido en medio para decir 'se veían iguales'."]),
    (9, None, ["'¿Podemos servir mantequilla salada con mermelada dulce de fresa?' Con verbos modales basta invertir las dos primeras palabras en", (None, 'Can we serve'), 'para preguntar qué opción es posible.']),
    (10, None, ["'¡Espera, la mantequilla salada es terrible para la mermelada, pero increíble para los huevos revueltos!' El desayuno clásico de", (None, 'scrambled eggs'), 'toma su nombre del verbo revolver y mezclar en la sartén.']),
    (11, None, ["'¡Uf! Pensar rápido salva el desayuno otra vez.' La interjección", (None, 'Phew'), 'imita el suspiro de alivio, y', (None, 'Quick thinking'), 'convierte el verbo en sustantivo: rapidez mental.']),
]
