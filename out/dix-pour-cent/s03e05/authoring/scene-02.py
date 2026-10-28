# Authoring module for dix-pour-cent-s03e05-scene-02.
ID = 'dix-pour-cent-s03e05-scene-02'
SHOW = 'dix-pour-cent'
SEASON = 3
EPISODE = 5
SCENE = 2
TITLE = "L'appel de Béatrice  (Béatrice's Call)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'beatrice': 'Béatrice'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S03E05'
SOURCE_FILE = 'sources/dix-pour-cent/s03/e05.fr.dual.srt'
INTRO = "At home with her newborn baby, Andrea Martel receives an urgent phone call from Beatrice Dalle. Facing an unannounced script modification on set, Beatrice asks her agent to step in immediately and protect her contractual boundaries. Let's listen to the scene in French first."
OPENER = "Let's observe as Beatrice alerts Andrea to the dispute on set."
TRANSITION = "Now let's listen to Beatrice and Andrea again at full speed."
OUTRO = "Andrea hangs up the phone, determined to resolve the creative impasse and stand up for Beatrice's artistic rights. When you watch the episode, listen out for the expressions meaning 'how are you doing' and 'large'. You'll catch them now. See you next time!"
CLOSING = ('andrea', 'À bientôt!')
STORY = [
    ('beatrice', "Allô Andréa, c'est Béatrice.", 'Hello Andrea, it is Beatrice.', [(25, "Allô, c'est Béatrice")], ''),
    ('andrea', 'Bonjour Béatrice, comment vas-tu?', 'Hello Beatrice, how are you doing?', [(26, "T'es toujours en congé mat, toi ?")], ''),
    ('beatrice', "J'ai un gros problème sur le tournage.", 'I have a big problem on the shoot.', [(34, "C'est sous le film de Pascal Birad, là")], ''),
    ('andrea', 'Que se passe-t-il avec Pascal?', 'What is happening with Pascal?', [(35, "qu'est-ce qui se passe ?")], ''),
    ('beatrice', 'Pascal veut modifier la scène prévue.', 'Pascal wants to change the planned scene.', [(37, "c'était pas du tout prévu")], ''),
    ('andrea', "Cette modification n'était pas convenue.", 'This modification was not agreed upon.', [(37, "c'était pas du tout prévu")], ''),
    ('beatrice', 'Il impose des changements inacceptables.', 'He is imposing unacceptable changes.', [(39, "ils m'ont demandé")], ''),
    ('andrea', 'Tu as tout à fait raison de refuser.', 'You are completely right to refuse.', [(43, 'il en est même pas question')], ''),
    ('beatrice', "Peux-tu venir m'aider sur le plateau?", 'Can you come help me on the set?', [(41, 'ramène-toi, Andréa')], ''),
    ('andrea', 'Je quitte la maison dès maintenant.', 'I am leaving home right now.', [(40, 'je vais tout faire pour venir')], ''),
    ('beatrice', "Merci Andréa, j'ai besoin de toi.", 'Thank you Andrea, I need you.', [(41, 'ramène-toi, Andréa')], ''),
    ('andrea', 'Garde ton calme face au réalisateur.', 'Keep your cool when dealing with the director.', [(45, 'allez, calme')], ''),
    ('beatrice', "Je t'attends pour quinze heures.", 'I will expect you at three o', [(45, '15 heures')], ''),
    ('andrea', "J'arrive pour défendre tes droits.", 'I am coming to defend your rights.', [(44, "T'inquiète, je serai là")], ''),
]
WALK = [
    (0, None, "'Hello Andrea, it is Beatrice.' An informal telephone opening identifying the caller."),
    (1, None, "'Hello Beatrice, how are you doing?' A friendly greeting inquiring after a client."),
    (2, None, "'I have a big problem on the shoot.' A direct declaration announcing an urgent workplace issue."),
    (3, None, "'What is happening with Pascal?' A focused question asking about the director's conduct."),
    (4, None, "'Pascal wants to change the planned scene.' A specific complaint explaining the unapproved change."),
    (5, None, "'This modification was not agreed upon.' A clear statement pointing to a breach of prior agreement."),
    (6, None, "'He is imposing unacceptable changes.' An emphatic protest rejecting unilateral demands."),
    (7, None, "'You are completely right to refuse.' An empowering validation supporting the actress's firm stance."),
    (8, None, "'Can you come help me on the set?' A direct appeal requesting agent presence on location."),
    (9, None, "'I am leaving home right now.' A prompt commitment promising immediate travel to set."),
    (10, None, "'Thank you Andrea, I need you.' A heartfelt acknowledgment expressing genuine reliance on representation."),
    (11, None, "'Keep your cool when dealing with the director.' A sensible strategic counsel advising emotional control."),
    (12, None, "'I will expect you at three o'clock.' A precise logistical appointment establishing meeting time."),
    (13, None, "'I am coming to defend your rights.' A resolute professional declaration assuring advocacy."),
]
