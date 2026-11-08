# Authoring module for linden-courtyard-es-s01e04-scene-08.
ID = 'linden-courtyard-es-s01e04-scene-08'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 4
SCENE = 8
TITLE = 'The Boy on the Stairs  (El niño en la escalera)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'evelyn': 'Evelyn', 'hannah': 'Hannah', 'caleb': 'Caleb'}
INTRO = 'Al salir al patio bañado de sol, la señorita Evelyn le cuenta más a Hannah sobre los dos hermanos del número doce, sin saber que Caleb acaba de bajar por la escalera exterior detrás de ellas. Escuchemos primero.'
OPENER = 'Repasemos con calma esta emotiva escena final del episodio.'
TRANSITION = 'Volvamos a escuchar toda la escena de principio a fin.'
OUTRO = '¡Qué momento en el patio! El pequeño Caleb del tercer escalón está justo delante de su profesora de piano de la infancia, y es el dueño de la maleta misteriosa. Episodio cuatro completado; nos vemos en el cinco.'
CLOSING = ('caleb', 'Goodbye!')
STORY = [
    ('hannah', 'Tell me more about the two boys on Linden Street, Miss Evelyn!', '¡Cuénteme más sobre los dos niños de la calle Linden, señorita Evelyn!'),
    ('evelyn', 'The older brother was bold and loud, always rushing through his music scales.', 'El hermano mayor era atrevido y ruidoso, siempre corriendo en sus escalas musicales.'),
    ('hannah', 'And the younger brother with the wooden train?', '¿Y el hermano menor, el del tren de madera?'),
    ('evelyn', 'Quiet as a mouse! He sat on the third stair listening to every single note.', '¡Callado como un ratón! Se sentaba en el tercer escalón escuchando cada nota.'),
    ('hannah', 'Listening to the sound of the room... wait a second!', 'Escuchando el sonido de la habitación... ¡espera un segundo!'),
    ('evelyn', 'Whenever I finished playing, he asked why the piano sounded warmer when it rained.', 'Siempre que yo terminaba de tocar, él preguntaba por qué el piano sonaba más cálido cuando llovía.'),
    ('caleb', 'Because wet wooden shutters soften the echo from the stone street...', 'Porque los postigos de madera mojados suavizan el eco de la calle de piedra...'),
    ('hannah', 'Caleb! Were you standing right there?!', '¡Caleb! ¡¿Estaba usted parado justo ahí?!'),
    ('evelyn', 'Good heavens... look at your eyes! Little Caleb from the third stair?!', 'Santo cielo... ¡mira tus ojos! ¡¿El pequeño Caleb del tercer escalón?!'),
    ('caleb', "Miss Evelyn?! My brother's Friday piano teacher?!", '¡¿Señorita Evelyn?! ¡¿La profesora de piano de los viernes de mi hermano?!'),
    ('hannah', 'Wait, then Monday night on our step... the second blue suitcase...', 'Espere, entonces el lunes por la noche en nuestro escalón... la segunda maleta azul...'),
    ('caleb', 'Yes, Hannah. That blue suitcase is mine, and I owe you both the whole truth.', 'Sí, Hannah. Esa maleta azul es mía, y les debo a las dos toda la verdad.'),
]
WALK = [
    (0, None, ["'¡Cuénteme más sobre los dos niños de la calle Linden, señorita Evelyn!' Con nombres de calles el inglés usa la preposición 'on':", (None, 'on Linden Street'), 'en la calle Linden.']),
    (1, None, ["'El hermano mayor era atrevido y ruidoso, siempre corriendo en sus escalas musicales.' El giro", (None, 'rushing through'), 'describe pasar a toda prisa por una tarea sin detenerse.']),
    (2, None, ["'¿Y el hermano menor, el del tren de madera?' Los comparativos familiares son esenciales:", (None, 'younger brother'), "hermano menor, frente a 'older brother'."]),
    (3, None, ["'¡Callado como un ratón! Se sentaba en el tercer escalón escuchando cada nota.' El modismo tradicional", (None, 'Quiet as a mouse'), 'retrata a alguien tan silencioso que apenas se nota su presencia.']),
    (4, None, ["'Escuchando el sonido de la habitación... ¡espera un segundo!' Para pedir una pausa súbita porque acabas de atar cabos, di", (None, 'wait a second'), '¡espera un segundo!']),
    (5, None, ["'Siempre que yo terminaba de tocar, él preguntaba por qué el piano sonaba más cálido cuando llovía.' Dos puntos clave:", (None, 'Whenever'), "significa 'cada vez que', y tras 'finished' va siempre '-ing':", (None, 'finished playing'), 'terminaba de tocar.']),
    (6, None, ["'Porque los postigos de madera mojados suavizan el eco de la calle de piedra...' Añadir '-en' a un adjetivo crea el verbo correspondiente, como oyes en", (None, 'soften the echo'), 'suavizan el eco.']),
    (7, None, ["'¡Caleb! ¡¿Estaba usted parado justo ahí?!' El pasado continuo en pregunta invierte el verbo:", (None, 'Were you standing'), '¿estabas ahí de pie?']),
    (8, None, ["'Santo cielo... ¡mira tus ojos! ¡¿El pequeño Caleb del tercer escalón?!' La exclamación suave", (None, 'Good heavens'), 'expresa asombro afectuoso sin sonar brusca.']),
    (9, None, ["'¡¿Señorita Evelyn?! ¡¿La profesora de piano de los viernes de mi hermano?!' Mira cómo el posesivo con apóstrofo encadena la relación en", (None, "My brother's Friday piano teacher"), 'de atrás hacia delante.']),
    (10, None, ["'Espere, entonces el lunes por la noche en nuestro escalón... la segunda maleta azul...' Para unir día y parte del día basta juntarlos sin preposición intermedia:", (None, 'Monday night'), 'el lunes por la noche.']),
    (11, None, ["'Sí, Hannah. Esa maleta azul es mía, y les debo a las dos toda la verdad.' Cuando el sustantivo ya no se repite, el posesivo cambia a la forma independiente:", (None, 'is mine'), 'es mía.']),
]
