# Authoring module for dix-pour-cent-s02e04-scene-03.
ID = 'dix-pour-cent-s02e04-scene-03'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 4
SCENE = 3
TITLE = 'Andréa appelle Sacha Hartman  (Calling Hartman)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'noemie': 'Noémie', 'sacha': 'Sacha'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E04'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e04.fr.dual.srt'
INTRO = "In her office at ASK, Andréa calls young director Sacha Hartman to propose Isabelle Adjani for his new film. Expecting enthusiasm, she is stunned when Hartman bitterly recounts an old grudge and flatly refuses to work with her. Let's listen to the scene in French first."
OPENER = "Let's examine how Andréa's phone call with Sacha Hartman turns into a disaster."
TRANSITION = "Now let's listen to Andréa's tense phone negotiation again at full speed."
OUTRO = 'Hartman holds a four-year grudge after Isabelle rejected his debut film, putting Andréa in an impossible bind. With Noémie watching, Andréa must urgently figure out how to save the deal. See you next time!'
CLOSING = ('andrea', 'Bonne journée!')
STORY = [
    ('andrea', "Allô Sacha? C'est Andréa, réveille-toi!", 'Hello Sacha? It is Andréa, wake up!', [(53, "-Allô ? -Sacha, c'est Andréa.")], ''),
    ('sacha', 'Salut Andréa, je dormais encore un peu.', 'Hi Andréa, I was still sleeping a bit.', [(54, '-Salut. -Tu dormais ?'), (55, '-Un peu.')], ''),
    ('andrea', 'Je viens de croiser Isabelle Adjani au bureau.', 'I just bumped into Isabelle Adjani at the office.', [(56, 'Je viens de croiser Isabelle Adjani.')], ''),
    ('andrea', "Elle meurt d'envie de te rencontrer.", 'She is dying to meet you.', [(57, "Elle meurt d'envie de te rencontrer.")], ''),
    ('andrea', 'Elle est parfaite pour ton nouveau film.', 'She is perfect for your new film.', [(59, 'Elle est parfaite pour le rôle de Milena.')], ''),
    ('sacha', 'Je refuse de travailler avec cette actrice.', 'I refuse to work with this actress.', [(66, 'Je refuse de travailler avec cette femme.')], ''),
    ('andrea', "Pourquoi? C'est une immense star du cinéma.", 'Why? She is an immense movie star.', [(69, 'mais quelle grande actrice.')], ''),
    ('sacha', 'Elle a refusé mon premier projet autrefois.', 'She refused my first project in the past.', [(78, "Elle ne l'était pas quand je lui ai envoyé le scénario de mon premier film."), (79, "C'était il y a quatre ans, personne ne vous connaissait.")], ''),
    ('sacha', "Elle m'a envoyé un message très méchant.", 'She sent me a very nasty message.', [(81, "Ça n'excuse pas l'e-mail infect que j'ai reçu en retour."), (82, "« Mademoiselle Adjani n'est pas intéressée. »")], ''),
    ('sacha', 'Dis-lui que je ne suis pas intéressé.', 'Tell her that I am not interested.', [(84, "Dites-lui que M. Hartman n'est pas intéressé non plus.")], ''),
    ('andrea', "Sacha, s'il te plaît, écoute-moi!", 'Sacha, please, listen to me!', [(63, 'Allô ?')], ''),
    ('noemie', "Alors Andréa, qu'est-ce qu'il a dit?", 'So Andréa, what did he say?', [(64, 'Alors ?'), (87, 'Comment ça ?')], ''),
    ('andrea', 'Hartman est furieux et refuse cette rencontre.', 'Hartman is furious and refuses this meeting.', [(86, "Hartman ne veut pas d'Adjani."), (90, 'Il est encore amer et refuse de la rencontrer.')], ''),
    ('noemie', "C'est une vraie catastrophe pour notre agence.", 'That is a real disaster for our agency.', [(95, 'On passe à côté de deux des plus grands noms du cinéma')], ''),
]
WALK = [
    (0, None, "'Hello Sacha? It is Andréa, wake up!' An energetic telephone greeting demanding attention."),
    (1, None, "'Hi Andréa, I was still sleeping a bit.' Answering the phone half-asleep, the young director admits he was still in bed."),
    (2, None, "'I just bumped into Isabelle Adjani at the office.' A recent past construction with 'venir de'."),
    (3, None, "'She is dying to meet you.' An idiomatic French expression showing extreme eagerness."),
    (4, None, "'She is perfect for your new film.' A strong descriptive claim promoting the casting."),
    (5, None, "'I refuse to work with this actress.' Sacha flatly refuses to make his movie with that actress."),
    (6, None, "'Why? She is an immense movie star.' An incredulous question citing industry stature."),
    (7, None, "'She refused my first project in the past.' A compound past verb recounting an old rejection."),
    (8, None, "'She sent me a very nasty message.' A compound past recalling an offensive email."),
    (9, None, "'Tell her that I am not interested.' An indirect imperative delivering retaliatory disinterest."),
    (10, None, "'Sacha, please, listen to me!' An urgent imperative begging for dialogue."),
    (11, None, "'So Andréa, what did he say?' A curious inquiry from an observant assistant."),
    (12, None, "'Hartman is furious and refuses this meeting.' A summary of the director's bitter resentment."),
    (13, None, "'That is a real disaster for our agency.' An exclamatory evaluation highlighting high stakes."),
]
