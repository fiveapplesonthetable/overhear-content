ID = 'paquita-salas-s01e02-scene-08'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 8
TITLE = 'Todo va vía link  (Everything Goes by Link)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'magui': 'Magüi', 'paquita': 'Paquita'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Window 00:06:57,720–00:07:58,040.'
INTRO = ("Magüi gently tells Paquita that casting has moved online and helps her post a short notice on an app with a strict word limit. "
         "Over lunch they chat about giving up vinegar and salt while waiting in vain for replies. "
         "Listen to the conversation first.")
OPENER = "Let's break down the scene line by line."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard Spain's everyday word a computer, how one neat word says whether text 'fits' in a box, and how Spanish expresses 'not yet' as 'of moment, nothing'. See you next time.")
CLOSING = ('paquita', '¡Nos vemos!')

STORY = [
    ('magui', 'Paquita, ahora todo va vía link.',
     'Paquita, everything goes by link nowadays.',
     [(141, 'Paquita, ahora todo va vía "link"')],
     'Trimmed opening hesitation and removed subtitle quotation marks.'),
    ('paquita', '¿Y eso qué es? ¿El ordenador?',
     'And what is that? The computer?',
     [(143, '¿Y eso qué es? El ordenador')],
     'Turned tag question into a direct question.'),
    ('magui', 'Internet.',
     'The Internet.',
     [(144, 'Internet')], ''),
    ('paquita', '¿Y de eso tenemos?',
     'And do we have any of that?',
     [(145, '¿Y de eso tenemos?')], ''),
    ('paquita', 'PS Management busca a la actriz tres sesenta.',
     'PS Management is looking for the three-sixty actress.',
     [(148, 'PS Management'), (148, 'Busca a la actriz')],
     'Joined dictated sentences and spelled out the numeral 360.'),
    ('magui', 'No cabe.',
     "It doesn't fit.",
     [(151, 'no cabe')],
     'Trimmed repetition.'),
    ('paquita', '¿Cómo que no cabe?',
     "What do you mean it doesn't fit?",
     [(151, '¿Cómo que no cabe?')], ''),
    ('magui', 'Esta aplicación tiene un máximo de palabras.',
     'This app has a word limit.',
     [(152, 'Esta aplicación'), (153, 'tiene un máximo de palabras')],
     'Joined across two cues and trimmed trailing relative clause.'),
    ('paquita', '¿Quién nos sigue?',
     'Who follows us?',
     [(157, '¿Quién nos sigue?')],
     'Trimmed preceding word phrase.'),
    ('magui', 'De momento, nada.',
     'Nothing so far.',
     [(158, 'De momento, nada')], ''),
    ('magui', 'No me gusta mucho el vinagre.',
     "I don't really like vinegar.",
     [(161, 'No me gusta mucho el vinagre')],
     'Trimmed follow-up question.'),
    ('paquita', 'La sal es muy mala. Yo la sal la estoy dejando también.',
     "Salt is very bad. I'm giving up salt too.",
     [(162, 'La sal es'), (162, 'muy mala'), (163, 'Yo la sal la estoy dejando también')],
     'Simplified first sentence and trimmed reply tag.'),
    ('paquita', 'Magüi, así no la vamos a encontrar.',
     "Magüi, we aren't going to find her like this.",
     [(165, 'Magüi, así no la vamos a encontrar')], '')
]

WALK = [
    (0, None, """'Paquita, everything goes by link nowadays.' Literally "now everything goes via link", using "goes" for how business operates today. Spanish speakers in media drop the borrowed English word "link" straight into conversation."""),
    (1, None, """'And what is that? The computer?' In Spain, people call a computer an "organiser", rather than using a word closer to English "computer". Notice the neuter word "that" when Paquita doesn't even know what kind of thing a link is."""),
    (2, None, """'The Internet.' Unlike English, Spanish normally names "Internet" as a bare word without "the" in front of it. Magüi answers with that single word to sum up the whole online world."""),
    (3, None, """'And do we have any of that?' Starting with "of that" puts Paquita's scepticism first, literally "and of that, we have?". You can reuse this handy pattern whenever someone mentions something unfamiliar and you wonder if you have any."""),
    (4, None, """'PS Management is looking for the three-sixty actress.' One compact Spanish word covers "looks for" without needing a separate word "for". Instead, the personal marker before "the actress" shows they are searching for a person, and "three sixty" means an all-round performer."""),
    (5, None, """'It doesn't fit.' Two short words say there isn't enough room, whether for clothes in a suitcase or characters in a text box. Swap in anything else as the subject when something won't fit."""),
    (6, None, """'What do you mean it doesn't fit?' Putting "how that" in front of someone's exact words is Spain's go-to way to challenge what they just said. It carries the surprised punch of "what do you mean...?"."""),
    (7, None, """'This app has a word limit.' Both "this" and "application" match as feminine singular here. Literally "a maximum of words", it flips the English order "word limit" around with "of" in the middle."""),
    (8, None, """'Who follows us?' On social media, the Spanish word "follows" works just like English "follow". The tiny word "us" sits right before "follows" rather than after it."""),
    (9, None, """'Nothing so far.' Literally "of moment, nothing", that opening two-word chunk is a super common everyday way to say "for now" or "so far". Paired with "nothing", it makes a crisp two-beat update."""),
    (10, None, """'I don't really like vinegar.' Spanish builds likes backwards compared with English: "vinegar does not please me much". Because she talks about vinegar in general, Spanish keeps "the" in front of "vinegar"."""),
    (11, None, """'Salt is very bad. I'm giving up salt too.' Salt is feminine in Spanish, so "bad" takes its feminine ending "-a", and general "salt" keeps "the" again. In the second sentence, "leaving" also means quitting a habit, and mentioning "the salt" early makes Spanish echo it with "her" before "am leaving"."""),
    (12, None, """'Magüi, we aren't going to find her like this.' That brisk two-syllable word after Magüi's name means "like this" or "this way". Then "no" and "her" sit together right before "we are going to find".""")
]
