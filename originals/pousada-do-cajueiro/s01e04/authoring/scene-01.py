ID = 'pousada-do-cajueiro-s01e04-scene-01'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 4, 1
TITLE = 'Seis e quarenta e cinco  (Six Forty-Five)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'camila': 'Camila', 'jorge': 'Jorge'}

INTRO = ('It is six forty-five in the morning at the Cashew Tree Guesthouse in Recife. While the guests still sleep '
 'upstairs, Jorge sketches a quick street map on paper for Camila. Listen to the whole scene first.')
OPENER = "Let's trace Jorge's street directions one line at a time."
TRANSITION = "Now let's listen to the whole dawn briefing again from start to finish."
OUTRO = ('Left at the gate, straight to the bridge, past the green pharmacy, and left into the square—Camila is off '
 'on her dawn mission. See you next time.')
CLOSING = ('camila', 'Até logo!')

STORY = [('camila',
  'Bom dia, Jorge! Os chuveiros lá em cima já estão frios mesmo?',
  'Good morning, Jorge! Are the showers upstairs really cold already?'),
 ('jorge',
  'Frios como água de rio. Leve esta válvula quebrada no bolso.',
  'Cold as river water. Take this broken valve in your pocket.'),
 ('camila',
  'Peguei. Agora me explique como chegar à loja de ferragens.',
  'Got it. Now explain to me how to get to the hardware shop.'),
 ('jorge',
  'Vire à esquerda fora do portão e siga reto até a ponte de pedra.',
  'Turn left outside the gate and walk straight to the stone bridge.'),
 ('camila',
  'À esquerda no portão e reto até a ponte. Eu atravesso o rio?',
  'Left at the gate and straight to the bridge. Do I cross the river?'),
 ('jorge',
  'Sim, atravesse a ponte e passe pela farmácia verde à sua direita.',
  'Yes, cross the bridge and pass the green pharmacy on your right.'),
 ('camila',
  'Ponte, depois farmácia verde à direita. E depois disso?',
  'Bridge, then green pharmacy on the right. And after that?'),
 ('jorge',
  'Entre à esquerda na praça pequena. Procure uma porta azul de madeira.',
  'Turn left into the small square. Look for a blue wooden door.'),
 ('camila', 'A loja tem uma placa grande lá fora?', 'Does the shop have a big sign outside?'),
 ('jorge',
  'Só uma chave dourada pintada acima da porta. Mostre esta peça ao balconista.',
  'Only a golden key painted above the door. Show this part to the clerk.'),
 ('camila',
  'Vinte milímetros, latão, válvula do aquecedor, vou repetir o caminho inteiro!',
  'Twenty millimetres, brass, heater valve, I will repeat it the whole way!'),
 ('jorge',
  'Corra rápido, Camila. O quarto quatro acorda às sete e quinze!',
  'Run fast, Camila. Room four wakes up at seven fifteen!')]

WALK = [(0,
  None,
  ["'Good morning, Jorge! Are the showers upstairs really cold already?' Placing ",
   (None, 'mesmo?'),
   " at the end of a question turns 'same' into 'really?' or 'for real?'."]),
 (2,
  None,
  ["'Got it. Now explain to me how to get to the hardware shop.' Quick ",
   (None, 'Peguei.'),
   " literally 'I grabbed it', works for catching a ball, taking an object, or getting an idea."]),
 (3,
  None,
  ["'Turn left outside the gate and walk straight to the stone bridge.' Essential walking direction ",
   (None, 'siga reto'),
   " means 'keep going straight ahead'."]),
 (4,
  None,
  ["'Left at the gate and straight to the bridge. Do I cross the river?' Recife is famous for its rivers and "
   'bridges, and ',
   (None, 'Eu atravesso'),
   " means 'I cross' to the other bank."]),
 (5,
  None,
  ["'Yes, cross the bridge and pass the green pharmacy on your right.' Pair ",
   (None, 'à sua direita.'),
   " meaning 'on your right' with 'on the left' from earlier."]),
 (6,
  None,
  ["'Bridge, then green pharmacy on the right. And after that?' Asking ",
   (None, 'E depois disso?'),
   " literally 'and after of-that?', keeps any set of instructions moving."]),
 (8,
  None,
  ["'Does the shop have a big sign outside?' On storefronts and roads alike, ",
   (None, 'uma placa'),
   ' names a sign or plaque.']),
 (11,
  None,
  ["'Run fast, Camila. Room four wakes up at seven fifteen!' Notice ",
   (None, 'acorda'),
   " for waking up—no extra 'up' needed in Portuguese."])]
