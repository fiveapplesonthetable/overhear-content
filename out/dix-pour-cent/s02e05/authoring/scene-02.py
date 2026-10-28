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
TRANSITION = "Now let's listen to Guy's alarming misunderstanding on set again at full speed."
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
    (0, None, "'Hello Guy, we are shooting scene thirty-four.' The director announces the current production sequence."),
    (1, None, "'Your character must change clothes here.' An explanation of physical character blocking in the scene."),
    (2, None, "'You take off your pajamas for your suit.' A specific costume change instruction symbolizing political return."),
    (3, None, "'What are you talking about exactly, young girl?' A bewildered question showing sudden disorientation."),
    (4, None, "'This woman is asking me to strip!' A dramatic misinterpretation reflecting acute cognitive confusion."),
    (5, None, "'Guy, calm down, everything is going very well.' A soothing intervention attempting to de-escalate tension."),
    (6, None, "'Gabriel, this stranger has a lot of nerve.' A dismissive complaint about someone he suddenly fails to recognize."),
    (7, None, "'But that is Vera, the director of the film!' Gabriel clarifies the director's key authority on set."),
    (8, None, "'No, I have never seen her before.' An alarming memory lapse denying prior collaboration."),
    (9, None, "'Yet you worked together last week.' Gabriel gently reminds him of their recent work meetings."),
    (10, None, "'I feel a bit tired now.' A defensive retreat acknowledging physical weakness."),
    (11, None, "'I prefer to go home right away.' A hasty departure avoiding public embarrassment."),
    (12, None, "'Wait Guy, we must shoot this scene!' An anxious plea trying to salvage the shooting schedule."),
    (13, None, "'No, we will talk later on the phone.' A stubborn dismissal cutting short on-set conversation."),
]
