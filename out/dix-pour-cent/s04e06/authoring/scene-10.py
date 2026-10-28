ID = "dix-pour-cent-s04e06-scene-10"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 10
TITLE = "La meilleure mort  (The best death)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
SOURCE_NAME = "Dix pour cent S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
VOICES = {'narrator': 'sky', 'lea': 'lucie', 'veto': 'theo'}
LABELS = {'lea': 'Arlette', 'veto': 'Vet'}

INTRO = "At the veterinary clinic, the vet gently speaks with Arlette about her beloved dog's passing while Jean-Gabriel stays by her side. We will hear it in French first, so don't worry about catching every word."
OPENER = "Let's go back through it. The vet explains the situation."
TRANSITION = "Let's listen to the whole scene again."
OUTRO = 'Arlette says her final goodbye to her dog.'

STORY = [
    ('veto', 'Il est mort dans son sommeil.', 'He died in his sleep.', [(393, "Gardez à l'esprit qu'il est mort dans son sommeil.")], ''),
    ('veto', "C'est la meilleure mort.", 'It is the best death.', [(394, "C'est la meilleure façon de mourir pour un chien.")], ''),
    ('veto', 'Et pour nous aussi.', 'And for us too.', [(395, "Et pour n'importe qui, d'ailleurs.")], ''),
    ('lea', "C'est vrai, merci.", 'It is true, thank you.', [], ''),
    ('veto', "J'ai réservé une place au cimetière.", 'I reserved a place at the cemetery.', [(396, "J'ai réservé une place pour lui au cimetière pour chiens d'Asnières.")], ''),
    ('veto', 'Ils viendront le chercher.', 'They will come pick him up.', [(397, 'Je les préviens, ils viendront le chercher.')], ''),
    ('veto', 'Je peux faire autre chose?', 'Can I do anything else?', [(398, "S'il y a quoi que ce soit que je puisse faire pour vous...")], ''),
    ('lea', "C'est bon, merci.", 'It is fine, thank you.', [], ''),
    ('lea', 'Pouvez-vous nous laisser?', 'Can you leave us?', [(399, "Pouvez-vous nous laisser, s'il vous plaît?")], ''),
    ('veto', 'Bien sûr.', 'Of course.', [(400, 'Bien sûr.')], ''),
    ('lea', 'Il est vraiment parti.', 'He is really gone.', [], ''),
    ('lea', 'Au revoir, mon chien.', 'Goodbye, my dog.', [], ''),
]

WALK = [
    (0, None, "'He died in his sleep.' The vet assures her it was peaceful."),
    (1, None, "'It is the best death.' He tries to make her feel better."),
    (2, None, "'And for us too.' He adds that it is ideal for anyone."),
    (3, None, "'It is true, thank you.' Arlette agrees sadly."),
    (4, None, "'I reserved a place at the cemetery.' He took care of the arrangements."),
    (5, None, "'They will come pick him up.' He explains the next step."),
    (6, None, "'Can I do anything else?' He offers further assistance."),
    (7, None, "'It is fine, thank you.' She declines politely."),
    (8, None, "'Can you leave us?' She asks for some privacy."),
    (9, None, "'Of course.' The vet respects her wish."),
    (10, None, "'He is really gone.' She realizes the finality of it."),
    (11, None, "'Goodbye, my dog.' She says a heartfelt farewell."),
]

CLOSING = ('lea', 'Adieu.')
