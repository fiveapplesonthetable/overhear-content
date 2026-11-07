# Authoring module for hotel-du-tilleul-s02e02-scene-04.
ID = 'hotel-du-tilleul-s02e02-scene-04'
SHOW = 'hotel-du-tilleul'
SEASON = 2
EPISODE = 2
SCENE = 4
TITLE = "Jeudi, c'est aujourd'hui?  (Thursday Means Today?)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'etienne': 'Étienne', 'henri': 'Henri'}
INTRO = ('Back at the Hotel du Tilleul, Henri is stripping clean copper wire on a stool when Etienne strolls up to '
         'the front desk beaming with pride over his telephone bargain. Listen first.')
OPENER = "Let's hear Etienne's great bargain again, piece by piece."
TRANSITION = "Now let's hear the whole conversation again."
OUTRO = ('Without his glasses, Etienne ordered twenty-four chairs for Saturday afternoon instead of Thursday, and '
         'the delivery van is already at the gate! See you next time.')
CLOSING = ('henri', 'Bon courage!')
STORY = [
    ('etienne',
     "Félicitez-moi, Henri! J'ai trouvé des chaises de jardin pliantes en bois à moitié prix!",
     'Congratulate me, Henri! I found folding wooden garden chairs at half price!'),
    ('henri',
     'À moitié prix? Pourquoi je suis déjà nerveux quand vous dites ça?',
     'Half price? Why do I already feel nervous when you say that?'),
    ('etienne',
     'Parce que le magasin donne ce prix seulement pour deux douzaines!',
     'Because the shop only gives that price for two dozen!'),
    ('henri',
     'Deux douzaines? Patron, deux douzaines, ça fait vingt-quatre chaises!',
     'Two dozen? Boss, two dozen makes twenty-four chairs!'),
    ('etienne',
     'Douze pour la chambre neuf, huit pour la cour, et quatre pour... les urgences!',
     'Twelve for Room Nine, eight for the courtyard, and four for... emergencies!'),
    ('henri',
     "Mais où est-ce qu'on range vingt-quatre chaises pendant qu'on peint toute la semaine?",
     'But where do we put away twenty-four chairs while we paint all week?'),
    ('etienne',
     "Du calme! J'ai dit au chauffeur de les apporter jeudi prochain, l'après-midi.",
     'Relax! I told the driver to bring them next Thursday, in the afternoon.'),
    ('henri',
     'Attendez, qui vient de garer une camionnette devant notre portail?',
     'Wait, who just parked a van in front of our gate?'),
    ('etienne',
     'Une camionnette bleue? Pourquoi il y a des chaises dessinées sur le côté?',
     'A blue van? Why are there chairs painted on the side?'),
    ('henri',
     'Montrez-moi votre carnet... patron, vous avez entouré samedi, quatorze heures!',
     'Show me your notepad... boss, you circled Saturday, two in the afternoon!'),
    ('etienne',
     "J'ai lu la mauvaise colonne sans mes lunettes! Ils les déchargent maintenant!",
     'I read the wrong column without my glasses! They are unloading them now!'),
    ('henri',
     'Vingt-quatre chaises en bois dans notre petite cour... bravo, patron!',
     'Twenty-four wooden chairs in our little courtyard... well done, boss!'),
]
WALK = [
    (0, None,
     ["'Congratulate me, Henri! I found folding wooden garden chairs at half price!' Look out for",
      (None, 'à moitié prix'),
      "literally 'at half price', the chunk you'll see on sale signs in every shop window."]),
    (1, None,
     "'Half price? Why do I already feel nervous when you say that?' Spoken French often keeps the normal "
     "word order after 'why' and simply lets the voice rise to ask."),
    (3, None,
     ["'Two dozen? Boss, two dozen makes twenty-four chairs!' To do sums out loud, Henri says",
      (None, 'ça fait'),
      "literally 'that makes', exactly what a shopkeeper says at the till."]),
    (5, None,
     ["'But where do we put away twenty-four chairs while we paint all week?' Henri's",
      (None, 'on range'),
      "means 'we put away', the same word French parents use when they tell children to tidy up."]),
    (7, None,
     ["'Wait, who just parked a van in front of our gate?' Henri's",
      (None, 'qui vient de garer'),
      "literally 'who comes from parking', is how French talks about something that happened seconds ago."]),
    (9, None,
     ["'Show me your notepad... boss, you circled Saturday, two in the afternoon!' French timetables count "
      "to twenty-four, so two in the afternoon is",
      (None, 'quatorze heures'),
      "'fourteen hours'."]),
    (11, None,
     ["'Twenty-four wooden chairs in our little courtyard... well done, boss!' Henri's",
      (None, 'bravo'),
      "is pure irony here: the word for 'well done', said in a flat voice, means the opposite."]),
]
