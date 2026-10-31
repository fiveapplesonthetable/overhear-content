# Authoring module for dix-pour-cent-s01e01-scene-26.
ID = 'dix-pour-cent-s01e01-scene-26'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 26
TITLE = 'Ta nouvelle assistante  (Your New Assistant)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'gabriel': 'Gabriel', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = ('Cecile has agreed to work with Mathias, and Gabriel feels betrayed. Back at the agency, their argument '
 'brings Andrea into the dispute, before Mathias tells her who revealed the bad news to Cecile. Listen to '
 'the exchange in French first.')
OPENER = "Let's go back over it. Gabriel starts with a thank-you, but he doesn't mean it at all."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "That's it for this scene. When you watch it, listen for the past tense with 'have' each time someone is accused of something; you'll hear plenty of it. See you next time!"
CLOSING = ('andrea', 'Bonne journée, Mathias!')
STORY = [('gabriel',
  'Merci, Mathias! Tu as volé Cécile!',
  'Thanks, Mathias! You stole Cecile!',
  [(684, 'Merci, Mathias'), (681, 'Il a volé Cécile')],
  'Thanks from cue684; Gabriel’s accusation from merged scene25 is addressed directly to Mathias.'),
 ('gabriel',
  "Et ne dis pas que c'était pour le bien de l'agence.",
  "And don't say it was for the good of the agency.",
  [(685, "pour le bien de l'agence")],
  ''),
 ('mathias',
  'Bien sûr que oui, Gabriel.',
  'Of course it was, Gabriel.',
  [(686, 'Bien sûr que oui, Gabriel')],
  ''),
 ('mathias',
  'Deux autres agences voulaient Cécile.',
  'Two other agencies wanted Cécile.',
  [(689, 'Deux autres agences')],
  ''),
 ('gabriel',
  'Encore vingt-quatre heures, et elle revient!',
  'Twenty-four more hours, and she comes back!',
  [(690, '24 heures de plus')],
  ''),
 ('mathias',
  "On n'avait pas vingt-quatre heures.",
  "We didn't have twenty-four hours.",
  [(691, "on n'avait pas 24 heures")],
  ''),
 ('gabriel',
  "Ce n'est pas un dossier. C'est Cécile.",
  "She's not a file. She's Cécile.",
  [(691, "C'est pas un"), (692, "C'est Cécile")],
  ''),
 ('mathias', "Oui, c'est Cécile.", "Yes, it's Cécile.", [(692, "Oui, c'est Cécile")], ''),
 ('andrea', 'Félicitations, Mathias.', 'Congratulations, Mathias.', [(693, 'Félicitations')], ''),
 ('andrea',
  'Tu as volé la star de Gabriel avec beaucoup de classe.',
  "You stole Gabriel's star with a lot of class.",
  [(694, 'Tu as volé la star de Gabriel avec beaucoup de classe')],
  ''),
 ('andrea', 'Tu es fier de toi?', 'Are you proud of yourself?', [(695, 'Tu en es fier')], ''),
 ('mathias',
  "J'ai sauvé une cliente de l'agence, c'est tout.",
  "I saved one of the agency's clients, that's all.",
  [(698, "sauver une cliente de l'agence")],
  ''),
 ('mathias',
  'Maintenant, laisse-moi te dire un truc.',
  'Now, let me tell you something.',
  [(699, 'Maintenant, laisse-moi te dire un truc')],
  ''),
 ('mathias',
  "Ta nouvelle assistante a dit à Cécile qu'elle est trop vieille.",
  'Your new assistant told Cecile that she is too old.',
  [(700, "C'est ta nouvelle assistante"), (700, "qu'elle était trop vieille")],
  ''),
 ('andrea', 'Camille? Mais pourquoi?', 'Camille? But why?', [], ''),
 ('mathias',
  "Tu l'as trouvée où? Elle est dangereuse.",
  "Where did you find her? She's dangerous.",
  [(701, "Tu l'as trouvée où ? Elle est dangereuse")],
  ''),
 ('mathias',
  'Gabriel ne sait rien. Mais règle ce problème très vite!',
  'Gabriel knows nothing. But fix this problem very quickly!',
  [(705, "Je n'en ai pas parlé à Gabriel"), (706, 'mais règle ça, tu veux bien')],
  ''),
 ('mathias', 'Bonne journée.', 'Have a nice day.', [(707, 'Bonne journée')], '')]
WALK = [(0, 'Merci, Mathias!', "'Thanks, Mathias!' Pure sarcasm. Then he says what he really thinks."),
 (0,
  'Tu as volé Cécile!',
  "'You stole Cécile!' This is the everyday past: the action word 'to have' plus the past form of 'steal'. "
  "It's the language point of this scene, and you'll hear it again and again."),
 (1,
  None,
  "'And don't say it was for the good of the agency.' Gabriel gives a negative command where the negative "
  "wraps around the casual 'say'. Gabriel knows exactly what Mathias will answer."),
 (2, None, "'Of course it was, Gabriel.' Literally 'of course yes'. Mathias doesn't apologise for anything."),
 (3,
  None,
  "'Two other agencies wanted Cécile.' The verb is 'to want' in the past, describing how things stood: a "
  'different past tense, used for background.'),
 (4,
  None,
  "'Twenty-four more hours, and she comes back!' Gabriel speaks in the present to make it vivid: one more "
  'day, and she would have come home.'),
 (5, None, "'We didn't have twenty-four hours.' The word at the start means 'we' in everyday speech."),
 (6,
  None,
  "'She's not a file. She's Cécile.' The word for 'file' is what agents call a case or a deal. For Gabriel "
  "she's a person, not a deal."),
 (7, None, "'Yes, it's Cécile.' Mathias repeats it calmly, and Gabriel storms off. Now Andréa speaks up."),
 (8,
  None,
  "'Congratulations, Mathias.' The word looks long but it's simply 'congratulations'. She says it drily."),
 (9,
  None,
  "'You stole Gabriel's star with a lot of class.' The past tense again, with 'have'. To say 'Gabriel's "
  "star', French says 'the star of Gabriel'."),
 (10,
  None,
  "'Are you proud of yourself?' Andréa asks a question made just by raising her voice at the end. Mathias "
  "isn't ashamed one bit."),
 (11,
  None,
  "'I saved one of the agency's clients, that's all.' Past tense with 'have' once more: 'I have saved'. The "
  "word for 'client' has an extra letter at the end because Cécile is a woman."),
 (12,
  None,
  "'Now, let me tell you something.' The short command meaning 'let' has 'me' attached with a hyphen. The "
  "final informal noun means 'a thing' or 'something'."),
 (14,
  None,
  "'Camille? But why?' Andrea identifies the assistant with a surprised question. The last word asks for a "
  'reason.'),
 (13,
  None,
  "'Your new assistant told Cecile that she is too old.' The description 'new' has a feminine form to match "
  'the female assistant. The final description of age is feminine as well.'),
 (16,
  None,
  "'Gabriel knows nothing. But fix this problem very quickly!' The first sentence combines the small "
  "negative before 'knows' with 'nothing' after it. The second gives Andrea a direct instruction."),
 (15,
  None,
  "'Where did you find her? She's dangerous.' This question word for 'where' comes at the very end, which is "
  'common in spoken French.'),
 (16,
  'Gabriel ne sait rien.',
  "'Gabriel knows nothing.' The negative pair leaves out the ordinary word for 'not': 'nothing' supplies the "
  "second part. Mathias says he has kept the assistant's mistake from Gabriel."),
 (16,
  'Mais règle ce problème très vite!',
  "'But fix this problem very quickly!' This instruction uses the familiar singular form without a separate "
  "'you'. The final two words add urgency."),
 (17,
  None,
  "'Have a nice day.' Literally 'good day'. A sweet goodbye that leaves Andréa with a big problem. Here is "
  'the whole scene one more time.')]
