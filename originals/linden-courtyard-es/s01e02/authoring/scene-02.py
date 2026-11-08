# Authoring module for linden-courtyard-es-s01e02-scene-02.
ID = 'linden-courtyard-es-s01e02-scene-02'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 2
SCENE = 2
TITLE = 'No Milk in the Fridge  (No hay leche en la nevera)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = 'De vuelta en la cocina del café, Tessa abre la nevera y suelta un suspiro justo cuando entran Hannah y el dueño, Arthur. Ocho huéspedes se están despertando arriba y el desayuno empieza en veinte minutos. Escucha primero.'
OPENER = 'Desgranemos ahora la escena línea por línea.'
TRANSITION = 'Escuchemos otra vez toda la escena a velocidad normal.'
OUTRO = 'Con una lista de compras y efectivo de la caja, Hannah sale disparada hacia el mercado de la esquina. La próxima vez veremos con qué regresa.'
CLOSING = ('hannah', 'See you later!')
STORY = [
    ('tessa', 'Oh no! Arthur, Hannah, we have a kitchen emergency!', '¡Oh, no! Arthur, Hannah, ¡tenemos una emergencia en la cocina!'),
    ('arthur', 'Please do not say the word emergency before my morning coffee!', '¡Por favor, no digas la palabra emergencia antes de mi café de la mañana!'),
    ('tessa', 'The dairy van has a flat tire outside town. Look in the fridge!', 'La furgoneta de los lácteos tiene una rueda pinchada a las afueras. ¡Miren en la nevera!'),
    ('hannah', 'One tiny splash of milk, two eggs, and no butter at all!', '¡Un chorrito diminuto de leche, dos huevos y nada de mantequilla!'),
    ('arthur', 'Eight hungry guests will come down the stairs at seven thirty!', '¡Ocho huéspedes hambrientos bajarán las escaleras a las siete y media!'),
    ('tessa', 'My bread is already in the oven, at least.', 'Mi pan ya está en el horno, al menos.'),
    ('hannah', 'Give me a bag and some cash! The corner market opens at seven.', '¡Dame una bolsa y algo de efectivo! El mercado de la esquina abre a las siete.'),
    ('arthur', 'Can you run there and back in ten minutes?', '¿Puedes ir corriendo y volver en diez minutos?'),
    ('hannah', 'Watch me! Tell me exactly what to buy.', '¡Mírame hacerlo! Dime exactamente qué comprar.'),
    ('tessa', 'Three bottles of milk, twenty eggs, butter, cheese, and red apples!', '¡Tres botellas de leche, veinte huevos, mantequilla, queso y manzanas rojas!'),
    ('arthur', 'Here is fifty from the cash box. Bring back the receipt!', 'Aquí tienes cincuenta de la caja. ¡Trae de vuelta el recibo!'),
    ('hannah', 'Hold the fort, I am already out the door!', '¡Cuiden el fuerte, que ya estoy saliendo por la puerta!'),
]
WALK = [
    (0, None, ["'¡Oh, no! Arthur, Hannah, ¡tenemos una emergencia en la cocina!' Al juntar dos sustantivos en", (None, 'kitchen emergency'), 'el primero actúa como adjetivo y describe de qué tipo de urgencia se trata.']),
    (1, None, ["'¡Por favor, no digas la palabra emergencia antes de mi café de la mañana!' Un ruego negativo educado empieza muy limpio con", (None, 'Please do not say'), 'seguido del verbo base.']),
    (2, None, ["'La furgoneta de los lácteos tiene una rueda pinchada a las afueras. ¡Miren en la nevera!' En inglés estadounidense un neumático desinflado se llama", (None, 'a flat tire'), "literalmente 'una llanta plana'."]),
    (3, None, ["'¡Un chorrito diminuto de leche, dos huevos y nada de mantequilla!' Añadir", (None, 'at all'), 'detrás de', (None, 'no butter'), "refuerza la negación: 'nada en absoluto'."]),
    (4, None, ["'¡Ocho huéspedes hambrientos bajarán las escaleras a las siete y media!' En inglés no 'tienes hambre' con el verbo tener, sino que 'estás hambriento' con adjetivo:", (None, 'hungry guests'), 'huéspedes con hambre.']),
    (5, None, ["'Mi pan ya está en el horno, al menos.' Para dar un tono de consuelo al final de la frase, se añade", (None, 'at least'), "que es la forma inglesa de decir 'al menos'."]),
    (6, None, ["'¡Dame una bolsa y algo de efectivo! El mercado de la esquina abre a las siete.' Para dinero en billetes o monedas usamos el incontable", (None, 'some cash'), 'nunca en plural.']),
    (7, None, ["'¿Puedes ir corriendo y volver en diez minutos?' El par", (None, 'there and back'), "resume de maravilla 'ida y vuelta' en solo tres palabras cortas."]),
    (8, None, ["'¡Mírame hacerlo! Dime exactamente qué comprar.' Cuando aceptas un reto con confianza,", (None, 'Watch me'), 'suena vivaz, y', (None, 'what to buy'), "une interrogativo con infinitivo igual que 'qué comprar'."]),
    (9, None, ["'¡Tres botellas de leche, veinte huevos, mantequilla, queso y manzanas rojas!' Como la leche es incontable en inglés, la medimos con un envase en", (None, 'Three bottles of milk'), 'mientras que huevos y manzanas van directo en plural.']),
    (10, None, ["'Aquí tienes cincuenta de la caja. ¡Trae de vuelta el recibo!' El verbo con partícula", (None, 'Bring back'), "expresa 'traer de vuelta' al regresar."]),
    (11, None, ["'¡Cuiden el fuerte, que ya estoy saliendo por la puerta!' El modismo cotidiano", (None, 'Hold the fort'), 'pide que se encarguen de todo mientras tú sales un momento.']),
]
