ID = 'paquita-salas-s01e04-scene-06'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 4
SCENE = 6
TITLE = 'No al nepotismo  (No to Nepotism)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'alex': 'Álex', 'paquita': 'Paquita', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E04: Divacel'
SOURCE_FILE = 'sources/paquita-salas/s01/e04.es.srt'
SOURCE_NOTE = 'Native Spanish captions from episode stream. Scene window 00:04:48,080–00:05:21,360.'
INTRO = "As courier Álex heads out of the office, he politely asks Paquita whether she has watched his cousin's showreel yet. Paquita warmly assures him it was fantastic, then immediately confesses to the camera that she hasn't touched it because PS Management stands for pure meritocracy. Listen to the Spanish first."
OPENER = "Now let's go through it line by line with the English translation."
TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = "You heard Álex's polite check-in at the door, Paquita's enthusiastic white lie, and her firm speech against nepotism once he leaves. See you next time."
CLOSING = ('alex', '¡Hasta pronto!')

STORY = [
    ('alex', 'Bueno, chicas, me marcho.', "Alright, girls, I'm heading off.", [(97, 'Bueno chicas, me marcho')], ''),
    ('paquita', 'Gracias, niño.', 'Thanks, lad.', [(98, 'Gracias, niño')], ''),
    ('alex', 'Oye, Paquita, no quiero ser pesado.', "Hey, Paquita, I don't want to be a nuisance.", [(98, 'Oye, Paquita, no quiero ser pesado')], ''),
    ('alex', 'Pero me ha preguntado mi prima si has visto su videobook.', "But my cousin asked me if you've watched her showreel.", [(99, 'pero me ha preguntado mi prima si has visto su videobook')], ''),
    ('paquita', 'Sí. Me ha encantado, un trabajazo.', 'Yes. I loved it, a fantastic piece of work.', [(100, 'Sí. Me ha encantado, un trabajazo')], ''),
    ('alex', '¿En serio? Se va a poner muy contenta. Hasta luego.', "Really? She's going to be so happy. See you later.", [(101, 'En serio'), (102, 'se va a poner muy contenta'), (102, 'Hasta luego')], ''),
    ('magui', 'Adiós.', 'Goodbye.', [(103, 'Adiós')], ''),
    ('paquita', 'Chao.', 'Bye.', [(103, 'Chao')], ''),
    ('paquita', 'No lo he visto. ¿Cómo lo voy a ver?', "I haven't watched it. How could I possibly watch it?", [(104, 'No lo he visto'), (104, 'cómo lo voy a ver')], ''),
    ('paquita', 'Yo, si es tu hermana, te lo veo, pero si es tu prima...', "If she's your sister, I'll watch it for you, but if she's your cousin...", [(105, 'Yo, si es tu hermana, te lo veo'), (106, 'pero si es tu prima')], ''),
    ('paquita', 'Prima, no. Yo no veo primas. No al nepotismo.', "Not a cousin. I don't watch cousins. No to nepotism.", [(107, 'Prima, no. Yo no veo primas'), (108, 'No al nepotismo')], ''),
    ('paquita', 'Aquí, en PS, la gente entra por su talento. Meritocracia.', 'Here at PS, people get in on their talent. Meritocracy.', [(109, 'Aquí, en PS, la gente entra por su talento'), (110, 'Meritocracia')], ''),
]

WALK = [
    (0, None, "'Alright, girls, I'm heading off.'"),
    (1, None, "'Thanks, lad.'"),
    (2, None, "'Hey, Paquita, I don't want to be a nuisance.'"),
    (3, None, "'But my cousin asked me if you've watched her showreel.'"),
    (4, None, "'Yes. I loved it, a fantastic piece of work.'"),
    (5, None, "'Really? She's going to be so happy. See you later.'"),
    (6, None, "'Goodbye.'"),
    (7, None, "'Bye.'"),
    (8, None, "'I haven't watched it. How could I possibly watch it?'"),
    (9, None, "'If she's your sister, I'll watch it for you, but if she's your cousin...'"),
    (10, None, "'Not a cousin. I don't watch cousins. No to nepotism.'"),
    (11, None, "'Here at PS, people get in on their talent. Meritocracy.'"),
]
