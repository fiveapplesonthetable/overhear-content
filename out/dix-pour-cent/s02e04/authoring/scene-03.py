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
INTRO = "In her office at ASK, Andrea calls young director Sacha Hartman to propose Isabelle Adjani for his new film. Expecting enthusiasm, she is stunned when Hartman bitterly recounts an old grudge and flatly refuses to work with her. Let's listen to the scene in French first."
OPENER = "Let's examine how Andrea's phone call with Sacha Hartman turns into a disaster."
TRANSITION = "Now let's listen to the whole phone negotiation again at full speed."
OUTRO = 'Hartman holds a four-year grudge after Isabelle rejected his debut film, putting Andrea in an impossible bind. With Noemie watching, Andrea must urgently figure out how to save the deal. See you next time!'
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
    (0, None, "'Hello Sacha? It is Andrea, wake up!' On the phone, callers introduce themselves with 'it is' rather than 'this is', followed here by a brisk command meaning 'wake yourself'."),
    (1, None, "'Hi Andrea, I was still sleeping a bit.' Sacha describes an ongoing state interrupted by the ring, softening it at the end with a handy chunk meaning 'a little'."),
    (2, None, "'I just bumped into Isabelle Adjani at the office.' Combining 'I come from' with an action is how you say 'I just did something' moments ago in French."),
    (3, None, "'She is dying to meet you.' Literally 'she dies of envy to meet you', this vivid idiom captures intense eagerness without sounding jealous."),
    (4, None, "'She is perfect for your new film.' Adding an extra silent letter to 'perfect' makes the final consonant sound out clearly when describing a female star in French."),
    (5, None, "'I refuse to work with this actress.' One pointer word covers both 'this' and 'that' in French, letting tone of voice carry Sacha's disdain."),
    (6, None, "'Why? She is an immense movie star.' French borrows 'star' straight from English for celebrities and introduces a full description after 'is' with 'it is' rather than 'she is'."),
    (7, None, "'She refused my first project in the past.' Ending with a single evocative word meaning 'formerly' or 'in bygone days' makes a four-year-old slight sound ancient."),
    (8, None, "'She sent me a very nasty message.' Notice how 'me' sits before 'has sent' in French, while 'message' is an easy cognate pronounced with a soft second syllable."),
    (9, None, "'Tell her that I am not interested.' Joining the command to 'to her' with a hyphen builds 'tell her', and that same attachment can mean 'tell him' too."),
    (10, None, "'Sacha, please, listen to me!' Unlike English, French needs no word meaning 'to' after 'listen' — the stressed 'me' attaches straight onto the command."),
    (11, None, "'So Andrea, what did he say?' Opening with 'so' or 'well then', Noemie uses a classic question starter that literally strings together 'what is it that'."),
    (12, None, "'Hartman is furious and refuses this meeting.' Notice the cognate 'furious' alongside a word meaning 'meeting' that is built from the action 'to meet'."),
    (13, None, "'That is a real disaster for our agency.' Both 'catastrophe' and 'agency' are transparent cognates, while 'our' keeps one short form before any single thing in French."),
]
