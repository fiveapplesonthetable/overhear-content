# Authoring module for linden-courtyard-es-s01e06-scene-05.
ID = 'linden-courtyard-es-s01e06-scene-05'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 6
SCENE = 5
TITLE = 'Page Two, Clause Fourteen  (Página dos, cláusula catorce)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'arthur': 'Arthur', 'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = 'En la recepción, Arthur le entrega el aviso de dos páginas a Caleb mientras Hannah contiene el aliento junto al libro de reservas. Caleb pasa de inmediato a la segunda hoja. Escucha primero.'
OPENER = 'Vamos a repasar cada frase de este descubrimiento.'
TRANSITION = 'Escuchemos otra vez toda la escena seguida.'
OUTRO = 'La página dos lo cambió todo: abrir las cuatro mesas del desayuno a los vecinos del barrio protege la posada durante diez años más. En la próxima escena, Arthur tiene dos grandes anuncios en la cafetería.'
CLOSING = ('hannah', 'Take care!')
STORY = [
    ('arthur', "Look at page one, Caleb: 'commercial office conversion next month.' We are finished!", "Mira la página uno, Caleb: 'conversión a oficinas comerciales el mes que viene'. ¡Estamos acabados!"),
    ('caleb', 'Wait a moment, sir. Did you read page two clipped underneath?', 'Espere un momento, señor. ¿Leyó la página dos sujeta con clip debajo?'),
    ('arthur', 'Only small gray numbers! My heart stopped at page one!', '¡Solo números grises pequeños! ¡Se me paró el corazón en la página uno!'),
    ('hannah', 'Look where Caleb is pointing with his pencil, Arthur!', '¡Mira adónde está señalando Caleb con su lápiz, Arthur!'),
    ('caleb', 'Clause fourteen of the Portland Old Quarter Act, and my brother here just nodded!', 'Cláusula catorce de la Ley del Barrio Antiguo de Portland, ¡y mi hermano aquí acaba de asentir!'),
    ('arthur', 'In plain words, please! What does Clause fourteen say?', '¡En palabras llanas, por favor! ¿Qué dice la cláusula catorce?'),
    ('caleb', 'No courtyard building over eighty years old may become private offices if the first floor serves neighbors daily.', 'Ningún edificio con patio de más de ochenta años puede convertirse en oficinas privadas si la planta baja atiende a los vecinos a diario.'),
    ('hannah', "'Serves neighbors daily'... like a public morning cafe?!", "'Atiende a los vecinos a diario'... ¡¿como una cafetería pública de mañana?!"),
    ('caleb', 'Exactly! Right now your four tables only serve overnight hotel guests.', '¡Exacto! Ahora mismo sus cuatro mesas solo atienden a huéspedes alojados en el hotel.'),
    ('arthur', 'Wait, if we open our courtyard gate every morning for neighborhood coffee and bread...', 'Espera, si abrimos la verja de nuestro patio cada mañana para café y pan del barrio...'),
    ('caleb', 'Then your guesthouse lease is protected for another ten years by city law!', '¡Entonces el contrato de su posada queda protegido otros diez años por la ley municipal!'),
    ('hannah', 'Arthur! Your glasses just fell off your nose for a happy reason!', '¡Arthur! ¡Se te acaban de caer las gafas de la nariz por un motivo feliz!'),
]
WALK = [
    (0, None, ["'Mira la página uno, Caleb: conversión a oficinas comerciales el mes que viene. ¡Estamos acabados!' Para un desastre que parece definitivo, el inglés dice", (None, 'We are finished'), 'estamos acabados.']),
    (1, None, ["'Espere un momento, señor. ¿Leyó la página dos sujeta con clip debajo?' Con páginas numeradas no se usa artículo:", (None, 'read page two'), 'leíste la página dos.']),
    (2, None, ["'¡Solo números grises pequeños! ¡Se me paró el corazón en la página uno!' La hipérbole simpática", (None, 'My heart stopped'), 'cuenta el susto con mucho humor.']),
    (3, None, ["'¡Mira adónde está señalando Caleb con su lápiz, Arthur!' En cláusulas con 'where' dentro de otra oración se mantiene el orden normal:", (None, 'where Caleb is pointing'), 'adónde señala Caleb.']),
    (4, None, ["'Cláusula catorce de la Ley del Barrio Antiguo de Portland, ¡y mi hermano aquí acaba de asentir!' 'Asentir con la cabeza' en inglés es un solo verbo:", (None, 'nodded'), "y con 'just' delante significa que lo acaba de hacer."]),
    (5, None, ["'¡En palabras llanas, por favor! ¿Qué dice la cláusula catorce?' Cuando alguien cita leyes o tecnicismos, pide claridad con", (None, 'In plain words'), 'en palabras sencillas.']),
    (6, None, ["'Ningún edificio con patio de más de ochenta años puede convertirse en oficinas privadas si la planta baja atiende a los vecinos a diario.' Aquí el modal formal", (None, 'may become'), 'expresa lo que la ley permite o prohíbe.']),
    (7, None, ["'Atiende a los vecinos a diario... ¡¿como una cafetería pública de mañana?!' Para poner un ejemplo concreto se introduce con", (None, 'like a public morning cafe'), "igual que nuestro 'como'."]),
    (8, None, ["'¡Exacto! Ahora mismo sus cuatro mesas solo atienden a huéspedes alojados en el hotel!' Como adjetivo delante del nombre,", (None, 'overnight hotel guests'), 'significa huéspedes que pasan la noche.']),
    (9, None, ["'Espera, si abrimos la verja de nuestro patio cada mañana para café y pan del barrio...' En condicionales reales sobre planes posibles empieza con presente simple:", (None, 'if we open'), 'si abrimos.']),
    (10, None, ["'¡Entonces el contrato de su posada queda protegido otros diez años por la ley municipal!' Aunque 'ten years' sea plural, 'another' trata el bloque completo como una unidad:", (None, 'another ten years'), 'otros diez años.']),
    (11, None, ["'¡Arthur! ¡Se te acaban de caer las gafas de la nariz por un motivo feliz!' El verbo con preposición", (None, 'fell off your nose'), 'describe algo que se desprende y cae de una superficie.']),
]
