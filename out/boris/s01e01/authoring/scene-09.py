# Authoring module for boris-s01e01-scene-09.
ID = 'boris-s01e01-scene-09'
SHOW = 'boris'
SEASON = 1
EPISODE = 1
SCENE = 9
TITLE = 'La fotografia e la pubblicità  (Worse Than the Commercials)'
LEVEL = 'A1 — beginner'
PAIR = 'it-en'
LABELS = {'duccio': 'Duccio', 'alessandro': 'Alessandro'}
SOURCE_NAME = 'Boris S01E01'
SOURCE_FILE = 'sources/boris/s01/e01.it.srt'
INTRO = (
    'Alessandro finally finds director of photography Duccio relaxing in his dim dressing room. '
    'When the eager intern praises the look of the show, Duccio reveals the cynical golden rule of commercial television lighting. '
    'Listen to the Italian scene first without worrying about catching every word.'
)
OPENER = (
    "Let's unpack Duccio's philosophy of terrible lighting one line at a time."
)
TRANSITION = 'Now hear Duccio and Alessandro\'s whole conversation again from start to finish.'
OUTRO = (
    'You have heard "fa schifo" for calling something awful, "la pubblicita" for commercials, '
    'and "cambia canale" for changing the channel. See you next time.'
)
CLOSING = ('duccio', 'Buona serata!')
STORY = [
    ('duccio', 'Siediti.', 'Sit down.', [(310, 'Siediti')], ''),
    ('duccio', 'Hai visto le prime due puntate?', 'Did you watch the first two episodes?', [(311, 'le prime due puntate')], 'Standardised colloquial "L\'hai vista" to "Hai visto".'),
    ('alessandro', 'Sì, qualcosa.', 'Yes, a little bit.', [(312, 'Sì, qualcosa')], ''),
    ('duccio', 'Ti è piaciuta la fotografia?', 'Did you like the cinematography?', [(313, 'Ti è piaciuta la fotografia')], ''),
    ('alessandro', 'Molto.', 'Very much.', [(314, 'Molto')], ''),
    ('duccio', 'Non capisci niente.', 'You do not understand anything.', [(315, 'Non capisci')], 'Softened vulgarity to everyday "niente" for A1 learners.'),
    ('duccio', 'La fotografia fa schifo.', 'The cinematography is awful.', [(316, 'La fotografia fa schifo')], ''),
    ('duccio', 'Lo sai perché fa schifo?', 'Do you know why it is awful?', [(317, 'Lo sai perché fa schifo')], ''),
    ('alessandro', 'Non lo so.', 'I do not know.', [(318, 'Non lo so')], ''),
    ('duccio', 'Perché lo vogliono loro.', 'Because that is how they want it.', [(319, 'Perché lo vogliono loro')], ''),
    ('duccio', 'La fotografia non deve essere più bella della pubblicità.', 'The cinematography must not be prettier than the commercials.', [(320, 'La fotografia non deve essere più bella'), (320, 'della pubblicità')], ''),
    ('duccio', 'Se no la gente cambia canale.', 'Otherwise people change the channel.', [(321, 'se no la gente cambia canale')], ''),
    ('duccio', 'Hanno pensato a tutto.', 'They have thought of everything.', [(322, 'Hanno pensato a tutto')], ''),
    ('alessandro', 'Arianna voleva sapere per la scena...', 'Arianna wanted to know about the scene...', [(323, 'Arianna voleva sapere')], ''),
    ('duccio', 'Manda via Arianna.', 'Send Arianna away.', [(324, 'Manda'), (324, 'Arianna')], 'Softened Duccio\'s blunt dismissal for A1 learners.'),
]
WALK = [
    (0, None, "'Sit down.' \"Siediti\" tucks \"ti\", \"yourself\", onto the end of \"siedi\" to make a casual one-word invitation to take a seat."),
    (1, None, "'Did you watch the first two episodes?' In Italian television, an episode of a series is \"una puntata\", while \"le prime due\" puts \"the first\" ahead of \"two\"."),
    (2, None, "'Yes, a little bit.' \"Qualcosa\" literally means \"something\", and on its own it works nicely for \"a bit here and there\"."),
    (3, None, "'Did you like the cinematography?' Notice \"piaciuta\" ends in \"-a\" because \"la fotografia\" — literally photography, and in film the cinematography — is feminine."),
    (4, None, "'Very much.' Alessandro tries to flatter his elder with a polite single-word \"molto\", and walks straight into a trap."),
    (5, None, "'You do not understand anything.' \"Capisci\" comes from \"capire\", \"to understand\", paired once again with \"non\" and \"niente\"."),
    (6, None, "'The cinematography is awful.' \"Fa schifo\" literally says \"it makes disgust\", the punchiest everyday Italian way to say something stinks."),
    (7, None, "'Do you know why it is awful?' Adding little \"lo\" before \"sai\" literally asks \"do you know it, why...\", a very natural Italian rhythm."),
    (8, None, "'I do not know.' In English \"I don't know\" needs no object, whereas Italian almost always keeps \"lo\" for \"it\": \"non lo so\"."),
    (9, None, "'Because that is how they want it.' Placing \"loro\", \"they\", at the very end throws extra weight onto the shadowy network bosses: \"they\" are the ones who want it bad."),
    (10, None, "'The cinematography must not be prettier than the commercials.' \"Piu bella\" builds \"prettier\" with \"piu\", \"more\", and \"la pubblicita\" covers advertising and TV commercials."),
    (11, None, "'Otherwise people change the channel.' \"Se no\" — literally \"if not\" — means \"otherwise\". Also notice \"la gente\", \"people\", is singular in Italian, so it takes \"cambia\"."),
    (12, None, "'They have thought of everything.' Unlike English \"think of\", Italian links \"pensare\" with \"a\": \"pensare a tutto\"."),
    (13, None, "'Arianna wanted to know about the scene...' Once again Alessandro uses gentle past-time \"voleva\", \"wanted\", to soften an awkward question."),
    (14, None, "'Send Arianna away.' \"Mandare via\" pairs \"mandare\", \"to send\", with \"via\", \"away\" — Duccio has zero intention of rushing back to set."),
]
