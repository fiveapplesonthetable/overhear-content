ID = "dix-pour-cent-s04e06-scene-09"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 9
TITLE = "Il sera là dans 5 minutes  (He will be here in 5 minutes)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
SOURCE_NAME = "Dix pour cent S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
VOICES = {'narrator': 'sky', 'lea': 'lucie', 'gabriel': 'theo'}
LABELS = {'lea': 'Arlette', 'gabriel': 'Gabriel'}

INTRO = "Gabriel tells Arlette that the man is coming. We will hear it in French first, don't worry about catching every word. Just listen to the rhythm and try to spot familiar phrases as Gabriel nervously speaks."
OPENER = "Let's go back through it. Gabriel reassures Arlette."
TRANSITION = "Let's listen to the whole scene again."
OUTRO = 'Arlette is very sad about her dog.'

STORY = [
    ('gabriel', "Ne t'inquiète pas, Arlette.", 'Do not worry, Arlette.', [], ''),
    ('lea', 'Il est vraiment parti?', 'Is he really gone?', [], ''),
    ('gabriel', "Oui, c'est fini.", 'Yes, it is finished.', [], ''),
    ('lea', 'Mon pauvre Jean Gabin.', 'My poor Jean Gabin.', [], ''),
    ('gabriel', 'Il a eu une belle vie.', 'He had a beautiful life.', [], ''),
    ('lea', "Qui va s'occuper de lui?", 'Who is going to take care of him?', [], ''),
    ('gabriel', 'Le monsieur.', 'The man.', [], ''),
    ('gabriel', 'Il est en route.', 'He is on his way.', [], ''),
    ('gabriel', 'Il sera là dans 5 minutes.', 'He will be there in 5 minutes.', [(392, 'Il sera là dans 5 minutes.')], ''),
    ('lea', "D'accord, merci Gabriel.", 'Okay, thank you Gabriel.', [], ''),
    ('gabriel', 'Je reste avec toi.', 'I am staying with you.', [], ''),
    ('lea', "C'est gentil.", 'That is kind.', [], ''),
]

WALK = [
    (0, None, "'Do not worry, Arlette.' Gabriel tries to comfort his colleague."),
    (1, None, "'Is he really gone?' Arlette asks if her dog is dead."),
    (2, None, "'Yes, it is finished.' He confirms the sad news."),
    (3, None, "'My poor Jean Gabin.' She mourns her dear pet."),
    (4, None, "'He had a beautiful life.' He tries to remind her of the good times."),
    (5, None, "'Who is going to take care of him?' She asks about the next steps."),
    (6, None, "'The man.' He refers to the undertaker."),
    (7, None, "'He is on his way.' The man is already coming."),
    (8, None, "'He will be there in 5 minutes.' He gives her an exact time."),
    (9, None, "'Okay, thank you Gabriel.' She appreciates his help."),
    (10, None, "'I am staying with you.' He refuses to leave her alone."),
    (11, None, "'That is kind.' She is grateful for his presence."),
]

CLOSING = ('lea', 'Je suis triste.')
