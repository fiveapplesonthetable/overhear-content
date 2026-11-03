ID = 'paquita-salas-s01e04-scene-10'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 4
SCENE = 10
TITLE = 'Me ha colgado  (She Hung Up on Me)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'mariona': 'Mariona', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E04: Divacel'
SOURCE_FILE = 'sources/paquita-salas/s01/e04.es.srt'
SOURCE_NOTE = 'Native Spanish captions from episode stream. Scene window 00:08:47,520–00:09:29,840.'
INTRO = 'Magüi dials the casting office and hands the receiver to Paquita, only for an assistant to answer because the casting director is in the bathroom. Paquita launches into a glowing pitch for Mariona anyway, until the line suddenly goes dead and she has to tell Mariona the truth. Listen to the Spanish first.'
OPENER = "Now let's go through it line by line with the English translation."
TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = "You heard Paquita leave a lively phone message praising Mariona's sparkle and energy, followed by the blunt disappointment when the call gets cut off. See you next time."
CLOSING = ('magui', '¡Adiós!')

STORY = [
    ('paquita', 'Hola, mira, soy Paquita. ¿Y tú cómo te llamas?', "Hello, look, this is Paquita. And what's your name?", [(204, 'Hola, mira, soy'), (205, 'Y tú cómo te llamas')], ''),
    ('paquita', '¿Me puedes pasar con ella, que le tengo que decir una cosita?', 'Can you put me through to her, since I have a little thing to tell her?', [(206, 'Me puedes pasar con'), (206, 'que le tengo que decir una cosita')], 'Used ella instead of unlisted name.'),
    ('paquita', '¿En el baño? Bueno, pues te dejo a ti el recado, ¿vale?', "In the bathroom? Alright, then I'll leave the message with you, okay?", [(207, 'En el baño'), (208, 'Bueno, pues te dejo a ti el recado'), (208, 'vale')], ''),
    ('paquita', 'Tengo a la protagonista de la nueva película.', "I've got the leading lady for the new film.", [(209, 'Tengo a la protagonista'), (210, 'de la nueva película')], ''),
    ('paquita', 'Mariona Terés, lo que estáis buscando.', "Mariona Terés, just what you're looking for.", [(211, 'Mariona Terés, lo que estáis buscando')], ''),
    ('paquita', 'Muy graciosa, con muchísima chispa, espontánea, natural...', 'Very funny, with tons of spark, spontaneous, natural...', [(212, 'Muy graciosa, con muchísima chispa, espontánea, natural')], ''),
    ('paquita', 'La tenéis que ver porque os va a encantar, de verdad.', "You have to see her because you're going to love her, truly.", [(214, 'la tenéis que ver porque os va a encantar, de verdad')], ''),
    ('paquita', 'Perfecto, claro. Un besito a ti... Me ha colgado.', 'Perfect, of course. A little kiss for you... She hung up on me.', [(215, 'Perfecto'), (216, 'Claro'), (217, 'un besito a ti'), (217, 'Me ha colgado')], ''),
    ('mariona', '¿Me van a ver? Paquita, ¿me van a ver?', 'Are they going to see me? Paquita, are they going to see me?', [(218, 'Me van a ver? Paquita, ¿me van a ver')], ''),
    ('magui', 'No la van ni a ver.', "They won't even see her.", [(219, 'No la van ni a ver')], ''),
    ('paquita', 'No, cariño, no te van a ver.', "No, darling, they aren't going to see you.", [(219, 'No, cariño, no te van a ver')], ''),
    ('paquita', 'Que no quieren caras nuevas. Siempre igual.', "They don't want new faces. It's always the same.", [(220, 'Que no quieren caras nuevas'), (222, 'Siempre igual')], ''),
]

WALK = [
    (0, None, "'Hello, look, this is Paquita. And what's your name?'"),
    (1, None, "'Can you put me through to her, since I have a little thing to tell her?'"),
    (2, None, "'In the bathroom? Alright, then I'll leave the message with you, okay?'"),
    (3, None, "'I've got the leading lady for the new film.'"),
    (4, None, "'Mariona Terés, just what you're looking for.'"),
    (5, None, "'Very funny, with tons of spark, spontaneous, natural...'"),
    (6, None, "'You have to see her because you're going to love her, truly.'"),
    (7, None, "'Perfect, of course. A little kiss for you... She hung up on me.'"),
    (8, None, "'Are they going to see me? Paquita, are they going to see me?'"),
    (9, None, "'They won't even see her.'"),
    (10, None, "'No, darling, they aren't going to see you.'"),
    (11, None, "'They don't want new faces. It's always the same.'"),
]
