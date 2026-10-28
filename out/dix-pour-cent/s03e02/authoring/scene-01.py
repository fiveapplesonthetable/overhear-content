# Authoring module for dix-pour-cent-s03e02-scene-01.
ID = 'dix-pour-cent-s03e02-scene-01'
SHOW = 'dix-pour-cent'
SEASON = 3
EPISODE = 2
SCENE = 1
TITLE = 'Le point tutelle  (The Check-In)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'gabriel': 'Gabriel'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S03E02'
SOURCE_FILE = 'sources/dix-pour-cent/s03/e02.fr.dual.srt'
INTRO = "In Gabriel's office at ASK, supervisory agent Andrea Martel conducts a formal weekly check-in on his recovery. Inspecting his office furniture, Andrea discovers a hidden backlog of urgent client mail, including a request from superstar Monica Bellucci. Let's listen to the scene in French first."
OPENER = "Let's observe as Andrea confronts Gabriel about the neglected client files."
TRANSITION = "Now let's listen to Andrea and Gabriel again at full speed."
OUTRO = "Andrea pushes Gabriel to face his responsibilities, ensuring that star client Monica Bellucci receives prompt agency attention. When you watch the episode, listen out for the expressions meaning 'come' and 'meeting'. You'll catch them now. See you next time!"
CLOSING = ('andrea', 'Au revoir!')
STORY = [
    ('andrea', 'Je viens pour notre point tutelle hebdomadaire.', 'I come for our weekly check-in.', [(1, "Ok, je viens pour un point tutelle. T'en es où aujourd'hui ?")], ''),
    ('gabriel', 'Tout va bien, je remonte la pente.', 'Everything is fine, I am getting back on track.', [(7, 'Voilà, je remonte la pente, je travaille.')], ''),
    ('andrea', 'Où est ta pile de dossiers urgents?', 'Where is your pile of urgent files?', [(11, 'Elle est où cette pile ?')], ''),
    ('gabriel', 'Elle est rangée dans ce grand placard.', 'It is stored in this large cupboard.', [(13, 'la pile elle est là.')], ''),
    ('andrea', 'Tu as caché tous ces dossiers importants?', 'Did you hide all these important files?', [(14, "J'ai pas eu le temps de trier.")], ''),
    ('gabriel', "Je n'ai pas eu le temps de trier.", 'I did not have time to sort.', [(14, "J'ai pas eu le temps de trier.")], ''),
    ('andrea', "Mais c'est un message de Monica Bellucci!", 'But this is a message from Monica Bellucci!', [(18, 'Rappeler Monica ?'), (19, 'Bellucci.')], ''),
    ('gabriel', "C'est pour son contrat publicitaire avec Cartier.", 'It is for her advertising contract with Cartier.', [(21, "C'est au sujet du renouvellement de son contrat publicitaire avec Cartier,")], ''),
    ('andrea', 'Tu as laissé Monica Bellucci sans réponse?', 'Did you leave Monica Bellucci without an answer?', [(23, "T'as laissé les droits publicitaires de Monica Bellucci dans le placard")], ''),
    ('gabriel', "J'allais justement m'en occuper ce matin.", 'I was just going to handle it this morning.', [(25, "c'est que je vais m'en occuper.")], ''),
    ('andrea', 'Tu es un véritable danger public, Gabriel!', 'You are a veritable public hazard, Gabriel!', [(24, "t'as peut-être été un danger public toi.")], ''),
    ('gabriel', "Ne t'énerve pas, je l'appelle tout de suite.", 'Do not get upset, I am calling her right away.', [(25, "je vais m'en occuper.")], ''),
    ('andrea', 'Sois très attentif et très convaincant.', 'Be very attentive and very convincing.', [(24, 'danger public')], ''),
    ('gabriel', 'Fais-moi confiance, je gère la situation.', 'Trust me, I am managing the situation.', [(7, 'je travaille.')], ''),
]
WALK = [
    (0, None, "'I come for our weekly check-in.' Andréa establishes supervisory duty."),
    (1, None, "'Everything is fine, I am getting back on track.' Gabriel expresses professional recovery."),
    (2, None, "'Where is your pile of urgent files?' Andréa asks for pending paperwork."),
    (3, None, "'It is stored in this large cupboard.' Gabriel reveals hidden client files."),
    (4, None, "'Did you hide all these important files?' Andréa challenges office disorganization."),
    (5, None, "'I did not have time to sort.' Gabriel pleads heavy workload."),
    (6, None, "'But this is a message from Monica Bellucci!' Andréa identifies a major international client."),
    (7, None, "'It is for her advertising contract with Cartier.' Gabriel explains commercial stakes."),
    (8, None, "'Did you leave Monica Bellucci without an answer?' Andréa reproaches client neglect."),
    (9, None, "'I was just going to handle it this morning.' Gabriel asserts immediate readiness."),
    (10, None, "'You are a veritable public hazard, Gabriel!' Andréa criticizes professional carelessness."),
    (11, None, "'Do not get upset, I am calling her right away.' Gabriel offers prompt remedy."),
    (12, None, "'Be very attentive and very convincing.' Paired imperative adjectives demanding professional excellence."),
    (13, None, "'Trust me, I am managing the situation.' Gabriel promises competent execution. Now let's listen to Andrea and Gabriel again at full speed."),
]
