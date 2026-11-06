ID = 'pousada-do-cajueiro-s01e01-scene-01'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 1, 1
TITLE = 'Levante a maçaneta  (Lift the Handle)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'camila': 'Camila', 'jorge': 'Jorge'}

INTRO = ('Camila arrives early for her very first morning at the Cashew Tree Guesthouse in Recife. Behind the front '
 'desk, veteran handyman Jorge is already pouring hot tea. Listen to the scene in Brazilian Portuguese first '
 'without worrying about catching every word.')
OPENER = "Now let's walk through the conversation one line at a time."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = ("Camila is inside, the eight brass keys are on the board, and her first morning in Recife has begun. Don't "
 'worry if a few words went past quickly; they come back all week. See you next time.')
CLOSING = ('camila', 'Até logo!')

STORY = [('camila', 'Bom dia! Com licença, a porta está trancada?', 'Good morning! Excuse me, is the door locked?'),
 ('jorge',
  'Bom dia. Não, levante a maçaneta primeiro e depois empurre.',
  'Good morning. No, lift the handle first and then push.'),
 ('camila',
  'Ah, abriu! Obrigada. Eu sou a Camila, a nova recepcionista.',
  'Oh, it opened! Thank you. I am Camila, the new receptionist.'),
 ('jorge', 'Eu sou o Jorge. Você chegou dez minutos cedo.', 'I am Jorge. You arrived ten minutes early.'),
 ('camila',
  'No primeiro dia eu sempre ando rápido. Onde fica o computador?',
  'On the first day I always walk fast. Where is the computer?'),
 ('jorge',
  'Na gaveta. Aqui a gente usa este caderno grande e um lápis.',
  'In the drawer. Here we use this big notebook and a pencil.'),
 ('camila', 'Um caderno de papel? Sério?', 'A paper notebook? Really?'),
 ('jorge', 'O papel nunca perde a lista quando chove.', 'Paper never loses the list when it rains.'),
 ('camila', 'Justo! E estas são as chaves?', 'Fair enough! And are these the keys?'),
 ('jorge',
  'Sim, oito quartos, oito chaves. O quarto quatro chega hoje.',
  'Yes, eight rooms, eight keys. Room four arrives today.'),
 ('camila',
  'Ótimo. Pode me contar tudo o que eu preciso saber.',
  'Great. You can tell me everything I need to know.'),
 ('jorge',
  'Regra número um: tome chá quente primeiro e depois atenda a campainha.',
  'Rule number one: drink hot tea first and then answer the bell.')]

WALK = [(0,
  None,
  ["'Good morning! Excuse me, is the door locked?' Opening with ",
   (None, 'Com licença,'),
   " literally asks 'with permission', which is the go-to Brazilian polite opener before stepping in or "
   'asking a stranger a question.']),
 (1,
  None,
  ["'Good morning. No, lift the handle first and then push.' Jorge pairs ",
   (None, 'primeiro'),
   " for 'first' with ",
   (None, 'depois'),
   " for 'afterwards' to give clear step-by-step instructions."]),
 (2,
  None,
  ["'Oh, it opened! Thank you. I am Camila, the new receptionist.' Because Camila is a woman, she says ",
   (None, 'Obrigada.'),
   " ending in 'a', literally 'obliged', whereas a man says the 'o' version."]),
 (3,
  None,
  ["'I am Jorge. You arrived ten minutes early.' Brazilian speakers routinely put 'the' in front of first "
   'names, so Jorge introduces himself as ',
   (None, 'o Jorge.'),
   " just as Camila used 'the' before hers."]),
 (4,
  None,
  ["'On the first day I always walk fast. Where is the computer?' Asking ",
   (None, 'Onde fica'),
   " literally asks 'where stays', the natural way to ask where a fixed object or building is located."]),
 (5,
  None,
  ["'In the drawer. Here we use this big notebook and a pencil.' Everyday Brazilian speech loves ",
   (None, 'a gente usa'),
   " for 'we use'—literally 'the people uses', always paired with a singular 'he or she' form."]),
 (7,
  None,
  ["'Paper never loses the list when it rains.' A rainy Recife storm can knock out the power, and ",
   (None, 'quando chove.'),
   " needs no dummy 'it' in Portuguese: that single weather word already means 'it rains'."]),
 (11,
  None,
  ["'Rule number one: drink hot tea first and then answer the bell.' In Portuguese, descriptors like ",
   (None, 'quente'),
   " for 'hot' come right after the thing they describe, so Jorge says 'tea hot'."])]
