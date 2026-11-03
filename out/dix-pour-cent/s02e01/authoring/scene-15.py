# Authoring module for dix-pour-cent-s02e01-scene-15.
ID = 'dix-pour-cent-s02e01-scene-15'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 1
SCENE = 15
TITLE = "L'ultimatum du producteur  (The Producer's Ultimatum)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'mathias': 'Mathias', 'michel': 'Michel'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E01'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e01.fr.dual.srt'
INTRO = "In Mathias's office, the telephone rings with an explosive call from movie producer Michel. Ramzy Bedia has vanished just one week before the premiere, and Michel delivers an uncompromising threat. Let's listen to the scene in French first."
OPENER = 'The producer loses his temper. Let us examine the lines with English notes.'
TRANSITION = 'Now listen to the heated exchange once more from beginning to end.'
OUTRO = 'With a lawsuit looming over ASK, Mathias urgently needs to track down Ramzy and calm the producer. Soon after, Gabriel approaches Mathias to propose a truce. See you next time!'
CLOSING = ('mathias', 'Bonne soirée!')
STORY = [
    ('michel', "Mathias, tu as l'air d'avoir mal compris.", 'Mathias, you seem to have misunderstood.', [(422, "tu as l'air d'avoir mal compris")], ''),
    ('michel', 'Ramzy ne répond plus jamais à mes appels!', 'Ramzy never answers my calls anymore!', [(423, 'Ramzy ne répond plus à mes appels et je suis le producteur du film')], ''),
    ('michel', 'Il a disparu une semaine avant la sortie.', 'He has disappeared a week before the release.', [(424, 'Il a disparu une semaine avant la sortie')], ''),
    ('mathias', 'Virginie fait la promotion, non?', 'Virginie is doing the promotion, right?', [(426, 'Virginie fait la promotion, non')], ''),
    ('michel', 'Tu plaisantes? Elle est comme un zombie!', 'Are you kidding? She is like a zombie!', [(427, 'Tu plaisantes ? Elle est comme un zombie')], ''),
    ('michel', 'Pas une seule photo utilisable!', 'Not a single usable photo!', [(428, 'Pas une seule photo utilisable')], ''),
    ('michel', 'On sort une comédie la semaine prochaine!', 'We are releasing a comedy next week!', [(430, 'On sort une comédie, la semaine prochaine')], ''),
    ('michel', 'Agissez de manière responsable!', 'Act in a responsible manner!', [(431, 'Agissez de manière responsable')], ''),
    ('mathias', 'Michel, tu as tout à fait raison.', 'Michel, you are completely right.', [(432, 'Michel, tu as tout à fait raison')], ''),
    ('mathias', 'Je raccroche et je trouve Ramzy.', 'I hang up and I find Ramzy.', [(432, 'Je raccroche')], ''),
    ('michel', "S'il ne fait pas l'émission de Drucker cette semaine, je l'attaque!", "If he does not do Drucker's show this week, I will sue him!", [(434, "S'il ne fait pas l'émission de Drucker cette semaine"), (435, "je l'attaque pour rupture de contrat")], ''),
    ('mathias', "Ne t'inquiète pas, il sera là.", 'Do not worry, he will be there.', [], ''),
    ('camille', "C'est une catastrophe, Mathias!", 'It is a disaster, Mathias!', [], ''),
    ('mathias', 'Je dois régler ce problème immédiatement.', 'I must settle this problem immediately.', [], ''),
]
WALK = [
    (0, ('michel', 'compris.'), "'Mathias, you seem to have misunderstood.' The film producer tells Mathias he has misunderstood, using the past participle to understand."),
    (1, ('michel', 'jamais'), "'Ramzy never answers my calls anymore!' Michel fumes that Ramzy is ignoring him, using the word for never."),
    (2, ('michel', 'disparu'), "'He has disappeared a week before the release.' He complains that his lead actor has vanished, using the past participle to disappear."),
    (3, ('mathias', 'promotion,'), "'Virginie is doing the promotion, right?' Mathias points out that she is doing the promotion, using this similar noun."),
    (4, ('michel', 'zombie!'), "'Are you kidding? She is like a zombie!' He compares her to a lifeless creature with this noun."),
    (5, ('michel', 'photo'), "'Not a single usable photo!' He complains they cannot use any picture, using the noun for photo."),
    (6, ('michel', 'semaine'), "'We are releasing a comedy next week!' He reminds them of the schedule, using the word for week."),
    (7, ('michel', 'manière'), "'Act in a responsible manner!' He urges them to act properly using the word for manner or way."),
    (8, ('mathias', 'raison.'), "'Michel, you are completely right.' Mathias tries to calm him down, telling him he is right with this noun meaning reason."),
    (9, ('mathias', 'raccroche'), "'I hang up and I find Ramzy.' Mathias promises immediate action, using the verb to hang up."),
    (10, ('michel', "l'attaque!"), "'If he does not do Drucker's show this week, I will sue him!' Michel threatens legal action using the verb to attack."),
    (11, ('mathias', "t'inquiète"), "'Do not worry, he will be there.' Mathias tells him not to worry with this verb."),
    (12, ('camille', 'catastrophe,'), "'It is a disaster, Mathias!' The assistant reacts to the tension using the word for disaster."),
    (13, ('mathias', 'problème'), "'I must settle this problem immediately.' Mathias vows to fix it using the noun for problem. Let's hear it once more."),
]
