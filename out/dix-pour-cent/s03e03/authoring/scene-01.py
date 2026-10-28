# Authoring module for dix-pour-cent-s03e03-scene-01.
ID = 'dix-pour-cent-s03e03-scene-01'
SHOW = 'dix-pour-cent'
SEASON = 3
EPISODE = 3
SCENE = 1
TITLE = 'Une chance pour Samy  (A Chance for Samy)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'gerard': 'Gérard', 'mathias': 'Mathias', 'samy': 'Samy'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S03E03'
SOURCE_FILE = 'sources/dix-pour-cent/s03/e03.fr.dual.srt'
INTRO = "At a Parisian cafe, agent Mathias Barneville meets his star client Gerard Lanvin to discuss shooting dates. Noticing that their ambitious young waiter Samy dreams of acting, Gerard suggests giving him a screen test for a bodyguard role. Let's listen to the scene in French first."
OPENER = "Let's observe as Gerard and Mathias offer Samy a screen test for the movie."
TRANSITION = "Now let's listen to Samy, Gerard, and Mathias again at full speed."
OUTRO = "Samy rushes to fetch his resume and headshots, thrilled by the sudden opportunity offered by Gerard Lanvin. When you watch the episode, listen out for the expressions meaning 'come' and 'minute'. You'll catch them now. See you next time!"
CLOSING = ('mathias', 'À demain!')
STORY = [
    ('mathias', 'Samy, viens voir une minute.', 'Samy, come see for a minute.', [(65, 'Samy !'), (66, 'Viens voir.')], ''),
    ('samy', "Oui, monsieur Barneville, j'arrive.", 'Yes, Mr. Barneville, I am coming.', [(67, 'Yes.')], ''),
    ('gerard', 'Tu veux toujours faire du cinéma?', 'Do you still want to do cinema?', [(68, "Ça t'intéresse toujours, le cinéma ?")], ''),
    ('samy', "Oui, c'est mon grand rêve!", 'Yes, it is my great dream!', [(70, 'Oui.')], ''),
    ('gerard', 'Tu veux passer un casting?', 'Do you want to audition?', [(71, 'Tu veux passer un casting ?')], ''),
    ('samy', 'Un casting? Vous êtes sérieux?', 'An audition? Are you serious?', [(72, 'Un casting ?'), (73, 'Vous êtes sérieux ?')], ''),
    ('gerard', "C'est pour mon film À cran.", 'It is for my film On Edge.', [(75, 'Pour ce film-là ? À cran ?')], ''),
    ('mathias', 'As-tu un CV et des photos?', 'Do you have a resume and photos?', [(77, 'Vous avez un CV et des photos ?')], ''),
    ('samy', "J'ai tout dans mon sac.", 'I have everything in my bag.', [(78, "Oui, j'ai tout ça."), (79, "Par contre, c'est dans mon sac.")], ''),
    ('mathias', 'Apporte-les tout de suite.', 'Bring them right away.', [(80, 'Je vous le ramène tout de suite.')], ''),
    ('samy', "Vous réalisez mon rêve aujourd'hui!", 'You are making my dream come true today!', [(83, "c'est un rêve, là, que vous êtes en train de réaliser.")], ''),
    ('mathias', 'Attention, ce sont juste des essais.', 'Careful, these are just screen tests.', [(84, 'Attends, attends.'), (85, "C'est des essais.")], ''),
    ('gerard', 'Si tu réussis, le rôle est à toi.', 'If you succeed, the role is yours.', [(86, 'Si tu les rates, on ne peut plus rien pour toi.')], ''),
    ('samy', 'Merci, je vais donner le meilleur!', 'Thank you, I will give my best!', [(87, "Ah non, mais il n'y a pas de problème.")], ''),
]
WALK = [
    (0, None, "'Samy, come see for a minute.' Mathias summons the waiter for a conversation."),
    (1, None, "'Yes, Mr. Barneville, I am coming.' Samy confirms immediate arrival."),
    (2, None, "'Do you still want to do cinema?' Gérard asks informally about Samy's ambition to work in cinema."),
    (3, None, "'Yes, it is my great dream!' Samy expresses genuine passion."),
    (4, None, "'Do you want to audition?' Gérard offers a casting opportunity."),
    (5, None, "'An audition? Are you serious?' Samy questions the reality of the offer."),
    (6, None, "'It is for my film On Edge.' Gérard identifies the upcoming motion picture."),
    (7, None, "'Do you have a resume and photos?' Mathias checks standard actor materials."),
    (8, None, "'I have everything in my bag.' Samy confirms confidently that he has everything in his bag."),
    (9, None, "'Bring them right away.' Mathias commands immediate delivery of the files."),
    (10, None, "'You are making my dream come true today!' Samy exclaims with joy that Gérard is making his dream come true."),
    (11, None, "'Careful, these are just screen tests.' Mathias sets realistic expectations."),
    (12, None, "'If you succeed, the role is yours.' Gérard motivates the young actor."),
    (13, None, "'Thank you, I will give my best!' Samy promises maximum effort. Now let's listen to Samy, Gerard, and Mathias again at full speed."),
]
