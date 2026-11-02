# Authoring module for dix-pour-cent-s02e05-scene-03.
ID = 'dix-pour-cent-s02e05-scene-03'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 5
SCENE = 3
TITLE = 'Le diagnostic du médecin  (Minor Stroke)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'gabriel': 'Gabriel', 'guy': 'Guy', 'medecin': 'Le médecin'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E05'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e05.fr.dual.srt'
INTRO = "In the examination room, a doctor explains the test results to Guy Marchand and his agent Gabriel. While Guy is relieved that he does not have Alzheimer's disease, the doctor warns that his minor stroke will cause lingering confusion. Let's listen to the scene in French first."
OPENER = "Let's examine how the doctor explains Guy Marchand's medical diagnosis."
TRANSITION = "Now let's listen to the whole dialogue again."
OUTRO = 'The diagnosis of a minor stroke relieves Guy but leaves Gabriel deeply concerned about the production. Keeping Guy on set without risking another public incident will test the agency to its limits. See you next time!'
CLOSING = ('guy', 'À bientôt!')
STORY = [
    ('medecin', "Regardez les examens, ce n'est pas Alzheimer.", "Look at the tests, it is not Alzheimer's.", [(77, "Ce n'est pas Alzheimer.")], ''),
    ('medecin', "Ce n'est pas une maladie neurodégénérative grave.", 'It is not a serious neurodegenerative disease.', [(78, "Ce n'est pas une maladie neurodégénérative.")], ''),
    ('gabriel', "C'est donc une bonne nouvelle, docteur?", 'So that is good news, doctor?', [(80, 'En quoi est-ce une bonne nouvelle ?')], ''),
    ('medecin', 'Vous avez simplement eu un petit AVC.', 'You simply had a minor stroke.', [(83, 'Vous avez eu un petit AVC.')], ''),
    ('medecin', "Un petit vaisseau sanguin s'est bouché.", 'A small blood vessel got blocked.', [(84, "Un vaisseau s'est bouché,")], ''),
    ('medecin', 'Cela explique votre récente confusion au travail.', 'That explains your recent confusion at work.', [(87, "D'où votre confusion récente.")], ''),
    ('guy', 'Est-ce que cela va passer vite?', 'Will that pass quickly?', [(81, 'Ça va passer.')], ''),
    ('medecin', "Oui, cela va s'améliorer avec le temps.", 'Yes, that will improve with time.', [(82, "Ça va s'améliorer tout seul, avec le temps.")], ''),
    ('guy', 'Formidable, je vais très bien dormir ce soir.', 'Wonderful, I am going to sleep very well tonight.', [(89, 'Parfait !'), (95, 'Une bonne nuit de sommeil, un bol de muesli au petit-déjeuner,')], ''),
    ('guy', "Et demain matin, j'irai tourner à vélo!", 'And tomorrow morning, I will go shoot by bike!', [(97, "j'irai au plateau à vélo, bien en avance !")], ''),
    ('medecin', 'Attention, vous aurez encore des moments de confusion.', 'Watch out, you will still have moments of confusion.', [(102, 'M. Marchand aura des périodes de flottement,'), (103, 'de confusion...')], ''),
    ('gabriel', 'Des moments de confusion pendant le tournage?', 'Moments of confusion during filming?', [(104, 'Les semaines à venir ?')], ''),
    ('medecin', 'Oui, pendant les prochaines semaines à venir.', 'Yes, over the coming weeks.', [(99, 'ça sera résorbé dans les semaines à venir.')], ''),
    ('gabriel', 'Merci docteur, nous allons être très prudents.', 'Thank you doctor, we are going to be very careful.', [(110, 'On vous laisse vous occuper de ceux qui en ont vraiment besoin.')], ''),
]
WALK = [
    (0, None, "'Look at the tests, it is not Alzheimer's.' Unlike English, French needs no 'at' after 'look' — it says 'look the exams' directly, using the same word for medical scans and school tests."),
    (1, None, "'It is not a serious neurodegenerative disease.' Both descriptions come after 'illness' in French, ending on a cognate of 'grave' that simply means 'serious' in everyday speech."),
    (2, None, "'So that is good news, doctor?' Where English treats 'news' as uncountable, French counts a single update as 'a good new thing', built from the everyday word meaning 'new'."),
    (3, None, "'You simply had a minor stroke.' Notice how 'simply' wedges right between 'have' and 'had', while French speakers refer to a stroke by a three-letter medical abbreviation softened here by 'little'."),
    (4, None, "'A small blood vessel got blocked.' You can spot a cognate of 'vessel' paired with 'blood-related', while 'got blocked' comes from the same root as a bottle cork."),
    (5, None, "'That explains your recent confusion at work.' Three cognates in a row make this diagnosis easy to follow, and 'at work' literally says 'at the work' in French."),
    (6, None, "'Will that pass quickly?' Guy builds the near future from 'goes to pass', ending on a single brisk word that covers both 'fast' and 'quickly' in French."),
    (7, None, "'Yes, that will improve with time.' Here 'improve' is a cousin of English 'ameliorate', and French says 'with the time' rather than bare 'with time'."),
    (8, None, "'Wonderful, I am going to sleep very well tonight.' In French, that opening cognate means 'terrific' rather than intimidating, and 'very well' sits right before 'to sleep' instead of at the end."),
    (9, None, "'And tomorrow morning, I will go shoot by bike!' French packs 'I will go' into a single word after 'tomorrow morning', followed straight away by 'to shoot' with no 'and' in between."),
    (10, None, "'Watch out, you will still have moments of confusion.' Used on its own at the start, that cognate of 'attention' means 'careful!' or 'watch out!', and the word after 'will have' can mean either 'still' or 'again'."),
    (11, None, "'Moments of confusion during filming?' Unlike English, French almost never leaves 'moments' bare at the start — it puts an untranslated 'some' right out front."),
    (12, None, "'Yes, over the coming weeks.' Word for word, the doctor says 'during the next weeks to come', pairing 'next' before 'weeks' with 'to come' right after."),
    (13, None, "'Thank you doctor, we are going to be very careful.' What looks like formal English 'prudent' is simply how you'd say 'careful' in everyday French."),
]
