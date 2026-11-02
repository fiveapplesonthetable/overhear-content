ID = 'paquita-salas-s01e02-scene-07'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 7
TITLE = 'Lo envió hace años  (She Sent It Years Ago)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Window 00:05:50,160–00:06:57,640.'
INTRO = ("Thrilled by an old showreel on the office shelf, Paquita rings actress Hiba Abouk to offer her representation. "
         "Hiba quickly hangs up, and Magüi breaks the news that she already stars in a hit series watched by millions. "
         "Listen to the Spanish first, then we'll go through it together.")
OPENER = "Let's go through Paquita's phone call and what happens after."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how Spanish expresses 'years ago' with the verb meaning 'makes', how 'paper' also means an acting role, and why 'man!' is an everyday exclamation for anyone in Spain. See you next time.")
CLOSING = ('magui', '¡Hasta pronto!')

STORY = [
    ('paquita', '¡La tenemos! La voy a llamar y darle la sorpresa.',
     "We've got her! I'm going to call her and give her the surprise.",
     [(120, 'La tenemos'), (120, 'La voy a llamar y darle la sorpresa')],
     'Added exclamation marks and trimmed conversational tag.'),
    ('paquita', 'Hola, ¿Hiba Abouk?',
     'Hello, Hiba Abouk?',
     [(121, 'Hola'), (121, '¿Hiba Abouk?')],
     'Trimmed repeated greeting and phone reply.'),
    ('paquita', 'Mira, soy Paquita Salas, de PS Management.',
     "Look, I'm Paquita Salas, from PS Management.",
     [(122, 'Mira, soy'), (122, 'de PS Management'), (122, 'Paquita Salas')],
     'Placed personal name before agency name.'),
    ('paquita', 'Hemos visto tu material y nos ha gustado muchísimo.',
     "We've seen your portfolio, and we really liked it.",
     [(124, 'hemos visto tu material'), (125, 'y nos ha gustado muchísimo')],
     'Joined across two cues and trimmed opening filler.'),
    ('paquita', 'Me ha colgado.',
     'She hung up on me.',
     [(128, 'Me ha colgado')], ''),
    ('paquita', 'Dice que lo envió hace años.',
     'She says she sent it years ago.',
     [(129, 'dice que lo envió hace años')],
     'Trimmed opening discourse marker pues.'),
    ('magui', 'Te lo quería comentar antes de llamarla.',
     'I wanted to mention it to you before calling her.',
     [(130, 'Te lo quería'), (130, 'antes de llamarla')],
     'Simplified haber comentado to comentar and trimmed unfinished clause.'),
    ('magui', 'Está haciendo de protagonista de El Príncipe.',
     "She's playing the lead in El Príncipe.",
     [(131, 'Está haciendo de protagonista'), (132, 'El Príncipe')],
     'Restored uncontracted de before title El Príncipe and removed subtitle quotes.'),
    ('paquita', 'Pero esa serie tampoco la ve tanta gente.',
     'But not that many people watch that series anyway.',
     [(133, 'Pero esa serie tampoco la ve tanta gente')], ''),
    ('magui', 'Hombre, como seis millones de personas.',
     'Come on, around six million people.',
     [(134, 'Hombre, como seis millones'), (135, 'De personas')],
     'Joined phrase across two cues.'),
    ('paquita', '¿Y ella tiene mucho papel?',
     'And does she have a big part?',
     [(137, '¿Y ella tiene mucho papel')],
     'Trimmed opening clause and trailing word habla.'),
    ('paquita', 'De los videobooks que había en la estantería era el mejor.',
     'Of the showreels on the shelf, it was the best.',
     [(139, 'de los "videobooks" que había en la estantería'), (140, 'era el mejor')],
     'Trimmed opening clause and removed subtitle quotation marks.')
]

WALK = [
    (0, None, """'We've got her! I'm going to call her and give her the surprise.' Both openings start with the short feminine short word for "her", sitting right before "we have" and "I'm going to". Near the end, "to her" tacks straight onto the end of "give" as one combined word."""),
    (1, None, """'Hello, Hiba Abouk?' The silent first letter in Spain's greeting "hello" vanishes completely when spoken. Rising intonation turns the actress's name into a polite phone check without needing extra words."""),
    (2, None, """'Look, I'm Paquita Salas, from PS Management.' Spaniards often start a phone call with the casual command "look" in the sense of "listen". On the phone, Spanish says "I am Paquita" rather than "this is Paquita", followed by the linking word "from"."""),
    (3, None, """'We've seen your portfolio, and we really liked it.' Casting agents in Spain use the word "material" to mean an actor's clips and photos. Instead, of "we liked it", Spanish literally says "to us it has pleased", boosted by a strong ending meaning "so very much"."""),
    (4, None, """'She hung up on me.' In Spanish, "hung" covers ending a phone call too, just like English "hang up". Putting the tiny short word "on me" right at the front shows Paquita felt the slam of the receiver personally."""),
    (5, None, """'She says she sent it years ago.' Where English puts "ago" after "years", Spanish puts "makes" before the time: literally "makes years". A short object short word "it" sits right before "sent" and points back to her showreel."""),
    (6, None, """'I wanted to mention it to you before calling her.' Two tiny words at the start stack "to you" and "it" neatly before "wanted". At the end, "before of" links smoothly into "calling her", with "her" attached to the action."""),
    (7, None, """'She's playing the lead in El Príncipe.' Literally, "doing of protagonist", this handy expression means playing a particular part on screen or stage. Although "of" and masculine "the" normally merge in Spanish, they stay separate here because "El" belongs to the show's title."""),
    (8, None, """'But not that many people watch that series anyway.' Mentioning "that series" first lets Paquita shrug it off, and Spanish echoes it with a little feminine "it" before "watches". The negative "neither" gives the sense of "not either", while "people" stays singular."""),
    (9, None, """'Come on, around six million people.' Opening with the exclamation "man" is a classic reaction across Spain — even between two women — meaning "well, come on!". Unlike English "six million people", Spanish adds the linking word "of" before "people"."""),
    (10, None, """'And does she have a big part?' The everyday word "paper" doubles as an actor's "role" or "part", from the days when scripts came on paper rolls. Asking whether someone has "much paper" is a natural way to ask how big their role is."""),
    (11, None, """'Of the showreels on the shelf, it was the best.' Spanish agencies borrow "videobook" for an actor's video showreel. Notice the past-time form meaning "there were" before "on the bookcase", and how "the best" stands cleanly on its own at the end.""")
]
