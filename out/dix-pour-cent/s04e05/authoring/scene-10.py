# Authoring module for dix-pour-cent-s04e05-scene-10.
ID = 'dix-pour-cent-s04e05-scene-10'
SHOW = 'dix-pour-cent'
SEASON = 4
EPISODE = 5
SCENE = 10
TITLE = 'Message pour Colette  (A Message for Colette)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'elise': 'Élise'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S04E05'
SOURCE_FILE = 'sources/dix-pour-cent/s04/e05.fr.dual.srt'
INTRO = "Alone in her quiet apartment, Andrea Martel dials Colette Brancillon's phone number. Reaching voicemail, she leaves a gentle message expressing her worry and yearning for news. Moments later, rival agent Elise Formain sends an unexpected message with a timely solution for baby Flora. Let's listen to their words in French first."
OPENER = "Let's examine the messages line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."
OUTRO = "Although Andrea misses Colette deeply, Elise's surprising generosity solves her immediate childcare dilemma. When you watch the episode, listen out for the expressions meaning 'telephone' and 'wanted'. You'll catch them now. See you next time!"
CLOSING = ('andrea', 'Bonne journée!')
STORY = [
    ('andrea', "Colette, c'est moi au téléphone.", 'Colette, it is me on the phone.', [(434, "Colette, c'est moi.")], ''),
    ('andrea', 'Je voulais savoir comment tu vas.', 'I wanted to know how you are doing.', [(435, 'Je voulais juste savoir comment tu allais')], ''),
    ('andrea', 'Tu ne réponds plus à mes messages.', 'You no longer answer my messages.', [(435, 'parce que je...')], ''),
    ('andrea', "Je m'inquiète beaucoup pour toi.", 'I worry a lot about you.', [(436, "Je m'inquiète.")], ''),
    ('andrea', 'Flora et moi, on pense à toi.', 'Flora and I, we think of you.', [(436, "Je m'inquiète.")], ''),
    ('andrea', "Rappelle-moi vite, s'il te plaît.", 'Call me back soon, please.', [(437, 'Rappelle-moi, donne-moi de tes nouvelles.')], ''),
    ('andrea', 'Prends bien soin de toi.', 'Take good care of yourself.', [(437, 'Prends soin de toi.')], ''),
    ('andrea', 'Le silence est très lourd ce soir.', 'The silence is very heavy tonight.', [(437, 'Prends soin de toi.')], ''),
    ('elise', "Andréa, j'ai une bonne nouvelle!", 'Andrea, I have good news!', [(438, 'Ma nièce peut garder Flora jour et nuit.')], ''),
    ('elise', 'Ma nièce cherche un nouveau travail.', 'My niece is looking for new work.', [(438, 'Ma nièce peut garder Flora')], ''),
    ('elise', 'Elle peut garder Flora jour et nuit.', 'She can babysit Flora day and night.', [(438, 'jour et nuit. De rien !')], ''),
    ('andrea', "C'est une offre tout à fait inattendue.", 'It is a completely unexpected offer.', [(438, 'De rien !')], ''),
    ('andrea', 'Cela sauve ma semaine de travail!', 'That saves my work week!', [(438, 'De rien !')], ''),
]
WALK = [
    (0, None, "'Colette, it is me on the phone.' Andrea begins her voicemail message."),
    (1, None, "'I wanted to know how you are doing.' Andrea inquires softly after Colette's well-being."),
    (2, None, "'You no longer answer my messages.' Andrea notes the absence of communication."),
    (3, None, "'I worry a lot about you.' Andrea confesses her anxiety."),
    (4, None, "'Flora and I, we think of you.' Andrea highlights their shared family bond."),
    (5, None, "'Call me back soon, please.' Andrea requests an answer without demanding."),
    (6, None, "'Take good care of yourself.' Andrea closes with a warm expression of care."),
    (7, None, "'The silence is very heavy tonight.' Andrea reflects on the loneliness of her home."),
    (8, None, "'Andrea, I have good news!' Elise sends an enthusiastic message."),
    (9, None, "'My niece is looking for new work.' Elise presents her niece's job search."),
    (10, None, "'She can babysit Flora day and night.' Elise proposes round-the-clock childcare."),
    (11, None, "'It is a completely unexpected offer.' Andrea marvels at the convenient timing."),
    (12, None, "'That saves my work week!' Andrea feels a huge burden lifted from her shoulders. Now let's listen to the complete discussion once more to reinforce the vocabulary."),
]
