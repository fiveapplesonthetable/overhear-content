# Authoring module for dix-pour-cent-s01e03-scene-01.
ID = 'dix-pour-cent-s01e03-scene-01'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = 'La lettre oubliée  (The Forgotten Letter)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'gabriel': 'Gabriel', 'andrea': 'Andréa', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E03'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e03.fr.dual.srt'
INTRO = ('This is Call My Agent, set in a Paris talent agency. Gabriel has forgotten to post an important letter. '
 'Sending this letter could help the firm through a tax audit. His colleagues Andrea and Mathias ask what '
 'happened, while a client waits outside. Listen to the French story first; you do not need to catch every '
 'word.')
OPENER = ("Let's follow the forgotten letter. First Gabriel finishes a cheerful call, before Andrea brings up the tax "
 'audit.')
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ("Gabriel's missing letter has cost the agency an important ally at the tax office. You have heard how to "
 'describe completed actions, apologise and ask what happened. See you next time!')
CLOSING = ('andrea', 'À bientôt!')
STORY = [('gabriel',
  'Cécile! Oui, super. Rappelle-moi. Salut.',
  'Cécile! Yes, great. Call me back. Bye.',
  [(1, 'Cécile ! Oui, super'), (3, 'rappelle-moi. Salut')],
  ''),
 ('andrea',
  'Le contrôle fiscal. Cette lettre pour monsieur Jarron?',
  'The tax audit. That letter for Mr Jarron?',
  [(5, 'Le contrôle fiscal'), (6, 'Cette lettre pour M. Jarron')],
  ''),
 ('gabriel', "Oui, je l'ai envoyée.", 'Yes, I sent it.', [(7, "Oui, je l'ai envoyée")], ''),
 ('gabriel',
  "J'ai pris la lettre. Je l'ai mise dans une enveloppe.",
  'I took the letter. I put it in an envelope.',
  [(8, "J'ai pris la lettre"), (8, "je l'ai mise dans une enveloppe")],
  ''),
 ('gabriel', 'Oh non!', 'Oh no!', [], ''),
 ('gabriel', 'Je suis désolé.', "I'm sorry.", [], 'New short apology connecting the source exchange.'),
 ('gabriel',
  'À quoi ça sert de payer une assistante?',
  "What's the point of paying an assistant?",
  [(10, 'À quoi ça sert de payer une assistante ?')],
  ''),
 ('mathias',
  'Non, Gabriel, on ne peut pas toujours tout arranger!',
  "No, Gabriel, you can't always fix everything!",
  [(15, 'Non, Gabriel, on ne peut pas toujours tout arranger')],
  ''),
 ('mathias', 'On a eu un appel ce matin.', 'We had a call this morning.', [(16, 'un appel ce matin')], ''),
 ('mathias',
  'Le dossier est dans un autre service.',
  'The file is in another department.',
  [(17, 'dans un autre service')],
  ''),
 ('mathias',
  'Jarron était notre seul allié.',
  'Jarron was our only ally.',
  [(18, 'Jarron était notre seul allié')],
  ''),
 ('gabriel',
  'Il faut peut-être mettre nos comptes en ordre.',
  'Maybe we need to put our books in order.',
  [(19, 'peut-être'), (19, 'mettre nos comptes en ordre')],
  ''),
 ('mathias',
  "La vie, c'est une grande blague pour toi?",
  'Is life a big joke to you?',
  [(21, 'une grande blague pour toi')],
  ''),
 ('mathias',
  'Tu es aussi stupide que ça?',
  'Are you really that stupid?',
  [(22, 'Tu es aussi stupide que ça ?')],
  ''),
 ('gabriel', 'Fais-lui un café.', 'Make her a coffee.', [(24, 'Fais-lui un café')], '')]
WALK = [(0,
  None,
  'Gabriel greets Cecile and gives an enthusiastic yes, saying that things sound great. He asks her to call '
  'back and finishes with a casual goodbye. The request to call back is a familiar command. A hyphen joins '
  'the command to a short object word identifying the person asking for the return call.'),
 (1,
  'Le contrôle fiscal.',
  "'The tax audit.' Literally 'the fiscal control'. The describing word follows the thing being checked: the "
  "agency's tax affairs."),
 (1,
  'Cette lettre pour monsieur Jarron?',
  "'That letter for Mr Jarron?' The first word means 'this' or 'that' in a feminine form, because the word "
  'for letter is feminine.'),
 (2,
  None,
  "'Yes, I sent it.' The object word refers back to the letter and comes before the helping word. It loses "
  'its vowel before the next word. Because the letter is feminine, the completed action has an additional '
  'feminine ending in writing.'),
 (3,
  "J'ai pris la lettre.",
  "'I took the letter.' The completed action uses 'have' and the past form of 'take'. Gabriel tries to "
  'remember the steps he followed.'),
 (3,
  "Je l'ai mise dans une enveloppe.",
  "'I put it in an envelope.' The object word again refers to the letter. Its feminine gender gives the "
  'completed action an extra ending in writing.'),
 (4,
  None,
  "'Oh no!' This short reaction replaces a swearword in the episode. Gabriel suddenly realises that putting "
  'the letter in an envelope was not the same as posting it.'),
 (5,
  None,
  "'I'm sorry.' This written apology has a masculine ending because Gabriel is speaking. An apology by a "
  'woman would add a silent e.'),
 (6,
  None,
  "'What's the point of paying an assistant?' Literally 'to what does it serve to pay an assistant'. Gabriel "
  'tries to shift the blame for his own mistake.'),
 (7,
  None,
  "'No, Gabriel, you can't always fix everything!' The short word before the action can refer to a group "
  'including the speaker, or to people in general. Here Mathias is talking about people in general as he '
  "rejects Gabriel's easy reassurance."),
 (8,
  None,
  "'We had a call this morning.' The completed past of 'have' pairs a present helper with the short past "
  'form. The last two words identify this morning.'),
 (9,
  None,
  "'The file is in another department.' The word for 'another' follows an indefinite article. Their tax case "
  'has moved away from the person who could help them.'),
 (10,
  None,
  "'Jarron was our only ally.' The past form of 'be' describes how things stood. The word for 'only' comes "
  'before the person described: their ally.'),
 (11,
  None,
  "'Maybe we need to put our books in order.' The first two words express necessity. Gabriel suggests doing "
  'what the audit demands, which is not what his colleagues want to hear.'),
 (12,
  None,
  "'Is life a big joke to you?' The word for 'you' after 'for' is the full form that can stand alone. "
  'Mathias turns the problem into a personal accusation.'),
 (13,
  None,
  "'Are you really that stupid?' Literally 'are you as stupid as that?'. The two comparison words surround "
  "the description. Just then Herve announces Laura's arrival."),
 (14,
  None,
  "'Make her a coffee.' This instruction attaches 'to her' after 'make' with a hyphen. Gabriel is keen to "
  'leave the meeting and see his waiting client.')]
