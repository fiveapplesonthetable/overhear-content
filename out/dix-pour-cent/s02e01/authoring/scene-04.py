# Authoring module for dix-pour-cent-s02e01-scene-04.
ID = 'dix-pour-cent-s02e01-scene-04'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 1
SCENE = 4
TITLE = 'Mathias et Camille au café  (Mathias and Camille at the Café)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E01'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e01.fr.dual.srt'
INTRO = "Mathias meets his secret daughter Camille at a quiet cafe across town. After his wife Catherine kicked him out for his years of lies, Mathias wants to come clean to everyone at ASK. However, Camille is horrified by the prospect of being exposed. Let's listen to their conversation in French first."
OPENER = "Let's examine how Mathias and Camille discuss their hidden family secret."
TRANSITION = "Now let's listen to their conversation at the cafe again without interruptions."
OUTRO = 'Camille desperately wants to protect her independent life at the agency. Mathias agrees to keep quiet for now, but keeping such a major secret is never easy. See you next time!'
CLOSING = ('camille', 'À demain!')
STORY = [
    ('mathias', "Tu es sûre d'avoir assez mangé?", 'Are you sure you have eaten enough?', [(92, 'assez mangé ?')], ''),
    ('camille', 'Alors, tu as quelque chose à me dire.', 'So, you have something to tell me.', [(94, 'Alors,'), (95, 'Tu as quelque chose à me dire.')], ''),
    ('mathias', "J'ai fait du mal en cachant la vérité pendant des années.", 'I caused harm by hiding the truth for years.', [(97, "j'ai fait beaucoup de mal"), (98, 'pendant des années.')], ''),
    ('mathias', "Catherine m'a mis à la porte.", 'Catherine threw me out.', [(99, "Catherine m'a mis à la porte,")], ''),
    ('mathias', 'Elle pense que je suis un menteur.', 'She thinks I am a liar.', [(100, 'elle pense que je suis'), (100, 'menteur.')], ''),
    ('mathias', 'Je veux réparer ça et dire la vérité.', 'I want to fix that and tell the truth.', [(102, 'Je veux réparer ça.'), (104, 'dire la vérité,')], ''),
    ('mathias', 'Je veux dire à tout le monde que tu es ma fille.', 'I want to tell everyone that you are my daughter.', [(104, 'dire que tu es ma fille.'), (107, 'je veux dire à tout le monde.')], ''),
    ('camille', "À l'agence? Mais maintenant j'ai peur.", 'At the agency? But now I am afraid.', [(108, "À l'agence..."), (113, "maintenant j'ai peur.")], ''),
    ('mathias', 'Peur de quoi, Camille?', 'Afraid of what, Camille?', [(115, 'Peur de quoi ?')], ''),
    ('camille', "J'ai peur de perdre la confiance de mes collègues.", 'I am afraid of losing the trust of my colleagues.', [(116, 'De perdre la confiance des gens,')], ''),
    ('camille', "Tu crois qu'Andréa veut de ta fille comme assistante?", 'Do you think Andréa wants your daughter as an assistant?', [(118, "Tu crois qu'Andréa veut de ta fille comme assistante ?")], ''),
    ('camille', 'Hervé et Noémie sont mes amis maintenant.', 'Hervé and Noémie are my friends now.', [(119, 'Ce sont mes amis maintenant.')], ''),
    ('camille', 'Ils vont penser que je suis une menteuse.', 'They will think that I am a liar.', [(120, 'comme une sorte de')], ''),
    ('camille', 'Je suis très heureuse ici, je ne veux pas gâcher ça.', 'I am very happy here, I do not want to ruin that.', [(121, 'je ne veux pas gâcher ça.')], ''),
]
WALK = [
    (0, ('mathias', 'assez'), "Over breakfast, Mathias checks with fatherly concern that Camille has eaten enough. He uses the word for 'enough'."),
    (1, ('camille', 'Alors,'), "Camille senses his hesitation and prompts him to say what is on his mind, starting with the word for 'so'."),
    (2, ('mathias', 'vérité'), "Mathias admits he caused real pain by hiding the truth for so many years. He uses the word for 'truth'."),
    (3, ('mathias', 'porte.'), "Mathias uses an everyday expression that literally means 'put to the door'. He uses the word for 'door'."),
    (4, ('mathias', 'menteur.'), "Mathias sighs that his wife Catherine now sees him as a liar, using the word for 'liar'."),
    (5, ('mathias', 'réparer'), "Mathias says he wants to fix things and tell the truth. He uses the action word for 'repair'."),
    (6, ('mathias', 'fille.'), "Mathias states his wish to acknowledge his child publicly, referring to her as his daughter."),
    (7, ('camille', 'peur.'), "Camille reacts with shock followed by an expression of fear, saying she is afraid. She uses the word for 'fear'."),
    (8, ('mathias', 'de quoi,'), "Mathias gently asks Camille what she is afraid of. He asks 'of what?'."),
    (9, ('camille', 'confiance'), "Camille admits she is afraid of losing her colleagues' trust. She uses the word for 'trust'."),
    (10, ('camille', 'assistante?'), "Camille highlights professional vulnerability, mentioning her role as an assistant."),
    (11, ('camille', 'maintenant.'), "Camille describes her newly built personal and professional bonds, noting they are her friends now. She uses the word for 'now'."),
    (12, ('camille', 'menteuse.'), "Camille expresses her fear of social rejection, worrying they will think she is a liar. She uses the feminine word for 'liar'."),
    (13, ('camille', 'heureuse'), "Camille makes a heartfelt appeal to preserve her current happiness. She says she is very happy, using the feminine word for 'happy'."),
]
