# Authoring module for linden-courtyard-es-s01e04-scene-05.
ID = 'linden-courtyard-es-s01e04-scene-05'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 4
SCENE = 5
TITLE = 'Five-Star Showers  (Duchas de cinco estrellas)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'arthur': 'Arthur', 'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = 'Veinte minutos más tarde, en el soleado rincón del desayuno, Caleb baja renovado mientras Hannah sirve café y Arthur revolotea cerca con nerviosismo. Escucha primero.'
OPENER = 'Repasemos cada intervención con tranquilidad.'
TRANSITION = 'Volvamos a oír la escena completa a ritmo normal.'
OUTRO = 'Arthur soltó el secreto en tiempo récord y, en vez de enfadarse, Caleb les invita a salir al patio para mostrarles a qué se dedica realmente. Hasta pronto.'
CLOSING = ('caleb', 'Take care!')
STORY = [
    ('caleb', 'Good morning, Hannah! Good morning, sir! What a bright morning after the rain.', '¡Buenos días, Hannah! ¡Buenos días, señor! Qué mañana tan luminosa después de la lluvia.'),
    ('hannah', 'Good morning, Caleb! Did you sleep well under the roof beams?', '¡Buenos días, Caleb! ¿Durmió bien bajo las vigas del tejado?'),
    ('caleb', 'Best sleep I have had all month, and the shower water was wonderfully hot!', '¡El mejor sueño que he tenido en todo el mes, y el agua de la ducha estaba maravillosamente caliente!'),
    ('arthur', 'Hot! Hear that, Hannah? Reliable, modern, five-star hot water!', '¡Caliente! ¿Oyes eso, Hannah? ¡Agua caliente fiable, moderna y de cinco estrellas!'),
    ('caleb', 'Old brick buildings usually take ages to warm up on the top floor.', 'Los edificios viejos de ladrillo suelen tardar muchísimo en calentarse en el último piso.'),
    ('arthur', "Please write that down! 'Hot water on the third floor: ten out of ten!'", "¡Por favor, apunte eso! 'Agua caliente en el tercer piso: ¡diez de diez!'"),
    ('caleb', 'Excuse me? Ten out of ten?', '¿Perdón? ¿Diez de diez?'),
    ('hannah', 'What Arthur means is... we hope every guest feels ten out of ten here!', 'Lo que Arthur quiere decir es... ¡esperamos que cada huésped se sienta diez de diez aquí!'),
    ('arthur', 'No, Hannah, let us be honest professionals! Sir, we respect the Portland Travel Guide!', '¡No, Hannah, seamos profesionales sinceros! ¡Señor, respetamos la Guía de Viajes de Portland!'),
    ('caleb', 'The Portland Travel Guide? Wait, do you think I am a hotel inspector?', '¿La Guía de Viajes de Portland? Esperen, ¿creen que soy un inspector de hoteles?'),
    ('hannah', "When your notebook fell open on the counter last night, we saw 'nine out of ten'...", "Cuando su cuaderno cayó abierto sobre el mostrador anoche, vimos 'nueve de diez'..."),
    ('caleb', 'Oh! Come outside to the courtyard for a minute. Let me show you what I really do!', '¡Oh! Salgan afuera al patio un minuto. ¡Déjenme enseñarles lo que hago en realidad!'),
]
WALK = [
    (0, None, ["'¡Buenos días, Hannah! ¡Buenos días, señor! Qué mañana tan luminosa después de la lluvia.' Otra exclamación clásica con sustantivo singular:", (None, 'What a bright morning'), '¡qué mañana tan luminosa!']),
    (1, None, ["'¡Buenos días, Caleb! ¿Durmió bien bajo las vigas del tejado?' Con el auxiliar en pasado,", (None, 'Did you sleep well'), 'deja el verbo principal en su forma base.']),
    (2, None, ["'¡El mejor sueño que he tenido en todo el mes, y el agua de la ducha estaba maravillosamente caliente!' El presente perfecto", (None, 'I have had all month'), 'conecta el mes que aún sigue en curso con hoy.']),
    (3, None, ["'¡Caliente! ¿Oyes eso, Hannah? ¡Agua caliente fiable, moderna y de cinco estrellas!' En el habla rápida,", (None, 'Hear that'), "abrevia '¿oyes eso?' quitando el auxiliar inicial."]),
    (4, None, ["'Los edificios viejos de ladrillo suelen tardar muchísimo en calentarse en el último piso.' El giro coloquial", (None, 'take ages'), "significa literalmente 'tardar siglos', es decir, muchísimo tiempo."]),
    (5, None, ["'¡Por favor, apunte eso! Agua caliente en el tercer piso: ¡diez de diez!' Con pronombre en medio,", (None, 'write that down'), 'significa anotarlo por escrito en papel.']),
    (6, None, ["'¿Perdón? ¿Diez de diez?' Con entonación ascendente,", (None, 'Excuse me'), 'pide que te aclaren algo sorprendente que acabas de oír.']),
    (7, None, ["'Lo que Arthur quiere decir es... ¡esperamos que cada huésped se sienta diez de diez aquí!' Para suavizar o aclarar las palabras de otra persona, abre con", (None, 'What Arthur means is'), 'lo que quiere decir es.']),
    (8, None, ["'¡No, Hannah, seamos profesionales sinceros! ¡Señor, respetamos la Guía de Viajes de Portland!' La fórmula", (None, 'let us be'), 'propone una actitud compartida para todo el equipo.']),
    (9, None, ["'¿La Guía de Viajes de Portland? Esperen, ¿creen que soy un inspector de hoteles?' En inglés todo oficio en singular lleva artículo indefinido:", (None, 'a hotel inspector'), 'un inspector de hoteles.']),
    (10, None, ["'Cuando su cuaderno cayó abierto sobre el mostrador anoche, vimos nueve de diez...' Recuerda que 'anoche' nunca usa preposición: se dice", (None, 'last night'), 'la noche pasada.']),
    (11, None, ["'¡Oh! Salgan afuera al patio un minuto. ¡Déjenme enseñarles lo que hago en realidad!' Para mostrar algo en persona, el giro natural es", (None, 'Let me show you'), 'déjenme enseñarles.']),
]
