ID = 'porta-dos-fundos-s01e01-scene-02'
SHOW, SEASON, EPISODE, SCENE = 'porta-dos-fundos', 1, 1, 2
TITLE = 'Segunda-feira de manhã  (Monday Morning Meeting)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'colega': 'Colega', 'financeiro': 'Funcionário'}
SOURCE_NAME = 'Porta dos Fundos — Vem pra reunião (2026-01-05)'
SOURCE_FILE = 'sources/porta-dos-fundos/s01/e01.pt.srt'

INTRO = (
    'Back at the desks, the finance employee has just asked why on earth he belongs in a marketing meeting. '
    'His colleague finally drops the act and points through the office glass at another unlucky visitor. '
    'Listen to the Brazilian Portuguese first without worrying about catching every word.'
)
OPENER = "Now let's unpack what each speaker says in the scene, line by line."
TRANSITION = "Now let's listen to the whole scene again at natural speed."
OUTRO = (
    'Not even the fire warden escaped the creative brainstorm, and the finance employee still has real work piled up. '
    'Next time, his colleague tries an even wilder warning. See you next time!'
)
CLOSING = ('colega', 'Até mais!')

STORY = [
    ('colega', 'Se eu vou entrar, eu quero que você entre também.', "If I'm going in, I want you to go in too.", [(57, 'se eu vou'), (59, 'entrar, eu quero que você entre também')], 'Simplified vou ter que entrar to vou entrar.'),
    ('colega', 'É uma reunião segunda-feira de manhã!', "It's a meeting on Monday morning!", [(65, 'uma reunião segunda-feira'), (67, 'manhã')], 'Shortened 11 horas da manhã to de manhã.'),
    ('financeiro', 'Mas é inútil eu participar dessa reunião.', "But it's pointless for me to join that meeting.", [(69, 'Mas é inútil eu participar dessa'), (71, 'reunião')], ''),
    ('financeiro', 'Eles falam muita coisa que eu não entendo.', "They say a lot of things that I don't understand.", [(71, 'coisa que'), (73, 'eu não entendo')], 'Adapted um monte de coisa to muita coisa and standard plural falam.'),
    ('colega', 'Você é fofo. Deixa eu te falar uma coisa.', "You're sweet. Let me tell you something.", [(77, 'Você é fofo. Deixa eu te falar'), (79, 'uma coisa')], ''),
    ('colega', 'Olha lá para dentro. Você tá vendo aquela moça ali?', 'Look in there. Do you see that young woman over there?', [(79, 'Olha lá para dentro. Você tá'), (81, 'vendo aquela moça ali')], 'Omitted unclear caption tail.'),
    ('colega', 'Ela é brigadista de incêndio.', "She's a fire warden.", [(83, 'Ela é brigadista de incêndio')], ''),
    ('colega', 'Ela veio aqui olhar um extintor.', 'She came here to check a fire extinguisher.', [(83, 'Ela veio'), (85, 'aqui')], 'Simplified fiscalizar to olhar and fixed caption spelling extintor.'),
    ('colega', 'Agora ela tá numa reunião com a nossa equipe.', "Now she's in a meeting with our team.", [(87, 'numa reunião'), (89, 'com a nossa'), (91, 'equipe')], 'Shortened brainstorm criativo com a nossa equipe de criação.'),
    ('financeiro', 'Isso atrasa os outros! Eu tenho muita coisa para resolver.', 'That slows everyone else down! I have a lot to sort out.', [(97, 'isso atrasa os'), (99, 'outros'), (99, 'coisa para resolver')], 'Shortened cues 97-99 and omitted bleeped cues 105-109.'),
]

WALK = [
    (0, None, "'If I'm going in, I want you to go in too.' Watch how \"entrar\" shifts to \"entre\" after \"eu quero que\": when you say what you want someone else to do, Portuguese swaps the ending to mark it as a wish rather than a fact."),
    (1, None, "'It's a meeting on Monday morning!' The names for days of the week in Portuguese count up from Sunday as a market day, so \"segunda-feira\" literally means \"second fair\" for Monday."),
    (2, None, "'But it's pointless for me to join that meeting.' Where English needs \"for me to join\", Portuguese simply puts \"eu\" right in front of \"participar\", and \"dessa\" blends \"de\" with \"essa\"."),
    (3, None, "'They say a lot of things that I don't understand.' \"Muita coisa\" stays singular even though it means \"many things\", a very natural Brazilian way to talk about a whole pile of stuff."),
    (4, None, "'You're sweet. Let me tell you something.' Calling a grown coworker \"fofo\" — \"cute\" or \"sweet\" — is pure teasing condescension here, followed by \"deixa eu\", the everyday spoken way to say \"let me\"."),
    (5, None, "'Look in there. Do you see that young woman over there?' Spoken Brazilian Portuguese trims \"esta\" down to \"ta\", so \"voce ta vendo\" is how people actually ask \"do you see?\"."),
    (6, None, "'She's a fire warden.' Just like English drops \"a\" in titles at times, Portuguese says \"ela e brigadista\" with no \"uma\" in between when naming someone's job."),
    (7, None, "'She came here to check a fire extinguisher.' \"Veio\" means \"she came\", and Portuguese links it straight to \"olhar\" without needing an extra word for \"to\"."),
    (8, None, "'Now she's in a meeting with our team.' \"Numa\" squeezes \"em\" and \"uma\" into one smooth two-beat word meaning \"in a\"."),
    (9, None, "'That slows everyone else down! I have a lot to sort out.' \"Atrasar\" is built on \"atras\", meaning \"behind\", so slowing people down literally puts them behind schedule."),
]
