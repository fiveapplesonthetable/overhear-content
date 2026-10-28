# Authoring module for dix-pour-cent-s02e05-scene-03.
ID = 'dix-pour-cent-s02e05-scene-03'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 5
SCENE = 3
TITLE = 'Le diagnostic du médecin  (Minor Stroke)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
VOICES = {'narrator': 'sky', 'medecin': 'theo', 'guy': 'marcel', 'lea': 'lucie'}
LABELS = {'medecin': 'Le médecin', 'guy': 'Guy', 'lea': 'Andréa'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E05'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e05.fr.dual.srt'
INTRO = "In the examination room, a doctor explains the test results to Guy Marchand and his agent Gabriel. While Guy is relieved that he does not have Alzheimer's disease, the doctor warns that his minor stroke will cause lingering confusion. Let's listen to the scene in French first."
OPENER = "Let's examine how the doctor explains Guy Marchand's medical diagnosis."
TRANSITION = "Now let's listen to the doctor's reassuring consultation again at full speed."
OUTRO = 'The diagnosis of a minor stroke relieves Guy but leaves Gabriel deeply concerned about the production. Keeping Guy on set without risking another public incident will test the agency to its limits. See you next time!'
CLOSING = ('guy', 'À bientôt!')
STORY = [
    ('medecin', "Regardez les examens, ce n'est pas Alzheimer.", 'Look at the tests, it is not Alzheimer', [(77, "Ce n'est pas Alzheimer.")], ''),
    ('medecin', "Ce n'est pas une maladie neurodégénérative grave.", 'It is not a serious neurodegenerative disease.', [(78, "Ce n'est pas une maladie neurodégénérative.")], ''),
    ('lea', "C'est donc une bonne nouvelle, docteur?", 'So that is good news, doctor?', [(80, 'En quoi est-ce une bonne nouvelle ?')], ''),
    ('medecin', 'Vous avez simplement eu un petit AVC.', 'You simply had a minor stroke.', [(83, 'Vous avez eu un petit AVC.')], ''),
    ('medecin', "Un petit vaisseau sanguin s'est bouché.", 'A small blood vessel got blocked.', [(84, "Un vaisseau s'est bouché,")], ''),
    ('medecin', 'Cela explique votre récente confusion au travail.', 'That explains your recent confusion at work.', [(87, "D'où votre confusion récente.")], ''),
    ('guy', 'Est-ce que cela va passer vite?', 'Will that pass quickly?', [(81, 'Ça va passer.')], ''),
    ('medecin', "Oui, cela va s'améliorer avec le temps.", 'Yes, that will improve with time.', [(82, "Ça va s'améliorer tout seul, avec le temps.")], ''),
    ('guy', 'Formidable, je vais très bien dormir ce soir.', 'Wonderful, I am going to sleep very well tonight.', [(89, 'Parfait !'), (95, 'Une bonne nuit de sommeil, un bol de muesli au petit-déjeuner,')], ''),
    ('guy', "Et demain matin, j'irai tourner à vélo!", 'And tomorrow morning, I will go shoot by bike!', [(97, "j'irai au plateau à vélo, bien en avance !")], ''),
    ('medecin', 'Attention, vous aurez encore des moments de confusion.', 'Watch out, you will still have moments of confusion.', [(102, 'M. Marchand aura des périodes de flottement,'), (103, 'de confusion...')], ''),
    ('lea', 'Des moments de confusion pendant le tournage?', 'Moments of confusion during filming?', [(104, 'Les semaines à venir ?')], ''),
    ('medecin', 'Oui, pendant les prochaines semaines à venir.', 'Yes, over the coming weeks.', [(99, 'ça sera résorbé dans les semaines à venir.')], ''),
    ('lea', 'Merci docteur, nous allons être très prudents.', 'Thank you doctor, we are going to be very careful.', [(110, 'On vous laisse vous occuper de ceux qui en ont vraiment besoin.')], ''),
]
WALK = [
    (0, None, "'Look at the tests, it is not Alzheimer's.' The doctor rules out a feared degenerative illness."),
    (1, None, "'It is not a serious neurodegenerative disease.' Reassuring medical terminology dismissing long-term dementia."),
    (2, None, "'So that is good news, doctor?' Gabriel seeks confirmation with a relief-seeking question."),
    (3, None, "'You simply had a minor stroke.' A clinical diagnosis identifying the medical episode."),
    (4, None, "'A small blood vessel got blocked.' A clear anatomical explanation of the transient ischemic attack."),
    (5, None, "'That explains your recent confusion at work.' The physician attributes the on-set disorientation."),
    (6, None, "'Will that pass quickly?' Guy inquires about the expected duration of recovery."),
    (7, None, "'Yes, that will improve with time.' A hopeful prognosis promising natural gradual healing."),
    (8, None, "'Wonderful, I am going to sleep very well tonight.' An optimistic reaction from the spirited veteran actor."),
    (9, None, "'And tomorrow morning, I will go shoot by bike!' Defiant athletic determination to return to work immediately."),
    (10, None, "'Watch out, you will still have moments of confusion.' A strict medical caution warning of temporary lapses."),
    (11, None, "'Moments of confusion during filming?' Gabriel spots the massive professional and financial risk."),
    (12, None, "'Yes, over the coming weeks.' A realistic timeline establishing the danger window for the film."),
    (13, None, "'Thank you doctor, we are going to be very careful.' Gabriel politely commits to vigilant monitoring."),
]
