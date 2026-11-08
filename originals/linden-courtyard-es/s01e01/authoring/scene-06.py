# Authoring module for linden-courtyard-es-s01e01-scene-06.
ID = 'linden-courtyard-es-s01e01-scene-06'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = 'The Luggage Tag  (La etiqueta del equipaje)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'arthur': 'Arthur'}
INTRO = 'De vuelta en recepción, Hannah, Evelyn y el dueño, Arthur, se inclinan sobre la maleta azul bajo la lámpara del mostrador. Por fin Arthur les da buen uso a sus gafas. Escucha primero la escena.'
OPENER = 'Revisemos ahora cada frase con tranquilidad.'
TRANSITION = 'Escuchemos de nuevo la conversación entera a paso normal.'
OUTRO = 'Todavía no hay noticias en la estación, y el misterioso dueño vive a solo cinco minutos de allí. En la próxima escena, Tessa interviene para salvar la tarde de Evelyn.'
CLOSING = ('arthur', 'See you soon!')
STORY = [
    ('arthur', 'Dear me, what a mix-up! Let me look at the tag with my glasses.', '¡Vaya por Dios, qué confusión! Déjeme mirar la etiqueta con mis gafas.'),
    ('evelyn', 'Is there a name or a phone number on it?', '¿Hay algún nombre o número de teléfono en ella?'),
    ('arthur', 'No phone number, unfortunately. Only two initials and an old street name.', 'Ningún número de teléfono, por desgracia. Solo dos iniciales y el nombre de una calle antigua.'),
    ('hannah', 'Wait, that street is right here in our neighborhood, five minutes away!', '¡Espera, esa calle está aquí mismo en nuestro barrio, a cinco minutos!'),
    ('evelyn', 'How strange! We rode the same morning train to the same district.', '¡Qué raro! Viajamos en el mismo tren de la mañana hacia el mismo barrio.'),
    ('arthur', 'Hannah, call the station lost and found office right away.', 'Hannah, llama enseguida a la oficina de objetos perdidos de la estación.'),
    ('hannah', 'I am dialing now... Hello? Did anyone report a swapped blue suitcase?', 'Estoy marcando ahora... ¿Hola? ¿Alguien reportó una maleta azul cambiada?'),
    ('evelyn', 'Tell them mine has a red ribbon inside the top pocket!', '¡Diles que la mía tiene una cinta roja dentro del bolsillo superior!'),
    ('hannah', 'Not yet? Please take our guesthouse number and address. Thank you!', '¿Todavía no? Por favor, tome el número y la dirección de nuestra posada. ¡Gracias!'),
    ('arthur', "They have nothing yet, ma'am, I am terribly sorry.", 'Todavía no tienen nada, señora, lo siento muchísimo.'),
    ('evelyn', 'It is not your fault. Still, I only have the coat on my back!', 'No es culpa suya. ¡Aun así, solo llevo puesto el abrigo que traigo encima!'),
    ('hannah', 'Wait one moment, Tessa in the cafe just waved to me with an idea!', '¡Espere un momento, Tessa en la cafetería me acaba de hacer señas con la mano porque tiene una idea!'),
]
WALK = [
    (0, None, ["'¡Vaya por Dios, qué confusión! Déjeme mirar la etiqueta con mis gafas.' Para exclamar '¡qué lío!' ante un sustantivo contable, el inglés intercala el artículo en", (None, 'what a mix-up'), 'y añade', (None, 'look at'), 'para enfocar la vista.']),
    (1, None, ["'¿Hay algún nombre o número de teléfono en ella?' Para preguntar si 'hay' algo, inviertes las dos primeras palabras en", (None, 'Is there'), 'igual que con cualquier pregunta del verbo ser o estar.']),
    (2, None, ["'Ningún número de teléfono, por desgracia. Solo dos iniciales y el nombre de una calle antigua.' Antepuesto directamente al sustantivo,", (None, 'No phone number'), "equivale a 'ningún número de teléfono'."]),
    (3, None, ["'¡Espera, esa calle está aquí mismo en nuestro barrio, a cinco minutos!' Añadir", (None, 'away'), 'al final de', (None, 'five minutes away'), 'expresa a qué distancia queda un sitio.']),
    (4, None, ["'¡Qué raro! Viajamos en el mismo tren de la mañana hacia el mismo barrio.' Delante de un adjetivo suelto la exclamación arranca con", (None, 'How strange'), 'mientras que', (None, 'rode'), 'es el pasado de viajar en tren.']),
    (5, None, ["'Hannah, llama enseguida a la oficina de objetos perdidos de la estación.' La sección de objetos perdidos se conoce siempre por el par fijo", (None, 'lost and found'), "literalmente 'perdido y encontrado'."]),
    (6, None, ["'Estoy marcando ahora... ¿Hola? ¿Alguien reportó una maleta azul cambiada?' En preguntas en pasado,", (None, 'Did anyone report'), 'concentra el pasado en el auxiliar inicial y deja el verbo principal en su forma base.']),
    (7, None, ["'¡Diles que la mía tiene una cinta roja dentro del bolsillo superior!' El posesivo independiente", (None, 'mine'), "sustituye a 'mi maleta' sin necesitar artículo delante."]),
    (8, None, ["'¿Todavía no? Por favor, tome el número y la dirección de nuestra posada. ¡Gracias!' Dos sílabas muy útiles al teléfono:", (None, 'Not yet'), "pregunta o confirma '¿todavía no?'."]),
    (9, None, ["'Todavía no tienen nada, señora, lo siento muchísimo.' Para disculparte con mucha cortesía,", (None, 'terribly sorry'), "intensifica la disculpa aunque empiece pareciéndose a 'terrible'."]),
    (10, None, ["'No es culpa suya. ¡Aun así, solo llevo puesto el abrigo que traigo encima!' Qué buena frase para quitar hierro a un problema:", (None, 'It is not your fault'), 'no es tu culpa.']),
    (11, None, ["'¡Espere un momento, Tessa en la cafetería me acaba de hacer señas con la mano porque tiene una idea!' Colocar", (None, 'just waved'), 'indica algo que acaba de ocurrir hace apenas unos segundos.']),
]
