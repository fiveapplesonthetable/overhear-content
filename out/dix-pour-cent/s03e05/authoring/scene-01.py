# Authoring module for dix-pour-cent-s03e05-scene-01.
ID = 'dix-pour-cent-s03e05-scene-01'
SHOW = 'dix-pour-cent'
SEASON = 3
EPISODE = 5
SCENE = 1
TITLE = "Le tournage de Béatrice  (Béatrice's Shoot)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'beatrice': 'Béatrice', 'maquilleuse': 'Maquilleuse'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S03E05'
SOURCE_FILE = 'sources/dix-pour-cent/s03/e05.fr.dual.srt'
INTRO = "On a grueling movie set, iconic actress Beatrice Dalle catches her breath after twenty-seven exhausting takes. When the makeup artist insists on applying full-body makeup for a body bag scene, Beatrice suspects director Pascal of bad faith. Let's listen to the scene in French first."
OPENER = "Let's observe as Beatrice discusses the unexpected body makeup on set."
TRANSITION = "Now let's listen to Beatrice and the makeup artist again at full speed."
OUTRO = "Convinced that director Pascal intends to film her unclothed without prior consent, Beatrice heads backstage. When you watch the episode, listen out for the expressions meaning 'filming' and 'rough'. You'll catch them now. See you next time!"
CLOSING = ('beatrice', 'Bonne journée!')
STORY = [
    ('beatrice', "Ce tournage est particulièrement rude aujourd'hui.", 'This shoot is particularly rough today.', [(9, "C'est rude, 27 prises")], ''),
    ('maquilleuse', 'Vous avez fait vingt-sept prises difficiles.', 'You did twenty-seven difficult takes.', [(9, "C'est rude, 27 prises")], ''),
    ('beatrice', "J'ai défoncé cette porte vingt-sept fois!", 'I smashed through that door twenty-seven times!', [(10, "27 fois, j'ai défoncé cette")], ''),
    ('maquilleuse', 'Il faut préparer la scène suivante.', 'We must prepare the next scene.', [(16, "ce serait bien qu'on y aille")], ''),
    ('beatrice', "J'ai encore quelques minutes de repos.", 'I still have a few minutes of rest.', [(17, 'On a le temps')], ''),
    ('maquilleuse', 'Nous devons maquiller tout votre corps.', 'We have to do your whole body with makeup.', [(19, 'on a tout le corps à faire')], ''),
    ('beatrice', "C'est la scène de la mort?", 'Is this the death scene?', [(20, "C'est la scène de la mort, oui ?")], ''),
    ('maquilleuse', "Oui, exactement, c'est cette scène.", 'Yes, exactly, it is that scene.', [(21, 'Bah oui')], ''),
    ('beatrice', 'Mais mon personnage est dans un sac!', 'But my character is inside a bag!', [(22, 'Mais je suis dans un sac')], ''),
    ('maquilleuse', 'Pascal a demandé un maquillage complet.', 'Pascal asked for full-body makeup.', [(23, "Pascal m'a dit maquillage corps entier")], ''),
    ('beatrice', 'Pourquoi maquiller mon corps entier?', 'Why put makeup on my entire body?', [(23, "Pascal m'a dit maquillage corps entier")], ''),
    ('maquilleuse', 'Je ne sais pas, ce sont les ordres.', 'I do not know, these are orders.', [(23, "Pascal m'a dit maquillage corps entier")], ''),
    ('beatrice', 'Pascal prépare une mauvaise surprise.', 'Pascal is preparing a nasty surprise.', [(24, 'je ressens pas cet embrouille')], ''),
    ('maquilleuse', 'Venez vous installer au maquillage.', 'Come and sit down in makeup.', [(16, "ce serait bien qu'on y aille")], ''),
]
WALK = [
    (0, None, "'This shoot is particularly rough today.' A candid observation acknowledging grueling working conditions."),
    (1, None, "'You did twenty-seven difficult takes.' An empathetic confirmation validating the physical strain."),
    (2, None, "'I smashed through that door twenty-seven times!' An exclamatory complaint describing intense physical exertion."),
    (3, None, "'We must prepare the next scene.' A polite professional reminder urging timely stage preparation."),
    (4, None, "'I still have a few minutes of rest.' A defensive plea asserting a brief break before further filming."),
    (5, None, "'We have to do your whole body with makeup.' A surprising procedural instruction announcing extensive cosmetics."),
    (6, None, "'Is this the death scene?' A clarifying question identifying the scheduled script sequence."),
    (7, None, "'Yes, exactly, it is that scene.' An affirmative confirmation verifying the plot point."),
    (8, None, "'But my character is inside a bag!' A logical objection protesting unnecessary body cosmetics."),
    (9, None, "'Pascal asked for full-body makeup.' A direct quote attributing the directive to the movie director."),
    (10, None, "'Why put makeup on my entire body?' A sharp suspicious question probing the director's true intentions."),
    (11, None, "'I do not know, these are orders.' A neutral disavowal reflecting crew hierarchy."),
    (12, None, "'Pascal is preparing a nasty surprise.' A perceptive suspicion detecting an unscripted nude scene."),
    (13, None, "'Come and sit down in makeup.' A gentle imperative repeating the backstage summons."),
]
