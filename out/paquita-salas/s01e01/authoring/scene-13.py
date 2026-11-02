ID = 'paquita-salas-s01e01-scene-13'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 1
SCENE = 13
TITLE = '¿Has recibido un mail mío?  (Did You Get My Email?)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'macarena': 'Macarena'}
SOURCE_NAME = 'Paquita Salas S01E01: Casada con esto'
SOURCE_FILE = 'sources/paquita-salas/s01/e01.es.srt'
SOURCE_NOTE = 'Window 00:14:51,600–00:17:07,160.'
INTRO = ("Still dressed in her navy wedding suit, Paquita surprises Macarena outside her television studio with the blue premiere dress and shoes ready in the car. "
         "Macarena twice asks whether Paquita received her email, while an oblivious Paquita blames technology and hurries her to get changed. "
         "Listen to the Spanish first.")
OPENER = "Let's follow their reunion outside the studio."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how 'un mail mío' says 'an email of mine', and how Spanish puts 'ya' with 'estar' plus an '-ndo' form for 'is already sorting it out'. See you next time.")
CLOSING = ('macarena', '¡Hasta luego!')

STORY = [
    ('paquita', '¡Maqui! ¿Qué tal?',
     'Maqui! How are things?',
     [(331, '¡Maqui!'), (332, '¿Qué tal?')], ''),
    ('macarena', '¿Qué tal, Paquita? ¿Qué haces aquí?',
     'How are things, Paquita? What are you doing here?',
     [(333, '¿Qué tal, Paquita?'), (335, '¿Qué haces aquí?')], ''),
    ('paquita', 'Ha habido un lío de mails.',
     "There's been a mix-up with the emails.",
     [(337, 'Ha habido un lío de mails')], ''),
    ('paquita', 'He venido a llevarte a la Seminci esta noche.',
     "I've come to take you to Seminci tonight.",
     [(340, 'he venido a llevarte a'), (340, 'esta noche'), (341, 'la Seminci')], ''),
    ('paquita', 'Tengo todo en el coche: vestido y zapatos para que veas la película.',
     'I have everything in the car: dress and shoes so you can see the film.',
     [(349, 'Tengo todo en el coche'), (350, 'Vestido, zapatos'), (350, 'para que veas la película')], ''),
    ('paquita', '¿Cuál es el problema? Está todo bien.',
     "What's the problem? Everything is fine.",
     [(351, '¿Cuál es el problema?'), (352, 'Está todo bien')], ''),
    ('paquita', 'Ya sé lo que te pasa.',
     "I know what's up with you.",
     [(356, 'Ya sé lo que te pasa')], ''),
    ('paquita', 'Es que iba a la boda de Paco con Magüi.',
     "The thing is, I was going to Paco's wedding with Magüi.",
     [(358, 'Es que'), (358, 'a la boda'), (358, 'Magüi')],
     'Replaced del Cerdeña / la Magüi with Paco / Magüi.'),
    ('paquita', 'Me has hecho un favor.',
     "You've done me a favour.",
     [(362, 'Me has hecho un favor')], ''),
    ('macarena', 'Oye, Paquita, ¿has recibido un mail mío?',
     'Listen, Paquita, have you received an email of mine?',
     [(369, 'Oye, Paquita'), (371, 'has recibido un'), (371, 'mío')],
     'Used mail spelling consistently.'),
    ('paquita', 'No, no he recibido el mail. No sé qué pasó con el mail.',
     "No, I haven't received the email. I don't know what happened with the email.",
     [(373, 'No, no he recibido el mail. No sé qué pasó con el mail')], ''),
    ('paquita', 'Es la tecnología, ya está Magüi solucionándolo.',
     "It's technology, Magüi is already sorting it out.",
     [(374, 'La tecnología, ya está Magüi solucionándolo')],
     'Added es for a complete beginner sentence.'),
    ('macarena', 'Me voy a cambiar.',
     "I'm going to get changed.",
     [(375, 'Me voy a cambiar')], ''),
    ('paquita', 'Sí, cámbiate.',
     'Yes, get changed.',
     [(375, 'Sí, cámbiate')], ''),
    ('macarena', 'El vestido azul es muy bonito. ¿No has recibido el mail entonces?',
     "The blue dress is very pretty. You haven't received the email then?",
     [(378, 'El vestido, muy bonito el azul'), (379, '¿No has recibido el'), (379, 'entonces?')],
     'Joined dress compliment into a complete clause.')
]

WALK = [
    (0, None, "'Maqui! How are things?' Greeting Macarena by her nickname Maqui and that handy phrase for how are things sets Paquita's warm, maternal tone right away."),
    (1, None, "'How are things, Paquita? What are you doing here?' Unlike English, Spanish uses simple present what do you do here rather than an ing-form for what are you doing here."),
    (2, None, "'There's been a mix-up with the emails.' Just as one unchanging three-letter word means there is and there are, has been stays singular here too. The word for tangle or mess is masculine."),
    (3, None, "'I've come to take you to Seminci tonight.' After I have come, Spanish adds the little word for to before take you, and tacks casual you onto the end of take."),
    (4, None, "'I have everything in the car: dress and shoes so you can see the film.' Notice the two-word link meaning so that or in order that, which triggers the a-ending form of you see."),
    (5, None, "'What's the problem? Everything is fine.' Before is the problem, Spanish asks which is the problem rather than what is the problem."),
    (6, None, "'I know what's up with you.' Putting already before I know means I've worked it out now, followed by the neuter two-word chunk meaning what happens to you."),
    (7, None, "'The thing is, I was going to Paco's wedding with Magüi.' That opening two-word excuse literally says it is that, followed by ongoing I was going for a plan that was interrupted."),
    (8, None, "'You've done me a favour.' Literally to me you have made a favour, using the same irregular form for made or done that Lidia used earlier."),
    (9, None, "'Listen, Paquita, have you received an email of mine?' Putting mine after an email lets Macarena ask casually about an email of mine rather than saying the email."),
    (10, None, "'No, I haven't received the email. I don't know what happened with the email.' Notice how Paquita swaps the word for an out for the definite word for the, thinking Macarena means Juanfran's schedule notice."),
    (11, None, "'It's technology, Magüi is already sorting it out.' General ideas like technology take the feminine word for the in Spanish. At the end, sorting out tacks masculine it onto one word."),
    (12, None, "'I'm going to get changed.' Changing something else is plain change; adding the little word for myself at the front means changing your own clothes."),
    (13, None, "'Yes, get changed.' In a positive command, that same little word for yourself jumps onto the back of change, adding an accent mark on the first syllable."),
    (14, None, "'The blue dress is very pretty. You haven't received the email then?' Blue sits after dress and keeps the same ending for masculine and feminine things. Closing with then gently tests whether Paquita truly doesn't know.")
]
