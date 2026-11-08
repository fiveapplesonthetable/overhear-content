# Authoring module for linden-courtyard-es-s01e05-scene-05.
ID = 'linden-courtyard-es-s01e05-scene-05'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 5
SCENE = 5
TITLE = 'Simple Words First  (Primero palabras sencillas)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = 'Veinte minutos antes del mediodía, Caleb camina de un lado a otro sobre las piedras del patio con una hoja arrugada en la mano mientras Hannah se acerca con un vaso de agua. Escucha primero.'
OPENER = 'Repasemos cada frase con tranquilidad.'
TRANSITION = 'Volvamos a oír la escena completa a velocidad natural.'
OUTRO = 'Nada de discursos de diecinueve puntos: solo gracias por venir, te eché de menos, y siéntate a tomar té y pastel de limón. Quedan diez minutos para las doce. Hasta la próxima.'
CLOSING = ('caleb', 'Take care!')
STORY = [
    ('hannah', 'Here, drink a sip of cool water, Caleb. What is on that paper?', 'Toma, bebe un sorbo de agua fresca, Caleb. ¿Qué hay en ese papel?'),
    ('caleb', 'A five minute speech explaining nineteen reasons why we were both wrong in April.', 'Un discurso de cinco minutos explicando diecinueve razones por las que ambos nos equivocamos en abril.'),
    ('hannah', 'Nineteen reasons?! Are you welcoming your brother or reading a train schedule?', '¡¿Diecinueve razones?! ¿Vas a darle la bienvenida a tu hermano o a leer un horario de trenes?'),
    ('caleb', 'When I get nervous, my sentences grow very long and formal!', '¡Cuando me pongo nervioso, mis frases se vuelven muy largas y formales!'),
    ('hannah', 'Fold that paper and put it in your pocket right now.', 'Dobla ese papel y mételo en tu bolsillo ahora mismo.'),
    ('caleb', 'Without my notes, what do I say when he walks through that gate?', 'Sin mis notas, ¿qué digo cuando él cruce esa verja?'),
    ('hannah', "Start with three short sentences. First: 'Hello, Owen, thank you for coming.'", "Empieza con tres frases cortas. Primera: 'Hola, Owen, gracias por venir.'"),
    ('caleb', "'Hello, Owen, thank you for coming.' Okay, I can remember that.", "'Hola, Owen, gracias por venir.' Vale, puedo recordar eso."),
    ('hannah', "Second: 'I missed you these three years.'", "Segunda: 'Te eché de menos estos tres años.'"),
    ('caleb', "'I missed you these three years.' Honest and clear. And third?", "'Te eché de menos estos tres años.' Sincero y claro. ¿Y la tercera?"),
    ('hannah', "'Sit down, there is hot tea and Friday lemon cake.'", "'Siéntate, hay té caliente y pastel de limón de los viernes.'"),
    ('caleb', 'Tea and lemon cake! Hannah, you should open a school for nervous brothers.', '¡Té y pastel de limón! Hannah, deberías abrir una escuela para hermanos nerviosos.'),
]
WALK = [
    (0, None, ["'Toma, bebe un sorbo de agua fresca, Caleb. ¿Qué hay en ese papel?' Para lo escrito sobre una hoja el inglés dice siempre", (None, 'on that paper'), 'sobre ese papel.']),
    (1, None, ["'Un discurso de cinco minutos explicando diecinueve razones por las que ambos nos equivocamos en abril.' Cuando una medida va delante del sustantivo pierde el plural:", (None, 'five minute speech'), 'discurso de cinco minutos.']),
    (2, None, ["'¡¿Diecinueve razones?! ¿Vas a darle la bienvenida a tu hermano o a leer un horario de trenes?' Con un solo auxiliar al principio,", (None, 'Are you welcoming'), "abarca también a 'reading' después de 'or'."]),
    (3, None, ["'¡Cuando me pongo nervioso, mis frases se vuelven muy largas y formales!' Dos verbos de cambio muy útiles en la misma línea:", (None, 'get nervous'), 'ponerse nervioso, y', (None, 'grow very long'), 'hacerse muy largas.']),
    (4, None, ["'Dobla ese papel y mételo en tu bolsillo ahora mismo.' Dos imperativos claros y directos,", (None, 'Fold that paper'), "seguido de 'put it in your pocket'."]),
    (5, None, ["'Sin mis notas, ¿qué digo cuando él cruce esa verja?' En cláusulas temporales con 'when', el inglés usa presente simple,", (None, 'when he walks through'), 'igual que para atravesar un portón.']),
    (6, None, ["'Empieza con tres frases cortas. Primera: Hola, Owen, gracias por venir.' Agradecer que alguien haya acudido es tan sencillo como", (None, 'thank you for coming'), "con '-ing'."]),
    (7, None, ["'Hola, Owen, gracias por venir. Vale, puedo recordar eso.' Con el modal 'can' el verbo va limpio sin 'to':", (None, 'I can remember that'), 'puedo recordar eso.']),
    (8, None, ["'Segunda: Te eché de menos estos tres años.' Donde el español necesita cuatro palabras para 'te eché de menos', el inglés lo dice en tres:", (None, 'I missed you'), 'directo y sincero.']),
    (9, None, ["'Te eché de menos estos tres años. Sincero y claro. ¿Y la tercera?' Con dos palabras,", (None, 'And third'), "pide el tercer punto de la lista sin repetir 'sentence'."]),
    (10, None, ["'Siéntate, hay té caliente y pastel de limón de los viernes.' Añadir 'down' a sentarse en", (None, 'Sit down'), 'suena hospitalario y natural cuando invitas a alguien a la mesa.']),
    (11, None, ["'¡Té y pastel de limón! Hannah, deberías abrir una escuela para hermanos nerviosos.' Para dar una recomendación afectuosa o en broma se usa", (None, 'you should open'), 'deberías abrir.']),
]
