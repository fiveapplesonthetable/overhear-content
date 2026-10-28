# Authoring module for dix-pour-cent-s02e01-scene-15.
ID = 'dix-pour-cent-s02e01-scene-15'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 1
SCENE = 15
TITLE = "L'ultimatum du producteur  (The Producer's Ultimatum)"
LEVEL = "A1 — débutant"
PAIR = 'fr-en'
VOICES = {"narrator": "sky", "michel": "marcel", "camille": "emilie"}
LABELS = {"michel": "Michel", "camille": "Camille"}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E01'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e01.fr.dual.srt'
INTRO = "In Mathias's office, the telephone rings with an explosive call from movie producer Michel. Ramzy Bedia has vanished just one week before the premiere, and Michel delivers an uncompromising threat. Let's listen to the scene in French first."
OPENER = 'The producer loses his temper. Let us examine the lines with English notes.'
TRANSITION = 'Now listen to the heated exchange once more from beginning to end.'
OUTRO = 'With a lawsuit looming over ASK, Mathias urgently needs to track down Ramzy and calm the producer. Soon after, Gabriel approaches Mathias to propose a truce. See you next time!'
CLOSING = ("camille", "Bonne soirée!")
STORY = [
    ('michel', "Mathias, tu as l'air d'avoir mal compris.", 'Mathias, you seem to have misunderstood.', [(422, "tu as l'air d'avoir mal compris")], ''),
    ('michel', 'Ramzy ne répond plus jamais à mes appels!', 'Ramzy never answers my calls anymore!', [(423, 'Ramzy ne répond plus à mes appels et je suis le producteur du film')], ''),
    ('michel', 'Il a disparu une semaine avant la sortie.', 'He has disappeared a week before the release.', [(424, 'Il a disparu une semaine avant la sortie')], ''),
    ('camille', 'Virginie fait la promotion, non?', 'Virginie is doing the promotion, right?', [(426, 'Virginie fait la promotion, non')], ''),
    ('michel', 'Tu plaisantes? Elle est comme un zombie!', 'Are you kidding? She is like a zombie!', [(427, 'Tu plaisantes ? Elle est comme un zombie')], ''),
    ('michel', 'Pas une seule photo utilisable!', 'Not a single usable photo!', [(428, 'Pas une seule photo utilisable')], ''),
    ('michel', 'On sort une comédie la semaine prochaine!', 'We are releasing a comedy next week!', [(430, 'On sort une comédie, la semaine prochaine')], ''),
    ('michel', 'Agissez de manière responsable!', 'Act in a responsible manner!', [(431, 'Agissez de manière responsable')], ''),
    ('camille', 'Michel, tu as tout à fait raison.', 'Michel, you are completely right.', [(432, 'Michel, tu as tout à fait raison')], ''),
    ('camille', 'Je raccroche et je trouve Ramzy.', 'I hang up and I find Ramzy.', [(432, 'Je raccroche')], ''),
    ('michel', "S'il ne fait pas l'émission de Drucker cette semaine, je l'attaque!", 'If he does not do Drucker', [(434, "S'il ne fait pas l'émission de Drucker cette semaine"), (435, "je l'attaque pour rupture de contrat")], ''),
    ('camille', "Ne t'inquiète pas, il sera là.", 'Do not worry, he will be there.', [], ''),
    ('camille', "C'est une catastrophe, Mathias!", 'It is a disaster, Mathias!', [], ''),
    ('camille', 'Je dois régler ce problème immédiatement.', 'I must settle this problem immediately.', [], ''),
]
WALK = [
    (0, None, "'Mathias, you seem to have misunderstood.' Michel opens with the word for 'have' and lands on 'understood' at the close."),
    (1, None, "'Ramzy never answers my calls anymore!' Repondre a means to answer."),
    (2, None, "'He has disappeared a week before the release.' The key word here means 'has', paired with 'release' to make the point clear."),
    (3, None, "'Virginie is doing the promotion, right?' Mathias pairs the verb meaning 'does' with the noun for 'promotion'."),
    (4, None, "'Are you kidding? She is like a zombie!' Listen for the expression meaning 'are joking', which leads naturally into 'zombie'."),
    (5, None, "'Not a single usable photo!' The adjective meaning 'single' agrees in gender and number with feminine noun 'photo'."),
    (6, None, "'We are releasing a comedy next week!' Michel opens with the word for 'release' and lands on 'next' at the close."),
    (7, None, "'Act in a responsible manner!' The key word here means 'act', paired with 'responsible' to make the point clear."),
    (8, None, "'Michel, you are completely right.' The key word here means 'have', paired with 'right' to make the point clear."),
    (9, None, "'I hang up and I find Ramzy.' The verb meaning 'hang up' anchors the whole remark."),
    (10, None, "'If he does not do Drucker's show this week, I will sue him!' Notice how the verb for 'does' leads straight into 'week'."),
    (11, None, "'Do not worry, he will be there.' Mathias opens with the word for 'not' and lands on 'there' at the close."),
    (12, None, "'It is a disaster, Mathias!' Camille reacts with alarm to the legal threat."),
    (13, None, "'I must settle this problem immediately.' Listen for the expression meaning 'must', which leads naturally into 'immediately'."),
]
