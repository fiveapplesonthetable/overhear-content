# Authoring module for boris-s01e01-scene-01.
ID = 'boris-s01e01-scene-01'
SHOW = 'boris'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Lo stagista  (The New Intern)'
LEVEL = 'A1 — beginner'
PAIR = 'it-en'
LABELS = {'alessandro': 'Alessandro', 'rene': 'René', 'arianna': 'Arianna'}
SOURCE_NAME = 'Boris S01E01'
SOURCE_FILE = 'sources/boris/s01/e01.it.srt'
INTRO = (
    'Boris is an Italian comedy set behind the scenes of a chaotic Rome soap opera. '
    'On his first morning at the studio, the new intern Alessandro looks for the director Rene, '
    'who is busy pep-talking his lucky goldfish Boris before assistant director Arianna stops Alessandro in the hall. '
    'You will hear the whole scene in Italian first, so do not worry about catching every word.'
)
OPENER = (
    "Let's walk through that brisk welcome line by line, starting with Alessandro arriving at the studio."
)
TRANSITION = 'Now listen to the whole corridor scene again from start to finish.'
OUTRO = (
    'You have heard polite questions with "scusi", how Alessandro introduces himself as the intern, '
    'and how Arianna stacks two negatives to shut him down. See you next time.'
)
CLOSING = ('alessandro', 'Ciao!')
STORY = [
    ('alessandro', "Scusi, sa dov'è il regista?", 'Excuse me, do you know where the director is?', [(1, "Scusi, sa dov'è il regista")], ''),
    ('rene', 'Ascoltami bene adesso, Boris.', 'Listen to me carefully now, Boris.', [(18, 'ascoltami bene adesso, Boris')], ''),
    ('rene', 'Noi dobbiamo fare una grandissima regia.', 'We have to do some truly great directing.', [(19, 'Noi dobbiamo fare una grandissima regia')], ''),
    ('rene', "Ti voglio concentrato come l'anno scorso, capito?", 'I want you focused like last year, got it?', [(20, "ti voglio concentrato come l'anno scorso, capito")], ''),
    ('alessandro', 'Scusi, lei è il regista?', 'Excuse me, are you the director?', [(24, 'Scusi, lei è il regista')], ''),
    ('arianna', 'È arrivato Lopez.', 'Lopez has arrived.', [(25, 'È arrivato Lopez')], ''),
    ('arianna', 'Chi sei? Che vuoi? Che fai qua?', 'Who are you? What do you want? What are you doing here?', [(26, 'Che vuoi? Che fai qua')], 'Whisper heard "Che sei"; restored to standard "Chi sei".'),
    ('alessandro', 'Veramente, sono lo stagista.', "Actually, I'm the intern.", [(27, 'veramente, sono lo stagista')], ''),
    ('alessandro', 'Volevo solo...', 'I just wanted...', [(28, 'Volevo solo')], ''),
    ('arianna', 'No, tu non vuoi niente.', "No, you don't want anything.", [(29, 'No, tu non vuoi niente')], ''),
    ('arianna', 'Tu stai fermo qui, in silenzio.', 'You stay right here, quietly.', [(30, 'Tu stai fermo qui, in silenzio')], ''),
    ('arianna', 'E aspetti ordini, ok?', 'And you wait for instructions, okay?', [(30, 'e aspetti ordini, ok')], ''),
    ('arianna', 'Non è del tuo reparto.', "It's not from your department.", [(31, 'Non è del tuo reparto')], ''),
]
WALK = [
    (0, None, "'Excuse me, do you know where the director is?' Alessandro opens politely with \"scusi\", the formal way to get a stranger's attention. Notice how \"dove\" and \"e\" squeeze together into \"dov'e\" for \"where is\"."),
    (1, None, "'Listen to me carefully now, Boris.' Rene is talking to a goldfish in a glass bowl. In Italian, the little word \"mi\" for \"to me\" hooks straight onto the end of \"ascolta\", making one compact command."),
    (2, None, "'We have to do some truly great directing.' Adding the ending \"-issima\" to \"grande\" cranks \"big\" all the way up to \"huge\" or \"truly great\", a favourite Italian way to exaggerate."),
    (3, None, "'I want you focused like last year, got it?' \"L'anno scorso\" literally puts \"the year\" before \"last\". Tacking \"capito\" onto the end is the everyday Italian check for \"understood?\""),
    (4, None, "'Excuse me, are you the director?' Here \"lei\" literally means \"she\", yet in polite Italian it serves as the respectful \"you\" for a boss or a stranger, even when speaking to a man like Rene."),
    (5, None, "'Lopez has arrived.' Arianna cuts in with urgent set news. Italian often puts the action before the person's name when announcing who just walked in."),
    (6, None, "'Who are you? What do you want? What are you doing here?' Three rapid-fire questions, and Arianna switches straight to the casual \"tu\" forms because she already outranks the newcomer."),
    (7, None, "'Actually, I'm the intern.' \"Veramente\" gently corrects someone without sounding rude. Before \"stagista\", Italian uses \"lo\" for \"the\" because the word starts with \"s\" plus another consonant."),
    (8, None, "'I just wanted...' Using the past form \"volevo\" softens the request, just like \"I was hoping\" in English, while \"solo\" adds \"only\" or \"just\" before he gets cut off."),
    (9, None, "'No, you don't want anything.' Italian happily pairs \"non\" before the action with \"niente\" after it; the two negatives reinforce each other rather than cancelling out."),
    (10, None, "'You stay right here, quietly.' \"Fermo\" means \"still\" and ends in \"-o\" to match Alessandro. At the end, \"in silenzio\" literally says \"in silence\", telling him not to make a sound."),
    (11, None, "'And you wait for instructions, okay?' Unlike English, \"aspettare\" needs no extra word for \"for\": you simply wait the instructions directly."),
    (12, None, "'It's not from your department.' When Alessandro reaches out to help on set, Arianna stops him again with \"reparto\", the everyday crew word for a film department."),
]
