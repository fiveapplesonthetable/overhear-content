# Authoring module for dix-pour-cent-s02e03-scene-02.
ID = 'dix-pour-cent-s02e03-scene-02'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 3
SCENE = 2
TITLE = "Gabriel négocie à l'accueil  (Begging the Receptionist)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'gabriel': 'Gabriel', 'receptionniste': 'Réceptionniste'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E03'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e03.fr.dual.srt'
INTRO = "At the driving exam registration office, Gabriel Sarda desperately attempts to negotiate an early test date for Norman. With the film shoot fast approaching, every week counts, but the strict receptionist refuses to grant special treatment. Let's listen to the scene in French first."
OPENER = "Let's examine how Gabriel tries to persuade the driving center receptionist."
TRANSITION = "Now let's listen to Gabriel's tense discussion at the counter again at full speed."
OUTRO = "The receptionist refuses to bend the rules for a celebrity client, reminding Gabriel that everyone must wait. Faced with a two-month delay, Gabriel must find another solution for Norman's role. See you next time!"
CLOSING = ('receptionniste', 'Au revoir, monsieur.')
STORY = [
    ('receptionniste', "Il n'y a rien de disponible pour avril.", 'There is nothing available for April.', [(32, 'Rien de disponible pour avril.')], ''),
    ('receptionniste', 'La prochaine date est le seize juin.', 'The next date is June sixteenth.', [(35, 'Le 16 juin.')], ''),
    ('gabriel', "C'est beaucoup trop tard, ça ne va pas.", 'It is much too late, that will not work.', [(36, 'Trop tard, ça ne va pas.')], ''),
    ('gabriel', 'Mon client joue dans un grand film.', 'My client acts in a major movie.', [(39, 'Mon client, Norman Thavaud, joue dans le nouveau film de Jacques Audiard.')], ''),
    ('receptionniste', 'Norman? Mes enfants parlent souvent de lui.', 'Norman? My children often talk about him.', [(41, 'Norman ? Mes enfants parlent de lui.')], ''),
    ('gabriel', "Exactement, c'est un moment clé pour lui.", 'Exactly, it is a key moment for him.', [(43, 'Exactement.'), (44, "C'est pourquoi c'est un moment clé dans sa carrière.")], ''),
    ('gabriel', 'Dans le film, il joue un chauffeur de taxi.', 'In the movie, he plays a taxi driver.', [(45, 'Dans le film il joue un jeune chauffeur de taxi')], ''),
    ('gabriel', 'Le tournage commence dans deux semaines seulement.', 'The shooting starts in two weeks only.', [(48, 'Le tournage commence dans deux semaines.')], ''),
    ('receptionniste', 'Vous devez simplement reporter ce tournage.', 'You must simply postpone this shoot.', [(49, 'Vous devez le reporter.')], ''),
    ('gabriel', 'Tout le monde est prêt pour tourner.', 'Everyone is ready to shoot.', [(51, 'Tout le monde est prêt.')], ''),
    ('gabriel', 'Pouvez-vous faire un effort pour nous?', 'Can you make an effort for us?', [(53, 'Si vous pouviez faire un effort'), (54, 'pour avancer un peu la date...')], ''),
    ('receptionniste', 'Non, les règles sont les mêmes pour tous.', 'No, the rules are the same for all.', [(57, "Les règles s'appliquent à tout le monde.")], ''),
    ('receptionniste', "J'ai attendu dix ans pour mes papiers.", 'I waited ten years for my papers.', [(60, "Dix ans j'ai attendu, mais au final,"), (61, "J'ai eu mes papiers.")], ''),
    ('receptionniste', 'Alors, vous voulez le seize juin?', 'So, do you want June sixteenth?', [(66, 'Alors...'), (67, 'tu veux le 16 juin ?')], ''),
]
WALK = [
    (0, None, "'There is nothing available for April.' The receptionist introduces the month."),
    (1, None, "'The next date is June sixteenth.' The receptionist specifies the calendar appointment."),
    (2, None, "'It is much too late, that will not work.' Gabriel expresses urgency."),
    (3, None, "'My client acts in a major movie.' Gabriel proudly tells the driving-school receptionist that his client is starring in a major film."),
    (4, None, "'Norman? My children often talk about him.' The receptionist recognizes Norman's name because her children talk about his videos all the time."),
    (5, None, "'Exactly, it is a key moment for him.' Gabriel agrees warmly and explains that this movie is a turning point for Norman."),
    (6, None, "'In the movie, he plays a taxi driver.' Gabriel describes the character's occupation."),
    (7, None, "'The shooting starts in two weeks only.' Gabriel expresses imminent production."),
    (8, None, "'You must simply postpone this shoot.' The receptionist expresses an uncompromising practical solution."),
    (9, None, "'Everyone is ready to shoot.' Gabriel announces that everyone on set is ready to shoot."),
    (10, None, "'Can you make an effort for us?' Gabriel asks for special assistance."),
    (11, None, "'No, the rules are the same for all.' The receptionist rejects exceptionalism."),
    (12, None, "'I waited ten years for my papers.' The receptionist illustrates personal resilience and delay."),
    (13, None, "'So, do you want June sixteenth?' The receptionist offers the only remaining appointment. Now let's listen to Gabriel's tense discussion at the counter again at full speed."),
]
