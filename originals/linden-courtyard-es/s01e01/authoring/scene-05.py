# Authoring module for linden-courtyard-es-s01e01-scene-05.
ID = 'linden-courtyard-es-s01e01-scene-05'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = 'Not My Clothes!  (¡No es mi ropa!)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'evelyn': 'Evelyn', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Dos minutos después de subir, el zumbador de la habitación cuatro suena en el mostrador: no dos veces, sino cuatro seguidas. Hannah sube corriendo y encuentra a Evelyn y a Graham mirando la maleta abierta. Escucha primero.'
OPENER = 'Veamos despacio qué acaba de pasar línea por línea.'
TRANSITION = 'Volvamos a oír toda la escena a ritmo normal.'
OUTRO = 'En vez de vestidos y partituras, la maleta azul guarda zapatos marrones grandes y un trencito de madera. La próxima vez veremos qué dice esa etiqueta.'
CLOSING = ('hannah', 'Goodbye!')
STORY = [
    ('hannah', 'Miss Evelyn, is everything all right? You rang the bell!', 'Señorita Evelyn, ¿está todo bien? ¡Usted tocó el timbre!'),
    ('evelyn', 'Look inside this suitcase, Hannah! This is not my bag!', '¡Mira dentro de esta maleta, Hannah! ¡Esta no es mi maleta!'),
    ('hannah', 'Wait, it is dark blue, just like yours!', '¡Espera, es azul oscuro, igualita a la tuya!'),
    ('evelyn', 'The outside is identical, yes! But look inside!', '¡Por fuera es idéntica, sí! ¡Pero mira adentro!'),
    ('graham', "Two pairs of big brown men's shoes and gray sweaters.", 'Dos pares de zapatos marrones grandes de hombre y suéteres grises.'),
    ('hannah', 'And what is this wrapped in white paper? A little wooden train!', '¿Y qué es esto envuelto en papel blanco? ¡Un trencito de madera!'),
    ('evelyn', 'I certainly do not wear size eleven shoes!', '¡Desde luego yo no uso zapatos de la talla once!'),
    ('graham', 'No wonder it was so heavy. Wood and leather!', 'Con razón pesaba tanto. ¡Madera y cuero!'),
    ('evelyn', 'Someone at the train station took my blue suitcase by mistake!', '¡Alguien en la estación de tren se llevó mi maleta azul por error!'),
    ('hannah', "Please sit down, ma'am. Do not worry, we will check the tag right now.", 'Siéntese, por favor, señora. No se preocupe, revisaremos la etiqueta ahora mismo.'),
    ('graham', 'There is a small paper card tied to the side handle.', 'Hay una tarjetita de papel atada al asa lateral.'),
    ('evelyn', 'Oh, let us bring it downstairs to the light!', '¡Ay, bajémosla a donde haya buena luz!'),
]
WALK = [
    (0, None, ["'Señorita Evelyn, ¿está todo bien? ¡Usted tocó el timbre!' Combinar", (None, 'Miss Evelyn'), 'con el nombre de pila suena cálido y respetuoso, y', (None, 'rang'), 'es el pasado irregular del verbo sonar o tocar el timbre.']),
    (1, None, ["'¡Mira dentro de esta maleta, Hannah! ¡Esta no es mi maleta!' Para negar con el verbo ser basta colocar", (None, 'This is not'), 'al inicio, sin cambiar el resto de la frase.']),
    (2, None, ["'¡Espera, es azul oscuro, igualita a la tuya!' El pronombre independiente", (None, 'yours'), "significa 'la tuya' o 'la suya' sin tener que repetir la palabra 'maleta'."]),
    (3, None, ["'¡Por fuera es idéntica, sí! ¡Pero mira adentro!' Observa el contraste limpio entre", (None, 'The outside'), 'para el exterior del equipaje y', (None, 'inside'), 'para el interior.']),
    (4, None, ["'Dos pares de zapatos marrones grandes de hombre y suéteres grises.' Incluso cuando un plural es irregular y cambia su vocal interna, toma apóstrofo y ese para indicar pertenencia en", (None, "men's shoes"), 'zapatos de hombre.']),
    (5, None, ["'¿Y qué es esto envuelto en papel blanco? ¡Un trencito de madera!' Para describir de qué material está hecho el juguete, el sustantivo madera suma sufijo adjetivo en", (None, 'wooden train'), 'tren de madera.']),
    (6, None, ["'¡Desde luego yo no uso zapatos de la talla once!' Con ropa, calzado o gafas que llevas encima, el inglés emplea siempre", (None, 'wear'), 'para vestir o calzar.']),
    (7, None, ["'Con razón pesaba tanto. ¡Madera y cuero!' La expresión inicial", (None, 'No wonder'), "traduce al pie de la letra nuestro 'con razón' o 'no me extraña'."]),
    (8, None, ["'¡Alguien en la estación de tren se llevó mi maleta azul por error!' El bloque final", (None, 'by mistake'), "es la forma estándar de decir 'por equivocación' o 'sin querer'."]),
    (9, None, ["'Siéntese, por favor, señora. No se preocupe, revisaremos la etiqueta ahora mismo.' Tranquilizar a alguien es tan fácil como decir", (None, 'Do not worry'), 'seguido de lo que vas a hacer para ayudar.']),
    (10, None, ["'Hay una tarjetita de papel atada al asa lateral.' Para decir 'hay' con una sola cosa, el inglés arranca en singular con", (None, 'There is'), 'mientras que con varias pasa al plural.']),
    (11, None, ["'¡Ay, bajémosla a donde haya buena luz!' Las propuestas conjuntas en primera persona plural se abren con", (None, 'let us bring it downstairs'), "donde la última palabra ya significa 'al piso de abajo'."]),
]
