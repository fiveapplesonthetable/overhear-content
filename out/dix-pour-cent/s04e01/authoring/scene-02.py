# Authoring module for dix-pour-cent-s04e01-scene-02.
ID = 'dix-pour-cent-s04e01-scene-02'
SHOW = 'dix-pour-cent'
SEASON = 4
EPISODE = 1
SCENE = 2
TITLE = "L'enthousiasme de Charlotte  (Charlotte's Enthusiasm)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'charlotte': 'Charlotte', 'oscar': 'Oscar'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S04E01'
SOURCE_FILE = 'sources/dix-pour-cent/s04/e01.fr.dual.srt'
INTRO = "At the airport arrival terminal, Andrea Martel greets internationally acclaimed actress Charlotte Gainsbourg after an eleven-hour flight. When Charlotte inquires about the artistic merit of her lifelong friend Oscar Rondo's screenplay, Andrea bluffs and lavishes it with praise. Just as Camille sends a text warning that the script is unwatchable, Oscar himself walks up to seal the deal. Let's listen to the scene in French first."
OPENER = "Let's observe as Andrea bluffs about the script just as director Oscar arrives."
TRANSITION = "Now let's listen to Andrea, Charlotte, and Oscar again at full speed."
OUTRO = "Having endorsed a script that she has not read and that Camille considers dreadful, Andrea is trapped in her own lie. When you watch the episode, listen out for the expressions meaning 'remain' and 'magnificent'. You'll catch them now. See you next time!"
CLOSING = ('andrea', 'À demain!')
STORY = [
    ('andrea', 'Tu restes magnifique après ce long voyage.', 'You remain gorgeous after this long journey.', [(31, "11 h d'avion")], ''),
    ('charlotte', "J'ai dormi pendant tout le vol.", 'I slept during the whole flight.', [(31, "11 h d'avion")], ''),
    ('charlotte', "Je refuse ce rôle si c'est mauvais.", 'I refuse this role if it is bad.', [(41, "si ce n'est pas bien")], ''),
    ('charlotte', "Dis-moi, tu as lu le scénario d'Oscar?", 'Tell me, did you read Oscar', [(46, "Tu l'as lu")], ''),
    ('andrea', "Oui, je l'ai lu ce matin.", 'Yes, I read it this morning.', [(47, "Oui, je l'ai lu")], ''),
    ('andrea', "C'est vraiment une histoire formidable.", 'It is really a wonderful story.', [(49, "C'est vraiment bien")], ''),
    ('charlotte', 'Je suis tellement soulagée de ton avis!', 'I am so relieved by your opinion!', [(50, 'Je suis tellement soulagée')], ''),
    ('andrea', "Camille m'écrit que c'est une catastrophe.", 'Camille texts me that it is a disaster.', [(51, "C'EST NAZE")], ''),
    ('oscar', 'Charlotte, quelle joie de te retrouver ici!', 'Charlotte, what a joy to meet you here!', [(60, 'mon meilleur ami')], ''),
    ('charlotte', "Voici Oscar, mon ami d'enfance.", 'Here is Oscar, my childhood friend.', [(60, 'mon meilleur ami')], ''),
    ('charlotte', 'Mon agent adore ton nouveau scénario.', 'My agent loves your new script.', [(68, 'elle a adoré')], ''),
    ('oscar', "C'est un honneur immense pour moi.", 'It is an immense honor for me.', [(68, 'elle a adoré')], ''),
    ('charlotte', 'Nous allons faire ce beau film ensemble!', 'We are going to make this beautiful film together!', [(70, 'On fait un film ensemble')], ''),
    ('andrea', 'Je me retrouve dans un piège terrible.', 'I find myself in a terrible trap.', [(51, "C'EST NAZE")], ''),
]
WALK = [
    (0, None, "'You remain gorgeous after this long journey.' A warm greeting complimenting the actress on her radiant appearance."),
    (1, None, "'I slept during the whole flight.' A simple explanation crediting good rest for defying jet lag."),
    (2, None, "'I refuse this role if it is bad.' A clear professional boundary insisting on script quality despite personal friendship."),
    (3, None, "'Tell me, did you read Oscar's script?' A direct probe seeking honest feedback from her trusted agent."),
    (4, None, "'Yes, I read it this morning.' A reckless falsehood pretending to have reviewed the manuscript."),
    (5, None, "'It is really a wonderful story.' An exaggerated compliment intended to flatter and reassure the client."),
    (6, None, "'I am so relieved by your opinion!' A joyful reaction confirming that the agent's praise removed all doubts."),
    (7, None, "'Camille texts me that it is a disaster.' An internal panic reacting to the incoming devastating text message."),
    (8, None, "'Charlotte, what a joy to meet you here!' An affectionate surprise arrival catching both women off guard."),
    (9, None, "'Here is Oscar, my childhood friend.' An affectionate introduction highlighting their lifelong creative bond."),
    (10, None, "'My agent loves your new script.' An enthusiastic secondhand compliment locking the actress into the movie."),
    (11, None, "'It is an immense honor for me.' A proud and touched response welcoming the agent's apparent approval."),
    (12, None, "'We are going to make this beautiful film together!' A decisive declaration launching the collaborative film project."),
    (13, None, "'I find myself in a terrible trap.' A horrified realization acknowledging the disastrous consequences of a hasty bluff."),
]
