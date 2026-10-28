# Authoring module for dix-pour-cent-s02e03-scene-18.
ID = 'dix-pour-cent-s02e03-scene-18'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 3
SCENE = 18
TITLE = "Une rencontre embarrassante  (An Awkward Encounter)"
LEVEL = "A1 — débutant"
PAIR = 'fr-en'
VOICES = {"narrator": "sky", "catherine": "emilie", "mathias": "marcel", "lea": "lucie"}
LABELS = {"catherine": "Catherine", "mathias": "Mathias", "lea": "Andréa"}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E03'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e03.fr.dual.srt'
INTRO = 'At Le Grand Colbert restaurant, Mathias is having lunch with Camille and her mother Annick when Catherine arrives unexpectedly. A mortified Noémie stands beside her as Mathias tries to control the deeply uncomfortable situation. Listen to the scene in French first.'
OPENER = "Let's examine how Catherine unexpectedly joins Mathias for a family lunch."
TRANSITION = "Now let's listen to the icy encounter at Le Grand Colbert once more."
OUTRO = 'With ice in the air, Catherine takes her seat opposite Annick, leaving Mathias trapped between his past and present. Until next time.'
CLOSING = ("catherine", "Bonne soirée!")
STORY = [
    ('catherine', 'Annick, je présume?', 'Annick, I presume?', [(452, 'Annick, je présume')], ''),
    ('catherine', 'Je suis Catherine Barneville.', 'I am Catherine Barneville.', [(453, 'Catherine Barneville')], ''),
    ('mathias', "Catherine? Qu'est-ce que tu fais là?", 'Catherine? What are you doing here?', [(450, 'je ne savais pas que Mathias serait là')], ''),
    ('catherine', 'Je viens déjeuner avec vous tous.', 'I came to have lunch with you all.', [(446, 'Je viens avec toi')], ''),
    ('mathias', "Noémie, retournez au bureau, s'il vous plaît.", 'Noémie, please return to the office.', [(457, "Retournez au bureau, s'il vous plaît")], ''),
    ('lea', 'Très bien, je vous laisse.', 'Very well, I will leave you.', [(457, "D'accord")], ''),
    ('mathias', "Ce déjeuner n'était pas prévu ainsi.", 'This lunch was not planned this way.', [(451, "Je n'avais pas prévu de le voir")], ''),
    ('catherine', "Ce n'est rien, je m'assieds avec vous.", 'It', [(459, "Ne t'inquiète pas, c'est pas ta faute")], ''),
    ('mathias', 'Tu veux commander à manger?', 'Do you want to order something to eat?', [(460, 'Vous êtes trois ? Quatre ? Pour déjeuner ?')], ''),
    ('catherine', "Non, juste un café, s'il vous plaît.", 'No, just a coffee, please.', [(461, 'Non... non'), (462, "Un café, s'il vous plaît")], ''),
    ('mathias', 'Pourquoi tu es venue ici exactement?', 'Why did you come here exactly?', [(455, "C'est à propos de Christophe Lambert")], ''),
    ('catherine', "Je voulais faire la connaissance d'Annick.", 'I wanted to meet Annick.', [(453, 'Enchantée. Annick Valentini')], ''),
    ('mathias', 'Tu cherches à me provoquer?', 'Are you trying to provoke me?', [(456, 'Pardon ? Euh... non')], ''),
    ('catherine', 'Pas du tout, nous sommes civilisés.', 'Not at all, we are civilized.', [(458, "C'est moi qui ai proposé ce déjeuner")], ''),
    ('mathias', 'Alors soyons calmes devant tout le monde.', 'Then let', [(459, "Ne t'inquiète pas")], ''),
    ('catherine', 'Parfait. Buvons notre café.', 'Perfect. Let', [(463, 'Un café, voilà')], ''),
]
WALK = [
    (0, None, "'Annick, I presume?' Catherine approaches the table with sharp confidence. Listen for the expression meaning 'assume', which leads naturally into 'assume'."),
    (1, None, "'I am Catherine Barneville.' She introduces herself formally to Mathias's former mistress. Catherine opens with the word for 'am' and lands on 'am' at the close."),
    (2, None, "'Catherine? What are you doing here?' Mathias chokes on his surprise. The verb meaning 'are doing' anchors the whole remark."),
    (3, None, "'I came to have lunch with you all.' Catherine smiles icily. The key word here means 'arrived', paired with 'to have lunch' to make the point clear."),
    (4, None, "'Noémie, please return to the office.' Mathias quickly orders his assistant away. Listen for the expression meaning 'go back', which leads naturally into 'pleases'."),
    (5, None, "'Very well, I will leave you.' Noémie gladly seizes the chance to flee. Noémie opens with the word for 'quite' and lands on 'depart from' at the close."),
    (6, None, "'This lunch was not planned this way.' Mathias tries to defend the arrangement. Mathias pairs the verb meaning 'was' with the noun for 'midday meal'."),
    (7, None, "'It's nothing, I'll sit with you.' Catherine pulls out a chair deliberately. The verb meaning 'is' anchors the whole remark."),
    (8, None, "'Do you want to order something to eat?' Mathias asks nervously. Listen for the expression meaning 'care to', which leads naturally into 'consume food'."),
    (9, None, "'No, just a coffee, please.' Catherine declines food politely. Catherine opens with the word for 'no' and lands on 'pleases' at the close."),
    (10, None, "'Why did you come here exactly?' Mathias demands quietly. Mathias opens with the word for 'for what reason' and lands on 'precisely' at the close."),
    (11, None, "'I wanted to meet Annick.' Catherine explains her bold curiosity. The key word here means 'wished', paired with 'acquaintance' to make the point clear."),
    (12, None, "'Are you trying to provoke me?' Mathias suspects her hostile motives. Listen for the expression meaning 'are trying', which leads naturally into 'bait'."),
    (13, None, "'Not at all, we are civilized.' Catherine feigns polite innocence. Listen for the expression meaning 'not', which leads naturally into 'well-mannered'."),
    (14, None, "'Then let's be calm in front of everyone.' Mathias pleads for discretion. The adjective meaning 'composed' agrees in gender and number with masculine noun 'crowd'."),
    (15, None, "'Perfect. Let's drink our coffee.' Catherine takes control of the table. Catherine opens with the word for 'splendid' and lands on 'espresso' at the close."),
]
