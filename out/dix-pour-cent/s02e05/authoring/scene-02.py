# Authoring module for dix-pour-cent-s02e05-scene-02.
ID = 'dix-pour-cent-s02e05-scene-02'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 5
SCENE = 2
TITLE = 'Guy oublie son texte  (Guy Forgets His Lines)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'gabriel': 'Gabriel', 'guy': 'Guy', 'vera': 'Véra'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E05'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e05.fr.dual.srt'
INTRO = "On the movie set, director Vera Loiseau gives acting instructions to veteran star Guy Marchand. To everyone's surprise, Guy experiences sudden confusion, failing to recognize his director and leaving the set. Let's listen to the scene in French first."
OPENER = "Let's examine how Guy's sudden confusion disrupts the movie rehearsal."
TRANSITION = "Now let's listen to the whole dialogue again."
OUTRO = "Guy's sudden disorientation shocks director Vera and raises immediate alarm for Gabriel. Realizing that something is medically wrong with his star client, Gabriel seeks immediate medical help. See you next time!"
CLOSING = ('guy', 'Au revoir, Gabriel.')
STORY = [
    ('vera', 'Bonjour Guy, nous tournons la scène trente-quatre.', 'Hello Guy, we are shooting scene thirty-four.', [(40, 'Nous sommes à la scène 34.')], ''),
    ('vera', 'Votre personnage doit changer de vêtements ici.', 'Your character must change clothes here.', [(46, 'vous quittiez votre pyjama pour enfiler votre costume,')], ''),
    ('vera', 'Vous quittez votre pyjama pour votre costume.', 'You take off your pajamas for your suit.', [(46, 'vous quittiez votre pyjama pour enfiler votre costume,')], ''),
    ('guy', 'De quoi parlez-vous exactement, jeune fille?', 'What are you talking about exactly, young girl?', [(48, 'De quoi vous parlez ?')], ''),
    ('guy', 'Cette femme me demande de me déshabiller!', 'This woman is asking me to strip!', [(51, "vient me voir et, sans crier gare, me dit qu'elle veut que je me déshabille.")], ''),
    ('gabriel', 'Guy, calme-toi, tout va très bien.', 'Guy, calm down, everything is going very well.', [(54, '-Vous vous sentez bien ?')], ''),
    ('guy', 'Gabriel, cette inconnue a beaucoup de culot.', 'Gabriel, this stranger has a lot of nerve.', [(56, 'Elle a du culot, celle-là.')], ''),
    ('gabriel', "Mais c'est Véra, la réalisatrice du film!", 'But that is Vera, the director of the film!', [(58, "Guy, cette femme, c'est Véra. Elle est..."), (59, "C'est Véra Loiseau, la réalisatrice du film.")], ''),
    ('guy', "Non, je ne l'ai jamais vue auparavant.", 'No, I have never seen her before.', [(61, "on ne s'est jamais rencontrés.")], ''),
    ('gabriel', 'Vous avez pourtant travaillé ensemble la semaine dernière.', 'Yet you worked together last week.', [(61, "on ne s'est jamais rencontrés.")], ''),
    ('guy', 'Je me sens un peu fatigué maintenant.', 'I feel a bit tired now.', [(63, "Tu as l'air un peu stressé.")], ''),
    ('guy', 'Je préfère rentrer chez moi tout de suite.', 'I prefer to go home right away.', [(65, 'Bon, je rentre à la maison maintenant.')], ''),
    ('gabriel', 'Attends Guy, nous devons tourner cette scène!', 'Wait Guy, we must shoot this scene!', [(72, 'Guy !')], ''),
    ('guy', 'Non, nous parlerons plus tard au téléphone.', 'No, we will talk later on the phone.', [(66, 'On se parlera par téléphone.')], ''),
]
WALK = [
    (0, None, "'Hello Guy, we are shooting scene thirty-four.' Unlike English, French puts 'the' right before 'scene thirty-four', and 'shooting' literally means 'turning' the camera."),
    (1, None, "'Your character must change clothes here.' Watch out for a classic false friend: the subject looks like 'personage', yet in French it means a fictional character in a story or film."),
    (2, None, "'You take off your pajamas for your suit.' Another false friend sits at the end: the word spelled like 'costume' actually means an ordinary business suit in French, while 'leaving' clothes means taking them off."),
    (3, None, "'What are you talking about exactly, young girl?' Rather than stranding 'about' at the end, French opens right away with 'of what', showing how disoriented Guy suddenly is."),
    (4, None, "'This woman is asking me to strip!' That last action is built from an 'un-' prefix attached to 'dress', literally 'to undress myself'."),
    (5, None, "'Guy, calm down, everything is going very well.' Gabriel tacks 'yourself' onto 'calm' to soothe his friend, then adds 'everything goes very well' — a handy chunk for reassuring someone."),
    (6, None, "'Gabriel, this stranger has a lot of nerve.' Here 'stranger' comes from 'unknown', and 'having nerve' uses a lively everyday idiom for brazen cheek."),
    (7, None, "'But that is Vera, the director of the film!' In French, a movie director is literally 'the realizer' — the person who brings the script into reality on screen."),
    (8, None, "'No, I have never seen her before.' In the negative, French wraps 'never' around 'have', tucking the contracted 'her' right before 'have' rather than after 'seen'."),
    (9, None, "'Yet you worked together last week.' Notice the word order at the end: French says 'the week last', keeping 'the' and placing 'last' after 'week'."),
    (10, None, "'I feel a bit tired now.' Literally 'I feel myself a bit tired': without 'myself', that same action in French can mean 'I smell'!"),
    (11, None, "'I prefer to go home right away.' Instead of a separate word meaning 'home', French uses 'to my place', capped off by an expression that literally means 'all in sequence' for 'right away'."),
    (12, None, "'Wait Guy, we must shoot this scene!' Gabriel opens with a classic false friend: it looks just like English 'attend', yet in French it always means 'wait'."),
    (13, None, "'No, we will talk later on the phone.' French builds 'later' from 'more late', and says 'at the phone' where English says 'on the phone'."),
]
