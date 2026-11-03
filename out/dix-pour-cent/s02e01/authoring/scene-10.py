# Authoring module for dix-pour-cent-s02e01-scene-10.
ID = 'dix-pour-cent-s02e01-scene-10'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 1
SCENE = 10
TITLE = 'Ramzy boycotte la promotion  (Ramzy Boycotts the Promotion)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'mathias': 'Mathias', 'ramzy': 'Ramzy'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E01'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e01.fr.dual.srt'
INTRO = "Inside the elevator at ASK, Mathias rides down with an enraged Ramzy Bedia. Their romantic comedy is opening in theatres, but Ramzy flatly refuses to appear next to Virginie Efira for promotional interviews or press photos. Mathias tries every philosophical trick to change his mind. Let's listen to the scene in French first."
OPENER = "Let's observe Mathias trying to save a movie campaign with high-minded philosophy."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "Mathias's philosophical speech did not convince Ramzy at all. See you next time!"
CLOSING = ('mathias', 'Bonne soirée!')
STORY = [
    ('ramzy', 'Je ne veux pas la voir.', 'I do not want to see her.', [(270, 'Je ne veux pas la voir.')], ''),
    ('ramzy', "Les interviews, les photos pour le film, c'est hors de question.", 'Interviews, photos for the film, it is out of the question.', [(271, 'Les interviews, les photos promo pour le film... hors de question.')], ''),
    ('mathias', 'Sans promotion, le film va être un échec.', 'Without promotion, the film is going to be a failure.', [(272, 'Sans promotion, le film va faire un flop.')], ''),
    ('mathias', "C'est mauvais pour tout le monde.", 'It is bad for everyone.', [(272, "C'est mauvais pour tout le monde.")], ''),
    ('ramzy', "Ce qu'elle a fait est impardonnable.", 'What she did is unforgivable.', [(273, "Désolé, ce qu'elle a fait est impardonnable.")], ''),
    ('mathias', 'Ça dépend de ton école de pensée.', 'That depends on your school of thought.', [(274, 'Ça dépend de votre école.'), (276, 'École de pensée')], ''),
    ('ramzy', 'Quelle école de pensée?', 'What school of thought?', [(275, 'Quelle école ?')], ''),
    ('mathias', "Ton corps t'appartient. On ne possède pas quelqu'un.", 'Your body belongs to you. You do not own someone.', [(277, "Genre on ne possède pas quelqu'un, ton corps t'appartient.")], ''),
    ('mathias', "L'infidélité n'existe pas vraiment.", 'Infidelity does not really exist.', [(278, "L'infidélité n'existe pas. Ni la fidélité.")], ''),
    ('mathias', 'Tu pourrais promouvoir la paix et le progrès!', 'You could promote peace and progress!', [(280, 'Tu pourrais promouvoir la paix, le progrès')], ''),
    ('ramzy', 'Non! Pas du tout!', 'No! Not at all!', [(281, 'Non ?')], ''),
    ('camille', 'Bonjour, Ramzy! Bonne journée!', 'Hello, Ramzy! Have a nice day!', [(283, 'Bonne journée, Ramzy !')], ''),
    ('ramzy', 'Au revoir.', 'Goodbye.', [], ''),
    ('mathias', 'Il refuse tout, Camille.', 'He refuses everything, Camille.', [], ''),
    ('camille', 'Il ne veut vraiment pas faire la promotion?', 'Does he really not want to do the promotion?', [], ''),
    ('mathias', "Rien du tout. C'est une catastrophe.", 'Nothing at all. It is a disaster.', [], ''),
]
WALK = [
    (0, ('ramzy', 'voir'), "Ramzy refuses flatly to see Virginie, using the action word for 'see'."),
    (1, ('ramzy', 'film'), "Ramzy states that photos for the film are out of the question. The word for 'film' is almost identical in French."),
    (2, ('mathias', 'échec'), "Mathias warns that without promotion, the movie is going to be a failure. The word for 'failure' is used here."),
    (3, ('mathias', 'mauvais'), "Mathias warns Ramzy that the scandal is bad for everyone. The describing word for 'bad' is used here."),
    (4, ('ramzy', 'impardonnable'), "Ramzy declares that what she did is unforgivable. Notice the word for 'unforgivable'."),
    (5, ('mathias', 'école'), "Mathias switches to philosophical persuasion, mentioning a school of thought. The word for 'school' is used here."),
    (6, ('ramzy', 'Quelle'), "Ramzy asks sceptically what school of thought. The word for 'what' is used here."),
    (7, ('mathias', 'corps'), "Mathias states core principles of personal autonomy, starting with the body. The naming word for 'body' is used here."),
    (8, ('mathias', "L'infidélité"), "Mathias tries to argue that infidelity does not really exist, using this word."),
    (9, ('mathias', 'paix'), "Mathias argues grandly that forgiving Virginie would promote peace and progress. The word for 'peace' is used here."),
    (10, ('ramzy', 'Pas du tout'), "Ramzy rejects the argument completely, saying 'not at all'."),
    (11, ('camille', 'journée'), "Camille cheerfully greets the client as the elevator doors open, wishing him a nice day. The word for 'day' is used here."),
    (12, ('ramzy', 'Au revoir'), "Ramzy mutters a curt farewell as he storms off into the corridor, saying goodbye."),
    (13, ('mathias', 'tout'), "Mathias sighs with deep frustration, saying he refuses everything. The word for 'everything' is used here."),
    (14, ('camille', 'vraiment'), "Camille asks for confirmation if he really does not want to do the promotion. The word for 'really' is used here."),
    (15, ('mathias', 'catastrophe'), "Mathias sums up the hopeless situation by calling it a disaster. Let's listen to this hilarious elevator exchange one more time."),
]
