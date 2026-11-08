# Authoring module for linden-courtyard-es-s01e05-scene-08.
ID = 'linden-courtyard-es-s01e05-scene-08'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 5
SCENE = 8
TITLE = 'The Red-Stamped Letter  (La carta del sello rojo)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = 'Tras dejar pasar a Owen al patio para dar intimidad a los dos hermanos, Hannah entra sin hacer ruido a la recepción, donde Tessa mira con ternura y Arthur abre el sobre certificado. Escuchemos primero.'
OPENER = 'Repasemos con calma esta última escena del episodio cinco.'
TRANSITION = 'Volvamos a oír la escena completa de corrido.'
OUTRO = 'Afuera bajo el árbol dos hermanos distanciados por fin se sientan juntos, mientras adentro un aviso de venta comercial amenaza toda la posada en treinta días. Episodio cinco terminado; te esperamos en el gran final de temporada.'
CLOSING = ('arthur', 'Bye for now!')
STORY = [
    ('tessa', 'Hannah, look through the glass. They are standing face to face under the tree!', 'Hannah, mira a través del cristal. ¡Están de pie cara a cara bajo el árbol!'),
    ('hannah', 'Neither of them walked away! Caleb is pointing at the two chairs right now!', '¡Ninguno de los dos se marchó! ¡Caleb está señalando las dos sillas ahora mismo!'),
    ('arthur', 'Wonderful... let me just glance at this landlord letter while we wait.', 'Qué maravilla... déjenme echar un vistazo rápido a esta carta del propietario mientras esperamos.'),
    ('tessa', 'Probably a boring notice about painting the street shutters.', 'Probablemente un aviso aburrido sobre pintar los postigos de la calle.'),
    ('arthur', 'Oh... oh no. Where is my chair? My knees feel weak.', 'Oh... oh, no. ¿Dónde está mi silla? Siento flojas las rodillas.'),
    ('hannah', 'Arthur! Your face went completely white! Sit down, what does the letter say?', '¡Arthur! ¡Se te puso la cara completamente blanca! Siéntate, ¿qué dice la carta?'),
    ('arthur', 'Read the top line for me, Hannah. Tell me my glasses are playing tricks again!', 'Léeme la primera línea, Hannah. ¡Dime que mis gafas me están gastando bromas otra vez!'),
    ('hannah', "'Notice of Property Transfer: Number Eight Courtyard Building offered for commercial office sale.'", "'Aviso de transferencia de propiedad: Edificio del Patio Número Ocho ofrecido en venta para oficinas comerciales.'"),
    ('tessa', 'Commercial office sale?! Turn our guesthouse and kitchen into gray offices?!', '¡¿Venta para oficinas comerciales?! ¡¿Convertir nuestra posada y cocina en oficinas grises?!'),
    ('arthur', 'They give us thirty days before new buyers inspect the building!', '¡Nos dan treinta días antes de que los nuevos compradores inspeccionen el edificio!'),
    ('hannah', 'Wait, there is a second folded page clipped to the back of this notice...', 'Esperen, hay una segunda hoja doblada sujeta con un clip detrás de este aviso...'),
    ('arthur', 'Not a word to anyone outside yet! Let the two brothers have their Friday afternoon first!', '¡Ni una palabra a nadie afuera todavía! ¡Dejemos que los dos hermanos tengan primero su tarde de viernes!'),
]
WALK = [
    (0, None, ["'Hannah, mira a través del cristal. ¡Están de pie cara a cara bajo el árbol!' Idéntico en imagen a nuestro idioma,", (None, 'face to face'), 'significa cara a cara.']),
    (1, None, ["'¡Ninguno de los dos se marchó! ¡Caleb está señalando las dos sillas ahora mismo!' Con pronombre detrás añadimos 'of':", (None, 'Neither of them'), 'ninguno de los dos, con el verbo en afirmativo.']),
    (2, None, ["'Qué maravilla... déjenme echar un vistazo rápido a esta carta del propietario mientras esperamos.' El verbo", (None, 'glance at'), 'significa echar una mirada rápida y superficial.']),
    (3, None, ["'Probablemente un aviso aburrido sobre pintar los postigos de la calle.' De nuevo, después de 'about', el verbo aparece con '-ing':", (None, 'about painting'), 'sobre pintar.']),
    (4, None, ["'Oh... oh, no. ¿Dónde está mi silla? Siento flojas las rodillas.' Con partes del cuerpo como sujeto,", (None, 'My knees feel weak'), 'describe al instante el mareo de un susto.']),
    (5, None, ["'¡Arthur! ¡Se te puso la cara completamente blanca! Siéntate, ¿qué dice la carta?' Para cambios bruscos de color, el inglés emplea 'go' en pasado:", (None, 'went completely white'), 'se quedó blanca.']),
    (6, None, ["'Léeme la primera línea, Hannah. ¡Dime que mis gafas me están gastando bromas otra vez!' El modismo", (None, 'playing tricks'), 'describe cuando la vista o la memoria nos engaña.']),
    (7, None, ["'Aviso de transferencia de propiedad: Edificio del Patio Número Ocho ofrecido en venta para oficinas comerciales.' En lenguaje inmobiliario,", (None, 'for commercial office sale'), 'resume el destino empresarial del inmueble.']),
    (8, None, ["'¡¿Venta para oficinas comerciales?! ¡¿Convertir nuestra posada y cocina en oficinas grises?!' Para transformar una cosa en otra completamente distinta se usa", (None, 'Turn our guesthouse and kitchen into'), 'convertir en.']),
    (9, None, ["'¡Nos dan treinta días antes de que los nuevos compradores inspeccionen el edificio!' También tras 'before' referido al futuro basta el presente simple:", (None, 'before new buyers inspect'), 'antes de que inspeccionen.']),
    (10, None, ["'Esperen, hay una segunda hoja doblada sujeta con un clip detrás de este aviso...' El participio", (None, 'clipped to the back'), "convierte el sustantivo 'clip' en verbo: sujeta con un clip."]),
    (11, None, ["'¡Ni una palabra a nadie afuera todavía! ¡Dejemos que los dos hermanos tengan primero su tarde de viernes!' La orden elíptica", (None, 'Not a word to anyone'), 'pide guardar silencio absoluto por ahora.']),
]
