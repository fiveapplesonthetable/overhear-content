# Authoring module for dix-pour-cent-s02e02-scene-21.
ID = 'dix-pour-cent-s02e02-scene-21'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 2
SCENE = 21
TITLE = 'Visite surprise de Christophe Lambert  (Surprise Visit from Christophe Lambert)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'christophe': 'Christophe', 'mathias': 'Mathias', 'noemie': 'Noémie'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E02'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e02.fr.dual.srt'
INTRO = "Celebrated actor Christophe Lambert pays an unexpected visit to the ASK agency. Receptionist and assistant Noémie Leclerc is starstruck and eagerly asks for a commemorative photograph before Mathias whisks him into an office. Listen to the scene in French first. Don't worry about catching every word."
OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."
TRANSITION = "Now let's listen to the whole dialogue again."
OUTRO = 'Christophe Lambert charms the ASK office before heading off to read his new movie script. Remember the classic phrase for asking permission: je peux followed by an infinitive. See you next time!'
CLOSING = ('christophe', 'À bientôt!')
STORY = [
    ('noemie', "Oh mon Dieu, c'est Christophe Lambert!", 'Oh my goodness, it is Christophe Lambert!', [(718, 'Oh mon Dieu')], ''),
    ('christophe', 'Bonjour Noémie! Comment tu vas?', 'Hello Noémie! How are you doing?', [(714, 'Noémie ! Comment tu vas ?')], ''),
    ('noemie', 'Je vais très bien, merci beaucoup.', 'I am doing very well, thank you very much.', [(721, '-Tu es très émotive. -Oui')], ''),
    ('noemie', 'Je peux prendre une photo avec vous?', 'Can I take a photo with you?', [(722, 'Je peux prendre une photo ?')], ''),
    ('christophe', 'Oui, pas de problème avec plaisir!', 'Yes, no problem with pleasure!', [(723, 'Oui !'), (725, 'Pas de problème')], ''),
    ('noemie', 'Je suis une très grande fan.', 'I am a very big fan.', [(726, 'je suis fan de vous')], ''),
    ('christophe', 'Moi aussi, je suis très sympa.', 'Me too, I am very friendly.', [(727, 'Moi aussi je suis timide, mais je suis sympa')], ''),
    ('noemie', 'Mettez-vous plus près. Grand sourire!', 'Get closer. Big smile!', [(728, 'Plus près'), (729, 'Voilà. Grand sourire')], ''),
    ('mathias', 'Salut Christophe! Viens par ici.', 'Hi Christophe! Come this way.', [(731, '-Salut, Christophe'), (734, '-Par ici')], ''),
    ('christophe', "Mathias! C'est un plaisir de te voir.", 'Mathias! It is a pleasure to see you.', [(731, '-Mathias !'), (732, '-Comment tu vas ? -Bien')], ''),
    ('mathias', 'Le réalisateur te veut pour ce rôle.', 'The director wants you for this role.', [(736, 'Il te veut pour le rôle')], ''),
    ('mathias', 'Lis le scénario ce soir.', 'Read the script tonight.', [(741, 'Lis le scénario')], ''),
    ('christophe', "D'accord, je vais le lire rapidement.", 'All right, I will read it quickly.', [(743, 'Ouais, bien sûr')], ''),
    ('christophe', "À tout à l'heure Mathias. Au revoir!", 'See you later Mathias. Goodbye!', [(752, "À tout à l'heure, Mathias !"), (754, 'Au revoir')], ''),
]
WALK = [
    (0, None, "'Oh my goodness, it is Christophe Lambert!' Mon Dieu literally says 'my God', and c'est introduces who just walked in."),
    (1, None, "'Hello Noémie! How are you doing?' Lambert greets her informally: comment tu vas uses tu and vas from aller, 'to go'."),
    (2, None, "'I am doing very well, thank you very much.' Je vais très bien answers with aller again, literally 'I go very well', plus beaucoup, 'a lot'."),
    (3, None, "'Can I take a photo with you?' Je peux comes from pouvoir, 'can', followed by prendre, 'to take', while Noémie stays polite with vous."),
    (4, None, "'Yes, no problem with pleasure!' Lambert pairs pas de problème, 'no problem', with avec plaisir, 'with pleasure'."),
    (5, None, "'I am a very big fan.' Noémie uses the feminine article une and grande with a silent-no-longer final d because she is talking about herself."),
    (6, None, "'Me too, I am very friendly.' Moi aussi means 'me too', and sympa is everyday spoken French short for sympathique, 'nice' or 'friendly'."),
    (7, None, "'Get closer. Big smile!' Mettez-vous is the polite vous command of se mettre, and plus près means 'closer' before sourire, 'smile'."),
    (8, None, "'Hi Christophe! Come this way.' Mathias switches to casual salut and viens, the tu command of venir, 'to come', with par ici, 'this way'."),
    (9, None, "'Mathias! It is a pleasure to see you.' Un plaisir de te voir links plaisir, 'pleasure', to voir, 'to see', with te for 'you'."),
    (10, None, "'The director wants you for this role.' Réalisateur is a film director, and te veut puts the object pronoun te right before veut from vouloir."),
    (11, None, "'Read the script tonight.' Lis is the tu imperative of lire, 'to read', paired with le scénario, 'the script', and ce soir, 'tonight'."),
    (12, None, "'All right, I will read it quickly.' Lambert uses near-future je vais lire, 'I am going to read', tucking le, 'it', before the infinitive."),
    (13, None, "'See you later Mathias. Goodbye!' À tout à l'heure is used when you will see someone again later the same day."),
]
