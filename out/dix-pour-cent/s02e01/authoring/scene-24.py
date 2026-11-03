# Authoring module for dix-pour-cent-s02e01-scene-24.
ID = 'dix-pour-cent-s02e01-scene-24'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 1
SCENE = 24
TITLE = "La décision de Catherine  (Catherine's Decision)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'catherine': 'Catherine', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E01'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e01.fr.dual.srt'
INTRO = "At Catherine's apartment, Mathias Barneville arrives hoping for a calm conversation and a chance to repair their marriage. But Catherine has already made up her mind. Let's listen to the scene in French first."
OPENER = "Let's examine how Mathias and Catherine express their painful separation."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = 'Catherine has drawn the line after years of betrayals and demands a divorce. Mathias must face the reality that his family life is slipping away. See you next time!'
CLOSING = ('catherine', 'À demain!')
STORY = [
    ('catherine', 'Quelle heure est-il?', 'What time is it?', [(727, 'Quelle heure est-il ?')], ''),
    ('mathias', 'Neuf heures pile, comme convenu.', "Nine o'clock sharp, as agreed.", [(728, '9 heures pile, comme convenu.')], ''),
    ('mathias', 'Je peux avoir un café?', 'Can I have a coffee?', [(730, 'Je peux avoir un café ?')], ''),
    ('catherine', "Il n'en reste plus.", 'There is none left.', [(731, "Il n'en reste plus.")], ''),
    ('mathias', 'Ça va?', 'Are you okay?', [(732, 'Ça va ?')], ''),
    ('catherine', "Prends ce que tu veux, je m'en fiche.", 'Take whatever you want, I do not care.', [(735, "Prends ce que tu veux, je m'en fiche.")], ''),
    ('mathias', 'Au téléphone, tu voulais parler.', 'On the phone, you wanted to talk.', [(736, 'au téléphone'), (738, 'tu voulais parler.')], ''),
    ('catherine', 'Informe les gens de ta nouvelle adresse.', 'Inform people of your new address.', [(740, 'informe les gens de ta nouvelle adresse.')], ''),
    ('mathias', "Mais je ne change pas d'adresse!", 'But I am not changing address!', [(741, "Mais je ne change pas d'adresse,")], ''),
    ('mathias', "J'ai commis une grave erreur il y a vingt-quatre ans.", 'I made a serious mistake twenty-four years ago.', [(744, "J'ai commis une grave erreur il y a 24 ans.")], ''),
    ('catherine', "Je ne veux pas t'empêcher de t'amuser.", 'I do not want to stop you from having fun.', [(748, "Je ne veux pas t'empêcher de t'amuser.")], ''),
    ('mathias', 'Je suis son agent, pas son amant.', 'I am her agent, not her lover.', [(752, 'Je suis son agent,'), (753, 'pas son amant,')], ''),
    ('catherine', "Qu'est-ce que j'en sais?", 'What do I know about it?', [(754, "Qu'est-ce que j'en sais ?")], ''),
    ('mathias', "Elle a rompu avec Ramzy, c'est tout.", 'She broke up with Ramzy, that is all.', [(756, 'Elle a rompu avec Ramzy')], ''),
    ('catherine', 'Tu vois, je ne te crois plus.', 'You see, I do not believe you anymore.', [(757, "Tu vois, c'est ça le problème. Je ne te crois plus.")], ''),
    ('mathias', "C'est la vérité, Catherine.", 'It is the truth, Catherine.', [(758, "C'est la vérité, Catherine.")], ''),
    ('catherine', "Je n'en peux plus. On divorce.", 'We are getting a divorce.', [(761, "Je n'en peux plus."), (762, 'On divorce.')], ''),
]
WALK = [
    (0, None, ["'What time is it?' Catherine checks the ", ('catherine', 'heure'), ' meaning "time", as Mathias arrives to pack his things.']),
    (1, None, ["'Nine o'clock sharp, as agreed.' Mathias points out that he arrived at nine o'clock ", ('mathias', 'pile,'), ' meaning "sharp", just as agreed.']),
    (2, None, ["'Can I have a coffee?' Mathias tries to break the ice by asking politely for a ", ('mathias', 'café?'), ' meaning "coffee".']),
    (3, None, ["'There is none left.' Catherine replies coldly that there is none ", ('catherine', 'reste'), ' meaning "left".']),
    (4, None, ["'Are you okay?' Mathias asks softly how she is holding up, asking if it ", ('mathias', 'va?'), ' meaning "goes" or "is okay".']),
    (5, None, ["'Take whatever you want, I do not care.' Catherine tells him to take whatever he wants, saying she does not ", ('catherine', 'fiche.'), ' meaning "care".']),
    (6, None, ["'On the phone, you wanted to talk.' Mathias reminds her that on the ", ('mathias', 'téléphone,'), ' meaning "phone", she wanted to talk.']),
    (7, None, ["'Inform people of your new address.' Catherine hands him his mail and tells him to update his ", ('catherine', 'adresse.'), ' meaning "address".']),
    (8, None, ["'But I am not changing address!' Mathias protests that he is not ", ('mathias', 'change'), ' meaning "changing", his residence for good.']),
    (9, None, ["'I made a serious mistake twenty-four years ago.' He tries to frame his secret affair as a single ", ('mathias', 'erreur'), ' meaning "mistake", twenty-four years ago.']),
    (10, None, ["'I do not want to stop you from having fun.' Seeing the tabloid photo of Mathias with Virginie, Catherine bitterly tells him to go ", ('catherine', 'amuser.'), ' meaning "have fun".']),
    (11, None, ["'I am her agent, not her lover.' Mathias clarifies his professional relationship, stating he is not her ", ('mathias', 'amant.'), ' meaning "lover".']),
    (12, None, ["'What do I know about it?' Catherine asks what she could possibly ", ('catherine', 'sais?'), ' meaning "know", about what else he has been hiding.']),
    (13, None, ["'She broke up with Ramzy, that is all.' Mathias explains that she merely ", ('mathias', 'rompu'), ' meaning "broke up", with her boyfriend.']),
    (14, None, ["'You see, I do not believe you anymore.' Catherine states clearly that she does not ", ('catherine', 'crois'), ' meaning "believe", him anymore.']),
    (15, None, ["'It is the truth, Catherine.' He pleads that this is the ", ('mathias', 'vérité,'), ' meaning "truth".']),
    (16, "Je n'en peux plus.", ["'I cannot take it anymore.' Catherine admits she has reached her limit, saying ", ('catherine', "Je n'en peux plus."), ' meaning "I cannot take it anymore".']),
    (16, 'On divorce.', ["'We are getting a divorce.' Catherine quietly delivers her final decision to get a ", ('catherine', 'divorce.'), ' meaning "divorce".']),
]
