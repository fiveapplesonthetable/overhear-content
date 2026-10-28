# Authoring module for dix-pour-cent-s04e05-scene-17.
ID = 'dix-pour-cent-s04e05-scene-17'
SHOW = 'dix-pour-cent'
SEASON = 4
EPISODE = 5
SCENE = 17
TITLE = "L'aveu d'Hervé  (Hervé's Confession)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'gabriel': 'Gabriel', 'herve': 'Hervé'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S04E05'
SOURCE_FILE = 'sources/dix-pour-cent/s04/e05.fr.dual.srt'
INTRO = "In the hallway at ASK, Herve stops Gabriel to make a nervous confession about his secret acting career. However, Gabriel reveals that the secret is already out across the agency. Let's listen to their exchange in French first."
OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."
OUTRO = "Herve realizes to his dismay that his secret acting debut is already common knowledge at ASK. When you watch the episode, listen out for the expressions meaning 'minute' and 'is happening'. You'll catch them now. See you next time!"
CLOSING = ('gabriel', 'Au revoir!')
STORY = [
    ('herve', 'Gabriel, vous avez une minute?', 'Gabriel, do you have a minute?', [(736, 'Gabriel')], ''),
    ('gabriel', "Oui, qu'est-ce qui se passe?", 'Yes, what is going on?', [(737, 'Quoi')], ''),
    ('herve', "J'ai quelque chose à vous avouer.", 'I have something to confess to you.', [(737, "J'ai quelque chose à vous avouer")], ''),
    ('gabriel', 'Quoi donc? Rien de grave?', 'What then? Nothing serious?', [(737, 'Quoi'), (738, 'Rien de grave')], ''),
    ('herve', "Non, mais c'est très délicat.", 'No, but it is very delicate.', [], ''),
    ('gabriel', 'Allez, parlez, je vous écoute!', 'Come on, speak, I am listening to you!', [], ''),
    ('herve', "J'ai joué un rôle au cinéma.", 'I played a role in a movie.', [(739, "J'ai joué un rôle")], ''),
    ('herve', "J'ai tourné dans un vrai film!", 'I acted in a real movie!', [(739, 'dans un film')], ''),
    ('gabriel', 'Le film de Donzelli? Je sais.', 'The Donzelli movie? I know.', [(740, 'Le Donzelli? Je sais')], ''),
    ('gabriel', "Élise me l'a déjà dit.", 'Elise already told me.', [(740, "Élise me l'a dit")], ''),
    ('herve', "Quoi? Ce n'est pas vrai!", 'What? That is not true!', [], ''),
    ('herve', 'Elle devait garder le secret!', 'She was supposed to keep the secret!', [(741, 'garder le secret')], ''),
    ('gabriel', 'Mon Dieu, vous êtes tellement naïf!', 'My God, you are so naive!', [(742, 'Mon Dieu, vous êtes')], ''),
    ('herve', 'On ne peut faire confiance à personne.', 'You cannot trust anyone.', [], ''),
]
WALK = [
    (0, None, "'Gabriel, do you have a minute?' Hervé approaches Gabriel hesitantly and asks if he has a minute to talk."),
    (1, None, "'Yes, what is going on?' Gabriel stops and gives his assistant his attention."),
    (2, None, "'I have something to confess to you.' Hervé prepares to admit his secret acting job."),
    (3, None, "'What then? Nothing serious?' Gabriel hopes there is no crisis at the agency."),
    (4, None, "'No, but it is very delicate.' Hervé tries to soften the news before speaking."),
    (5, None, "'Come on, speak, I am listening to you!' Gabriel impatiently gestures for him to get to the point."),
    (6, None, "'I played a role in a movie.' Hervé finally reveals his appearance on the big screen."),
    (7, None, "'I acted in a real movie!' Hervé emphasizes that it was a legitimate feature production."),
    (8, None, "'The Donzelli movie? I know.' Gabriel immediately names the director without surprise."),
    (9, None, "'Elise already told me.' Gabriel explains how the news reached him first."),
    (10, None, "'What? That is not true!' Hervé is stunned that his confidence was betrayed."),
    (11, None, "'She was supposed to keep the secret!' Hervé complains that Elise promised not to tell."),
    (12, None, "'My God, you are so naive!' Gabriel teases Hervé for trusting a rival agency head."),
    (13, None, "'You cannot trust anyone.' Hervé laments the lack of discretion in the film industry. Now let's listen to the complete discussion once more to reinforce the vocabulary."),
]
