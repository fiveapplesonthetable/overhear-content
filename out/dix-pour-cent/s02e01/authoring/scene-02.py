# Authoring module for dix-pour-cent-s02e01-scene-02.
ID = 'dix-pour-cent-s02e01-scene-02'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 1
SCENE = 2
TITLE = "L'appel nocturne de Virginie  (Virginie's Night Call)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'mathias': 'Mathias', 'virginie': 'Virginie'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E01'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e01.fr.dual.srt'
INTRO = "At home late at night, agent Mathias Barneville tries to relax with a guided meditation session. Suddenly his phone rings. It is his star client Virginie Efira in a state of absolute panic after a night out. Let's listen to their conversation in French first."
OPENER = "Let's examine how Mathias handles a sudden emergency call from his actress."
TRANSITION = "Now let's listen to the late-night phone call again at full speed."
OUTRO = 'Virginie is terrified of losing both her partner and her career over the scandal. Mathias urges honesty, but in the morning the press will already have the story. See you next time!'
CLOSING = ('mathias', 'À bientôt!')
STORY = [
    ('mathias', "Allô? Virginie, que s'est-il passé?", 'Hello? Virginie, what happened?', [(31, 'Allô ?'), (33, "Que s'est-il passé ?")], ''),
    ('virginie', "Mathias, c'est terrible!", 'Mathias, it is terrible!', [(32, "Mathias, c'est terrible.")], ''),
    ('virginie', "J'étais dans la rue avec un ami.", 'I was in the street with a friend.', [(34, "J'étais dans la rue, avec un ami.")], ''),
    ('mathias', 'Un ami? Tu étais avec Ramzy?', 'A friend? Were you with Ramzy?', [(37, 'Un ami ? Tu étais avec Ramzy ?')], ''),
    ('virginie', 'Non, Ramzy est rentré chez lui.', 'No, Ramzy went home.', [(38, 'Non, il est rentré chez lui.')], ''),
    ('virginie', "J'ai vu un flash dans la nuit.", 'I saw a flash in the night.', [(36, 'il y a eu un flash')], ''),
    ('mathias', 'Vous avez été pris en photo par un paparazzi?', 'Were you photographed by a paparazzo?', [(45, 'vous avez été pris en photo par un paparazzi ?')], ''),
    ('virginie', 'Il faut que tu fasses quelque chose!', 'You have to do something!', [(47, 'il faut que tu fasses quelque chose')], ''),
    ('virginie', 'Appelle les magazines, ils ne doivent pas publier!', 'Call the magazines, they must not publish!', [(48, 'Appelle les magazines people'), (49, 'ils ne doivent pas le publier !')], ''),
    ('mathias', 'Mes menaces ne vont pas les arrêter.', 'My threats are not going to stop them.', [(50, 'Mes menaces ne les'), (51, 'arrêter.')], ''),
    ('virginie', "Alors qu'est-ce que je fais?", 'So what do I do?', [(52, "Alors qu'est-ce que je fais ?")], ''),
    ('mathias', 'Parle à Ramzy immédiatement.', 'Talk to Ramzy immediately.', [(53, 'Parle à Ramzy.')], ''),
    ('virginie', 'Non, je ne peux pas, il ne comprendra pas.', 'No, I cannot, he will not understand.', [(54, 'Non, je ne peux pas, il ne comprendra pas.')], ''),
    ('mathias', "Virginie, crois-moi, c'est la meilleure chose à faire.", 'Virginie, believe me, it is the best thing to do.', [(55, 'Crois-moi'), (56, "c'est la meilleure chose à faire.")], ''),
]
WALK = [
    (0, ('mathias', 'Allô?'), "'Hello? Virginie, what happened?' Mathias answers the phone with the standard greeting for 'hello' on the phone, before asking what happened."),
    (1, ('virginie', 'terrible!'), "'Mathias, it is terrible!' Virginie calls Mathias in a panic, exclaiming the word for 'terrible' because a disaster has just happened."),
    (2, ('virginie', 'dans la rue'), "'I was in the street with a friend.' Virginie explains that she was out, meaning 'in the street' late at night, with a male friend."),
    (3, ('mathias', 'Un ami?'), "'A friend? Were you with Ramzy?' Mathias checks warily whether she was actually out with Ramzy, repeating the phrase for 'a friend'."),
    (4, ('virginie', 'chez lui.'), "'No, Ramzy went home.' Virginie admits that Ramzy had already gone home alone, using the phrase for 'to his place'."),
    (5, ('virginie', 'nuit.'), "'I saw a flash in the night.' Virginie says she saw a camera flash go off in the dark, referring to the 'night'."),
    (6, ('mathias', 'pris en photo'), "'Were you photographed by a paparazzo?' Mathias expresses an unwanted media intrusion, asking if she was 'taken in photo' by a paparazzo."),
    (7, ('virginie', 'fasses'), "'You have to do something!' Virginie begs Mathias to stop the tabloid photos from coming out, which requires the subjunctive verb form for 'do'."),
    (8, ('virginie', 'Appelle'), "'Call the magazines, they must not publish!' Virginie demands that he call the magazines using the imperative form for 'call' and stop publication."),
    (9, ('mathias', 'arrêter.'), "'My threats are not going to stop them.' Mathias warns her that his threats will not stop the paparazzi from publishing, saying his threats will not 'stop' them."),
    (10, ('virginie', 'fais?'), "'So what do I do?' Virginie asks what she should do next using the verb for 'do'."),
    (11, ('mathias', 'immédiatement.'), "'Talk to Ramzy immediately.' Mathias advises Virginie to tell Ramzy the truth 'immediately' before the magazine hits the stands."),
    (12, ('virginie', 'comprendra'), "'No, I cannot, he will not understand.' Virginie insists she cannot tell him because he will not 'understand'."),
    (13, ('mathias', 'crois-moi'), "'Virginie, believe me, it is the best thing to do.' Mathias urges Virginie to trust him, using the phrase for 'believe me'.")
]
