ID = 'paquita-salas-s01e01-scene-08'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = '¿Me puedes ver ese enchufe?  (Can You Check That Plug?)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'alex': 'Álex', 'paquita': 'Paquita'}
SOURCE_NAME = 'Paquita Salas S01E01: Casada con esto'
SOURCE_FILE = 'sources/paquita-salas/s01/e01.es.srt'
SOURCE_NOTE = 'Window 00:08:07,760–00:09:03,040.'
INTRO = ("Friendly young courier Álex drops off a parcel at the agency, asks whether he can send his actress cousin's showreel, and compliments Magüi's red dress. "
         "Just as Álex is leaving, Paquita asks him to inspect a loose wall socket behind a lamp. "
         "Listen to the Spanish first.")
OPENER = "Let's go through Álex's visit to the office."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard everyday Madrid idioms like 'throwing a signature' and 'throwing an eye' to take a quick look, plus how commands bundle 'it' and 'to me' onto one word. See you next time.")
CLOSING = ('alex', '¡Hasta luego!')

STORY = [
    ('alex', 'Buenas tardes, Paquita. Dejo esto aquí.',
     "Good afternoon, Paquita. I'll leave this here.",
     [(183, 'Buenas tardes'), (185, 'Paquita. Dejo esto aquí')], ''),
    ('paquita', 'Muy bien, gracias.',
     'Very good, thank you.',
     [(186, 'Muy bien, gracias')], ''),
    ('alex', '¿Me echáis una firma?',
     'Could you sign here for me?',
     [(186, '¿Me echáis una firma?')], ''),
    ('alex', 'Oye, ¿te acuerdas que mi prima es actriz?',
     'Hey, do you remember that my cousin is an actress?',
     [(188, 'Oye, ¿te acuerdas que'), (188, 'mi prima es actriz?')],
     'Trimmed embedded te comenté que.'),
    ('paquita', 'Me acuerdo.',
     'I remember.',
     [(189, 'Me acuerdo')], ''),
    ('alex', '¿Te puedo mandar su videobook?',
     'Can I send you her showreel?',
     [(190, '¿Te puedo mandar su'), (190, 'videobook')], ''),
    ('paquita', 'Claro, mándamelo. Apunta el mail.',
     'Of course, send it to me. Write down the email.',
     [(191, 'Claro'), (191, 'Mándamelo, apunta el mail')], ''),
    ('paquita', 'Te dejo la tarjeta.',
     "Here, I'll give you our card.",
     [(196, 'Te dejo la tarjeta')], ''),
    ('alex', 'Qué guapa vas, Magüi.',
     'How gorgeous you look, Magüi.',
     [(198, 'Qué guapa vas, Magüi')], ''),
    ('alex', 'Muchas gracias, Paquita. Yo ya me voy.',
     "Thank you very much, Paquita. I'm heading off now.",
     [(199, 'muchas gracias, Paquita'), (200, 'yo ya me voy')], ''),
    ('paquita', 'Espera, cariño. ¿Me puedes ver ese enchufe? No sé qué le pasa.',
     "Hold on, darling. Can you check that socket for me? I don't know what's wrong with it.",
     [(200, 'Espera, cariño'), (201, '¿Me puedes ver ese enchufe? No sé qué le pasa')], ''),
    ('paquita', 'Tiré fuerte de la lámpara.',
     'I pulled hard on the lamp.',
     [(203, 'Tiré fuerte de la lámpara')], ''),
    ('alex', 'Está un poco suelto.',
     "It's a bit loose.",
     [(204, 'Está un poco suelto')], ''),
    ('alex', 'Tengo cinco minutos. Le echo un ojo.',
     "I have five minutes. I'll take a look at it.",
     [(205, 'Tengo cinco minutos. Le echo un ojo')], '')
]

WALK = [
    (0, None, "'Good afternoon, Paquita. I'll leave this here.' Spanish greetings are plural, literally good afternoons, because tardes is feminine. Then simple present I leave this here covers what Álex is doing right now."),
    (1, None, "'Very good, thank you.' The word for thanks is always plural too, literally graces, and pairs naturally with very well as a polite acknowledgement."),
    (2, None, "'Could you sign here for me?' Couriers in Spain casually ask do you throw me a signature, using the Castilian plural you-all ending because both Paquita and Magüi are at the desk."),
    (3, None, "'Hey, do you remember that my cousin is an actress?' That attention-getter at the start literally means hear or listen. Cousin ends in a feminine vowel for a female cousin, and actress needs no word for an."),
    (4, None, "'I remember.' Answering takes just two words: the little word for myself followed by the I form, matching the pattern of Álex's question."),
    (5, None, "'Can I send you her showreel?' Notice how the tiny word for to you sits right in front of can I, though tacking it onto send would mean the exact same thing. Spanish actors use the borrowed compound videobook for a video showreel."),
    (6, None, "'Of course, send it to me. Write down the email.' Earlier the word for clear meant understandable; on its own like this, it means of course. Then send bundles me and it onto one word, followed by jot down the email."),
    (7, None, "'Here, I'll give you our card.' Literally I leave you the card: the same everyday action word Álex used for leaving the parcel now means handing over a business card."),
    (8, None, "'How gorgeous you look, Magüi.' Literally what pretty you go: in Spain, saying someone goes pretty is a warm, idiomatic way to compliment how they are dressed to go out."),
    (9, None, "'Thank you very much, Paquita. I'm heading off now.' Because thanks is feminine plural, many before it takes the matching feminine plural ending too. Adding already before I leave gives the sense of I'm off now."),
    (10, None, "'Hold on, darling. Can you check that socket for me? I don't know what's wrong with it.' Literally can you see that plug or socket for me, then I don't know what happens to it, a reusable pattern whenever a gadget acts up."),
    (11, None, "'I pulled hard on the lamp.' Where English pulls on something, Spanish pulls of the lamp. The word for strong doubles here as hard without changing its ending."),
    (12, None, "'It's a bit loose.' Because socket is masculine, loose ends in o, and Spanish picks the temporary state form because being loose is a current condition rather than its nature."),
    (13, None, "'I have five minutes. I'll take a look at it.' Earlier Álex used throw for signing a form; now he says I throw an eye to it, Spain's favourite casual idiom for taking a quick look.")
]
